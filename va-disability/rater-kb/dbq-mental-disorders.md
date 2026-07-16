# Mental Disorders DBQ Field Structure

Scope: the field-level structure of VA Form 21-0960P-2 (Mental Disorders DBQ) and
the Initial PTSD DBQ (21-0960P-1), plus the related PTSD DBQ variant hosted at
reginfo.gov (21-0960P-3/-4) and the older 21-0960P-4 (Dec 2010) symptom checklist.
This file tells the harness what an examiner actually fills in, field by field, so
a simulated exam can be checked for completeness and internal consistency.

**Hard rule carried from research verification:** the DBQ symptom checklist is a
flat check-all-that-apply list, NOT a gated ascending "Level I–VI" structure. A
claim asserting a six-level gated grouping (Level IV = suicidal
ideation/rituals/panic/impulse/hygiene, Level VI = gross thought impairment) was
adversarially tested and refuted 0–3. Do not reintroduce that structure anywhere
in the harness.

---

## 1. Mental Disorders DBQ (VA Form 21-0960P-2)

Source: https://www.benefits.va.gov/compensation/docs/mental_disorders.pdf

The form has **8 sections**, DSM-5 based:

> "This evaluation should be based on DSM-5 diagnostic criteria ... SECTION 6 -
> COMPETENCY ... 7A. Remarks (Including any testing results) ... SECTION 8 -
> EXAMINER'S CERTIFICATION AND SIGNATURE"
> — benefits.va.gov/compensation/docs/mental_disorders.pdf

- **Section 1 — Diagnosis**
  - 1A: list of diagnoses
  - 1B: differentiation of symptoms/impairment attributable to each diagnosis,
    including any TBI comorbidity
  - 1C: the occupational/social-impairment checkbox (see § 2 below)
- **Section 2 — Clinical Findings** — evidence review plus history, broken into
  6 subareas (2A–2F): social/marital/family; occupational/educational;
  mental-health; legal/behavioral; substance-abuse — each one covering
  pre-military, during-military, and post-military periods
- **Section 3 — Symptoms** — the § 4.130-derived check-all-that-apply list (see
  § 3 below)
- **Section 4 — Behavioral Observations**
- **Section 5 — Other Symptoms**
- **Section 6 — Competency** (financial competency for VA purposes)
- **Section 7 — Remarks** — explicitly "Including any testing results," i.e. this
  is where psychometric/self-report instrument scores are recorded
- **Section 8 — Examiner's Certification and Signature**

Source: benefits.va.gov/compensation/docs/mental_disorders.pdf [claim verified
3-0 in prior adversarial pass]

### 1.1 The occupational/social-impairment checkbox (item C1)

The examiner selects **exactly one** checkbox summarizing impairment across **all**
mental diagnoses combined — not per-diagnosis:

> "C1. Which of the following best summarizes the Veteran's level of occupational
> and social impairment with regard to all mental diagnoses? (check only one)"
> — benefits.va.gov/compensation/docs/mental_disorders.pdf [3-0]

There are **seven** levels, running from "No mental disorder diagnosis" up to
"Total occupational and social impairment" — the six percentage-bearing levels
mirror the § 4.130 General Rating Formula verbatim (full text in
`criteria-4130-caselaw.md`), plus a zero-diagnosis floor level:

1. No mental disorder diagnosis
2. A mental condition has been formally diagnosed, but symptoms are not severe
   enough either to interfere with occupational and social functioning or to
   require continuous medication (→ 0%)
3. Mild or transient symptoms which decrease work efficiency and ability to
   perform occupational tasks only during periods of significant stress, or
   symptoms controlled by continuous medication (→ 10%)
4. Occasional decrease in work efficiency and intermittent periods of inability
   to perform occupational tasks (→ 30%)
5. Reduced reliability and productivity (→ 50%)
6. Occupational and social impairment with deficiencies in most areas (→ 70%)
7. Total occupational and social impairment (→ 100%)

This exact seven-level structure is independently confirmed on the Initial PTSD
DBQ (item 4A) and the reginfo.gov PTSD DBQ variant (Section VI item 6):

