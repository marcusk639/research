# VA Claim Corpus Audit — Remediation Plan

> Adapted from `superpowers:writing-plans` for document/evidence remediation rather than
> software implementation — no code, tests, or commits involved; "tasks" are document
> fixes, citation checks, or decisions, each with a concrete completion condition.
> **Spec:** `va-disability/CLAIM-CORPUS-AUDIT-2026-07-06.md` (Credibility Risks,
> Cross-Document Findings, Evidentiary Gaps, Open Questions, Recommended Action Plan).

**Goal:** Resolve every credibility risk, citation-verification need, evidentiary gap, and
consistency error the 2026-07-06 corpus audit identified, without fabricating evidence,
coaching any witness statement, or reframing true content to sound better or worse.

**Approach:** Two tracks, run in the sequence the audit itself specifies (credibility/
citations first, then evidentiary gaps by rating-impact, then mechanical fixes). **Track A**
is document/citation work that can be done directly (by the assistant or a future session)
without anyone else's input. **Track B** is blocked on a decision or original content only
the veteran, a witness, or a licensed professional can supply — these tasks cannot be
completed by editing a file; they end when that person acts, and this plan can only track
and remind, not close them.

## Global Constraints (apply to every task below)

- **Never draft, script, reword, or suggest wording for any buddy/spouse/lay witness
  statement** — identify and hand back only, per `va-witness-statement-guide` and this
  corpus's hard rule (`CLAIM-ASSESSMENT.md` §0.2).
- **Never independently judge a legal/CFR/case citation** — every citation fix in Track A
  is gated on an actual `citation-verifier` CONFIRMED/MISSTATED result, not on this plan's
  own reading.
- **Never fabricate, exaggerate, or reframe true content** — every Track A fix is either a
  citation correction, a cross-reference update, or reflecting an already-established fact
  more completely; never a rewording to sound more/less severe.
- **Log every claim-facing document change in `DOCUMENT-PROVENANCE.md`.**
- Not legal advice — Track B items involving the VSO/attorney decision remain that
  professional's call, not this plan's.

---

## Track A — Actionable now (no one else's input required)

### Task A1: Complete the citation-verification queue

**Files:** all documents listed in `CLAIM-CORPUS-AUDIT-2026-07-06.md`'s "Citations needing
citation-verifier" section.

**Status:** 4 of the ~40 consolidated citations are already independently verified this
session (the OCD DC 9404/9403 resolution, and all citations in
`CREDIBILITY-INCONSISTENCY-RESEARCH.md` via an earlier dedicated pass). 4 parallel
`citation-verifier` dispatches are in flight for the remainder (priority re-checks
`Vazquez-Claudio`/`Bankhead`/`Barr v. Nicholson`; remaining case law `Mauerhan`/
`Mittleider`/`Rice`/`AZ v. Shinseki`; PTSD/MST regs; SUD/rating-mechanics regs).

- [x] **Step 1:** Done 2026-07-06 — `citation-verifier` re-checked all 10 outstanding
      citations (Vazquez-Claudio, Bankhead, Barr v. Nicholson, Mauerhan, Mittleider, Rice, AZ
      v. Shinseki, 38 CFR 3.304(f)(5)/3.310/3.306) against live primary sources.
- [x] **Step 2:** **No MISSTATED results in the current-generation documents.** All 10 are
      CONFIRMED as used in `100-PERCENT-SCHEDULAR-PATHWAY.md`, `MASTER-STRATEGY.md`, and
      `NEXUS-LETTER-GUIDE-CHERIE.md`. The "Vasquez-Claudio" misspelling and any other
      misstatements traced to the **superseded** `claim-maximization-research-2026-06.md`
      only — not corrected there per repo convention (kept for history, not for use); flagged
      here rather than silently edited.
- [x] **Step 3:** Resolved — the correct spelling is **"Vazquez-Claudio"** (confirmed against
      the official CAFC opinion caption, docket 12-7114). All three current working documents
      already use this spelling; no edits needed.
