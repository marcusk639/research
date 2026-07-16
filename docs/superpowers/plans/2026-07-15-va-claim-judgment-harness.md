# VA Claim Corpus Judgment Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `/rate-claim` harness — a record-only mock VA adjudication pipeline over `va-disability/supporting-docs/` — plus its citation-verified `rater-kb/` knowledge base, per the approved spec at `docs/superpowers/specs/2026-07-15-va-claim-corpus-judgment-design.md`. Build only; the harness is NOT executed until the user authorizes the first run.

**Architecture:** Two tracks. Track A (Tasks 2–3) builds the five-file `rater-kb/` knowledge base via one deep-research run, then citation-verifies every legal cite. Track B (Tasks 4–6) scaffolds the `/rate-claim` skill: a report template plus a SKILL.md that orchestrates four subagent roles (intake → C&P examiner → RVSR → adversarial reviewer) with hard blindness, substance-only, citation-anchoring, and findings-and-remediation rules. Tasks 2–3 and 4–5 can run in parallel; Task 6 (validation) and Task 7 (navigation docs) need both.

**Tech Stack:** Claude Code project skill + subagents (`citation-verifier`, `claim-consistency-checker`, `deep-research` skill), macOS conversion tools (`textutil` for docx, `pdftotext`, AppleScript Pages export, `tesseract`/Vision OCR fallback). No build/test framework — this is a research repo; verification steps use file checks and agent passes.

## Global Constraints

- **Never execute `/rate-claim`** during implementation. No mock exam, no rating run, no report generated. The blind-rediscovery acceptance test in the spec is deferred until the user authorizes the first run.
- **PHI:** `va-disability/personal-records/` is gitignored real PHI. Never `git add` it or copy its contents into tracked files.
- **No coaching:** never draft, reword, or suggest framing for witness statements — in the skill's prompts AND in your own conduct while building it.
- **Substance-only:** clerical errors (DOB typos, name spellings, grammar) carry no rating weight anywhere in the harness (spec: "substance-only rule").
- Commit format: `<type>: <description>` (feat/fix/docs/chore). No attribution footers (disabled globally).
- A Prettier PostToolUse hook reformats every `.md` after Edit/Write — expect reflow; do not fight it. Re-Read a file before editing a region you just wrote.
- Skill frontmatter uses only keys the repo already uses (see `.claude/skills/va-rating-reassess/SKILL.md`): `name`, `description`, `disable-model-invocation`.
- Every legal citation in `rater-kb/` must be CONFIRMED by the `citation-verifier` agent or explicitly quarantined — the prior research pass had 40/109 citations misstated.

---

### Task 1: Scaffold `rater-kb/` and `ratings/` directories

**Files:**

- Create: `va-disability/rater-kb/README.md`
- Create: `va-disability/ratings/README.md`

**Interfaces:**

- Produces: the two directories all later tasks write into; the "KB INCOMPLETE" marker convention Task 5's SKILL.md checks for.

- [ ] **Step 1: Write `va-disability/rater-kb/README.md`**

```markdown
# Rater-Emulation Knowledge Base

Static, citation-verified knowledge the `/rate-claim` harness loads every run.
Built once via deep-research (spec:
`docs/superpowers/specs/2026-07-15-va-claim-corpus-judgment-design.md`), then
frozen — deterministic and citable, no per-run research.

**STATUS: KB INCOMPLETE — `/rate-claim` must refuse to run.**
(Delete this status line only when all five files below exist and each carries a
`## Verification Ledger` section with zero unresolved MISSTATED entries.)

| File                       | Contents                                                                       |
| -------------------------- | ------------------------------------------------------------------------------ |
| `dbq-mental-disorders.md`  | Field structure of the Mental Disorders + Initial PTSD DBQs                    |
| `rating-procedure.md`      | M21-1 RVSR procedure, evidence weighing, self-report-instrument weight caveats |
| `criteria-4130-caselaw.md` | § 4.130 criteria at each level + controlling case law                          |
| `mst-adjudication.md`      | § 3.304(f)(5) markers, MST-specialized processing, delayed disclosure          |
| `denial-patterns.md`       | Common denial/underrating patterns — powers the adversarial reviewer           |

