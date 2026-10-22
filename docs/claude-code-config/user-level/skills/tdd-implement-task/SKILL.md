---
name: tdd-implement-task
description: Complete one task file (from /tdd-task-breakdown) using strict, spec-first test-driven development across separate agents. Read the task end to end, ask clarifying questions, have a test author write positive/negative/edge/error tests from the spec (not from current code), review the tests in three passes, lock them and confirm they fail first, have a separate implementer write the code, review the code in three passes, then run a test-fix-review loop until every test passes and review is clean. Use when the user says "implement T03", "TDD this task", or runs it on a task file.
argument-hint: <path-to-task-file> [--commit none|split|single]
disable-model-invocation: true
---

# tdd-implement-task

You are the **orchestrator** for one task. You read, clarify, delegate, decide when a
phase is done, enforce the test lock, and run the tests. You do **not** write tests or
production code yourself. That separation is the point: an agent that writes both
tends to write tests that match its code rather than the spec, and coding agents have
been measured deleting, weakening, or hardcoding against tests to make them pass.

The roles are user-level subagents, invoked with the `Agent` tool:

| Role | `subagent_type` | Can edit |
|------|-----------------|----------|
| Test author | `tdd-test-author` | test files (+ interface stubs, phase 2 only) |
| Test reviewer | `tdd-test-reviewer` | nothing (read-only) |
| Implementer | `tdd-implementer` | production code, never tests |
| Code reviewer | `tdd-code-reviewer` | nothing (read-only) |

This skill must run in the **main thread** (a session started normally, or with
`claude --agent tdd-orchestrator`). Subagents cannot spawn subagents. If the `Agent` tool
is unavailable, or one of the four agents is not installed, stop and tell the user to run
`docs/claude-code-config/user-level/install.sh` (or copy the agents into
`~/.claude/agents/`).

Each subagent starts with a blank context. Every delegation prompt must include: the
absolute path of the task file, the paths of its dependency task files, the test
commands, the phase, and exactly what to return. Never assume a subagent remembers an
earlier invocation.

## Arguments and setup

- `$ARGUMENTS`: the task file path (required) and `--commit none|split|single` (default
  **`none`**).
  - `none`: never commit. Leave all changes in the working tree.
  - `split`: two commits, tests first (after Phase 4b) and code second (after Phase 8).
    The history then shows the tests came first.
  - `single`: one commit with tests and code after Phase 8.
  Commits stage **only the files this run created or changed**, added by explicit path
  (never `git add -A`/`.`). They never include the run directory (`.tdd-runs/`) or
  the task/INDEX files, are never pushed, and use the repo's commit-message convention
  if it has one, otherwise `test(T<NN>): <title>` / `feat(T<NN>): <title>`. With `split`,
  test changes made after the first commit go into the second one and are listed in
  the report. At the start, record `git status --porcelain`. If the directory is not a
  git repo, or a file this run needs to commit already had uncommitted changes before
  the run, downgrade to `none` and say so. Never commit someone else's changes.
- **Run directory:** `<task-dir>/.tdd-runs/T<NN>/`. It holds the test-lock manifest, the
  snapshot copies of the locked tests, and the command logs. Create it at the start. If
  the repo isn't ignoring it, suggest adding `.tdd-runs/` to `.gitignore` (don't edit
  `.gitignore` unasked).
- Set the task file's `Status` to `in-progress` (and its row in `INDEX.md`, if present).

## Phase 0 — Understand

1. Read the **entire task file**, top to bottom, before anything else. Then read every
   dependency task file's `Interfaces` section, the source-plan section it cites, and
   every file under `Context` and `Likely Files`.
2. Read the existing code the task touches and the repo's test conventions: framework,
   file location, naming, fixtures, how mocks are done here.
3. Confirm the task's test commands actually run (for example, run the full suite once
   and record the baseline in `run-dir/baseline.log`). **If the baseline suite is
   already failing, record which tests fail.** They are not this task's to fix. They
   are excluded from "all tests pass" only if they're unrelated, and the report must
   list them.
4. Write a **working summary** (shown to the user):
   - what behavior must exist when done
   - the ACs in your own words
   - the interfaces
   - what is out of scope
   - how the tests will be run

   If you cannot write any part of it plainly, you don't understand the task yet.

If the task file is missing template sections (no ACs, no test cases, no test
command), treat each gap as an ambiguity for Phase 1.

## Phase 1 — Clarify

List every ambiguity, contradiction, unstated behavior (especially failure behavior),
and unstated interface detail. Ask the user with `AskUserQuestion` (batched, with a
recommended answer for each). **Do not proceed while any blocking question is
open.** Record each answer in the task file under `Open Questions` as
`Q: … — Resolved: …` so later agents see the same spec you do. If nothing is
ambiguous, say so explicitly and move on.

