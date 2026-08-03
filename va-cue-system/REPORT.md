# VA Effective-Date & CUE Engine — Primary Synthesis

> Status: research complete (2 deep-research passes) · Started: 2026-07-16 · Last updated: 2026-07-16
>
> **What this is:** an evidence-based feasibility, technical-strategy, marketability, and
> revenue assessment of a proposed **RAG/agentic "Effective-Date & CUE Engine"** — a tool
> sold to **VA-accredited claims agents and attorneys** that ingests a veteran's C-file,
> reconstructs a date-stamped timeline of prior final VA decisions and the law in effect at
> each, tests each for **Clear and Unmistakable Error (CUE)** under 38 C.F.R. § 3.105(a),
> argues the earliest possible effective date, and drafts citation-ready instruments.
>
> **How it was produced:** two `/deep-research` passes (217 agents total). Full detail and
> per-claim ledgers live in the appendix files; this document is the integrated synthesis.
>
> - **Pass 1 — feasibility/strategy/market/revenue:** `deep-research-findings-2026-07-16.md`
>   (reconstructed from the agent journal because the workflow's auto-synthesis step failed).
> - **Pass 2 — wedge & moat verification:** `deep-research-wedge-moat-2026-07-16.md`
>   (clean synthesis; 25/25 verified claims confirmed, 0 refuted).
> - Source spec: `va-cue-rag-kb-system.md`. Research prompt: `va-cue-deep-research-prompt.md`.

---

## Bottom line

**The two hardest questions resolved in the concept's favor — the wedge is real and the moat is grounded in a genuine legal requirement — but with two caveats that keep it short of "validated," and a revenue ceiling that is small.**

- **Feasibility: buildable, no blockers** — every component is Feasible or Feasible-with-significant-effort. The binding constraints are C-file ingestion (bulk export + OCR, _not_ an API) and legal-RAG hallucination (~17–33% for leading tools → mandatory human-in-the-loop).
- **The wedge is CONFIRMED for every competitor checked (4 of them), not just asserted** — but only 4 tools were deep-verified, so it is not a _global_ fact. The closest competitor (VCH) is moving fast into effective-date _extraction_, so the window is narrowing.
- **The moat is GENUINE but narrow:** point-in-time regulation ≥2017 is a _free government commodity_ (no moat); the defensible asset is the **pre-1997 day-accurate corpus**, which rests on a real, black-letter CUE requirement to apply "the law that existed when that decision was made." Whether a legal-data vendor already sells this is the one decisive question still open.
- **Revenue is modest and structurally fragile:** with a verified fee-eligible TAM of only **~6,720 professionals**, the realistic base case is **~$1.0–1.3M ARR by Year 3** (a *good* outcome, not a floor); worst case is a sub-$100K stall.

**Single biggest risk:** an incumbent bolts a CUE/effective-date reasoning layer onto an existing C-file timeline product (VCH already builds the timeline; the regulation corpus is free), collapsing the wedge before the founder scales.
**Single biggest unknown:** whether the fee-charging buyer (agents/attorneys) can get _frictionless_ C-file ingestion — access is real but read-only, per-POA, suitability-gated, bulk-PDF-export, and the fast "access within minutes" portal flow was **not yet open to agents/attorneys** (only VSO reps) at the mid-2026 snapshot.

---

## 1. Technical feasibility

| Component                                           | Verdict                                                         | Binding constraint                                                                                                                                                          |
| --------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (a) Point-in-time 38 C.F.R. corpus **[the "moat"]** | Feasible now ≥2017; **Feasible w/ significant effort** pre-1997 | Free eCFR (day-level ≥Jan 2017) + GovInfo (annual ≥1997) solve the easy part; the defensible slice is pre-1997 exact-effective-date reconstruction + pre-1996 OCR/licensing |
| (b) C-file ingestion (VBMS / eFolder Express)       | **Feasible w/ significant effort**                              | No public API; ingestion = accredited user's own read-only per-POA session → bulk PDF/TIFF/IMG export → OCR. Fast portal onboarding not yet open to agents/attorneys        |
| (c) Timeline + CUE reasoning                        | **Feasible w/ significant effort**                              | Legal-RAG hallucination ~17–33% (Stanford); the "record + law as it existed at the time" constraint is unforgiving → mandatory human-in-the-loop; no autonomous filing      |
| (d) BVA / CAVC / Fed-Cir corpora                    | **Unverified (uncovered)**                                      | Availability/quality of bulk decision corpora was never fetched — open question                                                                                             |
| (e) Security / PII-PHI compliance                   | **Feasible w/ significant effort**                              | Privacy Act + §§ 5701/7332 + suitability gate; vendor **cannot** hold system access — processes only files the user lawfully pulled                                         |

**On the moat specifically (integrating both passes):** The claim that versioned point-in-time 38 C.F.R. is the "hardest, most defensible" asset is **half right**. For decisions **≥ 2017** it is a free government API (eCFR versioner, day-level, live endpoint verified 2016-12-14→2026-01-26) — _not_ defensible. But CUE is legally required to apply the regulation **as it read on the prior decision date** (38 C.F.R. § 3.105(a)(1)(iii); _Russell v. Principi_, 3 Vet. App. 310 (1992); M21-1), and § 3.105 alone was amended **~10× between 1961 and 2019** — so high-value CUE work (backpay runs to the original decision date) routinely needs 1980s–1990s text. GovInfo's machine-readable CFR XML only reaches **1997**; pre-1997 requires OCR of print editions reconciled to Federal Register effective dates. **That pre-1997 gap-fill is the genuine, defensible dataset** — narrower and less glamorous than "we built the versioned corpus," but real.

> **Correction carried forward:** point-in-time granularity is **day-level** (by Federal Register effective date), **not** annual "July-1 snapshots" (that claim was refuted 0-3). Annual snapshots are _affirmatively inadequate_ for CUE — a decision dated March 15 needs the text in force March 15.

---

## 2. Technical strategy & rough roadmap

**Reference architecture:** accredited user's own session → eFolder Express bulk export (.zip) → OCR + document typing → **evidentiary timeline graph** ("what VA knew, and when") → **point-in-time law retrieval** (eCFR versioner ≥2017; GovInfo annual + Federal Register effective-date reconciliation 1997–2016; OCR/licensed pre-1997) → **CUE-viability reasoning** (§ 3.105(a) + § 20.1403 three-part test) → citation-grounded drafting → **mandatory human review gate**.

**Build-vs-buy:** ingest the regulation corpus **free** (don't treat ≥2017 as the moat); **build** the OCR/structuring pipeline (no API to buy) and concentrate IP in the **pre-1997 effective-date dataset + the evidentiary graph**; treat LLM/OCR/vector-graph stores as commodity, chosen for auditability.

**MVP (smallest version that proves the moat):** **F1 timeline** + **F2 CUE-viability triage** + **F3 point-in-time regulation**, run on ≥2017 decisions first (corpus is free and clean), with a hard human-review gate.

**Roadmap:** MVP (prove timeline+triage saves specialist-firm hours) → parity (pre-1997 day-accurate corpus = the real IP; add BVA/CAVC/Fed-Cir RAG + drafting) → platform (firm/multi-seat, workflow integration).

**Top risks → mitigations:** hallucinated authorities → citation-grounding + attorney sign-off + no autonomous filing; moat-is-commodity → concentrate IP in pre-1997 dataset + graph; ingestion friction → design around bulk export + OCR; incumbent fast-follow → lead with accreditation-credibility and depth, plus a **corpus-hygiene** discipline (e.g., the research caught that the 2007 Part 3→Part 5 rewrite, E7-9542, was a _proposed rule that never became law_ — an engine that ingested it would apply text never in force).

---

## 3. Marketability

**Wedge — CONFIRMED for the four tools deep-verified, not proven globally.** None of **VCH, Vala, VeteranAi, or Dodonai** performs effective-date reconstruction, CUE analysis, or point-in-time law:

- **VCH** (professional-only): C-file AI analysis, 20+ auto-forms, 365-day appeal-_deadline_ tracker. **The near-miss:** its Jan–Mar 2026 releases build a chronological claims timeline that _extracts_ effective dates and answer Q&A like _"what's the earliest effective date for this PTSD claim?"_ — but that is **extraction + citation**, not arguing the earliest date or attacking a final decision (CUE is _functionally opposite_ — it attacks already-final decisions). VCH is **one reasoning-layer away.**
- **Vala** (professional): evidence-surfacing + auto-forms; no eff-date/CUE _as advertised_ (landing page, not a full feature list).
- **VeteranAi** (veteran self-service, $25/mo; also sells County-VSO seat licenses): prospective condition-spotting only.
- **Dodonai** (cross-domain SSDI/LTD/VA): medical-chronology/records-org; VA is only a submission destination.

**Not yet checked → the live risk to the thesis:** Caliber/Flagship, claim.vet (deep), ClaimClam, VetClaims.ai, Vetlex, RepScout — and any **legal-AI incumbent VA vertical** (Harvey/CoCounsel/Legora/Clearbrief/EvenUp). "No competitor does CUE" is confirmed for the verified set, **not** a settled global fact.

**Pain & willingness to pay:** CUE/earliest-effective-date work is delivered today as bespoke specialist-attorney labor, manual and high-dollar (a CUE win runs backpay to the original claim date). Adjacent tool prices: VCH ~$33–150/mo, claim.vet ~$49/mo. Proposed $150–400/seat + credits sits above the VA-tool band, far below horizontal legal-AI.

**Buyer & channels:** fee-eligible population **~6,720** (6,200 attorneys + 520 agents, RIN 2900-AR94, Oct 2024; older 2020 CRS ~8,080 + 525; full OGC roster ~18,310 incl. **9,705 non-fee VSO reps**). **~27,250 fee agreements filed/yr.** **NOVA** is the reachable channel (~850 members, dues ~$460/yr, two ~15-CLE-hour conferences/yr). Frictions: AI-hallucination skepticism, malpractice/ethics anxiety, firm security review, OCR-pipeline burden, and the "not representation itself" marketing line (§ 5904 / § 14.636).

**Competitive durability:** horizontal incumbents are structurally aimed at BigLaw and priced out of this niche (Harvey ~$1,200/seat/mo, 20–25 seat min, ~$288–360K/yr floor; CoCounsel ~$225–400/user/mo; none markets a VA vertical). But durability from below is **thin**: the regulation corpus is free, VCH already builds the timeline, and the CUE reasoning layer is the only real differentiator — replicable in a quarter or two. The defensible moats are (weakly) the **pre-1997 effective-date dataset** and (more durably) **accreditation-credibility + specialist trust** — not the technology.

---

## 4. Revenue — five scenarios _(founder-facing modeling on verified inputs; not itself a web-verified finding)_

Verified inputs: TAM **~6,720**; fee pool **$410.8M trailing-12-mo / $34.2M-mo** (VBA, 2026-07-06 — *corrected up from the spec's $396.8M*); ~27,250 fee agreements/yr; NOVA ~850 engaged; proposed $150–400/seat + credits. The spec's linear "5–15% → $1–3M ARR" is rejected: it treats penetration as instantaneous and frictionless, ignores that ~15% of 6,720 is only ~1,000 seats, and assumes flat ACV, zero churn, zero CAC, no ramp.

| Scenario             | Paying accts (Yr3)             | Blended ACV | Yr3 ARR           | Key assumptions                                                                            |
| -------------------- | ------------------------------ | ----------- | ----------------- | ------------------------------------------------------------------------------------------ |
| **Worst**            | ~20–40 (stall)                 | ~$3,000     | ~$60K (declining) | Wedge neutralized (VCH ships CUE) or ingestion impractical; 40%+ churn                     |
| **Conservative**     | ~120 (~1.8%)                   | ~$3,500     | ~$380K            | Slow solo adoption, 25–30% churn, long cycles, high CAC                                    |
| **Realistic (base)** | ~250–300 (~4%)                 | ~$4,500     | **~$1.0–1.3M**    | Wedge holds 2–3 yrs; ~20% churn; credits +30%; 3–5 small-firm deals                        |
| **Optimistic**       | ~350 accts / ~500 seats        | ~$5,500     | **~$2.5–2.8M**    | Frictionless ingestion, ~12% churn, NOVA converts, firm site licenses                      |
| **Aggressive**       | ~1,000 seats (~15% + VSO orgs) | ~$6,000     | **~$4.5–5M**      | _All_ must hold: frictionless ingestion, wedge stays open, firm + VSO-org deals, low churn |

**Sensitivity — what swings it:** (1) **firm/multi-seat site licenses** (the Conservative↔Realistic difference); (2) **churn** — at a 6,720 TAM there's no top-of-funnel to replace leaked accounts, so 30% vs 15% compounds brutally; (3) **ingestion friction** — if bulk-export+OCR onboarding is painful (and the fast portal stays closed to agents/attorneys), penetration and retention both collapse. **The $410.8M fee pool is veterans' money, not the vendor's market** — serviceable revenue is bounded by ~6,720 seats.

---

## 5. Verification highlights

Across both passes, **50 load-bearing claims** were adversarially verified (3 votes each). Full ledgers are in the two appendix files. Carry these forward:

**Corrections to the spec:**

- Fee pool is **$410.8M / $34.2M-mo (2026-07-06)**, not $396.8M — and it does **not** come from RIN 2900-AR94 (that RIN is the accreditation/CLE rule; it _does_ carry the ~6,720 population).
- Point-in-time granularity is **day-level**, not annual July-1 snapshots.
- **eFolder Express** (the Caseflow product) **is** the external accredited-rep access channel — the "VA-internal only" framing was wrong.
- **Correction to an earlier false alarm (resolved by `citation-verifier`):** _Chisholm v. Collins_ and _Hamill v. Collins_ — which the deep-research passes could not find and I flagged as possible fabrications — are **both real and correctly characterized in the spec** (as recent _effective-date_ decisions, not CUE cases): _Chisholm v. Collins_, **38 Vet. App. 140 (2025)** (CAVC — TDIU-form claim-preservation, § 3.2501) and _Hamill v. Collins_, **No. 24-1543 (Fed. Cir. Feb. 4, 2026)** (implicit-denial doctrine eliminated for AMA-era claims). The passes' failure to surface them was a search-recency gap (Hamill post-dates the Jan-2026 knowledge cutoff), not a citation error. The three-part CUE _test_ separately traces to _Russell v. Principi_, 3 Vet. App. 310 (1992) and _Fugo v. Brown_, 6 Vet. App. 40 (1993) — both confirmed.
- **Nehmer ≠ CUE** — § 3.816 is a district-court consent-decree Agent-Orange effective-date rule, a distinct mechanism the engine must not conflate with CUE.

**Confirmed as stated:** the ~6,720 population; the read-only, per-POA data-access regime (§§ 1.600–1.603, eff. 2022-07-25); the CUE regs (§ 3.105(a), § 20.1403) and the retroactive-effect mechanism; § 14.636 fee cap; free eCFR versioner + GovInfo bulk XML; and the wedge status of all four verified competitors.

---

## 6. Open items — what stands between "promising" and "validated"

Ranked by how load-bearing they are:

1. **Is the pre-2017 point-in-time CFR moat already a commercial product?** (HeinOnline / Westlaw / LexisNexis / vLex historical point-in-time retrieval + startup licensing cost.) **Decisive for the moat** — never resolved.
2. **Do the uncovered competitors or a legal-AI VA vertical already do effective-date/CUE?** Caliber, claim.vet, ClaimClam, VetClaims.ai, Vetlex, RepScout, and Harvey/CoCounsel/etc. The legal-AI fast-follow is the most credible well-capitalized threat.
3. **Real pre-1997 build cost** — OCR/scan of 1980s–1990s 38 C.F.R./38 U.S.C. reconciled to Federal Register effective dates. This is the actual differentiator work; unestimated.
4. **Ingestion friction for the fee-charging buyer** — confirm eFolder Express is bulk-`.zip`-only (no API), and whether the fast Accredited-Rep-Portal flow has opened to agents/attorneys since mid-2026.
5. **BVA/CAVC/Fed-Cir bulk corpora** availability/quality (never fetched).
6. **§ 14.632(c)(5) — MISSTATED in the spec (resolved by `citation-verifier`).** The subsection exists but is a **general "clearly unreasonable or otherwise prohibited" fee rule binding the accredited representative** — NOT a categorical ban on a vendor success/referral fee. The "no success fee" pricing conclusion should rest on **§ 14.636**'s reasonableness/20% regime + the accreditation fee-sharing framework, citing (c)(5) only as the general unreasonable-fee backstop. _(Correct in the spec at lines 96/104, the prompt, and anywhere it's framed as a categorical prohibition.)_
7. **Security architecture** — verified only as a regulatory boundary, not a design that passes a firm's + VA's review.

**Currency:** all competitor/pricing/portal/fee-pool figures are mid-2026 snapshots — re-verify before any launch decision; the wedge is narrowing fastest at VCH.

---

## Sources

Full cited source lists are in the two appendix files (`deep-research-findings-2026-07-16.md` §8 and `deep-research-wedge-moat-2026-07-16.md`). Key primary anchors: eCFR versioner API + point-in-time system; GovInfo CFR bulk data; Federal Register 2022-13312 (data-access rule) and 2024-23610 / RIN 2900-AR94 (population); VBA attorney-fee report; 38 C.F.R. §§ 3.105, 20.1403, 3.816, 1.600–1.603, 14.636; M21-1 Part X (CUE); competitor product pages (vaclaimhelper.com, valaclaims.com, veteranai.co, dodon.ai).

_Research assistance, not legal advice. Regulatory/fee-model interpretation should be confirmed with counsel before go-to-market._
