---
name: va-rating-strategy
description: Deep-research workflow to help a U.S. military veteran legitimately maximize their VA disability rating and benefits. Use for VA disability strategy, maximize VA rating, veteran benefits research, VA rating odds, C&P exam prep, TDIU/SMC eligibility, or building a ranked directory of VSOs and VA-accredited attorneys. Runs four gated phases — knowledge base, veteran profile, strategy+odds, resources — with strict citation discipline.
disable-model-invocation: true
---

# VA Rating Strategy

Staged deep research that helps a single U.S. military veteran develop a
legitimate, evidence-based strategy for maximizing their VA disability rating and
the benefits tied to it — including the **odds** of attaining each rating, how to
**optimize** those odds, and a **ranked, sourced directory** of help.

## Purpose

Produce four cited Markdown artifacts inside the active research subject directory:

1. `knowledge-base.md` — the domain facts the strategy depends on
2. `veteran-profile.md` — the specific veteran's situation
3. `strategy.md` — per-condition strategy, odds, and optimization levers
4. `resources.md` — free and paid help, ranked and substantiated

## Current Case State — Read Before Running (updated 2026-07-05)

This skill originally produced the four base artifacts. Much has changed since. **Before
running any phase, read `va-disability/COMPREHENSIVE-FINDINGS-2026-07.md` in full** — it is
the current source of truth and it explicitly supersedes parts of `veteran-profile.md` and
`strategy.md`. Do not treat the older four artifacts as authoritative where the findings doc
corrects them. Key items any rating strategy now must account for (not exhaustive — read the doc):

- **A confirmed clinical OCD diagnosis (F42.2)** missing from the personal statement and C&P
  prep. Its VA diagnostic code is **9404** (verified against 38 CFR 4.130 via Cornell LII /
  eCFR, 2026-07-05; DC **9403** is specific/social phobia, not OCD). OCD is rated under the
  same § 4.130 General Rating Formula as PTSD/MDD/GAD, so it folds into the single mental-health
  rating (anti-pyramiding) rather than adding separately — but its documented symptoms
  strengthen the overall severity picture.
- **A credibility risk** where a spouse's draft statement was found to have been directively
  coached. See the guardrails below — this changes how this skill may ever touch witness evidence.
- **A conflict** between the MST stressor narrative and a 2015 VA record containing an explicit
  MST denial and all-negative screens, repeated as "trauma denied" across most intakes through 2024. This must be affirmatively addressed with delayed-disclosure literature, not left silent.
- **A weaker-than-assumed iatrogenic-opioid-onset theory** (age-18 pre-service first use in the
  record); lead instead with the _Allen v. Principi_ secondary-to-PTSD/MDD/GAD theory.
- **An unexplained "Amphetamine-type SUD, Severe" diagnosis** with zero supporting documentation.
- **A materially deteriorated employment picture** that may change the 100%-schedular-vs-TDIU
  analysis (the prior June 2026 deep-research put 100% schedular at only 10–15%, contingent on
  genuine, undirected, contemporaneously-documented decline — never anything manufactured).

For an ad-hoc strategic re-analysis that does **not** require rebuilding all four artifacts from
scratch (e.g., "given these new facts, what's my realistic ceiling now, and what should I do?"),
use the companion **`/va-rating-reassess`** skill instead of re-running this full workflow.

## Required tooling — verify before you assert

- **`citation-verifier` subagent:** run it on **every** legal/CFR/case-law/USC/Federal-Register
  citation before you present it as fact in any artifact. 40 of 109 citations in the prior
  research were misstated; do not repeat them. Never state a citation as confirmed on the strength
  of training data alone.
- **`claim-consistency-checker` subagent:** run it before finalizing any claim-facing document
  (personal statement, 21-0781, buddy/spouse statement, nexus-letter guide) to catch factual
  drift across the corpus.
- **Internet currency (non-negotiable):** do **not** reason from training data for anything
  year-specific — compensation rates, SMC/DEA/poverty thresholds, dollar figures, CFR text,
  proposed-rule/docket status, appeal-docket timelines. Confirm each against a current primary
  source (va.gov, ecfr.gov / law.cornell.edu, govinfo.gov, the Federal Register) at run time,
  and record the effective year + source URL. When in doubt, say "not found / not confirmed."

