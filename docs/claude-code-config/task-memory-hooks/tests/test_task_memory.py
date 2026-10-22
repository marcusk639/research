"""End-to-end tests for task_memory.py: run each hook as Claude Code would (JSON on stdin).

    python3 -m unittest discover -s tests -v      (from the bundle directory)
"""

import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

BUNDLE = Path(__file__).resolve().parent.parent
SCRIPT = BUNDLE / "hooks" / "task_memory.py"

CHECKPOINT = """Done.

<task-checkpoint status="complete" complexity="moderate">
## Goal
Add retry logic to the fetch client
## Summary
Wrapped fetch() in exponential backoff in src/net.py; 3 retries, jittered.
## Follow-up context
- Branch feat/retry, commit abc123; run `pytest tests/net` to verify.
## Learnings (project)
- The fetch client is also imported by scripts/sync.py.
## Learnings (global)
- urllib raises HTTPError before reading the body; catch it separately.
## Open items
- none
</task-checkpoint>"""


class Transcript:
    """Builds a Claude Code-style JSONL transcript."""

    def __init__(self, path):
        self.path = Path(path)
        self.path.write_text("")
        self.n = 0
        self.ctx = 30000

    def _write(self, entry):
        self.n += 1
        entry.setdefault("uuid", f"u{self.n}")
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def human(self, text):
        self._write({"type": "user", "origin": {"kind": "human"}, "message": {"role": "user", "content": text}})

    def peer(self, text):
        self._write({"type": "user", "isMeta": True, "origin": {"kind": "peer"}, "message": {"role": "user", "content": text}})

    def assistant(self, text="ok", tools=(), output=200, grow=1000):
        self.ctx += grow
        mid = f"msg{self.n}"
        usage = {"input_tokens": 2, "cache_creation_input_tokens": grow, "cache_read_input_tokens": self.ctx - grow,
                 "output_tokens": output}
        content = [{"type": "text", "text": text}]
        # Claude Code writes one entry per content block, repeating the usage.
        self._write({"type": "assistant", "message": {"id": mid, "role": "assistant", "content": content, "usage": usage}})
        for i, name in enumerate(tools):
            self._write({"type": "assistant", "message": {"id": mid, "role": "assistant", "usage": usage,
                         "content": [{"type": "tool_use", "id": f"{mid}-t{i}", "name": name, "input": {}}]}})
            self._write({"type": "user", "message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": f"{mid}-t{i}", "content": "x"}]}})


class HookTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.home = self.tmp / "home"
        self.home.mkdir()
        self.tm_home = self.tmp / "tm"
        self.project = self.tmp / "proj"
        self.project.mkdir()
        self.t = Transcript(self.tmp / "t.jsonl")
        self.env = {
            "PATH": os.environ["PATH"], "HOME": str(self.home), "TASK_MEMORY_HOME": str(self.tm_home),
        }

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_hook(self, cmd, payload=None, env=None, raw=None):
        stdin = raw if raw is not None else json.dumps({
            "session_id": "s1", "transcript_path": str(self.t.path), "cwd": str(self.project), **(payload or {})})
        p = subprocess.run([sys.executable, str(SCRIPT), cmd], input=stdin, capture_output=True, text=True,
                           env={**self.env, **(env or {})}, timeout=30)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertFalse((self.tm_home / "errors.log").exists(),
                         (self.tm_home / "errors.log").read_text() if (self.tm_home / "errors.log").exists() else "")
        return p.stdout

    def stop(self, last_message, **kw):
        out = self.run_hook("stop", {"last_assistant_message": last_message, "stop_hook_active": False}, **kw)
        return json.loads(out) if out else None

    def project_store(self):
        dirs = list((self.tm_home / "projects").iterdir())
        self.assertEqual(len(dirs), 1)
        return dirs[0]


