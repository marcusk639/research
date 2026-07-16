# VA Claim Corpus Judgment Harness — Design

**Date:** 2026-07-15 (revised same day after plan review)
**Status:** Approved design, pending implementation plan
**Subject:** `va-disability/`

## Purpose

Build a re-runnable harness (`/rate-claim` project skill) that judges the evidence
record supporting Marcus's PTSD/MST claim (with MDD, GAD, OCD, and SUD) the way the
VA itself would: a mock C&P examination followed by a mock rating decision,
producing the **highest defensible rating** the evidence supports, plus
strengths/weaknesses, per-document helps/hurts, and a gap list toward the
next-higher rating.

The harness is built now but **not executed** until the user says go (records are
still being added to the corpus).

**Relationship to existing tools:** this is record-only mock adjudication — the
rater sees only what the VA would see. For strategy questions, odds re-scoring, or
legal research against the full case file, use `/va-rating-reassess`. Nothing else
in the repo emulates an adjudicator blind to strategy material; that blindness is
this harness's entire value.

## Decisions made during brainstorming and plan review

| Decision           | Choice                                                                                                                                                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rating target      | **Highest defensible** — the mock rater assigns 0/10/30/50/70/100 exactly as the evidence supports                                                                                                                            |
| Corpus             | The **markdown files** in `va-disability/supporting-docs/` — the source of the bulk of what was/will be submitted to the VA for the MH claims                                                                                 |
| Originals          | PDF/docx/pages originals co-located in `supporting-docs/` are **reference material** — consulted when a transcript is ambiguous, suspect, or missing; intake transcribes an original only when it has no markdown counterpart |
| Manifest           | Reuse `DOCUMENT-PROVENANCE.md` as the classification source of truth — no parallel manifest file                                                                                                                              |
| Deliverable shape  | Re-runnable project skill (`/rate-claim`); dated reports enable baseline → final comparison                                                                                                                                   |
| Examiner knowledge | One-time deep-research pass → static, citation-verified knowledge base in `va-disability/rater-kb/`                                                                                                                           |
| Architecture       | Intake → examiner → rater pipeline **plus** an adversarial denial-minded reviewer as a fourth stage                                                                                                                           |

## Directory layout (matches the 2026-07-15 reorganization — nothing new except `rater-kb/` and `ratings/`)

```
va-disability/
  supporting-docs/          # THE CORPUS: markdown transcripts (primary) + pdf/docx/pages
                            # originals (reference — consulted if possible and necessary)
  personal-records/         # gitignored signed PHI originals — fallback source only, for
                            # evidence documents with no copy in supporting-docs at all
  DOCUMENT-PROVENANCE.md    # existing provenance log — intake's classification source of truth
  rater-kb/                 # NEW: static rater-emulation knowledge base (5 files, below)
  ratings/                  # NEW: dated run outputs: YYYY-MM-DD-rating-report.md
.claude/skills/rate-claim/  # the skill (project-level, this repo)
  SKILL.md
```

## Pipeline (four roles, each a separate subagent)

No role grades its own work.

### 1. Intake clerk

- Scans `supporting-docs/`: the **markdown files are the rated record's text**. A
  non-markdown original (pdf/docx/pages) in the same directory is paired with its
  markdown counterpart and kept as reference — consulted when a transcript is
  ambiguous, suspected incomplete, or needs verification. An original with **no**
  markdown counterpart gets transcribed (AppleScript Pages export for `.pages`,
  `pdftotext`/docx conversion for documents, OCR fallback for scans);
  `personal-records/` is a fallback source only for evidence with no copy in
  `supporting-docs/` at all. Skips unchanged files by content hash. Unreadable
  files flagged `NEEDS-ATTENTION` — never silently skipped.
- **Evidence-of-record classification (first job):** for every document, determine
  from `DOCUMENT-PROVENANCE.md` whether it is (a) the signed/filed instrument,
  (b) a superseded draft, or (c) unsubmitted material. Only (a) — plus unsigned
  records that would reach the VA another way (e.g. treatment records the VA will
  obtain) — enters the rated record. Multiple versions of the same instrument
  (e.g. the three 21-0781 variants) are resolved to the filed one; the rest are
  excluded. Anything unresolvable is flagged, excluded, and **listed in the report
  as excluded with the reason** — never silently dropped, never silently included.
- Appends provenance rows for newly transcribed documents (per the existing
  `DOCUMENT-PROVENANCE.md` conventions) rather than maintaining a parallel manifest.

### 2. C&P examiner

- Reads **only** the rated record from intake + the claimed contentions (the MH
  package named in Purpose, hard-coded in the skill).
- Fills out the real Mental Disorders / Initial PTSD DBQ structure from the
  knowledge base, including the occupational/social-impairment checkbox that
  drives the rating.
- Runs the credibility hunt, dispatching the existing **claim-consistency-checker**
  agent scoped to the rated record (dates, diagnoses, employment status, symptom
  reports).
- **Citation anchoring (hard rule):** every DBQ endorsement and every finding must
  cite document + section. No uncited endorsements.

### 3. Rating specialist (RVSR)

- Takes the DBQ + rated record and writes a rating-decision-style report (format
  below), assigning the highest defensible percentage under 38 C.F.R. § 4.130.
- Same citation-anchoring rule: every criterion found met cites document + section.

### 4. Adversarial reviewer

- A denial-minded rater attacks the assigned rating using `denial-patterns.md`;
  every viable attack path is documented; sustained attacks are appended to the
  report as the priority weakness list. The RVSR's rating stands, annotated.