## Core Principle — Four Gated Phases

Execute the phases **in order**. Do **not** start a phase until the prior phase's
exit gate is met and explicitly confirmed. Never jump to strategy or resources
before the knowledge base and veteran profile exist.

Use the repo's existing tooling throughout:

- `deep-research` — fan-out web search + adversarial verification
- `source-capture` — archive sources/reviews into the subject's `sources/`
- `iterative-retrieval` — multi-pass gathering for the resource directory
- `/new-subject` — scaffold the subject directory if one does not exist yet

---

## Phase 1 — Domain Knowledge Base

**Goal:** Decide WHAT essential knowledge is required, then gather it. Do not
profile the veteran yet.

**Steps**

1. Enumerate the essential knowledge domains, at minimum:
   - VA claims process end-to-end (filing, evidence, C&P exams, DBQs,
     appeals / Higher-Level Review / supplemental claims, effective dates).
   - VASRD (38 CFR Part 4) rating schedule; how ratings are assigned per body system.
   - VA math / combined ratings table (38 CFR 4.25) and the "bilateral factor."
   - Monthly compensation per rating tier and dependent status (current year).
   - Benefits unlocked at each threshold (10/30/50/70/100%, TDIU, SMC, healthcare
     priority groups, dependents/education, property tax, etc.).
   - Rating-driving concepts: secondary service connection, presumptives
     (incl. PACT Act), aggravation, TDIU, SMC.
   - Evidence types that move outcomes: nexus letters, DBQs, buddy/lay statements,
     private medical opinions — and how each affects success.
   - Representation rules and fee law (VSOs free; 38 CFR 14.636 fee limits; no fees
     for initial claims).
2. Research each domain via web search + authoritative source fetching.
3. Write `knowledge-base.md` with EVERY claim cited inline. Prefer va.gov,
   ecfr.gov / 38 CFR, GAO and VA OIG data; label forums and law-firm blogs as
   secondary.

**Accuracy controls**

- Cite a primary source for every factual claim; otherwise mark it `UNVERIFIED`.
- Capture the effective **year** + source URL for every dollar figure and threshold.
- You are permitted and expected to say "not found" rather than guess.

**Gate:** Proceed only when all domains are covered, every claim is cited, and you
state confidence is **HIGH**. Otherwise list the gaps and keep researching.

---

## Phase 2 — Veteran Profile

**Goal:** Using Phase 1 to know what matters, build a complete profile of the
specific veteran.

**Steps**

1. From the knowledge base, derive the full fact list a strategy needs: service
   history, dates/locations of service, MOS/duties, exposures, current diagnosed
   conditions, undiagnosed symptoms, existing ratings and claim history, dependents,
   employment status, medical documentation on hand, and the veteran's **chosen
   location(s)** for resource/representation purposes.
2. Gather facts by asking the veteran clear, grouped questions. Ask only what you
   cannot infer; **never invent facts** about the veteran.
3. Write `veteran-profile.md`, clearly distinguishing **CONFIRMED** facts from
   **INFERRED/ASSUMED** items.

**Gate:** Proceed only when the profile is sufficient to reason about service
connection and ratings for each condition. List any missing critical facts and
request them first.

---

## Phase 3 — Strategy, Odds & Optimization

**Goal:** Synthesize the optimal legitimate strategy, with explicit probability of
success per opportunity and how to raise it.

**Steps**

1. For each condition, map to the relevant VASRD criteria and identify the evidence
   required to support the highest justified rating.
2. Identify opportunities grounded in the profile: secondary connections,
   presumptive / PACT-Act eligibility, aggravation, TDIU, SMC.
3. **Odds.** For each claimed rating/percentage, estimate the likelihood of
   attainment:
   - Express as a band (Low / Moderate / High / Very High) **and**, where
     defensible data exists, an approximate percentage.
   - State the **basis**: strength of nexus, documentation, alignment with VASRD
     criteria, presumptive status, published grant-rate data if found.
   - **Label** every estimate as `DATA-BACKED (source)` or
     `REASONED ESTIMATE — not statistically derived`. Never present an invented
     number as a statistic.