- [x] **Step 4:** One pincite remains UNVERIFIABLE (`Mittleider v. West`'s exact page
      pincite) — `100-PERCENT-SCHEDULAR-PATHWAY.md` already self-flags this; no further
      action needed.
- [x] **Step 5:** This remediation plan is the completion log; see
      `citation-verifier`'s full report (2026-07-06) for the per-citation table. The
      `CLAIM-CORPUS-AUDIT-2026-07-06.md` "priority re-check" flag on Vazquez-Claudio/Bankhead
      is closed — both confirmed correct in current docs.

### Task A2: Correct `COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 2 — Poquette quote

**Files:** `va-disability/COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 2.

**Finding:** The audit found `COMPREHENSIVE-FINDINGS-2026-07.md` quotes Poquette's
disclosure-timing language from a superseded draft, not the actual executed VA Form
21-10210 (`personal-records/supporting-docs/PocketBuddyLetterexportedtextfilled.pdf`,
signed 06/29/2026) — the executed form drops the in-service-disclosure sentence entirely.

- [x] **Step 1:** Confirmed 2026-07-06 — read the actual PDF text of
      `PocketBuddyLetterexportedtextfilled.pdf` directly (signed 06/29/2026, matches
      Poquette's contact info); this is the executed form.
- [x] **Step 2:** Done 2026-07-06 — `COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 2 now
      quotes the executed form's actual text and notes the dropped "2012"/in-service
      language.
- [x] **Step 3:** Done 2026-07-06 — new row added to `DOCUMENT-PROVENANCE.md`.
- [x] **Step 4:** Done 2026-07-06 — `MASTER-STRATEGY.md` item 14 now flags this.

### Task A3: Reconcile `MASTER-STRATEGY.md` staleness against `COMPREHENSIVE-FINDINGS-2026-07.md`

**Files:** `va-disability/MASTER-STRATEGY.md`.

**Finding:** `MASTER-STRATEGY.md` omits `COMPREHENSIVE-FINDINGS-2026-07.md` §0.8 (the
signed-document opioid contradiction) and §9a (disclosure-year conflict, Harmony Junction
stay-length mismatch, Erica surname discrepancy) from its own action-item list.