### Blindness rule (hard, applies to roles 2–4)

The examiner, RVSR, and adversarial reviewer are **prohibited from reading**
`planning-docs/`, `COMPREHENSIVE-FINDINGS-*`, `CLAIM-ASSESSMENT.md`,
`document-analysis/`, exam-prep or nexus-letter-guide material, `rater-kb/` aside
(the KB is law/procedure, not case strategy), and anything else outside the rated
record. Strategy material would contaminate the emulation and inflate the score.
The skill enforces this by passing roles 2–4 an explicit file list, not directory
access.

## Knowledge base (`rater-kb/`, built via deep-research; can proceed in parallel with skill scaffolding)

One deep-research run producing five files. **Every legal citation passes through
the project citation-verifier agent before a file is accepted** (prior research
pass: 40 of 109 citations misstated). Contradictions with
`claim-maximization-research-2026-06.md` are flagged explicitly in the KB, never
silently resolved.

1. `dbq-mental-disorders.md` — actual field structure of the Mental Disorders and
   Initial PTSD DBQs: impairment-level checkbox scale, symptom checklist, remarks,
   examiner completion instructions.
2. `rating-procedure.md` — M21-1 RVSR procedure: evidence weighing, lay-evidence
   competence/credibility rules, favorable findings, benefit-of-the-doubt
   (§ 3.102), required rating-decision structure, **and how raters weigh
   self-report instruments (vendor-scored DASS-21/WHODAS) versus clinician
   findings** — encoding the weight caveats already logged in
   `DOCUMENT-PROVENANCE.md`.
3. `criteria-4130-caselaw.md` — § 4.130 General Rating Formula at each level with
   controlling case law: _Vazquez-Claudio_ (symptom-driven analysis), _Mauerhan_
   (non-exhaustive symptom list), _Bankhead_ (suicidal ideation at 70%),
   total-impairment analysis.
4. `mst-adjudication.md` — § 3.304(f)(5) marker evidence, MST-specialized claim
   processing, delayed-disclosure handling, male-survivor presentation guidance.
5. `denial-patterns.md` — documented common denial/underrating reasons for MH and
   MST claims (insufficient exam findings, credibility inconsistencies,
   income/work-history conflicts, treatment gaps). Powers the adversarial reviewer.

## Report format (`ratings/YYYY-MM-DD-rating-report.md`)

VA-faithful sections, written as a rater would write them:

- Contentions
- Evidence considered (the rated record) **and evidence excluded, with reasons**
- Favorable findings
- Reasons and bases
- **Decision (assigned %)**

Assessment extras:

- Filled DBQ (examiner output, citation-anchored)
- Strengths / weaknesses ledger
- Per-document helps/hurts table
- Gap list keyed to the next-higher rating's criteria
- Sustained adversarial attacks, ranked by severity
- **Record-completeness section:** evidence the real adjudicator will have that
  this mock does not (STRs, DD-214 if untranscribed, VA treatment records, and —
  dominantly — the real C&P examiner's DBQ from a live interview). The report's
  framing is explicit: **the score is conditional on the actual C&P exam**; a
  records-only mock cannot substitute for the in-person examination that usually
  controls the impairment finding.
- Delta vs. the previous run's report (score and gap-list movement)

## Error handling

- Missing `rater-kb/` → skill stops: build the KB first (no improvised law).
- Empty rated record after classification → skill stops and reports why every
  candidate document was excluded.
- Untranscribable documents → `NEEDS-ATTENTION` flag **and** listed in the report.
- Consistency-checker findings are always surfaced in the report, even when the
  examiner judges them explainable.
- Provenance rows that can't classify a document → excluded + reported (see
  intake), with a prompt to the user to resolve provenance.

## Validation

- Structural review of the skill file (frontmatter, role prompts, file paths).
- Citation-verifier pass over all five KB files.
- **Blind-rediscovery acceptance test (run only when the user authorizes the first
  run):** the corpus contains known, documented defects — the nexus letter's DOB
  error ("1998" vs. actual 1989), Kline/Klein spelling drift, the two-way phone
  discrepancy, the opioid-origin claim contradicted by clinical records, the Reyes
  unit/DD-214 mismatch. The examiner runs blind; its credibility findings are then
  diffed against `COMPREHENSIVE-FINDINGS-*`. If it fails to independently
  rediscover the known defects, the credibility hunt is not examiner-grade and the
  examiner prompt gets revised before the score is trusted.

## Ethics guardrails (adopted verbatim in force from `/va-rating-reassess`)

- The objective is the maximum rating the veteran's genuine conditions
  legitimately support — accurate documentation, lawful claims. Never advise
  fabricating, exaggerating, or misrepresenting conditions, symptoms, or history
  (38 U.S.C. § 6103; 18 U.S.C. § 1001).
- **Never coach witness evidence.** The harness identifies credibility risks and
  hands them back; resolution belongs to the veteran and the actual witness in
  their own unedited words. It never drafts, rewords, or suggests framing for any
  witness statement.
- Reports close with: research assistance, not legal or medical advice; consult an
  accredited VSO or VA-accredited attorney before acting.

## Out of scope

- Non-mental-health contentions (ankle, chemical exposure, tinnitus increase) —
  the pipeline is MH/§ 4.130-specific in v1; the architecture doesn't preclude
  adding contention modules later.
- TDIU/SMC analysis — the rater notes when evidence implicates them but does not
  adjudicate them.
- Any filing/submission automation.
