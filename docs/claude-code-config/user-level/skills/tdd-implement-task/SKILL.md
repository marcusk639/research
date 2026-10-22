---
name: tdd-implement-task
description: Complete one task file (from /tdd-task-breakdown) using strict, spec-first test-driven development across separate agents. Read the task end to end, ask clarifying questions, have a test author write positive/negative/edge/error tests from the spec (not from current code), review the tests in three passes, lock them and confirm they fail first, have a separate implementer write the code, review the code in three passes, then run a test-fix-review loop until every test passes and review is clean. Optional commits via --commit (default none). With --unattended it never waits on the user: low-risk ambiguities are assumed and logged, real blockers are written to BLOCKERS.md as fully described tasks with suggested fixes, and the task's partial work is set aside.
argument-hint: <path-to-task-file> [--commit none|split|single] [--run-baseline <log>] [--known-failures <file>] [--target-failures <file>] [--unattended] [--blockers <file>] [--blocker-id <B-NN>] [--attempt <n>]
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
| Test author | `tdd-test-author` | test files (+ interface stubs, until Phase 4b ends) |
| Test reviewer | `tdd-test-reviewer` | nothing (read-only) |
| Implementer | `tdd-implementer` | production code, never tests or test config |
| Code reviewer | `tdd-code-reviewer` | nothing (read-only) |

Run this skill in the **main session**, or under the `tdd-orchestrator` agent launched
with `claude --agent`. It asks the user questions and delegates to four agents, so it needs
both `AskUserQuestion` and the `Agent` tool. If the `Agent` tool is unavailable, or one of
the four agents is not installed, stop and tell the user to run `install.sh` from the `docs/claude-code-config/user-level/` directory of
their config repo (or copy the agents into `~/.claude/agents/`).

**Delegation prompts.** Each subagent starts with a blank context, so every prompt must
include:
- the absolute path of the task file and its dependency task files
- the test commands
- the phase, and the pass focus if it's a review
- exactly what to return

Reviewers have no shell, so paste in the text they need: the **review diff** (defined in
Phase 5) and the relevant test-run output. Never assume a subagent
remembers an earlier invocation.

**Strategy brief.** `tdd-blocker-resolver` may write
`<tasks-dir>/.tdd-runs/T<NN>-strategy.md` before retrying a blocked task. It holds the
earlier diagnosis, what failed, and the chosen approach. If it exists, read it in Phase 0,
include it in **every** delegation prompt, and use it in your own diagnoses. The earlier
attempt's set-aside work it points to is a **reference draft only**. Everything still
goes through the full write, review and lock process.

**Spec questions from any agent.** Spec gaps reported by the test author, spec questions
from either reviewer, and test/spec conflicts reported by the implementer are all handled
the same way:
1. Ask the user (as in Phase 1).
2. Record the answer in the task file's `Open Questions`.
3. Re-delegate the affected work.
4. If a locked test is affected, or the answer adds behavior no test covers, use the
   test-change procedure.
5. If code has already been reviewed (Phase 6 or later) and the answer changes the
   spec, that code was reviewed against an outdated spec. Record the amended spec items
   in `run-dir/spec-amendments.md`. Then either set `unreviewed` with
   **spec-amended** mode (Phase 7), or restart Phase 6 at pass 1 if you're still in
   Phase 6.

Never resolve a spec question by guessing.

**Caps.** Every loop below has a cap. When a cap is hit, don't stop silently and don't
fake success. Show the user the outstanding findings or failures, what was tried, and
your diagnosis, then ask with `AskUserQuestion` whether to (a) continue for another round
of the same size, (b) answer or adjust something and continue, or (c) stop and mark the
task `blocked`. In unattended mode, a cap hit is a blocker (see below).

## Unattended mode

With `--unattended`, the skill **never waits on the user**. It's used for long runs
(`tdd-orchestrator` and `tdd-blocker-resolver` pass it). Every place in this skill that
says "ask the user" follows this table instead:

| Situation | Unattended behavior |
|-----------|---------------------|
| An ambiguity or spec question (Phase 1, spec questions from agents, Phase 7 "spec is ambiguous") that passes the **low-risk test** below | Assume the conventional default and record it in the task's `Open Questions` as `Q: … — Assumed (unattended): … because …`. Continue. |
| An ambiguity or spec question that fails the low-risk test | **Blocker** (type `spec-question`). |
| Test-change procedure step 2: the right behavior isn't clear from the spec | **Blocker** (type `test-spec-conflict`). |
| Any cap hit | **Blocker** (type `cap-hit`). |
| An environment or tooling failure the role agents can't fix within the task's scope (a missing tool, a service that won't start, credentials, network) | **Blocker** (type `environment`). |
| Phase 0 unknown failure | With `--run-baseline` (an orchestrator or resolver run): stop, archive, report. The caller handles it. Without it: a **blocker** (type `earlier-failure`). |
| Phase 0 dependency check fails | With `--run-baseline`: stop without a blocker entry. The caller records it. Without it: a **blocker** (type `other`). |

**The low-risk test.** Assume a default only if **all** of these hold. Otherwise it's a
blocker.
- It doesn't change anything in the task's `Interfaces` section, or any contract a
  dependent task relies on.
- It doesn't decide externally visible behavior the plan cares about: error types,
  messages or statuses that callers handle, output and persistence formats, security,
  authorization, or data retention or loss.
- There's a clear conventional choice: an established pattern in this codebase, the
  repo's existing behavior in the same situation, or the recommended answer in the task
  file.
- Reversing it later is a local change to this task's code and tests.

**Blocker protocol.** When a blocker occurs:
1. **Stop the current phase.** Don't push on, and don't start other work in this task.
2. **Write or extend the blocker entry** in the `--blockers` file (default
   `<tasks-dir>/BLOCKERS.md`), following
   [`blocker-template.md`](blocker-template.md):
   - With `--blocker-id B-NN` (a resolver retry), **every** blocker in this run extends
     B-NN. Never open a second entry. Update `What happened`, the hypothesis, the
     suggested fixes and `Type` with the new evidence. Add an `Attempts` row with
     `#` set to the `--attempt` number, `By: resolver-retry`, and the outcome
     `blocked again at <phase>`. Leave the status to the resolver.
   - Otherwise, append a new entry with the next free ID. Its first `Attempts` row says
     `By: original-run`.

   Fill **every section** from the evidence in `run-dir` and the reviews. "Suggested
   fixes" must be concrete and ranked, and each must say whether it needs a human
   decision. For `spec-question` and `test-spec-conflict`, `To unblock` must state the
   exact question, the options, and a recommendation.
3. **Set aside** the task's partial work (next section) and record the outcome in the
   entry's `State of the work`.
4. Write the Phase 9 report with status `blocked` and the blocker ID. Set
   `Status: blocked` in the task file and `INDEX.md`, with the reason `B-NN`.
5. Return. The caller continues with other work.

## Setting aside a blocked task's work

This is only safe **at the moment the task blocks**, because no other task has run since
and this run's records still say exactly which files are its own. Never set aside work
later (a retry needs the work already out of the tree). Interactive runs ask the user
first. Unattended runs do it automatically.

1. **Find the task's own work:**
   - files that differ from their `pre-run/` copy
   - files with no `pre-run/` copy that differ from `HEAD`, or are new and untracked

   Exclude the tasks directory. Check the list against the files reported by the test
   author and implementer and the guard manifest's task test files. A file that doesn't
   fit those, and the user didn't change, means the records are inconsistent. Don't
   touch it, and list it in the entry.
2. Save `git diff` of those tracked files, plus a diff against their `pre-run/` copies
   where one exists, to `run-dir/set-aside/changes.patch`. Move new untracked files into
   `run-dir/set-aside/files/`, keeping their paths.
3. Restore each tracked file to its `pre-run/` copy if it has one, otherwise to `HEAD`.
4. **Commits** this run made (from `state.md`):
   - Unattended: `git revert --no-edit <sha>` newest first. This adds revert commits and
     deletes nothing.
   - Interactive: ask first.
   - If a revert conflicts, run `git revert --abort`, leave that commit in place, and
     record it as `not reverted` with the reason.
5. Run the full suite. It should match `baseline.log` (apart from accepted failures).
   Record any difference in the entry. A task whose set-aside is incomplete (a commit not
   reverted, or files it didn't dare touch) says so in its entry, so the orchestrator can
   add its failing tests to the run's known failures.

## Arguments and setup

- `$ARGUMENTS`: the task file path (required), `--commit none|split|single` (default
  **`none`**), and three options passed by `tdd-orchestrator`:
  - `--run-baseline <log>`: the full-suite result from before the first task of a plan
    run
  - `--known-failures <file>`: failing tests the user has already accepted during the
    run
  - `--target-failures <file>`: for a fix task, the existing failing tests it exists to
    make pass
  - `--unattended`: never wait on the user (see "Unattended mode")
  - `--blockers <file>`: where blocker entries go (default `<tasks-dir>/BLOCKERS.md`)
  - `--blocker-id <B-NN>`: this run is a retry of that blocker; extend its entry rather
    than opening a new one
  - `--attempt <n>`: with `--blocker-id`, the resolver's attempt number, used for the
    `Attempts` row

  Commit modes:
  - `none`: never commit. Leave all changes in the working tree.
  - `split`: two commits, tests and stubs first (after Phase 4b), then code (after
    Phase 8). The history then shows the tests came first.
  - `single`: one commit with tests and code after Phase 8.

  Commit rules:
  - Stage **only the files this run created or changed**, added by explicit path
    (never `git add -A`/`.`).
  - Never include anything under the tasks directory: task files, `INDEX.md`, reports,
    `RUN-STATE.md`, `RUN-REPORT.md`, and `.tdd-runs/`.
  - Never push.
  - Use the repo's commit-message convention if it has one, otherwise
    `test(T<NN>): <title>` / `feat(T<NN>): <title>`.
  - With `split`, test files changed after the first commit (through the test-change
    procedure) go into the second commit and are listed in the report.
  - On a **fresh** start (not a resume), record `git status --porcelain` into
    `run-dir/pre-run-status.txt`. Copy every file it lists as modified or untracked
    (outside the tasks directory) into `run-dir/pre-run/`. These are the user's own
    changes. If the directory is not a git repo, downgrade to `none`. Before each commit,
    if any file to be committed is in `pre-run/`, skip that commit and say so. With `split`, if the
    tests commit was skipped, skip the code commit too (committed code must never ship
    ahead of its tests). If only the code commit was skipped, the report must state that
    the tests commit exists and the code is uncommitted. Never commit someone else's
    changes.
- **Run directory:** `<task-dir>/.tdd-runs/T<NN>/`, where `T<NN>` is the task's ID
  (every task, including a fix task, has its own unique ID). **Archiving** it means
  moving its contents, except earlier `attempt-*` folders, into
  `.tdd-runs/T<NN>/attempt-<k>/` (the next free `k`), and moving the task's report
  `T<NN>-<slug>.report.md` in there too. Then, in every `BLOCKERS.md` entry that links
  into the moved files, rewrite those paths to their `attempt-<k>/` location. This leaves
  no top-level `state.md`, so the next run is a fresh start. It holds the test-guard manifest, the
  snapshot copies of guarded files, and the command logs. Create it at the start. If the
  repo isn't ignoring it, suggest adding `.tdd-runs/` to `.gitignore` (don't edit
  `.gitignore` unasked).
- Set the task file's `Status` to `in-progress` (and its row in `INDEX.md`, if present).

## Task state and resuming

Keep `run-dir/state.md` current. It must always let a fresh session continue safely.
Fields:
- phase and step
- `unreviewed` and `spec-amended`
- Phase 3 pass count, Phase 4b round count, Phase 6 pass count and restart count, Phase 7
  cycle count
- `phase5-baseline taken: yes/no`
- commits made (SHAs)

Write it **before** every delegation and at every phase change. In Phase 7, set
`unreviewed: true` in it *before* delegating to the implementer, not after.

**Resuming.** If `run-dir/state.md` already exists when the skill starts, this is a
resume, not a fresh start.
- **Never re-create** `pre-run/`, `pre-run-status.txt`, `baseline.log`, `matrix.md`,
  `locked/`, `manifest.sha256`, `phase5-baseline/`, or `reviewed/` when they exist.
- Any file that differs from its `pre-run/` copy, or from `HEAD` when it has no `pre-run/`
  copy, is **this task's work**, never the user's.
- Always redo Phase 0's reading steps (1–3, 5). Do not re-run the baseline if it exists.
- If `manifest.sha256` exists, run the guard check before anything else.
- Then continue from the recorded phase. Counts carry over from `state.md`.

| Recorded phase | Resume at |
|---|---|
| 0–1 | Phase 1. |
| 2–3 | Delegate the test author to complete or correct the existing test files against `matrix.md`. Then Phase 3 from pass 1. |
| 4 | 4a only if the manifest is missing, then 4b. |
| 5 | If `phase5-baseline taken` is not `yes`, build both baselines from `pre-run/` or `git show HEAD:<path>`, **never from the working tree**, then mark it taken. Re-delegate the implementer to finish (tell it the code may be partly written). Then Phase 6. |
| 6 | Restart Phase 6 at pass 1. This counts as a restart. |
| 7 | Set `unreviewed: true` (the last code change may never have been reviewed). Go to step 1. |
| 8–9 | Redo Phase 8. Check `state.md` and `git log` for commits already made before committing anything. |

## Phase 0 — Understand

1. Read the **entire task file**, top to bottom, before anything else. Then read every
   dependency task file's `Interfaces` section, the source-plan section it cites, and
   every file under `Context` and `Likely Files`.
2. **Dependency check:** every task in `Depends on` must have `Status: done`. If one
   doesn't, stop and tell the user. Never build on an unfinished dependency.
3. Read the existing code the task touches and the repo's test conventions: framework,
   file location and naming globs, fixtures, test-runner config files, how mocks are
   done here.
4. On a fresh start, run the full suite once and save the output to
   `run-dir/baseline.log`. Every test already failing here must be classified before
   going on:
   - **Accepted failure:**
     - without `--run-baseline`: any failure unrelated to this task
     - with it: a failure that also fails in the run baseline, or is listed in
       `--known-failures`

     Record it in `run-dir/accepted-failures.txt`. It's not this task's to fix. It's
     excluded from "all tests pass", and the report lists it.
   - **Target failure:** listed in `--target-failures`. This takes precedence over
     "accepted" when a test is in both lists. Fixing it is this task's job. It
     is not accepted and not excluded. It counts as one of this task's tests: it should
     fail for the right reason in 4b and must pass by Phase 8.
   - **Unknown failure** (only possible with `--run-baseline`): something broken earlier
     in the plan run that nobody has accepted. **Stop before Phase 1.** Report the
     failures to the user (or the orchestrator). **Archive the run directory** and set
     the task's `Status` back to `todo`, so the next attempt starts fresh against the
     tree as it is then. Never start on top of an unknown failure.

   Do not run this skill on two tasks in the same working
   tree at once. Each run's deliberately failing tests would corrupt the other's
   baseline and results (parallel runs need separate git worktrees).
5. Write a **working summary** (shown to the user):
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
- **Stubs are requested:** for each interface in the task's `Interfaces` section that
  the task creates and that doesn't exist yet, create a minimal stub. Use the exact
  signature, with a body that only raises or returns "not implemented". This makes
  tests fail on assertions rather than imports. No logic in stubs. (Omit this point if
  the task creates no new interfaces.)
- Return: the matrix, the test files written, the stub files written, the self-check
  output, and any spec gaps.

Save the returned matrix to `run-dir/matrix.md`, and keep it in sync after every fix.

## Phase 3 — Review the tests (three passes, then verify)

Run three review passes **in order**, each a fresh `tdd-test-reviewer` invocation with one
focus. Include the task file path, the matrix, the test file paths, and the author's
latest self-check output. After each pass, send its blocking findings to
`tdd-test-author` to fix (findings verbatim, stub fixes allowed), then start the next
pass on the fixed tests.

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
has no blocking findings.

**Verification passes:** if any of the three passes was blocking, the fixes made after
it haven't been checked against their own focus yet. Run a **verification pass** with
**all three focuses**, listing the earlier findings so the reviewer confirms each one is
fixed. Repeat (fix, then verify) until a verification pass is clean. The phase is done
when the last pass is clean and no fix has happened since. **Cap: 5 passes total**,
then follow the cap rule.

## Phase 4 — Lock the tests and confirm they fail

**4a. Lock (the test guard).** The guard protects **every** source file that decides
test outcomes, not only this task's tests. It has two parts.

1. **Guarded files**, hashed whole:
   - this task's test files
   - every existing test file
   - test-only config (`pytest.ini`, `conftest.py`, `jest.config.*`, `vitest.config.*`,
     `setupTests.*`, `.mocharc.*`, and so on)
   - shared fixtures and test helpers
   - committed snapshot or golden files

   Write the globs to `run-dir/guard-globs.txt`. Globs name **source and data
   extensions** (for example `tests/**/*.py`, `**/*.test.ts`, `**/__snapshots__/*.snap`),
   never bare directories. Expand them only over tracked plus untracked-but-not-ignored
   files: `git ls-files -co --exclude-standard`, or without git, `find` with caches
   excluded. Always exclude generated output: `__pycache__`, `.pytest_cache`,
   `node_modules`, coverage, build directories, and `.tdd-runs/`.

   Hash every match into `run-dir/manifest.sha256` with `sha256sum` (or
   `shasum -a 256`). Copy each into `run-dir/locked/`, keeping its relative path.
2. **Mixed config files**, watched by section. These are files that hold test settings
   alongside other settings the task may legitimately need to change (dependencies,
   scripts), such as `package.json`, `pyproject.toml`, `setup.cfg`, `tox.ini`,
   `Cargo.toml`. List each in `run-dir/mixed-config.txt` with its test sections (for
   example `[tool.pytest.*]`, `[tool.coverage.*]`, the `"jest"` key, the `test` script).
   Copy each into `run-dir/locked/`.

From now on, a guarded file or a test section of a mixed config file may change **only**
through the test-change procedure below.

Run tests in **non-writing mode** where the framework has one (for example `jest --ci`),
and never pass a snapshot-update flag. A test run must never create or update
snapshots. Expected snapshots are authored by the test author before the lock.

**4b. Confirm they fail.** Run the task's test command and save the output to
`run-dir/red.log`. Classify every test:

- **Fails for the right reason:** an assertion failure, or the stub's not-implemented
  error. Expected.
- **Fails for the wrong reason:** a syntax error, a bad import of existing code, broken
  fixture or setup, or a missing test dependency. Also any `regression`-kind test that
  fails: either the test or your understanding of existing behavior is wrong, so check
  it against `baseline.log`. The test is broken.
- **Passes:** allowed only for a `regression`-kind test that guards existing behavior.
  Any other passing test is meaningless or tests the wrong thing.

Send wrong-reason and wrongly passing tests back to the test author. Run a
verification pass (all focuses) on the changes. If it's blocking, fix and verify again
within the same round. Then lock again (4a) and run 4b again. **Cap: 3 rounds**, and
at most 3 verification passes within one round. Hitting either follows the cap rule.
Proceed only when every non-regression test fails for the right reason and every
regression test passes. With `--commit split`, commit the tests and stubs now.

## Phase 5 — Write the code (implementer)

Delegate to a **new** `tdd-implementer`. The prompt states:

- Implement the task file's spec. The locked tests are the spec made executable.
- Read the tests, but **never create, edit, rename, delete, skip, or disable any test file,
  fixture, or test config**.
- Do not special-case test inputs, detect the test environment, or hardcode expected
  values. The code must be correct for inputs the tests don't use.
- Replace the stubs with real implementations and follow existing codebase patterns.
- **Do not run the test suite in this phase or Phase 6.** The tests run after the code
  passes review (Phase 7). A build, typecheck, or lint is allowed.
- If it believes a test contradicts the spec, it must **stop and report** the test, the
  spec text, and why. It does not work around it. (Handle per "Spec questions".)
- Return: the files changed, a summary of the design, the build/typecheck result, and any
  suspected test or spec conflicts.

**Review diff.** Before the first delegation in this phase, unless `state.md` says
`phase5-baseline taken: yes`, copy every production file the task may touch (the
`Likely Files` plus the stubs) into `run-dir/reviewed/`, and also into
`run-dir/phase5-baseline/`, which is never refreshed. Then record
`phase5-baseline taken: yes`. `run-dir/reviewed/` is
the reviewed baseline. The review diff is the difference between `run-dir/reviewed/` and
the working tree, for every non-guarded file the implementer reports changing (also
check `git status --porcelain` when in git). Produce it with
`git diff --no-index -- run-dir/reviewed/<path> <path>` or `diff -u`. For a changed file
with no baseline copy, take its pre-change version from `run-dir/pre-run/` if it's there
(the user's version), otherwise from `git show HEAD:<path>` if it's tracked, and copy that
into both `run-dir/reviewed/` and `run-dir/phase5-baseline/`. If neither exists, it's a new file: include its full content.

The baseline is refreshed (overwritten with the current versions of those files) only
at two points: when Phase 6 finishes clean, and after each clean review in Phase 7
step 3. **Never** refresh it between Phase 6 passes. Every Phase 6 pass, verification
passes included, reviews the whole implementation against the Phase 5 baseline.

**Guard check, after every implementer invocation (here and in Phases 6–7):**
1. **Guarded files:** re-expand `guard-globs.txt` (same filters as 4a), recompute the
   hashes, and diff against `manifest.sha256`. A changed or deleted file is a
   violation. So is a **new** match, if the implementer's own file list or the
   timestamps show it created the file. A file produced by one of your own test runs is
   not a violation. Right after each of your runs, record the hashes of any new guard
   matches in `run-dir/post-run.sha256` (never in `manifest.sha256`, which only 4a and the
   test-change procedure update). Investigate each one instead of assuming it's harmless.
   Phase 8 requires every new match to be explained (generated output that the guard
   globs should exclude, then excluded) or quarantined.
2. **Mixed config files:** diff each against its copy in `run-dir/locked/`. A change
   inside a listed test section is a violation. Other changes (for example adding a
   dependency) are allowed. Log them and include them in the review diff.
3. On any violation: restore the guarded file or the test section from
   `run-dir/locked/`. Move (never delete) an implementer-created new match into
   `run-dir/quarantine/`. Log the incident for the report, and re-delegate with a
   reminder of the rule.

## Phase 6 — Review the code (three passes, then verify)

Three passes **in order**, each a fresh `tdd-code-reviewer` invocation with one focus.
Include the task file path, the locked test paths, and the review diff. After each pass,
send its blocking findings to `tdd-implementer` to fix (guard check afterward), then start
the next pass on the fixed code.

1. **Matches the spec and is correct:** every AC is implemented as specified, with
   correct logic and correct interfaces (exact signatures and errors). Nothing outside
   the scope.
2. **Robust:** error handling, edge cases and boundaries, input validation, resource
   cleanup, concurrency where relevant, and security (injection, authorization, secrets,
   unsafe deserialization).
3. **Quality and test-gaming:** consistent with codebase patterns, readable, no dead
   code or duplication, no needless complexity. **No special-casing of test inputs, no
   hardcoded expected values, no test-environment detection.**

The verification-pass rule, the clean/blocking rules and the **5-pass cap** are the same
as Phase 3 (verification passes cover all three code focuses). A **restart** (after a
spec or test change) resets the pass count to zero. Restarts have their own cap of
**2**, and a third restart follows the cap rule. Reviewers do not run or
modify tests. They review code as written.

## Phase 7 — Test, fix, review loop

Keep one flag, **`unreviewed`**:
- It starts `false` only if Phase 6 actually finished with a clean pass and nothing
  changed afterwards. Otherwise go back to Phase 6.
- It becomes `true` whenever the implementer changes code.
- It becomes `false` only when a code review of those changes comes back clean.

Repeat. **Cap: 5 cycles** (one cycle = one run of step 1).

1. **Run** the task's tests and then the full suite. Save the output to
   `run-dir/cycle-<n>.log`.
2. **If anything fails** (not counting the tests in `accepted-failures.txt`),
   diagnose each failure before changing anything. Read the failure, the test, and the
   spec. Decide which case it is:
   - **The code is wrong** (the default assumption). Delegate to `tdd-implementer` with
     the failure output, the test name, and the AC it checks. The implementer may run
     the failing tests from now on. The fix must make the code do what the feature should
     do, not merely satisfy the assertion. Run the guard check. Set `unreviewed`.
   - **The test contradicts the spec.** Use the test-change procedure. Never edit the
     test to fit the code.
   - **The spec is ambiguous or contradictory.** Ask the user, record the answer in the
     task file, then apply it through whichever case it implies.
   - **A regression in another part of the suite.** Treat it as "the code is wrong",
     unless the task's spec explicitly changes that behavior, in which case it's a test
     change.

   Then go back to step 1.
3. **If everything passes and `unreviewed` is set**, run a `tdd-code-reviewer` pass with
   all three focuses, scoped to the review diff (the changes since the last clean
   review). In **spec-amended** mode, review the **whole implementation** instead,
   diffed against `run-dir/phase5-baseline/`, and give the reviewer
   `spec-amendments.md` so it checks the code against each amended item.
   - If it's clean, clear `unreviewed` (and spec-amended mode) and go to step 4.
     Nothing has changed since the passing run.
   - If it's blocking, delegate the fixes to `tdd-implementer` (run the guard check,
     keep `unreviewed` set) and go back to step 1. Modified code always gets its tests
     run again.
4. **Exit to Phase 8** when everything passes and `unreviewed` is clear. That means
   every code change since the last full run has been reviewed clean, and the run came
   after the last change.

### Test-change procedure (the only way a guarded file changes)

1. You (the orchestrator) write down which test is wrong or missing, the spec text
   involved, and why. "The code doesn't do this" is never a reason. Name **every guarded
   file** the change needs: tests, fixtures, helpers, test sections of mixed config
   files.
2. If the right behavior isn't obvious from the spec, ask the user.
3. Delegate the change to `tdd-test-author`, then run a `tdd-test-reviewer`
   verification pass (all three focuses) on the changed files. If it's blocking, fix
   and verify again (at most 3 passes, then the cap rule).
4. Before locking again, diff the guard against the manifest and the mixed-config
   copies. Only the guarded files named in step 1 may have changed. Any other change is an
   incident: restore it and log it. Also check the changed tests for real skip or
   only-marker syntax (`@pytest.mark.skip`, `pytest.skip(`, `it.skip(`, `describe.skip(`,
   `.only(`, `xit(`, `xdescribe(`, `t.Skip(`, or the framework's equivalent). Any such
   marker is rejected.
5. Lock again (4a: update the manifest and `run-dir/locked/`). Log the change (test,
   reason, before/after summary) for the report.
6. Return to where the procedure was entered:
   - **From Phase 4b** (after the lock): go back to the start of 4b.
   - **From Phase 5:** resume Phase 5. Re-delegate the implementer with the changed tests.
   - **From Phase 6:** delegate the implementer to bring the code in line with the
     changed tests (guard check), then restart Phase 6 at pass 1.
   - **From Phase 7:** go to step 1, so the tests rerun against the changed tests. The
     loop's exit still requires `unreviewed` to be clear.

## Phase 8 — Integrity check

All of the following must hold, otherwise return to Phase 7 (this counts against
Phase 7's cycle cap):

- The guard hashes match the final manifest. Every new match in `post-run.sha256`
  or from the implementer is explained or quarantined. The test
  sections of mixed config files match their locked copies. Every manifest change has a
  logged test change behind it.
- No skip or only-marker syntax (as listed in the test-change procedure) in the task's
  test files. No test file was deleted.
- Every `TC-n` and every row of the final matrix exists as a test, and every one passes.
  So does every test in `--target-failures`.
- The full suite passes apart from the tests in `accepted-failures.txt`.
- `unreviewed` is clear.
- The task's `Definition of Done` checklist is satisfied, item by item.

With `--commit single`, commit the production code and tests now. With `--commit split`,
commit the production code plus any test files changed after the first commit. Never
commit the run directory.

## Phase 9 — Report

Write `<task-dir>/T<NN>-<slug>.report.md` with these sections:

- **Summary:** status, files changed, commit SHAs or "not committed" (with the reason
  if a commit was skipped).
- **Clarifications:** the questions asked and the answers, including spec questions
  raised by agents.
- **Test matrix:** the final matrix with pass status.
- **Test review:** findings per pass and how each was resolved.
- **Failure check:** the classification from Phase 4b, with the number of rounds.
- **Code review:** findings per pass and how each was resolved.
- **Test-fix cycles:** the number of cycles, with the failures, diagnoses and reviews
  for each.
- **Test changes and guard incidents:** each change with its reason, quarantined files,
  and allowed mixed-config changes (for example new dependencies), or "none".
- **Accepted suite failures:** from `accepted-failures.txt`, with their sources, or "none".
- **Caps hit and decisions:** or "none".
- **Remaining risks / follow-ups.**

Set the task's `Status` to `done` (or `blocked`, with its blocker ID) in both the task
file and `INDEX.md`. In unattended mode, also list every `Assumed (unattended)` decision
under **Clarifications**, so a human can review them later. Tell the user the result in a
few lines and link the report.

## Hard rules

- The orchestrator never writes tests or production code. It delegates.
- The test author never reads the implementation of the code under change. The
  implementer never edits a guarded file.
- Never weaken, skip, or delete a test to get to green. A failing test is evidence. Fix
  the code, or change the test only through the test-change procedure.
- The task is never marked `done` while any test fails (apart from recorded
  accepted failures) or any code change is unreviewed.
- Report results exactly as they are. If tests fail, say so with the output.
- In unattended mode, never wait on the user, and never guess past the low-risk test.
  Anything that fails it is a fully documented blocker, not an assumption.