These files are law/procedure, NOT case strategy — they are the one exception to
the harness's blindness rule. Contradictions with
`../claim-maximization-research-2026-06.md` are flagged inline under
`## Conflicts with prior research`, never silently resolved.
```

- [ ] **Step 2: Write `va-disability/ratings/README.md`**

```markdown
# Mock Rating Reports

Dated output of `/rate-claim` runs: `YYYY-MM-DD-rating-report.md`, one per run.
Reports are cumulative — never overwritten — so baseline → final runs can be
diffed as evidence is added to `supporting-docs/`.

Every report is a mock, records-only adjudication: **the score is conditional on
the actual C&P exam**, which this harness cannot substitute for. Reports are
research assistance, not legal or medical advice.

No reports exist yet: the first run requires explicit user authorization
(spec: Validation section — blind-rediscovery acceptance test gates trust in the
first score).
```

- [ ] **Step 3: Verify both files exist**

Run: `ls va-disability/rater-kb/README.md va-disability/ratings/README.md`
Expected: both paths print, no error.

- [ ] **Step 4: Commit**

```bash
git add va-disability/rater-kb/README.md va-disability/ratings/README.md
git commit -m "feat: scaffold rater-kb and ratings directories for /rate-claim harness"
```

---

### Task 2: Build the five KB files via deep-research

**Files:**

- Create: `va-disability/rater-kb/dbq-mental-disorders.md`
- Create: `va-disability/rater-kb/rating-procedure.md`
- Create: `va-disability/rater-kb/criteria-4130-caselaw.md`
- Create: `va-disability/rater-kb/mst-adjudication.md`
- Create: `va-disability/rater-kb/denial-patterns.md`

**Interfaces:**

- Consumes: directory from Task 1.
- Produces: the five KB files Task 3 verifies and Task 5's SKILL.md loads by exact filename.

- [ ] **Step 1: Invoke the `deep-research` skill** with exactly this research brief as args:

> Research how the VA actually conducts and adjudicates a mental-health disability examination and rating for PTSD (MST stressor) with comorbid MDD, GAD, OCD, and SUD, so an AI can emulate a C&P examiner and an RVSR as faithfully as possible. Write the findings as five separate Markdown files into `va-disability/rater-kb/` (exact filenames below). Primary sources only where possible: va.gov (DBQ forms, C&P examiner guidance), the VA KnowVA M21-1 adjudication manual, eCFR (38 C.F.R. §§ 3.102, 3.304(f)(5), 4.125–4.130, 4.14), CourtListener/CAVC for case law. Cite every claim inline with source URL and effective year.
>
> 1. `dbq-mental-disorders.md` — the exact field structure of VA Form 21-0960P-2 (Mental Disorders DBQ) and the Initial PTSD DBQ: every section, the occupational/social-impairment checkbox scale verbatim, the symptom checklist verbatim, remarks fields, and the instructions examiners receive for completing them (including how they select ONE impairment level and how comorbid conditions are attributed).
> 2. `rating-procedure.md` — how an RVSR processes an MH claim per M21-1: evidence review order, competence vs. credibility of lay evidence, favorable findings (binding), benefit of the doubt (§ 3.102), how a rating decision document is structured, and how raters weigh vendor-scored self-report instruments (DASS-21, WHODAS 2.0) versus clinician findings.
> 3. `criteria-4130-caselaw.md` — the § 4.130 General Rating Formula criteria verbatim at 0/10/30/50/70/100 with controlling interpretation: Vazquez-Claudio v. Shinseki (severity-frequency-duration, not symptom-counting), Mauerhan v. Principi (list is non-exhaustive), Bankhead v. Shulkin (suicidal ideation alone can support 70), plus what distinguishes 70 from 100 in practice (total occupational AND social impairment).
> 4. `mst-adjudication.md` — § 3.304(f)(5) marker evidence categories verbatim, VA's MST-specialized claim processing (MST coordinators, dedicated reviewers), AZ v. Shinseki (absence of report not pejorative), delayed-disclosure handling, and published guidance on male-survivor presentation.
> 5. `denial-patterns.md` — documented common reasons MH/MST claims are denied or underrated: insufficient exam findings, credibility inconsistencies (including income/work-history conflicts with claimed impairment), treatment gaps, inadequate nexus language, stressor-marker insufficiency. Include BVA remand/denial patterns where documented.
>
> Each file must end with two sections: `## Verification Ledger` (every citation listed as UNVERIFIED — a separate pass confirms them) and `## Conflicts with prior research` (explicit flags where findings contradict `va-disability/claim-maximization-research-2026-06.md`, or "None found").

