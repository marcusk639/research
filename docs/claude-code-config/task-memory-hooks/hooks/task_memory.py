#!/usr/bin/env python3
"""task-memory: checkpoint discrete Claude Code tasks and survive compaction.

One script, four hook entry points (see README.md for the full design):

  stop           Stop hook. Classifies the work since the last checkpoint as
                 simple / moderate / complex. Non-simple work gets one nudge
                 asking Claude for a <task-checkpoint> block; when that block
                 appears it is persisted to disk, claude-mem and Serena, and
                 (opt-in) /compact is typed into the tmux pane.
  pre-compact    PreCompact hook. Prints compaction guidance (plain stdout is
                 merged into the compaction instructions by Claude Code).
  post-compact   PostCompact hook. Archives the compaction summary.
  session-start  SessionStart hook. Re-injects the latest checkpoint and the
                 recent task ledger after compact/clear (lighter on startup).

Standard library only. Every entry point fails open: any internal error is
logged to <TASK_MEMORY_HOME>/errors.log and the hook exits 0 with no output.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import time
import traceback
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

HOME = Path(
    os.environ.get("TASK_MEMORY_HOME")
    or Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "task-memory"
)

DEFAULTS = {
    # A span is SIMPLE only if every one of these holds (X = tokens, Y = context).
    "simple_max_tool_calls": 3,
    "simple_max_tokens": 8000,  # X: tokens Claude generated (output incl. thinking)
    "simple_max_context_growth": 20000,  # Y: context-window growth during the span
    # A non-simple span is COMPLEX if any of these holds; otherwise MODERATE.
    "complex_min_tool_calls": 20,
    "complex_min_tokens": 40000,
    "complex_min_context_growth": 60000,
    "complex_min_file_edits": 8,
    "complex_min_instructions": 4,
    "complex_min_subagents": 1,
    # Injection / integrations.
    "session_start_max_chars": 9000,
    "ledger_entries_on_start": 5,
    "claude_mem": True,
    "serena": True,
    "tmux_autocompact": False,
    "tmux_delay_seconds": 3,
    "state_retention_days": 14,
}

EDIT_TOOL_RE = re.compile(
    r"(^|__)(Edit|MultiEdit|Write|NotebookEdit|replace_symbol_body|replace_content|"
    r"insert_after_symbol|insert_before_symbol|rename_symbol|create_text_file|delete_lines|"
    r"replace_lines|insert_at_line)$"
)
SUBAGENT_TOOLS = {"Agent", "Task"}
NON_INSTRUCTION_PREFIXES = (
    "<command-",
    "<local-command",
    "<task-notification",
    "<system-reminder",
    "<bash-",
    "Caveat:",
)
CHECKPOINT_RE = re.compile(r"<task-checkpoint\b([^>]*?)>(.*?)</task-checkpoint>", re.S)
CHECKPOINT_SELF_CLOSING_RE = re.compile(r"<task-checkpoint\b([^>]*?)/>")
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
SECTION_NAMES = (
    "Goal",
    "Summary",
    "Follow-up context",
    "Learnings (project)",
    "Learnings (global)",
    "Open items",
)


# ---------------------------------------------------------------- utilities


def load_config():
    cfg = dict(DEFAULTS)
    try:
        cfg.update(json.loads((HOME / "config.json").read_text()))
    except (OSError, ValueError):
        pass
    if os.environ.get("TASK_MEMORY_TMUX_AUTOCOMPACT") is not None:
        cfg["tmux_autocompact"] = os.environ["TASK_MEMORY_TMUX_AUTOCOMPACT"] == "1"
    return cfg


def log_error(where):
    try:
        HOME.mkdir(parents=True, exist_ok=True)
        with open(HOME / "errors.log", "a") as f:
            f.write(f"--- {datetime.now().isoformat()} [{where}]\n{traceback.format_exc()}\n")
    except OSError:
        pass


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_text(text)
    os.replace(tmp, path)


def append(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(text)


def slugify(text, limit=50):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:limit].strip("-") or "task"


def project_root(cwd):
    try:
        out = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=3,
        )
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        pass
    return Path(cwd)


def project_dir(cwd):
    root = project_root(cwd)
    key = re.sub(r"[^A-Za-z0-9]+", "-", str(root)).strip("-") or "root"
    return root, HOME / "projects" / key


def state_path(inp):
    """Per-conversation state, keyed by transcript file (session ids can be inherited by nested runs)."""
    key = inp.get("transcript_path") or inp.get("session_id") or "unknown"
    return HOME / "state" / f"{hashlib.sha256(key.encode()).hexdigest()[:24]}.json"


def load_state(inp):
    try:
        return json.loads(state_path(inp).read_text())
    except (OSError, ValueError):
        return {}


def save_state(inp, state):
    atomic_write(state_path(inp), json.dumps(state))


# ------------------------------------------------------- transcript analysis


def _text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(
            b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"
        )
    return ""


def is_tool_result(entry):
    content = (entry.get("message") or {}).get("content")
    return isinstance(content, list) and any(
        isinstance(b, dict) and b.get("type") == "tool_result" for b in content
    )


def is_human_instruction(entry):
    """True for a prompt the user typed (not tool results, hook/system/peer/slash-command input)."""
    if entry.get("type") != "user" or entry.get("isSidechain"):
        return False
    if entry.get("isMeta") or entry.get("isCompactSummary") or is_tool_result(entry):
        return False
    text = _text_of((entry.get("message") or {}).get("content")).lstrip()
    if not text or text.startswith(NON_INSTRUCTION_PREFIXES):
        return False
    origin = entry.get("origin")
    if isinstance(origin, dict) and origin.get("kind"):
        return origin["kind"] == "human"
    return True


def context_size(usage):
    return sum(
        int(usage.get(k) or 0)
        for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
    )


def analyze(transcript_path, offset=0, baseline_ctx=None):
    """Measure the span of the transcript that starts at byte `offset`.

    tokens  = tokens Claude generated (output, including thinking), per unique API
              message. Input-side counts are not used: cache writes after a cache
              expiry or on a session's first request would flag trivial turns.
    growth  = sum of positive steps in context size between consecutive API
              requests (drops from compaction are ignored), starting from
              `baseline_ctx` when known.
    """
    s = {
        "instructions": 0, "tool_calls": 0, "file_edits": 0, "subagents": 0,
        "tokens": 0, "growth": 0, "last_ctx": baseline_ctx, "turn_key": None,
        "end_offset": offset, "last_assistant_text": "",
    }
    path = Path(transcript_path or "")
    if not transcript_path or not path.is_file():
        return s
    size = path.stat().st_size
    if offset > size:  # transcript was rewritten; start over
        offset = 0
    seen_msgs, seen_ctx, seen_tools = {}, {}, set()
    prev_ctx = baseline_ctx
    end = offset
    with open(path, "rb") as f:
        f.seek(offset)
        for raw in f:
            if not raw.endswith(b"\n"):
                break  # line still being written; leave it for the next span
            end += len(raw)
            try:
                entry = json.loads(raw)
            except ValueError:
                continue
            etype = entry.get("type")
            if etype == "user" and not entry.get("isSidechain") and not is_tool_result(entry):
                s["turn_key"] = entry.get("uuid") or s["turn_key"]
                if is_human_instruction(entry):
                    s["instructions"] += 1
            elif etype == "assistant" and not entry.get("isSidechain"):
                msg = entry.get("message") or {}
                for block in msg.get("content") or []:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") == "tool_use":
                        tid = block.get("id") or id(block)
                        if tid in seen_tools:
                            continue
                        seen_tools.add(tid)
                        name = block.get("name") or ""
                        s["tool_calls"] += 1
                        if EDIT_TOOL_RE.search(name):
                            s["file_edits"] += 1
                        if name in SUBAGENT_TOOLS:
                            s["subagents"] += 1
                    elif block.get("type") == "text" and block.get("text"):
                        s["last_assistant_text"] = block["text"]
                mid = msg.get("id")
                usage = msg.get("usage") or {}
                if mid and usage:
                    out_tokens = int(usage.get("output_tokens") or 0)
                    s["tokens"] += max(0, out_tokens - seen_msgs.get(mid, 0))
                    seen_msgs[mid] = max(out_tokens, seen_msgs.get(mid, 0))
                    if seen_ctx.get(mid):
                        continue
                    seen_ctx[mid] = True
                    ctx = context_size(usage)
                    if prev_ctx is not None and ctx > prev_ctx:
                        s["growth"] += ctx - prev_ctx
                    prev_ctx = ctx
    s["end_offset"] = end
    s["last_ctx"] = prev_ctx
    return s


def classify(s, cfg):
    if (
        s["tool_calls"] <= cfg["simple_max_tool_calls"]
        and s["file_edits"] == 0
        and s["subagents"] == 0
        and s["tokens"] < cfg["simple_max_tokens"]
        and s["growth"] < cfg["simple_max_context_growth"]
    ):
        return "simple"
    if (
        s["tool_calls"] >= cfg["complex_min_tool_calls"]
        or s["tokens"] >= cfg["complex_min_tokens"]
        or s["growth"] >= cfg["complex_min_context_growth"]
        or s["file_edits"] >= cfg["complex_min_file_edits"]
        or s["instructions"] >= cfg["complex_min_instructions"]
        or s["subagents"] >= cfg["complex_min_subagents"]
    ):
        return "complex"
    return "moderate"


def stats_line(s):
    return (
        f"{s['instructions']} instruction(s), {s['tool_calls']} tool calls, "
        f"{s['file_edits']} file edits, {s['subagents']} subagents, "
        f"~{s['tokens']:,} tokens generated, +{s['growth']:,} context"
    )


# ------------------------------------------------------------- checkpoints


def parse_checkpoint(text):
    """Return {'status','complexity','sections','raw'} for the last checkpoint block, or None."""
    if not text or "<task-checkpoint" not in text:
        return None
    full = list(CHECKPOINT_RE.finditer(text))
    if full:
        m = full[-1]
        attrs = dict(ATTR_RE.findall(m.group(1)))
        body = m.group(2).strip()
    else:
        closing = list(CHECKPOINT_SELF_CLOSING_RE.finditer(text))
        if not closing:
            return None
        attrs = dict(ATTR_RE.findall(closing[-1].group(1)))
        body = ""
    status = attrs.get("status", "complete").strip().lower()
    sections, current = {}, None
    for line in body.splitlines():
        header = re.match(r"^\s*#{2,3}\s+(.+?)\s*$", line)
        if header:
            current = header.group(1).strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    sections = {k: "\n".join(v).strip() for k, v in sections.items()}
    if status != "in-progress" and not sections.get("Summary"):
        return None  # a literal mention of the tag, not a real checkpoint
    return {
        "status": status,
        "complexity": attrs.get("complexity", "").strip().lower(),
        "sections": sections,
        "raw": body,
    }


def bullets(section_text):
    out = []
    for line in (section_text or "").splitlines():
        item = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line).strip()
        if item and item.lower().rstrip(".") not in {"none", "n/a", "na", "-"}:
            out.append(item)
    return out


def nudge_text(level, s):
    words = 250 if level == "moderate" else 600
    return f"""[task-memory] The work since the last checkpoint is a {level.upper()} task ({stats_line(s)}).

