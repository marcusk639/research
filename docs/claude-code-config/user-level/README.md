# User-level Claude Code config: TDD skills and agents

Source of truth for skills and agents meant to live at **user level**
(`~/.claude/`), so they're available in every repo. They're kept here only so
they're versioned. This directory is not loaded as project config.

## Install

```bash
docs/claude-code-config/user-level/install.sh          # skips files that differ
docs/claude-code-config/user-level/install.sh --force  # overwrites, backing up to *.bak-<timestamp>
```

Honors `$CLAUDE_CONFIG_DIR`. Restart Claude Code (or start a new session) afterwards.
The installer never deletes anything. If a skill or agent is renamed or removed here,
delete the old copy from `~/.claude/` by hand.

## Contents

| Path | What it is |
|------|------------|
| `skills/tdd-task-breakdown/` | `/tdd-task-breakdown <plan>`: splits an implementation plan into TDD-ready task files + `INDEX.md` (format: `task-template.md`) |
| `skills/tdd-implement-task/` | `/tdd-implement-task <task> [--commit none\|split\|single]`: completes one task through spec-first TDD (default: no commits) |
| `agents/tdd-test-author.md` | Writes tests from the spec, never from the implementation |
| `agents/tdd-test-reviewer.md` | Read-only; three-pass test review (coverage → accuracy → adversarial) |
| `agents/tdd-implementer.md` | Writes production code; never touches tests, fixtures, or test config (hash-guarded) |
| `agents/tdd-code-reviewer.md` | Read-only; three-pass code review (spec/correctness → robustness → quality and test-gaming) |
| `agents/tdd-orchestrator.md` | Runs a whole plan: breakdown → your approval → every task unattended, in dependency order → blocker resolution → run report. Resumable. |
| `agents/tdd-blocker-resolver.md` | Works through `BLOCKERS.md`: re-diagnoses, retries fresh with a strategy brief, splits oversized tasks, creates fix tasks, applies human decisions. Runs as the orchestrator's last stage or standalone. |
| `skills/tdd-implement-task/blocker-template.md` | The format of a `BLOCKERS.md` entry: a blocker written up as a task, with ranked suggested fixes |

## Flow

Whole plan, one command (must be the main session, since it spawns the role agents):

```bash
claude --agent tdd-orchestrator "path/to/plan.md [--commit none|split|single] [--interactive] [--strict]"
```

1. **Kickoff (interactive):** it breaks the plan down, asks its clarifying questions, and
   **waits for your approval** of the task set.
2. **Unattended run:** every task goes through the steps below, one at a time, in
   dependency order. Nothing waits on you:
   - low-risk ambiguities are assumed and logged for your review
   - anything else becomes a **blocker**, written to `tasks/BLOCKERS.md` as a fully
     described task with ranked suggested fixes
   - the blocked task's partial work is set aside, its dependents are skipped, and the
     run continues
3. **Resolution:** when no runnable work is left, the `tdd-blocker-resolver` process
   attempts each blocker (2 attempts by default). It retries fresh with a strategy
   brief, splits oversized tasks, creates fix tasks, and fixes in-repo environment
   problems. Spec decisions are never guessed. They become `needs-human`.
4. **Report:** the result goes in `tasks/RUN-REPORT.md`. To continue after answering
   `needs-human` entries (fill in their `Decision` sections):
   `claude --agent tdd-blocker-resolver "path/to/tasks"`.

State lives in `tasks/RUN-STATE.md`, so rerunning the same command resumes.
`--interactive` asks you mid-run instead. `--strict` stops at the first blocker.

Per skill:

```
plan ──/tdd-task-breakdown──▶ tasks/T01..Tnn + INDEX.md
task ──/tdd-implement-task──▶ understand → clarify → tests → 3× test review
     → lock + confirm failing → code → 3× code review
     → [run tests → fix code → rerun … → review changes (blocking → fix → rerun)]*
     → integrity check → report
```

`/tdd-implement-task` runs in the main session (or under `tdd-orchestrator`). It asks
you questions and delegates to the four role agents, which have no `Agent` tool of their
own. Each task keeps its progress in `.tdd-runs/T<NN>/state.md`, so an interrupted task
resumes safely. The implementer is stopped from changing tests by detection, not prevention:
it needs edit tools for the code. So the orchestrator hashes every file that decides test
outcomes (all test files, fixtures, test-runner config) and restores them after every
implementer call. It runs one task per working tree at a time. Parallel runs need
separate worktrees. Every review and fix loop has a cap. Hitting one asks you whether to
continue when run interactively. Unattended (`--unattended`), it becomes a documented
blocker. It never stops silently.

Design rationale and evidence (agents deleting or hardcoding tests, reward hacking that
grows with task size): `optimal-ai-dev-flow/findings/w3-verification.md`,
`app-dev/VERIFICATION-STRATEGY.md`.
