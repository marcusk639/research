<!--
Blocker entry format. The file holding these entries is <tasks-dir>/BLOCKERS.md. If it
doesn't exist, create it with this header:

  # Blockers

  Each entry is written as a task: everything a person or the tdd-blocker-resolver
  agent needs to pick it up cold. Status: open | resolving | resolved | needs-human.
  To unblock a needs-human entry, fill in its "Decision" section and rerun
  `claude --agent tdd-blocker-resolver "<tasks-dir>"`.

Append each new entry at the end. IDs are B-01, B-02, … (the next free number). Never
delete entries: resolved ones stay as history. Tasks blocked only because a dependency
is blocked do NOT get their own entry. They're listed under "Blocks" on the root entry.
-->

## B-<NN> — <one-line summary of what is blocked and why>

- **Status:** open <!-- open | resolving | resolved | needs-human -->
- **Task:** T<NN> — <task title> · **Phase:** <phase and step where it stopped>
- **Type:** <cap-hit | spec-question | test-spec-conflict | earlier-failure | environment | orphaned-work | other>
- **Opened:** <ISO time> by <tdd-implement-task | tdd-orchestrator | tdd-blocker-resolver>
- **Blocks:** <task IDs blocked through this one, or "none"> · **Unmet requirements:** <R-IDs>

### What was being attempted

<The task's goal and the specific step in progress, in plain words. Enough that a reader
who has never seen the run understands what "done" would have looked like.>

### What happened

<The facts, without interpretation:
- failing tests with their key assertion messages
- open review findings
- the question that couldn't be answered
- error output

Link the evidence by path, for example `.tdd-runs/T<NN>/cycle-4.log`,
`T<NN>-<slug>.report.md`, review findings.>

### Root-cause hypothesis

<Best explanation, with a confidence of high, medium or low, and the evidence for it.
List the plausible alternatives you couldn't rule out.>

### State of the work

- Partial work: <set aside in `.tdd-runs/T<NN>/set-aside/` (patch + files) | left in the
  tree: <files> | none>
- Commits: <reverted: <SHAs> | not reverted: <SHAs> (why) | none>
- Known failures added to the run: <test IDs | none>
- Suite after set-aside: <matches the task's baseline | differs: <details>>

### Suggested fixes (ranked)

1. **<short name>**
   - Steps: <concrete steps>
   - Tradeoffs: <tradeoffs>
   - Risk: <low | medium | high>
   - Needs a human decision: <yes | no>
2. **<short name>**
   - …

### To unblock

<What exactly is needed: a decision, information, an environment change, or another
attempt with a different strategy. If it's a decision, give the exact question, the
options, and a recommendation with its reason.>

### Decision (filled in by a human)

_None yet._

### Attempts

| # | When | By | Strategy | Outcome | Evidence |
|---|------|----|----------|---------|----------|
| 1 | <ISO time> | tdd-implement-task | original run | blocked at <phase> | `.tdd-runs/T<NN>/…` |
