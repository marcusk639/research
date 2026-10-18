# Sleep Apnea — Rating Maximization Analysis

> **⚠ CORRECTION 2026-10-18 — read [`STRATEGY-TO-100-2026-10-18.md`](STRATEGY-TO-100-2026-10-18.md) first.** 38 CFR 4.130 has no 90% mental-health rating (levels are 0/10/30/50/70/100), so every "90% MH" figure and the "90% MH + 50% sleep apnea = 100%" Route 2 in this document are invalid. The current rating is 20% (ankle 10% + tinnitus 10%): MH 70 → 80% combined; MH 70 + sleep apnea 50 → 90%; only MH 100 reliably reaches 100%. Odds and route math here are superseded; evidence work and guardrails still stand.

> **Status:** active · **Created:** 2026-07-31 · **Type:** internal planning doc (never submitted to VA)
> **Parent:** [`SLEEP-APNEA-CLAIM-EXECUTION-PLAN-2026-07-31.md`](./SLEEP-APNEA-CLAIM-EXECUTION-PLAN-2026-07-31.md) — sequencing and deadlines. **This file answers a different question: given that the claim gets filed, what determines whether it lands at 50% instead of 30% or 0%, and what is realistically the ceiling?**
> **Legal basis:** [`SLEEP-APNEA-SECONDARY-CLAIM.md`](./SLEEP-APNEA-SECONDARY-CLAIM.md) (verified citation log).
> **Not legal or medical advice.** ✅ **All four new citations in this document were verified by `citation-verifier` on 2026-07-31** — see §9 for verdicts and the corrections applied. ⚠️ **One dated re-check is required before any filing after August 2026** (38 CFR § 4.130 / RIN 2900-AQ82 — §9 item 3).

---

## 1. The honest ceiling — read this first

**The realistic maximum for this claim is 50%.** Not 100%.

The 100% tier under DC 6847 requires **chronic respiratory failure with carbon dioxide retention, or cor pulmonale, or a tracheostomy**. That is end-stage disease. Nothing in this veteran's record suggests it, and pursuing it would waste credibility on an unreachable tier while the winnable one is sitting right there.

**So the entire game is: land 50%, don't settle for 30%, and don't get zeroed.** Everything below serves that.

The _combined_ outcome is a separate question — 50% OSA is what converts a 90% mental-health rating into a **100% combined** rating (§4). But that leverage comes from the mental-health track, not from stretching the OSA rating past what the evidence supports.

---

## 2. The rating tiers, and exactly what moves you between them

**38 CFR § 4.97, DC 6847** (verbatim text verified; unchanged since the 2006 amendment):

| Rating   | Criterion                                                                                           | What actually establishes it                            | Realistic here?                                                |
| -------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------- |
| **0%**   | Asymptomatic, with documented sleep-disordered breathing                                            | A positive sleep study and nothing else                 | ⚠️ **The downside risk** — diagnosis without a device          |
| **30%**  | Persistent daytime hypersomnolence                                                                  | Documented, persistent daytime sleepiness in the record | ⚠️ **The consolation outcome** — avoid landing here by default |
| **50%**  | **"Requires use of breathing assistance device such as continuous airway pressure (CPAP) machine"** | **A prescribed, medically-required CPAP**               | ✅ **The target**                                              |
| **100%** | Chronic respiratory failure w/ CO2 retention or cor pulmonale; or requires tracheostomy             | End-stage disease                                       | ❌ Not realistic — do not pursue                               |

### The single hinge: "requires"

The 50% tier does not turn on severity, AHI number, or how badly you sleep. **It turns on one word: _requires_.** A prescribed device that you are medically required to use is 50%. The same diagnosis without a prescribed device is 30% at most — and 0% if daytime hypersomnolence isn't documented either.

This is the highest-leverage, lowest-effort fact in the entire sleep-apnea track: **a 20-point rating swing sits on whether a CPAP prescription exists and is documented as medically necessary.**

**Therefore:**

