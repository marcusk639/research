# task-memory hooks

User-level Claude Code hooks that save a **checkpoint** of each **moderate or complex
task** when it finishes. A checkpoint is a summary, the context follow-up tasks need, and
learnings. It goes to disk, **claude-mem** and **Serena**, and returns to context after
compaction. Compaction then happens automatically: at a lowered auto-compact threshold
or, opt-in, by typing `/compact` into your tmux pane. Simple tasks are left alone.

Tested on Claude Code 2.1.307 with Python 3.13 (standard library only).

## What counts as a task

A **task** is one or more instructions working toward one goal. The hooks measure it as a
**span**: everything since the last saved checkpoint (or since the session started).
Each time Claude stops, the span is classified:

| Class | Definition | What happens |
|---|---|---|
| **Simple** | One trivial goal. **All** hold: ≤ 3 tool calls · 0 file edits · 0 subagents · < **X** tokens generated · < **Y** context growth | Nothing. No checkpoint, no memory saves, no compaction, even if Claude writes a block anyway. |
| **Moderate** | Anything beyond simple that isn't complex | Checkpoint (≤ 250 words) + memory saves + compaction |
| **Complex** | **Any** of: ≥ 20 tool calls · ≥ 8 file edits · ≥ 1 subagent · ≥ 4 instructions · ≥ 40k tokens generated · ≥ 60k context growth | Checkpoint (≤ 600 words) + memory saves + compaction |

**X = 8,000 tokens generated.** This counts the output tokens Claude produced during the
span, including thinking, which measures how much reasoning and writing the task took.
- Input-side counts are deliberately excluded.
- A session's first request writes the whole system prompt to cache (about 27k tokens),
  and so does any request after the cache expires. Counting those would make a one-line
  question look expensive.

**Y = 20,000 tokens of context growth.** This is how much the context window grew during
the span: the sum of the increases in prompt size between consecutive API requests.
- File reads, tool output and long answers all add to it.
- A drop in size caused by compaction is ignored.
- 20k is about 10% of a 200k window.

Notes:
- **File edits** are calls to `Edit`, `MultiEdit`, `Write`, `NotebookEdit`, or Serena's
  symbol and line editing tools.
- **Instructions** count only prompts you typed. Tool results, hook output, subagent
  reports, task notifications and slash commands don't count.
- Trivial questions stay in the span until the next checkpoint, so "4 quick questions,
  then an edit" counts as one complex task. The class only sets the word budget.

Every threshold can be changed in `~/.claude/task-memory/config.json`.

## How checkpoints get written

**Inline mode (default).** Claude writes the checkpoint itself, with the full context:

1. **Session start.** The hook injects a short protocol: when a task that took real work
   is finished, Claude adds a `<task-checkpoint>` block **after** its normal answer. When
   it stops to wait for you (a question, plan approval), it adds
   `<task-checkpoint status="in-progress"/>` instead.
2. **Stop.** If the final reply has a block, the hook saves it. No extra turn is needed,
   and the answer stays first.
3. **Fallback.** If Claude forgot, the hook asks once. It uses Stop
   `additionalContext`, which shows as "Stop hook feedback", not as an error. Claude
   then replies with just the block.

On real runs, Opus 5.5 followed the protocol without being asked, and Haiku 5.5 needed
the fallback.

**Background mode (opt-in, `--background-checkpoints`).** At Stop, the hook starts a
detached `claude -p --model haiku` call that reads a condensed log of the span and writes
the checkpoint.
- **Pros:** the main model takes no extra turn, nothing is added to your chat, and no
  protocol is injected.
- **Cons:** an extra Haiku call per task. It also sees only a condensed log, so its
  summaries are thinner and it can't record learnings it wasn't told about.
- **How it runs:** with no tools, no MCP servers, no user or plugin settings (so no
  hooks), no session saving, and `TASK_MEMORY_DISABLE=1`.
- **Requirements:** `claude` must be on `PATH` (or `CLAUDE_CODE_EXECPATH` set). Login
  must come from OAuth or the environment, because an `apiKeyHelper` in user settings
  isn't loaded.

### The checkpoint block