class ClassificationTests(HookTestCase):
    def test_simple_question_is_not_nudged(self):
        self.t.human("what does this function return?")
        self.t.assistant("It returns a list.", tools=["Read"])
        self.t.assistant("It returns a list.")
        self.assertIsNone(self.stop("It returns a list."))

    def test_any_file_edit_makes_it_moderate(self):
        self.t.human("rename foo to bar")
        self.t.assistant("Renaming.", tools=["Edit"])
        self.t.assistant("Done.")
        out = self.stop("Done.")
        self.assertEqual(out["decision"], "block")
        self.assertIn("MODERATE", out["reason"])
        self.assertIn('<task-checkpoint status="complete" complexity="moderate">', out["reason"])

    def test_token_threshold_x(self):
        self.t.human("explain the architecture")
        self.t.assistant("Long explanation", output=9000)
        self.assertEqual(self.stop("Long explanation")["decision"], "block")

    def test_context_threshold_y(self):
        self.t.human("read these")
        self.t.assistant("reading", tools=["Read"], grow=500)
        self.t.assistant("summary", grow=25000)
        self.assertEqual(self.stop("summary")["decision"], "block")

    def test_subagent_makes_it_complex(self):
        self.t.human("research X")
        self.t.assistant("spawning", tools=["Agent"])
        self.t.assistant("report")
        self.assertIn("COMPLEX", self.stop("report")["reason"])

    def test_meta_and_peer_messages_are_not_instructions(self):
        self.t.human("do it")
        for _ in range(5):
            self.t.peer("<task-notification>done</task-notification>")
        self.t.assistant("x", tools=["Edit"])
        self.assertIn("1 instruction(s)", self.stop("x")["reason"])

    def test_subagent_stop_is_ignored(self):
        self.t.human("do it")
        self.t.assistant("x", tools=["Edit"])
        out = self.run_hook("stop", {"last_assistant_message": "x", "agent_id": "a1"})
        self.assertEqual(out, "")


class CheckpointFlowTests(HookTestCase):
    def test_full_cycle(self):
        (self.project / ".serena").mkdir()
        (self.project / ".serena" / "project.yml").write_text("project_name: p\n")
        (self.home / ".serena").mkdir()

        self.t.human("add retries")
        self.t.assistant("working", tools=["Read", "Edit", "Bash"])
        self.t.assistant("Done.")
        self.assertEqual(self.stop("Done.")["decision"], "block")
        # Same turn, Claude declines to checkpoint: no second nudge (no loop).
        self.assertIsNone(self.stop("Done."))

        self.t.assistant(CHECKPOINT)
        out = self.stop(CHECKPOINT)
        self.assertIn("task checkpoint saved", out["systemMessage"])
        self.assertIn("Serena", out["systemMessage"])

        store = self.project_store()
        latest = (store / "latest.md").read_text()
        self.assertIn("# Add retry logic to the fetch client", latest)
        self.assertIn("## Follow-up context", latest)
        self.assertEqual(len(list((store / "checkpoints").glob("*.md"))), 1)
        self.assertIn("**Add retry logic to the fetch client**", (store / "ledger.md").read_text())
        self.assertIn("scripts/sync.py", (store / "learnings.md").read_text())
        self.assertNotIn("HTTPError", (store / "learnings.md").read_text())  # global stays global
        self.assertIn("HTTPError", (self.tm_home / "global-learnings.md").read_text())

        month = time.strftime("%Y-%m")
        serena_proj = (self.project / ".serena" / "memories" / "learnings" / f"{month}.md").read_text()
        self.assertIn("scripts/sync.py", serena_proj)
        self.assertNotIn("HTTPError", serena_proj)
        serena_glob = (self.home / ".serena" / "memories" / "global" / "learnings" / f"{month}.md").read_text()
        self.assertIn("HTTPError", serena_glob)
        self.assertNotIn("scripts/sync.py", serena_glob)

        # Same block again (lagging transcript): not persisted twice.
        self.assertIsNone(self.stop(CHECKPOINT))
        self.assertEqual(len(list((store / "checkpoints").glob("*.md"))), 1)

        # The span restarted at the checkpoint: a trivial follow-up is simple.
        self.t.human("thanks, what branch was that?")
        self.t.assistant("feat/retry")
        self.assertIsNone(self.stop("feat/retry"))

    def test_no_serena_writes_without_serena(self):
        self.t.human("add retries")
        self.t.assistant("working", tools=["Edit"])
        self.stop("working")
        out = self.stop(CHECKPOINT)
        self.assertNotIn("Serena", out["systemMessage"])
        self.assertFalse((self.project / ".serena").exists())
        self.assertFalse((self.home / ".serena").exists())

    def test_in_progress_marker_suppresses_until_new_work(self):
        self.t.human("plan a migration")
        self.t.assistant("researching", tools=["Read", "Read", "Grep", "Glob"])
        self.t.assistant("Here is the plan. Approve?")
        self.assertEqual(self.stop("Here is the plan. Approve?")["decision"], "block")
        self.t.assistant('<task-checkpoint status="in-progress"/>')
        self.assertIsNone(self.stop('<task-checkpoint status="in-progress"/>'))
        # User replies, Claude only talks: no nudge.
        self.t.human("what about rollback?")
        self.t.assistant("Rollback is X.")
        self.assertIsNone(self.stop("Rollback is X."))
        # User approves, Claude does work: nudged again.
        self.t.human("approved, go")
        self.t.assistant("implementing", tools=["Edit"])
        self.assertEqual(self.stop("implemented")["decision"], "block")

    def test_literal_tag_mention_is_not_a_checkpoint(self):
        self.t.human("explain your hook")
        self.t.assistant("x", tools=["Edit"])
        out = self.stop("The hook looks for <task-checkpoint> blocks.")
        self.assertEqual(out["decision"], "block")