> "4A. WHICH OF THE FOLLOWING BEST SUMMARIZES THE VETERAN'S LEVEL OF OCCUPATIONAL
> AND SOCIAL IMPAIRMENT ... (Check only one) ... TOTAL OCCUPATIONAL AND SOCIAL
> IMPAIRMENT ... WITH DEFICIENCIES IN MOST AREAS ... WITH REDUCED RELIABILITY AND
> PRODUCTIVITY"
> — https://cck-law.com/wp-content/uploads/2020/06/PTSD-Initial-DBQ.pdf (May 22
> 2018 version) [3-0]

> "6. WHICH OF THE FOLLOWING BEST REPRESENTS THE VETERAN'S LEVEL OF OCCUPATIONAL
> AND SOCIAL IMPAIRMENT? ... occasional decrease in work efficiency ... reduced
> reliability and productivity ... deficiencies in most areas ... Total
> occupational and social impairment"
> — https://www.reginfo.gov/public/do/DownloadDocument?objectID=22857101 [2-1]

### 1.2 Comorbid-condition attribution (items B2/C2)

When a veteran has more than one diagnosed mental disorder, the examiner does not
simply add impairment together — the form forces an explicit differentiation
question, with a fallback rule when differentiation is impossible:

> "B2. Is it possible to differentiate what symptom(s) is/are attributable to each
> diagnosis? ... C2. For the indicated occupational and social impairment, is it
> possible to differentiate which impairment is caused by each mental disorder?"
> — benefits.va.gov/compensation/docs/mental_disorders.pdf [3-0]

If **yes**, the examiner lists which symptoms/impairment attach to which
diagnosis and discusses the clinical basis for that association. If **no**, the
examiner must give a reason, and the resulting practice — confirmed on the older
21-0960P-4 (Dec 2010) symptom checklist — is to treat the impairment as an
undifferentiated whole:

> "5. SYMPTOMS ... CONSIDER THE CUMULATIVE IMPACT OF ALL DIAGNOSED MENTAL
> DISORDERS THAT THE EXAMINER JUDGES RELATED TO MILITARY SERVICE, WITHOUT
> ATTEMPTING TO DIFFERENTIATE WHICH SYMPTOMS ARE SPECIFICALLY CAUSED BY WHICH
> MENTAL DISORDER"
> — reginfo.gov/.../objectID=22857101 (VA Form 21-0960P-4, Dec 2010) [3-0]

**Practical rule for the harness:** if an examiner cannot differentiate
symptoms/impairment among comorbid diagnoses (the common case), the rater treats
all diagnosed, service-connected mental disorders as a single combined
disability picture for rating purposes — this is the DBQ-level mechanism behind
the anti-pyramiding practice a rater applies under § 4.130 (see
`rating-procedure.md` and `criteria-4130-caselaw.md`).

### 1.3 Section 3 symptom checklist

31 symptoms drawn verbatim from § 4.130, explicitly framed as being for rating
purposes, check-all-that-apply (**not** gated or leveled):

> "3A. For VA rating purposes, check all symptoms that apply ... Depressed Mood
> ... Suicidal ideation ... Obsessional rituals which interfere with routine
> activities ... Disorientation to time or place"
> — benefits.va.gov/compensation/docs/mental_disorders.pdf [3-0]

---

## 2. Initial PTSD DBQ (VA Form 21-0960P-1, May 22 2018 version)

Source: https://cck-law.com/wp-content/uploads/2020/06/PTSD-Initial-DBQ.pdf

### 2.1 Differentiation items (3B, 4B)

Same structure as the Mental Disorders DBQ's B2/C2, applied to PTSD plus any
comorbid diagnosis:

> "3B. IS IT POSSIBLE TO DIFFERENTIATE WHAT SYMPTOM(S) ... 4B. FOR THE INDICATED
> OCCUPATIONAL AND SOCIAL IMPAIRMENT, IS IT POSSIBLE TO DIFFERENTIATE WHICH
> IMPAIRMENT IS CAUSED BY EACH MENTAL DISORDER?"
> — cck-law.com/.../PTSD-Initial-DBQ.pdf [3-0]

