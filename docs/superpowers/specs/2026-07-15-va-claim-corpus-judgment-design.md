# VA Claim Corpus Judgment Harness — Design

**Date:** 2026-07-15
**Status:** Approved design, pending implementation plan
**Subject:** `va-disability/`

## Purpose

Build a re-runnable harness (`/rate-claim` project skill) that judges the corpus of
documentation supporting Marcus's PTSD/MST claim (with MDD, GAD, OCD, and SUD) the
way the VA itself would: a mock C&P examination followed by a mock rating decision,
producing the **highest defensible rating** the evidence supports, plus
strengths/weaknesses, per-document helps/hurts, and a gap list toward the
next-higher rating.

The harness is built now but **not executed** until the user says go (records are
still being added to the corpus).

## Decisions made during brainstorming

| Decision           | Choice                                                                                               |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| Rating target      | **Highest defensible** — the mock rater assigns 0/10/30/50/70/100 exactly as the evidence supports   |
| Corpus location    | Originals in `va-disability/supporting-docs/` (user-managed); transcripts in `va-disability/corpus/` |
| Deliverable shape  | Re-runnable project skill (`/rate-claim`); dated reports enable baseline → final comparison          |
| Examiner knowledge | One-time deep-research pass → static, citation-verified knowledge base in `va-disability/rater-kb/`  |
| Architecture       | Intake → examiner → rater pipeline **plus** an adversarial denial-minded reviewer as a fourth stage  |

## Directory layout

```
va-disability/
  supporting-docs/          # originals dropped by the user (PDF, .pages, images, scans)
  corpus/                   # harness-managed markdown transcripts, one per original
    MANIFEST.md             # inventory: file, type, date, author, what it evidences,
                            # transcription status, content hash
  rater-kb/                 # static rater-emulation knowledge base (5 files, below)
  ratings/                  # dated run outputs: YYYY-MM-DD-rating-report.md
.claude/skills/rate-claim/  # the skill (project-level, this repo)
  SKILL.md
```

## Pipeline (four roles, each a separate subagent)

No role grades its own work.

1. **Intake clerk** — scans `supporting-docs/`, transcribes new/changed files into
   `corpus/` (AppleScript Pages export for `.pages`, `pdftotext` for text PDFs, OCR
   fallback for scans), updates `MANIFEST.md`. Skips unchanged files by content
   hash. Unreadable files are flagged `NEEDS-ATTENTION` in the manifest — never
   silently skipped.
2. **C&P examiner** — reads the full corpus + the claimed contentions (the MH
   package named in Purpose, hard-coded in the skill); fills out the
   real Mental Disorders / Initial PTSD DBQ structure from the knowledge base
   (including the occupational/social-impairment checkbox that drives the rating);
   runs the credibility hunt, dispatching the existing project
   **claim-consistency-checker** agent for the cross-document contradiction sweep
   (dates, diagnoses, employment status, symptom reports).
3. **Rating specialist (RVSR)** — takes the DBQ + corpus and writes a
   rating-decision-style report (format below), assigning the highest defensible
   percentage under 38 C.F.R. § 4.130.
4. **Adversarial reviewer** — a denial-minded rater attacks the assigned rating
   using `denial-patterns.md`; every viable attack path is documented; sustained
   attacks are appended to the report as the priority weakness list. The RVSR's
   rating stands, annotated with sustained attacks.

## Knowledge base (`rater-kb/`, built first via deep-research)

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
   (§ 3.102), required rating-decision structure.
3. `criteria-4130-caselaw.md` — § 4.130 General Rating Formula at each level with
   controlling case law: _Vazquez-Claudio_ (symptom-driven analysis), _Mauerhan_
   (non-exhaustive symptom list), _Bankhead_ (suicidal ideation at 70%),
   total-impairment analysis.
4. `mst-adjudication.md` — § 3.304(f)(5) marker evidence, MST-specialized claim
   processing, delayed-disclosure handling, male-survivor presentation guidance.
5. `denial-patterns.md` — documented common denial/underrating reasons for MH and
   MST claims (insufficient exam findings, credibility inconsistencies,
   income/work-history conflicts, treatment gaps). Powers the adversarial reviewer.

The skill loads these files every run — deterministic and citable, no per-run
research.

## Report format (`ratings/YYYY-MM-DD-rating-report.md`)

VA-faithful sections, written as a rater would write them:

- Contentions
- Evidence considered
- Favorable findings
- Reasons and bases
- **Decision (assigned %)**

Assessment extras:

- Filled DBQ (examiner output)
- Strengths / weaknesses ledger
- Per-document helps/hurts table
- Gap list keyed to the next-higher rating's criteria
- Sustained adversarial attacks, ranked by severity
- Delta vs. the previous run's report (score and gap-list movement)

## Error handling

- Missing `rater-kb/` → skill stops: build the KB first (no improvised law).
- Empty/missing `supporting-docs/` or `corpus/` → skill stops with instructions.
- Untranscribable documents → `NEEDS-ATTENTION` in manifest **and** listed in the
  report, so evidence never silently drops out of the record.
- Consistency-checker findings are always surfaced in the report, even when the
  examiner judges them explainable.

## Validation (pre-first-run)

- Structural review of the skill file (frontmatter, role prompts, file paths).
- Citation-verifier pass over all five KB files — the only "execution" now.
- First real run only when the user says go.

## Bright line (stated in the skill itself)

The harness assesses truthfully-documented evidence as a rater would. It never
suggests manufacturing, exaggerating, or coaching evidence (38 U.S.C. § 6103;
18 U.S.C. § 1001) — consistent with the fraud flag in the June research.

## Out of scope

- Non-mental-health contentions (ankle, chemical exposure, tinnitus increase) —
  the pipeline is MH/§ 4.130-specific in v1; the architecture doesn't preclude
  adding contention modules later.
- TDIU/SMC analysis — the rater notes when evidence implicates them but does not
  adjudicate them.
- Any filing/submission automation.
