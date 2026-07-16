---
name: rate-claim
description: Record-only mock VA adjudication of the va-disability mental-health claim corpus — intake → C&P examiner → RVSR → adversarial reviewer over the markdown evidence in va-disability/supporting-docs/, producing a dated, citation-anchored rating report in va-disability/ratings/ where every finding carries a suggested remediation. Judges the highest defensible rating under 38 C.F.R. § 4.130. For strategy, odds, or legal-research questions use /va-rating-reassess instead — this skill sees ONLY what the VA would see.
disable-model-invocation: true
---

# /rate-claim — Mock VA Adjudication Harness

Emulates the VA's own process on the evidence record as it stands today:
a C&P examiner fills the DBQ, an RVSR writes a rating decision, a denial-minded
reviewer attacks it. The value of this skill is **blindness** — roles 2–4 see only
the rated record + the law, never strategy material. Spec:
`docs/superpowers/specs/2026-07-15-va-claim-corpus-judgment-design.md`.

## Preconditions — stop immediately if any fails

1. `va-disability/rater-kb/README.md` contains `STATUS: KB COMPLETE`. If not:
   stop — "the knowledge base is unbuilt/unverified; no improvised law."
2. `va-disability/supporting-docs/` contains at least one `.md` evidence file.
   If not: stop with instructions to populate it.
3. This run was explicitly requested by the user in this conversation. Never
   auto-run.

## Corpus rules

- The **markdown files** in `va-disability/supporting-docs/` are the rated
  record's text — faithful, unmodified conversions of the pdf/docx/pages
  originals, made for AI analysis.
- The co-located **originals are authoritative**: consult one when a transcript
  is ambiguous or suspect; **on any discrepancy the original controls**, and the
  discrepancy is reported so the conversion gets fixed.
- `personal-records/` (gitignored PHI) is a fallback source ONLY for evidence
  with no copy in `supporting-docs/` at all. Never copy its contents into
  tracked files.

## Stage 1 — Intake (run in the main thread)

1. List `supporting-docs/`. Pair each markdown with its original (pdf/docx/pages)
   where one exists. An original with **no** markdown counterpart gets
   transcribed now (`textutil -convert txt` for docx, `pdftotext` for PDFs,
   AppleScript Pages export for `.pages`, OCR fallback for scans), saved as a
   sibling `.md`, and a provenance row appended to
   `va-disability/DOCUMENT-PROVENANCE.md` per its conventions. If a transcript
   exists but its original is newer (mtime), flag the pair for original-check
   during examination. Unreadable files: flag `NEEDS-ATTENTION`, list in the
   report — never silently skip.
2. **Evidence-of-record classification (first job):** for every document,
   determine from `DOCUMENT-PROVENANCE.md` whether it is (a) the signed/filed
   instrument, (b) a superseded draft, or (c) unsubmitted material. Only (a) —
   plus unsigned records that reach the VA another way (treatment records) —
   enters the rated record. Multiple versions of one instrument resolve to the
   filed one; the rest are excluded. Unresolvable → flagged, excluded, listed in
   the report with the reason, and the user is prompted to resolve provenance.
   Never silently dropped, never silently included.
3. Output: the **rated-record file list** (exact paths) + the exclusions list.
   If the rated record is empty, stop and report why every candidate was
   excluded.

## Stage 2 — Consistency sweep

Dispatch the **claim-consistency-checker** agent scoped to the rated-record file
list only. Keep **substantive** findings: contradictions in diagnoses, symptom
reports, employment/functional status, treatment history, stressor accounts.
Clerical errors (DOB typos, name spellings, phone slips, grammar) carry no
weight — collapse them to a single errata footnote.

## Stage 3 — C&P examiner (subagent)

Dispatch one subagent with: the rated-record file list, the Stage 2 substantive
findings, the five `rater-kb/` files, and these instructions:

