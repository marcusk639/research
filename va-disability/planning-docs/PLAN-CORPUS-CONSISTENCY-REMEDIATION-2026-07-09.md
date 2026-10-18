# Execution Plan — Corpus Consistency & Contradiction Remediation

> **⚠ CORRECTION 2026-10-18 — read [`STRATEGY-TO-100-2026-10-18.md`](STRATEGY-TO-100-2026-10-18.md) first.** 38 CFR 4.130 has no 90% mental-health rating (levels are 0/10/30/50/70/100), so every "90% MH" figure and the "90% MH + 50% sleep apnea = 100%" Route 2 in this document are invalid. The current rating is 20% (ankle 10% + tinnitus 10%): MH 70 → 80% combined; MH 70 + sleep apnea 50 → 90%; only MH 100 reliably reaches 100%. Odds and route math here are superseded; evidence work and guardrails still stand.

> **Status:** active plan · **Created:** 2026-07-09 · **Type:** phased remediation plan (via `make-plan`)
> **Goal:** resolve every inconsistency/contradiction across the `va-disability/` corpus, cleanly separating what the corpus _maintainer_ may reconcile from what only the _veteran/VSO/clinician_ may resolve.
> **Discovery basis:** a full-corpus `claim-consistency-checker` sweep (2026-07-09) + a `citation-verifier` pass on the outstanding H-5 cites (2026-07-09). Both are consolidated in Phase 0.
> **The governing distinction (read before doing anything):**
>
> - **TYPE-A — corpus-internal:** analysis/strategy docs disagree with each other or with the facts canon. **Safe for the maintainer to reconcile** by editing the analysis docs to one correct statement.
> - **TYPE-B — claim-facing/evidentiary:** the conflict touches a signed statement, the actual VA record, a witness account, or the clinician's letter. **The maintainer may NEVER "fix" these by editing what a document says happened.** They are flagged and handed to the veteran + VSO + clinician; witnesses resolve their own content in their own words. **No drafting, scripting, or suggested wording — ever.**
>   **Not legal/medical advice.** TYPE-B resolution belongs to the veteran and an accredited VSO/attorney.

---

## Phase 0 — Discovery (COMPLETE — consolidated inventory)

### 0.1 Citation resolution (H-5 CLEARED, 2026-07-09)

`citation-verifier` **CONFIRMED** all four outstanding cites against primary sources: _Nieves-Rodriguez v. Peake_, 22 Vet. App. 295 (2008); 38 C.F.R. § 4.2 (verbatim); BVA 1513531 and 22009295 (both genuinely adverse on the married-veteran question, non-precedential). **Action carried into Phase 1:** flip their `[pending citation-verifier]` tags to `[confirmed]`. **One caveat:** if the _Nieves-Rodriguez_ "expert witnesses" phrase is ever placed inside quotation marks in a filing, confirm exact wording against the opinion PDF first (the substantive proposition is confirmed regardless).

### 0.2 TYPE-B inventory (claim-facing — hand-off only)

| ID      | Conflict                                                                                                                                                                                                                                                                                               | Severity                      | Register map                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------- |
| **B1**  | Strategy docs assert a **Dec-2024 job loss attributed by Erica to depression/SUD** as established; **Erica's signed statement lists only 2018/2023/2026 and contains no Dec-2024 event**. (COMPREHENSIVE §2 notes a Dec-2024 "recently laid off" Starlite readmission, so an event _may_ exist.)       | **Critical**                  | NEW (touches I-4/I-6/I-20)                        |
| **B2**  | Ankle fracture **"May 2011"** (personal statement) vs **"2012"** (2015 VA intake) — self-contradiction in the veteran's own records; feeds the direct-SC ankle claim                                                                                                                                   | Medium                        | NEW (in COMPREHENSIVE §2, not in master register) |
| **B3a** | Reyes buddy form: **"4th Maintenance Squadron"** vs DD-214 **"4th Equipment Maintenance Squadron"**                                                                                                                                                                                                    | Medium                        | COMPREHENSIVE §9a-3; dropped from master register |
| **B3b** | Spouse surname: personal-statement evidence list **"Erica Jure"** vs **"Erica Klein"** elsewhere — confirm legal name before she signs a 21-10210                                                                                                                                                      | Medium                        | §9a-5; dropped                                    |
| **B3c** | Harmony stay **"25 day"** (statement) vs discharge dates computing to **24 days**                                                                                                                                                                                                                      | Low                           | §9a-4; dropped                                    |
| **B3d** | CPT Impact Statement **"age twenty-two"** vs assault date → age 23 (DOB 05/30/1989)                                                                                                                                                                                                                    | Low                           | §9a-6; dropped                                    |
| **B4**  | Cherie's signed nexus letter: **DOB "30 May 1998"** (should be 1989), surname **"Kline"/"Klein"**, two phone numbers; and **SUD omitted from the condition-line and formal conclusion** (though pled as secondary in the body)                                                                         | Medium (IDs) / Low (omission) | DOCUMENT-PROVENANCE / COMPREHENSIVE §0.13         |
| **B5**  | Marriage: new **caretaker/roommate, ADL/hygiene-dependent** framing exists in **no signed/authored document** — Erica's statement + blog draft describe devotion/partnership; nexus letter says only "near-divorce strain"                                                                             | High                          | **I-20** (confirmed accurate)                     |
| **B6**  | Confirmed still-open (verified current): SI-fluctuation **I-7**; opioid/pre-service-use statement contradiction **I-8**; MST non-disclosure **I-9**; Poquette timing **I-10**; two PsychEvals **I-17**; OCD absent from 21-0781 **I-13**; F15.20 **I-11**; ADL/delusions not yet in record **I-1/I-5** | varies                        | existing IDs                                      |

