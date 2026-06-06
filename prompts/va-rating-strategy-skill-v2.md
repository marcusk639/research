You are an expert Claude Code skill author. Build a specialized, user-invocable
deep-research skill that helps a single U.S. military veteran develop a legitimate,
evidence-based strategy for maximizing their VA disability rating and benefits —
including the ODDS of achieving each rating, how to OPTIMIZE those odds, and a
ranked, sourced directory of RESOURCES that can help them get there.

<skill_identity>

- name: va-rating-strategy
- purpose: Staged deep research on VA disability — processes, the rating schedule,
  compensation/income per rating, benefits per tier — plus per-condition probability
  modeling and a vetted resource/representation directory, culminating in the most
  effective LEGITIMATE strategy for a specific veteran.
- output location: cited Markdown artifacts written into the active research subject
  directory (this repo uses one directory per subject).
  </skill_identity>

<core_principle>
Execute FOUR phases IN ORDER, with a hard gate between each. Do not begin a phase
until the prior phase's exit criteria are met and explicitly confirmed. Never jump
to strategy or resources before the knowledge base and veteran profile exist.
</core_principle>

<phase_1 name="Domain Knowledge Base">
<goal>Determine WHAT essential knowledge is required, then gather it. Do not
profile the veteran yet.</goal>
<steps>

1. Enumerate essential knowledge domains, at minimum:
   - VA claims process end-to-end (filing, evidence, C&P exams, DBQs,
     appeals/HLR/supplemental claims, effective dates).
   - VASRD (38 CFR Part 4) rating schedule; how ratings are assigned per body system.
   - VA math / combined ratings table (38 CFR 4.25) and the "bilateral factor."
   - Monthly compensation per rating tier and dependent status (current year).
   - Benefits unlocked at each threshold (10/30/50/70/100%, TDIU, SMC, healthcare
     priority groups, dependents/education, property tax, etc.).
   - Rating-driving concepts: secondary service connection, presumptives (incl.
     PACT Act), aggravation, TDIU, SMC.
   - Evidence types that move outcomes: nexus letters, DBQs, buddy statements,
     private medical opinions, lay evidence, and how each affects success.
   - Representation rules and fee law (VSOs free; 38 CFR 14.636 fee limits; no fees
     for initial claims).
2. Research each domain via web search + authoritative source fetching.
3. Write findings to `knowledge-base.md` with EVERY claim cited inline (prefer
   va.gov, ecfr.gov/38 CFR, GAO/VA OIG data; label forums and law-firm blogs as
   secondary).
   </steps>
   <accuracy_controls>

- Cite a primary source for every factual claim; otherwise mark "UNVERIFIED".
- Capture the effective year + source URL for all dollar figures and thresholds.
- You are permitted and expected to say "not found" rather than guess.
  </accuracy_controls>
  <gate>Proceed only when all domains are covered, every claim is cited, and you
  state confidence is HIGH. Otherwise list gaps and keep researching.</gate>
  </phase_1>

<phase_2 name="Veteran Profile">
<goal>Using Phase 1 to know what matters, build a complete profile of the specific
veteran.</goal>
<steps>

1. Derive the full fact list a strategy needs (service history, dates/locations,
   MOS/duties, exposures, current diagnosed conditions, undiagnosed symptoms,
   existing ratings and claim history, dependents, employment status, current
   medical documentation on hand, and the veteran's chosen location(s) for
   resource/representation purposes).
2. Gather by asking the veteran clear, grouped questions. Ask only what cannot be
   inferred; never invent facts about the veteran.
3. Write to `veteran-profile.md`, distinguishing CONFIRMED facts from
   INFERRED/ASSUMED items.
   </steps>
   <gate>Proceed only when the profile is sufficient to reason about service
   connection and ratings for each condition. List missing critical facts and request
   them first.</gate>
   </phase_2>

<phase_3 name="Strategy, Odds & Optimization">
<goal>Conduct deep research and synthesize the optimal legitimate strategy, with
explicit probability of success per opportunity and how to raise it.</goal>
<steps>

1. For each condition, map to the relevant VASRD criteria and identify the evidence
   required to support the highest justified rating.
2. Identify opportunities grounded in the profile: secondary connections,
   presumptive/PACT-Act eligibility, aggravation, TDIU, SMC.
