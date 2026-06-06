You are an expert Claude Code skill author. Build a specialized, user-invocable
deep-research skill that helps a single U.S. military veteran develop a legitimate,
evidence-based strategy for maximizing their VA disability rating and associated
benefits.

<skill_identity>

- name: va-rating-strategy
- purpose: Conduct staged deep research on VA disability — processes, the rating
  schedule, compensation/income per rating, benefits unlocked at each rating tier —
  and synthesize the most effective LEGITIMATE strategies for a specific veteran to
  achieve the maximum rating their conditions support.
- output location: all artifacts written as cited Markdown into the active research
  subject directory (this repo uses one directory per subject).
  </skill_identity>

<core_principle>
The skill must execute THREE phases IN ORDER, with a hard gate between each. It may
not begin a phase until the prior phase's exit criteria are met and explicitly
confirmed. Never skip ahead to strategy before the knowledge base and veteran
profile exist.
</core_principle>

<phase_1 name="Domain Knowledge Base">
<goal>
Before anything else, determine WHAT essential knowledge is required, then gather
it. Do not profile the veteran yet.
</goal>
<steps>

1. Enumerate the essential knowledge domains to research, at minimum:
   - The VA claims process end-to-end (filing, evidence, C&P exams, appeals/HLR/
     supplemental claims, effective dates).
   - The VASRD (38 CFR Part 4) rating schedule and how individual ratings are
     assigned per body system.
   - VA math / combined ratings table (38 CFR 4.25) and the "bilateral factor."
   - Monthly compensation amounts per rating tier and dependent status (current
     year), i.e. income-per-rating.
   - Benefits unlocked at each threshold (e.g. 10/30/50/70/100%, TDIU, SMC,
     healthcare priority groups, dependents/education, property tax, etc.).
   - Concepts that drive higher ratings: secondary service connection,
     presumptive conditions (incl. PACT Act), aggravation, TDIU, SMC.
2. Research each domain using web search and authoritative source fetching.
3. Write findings to `knowledge-base.md` with EVERY claim cited inline to its
   source (prefer va.gov, ecfr.gov/38 CFR, official VA documents; treat forums
   and law-firm blogs as secondary, clearly labeled).
   </steps>
   <accuracy_controls>

- Cite a primary source for every factual claim; if you cannot, mark it
  "UNVERIFIED" rather than stating it as fact.
- Compensation figures and benefit thresholds change yearly — always capture the
  effective year and source URL.
- You are permitted and expected to say "I don't know / not found" instead of
  guessing.
  </accuracy_controls>
  <gate>
  Do NOT proceed to Phase 2 until: (a) all listed domains are covered, (b) every
  claim is cited, and (c) you state your confidence is HIGH. If confidence is not
  high, identify gaps and continue researching.
  </gate>
  </phase_1>

<phase_2 name="Veteran Profile">
<goal>
Using the Phase 1 knowledge to know what matters, build a complete profile of the
specific veteran the strategy is for.
</goal>
<steps>

1. From the knowledge base, derive the full list of facts needed to build a
   strategy (service history, dates and locations of service, MOS/duties,
   exposures, current diagnosed conditions, undiagnosed symptoms, existing
   ratings and claim history, dependents, employment status).
2. Gather these facts by asking the veteran clear, grouped questions. Ask only
   what you cannot already infer; never invent facts about the veteran.
3. Write the result to `veteran-profile.md`. Distinguish CONFIRMED facts (stated
   by the veteran or documented) from INFERRED/ASSUMED items.
   </steps>
   <gate>
   Do NOT proceed to Phase 3 until the profile is sufficient to reason about
   service connection and ratings for each condition. List any missing critical
   facts and request them before continuing.
   </gate>
   </phase_2>

<phase_3 name="Strategy Synthesis">
<goal>
Conduct deep research and synthesize the optimal, legitimate strategy for THIS
veteran to maximize their rating and benefits.
</goal>
<steps>

1. For each of the veteran's conditions, map to the relevant VASRD criteria and
   identify the evidence required to support the highest justified rating.
2. Identify opportunities grounded in the profile: secondary connections,
   presumptive/PACT-Act eligibility, aggravation, TDIU, SMC.
3. Compute the projected combined rating (show the VA-math) and the resulting
   monthly compensation and unlocked benefits.
4. Produce a prioritized, step-by-step action plan: what to file, what evidence to
   gather, which exams to prepare for, and sequencing.
5. Write to `strategy.md`, fully cited, with every recommendation traceable to
   both the knowledge base and the veteran's profile.
   </steps>
   </phase_3>

<ethics_guardrail>
The objective is the MAXIMUM rating the veteran's genuine conditions LEGITIMATELY
support — accurate documentation, lawful claims, and full use of entitled programs.
Never advise fabricating, exaggerating, or misrepresenting conditions, symptoms, or
service history. Include a disclaimer that this is research assistance, not legal/
medical advice, and recommend consulting an accredited VSO or VA-accredited
attorney.
</ethics_guardrail>

<skill_requirements>

- Frontmatter: user-invocable; a description that triggers on "VA disability
  strategy", "maximize VA rating", "veteran benefits research".
- Reuse this repo's existing tooling: `deep-research` for fan-out research,
  `source-capture` for archiving sources, `new-subject` for scaffolding.
- Keep the three-phase gated structure and citation discipline explicit in the
  SKILL.md body.
- Reference authoritative sources (va.gov, 38 CFR) over secondary commentary.
  </skill_requirements>

Now generate the complete skill, including SKILL.md frontmatter and body.