### 0.3 TYPE-A inventory (corpus-internal — maintainer reconciles)

| ID     | Conflict                                                                                                                                                                                                                                                                                                      | Fix target                                                                                                                                                                                                                                                | Severity |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| **A1** | Stale/wrong WHODAS description ("psychologist-signed," "high-severity GAD/MDD scores," "broken export") persists although COMPREHENSIVE §0.7 is already corrected                                                                                                                                             | `MASTER-STRATEGY.md` §1 item 10; `NEXUS-LETTER-GUIDE-CHERIE.md` §6; `CLAIM-ASSESSMENT.md` §0.2/#10; `ACTION-CHECKLIST-100-PERCENT.md` line 69. **Re-scope H-2** (it wrongly names §0.7, already fixed)                                                    | Medium   |
| **A2** | Route 2 "more reliable than Route 1" walk-back applied only in the master guide                                                                                                                                                                                                                               | Propagate "modestly higher-probability if positive; inherits 90%-MH burden; not a safe fallback" to `PATH-TO-100` §1/§5/§9, `CLAIM-COMPLETION-PLAN` §3, `CLAIM-MASTER-BRIEF` §1                                                                           | Medium   |
| **A3** | "Single most outcome-determinative = examiner's selection" contradicts the corrected 4.126(a) whole-record posture; the `PATH-TO-100` §11-V4 softening was never applied                                                                                                                                      | `CP-EXAM-PREP-MENTAL-HEALTH.md` header; `100-PERCENT-SCHEDULAR-PATHWAY.md` §3 (lines 41, 116)                                                                                                                                                             | Medium   |
| **A4** | Superseded "80–90% combined / 100% a stretch" odds                                                                                                                                                                                                                                                            | Point `MASTER-STRATEGY.md` **and** `CLAIM-ASSESSMENT.md` Part 2 at `PATH-TO-100` §9 as governing (**extend H-4** to CLAIM-ASSESSMENT)                                                                                                                     | Medium   |
| **A5** | Master guide §1 lists Route 1 "40–50%" while its own Status-update says "25–35% today / 45–50% if it lands," unannotated                                                                                                                                                                                      | Annotate the §1 Route 1 figure as refined by the Status-update/reassessment                                                                                                                                                                               | Low      |
| **A6** | Master guide §5 header still says "**24 issues**" / "extended (I-16…**I-19**)" though I-20 exists and the summary line totals 25                                                                                                                                                                              | `MASTER-CLAIM-STRATEGY` §5 header → 25 / "I-16…I-20"                                                                                                                                                                                                      | Low      |
| **A7** | Claim date **19 vs 29 May**, plus "development letter" relabeled as "acknowledgment/receipt" in newer docs                                                                                                                                                                                                    | Reconcile to COMPREHENSIVE §2 (received 19 May; development letter 29 May); **VSO confirms the VA-recorded receipt date at the eFolder pull** (interacts with I-16). **= H-3**, note the relabeling wrinkle                                               | Medium   |
| **A8** | Citation-label drift: _Nieves-Rodriguez_ pending in some docs but "confirmed real" in `CREDIBILITY-INCONSISTENCY-RESEARCH.md`; _Rice v. Shinseki_ pincited-as-settled in some docs, pending in master; married-vet BVA balance shown **1-adverse-vs-1** in `PATH-TO-100` §2.2/§9 but **3-vs-1** in later docs | Apply the H-5 result (Nieves-Rodriguez → confirmed); set one consistent label per cite; reconcile the married-vet balance to the current **3-adverse-vs-1-favorable** (labeled a non-representative sample, not weight-of-authority) across `PATH-TO-100` | Low      |