class ClaudeMemTests(HookTestCase):
    def test_saves_to_worker(self):
        received = []

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200 if self.path == "/api/health" else 404)
                self.end_headers()

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                received.append((self.path, body))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')

            def log_message(self, *a):
                pass

        server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            env = {"CLAUDE_MEM_WORKER_PORT": str(server.server_port)}
            self.t.human("add retries")
            self.t.assistant("working", tools=["Edit"])
            self.stop("working", env=env)
            out = self.stop(CHECKPOINT, env=env)
        finally:
            server.shutdown()
            server.server_close()
        self.assertIn("claude-mem", out["systemMessage"])
        path, body = received[0]
        self.assertEqual(path, "/api/memory/save")
        self.assertEqual(body["title"], "Task checkpoint: Add retry logic to the fetch client")
        self.assertIn("exponential backoff", body["text"])
        self.assertEqual(body["cwd"], str(self.project))
        self.assertEqual(body["metadata"]["kind"], "task-checkpoint")

    def test_worker_down_is_harmless(self):
        (self.home / ".claude-mem").mkdir()
        env = {"CLAUDE_MEM_WORKER_PORT": "1"}
        self.t.human("add retries")
        self.t.assistant("working", tools=["Edit"])
        self.stop("working", env=env)
        out = self.stop(CHECKPOINT, env=env)
        self.assertIn("(disk)", out["systemMessage"])


class CompactionTests(HookTestCase):
    def test_pre_compact_guidance(self):
        self.t.human("refactor")
        self.t.assistant("x", tools=["Edit"])
        out = self.run_hook("pre-compact", {"trigger": "auto", "custom_instructions": None})
        self.assertIn("NOT saved", out)
        self.stop("x")
        self.stop(CHECKPOINT)
        out = self.run_hook("pre-compact", {"trigger": "manual"})
        self.assertIn("verbatim", out)
        self.assertNotIn("NOT saved", out)

    def test_pre_compact_silent_when_nothing_to_say(self):
        self.t.human("hi")
        self.t.assistant("hello")
        self.assertEqual(self.run_hook("pre-compact", {"trigger": "auto"}), "")

    def test_post_compact_archives_summary(self):
        self.run_hook("post-compact", {"trigger": "auto", "compact_summary": "We did A then B."})
        files = list((self.project_store() / "compactions").glob("*-auto.md"))
        self.assertEqual(len(files), 1)
        self.assertIn("We did A then B.", files[0].read_text())

    def test_session_start_after_compact_injects_checkpoint(self):
        self.t.human("add retries")
        self.t.assistant("working", tools=["Edit"])
        self.stop("working")
        self.stop(CHECKPOINT)
        ctx = json.loads(self.run_hook("session-start", {"source": "compact"}))["hookSpecificOutput"]
        self.assertEqual(ctx["hookEventName"], "SessionStart")
        self.assertIn("### Latest task checkpoint", ctx["additionalContext"])
        self.assertIn("exponential backoff", ctx["additionalContext"])
        self.assertLessEqual(len(ctx["additionalContext"]), 9000)
        start = json.loads(self.run_hook("session-start", {"source": "startup"}))["hookSpecificOutput"]
        self.assertNotIn("### Latest task checkpoint", start["additionalContext"])
        self.assertIn("### Recent tasks", start["additionalContext"])

    def test_session_start_flags_unsaved_work_and_truncates(self):
        self.t.human("refactor")
        self.t.assistant("x", tools=["Edit"])
        self.stop("x")
        big = CHECKPOINT.replace("Wrapped fetch()", "Wrapped fetch() " + "z" * 20000)
        self.stop(big)
        self.run_hook("pre-compact", {"trigger": "auto"})
        ctx = json.loads(self.run_hook("session-start", {"source": "compact"}))["hookSpecificOutput"]["additionalContext"]
        self.assertLessEqual(len(ctx), 9000)
        self.assertIn("[truncated]", ctx)

    def test_session_start_empty_project_outputs_nothing(self):
        self.assertEqual(self.run_hook("session-start", {"source": "startup"}), "")

    def test_unsaved_note_after_compact(self):
        self.t.human("refactor")
        self.t.assistant("x", tools=["Edit"])
        (self.tm_home / "projects").mkdir(parents=True)
        self.run_hook("pre-compact", {"trigger": "auto"})
        # Give the project a ledger so there's something to inject.
        self.stop("x")
        self.stop(CHECKPOINT)
        self.t.human("next task")
        self.t.assistant("y", tools=["Edit"])
        self.run_hook("pre-compact", {"trigger": "auto"})
        ctx = json.loads(self.run_hook("session-start", {"source": "compact"}))["hookSpecificOutput"]["additionalContext"]
        self.assertIn("still in progress", ctx)