If the goal of this task is now complete, reply with ONLY the block below: no tool calls, and don't repeat your answer. The hook saves it to disk, claude-mem and Serena, so later tasks and post-compaction context can use it.

<task-checkpoint status="complete" complexity="{level}">
## Goal
One line: the goal the user's instructions were working toward.
## Summary
What was done and the outcome: files created or changed, key decisions and why.
## Follow-up context
Facts a follow-up task needs without this conversation: paths, branch/commit, IDs, commands, config values, current state.
## Learnings (project)
- Gotchas, failed approaches, conventions specific to THIS project (or "- none").
## Learnings (global)
- Lessons that hold across projects: tools, APIs, workflows (or "- none").
## Open items
- Unfinished work, pending decisions, known risks (or "- none").
</task-checkpoint>

Keep it under {words} words, concrete, no filler.
If the task is NOT finished (you are waiting on the user for an answer or approval, or on background work), reply with only: <task-checkpoint status="in-progress"/>"""


def render_checkpoint(cp, meta):
    sec = cp["sections"]
    lines = [
        f"# {meta['title']}",
        "",
        f"- **When:** {meta['when']}",
        f"- **Project:** {meta['root']}",
        f"- **Session:** {meta['session_id']}",
        f"- **Complexity:** {meta['level']}",
        f"- **Span:** {meta['stats']}",
        "",
    ]
    for name in SECTION_NAMES:
        if sec.get(name):
            lines += [f"## {name}", sec[name], ""]
    for name, text in sec.items():  # keep any extra sections Claude added
        if name not in SECTION_NAMES and text:
            lines += [f"## {name}", text, ""]
    return "\n".join(lines).rstrip() + "\n"


def find_serena_root(cwd, root):
    """Nearest directory from cwd up to the project root that has .serena/project.yml."""
    cur = Path(cwd).resolve()
    stop = Path(root).resolve()
    while True:
        if (cur / ".serena" / "project.yml").is_file():
            return cur
        if cur == stop or cur.parent == cur:
            return None
        cur = cur.parent


def serena_home():
    return Path(os.environ.get("SERENA_HOME") or Path.home() / ".serena")


def learnings_entry(items, meta):
    head = f"\n### {meta['when']} · {meta['title']}\n_Source: task-memory checkpoint, project {meta['root']}_\n"
    return head + "".join(f"- {i}\n" for i in items)


def claude_mem_ports():
    ports = []
    env_port = os.environ.get("CLAUDE_MEM_WORKER_PORT")
    if env_port:
        ports.append(env_port)
    data_dir = Path(os.environ.get("CLAUDE_MEM_DATA_DIR") or Path.home() / ".claude-mem")
    try:
        settings = json.loads((data_dir / "settings.json").read_text())
        if settings.get("CLAUDE_MEM_WORKER_PORT"):
            ports.append(str(settings["CLAUDE_MEM_WORKER_PORT"]))
    except (OSError, ValueError, AttributeError):
        pass
    if not ports and not data_dir.exists():
        return []  # claude-mem isn't installed
    uid = os.getuid() if hasattr(os, "getuid") else 0
    ports += [str(37700 + uid % 100), "37777"]
    return list(dict.fromkeys(ports))


def claude_mem_save(title, text, cwd, metadata):
    """POST to the claude-mem worker. Returns 'saved', 'unavailable' or an error string."""
    for port in claude_mem_ports():
        base = f"http://127.0.0.1:{port}"
        try:
            with urllib.request.urlopen(f"{base}/api/health", timeout=0.5) as r:
                if r.status != 200:
                    continue
        except (OSError, ValueError):
            continue
        for body in (
            {"title": title, "text": text[:8000], "cwd": cwd, "metadata": metadata},
            {"title": title, "text": text[:8000], "cwd": cwd},  # older/stricter schemas
        ):
            req = urllib.request.Request(
                f"{base}/api/memory/save",
                data=json.dumps(body).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=4) as r:
                    if 200 <= r.status < 300:
                        return "saved"
            except urllib.error.HTTPError as e:
                if e.code != 400:
                    return f"error HTTP {e.code}"
            except (OSError, ValueError) as e:
                return f"error {e}"
        return "error HTTP 400"
    return "unavailable"


def persist_checkpoint(cp, inp, s, cfg):
    cwd = inp.get("cwd") or os.getcwd()
    root, pdir = project_dir(cwd)
    sec = cp["sections"]
    level = cp["complexity"] if cp["complexity"] in ("moderate", "complex") else classify(s, cfg)
    goal = (sec.get("Goal") or sec.get("Summary") or "Task").strip().splitlines()[0]
    title = re.sub(r"^[-*#\s]+", "", goal)[:100] or "Task"
    now = datetime.now()
    meta = {
        "title": title,
        "when": now.strftime("%Y-%m-%d %H:%M"),
        "root": str(root),
        "session_id": inp.get("session_id", ""),
        "level": level,
        "stats": stats_line(s),
    }
    md = render_checkpoint(cp, meta)
    name = f"{now.strftime('%Y%m%d-%H%M%S')}-{slugify(title)}.md"
    atomic_write(pdir / "checkpoints" / name, md)
    atomic_write(pdir / "latest.md", md)
    summary_line = bullets(sec.get("Summary"))[0][:160] if bullets(sec.get("Summary")) else ""
    append(pdir / "ledger.md", f"- {meta['when']} · {level} · **{title}** — {summary_line} → checkpoints/{name}\n")
    results = {"file": str(pdir / "checkpoints" / name)}

    project_items = bullets(sec.get("Learnings (project)"))
    global_items = bullets(sec.get("Learnings (global)"))
    month = now.strftime("%Y-%m")
    if project_items:
        append(pdir / "learnings.md", learnings_entry(project_items, meta))
    if global_items:
        append(HOME / "global-learnings.md", learnings_entry(global_items, meta))

    if cfg["serena"]:
        sroot = find_serena_root(cwd, root)
        if sroot and project_items:
            append(sroot / ".serena" / "memories" / "learnings" / f"{month}.md", learnings_entry(project_items, meta))
            results["serena_project"] = f"learnings/{month}"
        if serena_home().is_dir() and global_items:
            append(serena_home() / "memories" / "global" / "learnings" / f"{month}.md", learnings_entry(global_items, meta))
            results["serena_global"] = f"global/learnings/{month}"

    if cfg["claude_mem"]:
        results["claude_mem"] = claude_mem_save(
            f"Task checkpoint: {title}",
            md,
            cwd,
            {"source": "task-memory", "kind": "task-checkpoint", "complexity": level,
             "session_id": meta["session_id"]},
        )
    return level, results


def claude_owns_pane(pane):
    """True only if the Claude process running this hook is the foreground job of `pane`.

    Guards against typing into the pane from a headless `claude -p` (a script, a
    Bash tool call) that merely inherited TMUX/TMUX_PANE.
    """
    if os.environ.get("CLAUDE_CODE_ENTRYPOINT", "").startswith("sdk"):
        return False
    try:
        pane_tty = subprocess.run(
            ["tmux", "display-message", "-p", "-t", pane, "#{pane_tty}"],
            capture_output=True, text=True, timeout=2,
        ).stdout.strip()
        pid = os.getppid()
        for _ in range(8):  # walk up to the nearest claude process
            fields = subprocess.run(
                ["ps", "-o", "ppid=,pgid=,tpgid=,tty=,comm=", "-p", str(pid)],
                capture_output=True, text=True, timeout=2,
            ).stdout.split(None, 4)
            if len(fields) < 5:
                return False
            ppid, pgid, tpgid, tty, comm = fields
            if "claude" in os.path.basename(comm.strip()).lower():
                return (
                    pgid == tpgid
                    and bool(pane_tty)
                    and tty.replace("/dev/", "") == pane_tty.replace("/dev/", "")
                )
            pid = int(ppid)
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return False


# $1 delay, $2 pane, $3 text. Waits for the pane to stop redrawing (Claude's UI can
# reset the input box just after a turn ends), types the command, then checks that a
# compaction started; retries once if the keystrokes were swallowed.
TMUX_SEND_SCRIPT = r'''
sleep "$1"
compactions() { tmux capture-pane -p -t "$2" -S - 2>/dev/null | grep -c -E "Compact(ing|ed)"; }
for attempt in 1 2; do
  prev=""; i=0
  while [ $i -lt 10 ]; do
    cur=$(tmux capture-pane -p -t "$2" 2>/dev/null) || exit 0
    [ "$cur" = "$prev" ] && break
    prev=$cur; i=$((i + 1)); sleep 1
  done
  before=$(compactions)
  [ $attempt -gt 1 ] && tmux send-keys -t "$2" C-u
  tmux send-keys -t "$2" -l "$3" && tmux send-keys -t "$2" Enter || exit 0
  i=0
  while [ $i -lt 8 ]; do
    sleep 1
    [ "$(compactions)" -gt "$before" ] && exit 0
    i=$((i + 1))
  done
done
'''


def schedule_tmux_compact(cfg):
    pane = os.environ.get("TMUX_PANE")
    if not (cfg["tmux_autocompact"] and os.environ.get("TMUX") and pane):
        return False
    if not claude_owns_pane(pane):
        return False
    instructions = (
        "/compact Keep the most recent <task-checkpoint> block verbatim; "
        "summarize earlier work briefly; keep any unfinished work in full detail."
    )
    delay = max(0, int(cfg["tmux_delay_seconds"]))
    subprocess.Popen(
        ["sh", "-c", TMUX_SEND_SCRIPT, "sh", str(delay), pane, instructions],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    return True


# ------------------------------------------------------------- entry points


def cmd_stop(inp, cfg):
    if inp.get("agent_id"):  # a subagent's stop; only the main thread checkpoints
        return None
    state = load_state(inp)
    s = analyze(inp.get("transcript_path"), state.get("offset", 0), state.get("baseline_ctx"))
    text = inp.get("last_assistant_message") or s["last_assistant_text"]
    cp = parse_checkpoint(text)

    if cp and cp["status"] == "in-progress":
        state["in_progress"] = True
        save_state(inp, state)
        return None

    if cp:
        digest = hashlib.sha256(cp["raw"].encode()).hexdigest()
        if digest == state.get("last_digest"):
            return None  # same block seen again (e.g. lagging transcript fallback)
        level, results = persist_checkpoint(cp, inp, s, cfg)
        save_state(inp, {
            "offset": s["end_offset"],
            "baseline_ctx": s["last_ctx"],
            "last_checkpoint": results["file"],
            "last_digest": digest,
        })
        tmux = schedule_tmux_compact(cfg)
        saved = ["disk"]
        if results.get("claude_mem") == "saved":
            saved.append("claude-mem")
        if results.get("serena_project") or results.get("serena_global"):
            saved.append("Serena")
        hint = "auto /compact queued in tmux" if tmux else "safe to /compact or /clear now"
        return {"systemMessage": f"📌 {level} task checkpoint saved ({', '.join(saved)}) → {results['file']} — {hint}."}

    level = classify(s, cfg)
    if level == "simple":
        return None
    if state.get("nudged_turn") == s["turn_key"]:
        return None  # one nudge per turn; Claude declined, don't loop
    if state.get("in_progress") and s["tool_calls"] <= state.get("tools_at_nudge", 0):
        return None  # still waiting on the user and no new work since the last nudge
    state.update({"nudged_turn": s["turn_key"], "tools_at_nudge": s["tool_calls"], "in_progress": False})
    save_state(inp, state)
    return {"decision": "block", "reason": nudge_text(level, s)}


def cmd_pre_compact(inp, cfg):
    state = load_state(inp)
    s = analyze(inp.get("transcript_path"), state.get("offset", 0), state.get("baseline_ctx"))
    unsaved = classify(s, cfg) != "simple"
    state["precompact_unsaved"] = unsaved
    save_state(inp, state)
    lines = ["Task-memory guidance:"]
    if state.get("last_checkpoint"):
        lines.append("- Keep the most recent <task-checkpoint> block verbatim.")
    if unsaved:
        lines.append(
            "- Work since the last checkpoint is NOT saved anywhere else: keep its goal, files "
            "touched, decisions, commands, and open items in full detail."
        )
    if len(lines) == 1:
        return None
    return "\n".join(lines)


def cmd_post_compact(inp, cfg):
    summary = (inp.get("compact_summary") or "").strip()
    if not summary:
        return None
    cwd = inp.get("cwd") or os.getcwd()
    root, pdir = project_dir(cwd)
    now = datetime.now()
    trigger = inp.get("trigger") or "unknown"
    md = (
        f"# Compaction summary ({trigger})\n\n- **When:** {now.strftime('%Y-%m-%d %H:%M')}\n"
        f"- **Project:** {root}\n- **Session:** {inp.get('session_id', '')}\n\n{summary}\n"
    )
    atomic_write(pdir / "compactions" / f"{now.strftime('%Y%m%d-%H%M%S')}-{trigger}.md", md)
    if cfg["claude_mem"]:
        claude_mem_save(
            f"Compaction summary ({trigger})", md, cwd,
            {"source": "task-memory", "kind": "compaction-summary", "session_id": inp.get("session_id", "")},
        )
    return None


def cmd_session_start(inp, cfg):
    source = inp.get("source") or "startup"
    cwd = inp.get("cwd") or os.getcwd()
    root, pdir = project_dir(cwd)
    state = load_state(inp)
    if source == "clear":  # nothing before the clear is in context any more
        tp = Path(inp.get("transcript_path") or "")
        state.update({"offset": tp.stat().st_size if tp.is_file() else 0, "baseline_ctx": None})
        save_state(inp, state)
    if source == "startup":
        cleanup_state(cfg)

    parts = []
    latest = pdir / "latest.md"
    if source in ("compact", "clear") and latest.is_file():
        parts.append("### Latest task checkpoint\n" + latest.read_text().strip())
    ledger = pdir / "ledger.md"
    if ledger.is_file():
        entries = [l for l in ledger.read_text().splitlines() if l.startswith("- ")]
        if entries:
            parts.append("### Recent tasks (newest last)\n" + "\n".join(entries[-cfg["ledger_entries_on_start"]:]))
    if source == "compact" and state.get("precompact_unsaved"):
        parts.append(
            "### Note\nA task was still in progress (not yet checkpointed) when compaction ran. "
            "Continue it; the Stop hook will ask for a checkpoint when it is done."
        )
    if not parts:
        return None

    pointers = [f"Full checkpoints: {pdir}/checkpoints/ · project learnings: {pdir}/learnings.md · "
                f"cross-project learnings: {HOME}/global-learnings.md"]
    if cfg["claude_mem"] and claude_mem_ports():
        pointers.append("Older work: query claude-mem's search tool (then timeline / get_observations).")
    if cfg["serena"] and find_serena_root(cwd, root):
        pointers.append("Serena memories: `learnings/<YYYY-MM>` (project) and `global/learnings/<YYYY-MM>` (global) via list_memories/read_memory.")
    header = f"## Task memory (task-memory hook, session {source})\n"
    footer = "\n\n" + "\n".join(pointers)
    budget = cfg["session_start_max_chars"] - len(header) - len(footer)
    body = "\n\n".join(parts)
    if len(body) > budget:
        body = body[: max(0, budget - 20)].rstrip() + "\n…[truncated]"
    return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": header + body + footer}}


def cleanup_state(cfg):
    cutoff = time.time() - cfg["state_retention_days"] * 86400
    for p in (HOME / "state").glob("*.json"):
        try:
            if p.stat().st_mtime < cutoff:
                p.unlink()
        except OSError:
            pass


COMMANDS = {
    "stop": cmd_stop,
    "pre-compact": cmd_pre_compact,
    "post-compact": cmd_post_compact,
    "session-start": cmd_session_start,
}


def main(argv):
    cmd = argv[1] if len(argv) > 1 else ""
    if cmd not in COMMANDS or os.environ.get("TASK_MEMORY_DISABLE") == "1":
        return 0
    try:
        raw = sys.stdin.read()
        inp = json.loads(raw) if raw.strip() else {}
        out = COMMANDS[cmd](inp, load_config())
    except Exception:  # fail open: never break the session
        log_error(cmd)
        return 0
    if isinstance(out, dict):
        sys.stdout.write(json.dumps(out))
    elif isinstance(out, str):
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