- [ ] If OSA is confirmed, **get the CPAP prescribed** — and make sure the record says it is _required/medically necessary_, not "offered," "trialed," or "discussed as an option."
- [ ] **Actually use it, and keep the compliance data.** Every CPAP machine logs nightly usage. That data objectively corroborates the "requires" element and is difficult for a rater to discount.
- [ ] If a dental appliance or positional therapy is prescribed _instead_ of CPAP, flag it — the regulation says "such as" CPAP, so other breathing-assistance devices can qualify, but this is a weaker argument and needs the VSO's attention before filing.

> ⚠️ **A well-controlled-on-CPAP outcome still rates 50% under the current rule.** Do not let anyone (including a well-meaning clinician) frame successful treatment as "resolved." The criterion is that you _require_ the device — not that you're still symptomatic while using it. This is exactly what the pending NPRM would change (§6), which is why timing matters.

---

## 3. Evidence map — what has to be in the file, element by element

| Element                                    | What satisfies it                                                        | Status                        | Where it comes from                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------ | ----------------------------- | ---------------------------------------------------------------------------- |
| **Current diagnosis**                      | Polysomnography or home sleep apnea test with AHI/RDI                    | ❌ **Not ordered yet** (consult only) | The sleep study                                                              |
| **"Requires" a device**                    | CPAP prescription + documented medical necessity + compliance data       | ❌ Not yet                    | Phase 2, §2 above                                                            |
| **Service-connected primary**              | PTSD granted                                                             | ⏳ Pending Supplemental Claim | The MH track                                                                 |
| **Medical nexus**                          | Reasoned opinion, "at least as likely as not," from a competent provider | ❌ **Does not exist**         | [`SLEEP-APNEA-NEXUS-OPINION-GUIDE.md`](./SLEEP-APNEA-NEXUS-OPINION-GUIDE.md) |
| **Daytime hypersomnolence** (30% fallback) | Documented persistent daytime sleepiness                                 | Partially — report accurately | [`SLEEP-APNEA-APPOINTMENT-PREP.md`](./SLEEP-APNEA-APPOINTMENT-PREP.md)       |
| **Lay corroboration**                      | Witnessed apneas/gasping/snoring                                         | Available — Erica             | Her own genuine observations                                                 |

**Note the fallback deliberately:** documenting daytime hypersomnolence honestly protects a 30% floor if the CPAP prescription doesn't materialize. That is not a reason to overstate sleepiness — it's a reason to report it accurately rather than minimizing it, which people routinely do.

---

## 4. What 50% is actually worth — combined-rating math

VA combined ratings are not additive (38 CFR § 4.25). Each condition applies to the _remaining_ efficiency:

| Mental-health anchor | + OSA 50%                       | Combined | Rounds to   |
| -------------------- | ------------------------------- | -------- | ----------- |
| **90%**              | 90 + (50% of remaining 10) = 95 | 95       | **100%** ✅ |
| **80%**              | 80 + (50% of remaining 20) = 90 | 90       | **90%**     |
| **70%**              | 70 + (50% of remaining 30) = 85 | 85       | **90%**     |

**The strategic conclusion is unchanged from `PATH-TO-100-PERCENT-2026-07-07.md` and worth restating plainly:**

> **Sleep apnea only produces 100% if the mental-health rating lands at 90%.** From a 70% anchor, a 50% OSA rating gets you to 90% combined — valuable, but not 100%, and no realistic stack of additional secondaries closes that gap.
>
> **Raising the mental-health rating from 70 → 90 is worth more than anything else in this claim.** Sleep apnea is the finisher, not the engine. Do not let sleep-apnea work displace mental-health evidence work.

Tinnitus (10%) and the ankle (10%) are insurance on top: 95 & 10 & 10 ≈ 96 → still 100%.

