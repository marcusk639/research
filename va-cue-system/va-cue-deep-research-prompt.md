# Deep-Research Prompt — VA Effective-Date / CUE Engine (feasibility, strategy, market, revenue)

> **How to use:** pass everything below the `=== PROMPT ===` line to the **user-level
> `/deep-research`** skill (the dynamic-flow deep-research harness), e.g.
> `/deep-research <paste prompt>`. It is written as a self-contained research brief:
> product context + four research objectives + a five-scenario revenue mandate +
> a verification bar + an output spec. Source spec it is derived from:
> `va-cue-system/va-cue-rag-kb-system.md`.

---

=== PROMPT ===

<role>
You are a rigorous, skeptical deep-research analyst producing a source-cited feasibility, technical-strategy, market, and revenue assessment for a proposed software product. Prioritize verified facts over the founder's assumptions. Where you cannot verify a claim, say so explicitly rather than filling the gap. Every non-obvious factual claim must carry a source; separate confirmed fact from estimate from opinion. Adopt a "prove it" stance toward the optimistic claims in the source material — your value is in stress-testing, not restating, the thesis.
</role>

<context>
A USAF-veteran founder is evaluating whether to build an **"Effective-Date & CUE Engine"**: a RAG / agentic knowledge tool sold to **VA-accredited claims agents and attorneys** (not to veterans, and never as representation itself). The core product ingests a veteran's VA C-file / e-folder and (a) reconstructs a date-stamped timeline of every prior final VA decision, the evidence of record at each point, and the law in effect at each point; (b) tests each prior final decision for **Clear and Unmistakable Error (CUE)** under 38 C.F.R. § 3.105(a); (c) argues the **earliest possible effective date**; and (d) produces citation-ready draft instruments (Supplemental Claim, HLR, Board appeal, CUE motion).

The strategic thesis (to be tested, not assumed) is that existing professional tools (Vala, VA Claim Helper/VCH, Caliber/Flagship, claim.vet, and veteran-facing tools like VeteranAi and VetClaims.ai) stop at C-file summarization, condition-spotting, and form-filling, and that **none** performs effective-date reconstruction or CUE detection — leaving that as an open, defensible "wedge." The hardest and most defensible technical asset is claimed to be a **point-in-time regulatory corpus**: versioned 38 C.F.R. (Parts 3, 4, 19, 20) and 38 U.S.C. keyed to effective dates, so the engine can apply and cite the regulation _as it read on the date of the prior decision_.

Key facts asserted in the source spec that this research must independently verify or correct (treat each as a hypothesis with a citation attached, and re-verify currency as of the research date — several are flagged in the spec as "current as of mid-2026, public pages only"):

