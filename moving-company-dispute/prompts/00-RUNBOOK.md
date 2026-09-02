# Runbook — Moving Company Dispute (Coastal Moving / Rapid Express)

Three prompts, run **in order**, each in a **fresh session**. Do not merge them.

| Phase | Prompt file                      | Reads                           | Writes                    | Gate to clear before next phase                                    |
| ----- | -------------------------------- | ------------------------------- | ------------------------- | ------------------------------------------------------------------ |
| 1     | `phase-1-evidence-extraction.md` | Gmail + attachments             | `evidence/FACT-LEDGER.md` | You read the ledger and confirm nothing material is missing/wrong  |
| 2     | `phase-2-legal-analysis.md`      | `evidence/FACT-LEDGER.md` + law | `REPORT.md`               | Every citation passes `citation-verifier`; you accept the theories |
| 3     | `phase-3-action-drafts.md`       | Ledger + `REPORT.md`            | `drafts/*.md`             | —                                                                  |

## Before Phase 1

Fill in the `<case_facts>` block at the top of `phase-1-evidence-extraction.md`. The
interstate-vs-intrastate answer is the single biggest fork in the analysis — if the move
crossed a state line, federal law (Carmack Amendment, 49 CFR Parts 371/375) governs and
largely displaces state-law claims **against the carrier**; if it did not, state utility /
motor-carrier regulators govern instead. Phase 2 is instructed to derive this from the
documents rather than trust your answer, but supplying it lets it flag a conflict.

## Why the phases are separated

Phase 1 forbids legal conclusions. This is deliberate: on document-heavy legal work the
dominant failure mode is the model forming a theory from the first two emails and then
reading the remaining documents to confirm it — skimming past the clause that actually
decides the case. Separating extraction from analysis, with a human gate between, prevents it.

## Non-negotiable rules baked into every phase

- **Attachment gate.** If the run cannot retrieve the actual bytes of every attachment, it
  must stop and hand you a precise download list. It must never reason from a filename.
- **Quote-before-conclude.** No factual assertion without a verbatim quote and a source ID.
- **`NOT IN RECORD`.** Missing facts get that literal marker. Never an inference dressed as a fact.
- **Citation verification.** Every statute, regulation, and case is verified against the
  primary source before it is relied on. This repo has a documented history of 40-of-109
  misstated citations in a prior legal research pass; treat unverified cites as wrong.

## Deadline warning

Several clocks may already be running (cargo-damage claim windows, chargeback windows,
state consumer-protection limitation periods). Phase 2 produces a deadline table as its
**first** output section for exactly this reason. If you only read one part of the report,
read that.

## Scope note

These prompts produce research, correspondence drafts, and complaint-filing packets. They
do not produce legal advice and no phase should claim to. Retaining a lawyer licensed in
the relevant state is listed as an option in Phase 2's recourse ranking, not an afterthought.
