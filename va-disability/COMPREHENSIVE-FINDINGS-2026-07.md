# Comprehensive Findings — VA Disability Claim (Full Corpus Read, 2026-07-05)

> **Purpose of this document:** this is a full synthesis of _every_ file in this repository's
> `va-disability/` tree — the prior strategy docs (`veteran-profile.md`, `strategy.md`,
> `knowledge-base.md`, `resources.md`, `CLAIM-EXECUTION-PLAN.md`, `claim-maximization-research-2026-06.md`),
> the `ClaudeChat/` transcript, the entire `ClaudeDisabilityAssets/` strategy-prep folder, and
> **every personal record** — DD-214, buddy/spouse statements, VBA-21-0781 drafts, DASS-21/psych-eval/FMLA
> documents, the Erica email chain, VA clinical records, and ~600 pages of scanned treatment records from
> Victory Addiction Recovery Center (2018) and Starlite Recovery Center (five separate admissions,
> 2022–2025). It supersedes and updates `veteran-profile.md` and `strategy.md` in the places noted below.
> It is written to be handed directly to a `/deep-research` pass and then a `/make-plan` session.
>
> **Not legal advice.** Execute with a VSO or VA-accredited attorney.

---

## Canonical facts (single source of truth — cite this, don't re-state)

- **Claim dates:** received **19 May 2026**; VA development letter **29 May 2026**. The VA-recorded receipt date governs the effective date — confirm at the eFolder pull.
- **WHODAS 2.0:** in-hand, self-administered vendor functional instrument (~69.72% overall; self-care 62.5%); auto-scored — **NOT** psychologist-signed, not a GAD/MDD subscale test, not a broken/expired export.
- **Odds anchor (per `PATH-TO-100-PERCENT-2026-07-07.md` §9 — REASONED ESTIMATES):** 70% ≈ 90%+, 90% ≈ 60–70%, 100% MH-alone ≈ 40–50%, 100% combined ≈ 50–60%.
- **PTSD diagnosis:** supplied by Cherie's signed **2 July 2026** letter.
- **Route 2 framing:** modestly higher-probability than Route 1 **if the sleep study is positive**; inherits the 90%-MH burden; **not a safe fallback**.
- **Married-veteran BVA balance:** 3 adverse vs 1 favorable — a non-representative sample, **not** weight-of-authority.

Future documents should cite this block rather than re-stating these facts, to prevent drift.

---

## 0. READ THIS FIRST — Critical, time-sensitive, and high-risk items

### 0.1 Filing-clock alert (URGENT — verify immediately)

Per the `ClaudeDisabilityAssets` digest: a **supplemental claim was received by VA on May 19, 2026**, a
**development letter went out May 29, 2026**, with a **soft evidence deadline of ~June 28, 2026** — which
is **already past** as of today (2026-07-05). **Confirm the current status of this claim on VA.gov or with
the VSO immediately.** If the deadline has lapsed without full evidence submission, find out whether VA is
proceeding to a decision on the existing record, whether an extension was granted, or whether a C&P exam has
already been scheduled. This is more time-critical than anything else in this document.

### 0.2 The single biggest credibility risk in the entire file set

The `EricaPTSDLetterEmailChain.pdf` digest found that Marcus's own edits to Erica's draft VA Form 21-10210
lay statement go well beyond proofreading. Specific instructed changes include:

- "I need to be portrayed as being incapable of social and occupational tasks **to the furthest extent
  possible**"
- An instruction to keep her statement **consistent with what he's separately telling therapist Cherie
  Mills and telling military friends for their buddy letters** — i.e., coordinating the narrative across
  independently-sourced evidence
- Reframing true, benign facts to sound worse (e.g., "stayed up working" rewritten to "stayed up playing
  video games," recasting overwork as trauma-avoidance rather than ambition)
- An instruction to run the final draft through an LLM specifically to avoid tripping the SUD "willful
  misconduct" bar
- Explicit instruction to omit any reference to "abuse during service" outside of alcohol consumption

VA Form 21-10210 is signed **under penalty of perjury**. This document's own prior research
(`claim-maximization-research-2026-06.md`) treats manufacturing or coaching evidence like this as a
potential violation of 18 U.S.C. § 1001 and 38 U.S.C. § 6103 (**corrected 2026-07-06**: the prior
draft of this passage misattributed the specific "paradigm case of VA benefits fraud" superlative to
coached witness statements — that source document's own "Fraud Line" section (line 157) actually
reserves that framing for a different scenario, staging a sham employment transition to manufacture
TDIU eligibility. Coached witness statements are listed among the same document's § 1001/§ 6103
concerns, just not singled out with that specific phrase. The substantive conclusion below is
unaffected — coached evidence is a real, serious fraud exposure either way — only the sourcing of
the superlative needed correcting; see `document-analysis/COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`
and the 2026-07-06 citation-verifier pass for the full finding). This would **cross-contaminate the
credibility of the entire MST/PTSD claim**, which
rests almost entirely on personal credibility given the ~12-14 year disclosure gap and non-disclosure
across nearly every clinical record reviewed (see §3 below). **This should be resolved before the spouse
statement is finalized or submitted** — Erica's statement should describe only what she has personally
observed, in her own words, without instruction on how to frame or omit facts. If this email chain were
ever produced in discovery or an adversarial review, it is difficult to overstate how damaging it would be.
This is not a moral aside — it is the largest concrete threat to the compensation outcome identified
anywhere in this corpus.

**Cross-reference (added 2026-07-06, Track A4):** §9a item 1 below separately flags the signed personal
statement's opioid-recollection contradiction as "the highest-priority item" on its own list. These are two
different, both-live risks on different axes — this section (§0.2) is about witness-coaching process/
credibility exposure; §9a item 1 is about a signed document's factual accuracy — not competing claims to the
single "#1 risk" in the corpus. Both need resolving; neither supersedes the other.

### 0.3 The MST stressor narrative directly conflicts with a 2015 VA record

A **2015-09-21/22 VA record** (Jennings CBOC, LA — `VA Clinical Summary.pdf` / `...0329am.pdf`) contains:

- **An explicit clinician-recorded statement: "Patient denies experiencing military sexual trauma (MST) in
  the past."**
- A **PC-PTSD 4-question screen: negative, 0/4** (no nightmares/avoidance/hypervigilance/numbness)
- A **PHQ-2 depression screen: negative, 0**
- An **AUDIT-C: negative, 3**
- No PTSD or depression diagnosis entered at all; mood recorded as "content"

This is a **formal, VA-generated baseline screen**, same-day as an explicit MST denial, negative across
every mental-health domain that would now be central to the claim. Separately, the **2018 Victory Addiction
Recovery Center intake** (two different standardized forms, 8/25/18 and 10/1/18) also has Marcus **explicitly
denying any history of physical, emotional, sexual, financial, or verbal abuse, exploitation, or "traumatic
event."** The **January 2022 Starlite intake** is internally self-contradictory (see §3.2). Every 2023
Starlite admission has trauma/abuse checkboxes **unchecked/"None Reported."** Only the 2026 claim materials
(21-0781, personal statement, buddy statements from Reyes/Poquette) describe the 2012 sexual assault.

**This is legally survivable** — delayed disclosure is itself a recognized behavioral marker under
38 CFR 3.304(f)(5), and _AZ v. Shinseki_ holds non-disclosure is not affirmative negative evidence — but it
is **not optional to address**. Cherie Mills's nexus letter and the personal statement need to affirmatively
explain the 2015 explicit denial and the repeated "none reported" trauma screens, using the recognized
clinical literature on delayed male-MST disclosure (already cited in the existing Cherie-letter guides).
Leaving this for a VA rater or C&P examiner to discover unaddressed is the second-largest risk in the file.

**The veteran's own explanation (2026-07-06):** he states the denials reflect genuine denial and active
avoidance of discussing the assault at the time — not a fabricated cover story — and that this is a
recognized, common pattern specifically for male MST survivors. Cherie Mills is able to corroborate this
clinically from her own treatment relationship with him. Her received nexus letter already states this
kind of framing generally ("commonly not categorized... as 'assault,'" `personal-records/supporting-docs/
nexus-letter-cherie.md`); the veteran's own personal statement / C&P exam answer should say the same thing
in his own words — denial and avoidance, not concealment of a fabricated event.

### 0.4 The SUD "iatrogenic onset" theory conflicts with self-reported age-18 first use

The personal statement and multiple prep documents lean on a theory that the May 2011 in-service ankle
fracture (oxycodone prescription) is an origin point for opioid use. But:

- **2018 Victory Addiction Recovery Center records:** patient self-reports **first opiate/heroin use at age
  18** (2007, ~2 years _before_ his November 2009 enlistment).
- **January 2023 Starlite records:** patient self-reports GAD and MDD diagnosed at age 18, and separately
  states substance use "began at the age of 18 with Kratom."
- **January 2022 Starlite records:** "escalated to opioids at 25" is recorded in one note (Dec 2024 Starlite
  chart), which conflicts with the age-18 self-report elsewhere.

This doesn't kill the theory — the personal statement pleads SUD in the alternative (Allen-secondary to
PTSD/MDD/GAD; aggravation under 3.306; direct iatrogenic OUD from the 2011 Rx) precisely because multiple
paths exist — but the **iatrogenic/direct theory specifically is weaker than the file set currently assumes**,
since it requires the record to show opioid use _starting_ from the 2011 prescription, and it does not.
The secondary-to-PTSD/MDD/GAD (_Allen v. Principi_) theory is not undermined by this and should be the
lead theory, consistent with what `C_Master_Rating_Strategy.pdf` already recommends.

