# VA Claim Document Analysis: 100-PERCENT-SCHEDULAR-PATHWAY.md

**Source:** `va-disability/100-PERCENT-SCHEDULAR-PATHWAY.md` · **Classification:** strategy-synthesis doc (legal/regulatory research subtype — analysis, not evidence to be submitted to VA)
**Provenance:** not logged in `DOCUMENT-PROVENANCE.md` — gap (that log currently tracks only witness/personal statements; no row exists for any legal-research or strategy doc, including this one)
**Checked against:** `COMPREHENSIVE-FINDINGS-2026-07.md`

## Summary

This document is a self-contained legal/regulatory research memo: it states the verbatim 38 CFR 4.130 criteria for 70%/100% mental-disorder ratings, summarizes five controlling cases (Mauerhan, Vazquez-Claudio, Bankhead, Rice, Mittleider), explains how comorbid diagnoses and OCD specifically fold into one rating, works through 38 CFR 4.25 combined-ratings arithmetic in three worked scenarios, and closes with three previously-open regulatory questions (attorney fees, bilateral factor, one-year appeal deadline) now resolved. Its stated purpose is to be the legal substrate underneath `MASTER-STRATEGY.md` and `CLAIM-ASSESSMENT.md` — it is explicitly not itself evidence and is not filed with VA.

## Score: 7/10 (accuracy · completeness-for-purpose · consistency · credibility — NOT persuasiveness)

Driven primarily by **credibility-risk exposure from unverified citations**, not by any identified factual error or internal inconsistency. On completeness-for-purpose the document does what it says: states rule text, hedges practice-pattern claims explicitly as "evidentiary-tendency, not black-letter law" (§3), self-flags an unverified pin cite (Mittleider, §4), and its combined-ratings arithmetic in §7 checks out under the standard VA combining-by-remaining-efficiency method for all three scenarios (A→90%, B→~95%→100%, C→95%→100%). It is also internally consistent with how `MASTER-STRATEGY.md` §3 uses its §7 math verbatim. The score is capped below 8–9 because: (1) this document has apparently not yet been run through the repo's own mandated citation-verifier pass despite being marked "Status: complete," and (2) two of its five cited cases (Vazquez-Claudio, Bankhead) were cited for closely related propositions in this corpus's earlier `claim-maximization-research-2026-06.md` and flagged there as MISSTATED — meaning there is a documented history of exactly this failure mode recurring with exactly these cases in this corpus, and nothing here indicates that history was checked before restating them.

## Strengths

- Explicitly separates verified regulatory text from practice-pattern inference: §3's header states "This section is evidentiary-tendency, not black-letter law — there's no published numeric threshold; treat it as informed pattern-recognition, not a guarantee."
- Self-flags its own weakest citation rather than presenting it as settled: §4, "exact primary-opinion pin cite is UNVERIFIED here, but the holding is standard and reliable." (Mittleider v. West).
- Combined-ratings math in §7 is arithmetically sound under the standard VA combine-by-remaining-efficiency method (independently checked by this analyst as a mechanical computation, not a legal-citation question): Scenario A (70/50/20/10/10) computes to ~90.3%, rounding to 90% as stated; Scenario B (70/50/30/30/20/10/10) computes to ~95.2%, rounding to 100% as stated; Scenario C (90/50) computes to exactly 95%, rounding to 100% as stated.
- §6 ("Rice mechanics") is framed conservatively and doesn't encourage evidentiary manipulation — point 5 explicitly states "There is no verified authority letting a veteran bar VA from considering Rice-raised TDIU..." rather than asserting a workaround that doesn't exist, consistent with this corpus's credibility-first posture (`CLAIM-ASSESSMENT.md` §0.2).
- OCD diagnostic code (DC 9404) in §5 matches the independent confirmation in `COMPREHENSIVE-FINDINGS-2026-07.md` §9 item 10 ("100-PERCENT-SCHEDULAR-PATHWAY.md already had the correct code").

## Weaknesses

- Case-name spelling inconsistency across the corpus: this document spells the case "Vazquez-Claudio v. Shinseki" (§2, §5, Strategy synthesis §3), while `claim-maximization-research-2026-06.md` spells it "Vasquez-Claudio v. Shinseki" throughout (lines 1036, 48). Both cannot be correct for the same case — an internal-consistency defect across this corpus's own legal-research documents that should be resolved by the citation-verifier pass.
- §4's Mittleider discussion states the holding is "directly useful for the SUD theory" but doesn't distinguish (a) Mittleider's actual function — attributing otherwise-inseparable symptoms to a disability once it's already service-connected, for rating-severity purposes — from (b) whether SUD is service-connected at all (handled elsewhere via Allen v. Principi, not mentioned in this document). A reader relying on this document alone could conflate "helps the SUD theory" with "establishes the SUD theory."

## Gaps

- No explicit scope note bounding this document to _rating-level_ mechanics as distinct from _service-connection_ mechanics for the underlying diagnoses (ties to the Mittleider/Allen point above).
- No citation-verification ledger of its own, unlike `claim-maximization-research-2026-06.md`'s model (a confirmed/misstated/unverifiable table). Given this repo's own agent roster instruction (repo CLAUDE.md: "Run citation-verifier before finalizing any document here that cites law or regulation") and this document's "Status: complete" header, this appears to be an outstanding step, not a completed one.

## Credibility Risk Assessment