## Phase 2 — Write the tests (test author)

Delegate to `tdd-test-author`. The prompt states:

- Source of truth: the task file (with resolved questions), the dependency interfaces,
  and the repo's test conventions.
- It must test **how the feature should behave per the spec**, through public
  interfaces. It must not read or mirror the implementation of the code under change.
  Existing code may be read only for public signatures, fixtures, and test conventions.
- First produce a **test plan matrix** covering every `TC-n` from the task, plus any
  additional cases it identifies. Each row gives the ID, the AC it covers, the kind
  (positive / negative / edge / error / regression), the input, and the expected
  observable result. Then write the tests.
- For interfaces the task creates that don't exist yet, it may create **minimal
  stubs**: the exact signature from the task's `Interfaces` section, with a body that
  only raises or returns a "not implemented" error. This makes tests fail on
  assertions rather than imports. No logic in stubs.
- Return: the matrix, the list of test files written, the list of stub files written.

## Phase 3 — Review the tests (three passes)

Run three review passes **in order**, each a fresh `tdd-test-reviewer` invocation with one
focus. After each pass, send its blocking findings to `tdd-test-author` to fix
(include the findings verbatim), then start the next pass on the fixed tests.

1. **Coverage:** every AC and every `TC-n` is tested. Every input-accepting or fallible AC
   has negative/error tests. Boundaries are covered. Nothing in the matrix is missing
   from the code, and nothing in the code is outside the spec.
2. **Accuracy against the spec:** each expected value and error matches the spec, not a
   guess about the implementation. Tests go through public interfaces, mock only true
   external boundaries, and assert outcomes, not internals or call order (unless
   call order is the spec).
3. **Adversarial:** for each test, could a wrong, partial, or hardcoded implementation
   pass it? Look for tests that pass trivially, tautological assertions, shared mutable
   state, order dependence, nondeterminism (time, randomness, network), and missing
   cleanup.

Reviewers label each finding `blocking` or `non-blocking`. A pass is **clean** when it
has no blocking findings. If pass 3 isn't clean, run more passes with the
adversarial-plus-coverage focus until one is clean. **Cap: 5 passes total.** If it's
still not clean, stop and show the user the outstanding findings.

## Phase 4 — Lock the tests and confirm they fail

**4a. Lock.**
1. Write `run-dir/manifest.sha256` with `sha256sum` (or `shasum -a 256`) of every test
   file from Phase 2.
2. Copy each file into `run-dir/locked/`, keeping its relative path.

From now on, a test file may change **only** through the test-change procedure below.

**4b. Confirm they fail.** Run the task's test command and save the output to
`run-dir/red.log`. Classify every test:

- **Fails for the right reason:** an assertion failure, or the stub's not-implemented
  error. Expected.
- **Fails for the wrong reason:** a syntax error, a bad import of existing code, broken
  fixture or setup, or a missing test dependency. The test is broken. Send it back to
  the test author (and one Phase 3 adversarial pass), then lock it again.
- **Passes:** allowed only for a `regression`-kind row that guards existing behavior.
  Any other passing test is meaningless or tests the wrong thing. Send it back the same
  way.

Proceed only when every non-regression test fails for the right reason. With
`--commit split`, commit the tests (and stubs) now.

## Phase 5 — Write the code (implementer)

Delegate to a **new** `tdd-implementer`. The prompt states:

- Implement the task file's spec. The locked tests are the spec made executable.
- Read the tests, but **never create, edit, rename, delete, skip, or disable a test
  file**.
- Do not special-case test inputs, detect the test environment, or hardcode expected
  values. The code must be correct for inputs the tests don't use.
- Replace the stubs with real implementations and follow existing codebase patterns.
- The implementer may run the tests while working.
- If it believes a test contradicts the spec, it must **stop and report** the test, the
  spec text, and why. It does not work around it.
- Return: the files changed, a summary of the design, and any suspected test or spec
  conflicts.

**After every implementer invocation (here and in Phases 6–7)**, check the test lock.
Recompute the hashes, compare them with the manifest, and look for new
`skip`/`xit`/`xdescribe`/`.only`/`@pytest.mark.skip`/`t.Skip` markers or deleted test
files. If anything changed, restore the files from `run-dir/locked/`, log the incident
in the report, and re-delegate with a reminder of the rule.

## Phase 6 — Review the code (three passes)

Three passes **in order**, each a fresh `tdd-code-reviewer` invocation with one focus.
After each pass, send its blocking findings to `tdd-implementer` to fix (lock check
afterward), then start the next pass on the fixed code.

