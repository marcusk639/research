# task-memory hooks

User-level Claude Code hooks that checkpoint each **moderate or complex task** when it
finishes. Each checkpoint records a summary, the context follow-up tasks need, and
learnings. It is saved to disk, **claude-mem** and **Serena**, and is re-injected after
compaction. Compaction then happens automatically: through a lowered auto-compact
threshold, through idle compaction, or (opt-in) by typing `/compact` into your tmux
pane. Simple tasks are left alone.

Tested on Claude Code 2.1.307 with Python 3.13 (standard library only).

## What counts as a task

A **task** is a series of one or more instructions working toward one goal. The hooks
measure each task as a **span**: everything in the conversation since the last saved
checkpoint (or since the session started). Every time Claude stops, the span is
classified:

| Class | Definition | Effect |
|---|---|---|
| **Simple** | A single trivial goal. **All** of these hold: ≤ 3 tool calls · 0 file edits · 0 subagents · < **X** tokens generated · < **Y** context growth | Nothing. No checkpoint, no compaction. |
| **Moderate** | Anything beyond simple that isn't complex. | Checkpoint (≤ 250 words) + memory saves + compaction |
| **Complex** | **Any** of these: ≥ 20 tool calls · ≥ 8 file edits · ≥ 1 subagent · ≥ 4 instructions · ≥ 40k tokens generated · ≥ 60k context growth | Checkpoint (≤ 600 words) + memory saves + compaction |

**X = 8,000 tokens generated.** This counts the output tokens Claude produced during the
span, including thinking.
- It measures how much reasoning and writing the task took.
- Input-side counts are deliberately left out. A session's first request writes the
  whole system prompt to cache (about 27k tokens), and so does any request after the
  cache expires. Counting those would make a one-line question look expensive.

**Y = 20,000 tokens of context growth.** This is how much the context window grew during
the span: the sum of the increases in prompt size between consecutive API requests.
- File reads, tool output and long answers all add to it.
- A drop in size caused by compaction is ignored.
- 20k is about 10% of a 200k window. Context this large is worth reclaiming.

Notes:
- **File edits** are calls to `Edit`, `MultiEdit`, `Write`, `NotebookEdit`, or Serena's
  symbol and line editing tools. Any single edit makes a task at least moderate.
- **Instructions** count only prompts you typed. Tool results, hook output, subagent
  reports, task notifications and slash commands don't count.
- Several trivial questions in a row stay simple, because they consume nothing worth
  saving. They become moderate only if they add up past X or Y.

Every threshold can be changed in `~/.claude/task-memory/config.json`.

## How it works

```
Claude stops ──► Stop hook classifies the span
                  ├─ simple ───────────────► allow stop
                  └─ moderate / complex ───► block once: "reply with a <task-checkpoint> block"
                                              │  (or <task-checkpoint status="in-progress"/> if
                                              │   still waiting on you)
Claude replies with the block ──► Stop hook parses it and writes:
     ~/.claude/task-memory/projects/<project>/checkpoints/<ts>-<slug>.md, latest.md, ledger.md
     project learnings ─► <project>/learnings.md + Serena  <repo>/.serena/memories/learnings/<YYYY-MM>.md
     global learnings  ─► ~/.claude/task-memory/global-learnings.md + Serena ~/.serena/memories/global/learnings/<YYYY-MM>.md
     whole checkpoint  ─► claude-mem  POST /api/memory/save  (searchable with claude-mem's search tool)
     then shows "📌 checkpoint saved …" and, if enabled, types /compact into your tmux pane

Compaction (auto at 60% · idle · tmux · manual)
     PreCompact  ─► tells the summarizer to keep the latest checkpoint verbatim, and to keep any
                    un-checkpointed work in full detail
     PostCompact ─► archives the summary to <project>/compactions/ and to claude-mem
     SessionStart(compact|clear) ─► re-injects latest.md + the 5 most recent ledger entries
     SessionStart(startup|resume) ─► injects the recent ledger only (claude-mem injects its own timeline)
```

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

Claude writes the block, so it can judge what's worth keeping. The hook script does all
the saving, so Claude makes no tool calls and you get no permission prompts. Each
task costs one short extra model turn.

### Guardrails

- **One nudge per turn.** If Claude declines to write a checkpoint, the hook doesn't ask
  again until you send another message.
- **Tasks waiting on you.** If the task isn't finished (a plan awaiting approval, a
  question for you), Claude replies with the in-progress marker. The hook stays quiet
  until there is new tool work.
- **No duplicates.** The same block is never saved twice.
- **Subagents** never checkpoint.
- **Fails open.** If a hook script hits an error, it logs it to
  `~/.claude/task-memory/errors.log` and lets Claude carry on as normal.
- **Turning it off.** Set `TASK_MEMORY_DISABLE=1` to switch off every hook for one
  session, for example in scripted `claude -p` runs.

## Why compaction isn't triggered directly