- **Documented recurrence risk, not a newly-found error:** Vazquez-Claudio v. Shinseki and Bankhead v. Shulkin are both restated here (§2) for propositions materially similar to how they were used in `claim-maximization-research-2026-06.md`'s "Mental Health Combined Rating — 70-100%" track — and both were independently flagged there as MISSTATED (case/reporter citation confirmed real, but the specific proposition attributed to the holding contained an overreach in each case; see that document's Citation Verification Ledger, lines 48–49). This document shows no evidence the propositions were re-derived from primary source rather than carried forward from that earlier, partially-misstated framing. This is the top item for citation-verifier to check — not because this document is presumptively wrong, but because this exact failure mode has already happened twice in this corpus with these exact two cases.
- **No coaching or persuasion-engineering language found.** Unlike the material described in `CLAIM-ASSESSMENT.md` §0.2 (the Erica email-chain coaching risk), this document doesn't instruct anyone to reframe facts, omit information, or match a target rating outcome — its Strategy synthesis argues for the accurate legal frame (total occupational AND social impairment), not a more favorable-sounding characterization of the facts.
- **Self-hedging reduces but doesn't eliminate risk.** The "not legal advice" banner and UNVERIFIED/evidentiary-tendency labels are good practice, but if synthesis sentences (§2, §6, "Strategy synthesis") get copied into a brief or letter without the hedge language attached, the underlying citation risk travels unlabeled.

## Citations Needing Verification

- 38 CFR 4.130, quoted verbatim in §1
- Mauerhan v. Principi, 16 Vet. App. 436 (2002) — §2
- Vazquez-Claudio v. Shinseki, 713 F.3d 112 (Fed. Cir. 2013) — §2 (note spelling variance above; note prior MISSTATED flag for a related use)
- Bankhead v. Shulkin, 29 Vet. App. 10 (2017) — §2 (prior MISSTATED flag for a related use)
- 38 CFR 4.14 (anti-pyramiding) — §4
- Mittleider v. West, 11 Vet. App. 181 (1998) — §4 (document itself flags pin cite as UNVERIFIED)
- M21-1, Part V, Subpart iii, Ch. 13 — §4
- DC 9404 (OCD) assignment under 38 CFR 4.130 — §5 (corroborated by cross-reference in `COMPREHENSIVE-FINDINGS-2026-07.md` but still needs its own formal pass)
- Rice v. Shinseki, 22 Vet. App. 447 (2009) — §6
- 38 CFR 4.25 (combined ratings) — §7 (arithmetic outcomes independently checked and consistent; the regulation text/method itself still needs verifier confirmation)
- 38 CFR 4.26 (bilateral factor) — §7, §8
- 38 CFR 14.636 (attorney/agent fees) — §8
- 38 CFR 3.2500 (one-year deadline / effective-date preservation) — §8

## Consistency Check vs. COMPREHENSIVE-FINDINGS

- **Confirms:** OCD rated under the same General Rating Formula (DC 9404) as PTSD/GAD/MDD — matches `COMPREHENSIVE-FINDINGS-2026-07.md` §9 item 10 and §3 exactly, including the DC 9403-vs-9404 resolution.
- **Confirms:** unemployment as legitimate "occupational impairment" evidence and Rice-raised TDIU as an acceptable fallback rather than something to suppress — this document §6 is the direct source `MASTER-STRATEGY.md` draws on, no divergence.
- **Confirms:** the combined-ratings framing that a 90% MH anchor + one 50% secondary (sleep apnea) is the efficient path to 100% combined — §7 Scenario C is cited near-verbatim in `MASTER-STRATEGY.md` §58.
- **Gap, not contradiction:** this document is silent on probability/likelihood entirely (pure legal mechanics), while `CLAIM-ASSESSMENT.md`/`MASTER-STRATEGY.md` carry the probability estimate (70% floor / 80–90% realistic / 100% a genuine stretch). Consistent with its stated scope — noting only that a reader relying on this document alone gets no sense of how likely 100% actually is, by design.
- No divergence found on any date, name, or diagnosis claim — this document makes no veteran-specific factual claims at all, so most cross-reference categories (dates, employment/financial facts, disclosure timing) don't apply to it.

## Notable Remarks

- This is the only document in the current working set that is pure legal/regulatory research with no veteran-specific facts — which is exactly why the citation-verification gap is the dominant issue rather than any factual/consistency defect.
- §8's bilateral-factor description ("combine the paired ratings normally, then add 10% of that combined value... A favorable-to-veteran exception exists") is more complete than §7's one-line mention — the two are consistent, not contradictory, but a reader skimming only §7 would get an incomplete picture of 4.26.

## Assumptions Made

- Classified this document as "strategy-synthesis doc" (closest fit among the five allowed categories) rather than inventing a sixth category for "legal/regulatory research memo."
- Treated the §7 arithmetic check as independently verifiable mechanical computation (within this analyst's scope), distinct from the case-law/CFR-text citations themselves, which were not judged and were routed to citation-verifier per the operating constraints.
- Surfaced the prior MISSTATED flags on Vazquez-Claudio/Bankhead as relevant context without concluding whether this document's restatement repeats the same overreach — that determination is left to citation-verifier.

## Open Questions for the User

- Has this document been run through citation-verifier since being marked "Status: complete" on 2026-07-05? No verification ledger or pass was found for it anywhere in the corpus.
- Which spelling of the Federal Circuit case is correct — "Vazquez-Claudio" (this document) or "Vasquez-Claudio" (`claim-maximization-research-2026-06.md`)? Resolve as part of the same citation-verifier pass.
- Should this document add an explicit scope note distinguishing rating-level mechanics from service-connection mechanics for SUD (handled elsewhere via Allen v. Principi) to prevent the Mittleider discussion in §4 from being read as broader than intended?

---

**CRITICAL flag: Yes** — no hard "must-see" credibility risk in the document's own content, but yes on unverified-citation need, including two cases with a documented prior MISSTATED history in this corpus.