- [ ] **Step 2: Verify all five files exist with required trailing sections**

Run: `for f in dbq-mental-disorders rating-procedure criteria-4130-caselaw mst-adjudication denial-patterns; do grep -L "## Verification Ledger" "va-disability/rater-kb/$f.md"; done`
Expected: no output (every file has the section). Repeat with `"## Conflicts with prior research"`.

- [ ] **Step 3: Spot-check each file states an effective year + source URL for its key claims**

Run: `grep -c "http" va-disability/rater-kb/*.md`
Expected: every file shows a nonzero count.

- [ ] **Step 4: Commit**

```bash
git add va-disability/rater-kb/
git commit -m "feat: build rater-emulation knowledge base via deep-research (citations unverified)"
```

---

### Task 3: Citation-verification pass over the KB

**Files:**

- Modify: all five `va-disability/rater-kb/*.md` (Verification Ledger sections)
- Modify: `va-disability/rater-kb/README.md` (STATUS line)

**Interfaces:**

- Consumes: the five KB files from Task 2.
- Produces: KB files whose every citation is CONFIRMED or quarantined; README STATUS flipped to complete — the state Task 5's SKILL.md precondition checks.

- [ ] **Step 1: Dispatch the `citation-verifier` agent once per KB file (5 dispatches, in parallel, single message)** with this prompt per file:

