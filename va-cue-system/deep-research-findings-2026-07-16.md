# Effective-Date & CUE Engine — Feasibility, Strategy, Market & Revenue Assessment

**Date:** 2026-07-16
**Subject:** A RAG/agentic "Effective-Date & CUE Engine" sold to VA-accredited claims agents and attorneys — ingests a veteran's C-file, reconstructs a date-stamped decision timeline with the law in effect at each point, tests each prior final decision for Clear and Unmistakable Error (CUE) under 38 C.F.R. § 3.105(a), argues the earliest possible effective date, and drafts citation-ready instruments.

> **⚠️ RECONSTRUCTION NOTICE.** This report was **reconstructed from the raw per-agent outputs** of a deep-research workflow (111 agents: 6 search angles → 28 sources fetched → 116 claims extracted → 25 adversarially verified, 23 confirmed / 2 refuted). The workflow's automated **final-synthesis step failed** and returned a degenerate stub (a single placeholder finding, "Test summary to isolate schema validation"). The underlying research is intact; this document re-synthesizes it by hand from the journal and workflow logs. Every factual claim below is traceable to a source the agents actually fetched. **Section 5 (Revenue) is explicitly founder-facing modeling built on the verified inputs — it is not itself a web-verified finding.**

---

## 1. Executive Summary

**Bottom line: the thesis is more right than wrong on the market wedge and the legal doctrine, but the "point-in-time regulatory corpus" moat is materially weaker than claimed, and the revenue ceiling is small. Lead with the moat problem, not the wedge win.**

**1. Technical feasibility — Feasible, but the flagship "moat" is half-commodity and depth-limited.** Every component is buildable, but the single asset the founder calls the hardest and most defensible — versioned point-in-time 38 C.F.R. — **already exists as a free government service back to ~January 2017** (eCFR point-in-time system + versioner API) and, at annual granularity, back to ~1996/1997 (GovInfo bulk CFR XML). The genuinely hard, unsolved part is pre-2017 _day-accurate_ regulation for decades-old decisions, which requires stitching GovInfo annual editions to Federal Register effective dates (and licensing/OCR of pre-1996 text). C-file ingestion is a **semi-automated bulk-PDF-export + OCR pipeline, not a live API**. CUE reasoning is feasible but carries an unsolved hallucination-rate problem (Stanford: leading legal-RAG tools hallucinate ~17–33%).

**2. Technical strategy — A defensible MVP is the _timeline + CUE-viability triage_, not the regulation corpus.** The corpus is table stakes an incumbent can replicate; the durable value is the evidentiary "what VA knew and when" graph plus disciplined, citation-grounded CUE triage with a human-in-the-loop gate. Build on the free eCFR/GovInfo corpora; spend the engineering budget on the pre-2017 gap-fill and the timeline graph.

**3. Marketability — The wedge is real but only _partially_ tested.** Of the named competitors, **only two (Vala, VCH) were deeply verified**; both stop at C-file summarization / condition-spotting / form-filling (VCH adds a 365-day appeal-_deadline_ tracker — forward-looking, not backward effective-date/CUE). That confirms the wedge is _unoccupied by the two tools checked_, not that "no competitor does CUE" globally. Notably, VCH's Jan-2026 "C-File AI Analysis" already builds a **chronological claims timeline that extracts existing effective dates** — closer to the wedge than the spec implies. Demand is real (CUE/earliest-effective-date work is high-dollar and done manually by specialist firms today), but the buyer pool is tiny and trust/ethics/security friction is high.

**4. Revenue — The spec's linear "5–15% → $1–3M ARR" is optimistic and structurally fragile.** With a verified fee-eligible TAM of only **~6,720 professionals**, a realistic base case lands near **$1.0–1.3M ARR by Year 3**, not as a floor but as a _good_ outcome, and only if firm/multi-seat deals land. Worst case is a sub-$100K stall.

**Single biggest risk:** the moat is not a moat — an incumbent (a VA tool like VCH/Vala, or a horizontal like Harvey/CoCounsel) bolts CUE/effective-date reasoning onto an existing C-file timeline product, since the regulation corpus is free and the timeline is already being built by VCH.

**Single biggest unknown:** whether fee-charging agents/attorneys can achieve _frictionless, near-automated_ C-file ingestion. Access is real but **read-only, per-POA, suitability-gated, and delivered as bulk PDF export** — and the fast "access within minutes" Accredited Representative Portal flow is **not yet available to the exact fee-charging buyer segment** (agents/attorneys), only VSO reps, as of the mid-2026 snapshot.

---

## 2. Technical Feasibility