```
<task-checkpoint status="complete" complexity="moderate|complex">
## Goal               one line
## Summary            what was done, files changed, key decisions and why
## Follow-up context  paths, branch/commit, IDs, commands, config values, current state
## Learnings (project) - project-specific gotchas and conventions   → project-only stores
## Learnings (global)  - lessons that hold across projects          → global stores
## Open items          - unfinished work, pending decisions, risks
</task-checkpoint>
```

The parser is tolerant:
- headers in any capitalisation, with `##`, `###` or `**bold**` and an optional colon;
- `status="completed"` or `"done"`;
- numbered or `*` bullets;
- list items that wrap onto several lines.

A block with no Summary gets one "please fix" request, then a warning. It is never saved
silently with half its content.

## Where checkpoints are saved

| Destination | What | Condition |
|---|---|---|
| `~/.claude/task-memory/projects/<project>/checkpoints/<ts>-<slug>.md`, `latest.md`, `ledger.md` | The full checkpoint and a one-line ledger entry | Always |
| `<project>/learnings.md` · `~/.claude/task-memory/global-learnings.md` | Project or global learnings, deduplicated | Always |
| `<repo>/.serena/memories/learnings/<YYYY-MM>.md` | Project learnings only | If the repo has `.serena/project.yml` |
| `~/.serena/memories/global/learnings/<YYYY-MM>.md` (`$SERENA_HOME`) | Global learnings only | If `~/.serena` exists |
| claude-mem `POST /api/memory/save` (`metadata.kind = task-checkpoint`) | The full checkpoint | If the worker is running |

Project learnings never go to the global stores, and global learnings never go to the
project stores.

## What comes back into context (SessionStart)

| Session start | Injected (capped at 9,000 characters) |
|---|---|
| `startup` | The protocol, the 8 latest project and global learnings, the 5 latest ledger entries, and pointers to the full files, claude-mem search and Serena memories |
| `compact` | The above, plus **this session's own** latest checkpoint and a note if a task was still in progress |
| `clear` | The above, plus the project's latest checkpoint, labelled "may be from another session" |
| `resume` | Nothing: the resumed transcript already has it |

- **Treated as data.** Injected notes are labelled as data written by earlier turns, not
  instructions. That keeps a web page Claude once read from planting instructions in
  future sessions through a checkpoint.
- **No sensitive details.** The protocol and every request tell Claude to leave secrets,
  credentials and personal, medical or financial details out of checkpoints.
- **No duplication with claude-mem.** Its own timeline injection keeps running and isn't
  repeated here.

## Compaction

Claude Code (as of 2.1.307) gives hooks no way to start `/compact`, and Claude can't run
it itself. So everything worth keeping is saved first; after that, compacting (or even
`/clear`) loses nothing. Compaction then comes from:

- **Earlier auto-compaction.** `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60` makes auto-compaction
  trigger at 60% of the window instead of near the limit.
- **tmux auto-`/compact` (opt-in, `--tmux-autocompact`).** After each saved checkpoint, a
  background process types `/compact <keep the checkpoint>` into your pane.
  - **Only from the interactive session.** It acts only when the Claude process running
    the hook is the foreground job of that pane, checked with `ps` and `tmux`. Native
    and npm installs are both recognised. Headless runs never type into a pane.
  - **Waits, then confirms.** It waits until the pane stops redrawing, then checks that a
    compaction started, and retries once (clearing the input first) if it didn't.
  - **Says why if it doesn't run.** The "📌 checkpoint saved" line gives the reason.
  - **Caveat:** if you start typing within about 3 seconds of a checkpoint, the command
    can mix with your text.
- **Idle compaction.** Claude Code can compact a long conversation while the session is
  idle. Anthropic controls whether it is on, and the `idleCompaction` setting can only
  turn it **off**. Treat it as a bonus.
- **Manual.** Run `/compact` or `/clear` when you see the "📌 checkpoint saved" line.

Around a compaction:
- **PreCompact** tells the summarizer to keep the latest checkpoint word for word and to
  keep un-checkpointed work in full. It relies on plain PreCompact stdout being merged
  into the compaction instructions, which isn't documented but works on 2.1.307. If that
  changes, re-injection still covers it.
- **PostCompact** archives the summary to `<project>/compactions/` and to claude-mem.

## Headless and scripted runs

