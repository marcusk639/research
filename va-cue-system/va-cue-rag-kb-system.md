# Product Spec & Go-to-Market Plan: A RAG/Agentic Knowledge Tool for VA-Accredited Claims Agents and Attorneys — The Effective-Date / CUE Wedge

## TL;DR

- **Build the tool that no competitor has built: an "Effective-Date & CUE Engine" that ingests a veteran's C-file/e-folder, reconstructs a timeline of every prior final decision and the evidence and law in effect at each, and outputs a CUE-viability analysis, an earliest-effective-date argument, and a citation-ready draft motion.** Every professional VA-claims tool on the market today (Vala, VCH, Caliber, claim.vet) stops at C-file summarization, condition-spotting, and form-filling — none does effective-date determination or CUE detection. That is the open, defensible wedge.
- **Sell it as per-seat SaaS to solo/small accredited practices first ($150–$400/seat/month), layered with a per-analysis "CUE deep-dive" credit, and reach buyers through the VA OGC public accreditation list, NOVA (National Organization of Veterans' Advocates), and content marketing anchored by a free CUE-viability screen as a lead magnet.** Avoid a success-fee model — it collides with 38 CFR §14.636 fee rules and creates accreditation risk.
- **The economics work because the profession is contingency-driven and effective-date errors are pure "found money":** VA paid **$396.8 million** in attorney/agent fees in the trailing 12 months (per VBA's Office of Performance Analysis and Integrity: "Last 12 Months: $396.8M · Avg. 12 Months: $33.1M"), all as 20% of past-due benefits. A tool that reliably finds earlier effective dates directly grows the 20% base its buyers are paid on, making ROI self-evident. Capturing 5% of ~6,700 fee-charging accredited professionals at ~$3,000/year ≈ **$1 million ARR**; 15% ≈ **$3 million ARR**.

## Key Findings

**1. The market gap is real and specific.** A product-by-product review of the professional-facing tools — Vala (valaclaims.com, demo-only pricing), VA Claim Helper/VCH ($33–$150/month tiered), Caliber/Flagship (free, used by vaclaims.us), and claim.vet's $49/month Agency tier — confirms that all of them stop at C-file analysis, evidence/condition surfacing, and VA-form generation. The closest adjacent feature anywhere is VCH's "Automated Appeal Deadline Guard" (tracking the 365-day appeal window). **None performs effective-date reconstruction or CUE analysis.** Consumer tools (VeteranAi, VetClaims.ai) are aimed at veterans, not accredited pros, and also lack these features.

**2. Effective-date and CUE work is the highest-value, most error-prone, least-automated task in the practice.** It is where the money is (moving an effective date back two years at a 70% rating with no dependents is worth over $43,000; at the TDIU/100% rate, over $47,000/year), where the law is hardest (CUE requires applying the facts _and the version of the regulation_ in effect at the time of the prior decision, and can only be based on evidence then of record), and where a mistake is nearly irreversible (a veteran generally gets only one CUE bite at a given decision). This is precisely the kind of high-stakes, rule-dense, document-heavy reasoning that a well-built GraphRAG + agentic system augments better than a human skimming a 2,000-page PDF.

**3. The buyer is well-defined and reachable.** There are roughly 6,700 fee-charging accredited professionals (~520 claims agents + ~6,200 attorneys per the Federal Register, RIN 2900-AR94), all publicly listed on the VA OGC accreditation search (the underlying roster runs to nearly 15,000 entries once VSO representatives and organizations are included). They concentrate in a modest number of boutique-to-mid firms (Chisholm Chisholm & Kilpatrick advertises "the most VA-accredited attorneys, practitioners, and claims agents of any law firm in the United States," with 25+ VA-accredited attorneys; Hill & Ponton, Berry Law, Woods & Woods, and Bergmann & Moore are other anchors) plus a long tail of solos. NOVA is the single best professional watering hole: it "represents over 850 accredited attorneys, agents, and qualified members" (per NOVA's June 2024 House Veterans' Affairs Committee testimony) and "conducts two conferences per year, each of which provide approximately 15 hours of continuing legal education (CLE) credit."

**4. Data access is now dramatically easier than it was two years ago.** Accredited attorneys/agents get read-only VBMS + Caseflow eFolder Express access (38 CFR §§1.600–1.603), and the new Accredited Representative Portal — per VA.gov, "The portal opens to all accredited representatives in Fall 2025... Access the VBMS eFolder within minutes of establishing representation" — plus "Appoint a Representative 2.0" (released to 100% of users on March 25, 2025, enabling reps to "establish the Power of Attorney relationship in the Veteran's VBMS eFolder within minutes (not days or weeks)," per VA's va.gov-team product documentation) now establishes POA and eFolder access within minutes. This makes automated C-file ingestion viable at scale.

**5. Regulatory constraints shape the design but do not block it.** The tool augments accredited humans; it must never be marketed as representation itself (unaccredited claim assistance for a fee is illegal under 38 U.S.C. §5904). VA has no rule prohibiting AI use in representation, but the §14.632 competence/diligence standard means the accredited user remains responsible for verifying every output — which argues for a citation-first, human-in-the-loop, no-hallucination architecture and rigorous PII/PHI security.

## Details

### 1. Prioritized Feature Spec (with rationale and value)

The real day-to-day workflow of an accredited agent/attorney building a claim, appeal, or CUE motion is: (a) intake and C-file/e-folder review; (b) identify prior final decisions and their effective dates; (c) determine what evidence was of record at the time of each prior decision; (d) apply the legal standard _in effect at that time_; (e) calculate and argue the earliest possible effective date; (f) spot special effective-date regimes (Nehmer, liberalizing-law, ITF, BDD, §3.400(o)(2) increases); (g) draft the appropriate instrument (Supplemental Claim, HLR, Board appeal, or CUE motion) with 38 CFR and case-law citations; and (h) track the matter through the AMA lanes and deadlines. Below, features are ranked by value × differentiation.

**TIER 1 — The Wedge (build first; this is the moat)**

- **F1. Effective-Date Timeline Reconstructor.** Ingests the full C-file/e-folder and produces a structured, date-stamped timeline: every claim filed (formal, informal, ITF), every rating decision and its assigned effective date, every NOD/appeal, what evidence entered the record on what date, and what was decided when. _Output:_ an interactive timeline + a "what the VA knew, and when" ledger. _Value:_ This is the substrate for every downstream argument and today takes hours of manual PDF review per case. _Rationale:_ An accredited advocate needs a chronology of "when VA knew what" — exactly what the tool should automate.

- **F2. CUE-Viability Analyzer.** For any prior final decision, runs the three-part CUE test (was the correct fact not before the adjudicator OR was the law incorrectly applied; was it an error on the record/law then existing; would correcting it have "manifestly changed the outcome"). Critically, it enforces the two hard CUE constraints that trip up practitioners: (i) only evidence _of record at the time_ may be used, and (ii) the _version of the regulation in effect at the time_ must be applied. _Output:_ a CUE-viability score with a plain-English rationale, the specific alleged error framed to meet the pleading-specificity requirement, and flags for common losing arguments (duty-to-assist breach, mere disagreement over weighing of evidence — both categorically barred). _Value:_ CUE is high-reward but one-shot; a screen that filters non-viable theories and sharpens viable ones is worth far more than its price in a single won case.

- **F3. Point-in-Time Regulation Retriever ("time-machine" RAG).** A versioned corpus of 38 CFR (Parts 3, 4, 19, 20) and 38 USC keyed to effective dates, so the engine can retrieve and cite the regulation _as it read on the date of the prior decision_, not today's text. _Value:_ This is the single hardest thing to do correctly and the single most defensible technical asset. Off-the-shelf legal-AI tools index current law; a point-in-time regulatory graph is a genuine barrier to entry.

- **F4. Nehmer / Special-Effective-Date Detector.** Automatically flags Agent Orange/herbicide (Nehmer, 38 CFR §3.816) fact patterns, liberalizing-law rules (§3.114), ITF (§3.155), BDD (§3.400(b)(2)), and factually-ascertainable-increase (§3.400(o)(2)) windows. _Value:_ Nehmer alone has driven billions in retroactive payments (NVLSP reports "more than $4.6 billion in retroactive benefits to more than 100,000 veterans and their survivors") and routinely produces effective dates years earlier than the general rule; missing it is malpractice-adjacent.

**TIER 2 — Table Stakes + Drafting (build to be competitive)**

- **F5. Evidence-of-Record Verifier.** Cross-checks a proposed argument against what was actually in the file on a given date — the guardrail that keeps a CUE motion from relying on later-added evidence.
- **F6. Citation-Grounded Draft Generator.** Produces first-draft Supplemental Claims, HLR requests, Board appeals, and CUE motions with pinpoint 38 CFR / CAVC / Federal Circuit citations and verbatim quotes, each linked to its source (no free-floating citations).
- **F7. C-File Analyzer / Condition & Secondary Spotter.** The commodity feature every competitor has: surface conditions, secondaries, gaps, and rating errors. Needed for parity, but not the differentiator.
- **F8. AMA Lane Recommender + Deadline Guard.** Given a decision, recommends the optimal lane (Supplemental / HLR / Board docket) to preserve the effective date, and tracks the one-year lane-switching clock under §3.2500.

**TIER 3 — Practice Infrastructure**

- **F9. VBMS/Portal ingestion connector** (read-only, per §§1.600–1.603).
- **F10. Rating/back-pay calculator** tied to the effective-date output, so the advocate can quantify the 20% fee at stake.

**Data/document types to ingest:** C-files/e-folders, rating decisions and codesheets, SOCs/SSOCs, prior BVA and CAVC/Federal Circuit decisions, DD-214s, service treatment records, VA Form 21-series (21-526EZ, 21-4138, 21-0966 ITF, 21-22a POA), 20-0995/20-0996/10182 decision-review forms, and C&P/DBQ exam reports.

**Systems to integrate:** VBMS + Caseflow eFolder Express (read-only accredited access), the Accredited Representative Portal, and the versioned eCFR/USC and BVA/CAVC decision corpora as the RAG knowledge base.

### 2. Competitive Positioning

**Where existing tools stop:** Vala, VCH, Caliber, VeteranAi, VetClaims.ai, and claim.vet all cluster on the _front end_ of a claim — reading records, spotting conditions, filling forms. This is the crowded, commoditizing part of the market where a free tool (Caliber, "Free, no seat or per claim fees") and a $33/month tool (VCH) already compete.

**Where the gap is:** the _retroactive/analytical_ end — reconstructing the past, testing final decisions for CUE, and arguing the earliest effective date. No competitor touches it, because it is hard: it requires point-in-time law, disciplined evidence-of-record logic, and defensible citations.

**Defensibility against a legal-AI incumbent (Harvey, CoCounsel) building a VA vertical:**

1. **Point-in-time regulatory graph** (F3) — incumbents index _current_ law; the historical, versioned 38 CFR corpus keyed to decision dates is a hand-built asset they don't have and won't prioritize for a niche vertical.
2. **Vertical depth over horizontal breadth** — Harvey's ~20-seat minimum and reported ~$1,200+/seat/month base pricing (roughly $288,000/year floor) make the ~6,700-professional VA niche commercially uninteresting to them; CoCounsel is ~$225/user/month standalone (higher bundled with Westlaw). A focused tool at a fraction of that price wins the segment before they arrive.
3. **Workflow lock-in via VBMS/Portal integration and matter history** — the accumulated per-firm timeline data and CUE work-product become switching costs.
4. **Founder credibility** — a USAF veteran who becomes VA-accredited himself and is visible in NOVA has trust and distribution an incumbent cannot buy quickly.

### 3. Pricing & Business Model

**Recommendation: per-seat SaaS + per-analysis credits. Do NOT use a success/referral fee.**

- **Core SaaS:** $150–$400/seat/month depending on tier (solo vs. firm), positioned deliberately _below_ general legal-AI (CoCounsel ~$225/user/month standalone; Harvey ~$1,200+/seat/month) and _above_ the commodity VA form-fillers (VCH $33–$150/month) — because the value delivered (found back pay) is an order of magnitude higher.
- **Per-analysis "CUE Deep-Dive" credits:** a metered add-on (e.g., a bundled credit per full effective-date/CUE workup on a complex file) that aligns cost with the highest-value use and lets solos pay as they win.
- **Why not a success fee:** tying the tool's revenue to the advocate's 20% contingency recovery would make the vendor a de facto participant in the fee, colliding with §14.636 (fees must be the accredited rep's, reasonable, and — for direct pay — capped at 20% of past-due benefits and filed with VA) and with the rule that **only accredited agents/attorneys may receive claimant fees at all** (§5904 / §14.636) — which a non-accredited vendor is not. §14.632(c)(5) adds only a **general backstop** barring any fee "clearly unreasonable or otherwise prohibited by law or regulation"; it is **not, by itself, a categorical vendor-success-fee ban** _(corrected 2026-07-16 per citation-verifier)_. A vendor is not accredited and cannot share in the contingency. Clean SaaS pricing avoids this entirely.

**Revenue model (illustrative, on ~6,700 fee-charging accredited professionals):**

- At ~$3,000/professional/year (blended seat + credits): 5% penetration ≈ **$1.0M ARR**; 10% ≈ **$2.0M ARR**; 15% ≈ **$3.0M ARR**.
- Firm-level deals (CCK-class buyers with 25+ accredited professionals) can anchor early ARR: a single mid-size firm at $300/seat/month × 20 seats ≈ **$72,000/year**.

The macro backdrop supports willingness to pay: $396.8M in trailing-12-month VA-paid attorney/agent fees (monthly average $33.1M), a Board that "adjudicated and dispatched a record 116,192 appeals" in FY2024 against pending appeals that "went down from 208,155" (per the BVA FY2024 Annual Report), and effective-date errors that VA itself concedes are common — the total addressable "found money" the tool helps unlock is very large relative to its price.

### 4. Phased Go-to-Market

**Phase 0 (0–3 months) — Earn credibility.** Complete SDVOSB certification and pursue VA accreditation personally (claims-agent exam — offered on set dates such as the August 25, 2026 and January 26, 2027 sittings — or, if eligible, the attorney route). Being on the OGC list confers trust, warm introductions, and firsthand access to VBMS to dogfood the product on real files. Build the point-in-time regulation corpus and F1/F2/F3 as an MVP.

**Phase 1 (3–9 months) — Solo & boutique beachhead.** Target solo accredited agents and small veterans-law firms (the long tail on the OGC list) who feel effective-date/CUE pain acutely but can't staff a dedicated appellate team.

- _Channels:_ the OGC public accreditation list (direct outreach), NOVA membership + the two annual CLE conferences (Spring in San Diego April 2026; Fall) and NOVA member forums, LinkedIn niche outreach, and content marketing (blog/CLE-style explainers on Nehmer, §3.400, CUE pleading).
- _Lead magnet:_ a **free CUE-viability screen** — upload one decision, get a preliminary viability read — which doubles as product demo and top-of-funnel capture.
- _Messaging:_ "Find the back pay other tools miss. The only engine that reconstructs the record and tests every final decision for CUE and the earliest effective date."

**Phase 2 (9–18 months) — Mid-size firms & VSOs.** Move upmarket to CCK/Hill & Ponton/Berry Law-class firms (site licenses, security review, VBMS integration) and to VSOs/accredited service officers (who don't charge fees but carry enormous claim volume and would value the analytical screen; price them on a separate non-contingency tier). Present at NOVA; pursue co-marketing with medical-opinion vendors already sponsoring NOVA (e.g., Mednick Associates, Prestige Veteran Medical Consulting).

**Phase 3 (18+ months) — Platform.** Add deeper drafting, matter management, and portal automation; defend with accumulated data and integrations.

### 5. Regulatory / Compliance Constraints to Design Around

- **Do not practice or "assist for a fee" without accreditation.** Only accredited agents/attorneys (and recognized VSOs) may assist claimants; charging fees for claim assistance without accreditation violates 38 U.S.C. §5904 and 38 CFR §14.636. **Design implication:** the product is a _tool sold to accredited professionals_, never a representation service to veterans. Marketing must not imply the tool represents veterans or guarantees outcomes.
- **The accredited user is responsible for competence and diligence** (38 CFR §14.632(b)(1): competent representation "requires the knowledge, skill, thoroughness, and preparation necessary for the representation," including understanding the applicable Title 38 USC/CFR provisions). **Design implication:** citation-first outputs, verbatim source quotes, human-in-the-loop confirmation, and explicit "verify before filing" guardrails — no unsourced assertions, no fabricated citations.
- **No AI-specific prohibition exists, but scrutiny is rising.** There is no 38 CFR/M21-1 rule barring AI in representation, but VA and veteran advocates are increasingly alert to AI-generated junk (unsigned nexus letters, fabricated content) and fraud. Position the tool as an augmentation that produces _verifiable, sourced_ work product.
- **Fee rules constrain the business model, not just the user.** §14.636's 20% direct-pay cap and reasonableness regime — plus the bar on anyone other than an accredited agent/attorney receiving claimant fees (§5904 / §14.636), which a vendor is not — are why a vendor success-fee is off the table. _(§14.632(c)(5) is a general "clearly unreasonable or otherwise prohibited" fee backstop binding the accredited rep, not a categorical success-fee prohibition — corrected 2026-07-16 per citation-verifier.)_
- **Data security / PII & PHI.** C-files contain SSNs, medical records, and service records. Handling implicates the Privacy Act, 38 U.S.C. §5701 and §7332 (confidentiality of VA records, especially drug/alcohol/HIV/sickle-cell), and HIPAA-adjacent obligations. VBMS access itself requires background suitability and read-only handling under §§1.600–1.603. **Design implication:** encryption in transit/at rest, strict access controls, tenant isolation, no training on client data without consent, and an architecture that can pass a firm's and VA's security review.
- **VBMS access is per-POA and read-only.** The tool may ingest and analyze but must not modify VA records, and access is limited to claimants the accredited user actually represents.

## Recommendations

1. **Build the wedge, not another C-file summarizer.** Ship F1 (timeline), F2 (CUE viability), and F3 (point-in-time regulation) as the MVP. If you build only one thing, build the versioned regulatory graph — it is the moat.
2. **Get accredited and SDVOSB-certified before selling.** Credibility and VBMS access are prerequisites, not nice-to-haves, in this trust-driven niche.
3. **Price as per-seat SaaS ($150–$400) + per-analysis credits; never a success fee.** This clears the §14.636/§14.632 fee-rule hazard and still captures value.
4. **Lead with a free CUE-viability screen** as the lead magnet and demo; convert through NOVA and direct OGC-list outreach.
5. **Sequence buyers:** solos/boutiques → mid-size firms + VSOs → platform.

**Benchmarks that would change the plan:**

- If a legal-AI incumbent or an existing VA tool ships a genuine point-in-time-law CUE feature, accelerate the moat (deepen the regulatory graph, lock in integrations) or pivot to firm-level exclusivity deals.
- If solo conversion is weak (<2% of outreach), shift emphasis upmarket to firm site licenses sooner.
- If per-analysis credits outsell seats, rebalance toward a usage-metered model.

## Caveats

- **Competitor pricing is partly opaque.** Vala and ClaimClam do not publish pricing; Harvey/CoCounsel figures are third-party estimates, not rate cards. Treat all competitor prices as reported, not official.
- **The "no CUE/effective-date feature" finding is current as of mid-2026** and based on public marketing pages; a gated product could add such a feature quietly. Re-verify before launch.
- **Population figures vary by source.** The ~520 agents / ~6,200 attorneys figures trace to RIN 2900-AR94; an older 2020 CRS report cited ~8,080 attorneys and ~525 agents. Use the OGC accreditation search for a current, authoritative count before sizing.
- **Revenue estimates are illustrative,** not forecasts; they assume blended pricing and simple linear penetration of the ~6,700 fee-charging population and ignore churn, CAC, and VSO (non-fee) segment dynamics.
- **The Nehmer landscape and case law shift** (e.g., recent CAVC/Federal Circuit effective-date decisions such as _Chisholm v. Collins_ and _Hamill v. Collins_); the tool's legal corpus must be continuously maintained, which is an ongoing cost, not a one-time build.
- **Regulatory interpretation here is not legal advice;** the founder should obtain a formal opinion on the SaaS model's fee-rule compliance before go-to-market.

---

## Addendum — Revised Phase Sequence (2026-07-17, plan-review driven)

> This addendum reorders the §4 go-to-market phases to fix three issues surfaced in
> review: (1) the original sequence proves the **commodity** (≥2017 point-in-time law
> is a free eCFR API) before the **moat** (the pre-1997 corpus); (2) there is no
> accuracy/eval methodology for a liability-sensitive legal tool; (3) it commits a
> ~12-month build + personal accreditation **before** validating the two decisive
> unknowns. The strategy in §§1–5 stands; this changes only sequencing, gates, and
> acceptance criteria. **Each phase has a hard gate — do not proceed until it is met.**

**Decide the goal first (one line, everything hangs on it):** the verified TAM caps a
realistic outcome at **~$1.0–1.3M ARR by Year 3** (the §3 linear "5–15% → $1–3M"
overstates it — it ignores churn, CAC, ramp, and the tiny 6,720 TAM). That is a solid
**bootstrapped / founder-scale** business and a poor **venture-scale** one. Pick the
lane before spending a year building.

### Phase V — Validation Sprint (2–4 weeks, ~$0 build). **Gate before ANY build.**

- **Customer discovery:** 8–12 interviews with accredited agents/attorneys via the OGC
  list + NOVA — confirm the effective-date/CUE pain is top-3, how they do it today, and
  willingness to pay $150–400/seat + credits.
- **Resolve the decisive moat question:** do HeinOnline / Westlaw / LexisNexis / vLex
  already sell **pre-2017 point-in-time CFR retrieval**? If yes, the technical moat is
  commoditized and the plan must pivot to the reasoning/timeline layer.
- **Close the wedge check:** deep-verify the uncovered competitors (Caliber, claim.vet,
  ClaimClam, VetClaims.ai, Vetlex, RepScout) and any **legal-AI VA vertical** (Harvey/
  CoCounsel/Legora/etc.) — the most credible fast-follow. Re-check VCH (already extracts
  effective dates; one reasoning-layer from the wedge).
- **GATE (go/no-go):** proceed only if — pain + WTP confirmed by ≥5 interviews **AND**
  the pre-2017 corpus is not already a cheap commercial product **AND** no competitor
  has shipped effective-date/CUE _reasoning_. Any failure → pivot or stop, before the
  build spend.

### Phase 0 — Foundation (parallel tracks, not serialized). **~3–6 months.**

- **Track A (build):** stand up the **pre-1997 corpus thin slice** — one high-value
  section (e.g., § 3.400 or § 3.105) across 2–3 historical versions, OCR'd and
  **reconciled to Federal Register effective dates**, with proposed-vs-final-rule
  hygiene (the E7-9542 trap). This is the moat, so it starts Day 1.
- **Track B (accreditation):** founder sits the claims-agent exam (Aug 2026 / Jan 2027)
  - SDVOSB — needed for VBMS _dogfooding_, **not** for corpus build or discovery, so it
    runs **concurrently**, not as a blocker.
- **Track C (design partners):** convert 1–2 Phase-V interviewees into committed design
  partners.
- **GATE:** the thin pre-1997 slice is queryable and effective-date-accurate; ≥1 design
  partner committed to test on real files.

### Phase 1 — Moat-first MVP (F1 + F2 + F3, triage only). **~3–4 months.**

- **Walking skeleton that tests the moat, not the commodity:** F1 timeline + F2
  CUE/effective-date **triage** + F3 point-in-time law **including the pre-1997 slice** —
  run against ≥2017 _and_ the historical fact pattern.
- **Eval harness is part of the MVP, not later:** a gold set of known
  CUE/effective-date outcomes, a **measured citation-fidelity rate**, a stated accuracy
  bar, a mandatory **human-in-the-loop gate**, and **no autonomous filing**. Decision-
  support only — **no auto-drafting of legal instruments in the MVP** (F6 is deferred as
  high-liability gold-plating).
- Dogfood on real C-files (uses Track-B accreditation).
- **GATE / acceptance:** hits the accuracy bar on the gold set (fabricated-authority rate
  ≈ 0 after the human gate) **AND** a design partner confirms it saves ≥X hours on a real
  effective-date/CUE workup. "It works" is not acceptance — the number is.

### Phase 2 — Parity + depth. **~6–9 months.**

- Broaden the pre-1997 corpus coverage; add **BVA/CAVC/Fed-Cir RAG** (feasibility of bulk
  corpora is still unverified — confirm early in this phase).
- Add **citation-grounded drafting (F6)** _only after_ the eval harness proves
  reliability at scale — gated, high-liability.
- Add table-stakes C-file spotting (F7) for competitive parity.
- **GATE:** paying (post-design-partner) customers; measured accuracy holds at volume;
  churn signal acceptable.

### Phase 3 — Scale / platform. **Only after retention + accuracy are proven.**

- Firm site licenses, multi-seat, workflow integration, VSO non-fee tier.
- **GATE:** Net revenue retention and accuracy metrics justify scaling spend.

### Anti-patterns this sequence removes

| Original risk                         | Fix                                                 |
| ------------------------------------- | --------------------------------------------------- |
| Deferred moat (pre-1997 in "Phase 2") | Corpus thin slice starts Phase 0; MVP tests it      |
| Untested "no-hallucination" claim     | Eval harness + accuracy bar + human gate in the MVP |
| Build-before-validate (12-mo bet)     | Phase V go/no-go gate precedes all build spend      |
| Serialized accreditation dependency   | Parallel Tracks A/B/C in Phase 0                    |
| Vague "it works" acceptance           | Numeric acceptance gate per phase                   |
| High-liability auto-drafting in MVP   | F6 deferred behind the eval gate                    |