---

## Phase 1 — Reconcile all TYPE-A contradictions (maintainer edits; safe, self-contained)

**What to do:** edit only the analysis/strategy docs named in 0.3 so each conflicting statement matches the already-established correct version. This is pure documentation hygiene — no claim-facing content, no signed documents, no witness/clinician wording.

**Task list (each = one reconciliation):**

1. **A1 (WHODAS):** replace every "psychologist-signed / high-severity GAD-MDD scores / broken export" description with the corrected "in-hand, self-administered vendor functional instrument (~69.72% overall, self-care 62.5%), not psychologist-signed" in the four files listed. Re-scope H-2's target text accordingly.
2. **A2 (Route 2 framing):** propagate the "modestly higher if positive, not a safe fallback, inherits the 90%-MH burden" language to the three files.
3. **A3 (exam framing):** soften "single most outcome-determinative" in the two files to the 4.126(a) whole-record posture (the examiner's selection is _influential_, not _dispositive_; the rater weighs the whole record).
4. **A4 (odds):** point CLAIM-ASSESSMENT Part 2 and MASTER-STRATEGY odds lines at `PATH-TO-100` §9 as governing.
5. **A5 (master §1 annotation):** annotate the Route 1 §1 figure as "refined by the 2026-07-09 reassessment — see Status update."
6. **A6 (register count):** master guide §5 header → "25 issues" / "I-16…I-20."
7. **A8 (citation labels):** flip _Nieves-Rodriguez_ to `[confirmed — citation-verifier 2026-07-09]` everywhere; set _Rice_ to one consistent label; reconcile the married-vet BVA balance to 3-vs-1 (non-representative sample) in `PATH-TO-100`.

**Special handling — B1's TYPE-A half:** in every strategy doc that asserts the Dec-2024 job loss as _established, Erica-attributed_ fact (`PATH-TO-100` §I-4(d), `CLAIM-COMPLETION-PLAN` Tier 2 #8, `CLAIM-MASTER-BRIEF` §5, `VA-SUBMISSION-GUIDE` §4, `CP-EXAM-PREP`), **downgrade the assertion** to: "the record notes a possible Dec-2024 layoff (COMPREHENSIVE §2); Erica's current statement does not describe one — she includes it only if she genuinely recalls it, in her own words." This corrects the overclaim without touching Erica's statement.

**Verification:** re-grep each fixed string is gone; the reconciled statement appears; no signed/claim-facing file (`personal-records/**`, `nexus-letter-cherie.md`, Erica's statement, buddy forms, blog draft) was modified.

**Anti-patterns:** do NOT "reconcile" a TYPE-B fact by editing an analysis doc to match a wrong record, or vice-versa; do NOT touch signed documents; do NOT delete the contradiction from the register — mark it resolved with a pointer.

---

## Phase 2 — Root-cause fix: one canonical fact block + register the orphans

**Why:** most TYPE-A drift is the same handful of facts re-stated across docs and updated in only some. Fix the _source_, not just the instances.

1. **Canonical fact block** — in `COMPREHENSIVE-FINDINGS-2026-07.md` (or a short new `CANONICAL-FACTS.md` it links), pin the single authoritative value for the recurring cross-doc facts: claim dates (received 19 May / development letter 29 May, pending eFolder confirm), WHODAS description, the odds anchor (`PATH-TO-100` §9), PTSD-diagnosis status (supplied by Cherie's 2 July letter), Route-2 framing, and the married-vet BVA balance (3-vs-1, non-representative). Future docs cite this block instead of re-asserting.
2. **Register the orphans** — carry **B2, B3a–d** from COMPREHENSIVE §9a into the master guide's §5 register as new tracked IDs (I-21…I-25) so each signed-document discrepancy has an owner. **Registering them is TYPE-A; resolving each is TYPE-B** (Phase 3).

**Verification:** each recurring fact has exactly one canonical statement; the orphaned discrepancies now appear in the master register with owners; the register count is updated again.

**Anti-patterns:** do not let the canonical block itself assert a TYPE-B fact as settled (e.g., don't "resolve" the ankle date — record both and flag for the veteran).

---

## Phase 3 — TYPE-B claim-facing reconciliation worklist (hand-off; flag-only, never coach)

**Output:** a single `CLAIM-RECONCILIATION-WORKLIST.md` for the veteran + VSO — every TYPE-B item (B1–B6 and the confirmed-open I-7/8/9/10/17), each with: (a) the conflict stated neutrally ("record X says P; record Y says Q"), (b) why it's a credibility/eligibility risk, (c) the owner (veteran / VSO / Cherie / Erica), (d) the concrete resolution action — **with zero drafted wording for any statement.**

**Ordering (most consequential first):**

1. **B1 (Critical)** — confirm whether a Dec-2024 job loss actually occurred (VSO checks records; COMPREHENSIVE §2 suggests a Starlite readmission event). Erica includes it **only if she genuinely recalls it, her own words**; until then, no doc may present it as her attribution.
2. **B5 / I-20 (High)** — the marriage characterization: the ADL/caretaker framing is in no signed document; the veteran/Erica/Cherie decide truthfully how to characterize it, consistently, without collision with the blog draft/earlier statement.
3. **I-8 (High per veteran)** — the pre-service-substance-use statement contradiction: confirm with the VSO how it was "resolved"; a corrective supplemental statement in the veteran's own words if needed (this is the _veteran's own_ statement — he may be helped to structure his genuine account, but it must be true and VSO/attorney-reviewed).
4. **I-17 (High)** — reconcile the two PsychEvals before either is submitted.
5. **B2, B4 (Medium)** — ankle-date and Cherie-letter identifier corrections (a wrong DOB on a nexus letter is a real RO ID-matching risk).
6. **B3a–d, I-7, I-9, I-10 (Medium/Low)** — the remaining signed-document and disclosure items.

**Hard rule restated:** for any buddy/spouse/lay statement (Erica, Reyes, Poquette, Goff) the worklist may only _identify_ the discrepancy; the witness resolves it in their own unedited words. The one exception is the veteran's _own_ statement, where structural help is permissible but the content must be genuinely his and attorney/VSO-reviewed.

**Verification:** every TYPE-B item present with an owner and action; no drafted witness wording anywhere; the worklist references (does not duplicate) the signed source docs.

---

## Phase 4 — Verification (whole effort)

1. **Re-run `claim-consistency-checker`** on the corpus; confirm every TYPE-A item is reconciled and **no TYPE-B item was silently "fixed" by editing claim-facing/signed content.**
2. Confirm citation labels are consistent and H-5 cites read `[confirmed]`.
3. Confirm B2/B3 now carry register owners and the canonical fact block is in place and referenced.
4. Confirm the register counts are internally consistent.
5. PHI gate before any commit: `git status` + name/PII grep; never stage `personal-records/`, `ClaudeChat/`, `ClaudeDisabilityAssets/`.
6. Commit the TYPE-A/Phase-2 doc fixes + the worklist; update PR #8. **Do not commit or alter any signed/claim-facing file.**

## Guardrails (every phase)

- **TYPE-B is flag-and-hand-off only.** Never resolve a claim-facing contradiction by changing what a document says happened; never draft or suggest witness/clinician wording.
- **Never touch signed/claim-facing files** (`personal-records/**`, `nexus-letter-cherie.md`, Erica's statement, buddy forms) — the maintainer edits analysis docs only.
- **Citation discipline** — every legal cite `[confirmed — source]` or `[pending citation-verifier]`.
- **PHI discipline** — real records stay gitignored; never stage them.
- **Honesty** — reconcile to what is _true and documented_, never to what is _convenient_; where truth is unknown (ankle date, Dec-2024 job loss), record the conflict and hand it off rather than picking the helpful version.

## Scoping note for the user

Phase 1 (TYPE-A fixes) and Phase 3 (the worklist) are the highest-value, lowest-risk deliverables and can be executed now. Phase 2's canonical-fact-block is a durable recurrence-preventer. Say the word and I'll execute Phase 1 + build the Phase 3 worklist, then commit to PR #8 — leaving every signed/claim-facing document untouched.