The hooks **skip `claude -p`, the Agent SDK and GitHub Actions** (any session whose
`CLAUDE_CODE_ENTRYPOINT` starts with `sdk`). Without this, a script would get the
checkpoint block back as its result. To turn them on there, set
`"run_in_headless": true` or `TASK_MEMORY_HEADLESS=1`.

**Limit:** a `claude -p` started *from inside* an interactive session inherits that
session's entrypoint, so it isn't detected. Set `TASK_MEMORY_DISABLE=1` for such nested
runs. `TASK_MEMORY_DISABLE=1` turns off every hook anywhere.

## Guardrails

- **Asks once per prompt.** If Claude declines, the hook doesn't loop. It uses the hook's
  `prompt_id` when present.
- **Tasks waiting on you.** After an in-progress marker, the hook stays quiet until
  there is new tool work.
- **No duplicates.** The same block is never saved twice. A background result for a span
  that a newer checkpoint already covers is dropped.
- **Half-written transcript lines** are left for the next span, not skipped.
- **Subagents** never checkpoint.
- **No transcript, no hooks.** If session saving is off (`transcript_path` empty), the
  hooks quietly do nothing.
- **Fails open.** Any error is logged to `~/.claude/task-memory/errors.log`, and Claude
  carries on as normal.

## Install

```bash
cd docs/claude-code-config/task-memory-hooks
./install.sh --tmux-autocompact            # inline checkpoints + tmux auto-/compact
./install.sh --background-checkpoints      # Haiku writes checkpoints instead
./install.sh --autocompact-pct 70          # different threshold (1-100)
./install.sh --no-autocompact-pct          # don't set CLAUDE_AUTOCOMPACT_PCT_OVERRIDE
```

What the installer does:
- Copies the script to `~/.claude/hooks/task-memory/`.
- Writes `~/.claude/task-memory/config.json`. An existing file is kept, except that the
  tmux and mode flags are updated to match the options you passed.
- Merges four hook entries into `~/.claude/settings.json`: `Stop`, `PreCompact`,
  `PostCompact`, and `SessionStart` with the matcher `startup|resume|clear|compact`.
- Backs up `settings.json` first.
- Never touches other hooks, settings or plugins, including claude-mem's hooks.
- Is safe to re-run, and respects `CLAUDE_CONFIG_DIR`.
- Leaves an existing `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` alone.
- Warns if your Claude Code is older than the version tested.

Restart Claude Code, or open `/hooks`, to load the hooks.

To remove: `./uninstall.sh`. Add `--purge` to also delete saved data. Memories already
written to Serena and claude-mem are kept.

Run the tests with `python3 -m unittest discover -s tests -v` (56 tests).

## Configuration (`~/.claude/task-memory/config.json`)

| Key | Default | Meaning |
|---|---|---|
| `simple_max_tool_calls` / `simple_max_tokens` (X) / `simple_max_context_growth` (Y) | 3 / 8000 / 20000 | Simple-task limits |
| `complex_min_*` | 20 tools, 40k tokens, 60k growth, 8 edits, 4 instructions, 1 subagent | Complex triggers |
| `checkpoint_mode` | `inline` | `inline` or `background` |
| `proactive_protocol` | `true` | Inject the protocol at session start (inline mode) |
| `background_model` / `background_timeout_seconds` / `background_max_chars` | `haiku` / 240 / 60000 | Background mode |
| `run_in_headless` | `false` | Run in `claude -p` / SDK sessions |
| `session_start_max_chars` / `ledger_entries_on_start` / `learnings_on_start` | 9000 / 5 / 8 | Injection size |
| `claude_mem` / `serena` | `true` | Integrations |
| `tmux_autocompact` / `tmux_delay_seconds` | `false` / 3 | tmux auto-`/compact` |
| `state_retention_days` | 14 | Prune per-session state |

Environment overrides: `TASK_MEMORY_DISABLE`, `TASK_MEMORY_HEADLESS`, `TASK_MEMORY_MODE`,
`TASK_MEMORY_TMUX_AUTOCOMPACT`, and `TASK_MEMORY_HOME` (the data directory).

`<project>` is the git top-level directory of the working directory, or the working
directory itself when it isn't a git repo.