**Escalation (2026-07-05 — see §0.8):** this isn't only a weak theory in strategy documents anymore. The
claim-consistency-checker pass confirmed the denial is asserted as fact in the **signed, dated (06/17/2026)
personal statement** and the **actual VA Form 21-0781** — both already submitted or submission-ready. See
§0.8 for the specifics and why this changes the urgency of resolving this from "pick the better theory" to
"decide what to do about an already-signed document that asserts the weaker one."

**NEW clarification per the veteran (2026-07-06):** in addition to the Kratom self-report above, there was a
**separate, distinct pre-service episode** — a medication prescribed for an unrelated reason, which the
veteran states he did not know was an opioid until told so later, during treatment. Per the veteran, this
prescribed use caused **zero substance-use disorder or associated problems at the time** — it was taken as
directed, with no misuse. The veteran states his actual SUD (the diagnosable disorder) only began **after
discharge and after the 2012 in-service assault** — consistent with the secondary-to-PTSD/MDD/GAD theory,
not a pre-existing disorder. **This is the veteran's own account, not yet corroborated by a specific document
in this corpus** — no Victory/Starlite record reviewed so far describes a prescribed medication this way
(the existing self-reports describe "first opiate/heroin use at age 18" and "Kratom" without this framing).
This isn't a contradiction to resolve by picking one account over the other — both the clinical records'
phrasing and the veteran's fuller account can be true simultaneously (a prescribed medication is a distinct,
separate fact from recreational Kratom experimentation) — but the veteran's fuller context should be reflected
honestly in his own personal statement and in what he tells Cherie/the C&P examiner, since the bare clinical-
record phrasing alone reads more ambiguously than his actual account.

### 0.5 OCD is a real, clinically diagnosed condition — but it's missing from the claim's core documents

Multiple Starlite records (Jan 2023 intake, July–August 2023 admission, and the July–August 2024 admission)
formally diagnose **F42.2 — Obsessive-Compulsive Disorder**, alongside GAD and MDD. The patient
self-reports it was diagnosed "recently" as of January 2023 by "my psychiatrist" (almost certainly Cherie
Mills, LCSW, or a co-treating prescriber). **However, OCD is completely absent from:**

- The finalized personal statement (21-0781 narrative)
- The C&P exam prep sheet
- The earliest nexus-letter guides for Cherie (only the three most recent Cherie-guide documents mention it)

This is a synchronization gap, not a fabrication risk — the diagnosis is real and well-documented in
clinical records — but it needs to be **explicitly incorporated into the personal statement and the C&P
exam prep** before any exam, and confirmed with Cherie Mills that she is prepared to speak to it (VA rates
OCD under the same § 4.130 general formula as PTSD/MDD/GAD, so it folds into the single mental-health
rating rather than adding separately — but the _symptoms_ of OCD, once documented, materially strengthen the
overall severity picture toward 70%).

### 0.6 An unexplained "Amphetamine-type Substance Use Disorder, Severe" diagnosis

The April–May 2026 Harmony Junction Recovery discharge summary lists **F15.20 — Amphetamine-type substance
use disorder, Severe** — a diagnosis that **appears nowhere else** in any of the ~600 pages of other
records. **Corrected 2026-07-06 (Track A4):** the discharge summary itself does contain one passing phrase
— "stabilization from polysubstance use involving opioids, benzodiazepines, and stimulants" (page 2) — so
"zero supporting narrative" is slightly overstated; the accurate characterization is **essentially
unsupported, with one unelaborated mention** (one word, no elaboration, no corroborating self-report
anywhere else in the record). This softening doesn't change the recommendation below. This needs to be
resolved directly with Harmony Junction (confirm whether this is a coding error, or reflects an undisclosed
stimulant use episode) before any of these records are submitted to VA — an unexplained severe SUD
diagnosis with no clinical support is exactly the kind of loose thread an adversarial C&P examiner or rater
could seize on.

### 0.7 The WHODAS 2.0 functional assessment file is corrupted — **RESOLVED 2026-07-07 (real file now in hand; see the 2026-07-07 update below)**

`personal-records/supporting-docs/psych-assessments-extracted/Recent Psych Assessments/Marcus-WHODAS_2_0-11Jun2026.pdf`
is not a real PDF — it contains only an expired AWS S3 pre-signed-URL error. This is the **only** WHODAS
functional-assessment data point referenced anywhere in the file set (it's listed as "provided" in
`Materials_Reviewed_for_Cherie.pdf`, but the actual file is unusable). **Re-download this from whatever
platform generated it** (likely the "Recover" FMLA-vendor portal, since the DASS-21 and psych-eval documents
trace to the same source) before it's needed for the claim.

**UPDATE (2026-07-06):** per the veteran, a signed WHODAS 2.0 assessment from a psychologist now exists,
confirming high-severity GAD and MDD scores on each subscale. **No file has been provided to this corpus
yet** — this is a status update, not a received document. Once the actual file is available, add it to
`personal-records/supporting-docs/` and get it reviewed (via `va-claim-document-analyst`, the same process
used for the nexus letter) before treating its specific figures as confirmed for use in the claim.

**UPDATE (2026-07-07) — the actual file is now in hand, and it corrects both notes above.** The real WHODAS 2.0
report (`personal-records/supporting-docs/Marcus-WHODAS_2_0-11Jun2026.pdf`, 11 Jun 2026) has been received and
read directly — a valid 10-page PDF, not the corrupted S3 export. Two corrections: (1) it is a
**self-administered, auto-scored functional-disability instrument from the "Recover" leave-support vendor —
NOT a psychologist-signed diagnostic**, and it measures functional disability (diagnosis-agnostic), not
"GAD/MDD subscale scores"; (2) **overall functional disability ≈ 69.72%** (complex scoring), all six domains
in the "high functional limitations" band (understanding 70.83%, mobility 65%, self-care 62.5%, getting-along
70%, life-activities 75%, participation 75%; the item "making new friends" scores "extreme / cannot do"). It
is the first objective corroboration of the ADL/hygiene 100%-tier anchor (self-care domain) and the
total-social-impairment prong (social domains), with the usual vendor-self-report weight caveats (§1.2). Full
assimilation and strategic use: `PATH-TO-100-PERCENT-2026-07-07.md` §11 / I-14; logged in
`DOCUMENT-PROVENANCE.md`. If a separate, genuinely psychologist-signed assessment also exists (the veteran's
original description), `MarcusKleinPsychEval.pdf` in the extracted psych-assessments folder may be it and is
worth reviewing. **Also confirmed 2026-07-07:** the **DASS-21 (09 Jun 2026) is likewise in hand** — Depression
36 / Anxiety 34 / Stress 38, all "Extremely severe," 98–100th percentile — which resolves the §6 / §10-item-6
re-export task for the symptom-severity instrument as well.

### 0.8 NEW (2026-07-05) — Signed documents already assert the contradicted opioid-origin claim

A `claim-consistency-checker` pass that read the actual signed forms (not just strategy drafts) found this
is a live exposure in executed documents, not a theory to fix in a future letter:

- **Signed personal statement** (06/17/2026), `personal-records/supporting-docs/VBA-21-0781-Signed-Personal-
Statement-Finalized.converted.txt` §6 and §9.2(c): _"I don't recall having taken opioids before 2011"_ /
  _"I have no recollection of using opioids before active duty."_