| Component                                         | Verdict                                                                                | Binding constraint                                                                                                                                                               | Confidence                                                            |
| ------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| (a) Point-in-time 38 C.F.R. corpus **[THE MOAT]** | **Feasible now for ≥2017; Feasible-with-significant-effort for pre-2017 day-accuracy** | Free eCFR/GovInfo already solve ≥2017 (day-level) and ≥1996 (annual); the moat reduces to the pre-2017 exact-effective-date gap-fill + pre-1996 licensing/OCR                    | High                                                                  |
| (b) C-file ingestion (VBMS / eFolder Express)     | **Feasible with significant effort**                                                   | No public/OAuth API; ingestion = accredited user's own read-only, per-POA session → bulk PDF/TIFF/IMG export → OCR. Fast-onboarding portal flow not yet open to agents/attorneys | High                                                                  |
| (c) Timeline reconstruction + CUE reasoning       | **Feasible with significant effort**                                                   | Legal-RAG hallucination ~17–33% (Stanford); CUE's "record + law as it existed at the time" constraint is unforgiving; requires human-in-the-loop                                 | Medium-High                                                           |
| (d) Legal corpora (BVA / CAVC / Fed Cir)          | **Not directly verified by this research**                                             | Availability/quality of bulk decision corpora was not fetched; only the CFR/USC and Nehmer case line were checked                                                                | Low (uncovered)                                                       |
| (e) Security/compliance for C-file PII/PHI        | **Feasible with significant effort**                                                   | Privacy Act + §§5701/7332 + suitability/PIV gate; vendor **cannot** hold system-level access — must process only files the accredited user lawfully pulled                       | Medium (regulatory boundary verified; architecture not stress-tested) |

### (a) The point-in-time regulatory corpus — the moat is thinner than claimed

The claim that versioned, effective-date-keyed 38 C.F.R. is the "hardest and most defensible" asset does not survive contact with the primary sources:

