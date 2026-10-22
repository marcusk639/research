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
| `agents/tdd-orchestrator.md` | Runs a whole plan: breakdown → your approval → every task in dependency order, with resumable state and a run report |

## Flow

Whole plan, one command (must be the main session, since it spawns the role agents):

```bash
claude --agent tdd-orchestrator "path/to/plan.md [--commit none|split|single] [--strict]"
```

It breaks the plan down, **waits for your approval**, asks each wave's clarifying
questions in one batch, then runs every task through the steps below, one at a time. A
blocked task blocks only the tasks that depend on it (`--strict` stops the run instead).
State lives in `tasks/RUN-STATE.md`, so rerunning the same command resumes. The result
goes in `tasks/RUN-REPORT.md`.

Per skill:

```
plan ──/tdd-task-breakdown──▶ tasks/T01..Tnn + INDEX.md
task ──/tdd-implement-task──▶ understand → clarify → tests → 3× test review
     → lock + confirm failing → code → 3× code review
     → [run tests → fix code → rerun … → review changes (blocking → fix → rerun)]*
     → integrity check → report
```

`/tdd-implement-task` must run in the main session (subagents can't spawn
subagents). The implementer is stopped from changing tests by detection, not prevention:
it needs edit tools for the code. So the orchestrator hashes every file that decides test
outcomes (all test files, fixtures, test-runner config) and restores them after every
implementer call. It runs one task per working tree at a time. Parallel runs need
separate worktrees. Every review and fix loop has a cap. Hitting one asks you whether to
continue rather than stopping silently.

Design rationale and evidence (agents deleting or hardcoding tests, reward hacking that
grows with task size): `optimal-ai-dev-flow/findings/w3-verification.md`,
`app-dev/VERIFICATION-STRATEGY.md`.