- **Market/competition:** No professional-facing competitor offers effective-date or CUE analysis (closest is VCH's appeal-deadline tracker). Competitor pricing: VCH ~$33–$150/mo; Caliber free; claim.vet ~$49/mo "Agency" tier; Vala and ClaimClam do not publish pricing. Horizontal legal-AI: Harvey ~$1,200+/seat/mo with ~20-seat minimum; CoCounsel ~$225/user/mo standalone.
- **Buyer population:** ~6,700 fee-charging accredited professionals (~520 claims agents + ~6,200 attorneys, per Federal Register RIN 2900-AR94); an older 2020 CRS report cited ~8,080 attorneys + ~525 agents; the full VA OGC accreditation roster (incl. VSO reps) runs ~15,000. NOVA (National Organization of Veterans' Advocates) reports ~850 members and two ~15-CLE-hour conferences/year.
- **Economics:** VBA reported ~$396.8M in trailing-12-month attorney/agent fees (avg ~$33.1M/mo), all as 20% of past-due benefits. Moving an effective date back ~2 years at 70% (no dependents) is worth ~$43,000; at TDIU/100%, >$47,000/year. Nehmer (38 C.F.R. § 3.816) has driven >$4.6B in retroactive benefits (NVLSP).
- **Data access:** Accredited attorneys/agents get read-only VBMS + Caseflow eFolder Express access (38 C.F.R. §§ 1.600–1.603); the Accredited Representative Portal (per VA.gov, opening to all accredited reps Fall 2025) and "Appoint a Representative 2.0" (100% rollout March 25, 2025) establish POA and eFolder access "within minutes."
- **Regulatory constraints:** Assisting claimants for a fee without accreditation violates 38 U.S.C. § 5904 / 38 C.F.R. § 14.636; the accredited user bears competence/diligence duties (§ 14.632); fee rules (§ 14.636 20% cap + the § 5904/§ 14.636 bar on non-accredited persons receiving claimant fees) make a vendor success/referral fee non-viable, with § 14.632(c)(5) only a general unreasonable-fee backstop [corrected 2026-07-16 per citation-verifier]; C-files carry PII/PHI implicating the Privacy Act, 38 U.S.C. §§ 5701 and 7332, and HIPAA-adjacent duties.
- **Proposed pricing:** per-seat SaaS $150–$400/seat/mo + metered per-analysis "CUE deep-dive" credits; explicitly NOT a success fee. Spec's illustrative revenue: 5% of ~6,700 @ ~$3,000/yr ≈ $1M ARR; 15% ≈ $3M ARR.

Do not take any of the above as established. Confirm, update, or refute each with current primary sources, and flag anything you cannot verify.
</context>

<research_objectives>
Produce findings on FOUR objectives. Treat each as a distinct section.

**1. Technical feasibility.** Can the core engine actually be built with today's technology and data access? Assess, with evidence:

- **Point-in-time regulation corpus (the claimed moat):** Does eCFR / GovInfo / the Federal Register expose _historical, versioned_ 38 C.F.R. (Parts 3, 4, 19, 20) and 38 U.S.C. keyed to effective dates in a machine-ingestible way? How complete/reliable is the version history, and how far back? What is the real effort to build and maintain a point-in-time regulatory graph? Is this genuinely hard/defensible or already partially solved by public datasets or existing legal-data vendors?
- **C-file ingestion:** Realistic path to programmatic or semi-automated ingestion of VBMS/Caseflow eFolder Express content given read-only, per-POA, human-suitability-gated access (§§ 1.600–1.603) and the new Accredited Rep Portal. Is there an API, or is it manual export/OCR of large scanned PDFs? Feasibility and accuracy of OCR + structuring of 1,000–2,000-page mixed-quality C-files.
- **Timeline reconstruction & CUE reasoning:** Feasibility/reliability of GraphRAG + agentic reasoning for (a) building the "what VA knew, and when" evidentiary timeline and (b) applying the three-part CUE test with the two hard constraints (only evidence of record at the time; the version of the regulation then in effect). What is the realistic error profile, and can it be made citation-grounded with no fabricated authorities?
- **Legal corpora for retrieval:** Availability/quality of bulk BVA, CAVC, and Federal Circuit decision corpora for RAG.
- **Security/compliance architecture:** What is required to handle C-file PII/PHI (Privacy Act, §§ 5701/7332, HIPAA-adjacent) and pass a law firm's + VA's security review (encryption, tenant isolation, no-training-on-client-data, access controls).
- Output a blunt **feasibility verdict per component** (Feasible now / Feasible with significant effort / Blocked or unproven), with the binding constraints and unknowns named.

**2. High-level technical strategy + rough-draft roadmap.** Given the feasibility findings, propose:

- A reference architecture (ingestion → OCR/structuring → evidentiary timeline graph → point-in-time law retrieval → CUE-viability reasoning → citation-grounded drafting → human-in-the-loop review), with the major build-vs-buy decisions (LLM providers, OCR, legal-data sources, vector/graph stores).
- An **MVP definition** (the spec proposes F1 timeline, F2 CUE-viability, F3 point-in-time regulation as the wedge) and a phased **rough roadmap** with milestones and rough sequencing (not precise dates): MVP → competitive-parity features → platform. Include the top technical risks and concrete mitigations, and the smallest defensible version that proves the moat.
- Keep it high-level and grounded in the feasibility findings — a strategy brief, not a detailed engineering design.

**3. Marketability to professional VA claim handlers.** Assess demand and go-to-market realism among VA-accredited agents/attorneys (and, separately, non-fee VSO service officers):

- **Verify the wedge:** Independently confirm or refute that no professional-facing competitor currently offers effective-date or CUE analysis. Check gated/demo-only products, recent releases, and any legal-AI VA verticals. This claim is the whole thesis — probe it hard.
- **Pain & willingness to pay:** Evidence that effective-date/CUE work is genuinely high-value, error-prone, and under-automated for this buyer; how professionals currently do it; what they pay for adjacent tools; realistic price sensitivity vs. the proposed $150–$400/seat + credits.
- **Buyer, channels, adoption barriers:** Validate the population sizing and reachability (OGC list, NOVA, boutique/mid firms vs. solo tail); adoption frictions specific to this niche — AI skepticism/trust, malpractice/ethics anxiety, firm security review, integration burden, and the regulatory line that the tool must not be marketed as representation.
- **Competitive durability:** Realistic assessment of whether a legal-AI incumbent (Harvey, CoCounsel) or an existing VA tool could add this feature, and how defensible the point-in-time corpus + integrations + accreditation-credibility moat actually is.

**4. Realistic revenue potential (five perspectives).** Build a grounded revenue/profit model that explicitly resists over-optimism. Anchor every input to a verified figure from Objective 3 (population, pricing, segment mix) and state each assumption. The spec's linear "5–15% penetration → $1–3M ARR" is a starting point to critique, NOT to adopt — it ignores churn, CAC, sales-cycle length, ramp time, and segment differences. Model FIVE named scenarios:

- **Worst case** — adoption stalls / the wedge is neutralized (e.g., a competitor ships CUE, or data access proves impractical); near-floor outcome.
- **Conservative** — slow solo adoption, meaningful churn, long sales cycles, high CAC.
- **Realistic** — the most probable base case given the verified evidence.
- **Optimistic** — strong solo + a few boutique/mid-firm deals, healthy retention.
- **Aggressive / best-case** — rapid penetration + firm site licenses + VSO tier; explicitly label the assumptions that would have to all be true.

For each scenario provide, at minimum: paying-customer count and segment mix (solo/boutique/firm/VSO), blended ACV (seat + credits), gross and net ARR trajectory over ~Year 1 → Year 3, and the key assumptions (penetration %, churn, CAC, ramp). Include a short sensitivity note on the 2–3 variables that most swing the outcome. Keep the total-addressable "found money" framing honest — a large TAM does not equal captured revenue.
</research_objectives>

<verification_and_quality_bar>

- **Cite every non-obvious factual claim** with a specific, retrievable source (primary sources preferred: eCFR/GovInfo, the Federal Register, VA.gov, VBA/OGC data, BVA/NOVA publications, and the CFR/USC sections and cases named above). Prefer primary over secondary.
- **Adversarially verify the load-bearing claims**, especially: (i) "no competitor does effective-date/CUE"; (ii) the fee-rule constraints that kill a success-fee model (§ 14.636 + the § 5904/§ 14.636 accreditation-fee bar; § 14.632(c)(5) is only a general backstop); (iii) the data-access reality (VBMS/eFolder Express + Accredited Rep Portal — API vs. manual); (iv) availability of point-in-time versioned 38 C.F.R.; (v) the $396.8M fee figure and the ~6,700 population; (vi) the case law named in the spec (Nehmer line; _Chisholm v. Collins_; _Hamill v. Collins_) — confirm the cases exist and are stated correctly, or correct them.
- **Distinguish** confirmed fact vs. estimate vs. opinion throughout. Where sources conflict (e.g., population counts), present the range and name the most authoritative source.
- **Flag currency:** several source-spec claims are a mid-2026, public-marketing-page snapshot. Note where a finding depends on something that could have changed and should be re-checked before any launch decision.
- **Grant yourself permission to say "unverified" or "unknown"** rather than guessing. Do not fabricate citations, statutes, cases, figures, or product features.
  </verification_and_quality_bar>

<output_format>
Produce a structured, cited Markdown report:

1. **Executive summary** — the bottom line on each of the four objectives in a few sentences each, plus the single biggest risk and the single biggest unknown.
2. **Technical feasibility** — per-component verdict table (component · verdict · binding constraint · confidence) + narrative.
3. **Technical strategy & rough roadmap** — reference architecture + MVP + phased roadmap + top risks/mitigations.
4. **Marketability** — wedge verification, pain/WTP, buyer/channels/barriers, competitive durability.
5. **Revenue — five scenarios** — a comparison table (scenario · paying customers · segment mix · blended ACV · Year-1/2/3 ARR · key assumptions) followed by a short narrative per scenario and a sensitivity note.
6. **Verification ledger** — a table of the load-bearing claims checked: claim · verdict (confirmed / corrected / unverified) · source. Include any spec figure or citation you corrected.
7. **Open questions & what to re-verify before launch.**
8. **Sources** — full list.
   Lead with the honest verdict, not the optimistic one. If the evidence undercuts the thesis on any objective, say so plainly.
   </output_format>

=== END PROMPT ===