**Also worth knowing:** if the mental-health condition alone is ever rated **100% — a _single_ disability rated as total** — a 50% OSA rating would count toward the **60%** required by **38 U.S.C. § 1114(s) / 38 CFR § 3.350(i)(1)**: additional service-connected disability or disabilities _"independently ratable at 60 percent, separate and distinct from the 100 percent service-connected disability and involving different anatomical segments or bodily systems."_ OSA (respiratory, § 4.97) satisfies the different-bodily-system element as against a mental disorder, and the fact that OSA is claimed as _secondary_ does not by itself defeat "separate and distinct." **A 50% OSA rating counts toward the 60% threshold — it does not meet it.** That's additional monthly compensation, not additional percentage. Raise it with the VSO only after the primary ratings land.

> ⚠️ **The word doing the work is "single."** A **combined** 100% rating does **not** qualify for SMC-S — it must be one disability rated as total. Also note the statute is broader than the regulation: § 1114(s) says "a service-connected disability rated as total," not "100 percent schedular," and _Bradley v. Peake_, 22 Vet.App. 280, 293 (2008) holds TDIU based on a _single_ disability can satisfy it. Since TDIU is not being pursued here, that has no practical effect — but don't state SMC-S as a schedular-only rule, because it isn't.

---

## 5. The pyramiding objection — anticipate it

**This is the most likely substantive attack on the claim, and it is answerable.**

38 CFR § 4.14 prohibits rating "the same manifestation under different diagnoses." A rater could argue that sleep problems are **already compensated** in the mental-health rating — because **"chronic sleep impairment" is a named symptom in the 30% tier of the § 4.130 General Rating Formula**. If that argument lands, the OSA rating gets absorbed and contributes nothing.

**The answer, which should be pled affirmatively rather than waiting for the objection:**

1. **The controlling legal test is _symptom overlap_ — lead with this.** "The critical element in permitting the assignment of several ratings under various diagnostic codes is that **none of the symptomatology for any one of the disabilities is duplicative or overlapping with the symptomatology of the other disability**" — _Esteban v. Brown_, 6 Vet.App. 259, 261-62 (1994) (verified 2026-07-31). The manifestations here are genuinely distinct: **apneic events and oxygen desaturation are not the same manifestation as trauma nightmares.**
2. **Supporting factual argument (not the legal standard).** OSA is an **organic respiratory disorder** — an upper-airway obstruction with objective polysomnographic findings (AHI/RDI) — rated under **§ 4.97**, while psychiatric "chronic sleep impairment" is insomnia/nightmares/non-restorative sleep as a _psychiatric_ symptom under **§ 4.130**.
   ⚠️ **Do not present "different body system, different diagnostic code" as the _Esteban_ test — it isn't.** _Esteban_ itself awarded three separate ratings under different DCs for residuals of **one** facial injury. Taxonomy is not what it turns on; symptom overlap is. Use this as corroborating fact, not as the rule.
3. **The device requirement is unique to OSA.** Nothing in the mental-health rating compensates for requiring nightly mechanical ventilatory support.

> ⚠️ **Know the adverse authority before the VSO meets it cold.** _Amberman v. Shinseki_, 570 F.3d 1377 (Fed. Cir. 2009) holds that **distinctly diagnosed conditions may _not_ be separately evaluated where the symptomatology is the same** — the mirror image of _Esteban_. And **BVA Citation Nr. A25013976 (Feb. 13, 2025)** denied a separate insomnia rating on exactly this ground, because the sleep symptoms overlapped with an already-compensated rating.
>
> **The fact that distinguishes this claim from A25013976 is the PSG-confirmed OSA diagnosis with objective AHI/RDI findings and a device requirement.** Without the sleep study, the _Esteban_ argument has nothing to stand on — objective apneic events are what make the symptomatology non-duplicative. This is one more reason the sleep study is the gate on everything.

- [ ] **Action:** have the VSO address pyramiding _in the filing_, not reactively on appeal. One paragraph pre-empting it is far cheaper than a Higher-Level Review.

---

## 6. Timing risk — the regulatory clock