> Verify every legal citation (case law, CFR/USC sections, M21-1 provisions, VA form numbers/revisions) in `va-disability/rater-kb/<FILE>`. For each: CONFIRMED (with the authoritative source URL you checked) / MISSTATED (what's wrong, what the correct statement is) / UNVERIFIABLE. Return a complete list — do not skip citations that look obviously correct; this corpus previously had 40/109 citations misstated.

- [ ] **Step 2: Apply the verdicts to each file's `## Verification Ledger`**

For each citation: mark CONFIRMED entries as such with the checked URL; for MISSTATED entries, correct the body text to the verified statement and log the correction in the ledger; for UNVERIFIABLE entries, move the claim itself into the ledger under a `QUARANTINED — do not rely on` heading and delete it from the body.

- [ ] **Step 3: Verify no unresolved entries remain**

Run: `grep -n "UNVERIFIED\|MISSTATED" va-disability/rater-kb/*.md`
Expected: no matches outside ledger lines that document a _resolved_ correction (i.e., no citation still pending).

- [ ] **Step 4: Flip the README status**

In `va-disability/rater-kb/README.md`, replace the line
`**STATUS: KB INCOMPLETE — /rate-claim must refuse to run.**` and its parenthetical
with: `**STATUS: KB COMPLETE — verified <YYYY-MM-DD>.**`

- [ ] **Step 5: Commit**

```bash
git add va-disability/rater-kb/
git commit -m "docs: citation-verify rater-kb — corrections applied, unverifiable claims quarantined"
```

---

### Task 4: Write the rating-report template

**Files:**

- Create: `.claude/skills/rate-claim/report-template.md`

**Interfaces:**

- Produces: the exact report skeleton Task 5's SKILL.md instructs the RVSR role to fill. Section names here are load-bearing — SKILL.md references them verbatim.

- [ ] **Step 1: Write `.claude/skills/rate-claim/report-template.md`**

```markdown
# Mock Rating Decision — {DATE}

> Records-only mock adjudication by the `/rate-claim` harness. **The score below
> is conditional on the actual C&P examination**, which usually controls the
> impairment finding and which this mock cannot substitute for. Research
> assistance, not legal or medical advice — consult an accredited VSO or
> VA-accredited attorney before acting.

## Contentions

{The MH package: PTSD (MST stressor) with MDD, GAD, OCD; SUD secondary.}

## Evidence considered (the rated record)

{Table: document · date · author · evidence-of-record class (filed instrument /
treatment record) · markdown path · original path if present}

## Evidence excluded, with reasons

{Every candidate document excluded at intake: superseded draft / unsubmitted /
unresolvable provenance / untranscribable (NEEDS-ATTENTION), with the reason.
"None" if none.}

## Favorable findings

{Findings binding in the veteran's favor, as a rater would record them.}

## Reasons and bases

{The § 4.130 analysis: symptoms → severity/frequency/duration → impairment level,
citation-anchored to document + section for every criterion found met.}

## DECISION

**Assigned rating: {N}%** under 38 C.F.R. § 4.130, General Rating Formula.

---

# Assessment extras (not part of a real rating decision)

## Filled DBQ (examiner output)

{The examiner's completed DBQ structure, citation-anchored.}

## Consistency findings (substantive only)

{claim-consistency-checker output, filtered to substance. Clerical errata: one
footnote line, no rating weight.}

## Strengths / weaknesses ledger

{Substance only. Every weakness pairs with a remediation — see below.}

## Per-document helps/hurts

{Table: document · helps (what/why, cited) · hurts (what/why, cited).}

## Gap list to the next-higher rating

{Each unmet criterion of the next level up · what evidence would meet it.}

## Sustained adversarial attacks (ranked by severity)

{Each attack: the argument · why it survived · affected rating element.}

## Findings and remediations

{EVERY issue above (weakness, gap, sustained attack, consistency finding) gets a
row: finding · suggested resolution (a remediation PATH — obtain a named record,
request a provider addendum on a specific gap, resolve provenance, have a witness
reconcile a discrepancy in their own words — NEVER drafted wording for witness
statements) · owner · expected rating impact. An issue with no remediation gets an
explicit "no remediation exists — accept and mitigate by {X}". No orphan findings.}

## Record-completeness

{Evidence the real adjudicator will have that this mock does not: STRs, DD-214 if
untranscribed, VA treatment records, and dominantly the real C&P examiner's DBQ
from a live interview.}

## Delta vs. previous run

{Score movement, gap-list items closed/opened, new evidence since last report.
"First run — no prior report" if none.}
```

- [ ] **Step 2: Verify the template's section headings**

Run: `grep -c "^## " .claude/skills/rate-claim/report-template.md`
Expected: `15` (Contentions · Evidence considered · Evidence excluded · Favorable findings · Reasons and bases · DECISION · Filled DBQ · Consistency findings · Strengths / weaknesses ledger · Per-document helps/hurts · Gap list · Sustained adversarial attacks · Findings and remediations · Record-completeness · Delta vs. previous run).

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/rate-claim/report-template.md
git commit -m "feat: add rating-report template for /rate-claim harness"
```

---

### Task 5: Write the `/rate-claim` SKILL.md

**Files:**

- Create: `.claude/skills/rate-claim/SKILL.md`

**Interfaces:**

- Consumes: KB filenames from Task 2 (`rater-kb/dbq-mental-disorders.md`, `rating-procedure.md`, `criteria-4130-caselaw.md`, `mst-adjudication.md`, `denial-patterns.md`); the KB README `STATUS: KB COMPLETE` marker from Task 3; `report-template.md` from Task 4.
- Produces: the invocable `/rate-claim` skill.

- [ ] **Step 1: Write `.claude/skills/rate-claim/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Verify the skill's internal references resolve**

Run: `grep -o "rater-kb/[a-z0-9-]*\.md" .claude/skills/rate-claim/SKILL.md | sort -u`
Expected: exactly the five KB filenames from Task 2 (plus no others). Then:
`ls .claude/skills/rate-claim/report-template.md` — exists.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/rate-claim/SKILL.md
git commit -m "feat: add /rate-claim mock-adjudication skill (four-role pipeline, not yet run)"
```

---

### Task 6: Structural validation of the harness (no execution)

**Files:**

- Modify (only if defects found): `.claude/skills/rate-claim/SKILL.md`, `.claude/skills/rate-claim/report-template.md`

**Interfaces:**

- Consumes: everything from Tasks 1–5.

- [ ] **Step 1: Frontmatter check against the repo's working example**

Run: `head -6 .claude/skills/rate-claim/SKILL.md && head -6 .claude/skills/va-rating-reassess/SKILL.md`
Expected: same key set (`name`, `description`, `disable-model-invocation`), valid YAML (`---` fences).

- [ ] **Step 2: Spec-rule presence check** — every hard rule greps to at least one hit:

Run: `grep -c "original controls" .claude/skills/rate-claim/SKILL.md` → ≥1
Run: `grep -c "explicit file lists" .claude/skills/rate-claim/SKILL.md` → ≥1
Run: `grep -c "substance only\|Substance only\|substance-only" .claude/skills/rate-claim/SKILL.md` → ≥2
Run: `grep -c "Never coach" .claude/skills/rate-claim/SKILL.md` → ≥1
Run: `grep -c "remediation" .claude/skills/rate-claim/SKILL.md` → ≥2
Run: `grep -c "STATUS: KB COMPLETE" .claude/skills/rate-claim/SKILL.md` → ≥1

- [ ] **Step 3: Path-existence check** — every repo path the skill references exists:

Run: `grep -oE "va-disability/[A-Za-z0-9._/-]+" .claude/skills/rate-claim/SKILL.md | sort -u | while read p; do ls -d "$p" >/dev/null 2>&1 || echo "MISSING: $p"; done`
Expected: no `MISSING:` lines (note: `ratings/YYYY-...` is a pattern, not a path — exclude it by eye).

- [ ] **Step 4: Fix any defects found, re-run the failing check, commit if changed**

```bash
git add .claude/skills/rate-claim/
git commit -m "fix: structural corrections to /rate-claim skill from validation pass"
```

---

### Task 7: Wire the harness into the subject's navigation docs

**Files:**

- Modify: `va-disability/CLAUDE.md` (the "Subject-specific tools" section)

**Interfaces:**

- Consumes: the finished skill from Tasks 5–6.

- [ ] **Step 1: Add `/rate-claim` to the tools list in `va-disability/CLAUDE.md`**

In the `## Subject-specific tools` section, after the `/va-rating-strategy` bullet, insert:

```markdown
- **`/rate-claim`** skill — record-only mock VA adjudication of the
  `supporting-docs/` markdown evidence (intake → C&P examiner → RVSR →
  adversarial reviewer), producing a dated rating report in `ratings/` where
  every finding carries a suggested remediation. Blind to all strategy docs by
  design. Requires `rater-kb/` (STATUS: KB COMPLETE) and explicit user request —
  never auto-run. For strategy/odds questions use `/va-rating-reassess`.
```

- [ ] **Step 2: Verify the edit**

Run: `grep -A2 "rate-claim" va-disability/CLAUDE.md | head -5`
Expected: the new bullet prints.

- [ ] **Step 3: Commit**

```bash
git add va-disability/CLAUDE.md
git commit -m "docs: register /rate-claim harness in va-disability subject tools"
```

---

## Parallelism note

Tasks 2–3 (KB track) and Tasks 4–5 (skill track) are independent — run them in
parallel lanes if using subagent-driven execution. Task 6 needs both tracks
done; Task 7 needs Task 6. Task 2 is the long pole (deep-research run).

## Explicitly deferred (requires user authorization)

- Any invocation of `/rate-claim` — including the blind-rediscovery acceptance
  test, which is defined in the SKILL.md's "First-run acceptance test" section
  and runs only with the first authorized run.
