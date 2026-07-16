# Action Plan — Fix Corpus Inconsistencies (short form)

> Condensed action list from [`PLAN-CORPUS-CONSISTENCY-REMEDIATION-2026-07-09.md`](./PLAN-CORPUS-CONSISTENCY-REMEDIATION-2026-07-09.md) (full detail + sources there). · 2026-07-09
> **Two lanes, never mixed:** **Lane A** = corpus/analysis-doc edits the maintainer can do safely. **Lane B** = claim-facing/record items only the veteran + VSO + clinician can resolve — **flag only, never draft witness wording.**
> _Research assistance, not legal/medical advice — confirm with your VSO/attorney._

---

## LANE A — Maintainer fixes (safe; analysis docs only, no signed files)

- [ ] **A1 · WHODAS description** — replace "psychologist-signed / high-severity GAD-MDD / broken export" with "in-hand self-administered vendor instrument (~69.72%, self-care 62.5%)" in `MASTER-STRATEGY §1.10`, `NEXUS-LETTER-GUIDE-CHERIE §6`, `CLAIM-ASSESSMENT §0.2/#10`, `ACTION-CHECKLIST line 69`. _(Medium)_
- [ ] **A2 · Route 2 framing** — change "more reliable than Route 1" to "modestly higher if positive, inherits 90%-MH burden, not a safe fallback" in `PATH-TO-100 §1/§5/§9`, `CLAIM-COMPLETION-PLAN §3`, `CLAIM-MASTER-BRIEF §1`. _(Medium)_
- [ ] **A3 · Exam framing** — soften "single most outcome-determinative = examiner's selection" to the 4.126(a) whole-record posture in `CP-EXAM-PREP` header + `100-PERCENT-SCHEDULAR-PATHWAY §3`. _(Medium)_
- [ ] **A4 · Odds** — point `MASTER-STRATEGY` **and** `CLAIM-ASSESSMENT Part 2` ("80–90% / a stretch") at `PATH-TO-100 §9` as governing. _(Medium)_
- [ ] **A5 · Master §1 note** — annotate the "Route 1 ≈40–50%" line as refined by the Status-update (25–35% today / 45–50% if it lands). _(Low)_
- [ ] **A6 · Register count** — `MASTER-CLAIM-STRATEGY §5` header "24 issues / I-16…I-19" → "25 / I-16…I-20." _(Low)_
- [ ] **A8 · Citation labels** — flip _Nieves-Rodriguez_ to `[confirmed]` (verified 2026-07-09); one consistent label for _Rice_; reconcile the married-vet BVA balance to **3-adverse-vs-1** (non-representative sample) in `PATH-TO-100`. _(Low)_
- [ ] **B1-A (part of Critical B1) · Stop the overclaim** — in `PATH-TO-100 §I-4(d)`, `CLAIM-COMPLETION-PLAN Tier2#8`, `CLAIM-MASTER-BRIEF §5`, `VA-SUBMISSION-GUIDE §4`, `CP-EXAM-PREP`: downgrade "Dec-2024 job loss, Erica-attributed" to "record notes a _possible_ Dec-2024 layoff; Erica's statement doesn't describe one — include only if she genuinely recalls it."
- [ ] **Root-cause** — add one **canonical fact block** (claim dates, WHODAS, odds anchor, PTSD-dx status, Route-2 framing, BVA balance) to `COMPREHENSIVE-FINDINGS`; future docs cite it instead of re-stating.
- [ ] **Register the orphans** — carry **B2, B3a–d** from `COMPREHENSIVE §9a` into the `MASTER-CLAIM-STRATEGY` register as I-21…I-25 (so each has an owner).

## LANE B — Claim-facing reconciliations (veteran + VSO + clinician; flag-only, no coaching)

Ordered most-consequential first. Owner in **bold**.

- [ ] **B1 (Critical) · Dec-2024 job loss** — **VSO** confirms whether it actually occurred (record hints at a Starlite readmission); **Erica** includes it only if she genuinely recalls it, her own words. Do not present it as her attribution until then.
- [ ] **B5 / I-20 (High) · Marriage characterization** — the caretaker/roommate + ADL framing is in **no** signed doc; **veteran/Erica/Cherie** decide truthfully & consistently (no collision with blog draft / earlier statement).
- [ ] **I-8 (High) · Pre-service substance use** — **VSO** confirms how the "no pre-service use vs age-18 use" contradiction was resolved; **veteran** files a corrective supplemental statement (his own words, VSO/attorney review) with the "didn't recognize it as a disorder until treatment" nuance.
- [ ] **I-17 (High) · Two PsychEvals** — **veteran/Cherie/VSO** reconcile the 5/14 vs 5/15 reports (one attributes PTSD to "childhood trauma") before either is submitted.
- [ ] **B4 (Medium) · Cherie's letter IDs** — **veteran/Cherie** fix DOB (1998→1989), Kline/Klein, phone number; note SUD missing from the condition line.
- [ ] **B2 (Medium) · Ankle date** — **veteran/VSO** reconcile "May 2011" vs "2012" in the records.
- [ ] **B3a (Medium) · Reyes unit** — **VSO/Reyes** correct "4th Maintenance Sq" → "4th Equipment Maintenance Sq" (DD-214).
- [ ] **B3b (Medium) · Spouse surname** — **veteran** confirm legal name (Jure vs Klein) before Erica signs a 21-10210.
- [ ] **I-7 (Med) · SI-frequency** / **I-9 (Med) · MST non-disclosure** / **I-10 (Med) · Poquette timing** — **veteran/witnesses** address in their own words; **VSO** confirms records.
- [ ] **B3c/B3d (Low)** — Harmony 24-vs-25 days; CPT age 22-vs-23 — correct if convenient.

## Verify when done

Re-run `claim-consistency-checker`; confirm no signed/claim-facing file was edited; PHI gate before commit.