- **VA Form 21-0781** itself, `personal-records/supporting-docs/VBA-21-0781-revised.pdf`, Section III item
  10B: _"Exposed to many opioids during service following 2011 ankle injury... Led to post discharge abuse
  related to MST event."_

Both directly contradict the age-18 self-reports documented at §0.4. If Cherie's nexus letter now leads with
the self-medication/secondary theory (correct clinical call), it will sit next to a signed prior statement
asserting the opposite fact pattern under penalty of perjury. **This was a decision for the veteran and a VSO
/ VA-accredited attorney — whether to proactively submit a corrective/clarifying supplemental statement, or
address it another way.** **RESOLVED 2026-07-06 (veteran confirmation):** this has been addressed with the
VSO/attorney. See `CORPUS-AUDIT-REMEDIATION-PLAN-2026-07-06.md` Task B1.

### 0.9 Other new findings from the 2026-07-05 claim-consistency-checker pass (see §9a for full list)

Ranked below §0.8 in severity but still worth resolving before filing/exam: a **disclosure-year conflict
between the two buddy statements** (Reyes: late 2013; Poquette: 2012, with internal ambiguity), **Reyes's
unit name fix still not applied** to the actual signed PDF despite being an open task since an earlier pass,
a **Harmony Junction stay-length mismatch** (25 days claimed vs. ~24 computed from the discharge summary's
own dates), the **spouse referred to by two different surnames** ("Erica Jure" vs. "Erica Klein") across
documents meant to go to VA together, and a **minor age-arithmetic slip** in the CPT Impact Statement. Full
detail in the new §9a below.

### 0.10 NEW (2026-07-06) — Signed personal statement's records-release claim is confirmed inaccurate

The signed personal statement (§10.1, "Submitted with this claim") states: _"VA Form 21-4142 and 21-4142a
authorizing release of records from Victory Recovery Center, Starlite Recovery Center, and Cherie Mills,
LCSW."_ **Confirmed 2026-07-06, veteran + VSO:** no release was ever submitted for Victory Recovery
Center or Starlite Recovery Center specifically — releases were only submitted for individual treating
providers/psychiatrists. This is a **third confirmed inaccuracy in the same signed document**, alongside
the §0.8 opioid-recollection contradiction.

**Practical consequence:** with no release on file for the treatment centers, VA currently has no
independent channel to pull those records directly — whatever the veteran submits himself (per his own
stated plan: he has an existing relationship with both facilities and is retrieving and submitting the
records manually) is the complete record VA will see initially. This does **not** relax the curation-vs-
cherry-picking guidance in `PRE-POST-SERVICE-SEVERITY-CONTRAST.md` — VA can still request a release for
these facilities later (especially if the record references treatment not otherwise documented), which
would reactivate the original duty-to-assist cross-check risk retroactively against whatever was already
submitted.

**RESOLVED 2026-07-06 (veteran confirmation):** this has been addressed with the VSO/attorney alongside
the §0.8 opioid-recollection correction and the §0.12 cross-document release-scope discrepancy. See
`CORPUS-AUDIT-REMEDIATION-PLAN-2026-07-06.md` Task B1.

### 0.11 NEW (2026-07-06) — The signed personal statement's own §4 claim about Poquette is not borne out by what Poquette actually signed

Found by an independent `claim-consistency-checker` pass verifying the Track A2 correction against the
primary documents directly. The **signed** personal statement (06/17/2026) §4 states: _"Wilfredo Reyes and
Zach Poquette have agreed to provide buddy statements under VA Form 21-10210 confirming that I disclosed
the assault to them **while we were still in service together**..."_ Poquette signed his statement 12 days
later, on 06/29/2026 — and his executed statement (see §9a item 2 above) contains **no** "while we were
still in service" language and no date anchor at all. Reyes's statement does affirmatively say this
("In late 2013, while we were both still serving..."), so the claim is true of Reyes but not of Poquette.

This is a distinct fact from the Reyes/Poquette disclosure-timing disagreement already tracked at §9a item
2 — it's not "the two witnesses disagree with each other," it's **the veteran's own already-signed
statement making a claim about what its corroborating evidence would show that one of the two named pieces
of evidence doesn't actually show.** The personal statement can't be edited after signing; this is
information for the veteran/VSO to be aware of, not something to fix by editing a file. Tracked as Task B13
in `CORPUS-AUDIT-REMEDIATION-PLAN-2026-07-06.md`.

### 0.12 NEW (2026-07-06) — The personal statement and the 21-0781 disagree with each other on which facilities the records release covers

Also found by the same pass, reading `personal-records/supporting-docs/VBA-21-0781-revised.pdf` directly.
Its Section V Remarks (Item 14) states: _"VA Forms 21 4142/4142a authorizing release of Starlite Recovery
Center and current civilian LCSW records"_ — no Victory Recovery Center. But the signed personal statement
§10.1 (§0.10 above) claims releases for **both** Victory _and_ Starlite. §0.10 already established neither
release was actually filed — this adds that the veteran's own two signed/submission-ready documents, filled
out around the same time, don't even agree with **each other** about which facilities the claimed release
covers, independent of either being contradicted by reality. **RESOLVED 2026-07-06 (veteran confirmation):**
addressed alongside §0.8/§0.10 as part of the same Task B1 resolution.

### 0.13 NEW (2026-07-06) — Cherie Mills's nexus letter received; SUD-sentence credibility question RESOLVED

Cherie Mills's signed nexus/diagnosis letter (`personal-records/supporting-docs/nexus-letter-cherie.md`,
dated 2 July 2026) has arrived and delivers this document's single most-flagged open item — an actual
clinical PTSD diagnosis (plus MDD/GAD/OCD/SUD), not just a nexus opinion assuming one. Full review:
`document-analysis/nexus-letter-cherie-ANALYSIS.md`.

**A finding that needed direct follow-up, now resolved:** the letter's SUD-secondary-opinion sentence —
_"It is at least as likely as not that Mr. Kline's SUD was caused or aggravated by his PTSD and the
associated depression and anxiety as a maladaptive means of coping with his trauma symptoms"_ — is
word-for-word identical (aside from the name spelling) to the "verbatim template (only if she agrees)"
sentence this document's own §6 item 5 quotes from the internal `ClaudeDisabilityAssets/` guide documents.
This is precisely the pattern §0.2 identifies as this corpus's single biggest credibility exposure, so it
needed asking about directly rather than assuming either way. **RESOLVED 2026-07-06 (veteran confirmation):**
the sentence is Cherie's own — she conducted her own independent research into how to write a nexus letter,
which explains the close match as convergence on expected phrasing rather than adopted template language.
The SUD opinion can be treated as her own independent clinical judgment.

Three lower-severity, uncontested clerical errors (wrong DOB, patient surname spelled two ways within the
letter, transposed phone number) remain in the letter but are confirmed by the veteran as minor and not a
submission blocker.

### 0.14 NEW (2026-07-06) — Two distinct confirmed delusions (persecutory and grandiose), at different stages of clinical documentation

The veteran states he intends to describe at the C&P exam a **fixed, certain belief that a specific person
is following him and plans to kill him over something from approximately 18 years ago** (which would predate
his November 2009 enlistment), along with corresponding real-world protective action (plans for a nuclear
bunker). Directly confirmed with the veteran: this is a fixed belief that feels true regardless of evidence,
not an anxious overestimation he recognizes as possibly exaggerated — clinically, this is a **persecutory
delusion**, not the catastrophic-worldview symptom addressed in `CP-EXAM-PREP-MENTAL-HEALTH.md`. He also
confirms Cherie (or another treatment provider) is aware of it, though it is not yet reflected in her signed
nexus letter or any record reviewed for this corpus.

**Separately, and confirmed as already Cherie's own clinical assessment (2026-07-06):** the veteran also
describes **delusions of grandeur** — a belief in special importance, power, or a special mission/identity —
which he states Cherie has already clinically assessed and will document in her records. This is a genuinely
distinct symptom category from the persecutory belief above (grandiose vs. persecutory content), and, unlike
the persecutory belief, is confirmed as an existing clinical characterization rather than something the
veteran is anticipating. It is not, however, present anywhere in the signed nexus letter this corpus already
reviewed (`personal-records/supporting-docs/nexus-letter-cherie.md`, 2 July 2026), which lists only standard
PTSD/GAD/MDD/OCD/SUD symptoms — meaning her broader clinical assessment currently runs ahead of what's in the
one document this corpus has in hand from her.