1. **Matches the spec and is correct:** every AC is implemented as specified, with
   correct logic and correct interfaces (exact signatures and errors). Nothing outside
   the scope.
2. **Robust:** error handling, edge cases and boundaries, input validation, resource
   cleanup, concurrency where relevant, and security (injection, authorization, secrets,
   unsafe deserialization).
3. **Quality and test-gaming:** consistent with codebase patterns, readable, no dead
   code or duplication, no needless complexity. **No special-casing of test inputs, no
   hardcoded expected values, no test-environment detection.**

The clean/blocking rules and the **5-pass cap** are the same as Phase 3. Reviewers
do not run or modify tests. They review code as written.

## Phase 7 — Test, fix, review loop

Repeat until the exit condition holds. **Cap: 5 cycles.** If the cap is hit, stop and
show the user the remaining failures, what was tried, and your diagnosis.

1. **Run** the task's tests and then the full suite. Save the output to
   `run-dir/cycle-<n>.log`.
2. **Exit** when every task test passes, the full suite passes apart from the
   pre-existing failures recorded in Phase 0, and the last review was clean. Go to
   Phase 8.
3. **Diagnose each failure** before changing anything. Read the failure, the test, and
   the spec. Decide which case it is:
   - **The code is wrong** (the default assumption). Delegate to `tdd-implementer` with
     the failure output, the test name, and the AC it checks. The fix must make the
     code do what the feature should do, not merely satisfy the assertion. Check the
     lock afterward.
   - **The test contradicts the spec.** Use the test-change procedure below. Never edit
     the test to fit the code.
   - **The spec is ambiguous or contradictory.** Ask the user, record the answer in the
     task file, then apply it through whichever case it implies.
   - **A regression in another part of the suite.** Treat it as "the code is wrong",
     unless the task's spec explicitly changes that behavior, in which case it's a test
     change.
4. **Review** once the previously failing tests pass. Run a `tdd-code-reviewer` pass
   focused on the changes made in this cycle (all three focus areas, scoped to the diff).
   If it has blocking findings, send them to the implementer.
5. **If the code changed in step 3 or 4**, go back to step 1 (the tests run again). If
   the review was clean and no code changed since the last run passed, the exit
   condition holds.

### Test-change procedure (the only way a locked test changes)

1. You (the orchestrator) write down which test is wrong, the spec text it contradicts,
   and why. "The code doesn't do this" is never a reason.
2. If the right behavior isn't obvious from the spec, ask the user.
3. Delegate the change to `tdd-test-author`, then run one `tdd-test-reviewer` pass
   (accuracy + adversarial) on the changed tests.
4. Lock the tests again: update `manifest.sha256` and `run-dir/locked/`. Log the change
   (test, reason, before/after summary) for the report.

## Phase 8 — Integrity check

All of the following must hold, otherwise go back to the phase that failed:

- The test hashes match the final manifest. Every manifest change has a logged test
  change behind it.
- No new skip or only-markers in the task's test files. No test file was deleted.
- Every `TC-n` and every row of the matrix from Phases 2–3 exists as a test, and every
  one passes.
- The full suite passes apart from the pre-existing failures recorded in Phase 0.
- The task's `Definition of Done` checklist is satisfied, item by item.

With `--commit split` or `single`, commit now (production code, plus tests for
`single`; never the run directory).

## Phase 9 — Report

Write `<task-dir>/T<NN>-<slug>.report.md` with these sections:

- **Summary:** status, files changed, commit SHAs or "not committed".
- **Clarifications:** the questions asked and the answers.
- **Test matrix:** the final matrix with pass status.
- **Test review:** findings per pass and how each was resolved.
- **Failure check:** the classification from Phase 4b.
- **Code review:** findings per pass and how each was resolved.
- **Test-fix cycles:** the number of cycles, with the failures and diagnoses for each.
- **Test changes and lock incidents:** each change with its reason, or "none".
- **Pre-existing suite failures:** or "none".
- **Remaining risks / follow-ups.**

Set the task's `Status` to `done` (or `blocked` if a cap or an unanswered question
stopped the run) in both the task file and `INDEX.md`. Tell the user the result in a
few lines and link the report.

## Hard rules

- The orchestrator never writes tests or production code. It delegates.
- The test author never reads the implementation of the code under change. The
  implementer never edits a test.
- Never weaken, skip, or delete a test to get to green. A failing test is evidence. Fix
  the code, or change the test only through the test-change procedure.
- Every cap that is hit ends in a report to the user, never a silent stop or a fake
  success.
- Report results exactly as they are. If tests fail, say so with the output.
