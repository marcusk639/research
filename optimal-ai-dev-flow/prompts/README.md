# Research Prompts — Solo Consultant Operating System

Three-phase split of `../solo-consultant-workflow-optimized.md` (the original combined prompt,
kept as the canonical source of the design).

## Run order

| Phase | File                   | Consumes                     | Produces                            | Web                          |
| ----- | ---------------------- | ---------------------------- | ----------------------------------- | ---------------------------- |
| A     | `phase-a-ledger.md`    | the six corpus docs in `../` | `../corpus-ledger.md`               | no                           |
| B     | `phase-b-research.md`  | `../corpus-ledger.md`        | `../findings/w1..w9-*.md`           | yes                          |
| C     | `phase-c-synthesis.md` | ledger + findings            | `../REPORT.md`, `../playbooks/*.md` | only to close a blocking gap |

**Check the ledger yourself between A and B.** That is the point of the split — every downstream
conclusion inherits Phase A's extraction, and an error there is invisible inside a 20k-word
report. The ledger is short enough to read in ten minutes.

## Why split at all

Not for input size — 306 lines is a normal driver prompt. For **output volume**: 11 deliverables
including six templated playbooks is realistically 15–25k words, and quality degrades
monotonically across a single pass. The back half of a deliverable list is where it shows, and
the consulting half (W6–W8) sits exactly there.

## Handoff contract

Phase A assigns every extracted claim a stable ID (`C-001`, …) and a workstream. Phase B returns
a verdict per ID. Phase C merges. **Never renumber claim IDs** — the later phases address claims
by ID, and renumbering silently breaks the chain.

## Split trigger for Phase C

Run Phase C as one pass. If the playbooks come back as **prose paragraphs instead of filled
templates** — missing entry criteria, artifacts, time-box, or exit test — re-run as two passes:

- **C1** — deliverables 1–3 and 8–11 (the report)
- **C2** — deliverables 4–7 (the playbooks), with C1 output as input

Split on that observed symptom, not on speculation.

## Downstream

The playbooks are the durable output. Two of them are skill candidates once they exist —
`domain-rampup.md` and `process-diagnosis.md` are procedures that run every engagement, which is
what makes a skill worth building. Build those _from_ the research; don't build a skill to
execute the research.
