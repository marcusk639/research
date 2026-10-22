# User-level Claude Code config: TDD skills and agents

Source of truth for skills and agents meant to live at **user level**
(`~/.claude/`), so they're available in every repo. They're kept here only so
they're versioned. This directory is not loaded as project config.

## Install

```bash
docs/claude-code-config/user-level/install.sh          # skips files that differ
docs/claude-code-config/user-level/install.sh --force  # overwrites, backing up to *.bak
```

Honors `$CLAUDE_CONFIG_DIR`. Restart Claude Code (or start a new session) afterwards.

## Contents

| Path | What it is |
|------|------------|
| `skills/tdd-task-breakdown/` | `/tdd-task-breakdown <plan>`: splits an implementation plan into TDD-ready task files + `INDEX.md` (format: `task-template.md`) |
| `skills/tdd-implement-task/` | `/tdd-implement-task <task> [--commit none\|split\|single]`: completes one task through spec-first TDD (default: no commits) |
| `agents/tdd-test-author.md` | Writes tests from the spec, never from the implementation |
| `agents/tdd-test-reviewer.md` | Read-only; three-pass test review (coverage → accuracy → adversarial) |
| `agents/tdd-implementer.md` | Writes production code; never touches tests (hash-checked) |
| `agents/tdd-code-reviewer.md` | Read-only; three-pass code review (spec/correctness → robustness → quality and test-gaming) |

## Flow

```
plan ──/tdd-task-breakdown──▶ tasks/T01..Tnn + INDEX.md
task ──/tdd-implement-task──▶ understand → clarify → tests → 3× test review
     → lock + confirm failing → code → 3× code review
     → [run tests → fix code → review → rerun]* → integrity check → report
```

`/tdd-implement-task` must run in the main session (subagents can't spawn
subagents). The implementer is stopped from changing tests by detection, not prevention:
it needs edit tools for the code, so the orchestrator hashes the locked tests and restores
them after every implementer call.

Design rationale and evidence (agents deleting or hardcoding tests, reward hacking that
grows with task size): `optimal-ai-dev-flow/findings/w3-verification.md`,
`app-dev/VERIFICATION-STRATEGY.md`.