- [x] **Step 1:** Done 2026-07-06 — `MASTER-STRATEGY.md` item 13.
- [x] **Step 2:** Done 2026-07-06 — `MASTER-STRATEGY.md` item 14 (updated to reflect the
      Task A2 correction: it's no longer a simple year mismatch).
- [x] **Step 3:** Done 2026-07-06 — `MASTER-STRATEGY.md` item 15 (job-loss year was already
      covered by the pre-existing item 7).
- [x] **Step 4:** Done 2026-07-06 — `MASTER-STRATEGY.md` item 16.

### Task A4: Fix `COMPREHENSIVE-FINDINGS-2026-07.md`'s internal "#1 priority" contradiction and stale task list

**Files:** `va-disability/COMPREHENSIVE-FINDINGS-2026-07.md` §0.2, §9a item 1, §0, §10.

**Finding:** §0.2 and §9a item 1 both claim to be the corpus's single highest-priority
risk, on different severity axes, never reconciled. Separately, the F15.20 "zero
supporting narrative" claim in §0 is softened later in §9a without the original passage
being updated, and two self-flagged inconsistencies (Harmony Junction stay-length, CPT
worksheet age-arithmetic error) never got promoted into the document's own open-task list.

- [x] **Step 1:** Done 2026-07-06 — cross-reference added at §0.2 and §9a item 1.
- [x] **Step 2:** Done 2026-07-06 — §0.6 now uses the softened language.
- [x] **Step 3:** Done 2026-07-06 — §10 items 17–18 added (plus item 19 for the §0.10
      records-release finding, not originally scoped in this task but the same gap pattern).

### Task A5: Add missing `DOCUMENT-PROVENANCE.md` entries for research/strategy docs

**Files:** `va-disability/DOCUMENT-PROVENANCE.md`.

**Finding:** 7 of 16 audited documents are absent from the provenance log
(`CP-EXAM-PREP-MENTAL-HEALTH.md`, `NEXUS-LETTER-GUIDE-CHERIE.md`,
`CREDIBILITY-INCONSISTENCY-RESEARCH.md`, `100-PERCENT-SCHEDULAR-PATHWAY.md`,
`SLEEP-APNEA-SECONDARY-CLAIM.md`, `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`, `DD214`). Most
are correctly out of that log's original claim-facing scope, but `PRE-POST-SERVICE-
SEVERITY-CONTRAST.md` proposes suggested first-person language for the signed personal
statement — exactly what the log exists to track.

- [~] **Step 1:** Not yet done as of 2026-07-06 — `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`
  still has no row in `DOCUMENT-PROVENANCE.md`. Remaining Track A work.
- [~] **Step 2:** Not yet decided. Recommend: **no** (keep the log scoped to witness/veteran
  statements) — add a one-line scope clarification to the header instead of rows for the
  6 research/strategy docs, since none of them raise an authorship question. Remaining
  Track A work.

### Task A6: Fix `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`'s completeness gap

**Files:** `va-disability/PRE-POST-SERVICE-SEVERITY-CONTRAST.md`.

**Finding:** The document builds its pre/post-service contrast entirely from the Starlite
record and never mentions the 2018 Victory Addiction Recovery Center's conflicting
self-report of first opiate/heroin use at age 18 (2007) — the one record that most
complicates the "kratom-only" narrative it recommends. It also overclaims relapse-cause
uniformity and miscounts total treatment admissions.

- [x] **Step 1:** Done (pre-existing, confirmed 2026-07-06) — `PRE-POST-SERVICE-SEVERITY-
CONTRAST.md` now addresses the duty-to-assist/release mechanics explicitly.
- [x] **Step 2:** Confirmed done 2026-07-06 by an independent `claim-consistency-checker`
      pass — the relapse-cause uniformity overclaim is now softened and matches §5.
- [x] **Step 3:** Confirmed done 2026-07-06 by the same pass — admission count corrected
      to "at least nine," cross-checked and consistent with `COMPREHENSIVE-FINDINGS-2026-07.md`'s
      chronology (a full-corpus grep confirmed all remaining "five admissions" references
      correctly scope to the five _Starlite_ admissions specifically, not a total count).
- [x] **Step 4:** Done (pre-existing) — the file already cross-references §0.8/Task B1.

### Task A7: Add the SI-frequency discrepancy to `NEXUS-LETTER-GUIDE-CHERIE.md` §7

**Files:** `va-disability/NEXUS-LETTER-GUIDE-CHERIE.md` §7.

**Finding:** The three conflicting suicidal-ideation data points (5/14/26 FMLA eval "denies
current SI... history of passive SI"; 6/17/26 personal statement "hits every day"; ~6/25/26
chart note "denies SI") **[RETRACTED 2026-10-08: no 6/25/26 SI denial exists — see CLAIM-ASSESSMENT.md §0.2]** are only partially rehearsed elsewhere in the corpus and omitted
entirely from this document's "flag for her awareness" section, despite that section's
purpose being exactly to prevent this kind of surprise.

- [x] **Step 1:** Done 2026-07-06 — third bullet added to §7 (header also updated from
      "Two things" to "Things" since it's now three).

### Task A8: Complete the CP-exam prep document's landmine list

**Files:** `va-disability/CP-EXAM-PREP-MENTAL-HEALTH.md`.

**Finding:** The document rehearses the trauma-disclosure cross-exam category generically
rather than naming the specific instances most likely to be probed (2015 explicit MST
denial + 0/4 PC-PTSD screen; two 2018 Victory intake denials), and has no prep at all for
the pre-service age-18 psychiatric/substance-use question, the unexplained F15.20 diagnosis,
or the "gainfully employed" (Aug 2024) vs. occupational-collapse sequencing question.

- [x] **Step 1:** Done 2026-07-06.
- [x] **Step 2:** Done 2026-07-06.
- [x] **Step 3:** Done 2026-07-06.
- [x] **Step 4:** Done 2026-07-06.

---

## Track B — Blocked on someone else's input (track and remind only; cannot be closed by editing a file)

### Task B1: VSO/attorney decision on the signed document's inaccuracies — **RESOLVED 2026-07-06 (veteran confirmation)**

**Was blocked on:** veteran + VSO/VA-accredited attorney. **Resolved per the veteran's direct
confirmation (2026-07-06):** the corrective steps for the signed document's inaccuracies have
been handled with the VSO/attorney. This plan doesn't independently know the specific
mechanism used (corrective supplemental statement, addendum, or otherwise) — that was the
professional judgment call this task always deferred to — but the open decision itself is
closed. See `COMPREHENSIVE-FINDINGS-2026-07.md` §0.8/§0.10/§0.12 and `MASTER-STRATEGY.md`
item 13, both updated to reflect this.

The three items this covered:

1. The opioid-recollection contradiction (§0.8), informed by
   `CREDIBILITY-INCONSISTENCY-RESEARCH.md`'s legal analysis. Per that document's own open
   question, the specific characterization ("incomplete recollection") needs to be checked
   against the veteran's actual, honest recollection before being used — not assumed.
2. **NEW (2026-07-06):** the §10.1 evidence-list claim that a VA Form 21-4142/21-4142a
   release was submitted for Victory Recovery Center and Starlite Recovery Center —
   confirmed inaccurate by the veteran and VSO; no such release was ever filed for those
   two facilities (only for individual providers).
3. **NEW (2026-07-06):** the personal statement and the 21-0781 don't even agree with
   _each other_ on which facilities the release covers — the 21-0781 names only Starlite
   and Cherie Mills; the personal statement adds Victory (§0.12). Any corrective filing
   needs to address both documents, not just the personal statement.

All three were inaccuracies/inconsistencies in the same pair of signed documents; per the
veteran's confirmation, the VSO/attorney decision on how to address them has been made and
executed.

### Task B2: Erica's independent statement rewrite

**Blocked on:** Erica.
**What unblocks it:** Erica producing a fresh statement from a blank page or the
open-ended `Spouse-Statement-Guide-and-Template-Erica.pdf`, with no reference to the
current AI-drafted text in `Erica Personal Statement.md` or
`Spouse_Statement_Draft_Erica.converted.txt`. If genuinely already done independently, the
open question is why the file still contains the unedited "Notes" section describing
itself as a first draft — that needs a real answer before this is treated as closed.
**This plan's role:** once a genuinely new, textually-independent version exists, update
`DOCUMENT-PROVENANCE.md` to log the new artifact's real origin, and mark the current
`Erica Personal Statement.md`/`Spouse_Statement_Draft_Erica.converted.txt` as superseded
(or deleted, per the veteran's decision in Task B3).
**STATUS (2026-07-06, per the veteran):** the statement is being finalized to include concrete
examples Erica can factually recall herself. No file has been provided to this corpus yet —
this is a status update, not a received document. Once the file exists, apply this plan's role
above.

### Task B3: Decide whether to delete/mark superseded the scripted Erica draft

**Blocked on:** veteran (a housekeeping decision, but one that shouldn't be made
unilaterally given it touches evidence).
**What unblocks it:** a decision on whether `Spouse_Statement_Draft_Erica.converted.txt`
should be deleted or clearly marked superseded, given the corpus's own guidance already
favors the open-ended guide/template instead.

### Task B4: Erica's correct legal surname and job-loss year

**Blocked on:** Erica/veteran.
**What unblocks it:** a direct confirmation of "Jure" vs. "Klein," and the correct
job-loss year (2024 vs. 2025), currently inconsistent across signed documents and drafts.

### Task B5: Reyes/Poquette disclosure-year reconciliation

**Blocked on:** Wilfredo Reyes and Zachary Poquette, independently, in their own words.
**What unblocks it:** each witness reviewing the conflict (2012 vs. "late 2013") and
stating what they actually recall — not something to draft or resolve on their behalf.
Route through `va-witness-statement-guide` (open-ended questions only) if either witness
needs help getting started.

### Task B6: Reyes's own DD-214/service-date confirmation

**Blocked on:** Wilfredo Reyes.
**What unblocks it:** Reyes providing his own separation date/service record to confirm
overlap with the "late 2013, while we were both still serving" disclosure window.

### Task B7: Reyes's unit-name correction in his signed statement

**Blocked on:** Wilfredo Reyes (it's his signed document; only he can correct or re-sign
it).
**What unblocks it:** Reyes re-executing or amending his VA Form 21-10210 to read "4th
Equipment Maintenance Squadron" per the DD-214, or explaining/confirming the AMU-vs-squadron
distinction if that's what he actually meant.

### Task B8: Obtain Goff's buddy statement

**Blocked on:** Liam Goff.
**What unblocks it:** Goff providing his own independent account, in his own words, per
`va-witness-statement-guide` if he needs a prompt to get started.

### Task B9: Sleep study / OSA diagnosis

**Blocked on:** veteran + a medical provider.
**What unblocks it:** scheduling and completing a polysomnography (private home test is
the faster route per `SLEEP-APNEA-SECONDARY-CLAIM.md`) — a hard legal prerequisite for the
secondary claim, not optional.

### Task B10: Formal PTSD diagnosis from Cherie Mills — **RESOLVED 2026-07-06**

**Was blocked on:** Cherie Mills, LCSW (clinical judgment). **Delivered:** her signed nexus
letter (`personal-records/supporting-docs/nexus-letter-cherie.md`, dated 2 July 2026)
contains an actual diagnosis of PTSD (plus MDD, GAD, OCD, SUD) — not just a nexus opinion
assuming one exists. This was the single most important open item across the entire corpus;
see `document-analysis/nexus-letter-cherie-ANALYSIS.md` for the full review.
**Remaining items closed 2026-07-06:** the credibility question about the SUD sentence is
resolved — see Task B14 below. The three identifying-info errors (DOB, name spelling, phone
number) are confirmed by the veteran as minor and not a submission blocker.

### Task B11: Cherie Mills's competency to opine on OSA causation

**Blocked on:** Cherie Mills + veteran.
**What unblocks it:** confirming whether she's comfortable opining on a sleep/pulmonary
mechanism outside her core specialty, or whether the OSA nexus opinion should come from a
sleep specialist instead.

### Task B12: In-service ankle injury witness corroboration

**Blocked on:** veteran (finding a witness) — Poquette's statement is "100% MST-focused"
and doesn't cover this.
**What unblocks it:** a different lay statement or STR confirmation of the in-service
ankle injury/hospital trip.

### Task B13: NEW (2026-07-06) — Awareness item: the signed personal statement's own claim about Poquette isn't borne out by his executed statement

**Blocked on:** nothing to fix by editing a file — the personal statement is already signed.
**What this is:** found by an independent `claim-consistency-checker` pass (§0.11). The
signed personal statement's §4 states Reyes _and_ Poquette would confirm disclosure
"while we were still in service together." True of Reyes; not true of what Poquette's
executed VA Form 21-10210 actually says (no in-service language, no date anchor). This is
a fact for the veteran/VSO to be aware of when assessing the file's overall coherence —
not a task with a completion condition, since the underlying signed document can't be
edited. Distinct from Task B5 (which is about Reyes and Poquette reconciling with _each
other_, not about the personal statement's own claim about them).

### Task B14: Confirm whether Cherie's SUD nexus sentence is independent or adopted template language — **RESOLVED 2026-07-06**

**Was blocked on:** Cherie Mills (a direct, honest answer). **Resolved per the veteran's
direct confirmation (2026-07-06):** the sentence is Cherie's own — she did her own
independent research into how to write a nexus letter, which explains the close wording match
to this corpus's internal guide template as convergence on standard/expected phrasing, not
adopted or coached language. The `va-claim-document-analyst` finding
(`document-analysis/nexus-letter-cherie-ANALYSIS.md`, score 4/10, CRITICAL flag) correctly
identified a pattern that needed asking about directly rather than assuming either way — that
question has now been asked and answered. The SUD opinion can be treated as her own
independent clinical judgment.
Depending on her answer, the veteran/VSO may want to ask her for a corrected addendum letter
that also fixes the DOB/name/phone errors (Task B10) and restates the SUD rationale in her
own words for the version actually submitted.

### Task B15: Confirm with Cherie whether/how two confirmed delusions (persecutory and grandiose) should be reflected in the clinical record — **UPDATE (2026-07-06): expected near-term correction**

**Blocked on:** Cherie Mills (or whichever treatment provider is already aware) + veteran.
**What this is:** the veteran describes two distinct confirmed delusions, at different stages of
documentation:

1. **Persecutory** — a fixed, certain belief that a specific person is following him and plans
   to kill him over something from ~18 years ago, plus corresponding protective plans (a nuclear
   bunker). Confirmed as a fixed belief, not an anxious overestimation. A treatment provider is
   aware of it, but it's not yet in Cherie's signed letter or documented notes as far as this
   corpus can see.
2. **Grandiose** — a belief in special importance, power, or a special mission/identity.
   Confirmed as **already part of Cherie's own clinical assessment** — a materially different
   confirmation status than item 1 — but also not yet in her signed letter.

Neither is a standard PTSD/GAD/MDD/OCD symptom. See `COMPREHENSIVE-FINDINGS-2026-07.md` §0.14
for the full context and why this needs care, not just logging as evidence.
**What unblocks it:** confirm directly with Cherie (a) whether both are reflected in her ongoing
treatment notes and current diagnostic picture — especially the persecutory one, whose
documentation status is less clear than the grandiose one — and (b) whether her letter/diagnosis
should be supplemented or amended to accurately capture what she's already assessed. **This
should happen before the exam** — introducing symptoms this specific and severe for the first
time at the exam, with no grounding in the letter actually in hand, is the same credibility-risk
pattern this corpus has flagged elsewhere, and more importantly, his actual care shouldn't wait
on the claim timeline.

**Update (2026-07-06, per the veteran):** confirmed expected, not just requested — Cherie will
update her letter to reflect both delusions, and Erica's forthcoming statement is expected to
independently corroborate them. Carrying this forward as an **expected near-term correction**
(one tier more confident than "not yet requested," per the same convention
`PROJECTED-REASSESSMENT-2026-07-06.md` uses for the Poquette/Cherie corrections there) — the
actual content of Cherie's updated letter and Erica's statement isn't yet in hand, and the value
of both still depends on what they specifically say, not a guarantee of any particular wording.
Neither should be told what to say; the expectation here is that the correction/corroboration
happens, not what it specifically states.

---

## Sequencing

1. **Now:** Track A1 (citation queue) — already dispatched, in progress.
2. **Immediately after A1 resolves:** A2 (Poquette quote correction) — highest-value single
   fix, corrects the corpus's own ground-truth document.
3. **In parallel with the above:** A3–A8 (staleness/consistency/gap fixes) — none depend on
   A1/A2 completing first.
4. **Ongoing, not sequenced (surface reminders, don't block Track A on them):** B1–B14 —
   these depend entirely on other people's timelines. Re-check status the next time
   `/va-claim-status` or a fresh corpus audit runs.

## Self-Review

- **Spec coverage:** every item in the audit's Credibility Risks, Cross-Document Findings,
  Evidentiary Gaps, and Open Questions sections maps to a task above (A1–A8, B1–B12).
- **Placeholder scan:** every Track A step names the exact file and the exact fix; every
  Track B task names exactly who it's blocked on and what unblocks it — no "TBD" or
  "handle appropriately" language.
- **No task asks anyone to draft witness-statement wording, reframe true content, or judge
  a citation without `citation-verifier`.**