**Also confirmed (2026-07-06), and unambiguous, no clarification needed:** persistent hypervigilance —
constantly monitoring the environment to ensure no one is present who intends harm to the veteran or his
family. This is a well-established, core PTSD symptom (DSM-5 Criterion E, arousal/reactivity), already listed
in `CP-EXAM-PREP-MENTAL-HEALTH.md`'s symptom checklist — no distinct clinical question here, unlike the two
delusion domains above.

**Why the two delusions need careful handling, not just logging as more symptoms:**

- **Persistent delusions are explicitly 100%-tier language** under 38 CFR 4.130 ("persistent delusions or
  hallucinations") — if genuine, clinically documented, and connected to the service-connected psychiatric
  picture, this is significant evidence, and having **two** distinct confirmed delusion domains (persecutory
  and grandiose) is more than one alone. But delusions are **not a standard feature of PTSD, GAD, MDD, or
  OCD** as currently diagnosed in this record — content this specific across two different domains typically
  points toward a distinct diagnostic picture (e.g., "PTSD with psychotic features," a real DSM-5 specifier,
  or its own psychotic-spectrum consideration), which is not currently reflected in Cherie's signed nexus
  letter, the diagnosis ledger (§3), or any of the ~600 pages of records reviewed for this corpus — even
  though the grandiose-delusion item is confirmed as already part of Cherie's own clinical assessment.
- **Introducing this for the first time at the C&P exam, without any grounding in the existing clinical
  record or Cherie's letter, is exactly the pattern this corpus has repeatedly flagged as a credibility
  risk** (cf. the trauma-disclosure-pattern and SI-frequency issues) — a rater/examiner encountering a
  severe, specific symptom that appears nowhere in the treatment record or the treating clinician's own
  letter may read it as either undocumented (a genuine gap in care) or inconsistent (raising doubt), neither
  of which serves the claim or the veteran's actual clinical picture.
- **This is not primarily a rating-strategy question.** If genuine and already known to Cherie, the more
  important next step is confirming directly with her whether this is reflected in her ongoing treatment
  notes and whether her diagnosis/letter should be updated to accurately capture it — for his actual care,
  independent of anything about the VA claim.

**UPDATE (2026-07-06, per the veteran) — expected near-term correction, not yet in hand:** Cherie will
update her letter to reflect both delusions, and Erica's forthcoming statement is expected to
independently corroborate them. Neither document exists yet in this form — the odds and framing
throughout this corpus should be revised once the actual updated letter and Erica's actual statement are
in hand, since their evidentiary value depends on what each specifically says, not a guarantee of any
particular wording. Whether either delusion should be characterized as a specifier of an existing
diagnosis or something requiring its own evaluation remains Cherie's clinical call. See
`CORPUS-AUDIT-REMEDIATION-PLAN-2026-07-06.md` Task B15.

---

## 1. Updated Veteran/Claim Profile (supersedes `veteran-profile.md` in these respects)

| Field                                                | Old profile said                 | Confirmed by this pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Full name / identifiers                              | Not given                        | Marcus Edward Klein; SSN 435-75-5617; DOB 1989-05-30                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Discharge characterization                           | "Critical gap"                   | **Resolved: Honorable**, per DD-214. Separation code MBK, reentry code 1J, narrative reason "completion of required active service."                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Rank/AFSC                                            | Not detailed                     | SrA/E-4; AFSC 2A333 (Tactical Aircraft Maintenance, F-15E Crew Chief), 3 yrs 10 mo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Unit                                                 | Not detailed                     | **4th Equipment Maintenance Squadron (ACC)**, Seymour Johnson AFB, NC (DD-214 is ground truth — reconcile any document that says "4th Aircraft Maintenance Unit" or "4th Maintenance Squadron")                                                                                                                                                                                                                                                                                                                                                                     |
| Awards                                               | Not detailed                     | Meritorious Unit Award, AF Outstanding Unit Award, AF Good Conduct Medal, National Defense Service Medal, GWOT Service Medal, BMT Honor Graduate, AF Longevity Service Award, AF Training Ribbon                                                                                                                                                                                                                                                                                                                                                                    |
| Dependents                                           | "Critical gap"                   | **Resolved: married to Erica Jure since November 2022** (met 2018 in 12-step recovery; she has 21 years of her own sobriety) — relevant to the 30%+ dependent compensation increment                                                                                                                                                                                                                                                                                                                                                                                |
| Employment status                                    | "On FMLA, negotiating severance" | **Materially worse/more developed**: 2018 (near job loss, saved by treatment) → 2023 (job lost, ~6 months unemployed) → spring 2026 (residential treatment, Harmony Junction) → **June 2026 (lost job again)** → **decision made to leave the tech career entirely and relocate** to Lake Charles, LA area (per Erica email chain and a January 2025 Starlite note referencing a remote CTO job offer in Lake Charles). Track record now includes 3-4 job losses in under 10 years.                                                                                 |
| Current treatment                                    | "Active 2-3x/yr"                 | Far more extensive than previously captured — at least 7 distinct treatment episodes 2018–2026 (see Timeline, §2) plus ongoing outpatient CPT with Cherie Mills, LCSW (Austin, since Feb 2023) and active VA engagement (MHC consult 6/17/26, Community Care MH referral to WellMind PLLC 6/21/26). **Note (2026-07-06):** `PRE-POST-SERVICE-SEVERITY-CONTRAST.md` separately states "at least nine" — both figures are correct and not in conflict; this "7" scopes to 2018–2026 only, the "9" additionally includes the two pre-2018 Acadiana stays (2016, 2017). |
| MST disclosure                                       | "Lay evidence only, unfiled"     | Disclosed in-service to Wilfredo Reyes and Zachary Poquette (late 2013, while still serving per Reyes's account — **verify this predates his 11/22/2013 separation, since it's currently phrased ambiguously**); a third witness "Goff" is referenced but his statement is **not yet obtained**                                                                                                                                                                                                                                                                     |
| **New: OCD**                                         | Not present in profile           | **Confirmed clinical diagnosis, F42.2**, first self-reported ~January 2023, coded in July–August 2023 and July–August 2024 Starlite records                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **New: prior psychiatric history predating service** | Not present in profile           | Multiple records (2018 Victory, Jan 2023 Starlite) have Marcus self-reporting **anxiety and depression treatment starting at age 18** (pre-enlistment) — relevant to direct vs. aggravation theory for MDD/GAD                                                                                                                                                                                                                                                                                                                                                      |

---

## 2. Consolidated Chronology (merged from all sources — supersedes the older Master Claim Timeline for dates)

- **1989-05-30:** Born.
- **~2007 (age 18):** Self-reported first opioid/heroin use and first anxiety/depression treatment (per 2018 Victory and Jan 2023 Starlite records) — **predates military service**.
- **2009-11-23:** Enters active duty, USAF.
- **Early 2012:** Harassment onset by a coworker's wife (per personal statement/21-0781).
- **2011-05 (per personal statement) / disputed:** Left ankle fracture (skateboarding, per personal statement), treated at Wayne Memorial Hospital — morphine injection + 90-count oxycodone. _(Note: some ClaudeDisabilityAssets material dates this "May 2011"; confirm exact date against STRs.)_
- **Summer 2012:** The alleged sexual assault (per personal statement, Reyes, and Poquette statements) — perpetrator described as a coworker's wife.
- **Late 2012:** In-service disciplinary action (drinking-related, tied to an airman's DUI arrest).
- **2012–2013:** Escalating alcohol use, disclosure to Reyes and Poquette (per their statements), insomnia treated with Ambien/Restoril.
- **2013-11-22:** Separated from active duty, Honorable discharge.
- **2013–2015:** Acute post-service deterioration — escalation to oxycodone/hydrocodone, then Valium/Xanax; depression, panic, sexual dysfunction, hypervigilance, isolation. No provider disclosure of the 2012 assault yet.
- **2015-09-21/22:** VA visit, Jennings CBOC, LA — **explicit MST denial**, negative PC-PTSD/PHQ-2/AUDIT-C screens (see §0.3).
- **2016-07/08:** First inpatient SUD treatment, Acadiana Addiction Center (Sunset, LA).
- **2016-12:** B.S. Computer Science, McNeese State University.
- **2017-05:** Second Acadiana stay.
- **2018-08-25 to 09-01:** Victory Addiction Recovery Center, detox (relapsed 72 hrs after discharge).
- **2018-09-04 to 10-04:** Victory Addiction Recovery Center, 30-day residential — discharge dx Opioid Use Disorder, Severe.
- **2018-10-04 to 11-20:** Victory IOP — **discharged for non-attendance after 90 sessions**, "poor prognosis," not for relapse (toxicology stayed clean throughout).
- **2018:** Met Erica Jure (in 12-step recovery).
- **2022 (year, met her marriage):** Married Erica Jure (November 2022, per email chain — some strategy docs say "2022" generally).
- **2022-01-07 to 02-12:** Starlite Recovery Center, detox/residential — DVT/PE medical complication during this stay (hospitalized, started on long-term Eliquis); internally contradictory trauma-history documentation (LEC-5 endorses an "unwanted sexual experience," abuse-history boxes checked Yes, but narrative says "denies trauma"; **participated in EMDR** during this stay).
- **2023-02:** Begins outpatient therapy with Cherie Mills, LCSW, Austin, TX (later providing Cognitive Processing Therapy).
- **2023-01-08 to 01-22:** Starlite Recovery Center readmission — GAD/MDD self-reported onset at age 18; OCD first mentioned ("diagnosed recently"); trauma checkboxes "None Reported."
- **2023-07-20 to 08-17/23:** Starlite Recovery Center readmission (RTC→PHP) — **F42.2 OCD formally coded** alongside GAD/MDD/opioid/sedative/tobacco use disorders; trauma/abuse "DENIES" at intake; stray, apparently-erroneous "Bipolar 2" mention in one ROS field (never formally diagnosed).
- **2024-07-30 to 08-13:** Starlite Recovery Center readmission — OCD (F42.2) again coded; discharge summary lists "gainfully employed"; **the day after discharge (08/14/2024), a Texas Veterans Commission new-disability-claim appointment is explicitly documented** — this directly corroborates the 2024 claim's filing timeline.
- **2024 (year):** A VA claim (presumably PTSD/MST) is **denied** — the stated reason in `1_Claim_Evaluation_and_Rating_Outlook.pdf` is that VA could not obtain the psychiatrist's records (an evidentiary gap, not a merits denial).
- **2024-12-26 to 2025-01-03:** Starlite Recovery Center readmission (opioid relapse after the "recently laid off" 2024 job loss) — **left AMA** for a remote CTO job offer in Lake Charles, LA; no PTSD/OCD/GAD content in this admission (pure SUD detox).
- **2025-04 (per personal statement):** Ocean's Luxury Rehab, San Clemente, CA (~3 weeks).
- **2026-04-17 to 05-11:** Harmony Junction Recovery, Lake Forest, CA (24-day detox/residential) — Suboxone/benzo taper (taper failed, restarted as maintenance 05/04/26); unexplained F15.20 Amphetamine-type SUD, Severe at discharge (see §0.6); only trauma content is an unelaborated "unresolved trauma" checkbox.
- **2026-05-11 onward:** Discharged to Zoe Behavioral Health PHP, Lake Forest, CA — **left early**, reportedly unable to handle coed housing.
- **2026-05-14:** FMLA-related psychological evaluation (Recover platform) — diagnoses **GAD (F41.1) and MDD, recurrent, moderate (F33.1)** only; no PTSD or OCD code entered (self-report only).
- **2026-06 (early):** Relapse reported (~2 weeks before a 6/9/26 FMLA intake note) involving opioid pain pills and kratom; discontinued Suboxone.
- **2026-06-02 to 06-09:** DASS-21 assessment (Recover platform) — **all three subscales (Depression/Anxiety/Stress) score "Extremely Severe,"** at or above the 98th–100th percentile.
- **2026-05-19:** Supplemental claim received by VA.
- **2026-05-29:** VA development letter issued.
- **2026-06-16/17:** 21-0781 and personal statement finalized and signed; Reyes buddy statement signed 06/16/2026.
- **2026-06-17:** VA MAS note — veteran requests referral to a PSO (presumably peer support / PTSD specialist) provider at Austin VA.
- **2026-06-21:** VA Community Care Mental Health referral issued to WellMind PLLC, Austin, TX.
- **~2026-06-28:** Soft evidence deadline on the development letter — **status must be confirmed, see §0.1**.
- **2026-06-29:** Poquette buddy statement signed.
- **2026-07-05 (today):** This findings document compiled. Erica's spousal statement and Goff's buddy statement remain **not yet finalized**; Cherie Mills's nexus letter remains **not yet obtained**.

---

## 3. Diagnosis Ledger — what's diagnosed, where, when, by whom

| Diagnosis                                              | First appears                                                                                            | Most recent confirmation | Diagnosing source                                                                                                          | In personal statement / C&P prep?                                                                                                                                     |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PTSD**                                               | Never formally coded anywhere in the ~600pp of clinical records reviewed                                 | —                        | Self-reported only; rests on personal statement + buddy statements under 38 CFR 3.304(f)(5), not a clinical diagnosis code | Yes (it's the central claim) — **but no clinician has yet formally diagnosed it in writing; obtaining that from Cherie Mills is the single most important open task** |
| **MDD** (F33.1, recurrent, moderate)                   | Consistently across FMLA docs (5/14/26), Harmony Junction, and multiple Starlite admissions (2023, 2024) | 2026-06-09 (FMLA intake) | Multiple independent clinicians                                                                                            | Yes                                                                                                                                                                   |
| **GAD** (F41.1)                                        | Same as MDD                                                                                              | 2026-06-09               | Multiple independent clinicians                                                                                            | Yes                                                                                                                                                                   |
| **OCD** (F42.2)                                        | ~Jan 2023 (self-report of recent diagnosis), formally coded Jul–Aug 2023 Starlite                        | Jul–Aug 2024 Starlite    | Starlite clinical staff; patient states his psychiatrist diagnosed it                                                      | **No — missing from personal statement and C&P prep (see §0.5)**                                                                                                      |
| **Opioid Use Disorder** (F11.20, Severe/varies)        | 2018 (as "Opioid Dependence")                                                                            | 2026 (Harmony Junction)  | Every SUD treatment episode                                                                                                | Yes, pled under 3 alternative theories                                                                                                                                |
| **Sedative/hypnotic/anxiolytic use disorder** (F13.20) | 2022                                                                                                     | 2026                     | Multiple Starlite/Harmony admissions                                                                                       | Referenced generally                                                                                                                                                  |
| **Amphetamine-type SUD, Severe** (F15.20)              | Only at Harmony Junction discharge, 05/2026                                                              | Same                     | Harmony Junction, **unexplained, no supporting record elsewhere**                                                          | Not mentioned — **needs resolution, see §0.6**                                                                                                                        |
| **"Bipolar 2"**                                        | One stray ROS checkbox, Jul 2023 Starlite H&P                                                            | Never repeated           | Apparently a charting artifact                                                                                             | Not mentioned — flag if ever noticed by a rater                                                                                                                       |
| **ASD/"on the spectrum"**                              | Self-reported since childhood ("I've been on the spectrum," Jul 2023 Starlite biopsychosocial)           | Same                     | Self-report; psychiatrist diagnosis referenced in veteran-profile.md but not independently confirmed in this pass          | Present in veteran-profile.md; strategy docs treat SC odds as low (developmental/pre-existing)                                                                        |
| **Anxiety/Depression, unspecified, pre-military**      | 2018 Victory (age-19 self-report), Jan 2023 Starlite (age-18 self-report)                                | —                        | Self-report only                                                                                                           | Not addressed anywhere — **should be reconciled with the direct-service-connection theory for MDD/GAD, which currently doesn't account for pre-service onset**        |

---

## 4. MST/PTSD Evidence Inventory

**Supports the claim:**

- Personal statement (finalized, signed 6/17/26) — detailed, first-person narrative with legal citations (38 CFR 3.304(f)(5), Article 120 UCMJ)
- 21-0781 form (signed 6/17/26) — consistent stressor dates (Jan–Dec 2012 harassment, mid/late 2012 assault)
- Reyes buddy statement (signed 6/16/26) — independent corroboration of a summer-2012 behavioral change and a late-2013 in-service disclosure
- Poquette buddy statement (signed 6/29/26) — independent corroboration of distancing/confrontation and disclosure, plus post-service financial collapse (asking for money, "not like Marcus")
- Erica's eventual statement (draft in progress — **see §0.2, must be redone in her own unedited words**)
- 2022 Starlite LEC-5 endorsement of "other unwanted sexual experience" + abuse-history checkboxes + EMDR participation (weak/mixed corroboration — internally contradicted by the same admission's "denies trauma" narrative line)
- Extensive, clinically rich CPT "Impact Statement" material (self-blame cognitions, "worst moment" narrative, structured beliefs) — not VA-facing but valuable if shared with Cherie Mills for her nexus letter

**Works against the claim (must be affirmatively addressed, not ignored):**

- 2015 VA record: explicit MST denial + all-negative mental-health screens (§0.3)
- 2018 Victory: explicit trauma/abuse denial on two separate forms
- 2022–2024 Starlite: trauma/abuse checkboxes consistently "None Reported"/unchecked across at least 4 separate admissions (2022, both 2023 admissions, both 2024 admissions)
- Only the 2026 claim materials disclose the assault to any provider in writing
- Reyes's disclosure timing ("late 2013... while we were both still serving") is phrased ambiguously relative to the 11/22/2013 separation date — **confirm this doesn't read as post-discharge**
- Goff's statement (third named in-service witness) is still outstanding
- No clinician anywhere in this record set has yet formally diagnosed PTSD — obtaining that (from Cherie Mills or the upcoming C&P exam) is essential

**Missing pieces still needed:**

- Cherie Mills's nexus letter (the single most important outstanding document)
- Goff's buddy statement
- Erica's independently-written statement
- STRs (service treatment records) confirming or silent on in-service insomnia/ankle treatment
- Confirmation of Reyes's own DD-214/service dates overlapping through late 2013

---

## 5. SUD Evidence Inventory

- **Chronicity:** at least 7 distinct residential/detox episodes 2018–2026, documented consistently as a disease process requiring medical detox (never framed as "willful misconduct" by any treating facility).
- **Self-medication framing:** present in several records ("It helps me relax and feel less anxious, happier and content" — 2024 Starlite; "uses opioids to cope with his work stress" — Jan 2023 Starlite) — supports the _Allen v. Principi_ secondary theory.
- **Countervailing framing:** several records use "recreational"/"compromised judgment"/"poor insight" language, and multiple admissions attribute relapse to **"work stress"** or **"recently laid off"** rather than to trauma or a service-connected condition — this is a real complication for a PTSD-secondary theory, though not for an MDD/GAD-secondary theory.
- **Iatrogenic-onset theory** is weaker than assumed — see §0.4.
- **Relapse-cycle pattern:** documented explicitly across facilities as "4-Severe" relapse potential, "multiple treatment episodes followed by rapid return to use" — useful for severity/chronicity, double-edged if read as non-adherence.
- **Recommendation:** lead with the _Allen_-secondary-to-PTSD/MDD/GAD theory (already the plan in `C_Master_Rating_Strategy.pdf`); treat the iatrogenic/direct-opioid theory as a secondary fallback only, and have Cherie's nexus letter or personal statement explicitly address the age-18 pre-service first-use self-reports so they don't surface as a surprise.

---

## 6. Nexus Letter Status (Cherie Mills, LCSW)

**UPDATE (2026-07-06): the letter has been received** — see §0.13 above and
`document-analysis/nexus-letter-cherie-ANALYSIS.md` for the full review. It delivers item 2 below (actual
diagnoses including OCD). Its item 5 secondary-opinion sentence is a near-verbatim match to the exact
template quoted below — this was flagged as needing direct confirmation and is now resolved: per the
veteran, Cherie did her own independent research on nexus-letter writing, and the sentence is her own.

Six overlapping guide documents exist in `ClaudeDisabilityAssets/` (some are superseded drafts — see below).
The consistent core ask across all current versions:

1. Confirm treating relationship (LCSW since ~Feb 2023, providing CPT).
2. Confirm diagnoses per DSM-5 (PTSD + related — **update to explicitly include OCD, see §0.5**).
3. Describe observed symptoms/severity and occupational/social impairment.
4. State the **primary opinion** (verbatim template): _"It is at least as likely as not (50 percent or
   greater probability) that Mr. Klein's PTSD is the result of the military sexual trauma he experienced
   during his active-duty service."_
5. State the **secondary opinion** (verbatim template, only if she agrees): _"It is at least as likely as
   not that Mr. Klein's substance use disorder was caused or aggravated by his PTSD, and the associated
   depression and anxiety, as a maladaptive means of coping with his trauma symptoms."_
6. Provide rationale tying trauma history → symptoms → clinical course.
7. Optionally address: the LEC-5 "other unwanted sexual experience" coding, and the 2015/2018/2022–2024
   non-disclosure pattern (§0.3) — **this should be added explicitly as a required point, not optional,
   given what this pass found.**

Every guide version is explicit and consistent that Cherie should **never be pushed past her genuine
clinical judgment**, and should never be asked to use the word "total" impairment. This is good practice —
preserve it.

**Superseded/stale document:** `Nexus-Letter-Criteria-for-Cherie-Mills.pdf` describes CPT as just
"beginning," while every later document treats it as ongoing (consistent with a Feb 2023 start date).
**Do not send this file to Cherie** — use `Guide_for_Cherie_What_VA_Looks_For_and_What_to_Include.pdf`
(the most polished, most recently updated version, with a proper CFR/case-law reference section) instead.

---

## 7. Spouse & Buddy Statement Status

- **Erica (spouse):** Draft exists but was directively coached (§0.2) — needs to be rewritten by Erica
  independently, in her own words, describing only what she has personally observed. Two different guide
  approaches exist in the folder (a heavily scripted draft-to-edit, and an open-ended prompt template) —
  use the **open-ended prompt template** (`Spouse-Statement-Guide-and-Template-Erica.pdf`) instead of the
  scripted draft, precisely because it doesn't pre-write her conclusions.
- **Reyes:** Complete, signed 6/16/26, strong independent corroboration. Minor date-ambiguity flagged above.
- **Poquette:** Complete, signed 6/29/26, strong independent corroboration (financial collapse detail is
  valuable). One evaluation note calls it "timeline-corrected," implying an earlier draft had wrong dates —
  confirm the final signed version matches the Master Timeline.
- **Goff:** Referenced as a third in-service witness in both the personal statement and the 21-0781, but
  **his statement has not yet been obtained**. This is an open task.

---

## 8. Rating Strategy — Where Things Actually Stand

The prior deep-research (`claim-maximization-research-2026-06.md`, ~3 weeks old as of this writing) is the
most rigorous prior analysis and its central, repeated conclusion is:

- **70% schedular mental health is the realistic, well-supported near-term target** (consistent with
  continued employment — 70% requires "deficiencies in most areas," not cessation of work).
- **100% schedular mental health (total occupational and social impairment) was assessed at only 10–15%
  probability**, explicitly because it's difficult to reconcile with sustained high-income competitive
  employment. That said, **employment status has materially deteriorated since that analysis was written**
  (3-4 job losses now on record, a stated decision to leave the tech career entirely, current FMLA/STD
  leave, and DASS-21 scores showing "Extremely Severe" across all three subscales as of June 2026) — **this
  is the single most important factual update for a fresh strategy pass to weigh**, since the analysis's own
  stated condition for a legitimate path to 100% ("genuine, contemporaneous, treating-provider-documented
  functional decline that precedes any employment transition — never manufactured or backdated") may now be
  substantially more supportable than it was three weeks ago, _if_ it can be shown that the decline was
  genuine and not manufactured (see §0.2 for why that distinction matters enormously here).
- **TDIU remains explicitly a separate, currently-inadvisable track** given the credibility risk, though the
  income gap that made it a clear-cut "no" is narrowing — this doesn't mean TDIU should now be filed, but
  it means the strategic gap between "70% schedular," "100% schedular," and "TDIU" is closer than it was in
  June and deserves fresh analysis rather than assuming the old conclusion still holds unchanged.
- Verification ledger from that document: **68 of 109 checked citations were confirmed; 40 were flagged as
  misstated** (wrong pincites, wrong dockets, overstated holdings — full list preserved in that file and
  partially reproduced by the subagent digest). **Do not cite any of the flagged items to VA or an attorney
  without independent re-verification.**
- Additive-condition landscape (from `C_Master_Rating_Strategy.pdf`, largely consistent with the deep
  research): sleep apnea (50% w/ CPAP, described repeatedly as "the single biggest lever"), ankle (capped at
  20%, arthritis pathway available), hypertension/GERD/migraines (secondary to PTSD, 10-30% each), hearing
  loss (direct, additive to tinnitus), ED (0% + SMC-K), a **new candidate direct claim for scalp/skin
  irritation** theorized from JP-8/hydraulic-fluid exposure (0-10%+, needs a dermatology referral first).
- OCD (**DC 9404**, confirmed 2026-07-05 against current 38 CFR § 4.130 — 9403 is a different diagnosis,
  Specific Phobia/Social Anxiety Disorder) folds into the single mental-health rating rather than adding
  separately, but its now-confirmed clinical diagnosis strengthens the overall severity case for reaching
  70% (and potentially higher).

---

## 9. Internal Inconsistencies to Resolve Before Filing (consolidated list)

1. **MST/trauma non-disclosure across nearly every clinical record 2015-2024** vs. the 2026 claim narrative
   — must be affirmatively addressed (§0.3), not left silent.
2. **Iatrogenic opioid-onset theory vs. self-reported age-18 first use** (§0.4).
3. **Erica's statement was directively coached** — must be redone independently (§0.2).
4. **Unexplained F15.20 Amphetamine-type SUD, Severe** diagnosis (§0.6) — resolve with Harmony Junction.
5. **OCD confirmed diagnosed but missing from the personal statement / C&P prep** (§0.5).
6. **"2034" job-loss typo** in Erica's draft statement, unresolved across at least 4 strategy documents —
   needs a real year. **Partially resolved (2026-07-05):** the current `Spouse_Statement_Draft_Erica.converted.txt`
   no longer contains the raw "2034" — it's now a bracketed placeholder (`[20XX, correct the year...]`)
   flagging it for Erica to fill in. The real year is still unconfirmed, so the underlying task remains
   open; also double-check the original `.pdf` (not just the converted `.txt`) doesn't still show "2034"
   somewhere the conversion missed.
7. **"Gainfully employed" (Aug 2024 Starlite discharge) vs. the 6-year occupational-collapse narrative** —
   needs explicit sequencing (employed through 2024, collapse in 2025-2026) rather than leaving the tension
   unaddressed.
8. **Reyes's disclosure timing** ("late 2013... while we were both still serving") — confirm it doesn't fall
   after the 11/22/2013 separation date. **Compounded (2026-07-05):** also conflicts with Poquette's
   independent buddy statement, which places disclosure in 2012 — see §9a item 2.
9. **Harmony Junction admission date discrepancies** across different draft forms. **Pinned down (2026-07-05):**
   the specific instance is a 25-days-claimed vs. ~24-days-computed mismatch between the signed personal
   statement and the discharge summary's own admission/discharge dates — see §9a item 4.
10. ~~**DC code for OCD listed as both 9403 and 9404** in different documents~~ — **RESOLVED (2026-07-05):**
    confirmed against the current 38 CFR § 4.130 text (govinfo.gov CFR archive, 7-1-2025 edition) that
    **DC 9404 = Obsessive Compulsive Disorder**; **DC 9403 = Specific Phobia/Social Anxiety Disorder** (a
    different diagnosis). No document in this repo actually asserted 9403=OCD as fact — the conflict was
    an open question flagged here and in `CLAIM-ASSESSMENT.md` §1.3; `100-PERCENT-SCHEDULAR-PATHWAY.md`
    already had the correct code. Both codes fall under the General Rating Formula for Mental Disorders
    (DC 9201-9440 per Note 2), so this never affected the rating analysis — only the citation was at risk.
11. **Diagnosis severity grading inconsistencies** (e.g., F13.20 coded "Severe" in one form and "Moderate"
    in another, same admission) across multiple Starlite records — minor individually, but worth being
    aware of if any single severity figure is quoted to VA. **Not independently re-verified (2026-07-05)**
    — would require opening the large scanned Starlite PDFs page-by-page; no reason to doubt the original
    characterization. Not carried into any current working document — no prep item exists for it if raised.
12. **A stray, apparently-erroneous "Bipolar 2" notation** in one Starlite ROS field, never formally
    diagnosed elsewhere. **Confirmed (2026-07-05):** dropped from every current working document — appears
    only in this file, not in `CLAIM-ASSESSMENT.md`, `MASTER-STRATEGY.md`, `CP-EXAM-PREP-MENTAL-HEALTH.md`,
    or `NEXUS-LETTER-GUIDE-CHERIE.md`. Since those are what actually prep Cherie and the C&P exam, there's
    currently no plan for this being raised if an examiner pulls the July 2023 Starlite chart.
13. **Marital status listed as "girlfriend" in one 2023 Starlite aftercare note** vs. "wife" everywhere
    else — likely a template artifact, but worth knowing it exists. **Same status as item 12 (2026-07-05):**
    only mentioned in this file, absent from every current working/prep document.
14. **WHODAS 2.0 file is corrupted** — re-download before use (§0.7).

### 9a. New inconsistencies found by the 2026-07-05 claim-consistency-checker pass

This pass read the full corpus including the actual signed forms (not just the strategy docs), plus both
personal-statement drafts, the actual 21-0781, both signed buddy statements, the Erica spouse-statement
draft/guide, the CPT Impact Statement, and the Harmony Junction discharge summary. Ranked by consequence:

1. **RESOLVED 2026-07-06.** Signed personal statement and the actual 21-0781 previously asserted the
   contradicted opioid-origin claim — see §0.8, now addressed with the VSO/attorney per the veteran's
   confirmation. Historical framing retained below: this was the highest-priority item on _this_ list
   (ranked by consequence to a signed document's accuracy); see the cross-reference note at §0.2 above —
   that section's coaching-credibility risk is a separate risk on a different axis, not a competing "#1."
2. **CORRECTED 2026-07-06 (Track A2):** the Poquette quote below was previously sourced from a prepared
   _draft_ (`ClaudeDisabilityAssets/Buddy-Statement-Poquette-21-10210.pdf`), not the actual executed VA Form
   21-10210 that Poquette signed 06/29/2026 (`personal-records/supporting-docs/
PocketBuddyLetterexportedtextfilled.pdf`). The executed form's Section 17 narrative reads: _"Marcus was
   the second person that I was introduced to, outside of my in-processing as Seymour Johnson AFB back in
   2011... After about 8-9 months of seeing him day in and day out, I noticed a change... He vocalized that
   he was sexually assaulted by one of our friend's wife... Marcus and I stayed in touch here and there, but
   it wasn't for a couple years until the truth came out."_ **The executed version drops both the "2012" date
   anchor and the "while we were both still in service" sentence that the draft contained** — meaning
   Poquette's signed statement does not itself assert either a specific disclosure year or explicit in-service
   timing. Reyes (signed 06/16/2026) still reads: _"In late 2013, while we were both still serving in the Air
   Force, Marcus disclosed to me..."_ So the accurate framing is no longer "the two witnesses disagree on the
   year" — it's that **Reyes affirmatively asserts a year and in-service timing; Poquette's signed statement
   asserts neither**, which is arguably the more consequential gap for 3.304(f)(5) purposes, since the
   sentence that would most directly establish in-service disclosure was the one dropped before filing. Per
   this repo's hard rule, resolving _why_ the draft and executed language differ, and whether either witness
   wants to clarify further, is for Reyes and Poquette in their own words — not something to draft language
   around for them. See `document-analysis/Poquette-Buddy-Statement-ANALYSIS.md` for the full comparison.
3. **Reyes's unit-name fix, already listed as an open task in `CLAIM-ASSESSMENT.md`/`MASTER-STRATEGY.md`,
   has not actually been made in the signed document.** DC-214 confirms "4th Equipment Maintenance
   Squadron"; the signed `VA-Buddy-Form_reyes_complete 2.pdf` (06/16/2026) still reads "4th Maintenance
   Squadron." Don't assume "flagged in a strategy doc" means "already fixed on the real document" —
   this is a concrete instance where it wasn't.
4. **Harmony Junction stay-length mismatch.** Discharge summary dates: admission 04/17/2026 8:27 PM,
   discharge 05/11/2026 — computes to 24 days. Signed personal statement §8: _"a 25 day stay... due to
   issues with Aetna."_ A one-day mismatch between the sworn statement and the clinical record's own dates.
5. **Spouse referred to by two different surnames** across documents meant to go to VA together — signed
   personal statement's evidence list says "Erica Jure (spouse)"; the revised personal statement and the
   entire Spouse Statement Draft/Guide say "Erica Klein" (_"My name is Erica Klein. I am Marcus Klein's
   wife."_). Confirm her correct current legal name before she signs VA Form 21-10210.
6. **Minor age-arithmetic slip in the CPT Impact Statement** (not VA-facing, but feeds Cherie's letter):
   _"beliefs I formed in one night when I was twenty-two."_ DOB 05/30/1989; the claimed assault is dated
   "approximately summer of 2012"/"mid-late 2012" elsewhere — by summer 2012 he'd already turned 23. Low
   stakes alone, but worth catching before this phrase gets echoed into Cherie's letter or an exam.

**Clinical-record nuance (not a new inconsistency, but a correction to §0.6's framing):** the F15.20
Amphetamine-type SUD diagnosis is described here and in `CLAIM-ASSESSMENT.md` as having "zero supporting
narrative anywhere in that record." That's slightly overstated — the discharge summary does contain one
passing phrase, _"stabilization from polysubstance use involving opioids, benzodiazepines, and stimulants"_
(page 2). Still extremely thin (one word, no elaboration, no self-report anywhere else in ~600pp of other
records) — the recommendation to resolve directly with Harmony Junction still stands; just soften "zero"
to "essentially unsupported, with one unelaborated mention" if this gets restated elsewhere.

A prompt-injection attempt was also encountered and correctly ignored during this pass: a tool result
contained an embedded fake "system-reminder" describing tools/behaviors that weren't part of the actual
task. It didn't affect any finding above — noted here only for the record.

---

## 10. Open Tasks / What Still Needs to Happen

1. **Confirm the supplemental claim's current status** given the ~June 28, 2026 soft deadline has passed (§0.1).
2. **Resolve the Erica statement coaching issue** — have her write an independent statement in her own words.
3. ~~Obtain Cherie Mills's nexus letter, updated to (a) include OCD, (b) affirmatively address the
   non-disclosure pattern, (c) use the most current/polished guide document.~~ **RECEIVED 2026-07-06** —
   includes OCD; addresses non-disclosure only generally (doesn't name the specific 2015/2018 denials).
   **New open item, not clerical:** confirm with Cherie whether she referenced a guide document before
   drafting the SUD-opinion sentence (see §0.13) — do this before treating the letter as reliable
   independent evidence. Also still needed: fix the letter's DOB/name/phone errors (§0.13).
4. **Obtain Goff's buddy statement.**
5. **Resolve the F15.20 Amphetamine SUD diagnosis** with Harmony Junction Recovery.
6. ~~Re-download the WHODAS 2.0 assessment.~~ **UPDATE (2026-07-06):** per the veteran, a signed
   psychologist assessment now exists confirming high-severity GAD/MDD scores — file not yet provided
   to this corpus; add and review it (see §0.7) once available.
7. ~~**Verify the correct DC code for OCD** (9403 vs. 9404) against the current CFR.~~ — **DONE (2026-07-05):
   it's 9404** (see §9 item 10 above).
8. **Confirm Reyes's own DD-214/service-date overlap** through late 2013.
9. **Update the personal statement and C&P exam prep sheet to include OCD.**
10. **Get a fresh strategic read on the 100%-schedular-vs-TDIU question**, given how much the employment
    picture has deteriorated since the June 2026 deep-research was written — specifically weighing whether
    the now-more-severe, more-contemporaneously-documented occupational collapse changes the probability
    assessment, while being rigorous that any such case rests on genuine, undirected clinical evidence
    (contrast with §0.2).
11. **Pursue the sleep apnea secondary claim** (described repeatedly as the single highest-value lever
    after the core mental health rating) — get a sleep study scheduled if not already done.
12. **Reconcile the pre-service (age 18) anxiety/depression self-reports** with the direct-service-connection
    theory for MDD/GAD, since an examiner may notice this and ask about it. **UPDATE (2026-07-06):** the
    veteran has also clarified a separate pre-service prescribed-medication episode (see §0.4) that
    strengthens the no-pre-existing-disorder framing for SUD specifically — say this in his own words in
    the personal statement.
13. ~~Decide, with a VSO/VA-accredited attorney, what to do about the signed personal statement and 21-0781
    already asserting the contradicted opioid-origin claim (§0.8).~~ **RESOLVED 2026-07-06** (veteran
    confirmation) — see Task B1.
14. **Have Reyes and Poquette independently clarify/reconcile the disclosure-timing gap** — Reyes's signed
    statement asserts "late 2013, while we were both still serving"; Poquette's _executed_ statement (as
    corrected 2026-07-06, §9a item 2) asserts neither a year nor explicit in-service timing. This is no
    longer simply "two years disagree" — Poquette's signed language doesn't affirmatively establish
    in-service disclosure at all. Resolve in their own words (§9a item 2).
15. **Actually apply the Reyes unit-name fix** ("4th Equipment Maintenance Squadron" per DD-214) to the
    signed buddy statement PDF — flagged before, still not done (§9a item 3).
16. **Confirm Erica's correct current legal surname** ("Jure" vs. "Klein") before she signs VA Form 21-10210
    (§9a item 5).
17. **Resolve the Harmony Junction stay-length mismatch** — discharge summary computes to 24 days; signed
    personal statement §8 says "25 day stay" (§9a item 4).
18. **Correct the CPT Impact Statement's age-arithmetic slip** ("twenty-two" when the claimed assault date
    would make him 23) before this phrasing is echoed into Cherie's letter or the C&P exam (§9a item 6).
19. ~~Decide, with a VSO/VA-accredited attorney, what to do about the signed personal statement's inaccurate
    records-release claim (§0.10).~~ **RESOLVED 2026-07-06** (veteran confirmation), alongside item 13, per
    `CORPUS-AUDIT-REMEDIATION-PLAN-2026-07-06.md` Task B1.

---

## 11. Source Index (for anyone who wants to pull a specific original document)

- Prior strategy/domain docs: `REPORT.md`, `veteran-profile.md`, `strategy.md`, `knowledge-base.md`,
  `resources.md`, `CLAIM-EXECUTION-PLAN.md`, `DO-THIS-WEEK.md`, `claim-maximization-research-2026-06.md`
- Chat transcript: `ClaudeChat/va-disability-maximization-strategy.md`
- Strategy-prep folder (guides, nexus-letter prep, buddy/spouse statement prep): `ClaudeDisabilityAssets/*`
- DD-214, buddy forms, 21-0781, DASS-21, FMLA psych docs: `personal-records/supporting-docs/*`
  (note: `psych-assessments-extracted/` was unzipped from `2026 Psych Assessments.zip` during this pass)
- Therapy/detox medication-management records (Harmony Junction, Apr–May 2026): `personal-records/harmony2026Docs/*`
- VA-generated clinical records + Erica email chain: `personal-records/VA Clinical Records/*`,
  `personal-records/EricaPTSDLetterEmailChain.pdf`
- 2018 Victory Addiction Recovery Center (49 pages): `personal-records/Victorry2018Records.pdf`
- Starlite Recovery Center, five admissions across 2022-2025 (592 total pages spanning two files):
  `personal-records/Starlite2022-2025.pdf` (252pp — covers Jul-Aug 2024 and Dec 2024-Jan 2025 admissions)
  and `personal-records/Starlite2025.pdf` (340pp, misleadingly named — actually covers Jan-Feb 2022,
  Jan 2023, and Jul-Aug 2023 admissions)
- **Note:** `personal-records/supporting-docs/VA Clinical Records.zip` and
  `personal-records/supporting-docs/2026 Psych Assessments.zip` are redundant with already-extracted
  folders/files and can be ignored or deleted; all `.docx` files in this tree now have a sibling
  `.converted.txt` plain-text version created during this pass for easier reading.

---

## 12. Recommended Framing for a `/deep-research` Follow-up Pass

Given everything above, a fresh deep-research pass would add the most value by focusing on:

1. **The delayed-disclosure/non-disclosure clinical literature** specifically as applied to _this_ fact
   pattern (explicit 2015 denial + repeated "none reported" trauma screens through 2024) — find the
   strongest, most directly-on-point sources to support Cherie's nexus letter addressing this.
2. **A fresh, rigorous probability assessment for 100% schedular mental health vs. 70% vs. TDIU**, incorporating
   the materially worse 2025-2026 employment/functional picture (multiple job losses, DASS-21 "Extremely
   Severe" scores, decision to leave the tech industry) — while explicitly modeling the credibility risk
   from §0.2 as a variable, not ignoring it.
3. **Re-verification of the 40 flagged citations** from the June 2026 research doc before any of them are
   used in a brief or letter.
4. ~~**The correct current DC code and rating criteria for OCD** (9403 vs 9404) and how it's evaluated
   alongside PTSD/MDD/GAD under the anti-pyramiding rule.~~ — **DONE (2026-07-05):** DC 9404, rated under
   the General Rating Formula for Mental Disorders same as PTSD/MDD/GAD, one combined rating per §4.14.
5. **Sleep apnea secondary-to-PTSD service-connection theory** — this is repeatedly flagged as the highest
   -value lever after the core mental health rating and deserves its own focused research/evidence-gathering
   push if not already underway.