- **eCFR's native point-in-time system already lets you view any section as it read on a past date — but only back to January 2017.** This is "the single most important constraint for CUE analysis, which requires the regulation as it read on decision dates that are often decades old." It shows the capability "partly already exists (undercutting defensibility) yet is depth-limited." (search finding, https://www.ecfr.gov/reader-aids/using-ecfr/ecfr-changes-through-time)
- **The eCFR versioner API exposes historical versioned amendments of Title 38 in machine-ingestible JSON**, each record carrying `date` (version), `amendment_date`, and `issue_date` fields — verified against the **live endpoint** `https://www.ecfr.gov/api/versioner/v1/versions/title-38.json`, observed date range **2016-12-14 to 2026-01-26**. Point-in-time full text is served as XML via `/full/{date}/title-38.xml`. (CONFIRMED 3-0; https://www.ecfr.gov/developers/documentation/api/v1)
- **GovInfo bridges the pre-2017 gap at annual granularity:** CFR annual editions in bulk XML extend back to **1996 (some titles) / 1997 (all titles)**, one snapshot per year per title, via Data.gov and GPO's Bulk Data Repository. (CONFIRMED 3-0; https://www.govinfo.gov/help/cfr, https://www.govinfo.gov/bulkdata/CFR)
- **e-CFR bulk XML (the continuously-updated product) only starts 2015**, and the GPO/FDsys bulk repository hosts **only the most recent** e-CFR data — historical point-in-time editions live at ecfr.gov, not the bulk repo. (CONFIRMED; https://github.com/usgpo/bulk-data/blob/main/ECFR-XML-User-Guide.md)
- **Pre-1996 digital CFR is not free** — GovInfo names HeinOnline (1938–present) as the paid source; older editions otherwise require Federal Depository Library access. (https://www.govinfo.gov/help/cfr)
- Bulk XML **is not the official legal format** — only PDF/text on GovInfo carry legal status — so the engine can ingest structure cheaply but must _cite_ the authoritative version. (https://github.com/usgpo/bulk-data/blob/main/ECFR-XML-User-Guide.md)

**What this means for the moat.** For decisions from 2017 onward, "point-in-time regulation" is a commodity government API — not defensible. For older decisions (where the highest-value CUE claims live, since backpay runs to the original claim date), the real, unglamorous work is: (1) reconstructing exact-effective-date text pre-2017 by reconciling GovInfo _annual_ editions against **Federal Register final rules** (which "contain amendatory instructions, the text of amendments, the effective dates, and the Federal Register date and page citation"), and (2) licensing or OCR'ing pre-1996 text. That gap-fill _is_ a defensible dataset — but it is a narrower, harder, and less glamorous asset than "we built the versioned corpus."

> **Critical correction (see Verification Ledger):** The spec-adjacent claim that Title 38's July-1 annual revision "sets the effective-date granularity of any point-in-time 38 C.F.R. corpus to annual (July 1) snapshots" was **REFUTED 0-3.** The July-1 cadence applies only to the _printed/bound annual edition_. Real point-in-time granularity is **day-level**, keyed to each amendment's actual Federal Register effective date. For CUE work this matters: a decision dated March 15 needs the text in force March 15, which can differ from both surrounding July-1 editions if a mid-year amendment intervened. **Annual snapshots are affirmatively inadequate for CUE.**

### (b) C-file ingestion — bulk export, not an API

- Access to VBMS + Caseflow (Queue, eFolder Express) is **read-only and per-POA** under 38 C.F.R. §§ 1.600–1.603 (final rule effective **July 25, 2022**). Users "will not be permitted to modify the data" (may only upload new documents), and access is limited to claimants who appointed them, authorized by a POA under § 14.631. (CONFIRMED 3-0; https://www.federalregister.gov/documents/2022/06/24/2022-13312/..., https://www.ecfr.gov/current/title-38/chapter-I/part-1/subject-group-ECFRae92831392dc7e6)
- **eFolder Express is the sanctioned bulk-download channel:** one-click download of _all_ of a veteran's files, chronological by receipt date, sourced from VBMS + Virtual VA; up to 64 eFolders can be compiled simultaneously; downloads stay in history 72 hours; files arrive as **mixed PDF/TIFF/IMG** requiring OCR/normalization. The Caseflow docs "do not document any programmatic API for third-party ingestion." (CONFIRMED 3-0; https://department-of-veterans-affairs.github.io/caseflow/task_trees/data-model/efolder_express.html)
- **Realistic ingestion path = downloaded ZIP/PDF corpus + OCR, not a live integration.** A vendor cannot hold system-level access; it can only process files the accredited user lawfully pulled through their own credentialed session.
- **Onboarding-speed caveat:** the Accredited Representative Portal's "eFolder access within minutes" (via the online 21-22 acceptance flow) is real for **VSO reps** but, per VA.gov, the Representation Requests feature **is currently not available to claims agents or attorneys** — the exact fee-charging buyers. They still rely on the slower legacy POA + VBMS/eFolder Express path. _(This VA.gov page returned no extractable claims to the fetcher and should be re-verified before launch.)_

> **Correction (see Ledger):** The characterization of eFolder Express as a **VA-internal-only** tool was **REFUTED 1-2.** The GitHub repo (`department-of-veterans-affairs/efolder-express`, a Python/Twisted tool requiring `connect_vbms`, archived read-only Aug 18 2023) _is_ internal and its README lists FOIA processors/OGC attorneys/contract examiners. **But** the _Caseflow product_ named "eFolder Express" in 38 C.F.R. §§ 1.600–1.603 is precisely the channel through which **external accredited attorneys/agents** get bulk eFolder access. The "internal-only, not for external reps" exclusion is **factually wrong** and would have undermined the data-access assumption in the wrong direction. Ingestion via eFolder Express by the target buyer is _permitted_; it is just manual/bulk, not API-driven.

### (c) Timeline reconstruction & CUE reasoning

The legal scaffolding is confirmed and stated correctly:

- **38 C.F.R. § 3.105(a):** a decision may be revised "at any time after [it] is final" on CUE; a CUE reversal "has the same effect as if the corrected decision had been made on the date of the reversed decision" — the retroactive effective-date hook the product depends on. (CONFIRMED; https://www.ecfr.gov/current/title-38/chapter-I/part-3/subpart-A/subject-group-ECFR63da83ba671b92b/section-3.105)
- **38 C.F.R. § 20.1403:** CUE review "must be based on the record and the law that existed when that decision was made" — the point-in-time-law constraint — and explicitly _excludes_ changed diagnoses, duty-to-assist failures, disagreements over how facts were weighed, and later changes in interpretation. Rule history: 57 FR 4109 (1992), amended 84 FR 192 (2019). (CONFIRMED; https://www.ecfr.gov/current/title-38/chapter-I/part-20/subpart-O/section-20.1403)
- **Doctrinal note (updated by `citation-verifier` 2026-07-16):** the three-part CUE test originates in _Russell v. Principi_, 3 Vet. App. 310 (1992) and _Fugo v. Brown_, 6 Vet. App. 40 (1993) — both confirmed. The spec's _Chisholm v. Collins_, 38 Vet. App. 140 (2025) and _Hamill v. Collins_, No. 24-1543 (Fed. Cir. Feb. 4, 2026) are **confirmed REAL effective-date decisions** (the spec never called them CUE cases). This pass failed to surface them due to search recency (Hamill post-dates the cutoff), not because they were fabricated — earlier "did not surface" language here was a false alarm.
- **Nehmer is a distinct mechanism, not CUE.** 38 C.F.R. § 3.816 implements _Nehmer v. United States Dept. of Veterans Affairs_, No. CV-86-6160 TEH (N.D. Cal.) — a district-court class-action consent-decree line (9th Cir. affirmance July 19, 2007), **not** a CAVC precedent. It sets a special Agent Orange retroactive effective-date rule (later of claim date or date disability arose). Any engine must not conflate Nehmer with CUE. (CONFIRMED; https://www.ecfr.gov/current/title-38/chapter-I/part-3/subpart-A/subject-group-ECFR2c3eca6251aa67b/section-3.816, https://caselaw.findlaw.com/court/us-9th-circuit/1219226.html)

**Reliability is the hard constraint.** A documented April-2026 case had Harvey produce a _fully fabricated_ LexisNexis citation; a Stanford study found leading legal-RAG tools hallucinate **~17–33%** of the time; even CoCounsel "still makes up citations and runs thin on appellate material." "No fabricated authorities" is a hard, _unsolved_ constraint even for well-funded incumbents — so the product must be architected as decision-support with mandatory attorney verification, not autonomous drafting. (https://www.aiforlegalresearch.com/tools/harvey-ai, https://www.vaquill.ai/blog/harvey-legora-cocounsel-pricing-reality)

### (d) Legal corpora & (e) security

Bulk BVA/CAVC/Fed-Cir decision corpora were **not fetched** by this research — treat availability/quality as an open question. On security: the regulatory boundary is verified (read-only, per-POA, suitability/PIV gate, vendor cannot hold system access), but a concrete PII/PHI architecture (Privacy Act, 38 U.S.C. §§ 5701/7332, HIPAA-adjacent) was not designed or stress-tested here.

---

## 3. Technical Strategy & Rough Roadmap

**Reference architecture (grounded in the feasibility findings):**

```
Accredited user's own session → eFolder Express bulk export (PDF/TIFF/IMG .zip)
   → OCR + document typing/normalization
   → Evidentiary timeline graph ("what VA knew, and when": each prior final decision, evidence of record at that point)
   → Point-in-time law retrieval (eCFR versioner ≥2017 day-level; GovInfo annual 1996–2016 reconciled to Federal Register effective dates; licensed/OCR pre-1996)
   → CUE-viability reasoning (§3.105(a) + §20.1403 three-part test; record-and-law-at-the-time constraints)
   → Citation-grounded drafting (Supplemental Claim / HLR / Board appeal / CUE motion)
   → Mandatory human-in-the-loop review gate
```

**Build-vs-buy:**

- **Regulation corpus: BUY/INGEST FREE.** Use eCFR versioner API (≥2017) + GovInfo bulk CFR XML (≥1996). Do **not** treat this as the moat. Spend engineering on the **pre-2017 effective-date reconciliation** and pre-1996 acquisition — the only genuinely defensible slice.
- **C-file ingestion: BUILD** a robust OCR/structuring pipeline for 1,000–2,000-page mixed-quality bundles; there is no API to buy.
- **LLM/OCR/vector+graph stores:** commodity; select for auditability and citation-grounding, not raw capability.

**MVP (smallest defensible version that proves value):**

- **F1 — Timeline:** reconstruct the date-stamped decision/evidence timeline from a C-file export. (This is the durable core; note VCH already does a version of this.)
- **F2 — CUE-viability triage:** flag which prior final decisions are _plausible_ CUE candidates under the three-part test, with the "record + law at the time" constraints enforced — triage, not autonomous adjudication.
- **F3 — Point-in-time regulation:** attach the regulation as it read on each decision date, day-accurate where the Federal Register supports it.

**Phased roadmap:**

1. **MVP → prove the moat:** F1+F2+F3 on ≥2017 decisions (where the corpus is free and clean), with a hard human-review gate. Prove the timeline+triage saves specialist-firm hours.
2. **Parity → close the gap:** pre-2017 day-accurate corpus (the real IP), plus BVA/CAVC/Fed-Cir RAG for argument support, plus drafting.
3. **Platform:** firm/team standardization, multi-seat, workflow integration.

**Top risks → mitigations:** (1) _Hallucinated authorities_ → citation-grounding to the authoritative PDF/text + mandatory attorney sign-off + no autonomous filing. (2) _Moat is commodity_ → concentrate IP in the pre-2017 effective-date dataset and the evidentiary graph, not the ≥2017 corpus. (3) _Ingestion friction_ → design around bulk PDF export + OCR; do not assume an API or the fast portal flow for agents/attorneys. (4) _Incumbent fast-follow_ → lead with accreditation-credibility and depth, not a feature an incumbent can replicate in a quarter.

---

## 4. Marketability

**Wedge verification (partially tested — this is the whole thesis, so state its limits plainly).** Two competitors were **deeply verified** and both leave the wedge open:

- **Vala** (attorneys/agents/VSOs): "instantly scans thousands of pages to surface key evidence, conditions, and gaps" + auto-generates completed VA forms. **No** effective-date reconstruction, point-in-time regulation, or CUE feature anywhere on the page; pricing unpublished. (CONFIRMED 3-0; https://valaclaims.com/)
- **VCH / VA Claim Helper** ("built exclusively for Accredited Agents and Attorneys"): C-File AI analysis that identifies "potential claims, secondary conditions, and key evidence," 20+ auto-filled forms, and an **"Automated Appeal Deadline Guard"** (365-day appeal-window tracker — forward-looking, _not_ backward effective-date/CUE). No CUE or effective-date analysis on the page. (CONFIRMED 3-0; https://vaclaimhelper.com/)

**Important caveat surfaced in verification:** VCH's Jan-30-2026 "C-File AI Analysis" launch blog shows VCH now builds "a chronological timeline of a veteran's entire claims history" that extracts "conditions, disability percentages, and effective dates" and runs a "gap analysis" of under-rated benefits. So VCH **extracts existing effective dates into a timeline** — it just doesn't _reconstruct/argue the earliest legally-correct_ date or do CUE. That is closer to the wedge than the spec implies, and it means the incumbent is one reasoning-layer away. (https://vaclaimhelper.com/blog/blog/2026/01/30/...)

Lightly-checked (search snippets only, not deep-verified): **VeteranAi** (veteran-facing C-file analyzer, condition-spotting), **claim.vet** (veteran-facing, file-faster/CFR-cited guides). **Not checked at all:** Caliber/Flagship, ClaimClam, legal-AI VA verticals. So the honest statement is: _"no competitor does CUE" is confirmed for Vala and VCH and consistent with the AI-native entrants that were glanced at, but it is not a settled global fact._

**Pain & willingness to pay.** CUE/earliest-effective-date work is delivered today as a **bespoke, attorney-provided legal service** (e.g., Hill & Ponton blog content), done manually by specialist firms — "under-automated, error-prone, high-value," consistent with the pain thesis. Dollar value is large: a CUE win runs backpay to the original claim date. Adjacent tool pricing anchors: VCH ~$33–150/mo, claim.vet ~$49/mo, Vala/ClaimClam unpublished. The proposed $150–400/seat + credits sits above the VA-tool band but far below horizontal legal-AI. (https://www.hillandponton.com/how-can-you-use-a-cue-claim-...)

**Buyer, channels, barriers.** Fee-eligible population is **~6,720** (6,200 attorneys + 520 agents, RIN 2900-AR94, Oct 2024); older 2020 CRS figure ~8,080 attorneys + 525 agents; full OGC roster ~18,310 including **9,705 VSO reps who legally cannot charge fees** (non-monetizable as paying seats in the same way). **~27,250 fee agreements are filed per year** (750 first-time + 26,500 repeat), indicating active fee-charging volume. **NOVA** is the reachable channel: ~850 members, dues $460/yr (new attorney/agent), two ~15-CLE-hour conferences/year — a small, credential-gated, reachable community. Adoption frictions: AI-hallucination skepticism, malpractice/ethics anxiety, firm security review, OCR-pipeline integration burden, and the "not representation itself" marketing line. (https://www.congress.gov/crs-product/R46428, https://www.federalregister.gov/documents/2024/10/11/2024-23610/..., https://www.vetadvocates.org/cpages/membership)

**Competitive durability.** Horizontal incumbents are structurally aimed at BigLaw and priced out of this segment: **Harvey ~$1,200/seat/mo** (range ~$150/seat at Am Law 100 scale up to ~$2,000 for small firms), **20–25 seat minimum, 12-month terms, ~$288K–360K/yr floor**, plus $10K–50K implementation; **CoCounsel ~$225–400/user/mo** (Westlaw-bundled, ~$639/mo solo); Legora $300–800/seat. None markets a VA/veterans-disability vertical. (https://www.casefleet.com/blog/legal-ai-pricing-rate-limits-and-overages, https://www.eesel.ai/blog/harvey-ai-pricing, https://www.aivortex.io/legal/compare/harvey-ai-vs-cocounsel/) **But durability is thin from below:** the regulation corpus is free, VCH already builds the timeline, and the CUE reasoning layer is the only real differentiator — replicable by an existing VA tool in a quarter or two. The defensible moats are (weakly) the pre-2017 effective-date dataset and (more durably) accreditation-credibility and specialist trust — not the technology.

---

## 5. Revenue — Five Scenarios _(FOUNDER-FACING MODELING, not a verified finding)_

> **This section is my modeling built on the verified inputs below — it is NOT web-verified research.** The workflow gathered market _inputs_; it did **not** build a financial model. I build it here and critique the spec's linear "5–15% → $1–3M ARR."

**Verified inputs used:** fee-eligible TAM **~6,720** (RIN 2900-AR94); VA-administered fee pool **$410.8M trailing-12-mo / $34.2M-mo** (VBA report, 2026-07-06) — *the corrected figure, higher than the spec's $396.8M*; ~27,250 fee agreements/yr; NOVA ~850 engaged members; VA-tool price band $33–150/mo; proposed price $150–400/seat/mo + credits. **Modeling assumptions (mine):** blended ACV = seat + metered CUE credits, richer for multi-seat/firm accounts; churn, CAC, ramp, and long credentialed sales cycles applied explicitly.

**Why the spec's "5% → $1M / 15% → $3M" is wrong as stated:** it treats penetration as instantaneous and frictionless, ignores that ~15% of a 6,720 TAM is only ~1,000 seats, and assumes a flat $3,000 ACV with zero churn, zero CAC, and no ramp. Real SaaS into a tiny, conservative, credential-gated professional base ramps over years and leaks to churn. Penetration is a _Year-3 steady-state_, not a Day-1 lever.

| Scenario             | Paying customers (Yr3)                                | Segment mix                                | Blended ACV | Yr1 ARR | Yr2 ARR | Yr3 ARR           | Key assumptions                                                                                                                                             |
| -------------------- | ----------------------------------------------------- | ------------------------------------------ | ----------- | ------- | ------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Worst**            | ~20–40 accounts (stall)                               | ~all solo                                  | ~$3,000     | ~$30K   | ~$75K   | ~$60K (declining) | Wedge neutralized (VCH/Vala ship CUE) or ingestion proves impractical; ~40%+ churn; no firm deals                                                           |
| **Conservative**     | ~120 accounts (~1.8% of TAM)                          | mostly solo, 1–2 boutiques                 | ~$3,500     | ~$60K   | ~$180K  | ~$380K            | Slow solo adoption, ~25–30% churn, long sales cycles, high CAC                                                                                              |
| **Realistic (base)** | ~250–300 accounts (~4%)                               | solo-heavy + a few boutiques (multi-seat)  | ~$4,500     | ~$120K  | ~$450K  | **~$1.0–1.3M**    | Wedge holds 2–3 yrs; ~20% churn; credits add ~30% to seat revenue; 3–5 small firm deals                                                                     |
| **Optimistic**       | ~350 accounts / ~500 seats (~7–8% weighted)           | solo + several boutique/mid site licenses  | ~$5,500     | ~$250K  | ~$900K  | **~$2.5–2.8M**    | Frictionless ingestion, healthy retention (~12% churn), NOVA channel converts, firm site licenses land                                                      |
| **Aggressive**       | ~1,000 paid seats (~15% fee TAM + some VSO org seats) | solo + firm site licenses + a VSO-org tier | ~$6,000     | ~$400K  | ~$1.6M  | **~$4.5–5M**      | _All must be true:_ agent/attorney ingestion frictionless, wedge stays unoccupied, multiple firm deals, VSO orgs licensed despite non-fee status, low churn |

**Narrative.**

- **Worst:** a competitor adds a CUE reasoning layer to an existing timeline (VCH is one step away) or agents/attorneys can't get workable ingestion — the product stalls as a lifestyle/failed outcome under $100K.
- **Conservative:** slow, solo-only, churn-eroded growth; a real business only if costs are tiny.
- **Realistic:** the honest base case is **~$1M ARR by Year 3** — matching the _top_ of the spec's naïve range but taking 3 years, requiring firm deals, and net of churn. This is a _good_ outcome for this TAM, not a floor.
- **Optimistic:** requires the ingestion story and firm site licenses both to work.
- **Aggressive:** requires a stacked list of things that must _all_ be true; treat as a ceiling, not a plan.

**Sensitivity — the 2–3 variables that swing everything:** (1) **whether firm/multi-seat site licenses land** — multi-seat multiplies ACV and is the difference between the Conservative and Realistic columns; (2) **churn** — at a ~6,720 TAM there is no large top-of-funnel to replace leaked accounts, so 30% vs 15% churn compounds brutally by Year 3; (3) **ingestion friction / activation** — if bulk-export + OCR onboarding is painful (and the fast portal flow stays closed to agents/attorneys), penetration and retention both collapse toward Worst. A large TAM framing would be dishonest here: **a $410.8M fee pool is the veterans' money, not the vendor's market** — the serviceable revenue is bounded by ~6,720 seats, and "found money" for veterans ≠ captured revenue for the tool.

---

## 6. Verification Ledger

25 load-bearing claims were adversarially verified (3 independent votes each): **23 confirmed, 2 refuted, 0 unverified.** Corrections and refutations are surfaced first.

| Claim                                                                                                                                                                                       | Verdict                         | Source                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **CORRECTION:** VA attorney/agent fee pool is **$410.8M trailing-12-mo / $34.2M-mo (as of 2026-07-06)** — higher than the spec's $396.8M / $33.1M-mo                                        | **Corrected & Confirmed (3-0)** | https://www.benefits.va.gov/REPORTS/attorney-fee-report/                                               |
| **CORRECTION:** The $396.8M-class fee figure does **not** come from RIN 2900-AR94; that RIN is a CLE/accreditation rule and contains no such figure (population count _is_ in it)           | **Confirmed (3-0)**             | https://www.federalregister.gov/documents/2024/10/11/2024-23610/...                                    |
| **REFUTED:** CFR July-1 annual revision "sets point-in-time granularity to annual (July 1) snapshots" — false; true granularity is **day-level** by Federal Register effective date         | **Refuted (0-3)**               | https://www.ecfr.gov/reader-aids/using-ecfr/ecfr-changes-through-time                                  |
| **REFUTED:** eFolder Express is "VA-internal-only, not for external accredited agents/attorneys" — the _Caseflow product_ is the external accredited-rep access channel under §§1.600–1.603 | **Refuted (1-2)**               | https://github.com/department-of-veterans-affairs/efolder-express (README) vs. 38 C.F.R. §§1.600–1.603 |
| eCFR native point-in-time system reaches back only to **~January 2017** (critical moat constraint)                                                                                          | Confirmed (search)              | https://www.ecfr.gov/reader-aids/using-ecfr/ecfr-changes-through-time                                  |
| Vala's capabilities stop at evidence/condition/gap surfacing + form generation; no effective-date/CUE                                                                                       | Confirmed (3-0)                 | https://valaclaims.com/                                                                                |
| VCH's C-file AI analysis stops at claim/condition/evidence spotting; no CUE/effective-date                                                                                                  | Confirmed (3-0)                 | https://vaclaimhelper.com/                                                                             |
| VCH's appeal feature is a 365-day deadline tracker, not effective-date/CUE                                                                                                                  | Confirmed (3-0)                 | https://vaclaimhelper.com/                                                                             |
| VCH marketing page makes no mention of effective-date/CUE                                                                                                                                   | Confirmed (3-0)                 | https://vaclaimhelper.com/                                                                             |
| GovInfo provides CFR annual editions back to ~1996/1997 (machine-readable, annual granularity)                                                                                              | Confirmed (3-0)                 | https://www.govinfo.gov/help/cfr                                                                       |
| Full CFR available as machine-ingestible bulk XML via Data.gov + GPO Bulk Data Repository                                                                                                   | Confirmed (3-0)                 | https://www.govinfo.gov/bulkdata/CFR                                                                   |
| eCFR versioner API exposes historical versioned Title 38 amendments in JSON, keyed to dates                                                                                                 | Confirmed (3-0)                 | https://www.ecfr.gov/api/versioner/v1/versions/title-38.json                                           |
| Each version record carries date / amendment_date / issue_date fields                                                                                                                       | Confirmed (3-0)                 | https://www.ecfr.gov/reader-aids/ecfr-developer-resources/understanding-ecfr-dates                     |
| GPO/FDsys bulk repo hosts only most-recent e-CFR; point-in-time editions live at ecfr.gov                                                                                                   | Confirmed (3-0)                 | https://github.com/usgpo/bulk-data/blob/main/ECFR-XML-User-Guide.md                                    |
| e-CFR bulk XML available only from 2015 forward                                                                                                                                             | Confirmed (2-1)                 | https://github.com/usgpo/bulk-data/blob/main/ECFR-XML-User-Guide.md                                    |
| VA final rule establishes 38 C.F.R. 1.600–1.603, effective July 25, 2022                                                                                                                    | Confirmed (3-0)                 | https://www.federalregister.gov/documents/2022/06/24/2022-13312/...                                    |
| Access is read-only; reps cannot modify VA data (may upload new docs)                                                                                                                       | Confirmed (3-0)                 | 38 C.F.R. §§1.600–1.603                                                                                |
| Access granted specifically to VBMS + Caseflow Queue + eFolder Express                                                                                                                      | Confirmed (3-0)                 | 38 C.F.R. §1.600                                                                                       |
| For attorneys/agents, access is per-POA (only claimants who appointed them)                                                                                                                 | Confirmed (3-0)                 | 38 C.F.R. §§1.600–1.601                                                                                |
| A representative may access only records of claimants who appointed them, via §14.631 POA, solely for representation                                                                        | Confirmed (3-0)                 | 38 C.F.R. §§1.600–1.603                                                                                |
| Caseflow eFolder Express is a bulk-download product (all files at once, from VBMS + VVA)                                                                                                    | Confirmed (3-0)                 | https://department-of-veterans-affairs.github.io/caseflow/task_trees/data-model/efolder_express.html   |
| eFolder Express (GitHub tool) depends on `connect_vbms` (internal connectivity, not public API)                                                                                             | Confirmed (3-0)                 | https://github.com/department-of-veterans-affairs/efolder-express                                      |
| 38 C.F.R. §1.600 grants accredited attorneys/agents/VSO reps read-only VBMS + Caseflow access                                                                                               | Confirmed (3-0)                 | https://www.ecfr.gov/current/title-38/chapter-I/part-1/subject-group-ECFRae92831392dc7e6               |
| RIN 2900-AR94 (Oct 2024): ~6,200 attorneys + 520 agents (~6,720 fee-eligible)                                                                                                               | Confirmed (3-0)                 | https://public-inspection.federalregister.gov/2024-23610.pdf                                           |
| RIN 2900-AR94 is a CLE/accreditation proposed rule (title confirmed; not a fee-totals doc)                                                                                                  | Confirmed (3-0)                 | https://www.federalregister.gov/documents/2024/10/11/2024-23610/...                                    |

**Additional confirmed context (not among the 25 formal votes but extracted with primary quotes):** 38 C.F.R. §3.105(a) retroactive-effect mechanism; §20.1403 CUE definition + record-and-law-at-the-time constraint + exclusions; §3.816 Nehmer effective-date rule; §14.636 fee cap (20% presumed reasonable, >33⅓% presumed unreasonable; fees only after AOJ initial decision; must file fee agreements); 2020 CRS counts (8,080 attorneys / 525 agents / 9,705 VSO reps); NOVA dues; Harvey/CoCounsel/Legora pricing; Stanford ~17–33% legal-RAG hallucination rate.

---

## 7. Open Questions & What to Re-Verify Before Launch

**What this research did NOT cover (do not treat as settled):**

- **The wedge thesis is only partially tested.** Only **Vala and VCH** were deep-verified for "no competitor does CUE." **Caliber/Flagship, ClaimClam, claim.vet (deep), and any legal-AI VA vertical were not deeply checked.** Re-verify the full competitor set — especially whether VCH/Vala have shipped a CUE or earliest-effective-date reasoning layer, since VCH already builds the timeline.
- **Pre-2017 point-in-time regulatory sourcing** — the real moat — was confirmed to be _hard_ but the actual reconciliation (GovInfo annual ↔ Federal Register effective dates) and pre-1996 acquisition (HeinOnline licensing vs. OCR) were not scoped or costed.
- **BVA / CAVC / Federal Circuit bulk decision corpora** (feasibility component d) were **not fetched at all** — availability and quality are unknown.
- **Whether eFolder Express offers any API vs. only manual bulk `.zip` export** for the target buyer — the sources point to manual/bulk, but confirm before assuming automated ingestion.
- **Whether the Accredited Representative Portal's fast "access within minutes" flow has opened to agents/attorneys** (not just VSO reps) since the mid-2026 snapshot — this materially affects onboarding friction and the revenue model. The VA.gov representative-help page returned no extractable data and must be re-checked.
- ~~**Case-law citations "Chisholm v. Collins" and "Hamill v. Collins"** did not surface~~ **RESOLVED (`citation-verifier` 2026-07-16):** both are real, correctly-cited effective-date decisions — _Chisholm v. Collins_, 38 Vet. App. 140 (2025); _Hamill v. Collins_, No. 24-1543 (Fed. Cir. Feb. 4, 2026). No longer an open item.
- ~~**Fee-rule model constraints** (§14.632(c)(5) success-fee prohibition unpulled)~~ **RESOLVED (`citation-verifier` 2026-07-16):** §14.636 confirmed; **§14.632(c)(5) was MISSTATED** — it is a general "clearly unreasonable or otherwise prohibited" fee rule binding the accredited rep, **not** a categorical vendor-success-fee ban. The no-success-fee conclusion holds but rests on §14.636 + the §5904/§14.636 bar on non-accredited persons receiving claimant fees. (Corrected in the spec, prompt, and REPORT.)
- **Security/compliance architecture** was verified only as a regulatory _boundary_, not as a concrete design that would pass a firm's + VA's review.

**Currency flags:** competitor feature sets, pricing, the fee pool, the portal-access rollout, and accreditation counts are all snapshots (mid-2026). Re-verify each before a launch decision.

---

## 8. Sources

**Primary (government / regulation / first-party):**

- https://www.ecfr.gov/reader-aids/using-ecfr/ecfr-changes-through-time — eCFR point-in-time system (back to ~Jan 2017)
- https://www.ecfr.gov/developers/documentation/api/v1 — eCFR API documentation
- https://www.ecfr.gov/api/versioner/v1/versions/title-38.json — live versioner endpoint (Title 38)
- https://www.govinfo.gov/app/collection/cfr/ and https://www.govinfo.gov/help/cfr — CFR annual editions (1996/1997+)
- https://www.govinfo.gov/bulkdata/CFR — GPO bulk CFR XML
- https://github.com/usgpo/bulk-data/blob/main/ECFR-XML-User-Guide.md — GPO eCFR XML user guide
- https://www.federalregister.gov/developers/documentation/api/v1 — Federal Register API (effective dates)
- https://www.federalregister.gov/documents/2022/06/24/2022-13312/... — Final rule, 38 C.F.R. §§1.600–1.603 (data access)
- https://www.ecfr.gov/current/title-38/chapter-I/part-1/subject-group-ECFRae92831392dc7e6 — 38 C.F.R. §§1.600–1.603 codified
- https://department-of-veterans-affairs.github.io/caseflow/task_trees/data-model/efolder_express.html — Caseflow eFolder Express data model
- https://github.com/department-of-veterans-affairs/efolder-express — eFolder Express GitHub tool (archived 2023)
- https://www.federalregister.gov/documents/2024/10/11/2024-23610/... and https://public-inspection.federalregister.gov/2024-23610.pdf — RIN 2900-AR94 (population ~6,720)
- https://www.benefits.va.gov/REPORTS/attorney-fee-report/ — VBA attorney/agent fee report ($410.8M / $34.2M-mo, 2026-07-06)
- https://www.congress.gov/crs-product/R46428 — CRS R46428 (2020 accreditation counts)
- https://www.law.cornell.edu/cfr/text/38/14.636 — 38 C.F.R. §14.636 fee cap
- https://www.vetadvocates.org/cpages/membership — NOVA membership/dues
- https://www.ecfr.gov/current/title-38/chapter-I/part-3/subpart-A/subject-group-ECFR63da83ba671b92b/section-3.105 — §3.105 CUE revision
- https://www.ecfr.gov/current/title-38/chapter-I/part-20/subpart-O/section-20.1403 — §20.1403 CUE standard
- https://www.ecfr.gov/current/title-38/chapter-I/part-3/subpart-A/subject-group-ECFR2c3eca6251aa67b/section-3.816 — §3.816 Nehmer

**Primary (competitor product pages):**

- https://valaclaims.com/ — Vala
- https://vaclaimhelper.com/ — VCH / VA Claim Helper (+ Jan-2026 C-File AI Analysis blog)

**Secondary:**

- https://caselaw.findlaw.com/court/us-9th-circuit/1219226.html — Nehmer (9th Cir. 2007)
- https://www.greene-marusak.com/cue — CUE three-part test (Russell/Fugo) _[not independently verified]_

**Blog / vendor-marketing (pricing & hallucination context — treat as corroborating estimates):**

- https://www.casefleet.com/blog/legal-ai-pricing-rate-limits-and-overages
- https://www.aiforlegalresearch.com/tools/harvey-ai (Harvey fabricated-citation case; Stanford ~17–33% hallucination)
- https://www.aivortex.io/legal/compare/harvey-ai-vs-cocounsel/
- https://bindlegal.com/resources/comparisons/harvey-pricing-2026/
- https://www.eesel.ai/blog/harvey-ai-pricing
- https://www.vaquill.ai/blog/harvey-legora-cocounsel-pricing-reality
- https://veteranai.co/va-cfile-analyzer — VeteranAi (lightly checked)
- https://claim.vet/blog/ai-va-disability-claims/ — claim.vet (lightly checked)
- https://www.hillandponton.com/how-can-you-use-a-cue-claim-to-get-an-earlier-effective-date-... — how CUE work is delivered today