If not possible, symptoms/impairment are documented as an undifferentiated whole
— same fallback as § 1.2 above.

### 2.2 Section 5 "SYMPTOMS"

Reproduces the § 4.130 symptom list verbatim, framed for rating purposes, with an
explicit instruction on what NOT to check — symptoms clearly caused by something
other than PTSD go elsewhere:

> "FOR VA RATING PURPOSES, CHECK ALL SYMPTOMS THAT APPLY ... Do NOT mark symptoms
> below that are clearly not attributable to the Criteria A stressor/PTSD.
> Instead, overlapping symptoms clearly attributable to other things should be
> noted under #7 - Other symptoms."
> — cck-law.com/.../PTSD-Initial-DBQ.pdf [2-1]

### 2.3 Stressor section — the examiner's role in MST marker development

Per stressor reported, the examiner documents:

1. Does the stressor meet Criterion A?
2. Does it relate to fear of hostile military or terrorist activity?
3. Does it relate to an in-service personal assault (e.g., military sexual
   trauma)?
4. If MST-related: describe the markers that may substantiate the stressor.

> "Is the stressor related to in-service personal assault, e.g. military sexual
> trauma? ... If yes, please describe the markers that may substantiate the
> stressor."
> — cck-law.com/.../PTSD-Initial-DBQ.pdf [3-0]

This makes the C&P examiner an active participant in § 3.304(f)(5) marker
development, not a passive scorer — see `mst-adjudication.md` for the full
marker-evidence framework this question is built on.

### 2.4 Records reviewed + per-stressor checklist (reginfo.gov variant)

The PTSD DBQ variant hosted at reginfo.gov documents which records were reviewed
(Section III) and repeats the per-stressor Criterion-A / symptom-relation
questions:

> "Does this stressor meet Criterion A ... Are the veteran's symptoms related to
> this stressor? ... 3B. CHECK ALL RECORDS THAT WERE REVIEWED"
> — reginfo.gov/.../objectID=22857101 [3-0]

---

## 3. Remarks / testing results and the nexus statement

Both DBQs route psychometric test results (Mississippi Scale, PCL, MMPI/MMPI-2,
etc.) into the free-text Remarks field rather than a scored field — see
`rating-procedure.md` § "Weighing self-report instruments" for how those results
are treated once they reach the rater, and the same file's nexus-probability
scale for how the examiner's etiology opinion is worded.

---

## Verification Ledger

- benefits.va.gov/compensation/docs/mental_disorders.pdf (Mental Disorders DBQ —
  8-section structure, C1 checkbox, B2/C2 differentiation, Section 3 symptom
  list) — UNVERIFIED
- https://cck-law.com/wp-content/uploads/2020/06/PTSD-Initial-DBQ.pdf (Initial
  PTSD DBQ, May 22 2018 — 4A checkbox, 3B/4B differentiation, Section 5 symptoms,
  stressor/MST marker item) — UNVERIFIED
- https://www.reginfo.gov/public/do/DownloadDocument?objectID=22857101 (PTSD DBQ
  variant 21-0960P-3, Section VI item 6; records-reviewed + per-stressor items;
  and VA Form 21-0960P-4 Dec 2010 cumulative-impact symptom rule) — UNVERIFIED
- § 4.130 seven-level occupational/social-impairment scale reconstruction is
  cross-referenced against `criteria-4130-caselaw.md`, which cites
  https://www.law.cornell.edu/cfr/text/38/4.130 — UNVERIFIED

## Conflicts with prior research

`../claim-maximization-research-2026-06.md` does not describe DBQ field
structure at all (it is a claim-strategy document, not a procedural reference),
so there is no overlapping claim to reconcile. One indirectly relevant note: that
document's own Verification Ledger flags its § 4.130 diagnostic-code-range
citation (DC 9201-9440) as MISSTATED (incomplete — omits eating-disorder codes
9520-9521). This file does not cite any diagnostic-code range, so the misstatement
does not propagate here.

None found beyond the above.