> You are a VA C&P mental-health examiner. Read ONLY the files listed — you have
> no other case knowledge. Contentions: PTSD (MST stressor) with comorbid MDD,
> GAD, OCD; SUD claimed secondary to the MH conditions. Complete the Mental
> Disorders/Initial PTSD DBQ structure in `rater-kb/dbq-mental-disorders.md`,
> including ONE occupational/social-impairment checkbox selection. HARD RULES:
> (1) every endorsement cites document + section — no uncited endorsements;
> (2) substance only — clerical errors carry no weight; (3) where the record is
> silent, say "record silent," never infer; (4) apply
> `rater-kb/mst-adjudication.md` for stressor-marker analysis; (5) note where a
> live interview would be required — you cannot conduct one.

## Stage 4 — RVSR rating (subagent)

Dispatch a second subagent with: the rated-record list, the filled DBQ, the five
KB files, `report-template.md`, and these instructions:

> You are a VA Rating Veterans Service Representative. Using
> `rater-kb/rating-procedure.md` and `rater-kb/criteria-4130-caselaw.md`, weigh
> the evidence (lay competence/credibility, self-report-instrument caveats,
> benefit of the doubt under § 3.102) and assign the **highest defensible
> rating** — 0/10/30/50/70/100 exactly as the evidence supports, no target.
> Fill every section of the report template. HARD RULES: citation-anchor every
> criterion found met; substance only; every weakness/gap you record must carry
> a remediation per the template's Findings-and-remediations section — a
> remediation PATH (obtain a record, request a provider addendum, resolve
> provenance, witness reconciles in their own words), NEVER drafted wording for
> any witness statement. Note (don't adjudicate) TDIU/SMC implications.

## Stage 5 — Adversarial review (subagent)

Dispatch a third subagent with the draft report, the rated-record list, and
`rater-kb/denial-patterns.md`:

> You are a skeptical, denial-minded VA reviewer. Attack the assigned rating:
> evidence weight, criteria fit, nexus sufficiency, substantive credibility.
> Clerical defects are NOT valid attack paths. For each attack: the argument,
> the evidence it rests on, whether it survives scrutiny. Try to knock the
> rating down a level — honestly.

Append sustained attacks to the report, ranked by severity, each with a
remediation row. The RVSR's rating stands, annotated.

## Stage 6 — Assemble and save

- Fill `Delta vs. previous run` by diffing against the newest existing report in
  `va-disability/ratings/` ("First run — no prior report" if none).
- Save as `va-disability/ratings/YYYY-MM-DD-rating-report.md` (today's date; if
  a report already exists for today, suffix `-2`, `-3`, …).
- Surface ALL consistency findings in the report even if the examiner judged
  them explainable. Verify no orphan findings (every issue has a remediation or
  an explicit accept-and-mitigate). Tell the user the assigned rating, the top 3
  remediations by rating impact, and the record-completeness caveat.

## Blindness rule (hard — stages 3–5)

Roles receive **explicit file lists, never directory access**. Prohibited:
`planning-docs/`, `COMPREHENSIVE-FINDINGS-*`, `CLAIM-ASSESSMENT.md`,
`document-analysis/`, exam-prep and nexus-letter-guide material, `ratings/`
(prior reports), and anything else outside the rated record + `rater-kb/` (the
KB is law/procedure, not case strategy). Strategy material contaminates the
emulation and inflates the score.

## Ethics guardrails (identical in force to /va-rating-reassess)

- The objective is the maximum rating the veteran's genuine conditions
  legitimately support. Never advise fabricating, exaggerating, or
  misrepresenting conditions, symptoms, or history (38 U.S.C. § 6103;
  18 U.S.C. § 1001).
- **Never coach witness evidence.** Identify credibility risks and hand them
  back; resolution belongs to the veteran and the actual witness in their own
  unedited words.
- Reports close with: research assistance, not legal or medical advice; consult
  an accredited VSO or VA-accredited attorney before acting.

## First-run acceptance test (do this once, when the user authorizes the first run)

After Stage 6, diff the examiner's blind credibility findings against the newest
`COMPREHENSIVE-FINDINGS-*.md`. The corpus contains known substantive issues (the
opioid-origin claim contradicted by clinical records; the Reyes unit/DD-214
mismatch affecting corroborative weight). If the blind examiner failed to
rediscover them, say so plainly, revise the Stage 3 prompt, and re-run before
trusting the score. Clerical defects are not part of this pass/fail bar.
