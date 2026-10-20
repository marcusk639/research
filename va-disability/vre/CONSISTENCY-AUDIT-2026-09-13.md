---
topic: vre-prep-consistency-audit
created: 2026-09-13
status: audit record — CRITICAL items open
scope: VRE-EVALUATION-PREP-2026-09-17.md vs. the va-disability corpus
---

# Consistency Audit — VR&E Prep Doc vs. Corpus

Cross-reference pass run by the repo's `claim-consistency-checker` agent after the prep document
was drafted, per the source prompt's Phase 6. **It caught three CRITICAL errors in the draft**,
two of which would have produced a misstatement to a federal official. Recording it here because
the failure mode is reusable, not because the findings are merely historical.

**Verification scope limit.** `personal-records/` and `ClaudeDisabilityAssets/` do not exist in
this checkout, and `supporting-docs/` holds only `PocketBuddyLetter.md`. The signed personal
statement, 21-0781, Cherie's nexus letter, and Erica's 07/12/2026 statement could not be read
directly. **Everything below is verified at _corpus_ level** — against research docs that quote
those primary documents.

---

## The root cause, stated once

All three CRITICAL findings share one cause, and it is worth fixing structurally rather than
case by case:

> **`va-disability/CLAUDE.md` names `MASTER-STRATEGY.md` and `CLAIM-ASSESSMENT.md` as the current
> working docs. `planning-docs/RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md` is ten days newer and
> REVERSES positions in both — and CLAUDE.md's "Start here" never mentions it.**

A subagent read exactly the corpus CLAUDE.md prescribes and came back wrong on three material
points. That is a navigation defect in the repo, not an agent error, and it will reproduce for
anyone who follows the documented reading path. Same applies to `PATH-TO-100-PERCENT-2026-07-07.md`
§9, which both files point to for odds via internal `[SUPERSEDED]` markers but which CLAUDE.md
also omits.

---

## CRITICAL — resolved in the prep doc, still open in fact

### C1 · TDIU posture is conflicted, not settled

- **Draft said:** TDIU "not being pursued — CONFIRMED"; answer **"no"** to 28-1902w Section VII
  Item 20.
- **Reality:** `RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md` **[CORRECTION 2]** turns Task 5 into
  "§ 4.16 **TDIU development**"; **[CORRECTION 3]** states the plan "now develops 100% schedular
  _and_ TDIU _and_ SMC A&A"; **line 158** lists **"TDIU application (T5) · VA Form 21-8940 ·
  VET/REP · [ ] filed."**
- **Why it mattered:** Item 20 asks whether the veteran has _filed for or is receiving_ IU/TDIU.
  A wrong "no" is a dated, signed misstatement to a federal official — on the exact axis the
  corpus already flags as the biggest fraud exposure.
- **Status:** prep doc §9.0.1 rewritten; row L retagged **CONFLICT**.
  **OPEN — requires the rep to confirm what has actually been filed since 2026-07-16.**

### C2 · The recommended framing contradicts the veteran's own signed evidence

- **Draft recommended:** _"I can work full time — I've done it at a senior level. What I haven't
  been able to do is sustain it."_
- **Conflicting signed evidence:** Cherie Mills LCSW nexus letter, 07/02/2026 — _"These symptoms
  have caused Marcus **total impairment in occupational and social realms**."_
  Plus **[CORRECTION 3]**: the marriage is a **"caretaker–patient dependency"** (spouse performs
  hygiene, feeds him, cuts his hair, reminds him to shower, attends appointments).
- **Why it mattered:** the draft's §5.4 "Liabilities" and §9.3 "landmines" contained **no
  reference whatsoever** to the nexus letter or the ADL dependency. A VRC note reading "veteran
  states he can work full time at a senior level" would sit in the same C-file as both.
- **Note:** the corpus independently flags this tension — `MASTER-STRATEGY.md` line 15 records
  that the "total impairment" sentence sits beside a description of "obsessive overworking," and
  treats the letter as **not yet** a settled improvement to the odds.
  `document-analysis/nexus-letter-cherie-ANALYSIS.md` flags the same. **The conflict predates
  VR&E.**
- **Status:** prep doc §9.0.2 added. **OPEN — only the veteran can decide which description is
  factually true, and §5/§8.3 must be rewritten if it is the caretaker-dependency picture.**

