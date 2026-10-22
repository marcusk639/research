---
name: tdd-task-breakdown
description: Break an implementation plan into concrete, discrete, well-defined tasks that one agent can build end to end with test-driven development. Writes one task file per task (goal, scope, interfaces, Given/When/Then acceptance criteria, required positive/negative/edge/error test cases, test command, definition of done) plus a dependency-ordered INDEX.md. Output is the input format for /tdd-implement-task.
argument-hint: <path-to-implementation-plan> [--out <tasks-dir>]
disable-model-invocation: true
---

# tdd-task-breakdown

Turn an implementation plan into a set of task files. Each task must be something **one
agent can take from an empty test file to passing code with no other input** besides the
task file, its listed dependencies, and the codebase. `/tdd-implement-task` consumes these
files, so the format in [`task-template.md`](task-template.md) is a contract: keep every
section, never rename one.

## Inputs

- `$ARGUMENTS` — path to the plan. `--out <dir>` overrides the output directory
  (default: `<plan-dir>/tasks/`).
- If no plan path is given, ask for one. Do not guess.
- If the output directory already has task files, stop and ask whether to (a) write
  to a new directory, (b) add to the set already there with new IDs, or (c) overwrite.
  Never silently clobber.

## Phase 1 — Read and understand

1. Read the **entire plan** end to end before writing anything. Read every document it
   links to or names as a requirement.
2. Survey the target codebase enough to write accurate tasks:
   - language(s), framework, package manager
   - test framework, test file naming and location, the exact command to run one
     test file and the whole suite
   - module layout, existing patterns the plan builds on, the public interfaces the
     plan touches
   If there is no test framework yet, the first task is setting one up (with a smoke
   test). Record this.
3. Write a private working summary: the requirements (number them `R-1`, `R-2`, …), the
   components, the data flow, external dependencies, and non-functional requirements
   (performance, security, compatibility).

## Phase 2 — Clarify

List every point where the plan is ambiguous, contradicts itself, leaves out a
behavior (especially error and edge behavior), or leaves out an interface. Ask the user
about them with `AskUserQuestion` (batch related questions; give a recommended default
for each). **Do not decompose until every blocking question is resolved.** A question
that only affects one task can instead go in that task's `Open Questions` section as
non-blocking, along with the assumption made.

## Phase 3 — Decompose

Rules for a well-formed task:

- **One behavioral outcome.** A task changes or adds one observable behavior. If its title
  needs "and", split it.
- **A vertical slice.** Prefer tasks that deliver a testable behavior through every layer
  it needs over layer-by-layer tasks ("all models", then "all endpoints"). Pure
  infrastructure tasks (test harness setup, schema migration) are allowed when the
  slices depend on them. They still need tests that can be checked.
- **Testable through a public interface.** Every acceptance criterion can be checked by
  a test that calls a public interface (function, class, endpoint, CLI, UI event). If a
  criterion can only be checked by inspecting internals, rewrite the criterion.
- **Independently completable.** All the task needs is its own file, the codebase, and
  the finished output of its listed dependencies. No task depends on an unfinished
  sibling.
- **Sized for one agent session.** Roughly 1–8 acceptance criteria and a handful of
  files. Bigger means split. A trivial one-liner is merged into a neighbor.
- **Explicit contracts at seams.** When task B uses something task A creates, both
  task files state that interface identically: name, signature, types, errors raised,
  side effects.

Order the tasks by dependency. Group tasks that have no dependency on each other into
**waves**: wave 1 depends on nothing, and wave N depends only on earlier waves. Tasks in
the same wave have no dependency on each other. They may be built in parallel only
in separate git worktrees, because in one working tree each run's deliberately failing
tests would corrupt the other's results.

## Phase 4 — Write the task files

For each task, copy [`task-template.md`](task-template.md) to
`<out>/T<NN>-<kebab-slug>.md` (two-digit zero-padded IDs in dependency order) and fill
every section:

- **Acceptance criteria** as numbered `AC-1…` Given/When/Then statements that describe
  behavior, never implementation.
- **Required test cases** as numbered `TC-1…` rows. Each one names the AC it covers and
  its kind: `positive`, `negative` (invalid input or a forbidden action is rejected
  correctly), `edge` (boundaries, empty, max, unicode, concurrency where relevant),
  `error` (a dependency fails, I/O fails, timeout), or `regression` (existing behavior
  that must not change). Every AC needs at least one positive test case. Every AC that
  accepts input or can fail needs at least one negative or error test case. This list
  is the floor, not the ceiling. The test author adds more.
- **Test command** exactly as it would be typed, for both the task's tests and the full
  suite.
- **Status:** `todo`.

Then write `<out>/INDEX.md`:

```markdown
# Task Index — <plan title>

Source plan: <relative path> · Generated: <date> · Tasks: <n>

## Conventions
- Test framework: <name> · Task test command pattern: `<cmd>` · Full suite: `<cmd>`
- Requirement coverage: see matrix below

## Waves
| Wave | Tasks (can run in parallel) |
|------|-----------------------------|
| 1    | T01, T02                    |

## Tasks
| ID | Title | Depends on | Covers | Status |
|----|-------|-----------|--------|--------|
| T01 | ... | — | R-1, R-3 | todo |

## Requirement → Task Matrix
| Requirement | Tasks |
|-------------|-------|
| R-1 <short text> | T01, T04 |

## Assumptions and Deferred Questions
- ...
```

## Phase 5 — Validate (repeat until clean)

Check the whole set against this list. Fix every failure, then run the whole
list again. Stop only after a full pass finds nothing. **Cap: 5 passes.** If problems
remain after that, show them to the user and ask whether to continue, accept them as
listed assumptions, or stop.

1. **Coverage:** every requirement `R-n` maps to at least one task, and every task maps
   to at least one requirement (no scope creep).
2. **No overlap:** no behavior is owned by two tasks.
3. **Dependencies:** the graph has no cycles, every dependency ID exists, and the waves
   are consistent with it.
4. **Contracts:** each interface shared across tasks is stated identically in both
   files.
5. **Each task:** has one outcome, a public-interface-testable AC for every
   behavior, and positive plus negative/error test cases per the rules above. The test
   command is exact. The scope's in/out lists are explicit. Nothing reads "TBD" unless
   it's listed under Open Questions with an assumption.
6. **Self-sufficiency:** reading only the task file, its dependencies' interface
   sections, and the codebase, could a fresh agent build it without asking anything?
   If not, add the missing context.

## Report

Tell the user: the number of tasks and waves, the output path, assumptions made,
non-blocking questions left open, and how to start:
- one task at a time: `/tdd-implement-task <out>/T01-<slug>.md`
- the whole set, unattended between questions:
  `claude --agent tdd-orchestrator "<plan-path> --out <out>"` (it picks up the existing
  `INDEX.md`)

## Constraints

- Do not write code or tests. This skill only produces task files.
- Never invent requirements the plan doesn't state. If something seems needed but
  isn't in the plan, raise it in Phase 2 or record it as an assumption.