4. **Odds optimization.** For each opportunity, list concrete levers that raise the
   probability — strong nexus letter, the correct DBQ, buddy/lay statements,
   treating + documenting symptoms before the C&P exam, filing fully developed
   claims, ordering conditions to leverage VA math. Tie each lever to _why_ it helps
   (cite Phase 1 where possible).
5. Compute the projected combined rating (**show the VA-math**), resulting monthly
   compensation, and unlocked benefits — for both a **conservative** and an
   **optimized** scenario.
6. Produce a prioritized, sequenced action plan: what to file, evidence to gather,
   exams to prepare for, and order of operations (highest expected value first).
7. Write `strategy.md`, fully cited, every recommendation traceable to both the
   knowledge base and the veteran's profile.

**Gate:** Proceed only when each opportunity has an odds band, a stated basis, and
at least one optimization lever.

---

## Phase 4 — Resources & Representation Directory

**Goal:** Build a vetted, sourced directory of resources the veteran can use to
obtain their rating — free and paid.

**Steps**

1. **Free / low-cost resources:**
   - Accredited Veterans Service Organizations (VSOs) — DAV, VFW, American Legion,
     state veterans affairs offices. Note that VSO claim help is **free**.
   - Free online tools, calculators, informational services (flag any with a
     commercial upsell).
   - VA-run resources (VA.gov, Vet Centers, help obtaining medical documentation).
2. **Paid representation** — attorneys and accredited claims agents who specialize
   in maximizing veteran ratings:
   - Verify **VA accreditation** (search VA's accreditation database) and record it.
   - Gather **evidence of effectiveness**: cited client reviews (Google, Avvo, BBB,
     Trustpilot), published success/grant rates if any, and disciplinary records.
   - **Rank by effectiveness** using explicit, stated criteria (e.g. weighted blend
     of review volume + rating, documented outcomes, accreditation, specialization
     depth). Show the criteria and each entry's score/rationale.
   - Record every claim with a source link; mark anything unsourced as `UNVERIFIED`
     and exclude it from the ranking.
3. **Location scope:** Default to **nationwide** coverage (VA-accredited reps can
   represent veterans in any state), but **specialize** toward the veteran's chosen
   location(s) from the profile — surface and rank local/in-state options first,
   then nationwide. Flag state-specific resources and benefits separately (state
   benefits and property-tax rules vary). If location(s) are unknown, ask before
   finalizing.
4. Write `resources.md` with ranked tables: free resources, location-specialized
   paid reps, and nationwide paid reps — each row carrying its citations.

**Gate:** Every ranked entry must have at least one cited, dated source and (for
paid reps) a verified accreditation status.

---

## Ethics & Legal Guardrails

- The objective is the **maximum rating the veteran's genuine conditions
  legitimately support** — accurate documentation, lawful claims, full use of
  entitled programs.
- **Never** advise fabricating, exaggerating, or misrepresenting conditions,
  symptoms, or service history.
- **Never** present an invented number as a statistic.
- **Never coach witness evidence.** Do not draft, script, reword, or suggest framing
  for any buddy, spouse, or lay statement, and never tell a witness what to emphasize,
  omit, or align with another account. Witness statements (VA Form 21-10210 / 21-4138)
  are signed under penalty of perjury; a coached statement is the paradigm case of VA
  benefits fraud (18 U.S.C. § 1001) and would cross-contaminate the credibility of the
  entire claim. You may **identify** a credibility risk or a consistency gap and hand it
  to the veteran — resolution belongs to the veteran and the actual witness, in their own
  unedited words. This mirrors the hard rule in the `claim-consistency-checker` subagent.
- **Genuine decline only.** Any argument for a higher rating (including any 100%-schedular
  or TDIU path) must rest on genuine, undirected, contemporaneously-documented functional
  decline — never anything manufactured, backdated, or coached. If the evidence is not
  already there, the answer is to build legitimate documentation over time, not to inflate.
- Note VA fee rules: VSOs are free; attorneys cannot charge for initial claims;
  fees are regulated under **38 CFR 14.636**.
- Always include the disclaimer: _this is research assistance, not legal or medical
  advice; consult an accredited VSO or VA-accredited attorney before acting._
