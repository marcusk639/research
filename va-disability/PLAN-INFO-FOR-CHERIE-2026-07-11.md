# Plan — Build an "Information for Dr. Mills's Clinical Review" Document

> **Status:** active plan · **Created:** 2026-07-11 · **Type:** phased plan (via `make-plan`)
> **Goal:** produce a document the veteran can hand to (or discuss with) his treating clinician, Cherie Mills, LCSW — a complete, honest inventory of **genuine symptoms and history** that the current nexus letter under-captures, so that *she* can independently assess them and, in her own clinical judgment, document what she finds. The purpose is a **fuller, more accurate** clinical picture (which happens to be what a strong 100% letter needs), not a scripted letter.
> **Inputs (both read):** `personal-records/supporting-docs/nexus-letter-cherie.md` (her signed 2 July 2026 letter) and `NEXUS-LETTER-EVALUATION.md` (the content evaluation + current-vs-100% gap map).

## The governing rule (design constraint for every phase)

This is a **patient giving his treating clinician true information about himself** — legitimate and encouraged. It is **NOT** coaching. So the document MUST:

- Contain **only genuine, truthful** symptoms/history the veteran actually experiences — nothing manufactured, exaggerated, or added because it "helps."
- Be framed as **information for her independent assessment** — every item says, in effect, "here is what I experience; you evaluate and document what your clinical judgment supports."
- **Never** tell Cherie what to conclude, what diagnosis to reach, what impairment level or rating tier to endorse, or how to word her letter.
- Leave all **characterizations to her** — most importantly, whether a belief is a *delusion* vs. *severe anxiety* is her clinical determination, not the veteran's label.
- Note that she includes **only what she independently concludes is accurate**; an over-reached letter is worse than an accurate one.

If any item can't be stated as "this is genuinely true about me," it does not go in.

---

## Phase 0 — Discovery (COMPLETE — consolidated)

**What the letter already covers well** (don't re-surface): correct nexus standard; actual DSM-5 diagnoses (PTSD/MDD/GAD/OCD/SUD); in-service MST stressor; treating-provider basis; SUD-as-self-medication theory; the male-MST minimization insight; continuity since discharge; and the phrase "total impairment in occupational and social realms."

**The gaps the evaluation identified** (these define the document's contents — each to be provided as the veteran's *genuine account* for her assessment):

1. **Social functioning outside the marriage** — the reality of his isolation (talks essentially only to his wife; no friends, no community, doesn't leave the house).
2. **Daily-living dependence** — self-care/hygiene he can't maintain; his wife assisting/managing hygiene, medications, and appointments; forgetting important appointments.
3. **Beliefs/paranoia** — the fixed fear he'll be fired at any moment despite no evidence, and any other beliefs that don't match reality (incl. the grandiose one) — reported as *what he believes and how convinced he is*, not self-labeled as "delusion."
4. **The overworking mechanism** — that compulsive overworking is driven by that fear, not ambition, and worsens his condition (the cycle).
5. **Frequency / severity / duration** — how often and how long the shutdowns, panic, SI, and ADL failures occur, and that they are current.
6. **Suicidal ideation** — an honest current account (how often; passive vs. active).
7. **The December 2024 job loss** — that it happened and his genuine experience of it as condition-driven.
8. **Cognitive symptoms** — memory lapses / concentration problems (e.g., missing appointments).
9. **SUD framing** — his genuine account of using substances to cope with the psychiatric symptoms (supports the self-medication theory; and SUD belongs in her conclusion, which currently omits it).

**Supporting evidence to point her to** (so she can review objective sources herself): the DASS-21 and WHODAS 2.0 instruments; the treatment records; Erica's forthcoming lay statement; the two "Recover" PsychEvals (with the reconciliation caveat).

---

## Phase 1 — Build the document

**Output:** `personal-records/supporting-docs/INFO-FOR-CHERIE-CLINICAL-REVIEW.md` (kept in `personal-records/` — it's detailed personal health information meant to be handed to the clinician; gitignored).

**Structure:**
- **Header** — states plainly: this is genuine information the veteran is providing to his treating clinician for her independent assessment; she evaluates and documents only what her clinical judgment supports; nothing here asks her to state anything she does not independently conclude; it is not a draft of her letter.
- **One section per gap area (1–9 above)** — each containing the veteran's *truthful* first-person account of that symptom/experience, with concrete specifics (what, how often, how long, current or not). Framed as "here is what I experience," ending each with the neutral note that its clinical significance and characterization are for her to determine.
- **"Records available for your review"** — the objective sources she can independently examine.
- **Closing** — reiterates she should include only what she genuinely finds; offers to answer follow-ups; notes the companion `NEXUS-LETTER-GUIDE-CHERIE.md` explains what VA's criteria ask about without telling her what to conclude.

**Verification for this phase:**
- Every item is a genuine symptom/experience (nothing invented or reaching).
- No sentence tells Cherie what to conclude, diagnose, or write; no rating-tier language directed at her; no drafted letter wording.
- "Delusion" and other clinical characterizations are left explicitly to her.
- The DBQ (21-0960P-2) is mentioned only as a form she *may* complete in her judgment — not scripted.

**Anti-patterns to prevent:**
- Turning "information for her assessment" into "conclusions for her to sign."
- Any item phrased as "tell her to say X" or "she should characterize the marriage/beliefs as Y."
- Adding a symptom because it maps to a 100%-tier criterion rather than because it's true.

---

## Phase 2 — Independent review + finalize

- Re-read the draft against **the governing rule** above: strike anything that scripts her conclusions or that isn't genuinely true.
- Optional: dispatch a reviewer (general-purpose, fed only the draft + the governing rule) to catch any coaching-by-objective slips — the same discipline used on the master guide.
- Confirm no legal citations are asserted as fact (this is a symptom/history document; if any criteria are referenced, mark for `citation-verifier`).
- Leave the document for the veteran to use in a **care-first conversation** with Cherie; she assesses and documents in her own judgment; if she updates her letter and/or completes a DBQ, log it in `DOCUMENT-PROVENANCE.md`.

## Guardrails (whole effort)
- Genuine information only; her independent clinical judgment governs everything.
- Never script her conclusions, diagnoses, tier-selections, or wording.
- Never manufacture or exaggerate a symptom.
- PHI stays in `personal-records/` (gitignored).
- _Research assistance, not legal or medical advice; the treating clinician exercises independent judgment; consult an accredited VSO/attorney._

## Note for the user
This plan produces the document; it does not draft Cherie's letter or opinion. If you want, I can execute Phase 1 now and generate `INFO-FOR-CHERIE-CLINICAL-REVIEW.md` — a genuine symptom/history inventory in your own first-person voice for her review — then run the Phase 2 check.
