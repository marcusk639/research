---
name: nexus-letter-evaluator
description: Evaluate a nexus letter, treating-provider medical opinion, or DBQ for a VA disability claim on its CONTENT — not surface polish — against three things at once: the legal requirements of a nexus opinion, the criteria of the rating tier being sought, and the claim's ACTUAL available supporting evidence. Use to grade a provider's letter, find why it under-supports the target rating, and identify what genuine content would strengthen it. Produces strengths / weaknesses / improvements / additions and a split content grade (service-connection vs target-rating). Companion to /va-rating-reassess (odds) and the citation-verifier / claim-consistency-checker agents.
disable-model-invocation: true
---

# Nexus Letter Evaluator

Grade a nexus letter / provider medical opinion / DBQ on **content** — its evidentiary and
legal substance toward the claim's goals — and say concretely how to make it stronger with
**genuine** content. This is an evaluation tool, not a drafting tool: it never writes the
clinician's opinion for them and never suggests reaching past their honest judgment.

## What this evaluates (and what it deliberately ignores)

- **Evaluates:** whether the letter (1) legally establishes **service connection** (nexus),
  and (2) supports the **specific rating tier being sought** — measured against the claim's
  **actual available supporting evidence**, not against an ideal.
- **Ignores (by design):** easily-correctable surface errors — wrong DOB, misspelled name,
  phone/typo, a diagnosis dropped from a header line. Note them in one line for a separate
  clean-up list; they are not what the grade is about. Say so explicitly so the grade isn't
  confused with proofreading.

## When to use

- "Grade / evaluate / critique this nexus letter (or DBQ, or IMO)."
- "Is this letter strong enough for [target rating]?"
- "What's missing from this provider opinion to get us to 100% / 70% / secondary connection?"
- After a provider letter arrives, before it's submitted — to catch under-support and
  over-reach while there's still time to supplement.

## Inputs to establish first

1. **The document** to evaluate (the letter / DBQ / opinion), read in full.
2. **The target** — what rating tier or connection theory is being sought (e.g., 100% schedular
   MH under 4.130; a secondary connection under 3.310). If unstated, ask.
3. **The claim's available supporting evidence** — the case corpus / records / instruments /
   other statements the letter's assertions can (or can't) be backed by.

## Steps

### 1. Build the two rubrics (general knowledge — verify, don't assume)

- **Legal nexus requirements:** a competent diagnosis; a stressor/in-service event or a
  service-connected primary (for secondaries); the "**at least as likely as not** (50% or
  greater)" standard, stated explicitly; a stated rationale/basis. For MH, both the **direct**
  and, where relevant, **aggravation** (38 CFR 3.306) and **secondary** (3.310) theories.
- **Target-rating criteria:** pull the exact tier language (e.g., 38 CFR 4.130 — 100% = "total
  occupational **AND** social impairment," with its example symptoms; 70% = "deficiencies in
  most areas"). Read the general knowledge base first
  (`~/dev/veteran-disability-ai-resources/knowledge-base/` if present); confirm CFR/tier text
  against primary sources (ecfr.gov / law.cornell.edu) — do not rely on memory for tier text.
- **Verify every legal citation** via a `citation-verifier` agent (or primary-source lookup)
  before treating it as fact.

### 2. Extract every assertion from the document

Diagnoses, the stressor/nexus, the causal theory, each impairment claim (occupational,
social), each symptom, each severity/frequency statement, and the conclusion. List them —
you are going to test each one.

### 3. Evidence-backing check (the core of this skill)

For **each** impairment/symptom/causation assertion, ask: **is it backed by the claim's
available evidence?**

- **Backed** — records/instruments/other statements corroborate it → strength.
- **Asserted but unbacked** — the letter claims it, nothing else in the record supports it →
  **over-reach risk** (a rater who notices discounts the whole letter). Flag it.
- **Evidence exists but the letter omits it** — the record supports a stronger or
  tier-matching point the letter didn't make → **missed opportunity** (the highest-value fixes
  usually live here).

### 4. Legal-and-tier sufficiency check

- Nexus standard stated correctly? Actual diagnosis vs. assumed? Stressor/primary identified?
- **Both prongs** addressed (for MH, occupational **AND** social — not just "can't work")?
- **Frequency / severity / duration** given, or just symptom presence? (_Vazquez-Claudio_ —
  symptoms must be shown to **cause** the tier's impairment, not merely exist.)
- **Tier-matching symptoms** present for the target tier? (e.g., for 4.130 100%: the letter's
  symptoms map to the 100% examples, or only to 70% and below?)
- **Internal contradictions** that undercut the target (e.g., "total occupational impairment"
  next to "obsessive overworking")? Flag every one — they are the most exploitable lines.

### 5. Over-reach / credibility check

Does the letter claim more than the evidence or the clinician's genuine judgment supports? An
over-reached letter is _worse_ than an accurate one — it invites a rater to discount
everything. Flag anything that reads as reaching, and note that the fix is accuracy, not
softening a genuinely-supported strong claim.

### 6. Grade — split by purpose

Give a content grade, split because a letter can be excellent at one and weak at the other:

- **As a service-connection (nexus) instrument:** X / 10.
- **As a driver of the target rating:** Y / 10.
- **Overall content:** ≈ Z / 10, with a one-sentence basis.

Label the basis; never present an invented number as a statistic. Be realistic — do not
inflate. If the letter supports 70% but not 100%, say exactly that.

### 7. Report

Produce, in this order:

- **Overall grade** (the split table) + one-sentence verdict.
- **Strengths** — what makes it work, concretely.
- **Weaknesses** — what limits it toward the target, each tied to a specific line and the
  doctrine it implicates.
- **Improvements** — to content already present (convert assertion→demonstration, reconcile
  contradictions, strengthen causal language).
- **Additions toward the target** — genuine content that would raise it, **only if the record
  and the clinician's honest judgment support it** — the tier-matching symptoms, the missing
  prong, a DBQ with the global-impairment box + narrative, etc.
- **The highest-leverage moves**, in order.

Run `claim-consistency-checker` if the letter's facts touch the rest of the claim file.

## Ethics & legal guardrails (identical in force to /va-rating-strategy)

- **This is an evaluation, never a drafting tool for the provider's opinion.** Never write,
  script, or suggest the clinician's conclusions or letter wording. Every "addition" is framed
  as _content the clinician would supply in their own genuine judgment if it is true_ — not
  language to insert.
- **Grade accuracy and sufficiency, never persuasiveness.** A letter is not "better" for
  claiming more; it is better for being accurate, evidence-backed, and legally complete.
  Reward honesty; penalize over-reach.
- **Never advise fabricating, exaggerating, backdating, or misrepresenting** conditions,
  symptoms, severity, or history. Additions must be genuinely true and genuinely supportable.
- **Never coach witness statements** — if the letter's gaps implicate lay-witness evidence,
  identify the gap; do not draft the witness's words (hand to /va-witness-statement-guide).
- **Verify every legal/CFR/case citation** via `citation-verifier` before presenting it as
  fact — this ecosystem's history includes 40 of 109 citations misstated in one prior pass.
- Always close with: _this is research assistance, not legal or medical advice; consult an
  accredited VSO or VA-accredited attorney, and the treating clinician exercises their own
  independent judgment._
