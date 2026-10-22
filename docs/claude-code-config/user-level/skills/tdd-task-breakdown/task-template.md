# T<NN> — <Title: one behavioral outcome, no "and">

- **Status:** todo <!-- todo | in-progress | blocked (B-NN or dependency T<NN> blocked) | done | superseded (by T<NN>, T<NN>) -->
- **Depends on:** <T-IDs, or "none">
- **Covers requirements:** <R-IDs from INDEX.md>
- **Source plan:** <relative path to plan, section anchor>

## Goal

<One or two sentences: what observable behavior exists when this task is done, and why
it matters.>

## Context

<What a fresh agent needs to know: the relevant part of the plan, the existing code it
builds on (paths), the domain rules, and the decisions already made. Link files, don't
paste large blocks.>

## Scope

**In scope**
- <behavior / file / component>

**Out of scope**
- <behavior a reader might assume is included but belongs to another task (name it) or to
  nobody>

## Interfaces

<Every public interface this task creates, changes, or uses: exact name, signature,
parameter and return types, errors/exceptions raised and when, side effects (I/O,
persistence, events). For interfaces from a dependency, write "from T<NN>:" and restate
it identically.>

## Acceptance Criteria

- **AC-1:** Given <precondition>, when <action through public interface>, then
  <observable outcome>.
- **AC-2:** ...

## Required Test Cases

The minimum set. The test author adds more. Kinds: positive · negative · edge · error ·
regression.

| ID | Covers | Kind | Case | Expected |
|----|--------|------|------|----------|
| TC-1 | AC-1 | positive | <input / situation> | <exact observable result> |
| TC-2 | AC-1 | negative | <invalid input> | <rejection: error type / message / status> |

## Likely Files

- Create: `<path>`
- Modify: `<path>`
- Tests: `<path following repo convention>`

## Test Commands

- This task's tests: `<exact command>`
- Full suite: `<exact command>`

## Definition of Done

- [ ] Every AC is covered by at least one passing test; every TC above exists.
- [ ] Guarded test files and test config are unmodified, or every change is justified in
      the run report.
- [ ] The full suite passes (no regressions).
- [ ] Code review (three passes plus any verification passes) is clean.
- [ ] <task-specific item, e.g. "migration is reversible">

## Open Questions

<Non-blocking questions, each with the assumption made: "Q: … — Assumed: …". Write
"None" if empty.>