class RobustnessTests(HookTestCase):
    def test_garbage_stdin_fails_open(self):
        p = subprocess.run([sys.executable, str(SCRIPT), "stop"], input="{not json", capture_output=True,
                           text=True, env=self.env)
        self.assertEqual((p.returncode, p.stdout), (0, ""))
        self.assertTrue((self.tm_home / "errors.log").exists())

    def test_missing_transcript(self):
        out = self.run_hook("stop", {"transcript_path": str(self.tmp / "nope.jsonl"), "last_assistant_message": "hi"})
        self.assertEqual(out, "")

    def test_disable_env(self):
        self.t.human("x")
        self.t.assistant("x", tools=["Edit"])
        self.assertEqual(self.run_hook("stop", {"last_assistant_message": "x"}, env={"TASK_MEMORY_DISABLE": "1"}), "")

    def fake_tmux_env(self, foreground=True):
        """Fake `tmux` (logs send-keys, reports pane tty pts/9) and `ps` (a claude process on pts/9)."""
        bindir = self.tmp / "bin"
        bindir.mkdir()
        log = self.tmp / "tmux.log"
        (bindir / "tmux").write_text(
            "#!/bin/sh\n"
            'if [ "$1" = display-message ]; then echo /dev/pts/9; exit 0; fi\n'
            # capture-pane: the UI shows "Compacted" once Enter has been sent.
            f'if [ "$1" = capture-pane ]; then grep -q Enter "{log}" 2>/dev/null && echo Compacted || echo idle; exit 0; fi\n'
            f'echo "$@" >> "{log}"\n')
        tpgid = "100" if foreground else "555"
        (bindir / "ps").write_text(f'#!/bin/sh\necho "1 100 {tpgid} pts/9 claude"\n')
        for f in ("tmux", "ps"):
            (bindir / f).chmod(0o755)
        self.tm_home.mkdir()
        (self.tm_home / "config.json").write_text(json.dumps({"tmux_autocompact": True, "tmux_delay_seconds": 0}))
        env = {"PATH": f"{bindir}:{os.environ['PATH']}", "TMUX": "/tmp/tmux-0/default,1,0", "TMUX_PANE": "%7",
               "CLAUDE_CODE_ENTRYPOINT": "cli"}
        return env, log

    def run_task_to_checkpoint(self, env):
        self.t.human("add retries")
        self.t.assistant("working", tools=["Edit"])
        self.stop("working", env=env)
        return self.stop(CHECKPOINT, env=env)

    def test_tmux_autocompact(self):
        env, log = self.fake_tmux_env()
        out = self.run_task_to_checkpoint(env)
        self.assertIn("auto /compact queued in tmux", out["systemMessage"])
        for _ in range(50):
            if log.exists() and "Enter" in log.read_text():
                break
            time.sleep(0.1)
        time.sleep(1.5)  # a retry would have fired by now
        calls = log.read_text().splitlines()
        self.assertEqual(len(calls), 2, calls)  # typed once, no retry
        self.assertTrue(calls[0].startswith("send-keys -t %7 -l /compact "), calls)
        self.assertEqual(calls[1], "send-keys -t %7 Enter")

    def test_tmux_skipped_when_claude_is_not_the_foreground_job(self):
        env, log = self.fake_tmux_env(foreground=False)
        self.assertIn("safe to /compact", self.run_task_to_checkpoint(env)["systemMessage"])
        time.sleep(0.3)
        self.assertFalse(log.exists())

    def test_tmux_skipped_for_headless_runs(self):
        env, log = self.fake_tmux_env()
        env["CLAUDE_CODE_ENTRYPOINT"] = "sdk-cli"
        self.assertIn("safe to /compact", self.run_task_to_checkpoint(env)["systemMessage"])

    def test_tmux_off_by_default(self):
        env = {"TMUX": "x", "TMUX_PANE": "%1"}
        self.t.human("add retries")
        self.t.assistant("working", tools=["Edit"])
        self.stop("working", env=env)
        self.assertIn("safe to /compact", self.stop(CHECKPOINT, env=env)["systemMessage"])


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cfg = self.tmp / ".claude"
        self.cfg.mkdir()
        self.existing = {
            "model": "opus",
            "env": {"FOO": "1"},
            "hooks": {"Stop": [{"matcher": "", "hooks": [{"type": "command", "command": "~/.claude/other.sh"}]}]},
        }
        (self.cfg / "settings.json").write_text(json.dumps(self.existing))
        self.env = {**os.environ, "CLAUDE_CONFIG_DIR": str(self.cfg), "HOME": str(self.tmp)}

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def sh(self, script, *args):
        p = subprocess.run(["bash", str(BUNDLE / script), *args], capture_output=True, text=True, env=self.env)
        self.assertEqual(p.returncode, 0, p.stderr)
        return json.loads((self.cfg / "settings.json").read_text())

    def test_install_is_idempotent_and_uninstall_restores(self):
        self.sh("install.sh", "--tmux-autocompact")
        s = self.sh("install.sh", "--tmux-autocompact")
        self.assertEqual(s["model"], "opus")
        self.assertEqual(s["env"], {"FOO": "1", "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "60"})
        stop_cmds = [h["command"] for g in s["hooks"]["Stop"] for h in g["hooks"]]
        self.assertEqual(len(stop_cmds), 2)
        self.assertIn("~/.claude/other.sh", stop_cmds)
        for event in ("PreCompact", "PostCompact", "SessionStart"):
            self.assertEqual(len(s["hooks"][event]), 1, event)
        self.assertEqual(s["hooks"]["SessionStart"][0]["matcher"], "startup|resume|clear|compact")
        self.assertTrue((self.cfg / "hooks" / "task-memory" / "task_memory.py").is_file())
        self.assertTrue(json.loads((self.cfg / "task-memory" / "config.json").read_text())["tmux_autocompact"])

        s = self.sh("uninstall.sh")
        self.assertEqual(s, self.existing)
        self.assertFalse((self.cfg / "hooks" / "task-memory").exists())

    def test_existing_autocompact_env_is_respected(self):
        self.existing["env"]["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] = "80"
        (self.cfg / "settings.json").write_text(json.dumps(self.existing))
        s = self.sh("install.sh")
        self.assertEqual(s["env"]["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"], "80")
        s = self.sh("uninstall.sh")
        self.assertEqual(s["env"]["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"], "80")

    def test_installed_hook_runs_with_config_dir(self):
        self.sh("install.sh")
        cmd = json.loads((self.cfg / "settings.json").read_text())["hooks"]["SessionStart"][0]["hooks"][0]["command"]
        p = subprocess.run(["sh", "-c", cmd], input=json.dumps({"source": "startup", "cwd": str(self.tmp)}),
                           capture_output=True, text=True, env=self.env)
        self.assertEqual((p.returncode, p.stdout), (0, ""))
        self.assertFalse((self.cfg / "task-memory" / "errors.log").exists())


if __name__ == "__main__":
    unittest.main()