### C3 · The corpus had already reconciled what the draft called unresolved

The draft flagged a "four-account, none reconciled" employment conflict and sent the veteran to
reconstruct it from memory. Two corpus documents already answered much of it:

- **`RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md` Task 5**, "Corrected occupational history":
  _"job loss **Dec 2024**; a new job then lost **June 2026** for **performance / threatened PIP**,
  resolved by a **negotiated severance**; after which the veteran **left the software-engineering
  career**."_
- The **Dec 2024 loss** was omitted from the draft entirely — corroborated by the Starlite
  admission 2024-12-26 (opioid relapse after being "recently laid off") and `CLAIM-MASTER-BRIEF.md`
  §5.
- Task 5 also records that **HR emails, the PIP record, the severance agreement, and
  FMLA/disability records all exist.**
- **Status:** prep doc §3.2 and §3.3 #3 corrected to the four-step chain. Open reconciliation:
  Erica's signed statement lists 2018/2023/2026 and omits Dec 2024 (`CLAIM-MASTER-BRIEF.md` §5).

---

## HIGH

| #      | Finding                                                                                                                                                                                                                                                                                                                                                                      | Status                                                            |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **H1** | Draft called in-service Restoril/Ambien **"documented corroboration."** `COMPREHENSIVE-FINDINGS-2026-07.md` §9b item 7 calls it the _"currently-unverified in-service Ambien claim now load-bearing in two signed documents"_; §4 lists STRs as still missing. This was carrying the **entire § 21.51(c)(1) causation bridge**                                               | Fixed — §4.4 and §5.3 retagged as recollection, not documentation |
| **H2** | Draft treated the Lake Charles address as a **subsistence-rate** question. `MASTER-STRATEGY.md` §3 (2026-07-31) calls it _"a live operational risk to both tracks"_ — a C&P notice to a stale address can be **failure to report**, and under **38 C.F.R. § 3.655(a)–(b)** the claim is **denied outright**                                                                  | Fixed — promoted to an urgent checklist item in §2                |
| **H3** | The **Metal employment statement (08/04/2026)** is recommended as key evidence, but has **no row in `DOCUMENT-PROVENANCE.md`** — a log whose stated purpose is tracking who wrote the substantive content of every claim-facing document. "Drafted **for you**" describes a third party producing a VA-facing statement about the veteran — the same axis as the Part 0 risk | **OPEN** — provenance unlogged and unasked                        |
| **H4** | Draft reasoned that declining TDIU "reduces the collision" with VR&E feasibility. Wrong: the schedular-100% target requires "total occupational **AND** social impairment" — **both prongs** — so declining TDIU narrows the collision to one prong but does not reduce occupational exposure at all                                                                         | Fixed — §9.1 rewritten                                            |
| **H5** | §6.2 recommended asking for **Long-Term Services** without noting that the corpus's _only_ prior VR&E analysis (`claim-maximization-research-2026-06.md` §D) proposes VR&E specifically to fund **the CPA-firm transition** — while the **same file, line 157**, calls a staged CPA-firm transition _"the paradigm case of VA benefits fraud"_                               | Fixed — warning added at the point of decision                    |
| **H6** | Draft's model "reason for leaving" sentence used a **medical-leave** framing; the corrected reason of record is **performance / threatened PIP resolved by negotiated severance**. The draft's own §9.3 warns "do not soften something a former employer would describe differently" — and its model sentence did exactly that                                               | Fixed — §8.3 rewritten                                            |

---

## MEDIUM

- **M1** — "Four-way conflict" overstated it. `claim-maximization-research-2026-06.md` lines 1845
  and 1897 establish that "his brother" and "family CPA firm" are **one entity**; the arithmetic
  agrees (~$200K → $40–60K ≈ 75%). The real difference between Accounts 1 and 2 is **tense**, not
  substance.
- **M2** — "**Meta**" appears in the ask list but not in the quoted recruiter evidence (which names
  MNTN, **Metal**, DISQO). Given `metal.ai` is a startup and Meta is Facebook, a one-letter
  conflation entering a federal employment form is a live data-entry risk.
- **M3** — Treatment count understated: the draft said "at least 9" while **its own enumerated list
  contains 11**, `veteran-profile.md` says "10+", and the **signed 21-0781** says "around 10."
  _Fixed to eleven, with a note to stay consistent with the signed form._