3. ODDS: For each claimed rating/percentage, estimate the likelihood of attainment.
   - Express as a band (e.g. Low / Moderate / High / Very High) AND, where
     defensible data exists, an approximate percentage.
   - State the BASIS for each estimate: strength of nexus, documentation, alignment
     with VASRD criteria, presumptive status, published grant-rate data if found.
   - LABEL every estimate as "DATA-BACKED (source)" or "REASONED ESTIMATE — not
     statistically derived." Never present an invented number as a statistic.
4. ODDS OPTIMIZATION: For each opportunity, list concrete levers that raise the
   probability — e.g. obtaining a strong nexus letter, completing the correct DBQ,
   securing buddy/lay statements, treating + documenting symptoms before the C&P
   exam, filing fully developed claims, ordering conditions to leverage VA math.
   Tie each lever back to how/why it improves odds (cite Phase 1 where possible).
5. Compute the projected combined rating (show the VA-math), resulting monthly
   compensation, and unlocked benefits — for both a conservative and an optimized
   scenario.
6. Produce a prioritized, sequenced action plan: what to file, evidence to gather,
   exams to prepare for, and order of operations (highest expected value first).
7. Write to `strategy.md`, fully cited, every recommendation traceable to both the
   knowledge base and the veteran's profile.
   </steps>
   <gate>Proceed only when each opportunity has an odds band, a stated basis, and at
   least one optimization lever.</gate>
   </phase_3>

<phase_4 name="Resources & Representation Directory">
<goal>Build a vetted, sourced directory of resources the veteran can use to obtain
their rating — free and paid.</goal>
<steps>

1. FREE / LOW-COST resources:
   - Accredited Veterans Service Organizations (VSOs) — DAV, VFW, American Legion,
     state veterans affairs offices — note that VSO claim help is FREE.
   - Free online tools, calculators, and informational services (label any with a
     commercial upsell).
   - VA-run resources (eBenefits/VA.gov, Vet Centers, VA medical documentation help).
2. PAID representation — attorneys and accredited claims agents who specialize in
   maximizing veteran ratings:
   - Verify VA accreditation (search VA's accreditation database) and note it.
   - For each, gather EVIDENCE of effectiveness: cited client reviews (Google,
     Avvo, BBB, Trustpilot), reported success/grant rates if published, and any
     disciplinary records.
   - RANK by effectiveness using explicit, stated criteria (e.g. weighted blend of
     review volume + rating, documented outcomes, VA accreditation, specialization
     depth). Show the criteria and each entry's score/rationale.
   - Record every claim with its source link; mark anything unsourced as
     "UNVERIFIED" and exclude it from the ranking.
3. LOCATION SCOPE: Default to nationwide coverage (VA-accredited reps can represent
   veterans in any state), but SPECIALIZE the directory toward the veteran's chosen
   location(s) from the profile — surface and rank local/in-state options first,
   then nationwide options. Always flag state-specific resources and benefits
   separately (state benefits and property-tax rules vary). If the veteran has not
   specified location(s), ask before finalizing this phase.
4. Write to `resources.md` with ranked tables: free resources, location-specialized
   paid reps, and nationwide paid reps — each row carrying its citations.
   </steps>
   <gate>Every ranked entry must have at least one cited, dated source and (for paid
   reps) a verified accreditation status.</gate>
   </phase_4>

<ethics_guardrail>
The objective is the MAXIMUM rating the veteran's GENUINE conditions LEGITIMATELY
support — accurate documentation, lawful claims, full use of entitled programs.
Never advise fabricating, exaggerating, or misrepresenting conditions, symptoms, or
service history. Do not present invented numbers as statistics. Note VA fee rules
(VSOs are free; attorneys cannot charge for initial claims; fees are regulated under
38 CFR 14.636). Include a disclaimer: this is research assistance, not legal/medical
advice; recommend consulting an accredited VSO or VA-accredited attorney.
</ethics_guardrail>

<skill_requirements>

- Frontmatter: user-invocable; description triggering on "VA disability strategy",
  "maximize VA rating", "veteran benefits research", "VA rating odds".
- Reuse repo tooling: deep-research (fan-out + verification), source-capture
  (archive reviews/sources), iterative-retrieval (resource gathering), new-subject
  (scaffolding).
- Keep the four-phase gated structure, odds-labeling discipline, and citation rules
  explicit in the SKILL.md body.
- Prefer authoritative sources (va.gov, 38 CFR) for facts; for attorney rankings,
  require multiple cited reviews per entry.
  </skill_requirements>

Now generate the complete skill, including SKILL.md frontmatter and body.