**NPRM 87 FR 8474** (Feb. 15, 2022) proposes restructuring DC 6847 so the automatic 50%-for-CPAP tier disappears. Per the `citation-verifier` correction logged in `PATH-TO-100-PERCENT-2026-07-07.md` §5.2, the proposed tiers are **0/10/50/100 based on treatment responsiveness — there is no 30% tier** — and **a veteran well-controlled on CPAP would likely fall to 0% or 10%**.

That would not reduce this claim's value. It would **eliminate** it — taking the Route 2 combined outcome from 100% down to ~90%.

Current status: **still proposed only.** No final rule, no effective date; the 50% CPAP tier remains in force. Existing CPAP-tier ratings are expected to be grandfathered if it finalizes.

- [ ] **Re-confirm the rule's status immediately before filing.**
- [ ] **Treat this as a reason to move fast.** It is the strongest argument against the "wait until the PTSD claim is finalized" instinct — every month of delay is exposure to a rule change that zeroes the claim.

---

## 7. Effective date — the other half of the money

The rating percentage determines the monthly amount. **The effective date determines how many months of backpay come with it.** These are independent, and the second is entirely procedural — it costs nothing but a form and a calendar entry.

- **Rule:** the effective date for a secondary condition is the date VA receives the claim (or a valid Intent to File), **not** the primary condition's effective date (38 CFR § 3.400).
- **Therefore:** filing the ITF today is worth real money regardless of when the diagnosis or nexus arrives.
- **The 365-day trap:** an ITF expires one year from receipt (§ 3.155(b)). Miss it and the effective date resets to the actual filing date — **no cure exists.**

See the parent execution plan §2–3 for the deadline mechanics and the `ITF + 10 months` trigger.

---

## 8. Risk register

| #   | Risk                                                             | Impact                                                                                                                                                                                                                   | Mitigation                                                                                                                                                            |
| --- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Sleep study is negative for OSA**                              | Claim ends                                                                                                                                                                                                               | Nothing to do but report symptoms accurately. If negative, **stop** — do not pursue a claim without a diagnosis, and redirect all effort to the mental-health rating. |
| 2   | **Diagnosed but no CPAP prescribed**                             | 50% → 30% or 0%                                                                                                                                                                                                          | §2 — ensure the prescription and medical-necessity language exist                                                                                                     |
| 3   | **Rater treats sleep symptoms as already compensated**           | Rating absorbed, contributes 0                                                                                                                                                                                           | §5 — plead the _Esteban_ / distinct-pathology argument affirmatively                                                                                                  |
| 4   | **DC 6847 rule finalizes before the grant**                      | Claim value → ~0                                                                                                                                                                                                         | §6 — file fast, re-verify at filing                                                                                                                                   |
| 5   | **Nexus opinion is a bare conclusion**                           | Low probative value; likely denial                                                                                                                                                                                       | [`SLEEP-APNEA-NEXUS-OPINION-GUIDE.md`](./SLEEP-APNEA-NEXUS-OPINION-GUIDE.md)                                                                                          |
| 6   | **ITF window expires while waiting on PTSD**                     | Backpay forfeited, no cure                                                                                                                                                                                               | Parent plan §2 — file inside the window regardless                                                                                                                    |
| 7   | **PTSD is denied**                                               | No service-connected primary → secondary fails                                                                                                                                                                           | Secondary claim gets deferred/denied with it; it revives if PTSD is won on appeal. Another reason the MH track is the priority.                                       |
| 8   | **Mental health lands at 70%, not 90%**                          | Combined caps at 90%, not 100%                                                                                                                                                                                           | §4 — this is a mental-health problem, not a sleep-apnea problem                                                                                                       |
| 9   | **C&P notice sent to stale address after the Lake Charles move** | Failure to report without good cause → an **original compensation claim** is _rated on the evidence of record_; **a claim for increase or a previously-disallowed supplemental claim is denied** (38 CFR § 3.655(a)–(b)) | Update the address with VA now. Sharper exposure on the **mental-health** track than on sleep apnea — see execution plan §3 item 0.2                                  |

---

## 9. Citations needing verification