- **M4** — Condition list omits **ASD**, **insomnia**, and hearing loss. 28-1902w Section VII covers
  **non-service-connected** disabilities too, and ASD is directly relevant to both § 21.52 severity
  and the interpretation of the aptitude/interest instruments.
- **M5** — The Part 0 characterization is **verbatim accurate** to `CLAIM-ASSESSMENT.md` §0.1 and
  not overstated. Two omissions: (a) provenance was **subsequently closed upward** — Erica's signed
  07/12/2026 statement is self-authored per `DOCUMENT-PROVENANCE.md`; (b) still open **downward** —
  `document-analysis/Erica-Personal-Statement-ANALYSIS.md` scores the working file 3/10 and finds it
  byte-identical to `BLOG-POST-DRAFT-OUR-STORY.md`. Minor mis-attribution: the "cascade" language is
  from `COMPREHENSIVE-FINDINGS-2026-07.md` §0.2, not `CLAIM-ASSESSMENT.md` Part 0.
- **M6** — Account 3 is corroborated in Erica's signed statement ¶8 "almost verbatim in structure
  and sequence," which raises its weight. But `COMPREHENSIVE-FINDINGS-2026-07.md` §1 sources the
  Lake Charles / tech-exit facts partly to the **Erica email chain** — the very thread Part 0 says
  not to derive from.
- **M7** — A **fifth** income figure exists: `planning-docs/strategy.md` line 26 says "~$157K";
  `MASTER-STRATEGY.md` line 21 says "~$150–200K". Section II asks gross monthly salary per job.

---

## LOW

- **L1** — Row B cites `veteran-profile.md` gap #4, which actually reads "**Tinnitus claim date**"
  — claim date ≠ date of notification of rating. Fact still unknown; citation imprecise.
- **L2** — Row D4 drops a hedge: corpus says "(**presumably** PTSD/MST) is denied."
- **L3** — "None rated / none adjudicated" sits against row D4's 2024 denial — a denial _is_ an
  adjudication. "None currently rated" is accurate.
- **L4** — Row D staleness can advance from 2026-07-06 to **2026-07-16**.
- **L5** — "Zoe Behavioral PHP" vs. corpus "Zoe Behavioral **Health** PHP" — trivial, but §7.3
  instructs transcribing facility names onto the form.
- **L6** — Gmail-sourced rows (28-1900 filing, eVA emails, recruiter mail, Metal statement) are
  outside this checkout and could not be independently checked.

---

## Verified clean

Discharge **2013-11-22**; enlistment 2009-11-23; Honorable, sep code MBK, reentry 1J; USAF F-15
crew chief, Seymour Johnson AFB, no deployment. The post-1/1/2013 carve-out arithmetic and the
"12 years expired 11/22/2025" backstop. Claim dates (received 2026-05-19, development letter
2026-05-29, soft deadline ~2026-06-28). **B.S. CS, McNeese State, 2016-12.** Married **Erica
Jure**, Nov 2022 (surname correctly resolved to "Jure"). **All eleven treatment episodes** —
facility names and date ranges — match `COMPREHENSIVE-FINDINGS-2026-07.md` §2 exactly. June 2026
relapse; FMLA window; sleep apnea status; ankle date dispute; tinnitus 10% sole SC. "3–4 job
losses in under 10 years" verbatim. The "work until I burn out, then relapse" cycle. The Aug-2024
Starlite "gainfully employed" note and its characterization as accurate-at-the-time. The
fraud-paradigm attribution to line 157. The Sunday/Thursday day-of-week correction.

---

## Open items carried forward

1. **What has the rep actually filed since 2026-07-16?** (C1)
2. **Which capacity description is factually true?** (C2) — gates §5 and §8.3 of the prep doc
3. **Provenance of the Metal employment statement** (H3)
4. Per-employer detail: employers, dates, gross monthly salary, reason for leaving
5. Reconcile the **Dec 2024** date against Erica's signed statement (C3)
6. Post-9/11 GI Bill months remaining
7. Current sobriety status (last data point: early June 2026)
8. Dependent children — corpus silent in both directions
9. Current residence — Lake Charles LA vs. Texas, and **update the address with VA** (H2)