Claude Code (as of 2.1.307) gives hooks no way to run `/compact`, and Claude can't call
`/compact` itself. Hooks can watch, block or add guidance to a compaction, but not start
one. So the hooks do the following instead:

1. Save everything worth keeping at the end of each moderate or complex task.
   Compaction (or even `/clear`) then loses nothing.
2. Compact through what Claude Code supports:
   - **Earlier auto-compaction.** `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60` makes
     auto-compaction trigger at 60% of the window instead of near the limit.
   - **Idle compaction.** Claude Code compacts long conversations while the session is
     idle, which usually means between tasks. It is on by default.
   - **tmux auto-`/compact` (opt-in).** After each checkpoint, a background process
     types `/compact <keep the checkpoint>` into your pane. It only does this when the
     Claude process running the hook is the foreground job of that pane (checked with
     `ps` and `tmux`), so headless `claude -p` runs launched from a tmux pane never
     type into it. Before typing, it waits for the pane to stop redrawing. It then checks
     that a compaction started and retries once (clearing the input first) if the
     keystrokes were swallowed. **Caveat:** if you start typing within about 3 seconds
     of a checkpoint, the command can mix with your text.
   - **Manual.** Run `/compact` or `/clear` whenever the "📌 checkpoint saved" line
     appears.

The PreCompact guidance uses a behaviour of Claude Code that isn't documented: plain
stdout from a PreCompact hook is merged into the compaction instructions. I confirmed it
on 2.1.307: the summary kept the checkpoint word for word. If a later version drops it,
the hooks still work, because the checkpoint is re-injected after compaction anyway.

## Install

```bash
cd docs/claude-code-config/task-memory-hooks
./install.sh --tmux-autocompact        # tmux auto-/compact on (opt-in)
./install.sh                           # without tmux auto-/compact
./install.sh --autocompact-pct 70      # different auto-compact threshold
./install.sh --no-autocompact-pct      # don't set CLAUDE_AUTOCOMPACT_PCT_OVERRIDE
```

What the installer does:
- Copies `hooks/task_memory.py` to `~/.claude/hooks/task-memory/`.
- Writes `~/.claude/task-memory/config.json`. An existing file is kept, except that the
  tmux flag is updated to match the option you passed.
- Merges four hook entries into `~/.claude/settings.json`: `Stop`, `PreCompact`,
  `PostCompact`, and `SessionStart` with the matcher `startup|resume|clear|compact`.
- Backs up `settings.json` first.
- Never touches other hooks, settings or plugins, including claude-mem's hooks.
- Is safe to re-run.
- Respects `CLAUDE_CONFIG_DIR`, and leaves an existing `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`
  alone.

Restart Claude Code, or open `/hooks`, to load the hooks.

To remove: `./uninstall.sh`. Add `--purge` to also delete saved checkpoints. Memories
already written to Serena and claude-mem are kept.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Integrations

**claude-mem** (optional):
- The worker port is found from `CLAUDE_MEM_WORKER_PORT`, then from
  `~/.claude-mem/settings.json`, then from the defaults: `37700 + uid % 100`, then 37777.
- If the worker isn't running, saving is skipped quietly. Disk saves always happen.
- Checkpoints are saved with `metadata.kind = "task-checkpoint"`, and compaction
  summaries with `"compaction-summary"`.
- claude-mem's own SessionStart injection, observation capture and summaries keep
  running alongside. The hooks don't duplicate its timeline.

**Serena** (optional):
- Project learnings go to `<repo>/.serena/memories/learnings/<YYYY-MM>.md`, but only when
  the repo already has `.serena/project.yml`. The hooks never create a Serena project.
- Global learnings go to `$SERENA_HOME/memories/global/learnings/<YYYY-MM>.md` (default
  `~/.serena`), but only when that directory exists.
- Both are plain Markdown memories, so Serena's `list_memories` and `read_memory` see
  them. Project memories live in the repo, so commit them or ignore them as you prefer.

**Global vs project**:
- Project learnings are stored per project only.
- Global learnings go to the global stores only. A learning is never written to both.

## Files

| Path | Contents |
|---|---|
| `~/.claude/task-memory/projects/<project>/checkpoints/` | Every checkpoint, one file each |
| `~/.claude/task-memory/projects/<project>/latest.md` | The most recent checkpoint (re-injected after compact or clear) |
| `~/.claude/task-memory/projects/<project>/ledger.md` | One line per task, newest last |
| `~/.claude/task-memory/projects/<project>/learnings.md` | Project-specific learnings |
| `~/.claude/task-memory/projects/<project>/compactions/` | Archived compaction summaries |
| `~/.claude/task-memory/global-learnings.md` | Cross-project learnings |
| `~/.claude/task-memory/state/` | Per-conversation span state (pruned after 14 days) |
| `~/.claude/task-memory/config.json` | Thresholds and switches |

`<project>` is the git top-level directory of the working directory, or the working
directory itself when it isn't a git repo.