Verified in `SLEEP-APNEA-SECONDARY-CLAIM.md`'s own 17-item log: DC 6847 / § 4.97, § 3.310, _Wallin_, _Allen_, VAOPGCPREC 1-2017, _Walsh_, BVA 1648003 and A21018009, McCall & Watson, Babson, § 3.159, 87 FR 8474.

**New in this document — all four ran through `citation-verifier` on 2026-07-31. Verdicts:**

1. ✅ **CONFIRMED (corroborated)** — _Esteban v. Brown_, 6 Vet.App. 259, 261-62 (1994) (§5). Citation, pincite, and proposition all check out; the OSA/§ 4.130 application is a fair use of the rule, **not** an overreach. Two deployment fixes were applied to §5: the legal test is **symptom overlap**, not different-body-system taxonomy, and the adverse authority (_Amberman v. Shinseki_, 570 F.3d 1377 (Fed. Cir. 2009); BVA A25013976) is now named. _Full opinion text not directly read — CourtListener HTML empty, API 401; certified via CourtListener search API and corroborated at the identical pincite across BVA 22016914 and A25013976._
2. ✅ **CONFIRMED-WITH-CORRECTION** — 38 CFR § **3.655(a)–(b)** (§8 row 9). Read verbatim from govinfo. The outcome is fixed by **claim type**, not a menu, and is gated on **"without good cause."** Corrected in the table. See execution plan §8 for the disclosed § 3.160 "original claim" interpretive tension.
3. ✅ **CONFIRMED** — 38 CFR § 4.130 (§5). Read verbatim from govinfo (2025 annual edition). **"Chronic sleep impairment" appears at the 30% tier and nowhere else** in the General Rating Formula (all six tiers checked). §5 is accurate as written.
   ⚠️ **DATED RE-CHECK REQUIRED — before any filing after August 2026.** VA's mental-disorders rating-schedule overhaul (**RIN 2900-AQ82**, NPRM at **87 FR 8498**, Feb. 15, 2022) is at **Final Rule Stage with projected final action 08/2026**. It would revise the General Rating Formula wholesale — domain-based criteria, a 10% minimum, and removal of the "total occupational and social impairment" requirement at 100%. **If it publishes, the "chronic sleep impairment at 30%" pyramiding defense in §5 may become obsolete, and the entire mental-health rating strategy shifts.** _(Note: the June 2026 corpus ledger recorded this rulemaking's FR start page and docket incorrectly — the correct values are **87 FR 8498** and **VA-2022-VBA-0010, RIN 2900-AQ82**. Do not propagate the old figures. This is a different rulemaking from the DC 6847 NPRM at 87 FR 8474 in §6.)_
4. ✅ **CONFIRMED-WITH-CORRECTION** — SMC-S, **38 U.S.C. § 1114(s) / 38 CFR § 3.350(i)(1)** (§4). Read verbatim from govinfo and Cornell LII. Three imprecisions corrected: "100% schedular" is not the requirement (a **single** disability **rated as total** is); a **combined** 100% does not qualify; and the omitted elements — **"separate and distinct"** and **"different anatomical segments or bodily systems"** — are now stated, with the 60% satisfiable by one **or more** disabilities. _Bradley v. Peake_, 22 Vet.App. 280, 293 (2008) corroborated but not directly read.

**Also corrected outside this document:** the same imprecise § 3.655 phrasing appeared untagged in `MASTER-STRATEGY.md` §3 and `ACTION-CHECKLIST-100-PERCENT.md` item 1a — both fixed 2026-07-31.

**Environment caveat from the verification pass:** ecfr.gov and federalregister.gov were unreachable (both 302-redirect to `unblock.federalregister.gov`). All CFR text was read from **govinfo.gov** annual editions instead, cross-checked against Cornell LII. The 2025 edition is revised as of **July 1, 2025** — it does not rule out an amendment published between then and now. No evidence of one was found for § 3.655 or § 3.350(i).

38 CFR § 4.14 (pyramiding), § 4.25 (combined ratings), and § 3.400 (effective dates) are cited elsewhere in this corpus but were not independently re-verified in this pass.
