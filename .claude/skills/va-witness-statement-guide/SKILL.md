---
name: va-witness-statement-guide
description: Generate an open-ended question list — never narrative text or example wording — to help a buddy, spouse, or lay witness write their own VA Form 21-10210 statement in their own words. Use when a witness needs help getting started, when gaps are identified in an existing witness draft, or when asked to "help X write their statement", "what should I ask [witness] about", or "give an example of what to say". This skill is structurally incapable of producing narrative/example content by design.
disable-model-invocation: true
---

# VA Witness Statement Guide

Turn a list of evidentiary gaps or topics into **questions**, never into example prose. This
skill exists because "just give an example, we'll phrase it ourselves" is a request that's
already come up in this claim, and the honest answer is that an example _is_ the coaching
problem, regardless of the label on it — see the Hard Constraint below before doing
anything else.

## When to use this

- A witness (buddy, spouse) is starting a statement from scratch and needs a prompt.
- `va-corpus-sync` or `claim-consistency-checker` identified gaps in an existing witness
  draft (missing topics, unresolved date conflicts) that the witness — not the veteran —
  needs to resolve.
- Someone asks for "an example" or "a draft to go by" for a witness statement. Redirect to
  this skill's output instead of complying with the literal request.

## Hard constraint — read this first, every time

**Output is a list of questions. Full stop. No declarative sentences describing events,
symptoms, or observations — even hedged, even labeled "example," even offered as
something to "just phrase in your own words."**

Why this is absolute rather than a judgment call: the specific mechanism that created
this claim's single biggest documented credibility risk (`CLAIM-ASSESSMENT.md` §0.2) was
an AI/veteran-produced draft that the witness then edited — the manipulative instructions
layered on top were what got caught, but the underlying mechanism (facts originating from
someone with a stake in the claim, not from the witness's own memory) is the actual
problem, and it survives even a well-intentioned "for tone and structure only" framing.
An example sentence about what someone might have witnessed is not meaningfully different
from a draft — both hand the witness content to react to instead of a blank page to fill
from memory.

If asked directly for an example, decline and explain this, then offer the question list
instead — this is the same handling this repo's own agents (`claim-consistency-checker`)
and skills (`va-rating-strategy`, `va-rating-reassess`) already use.

## Steps

### 1. Gather the topics

From `va-corpus-sync`, `claim-consistency-checker`, or direct instruction: what are the
specific gaps, missing topics, or unresolved inconsistencies this witness could address?
Ground every topic in something concrete — a rating-criteria symptom category, a specific
date conflict, a piece of corroboration another document is missing — not a generic
"tell us more."

### 2. Convert each topic into one or more open questions

Rules for a good question:

- It asks **whether** something happened and, if so, **what it looked like** — it never
  asserts the thing happened.
- It's specific enough to jog a real memory ("have you ever heard him snore loudly, stop
  breathing, or gasp in his sleep?") rather than vague ("tell me about his sleep").
- It doesn't embed the answer or a suggested severity ("how severe was it?" is fine; "he
  was very distressed, right?" is not).
- Where a factual cross-check is involved (e.g. a date conflict with another document),
  ask the witness to state what they actually recall, not which of two dates is "correct."

### 3. Present the list with a framing note

Always include, verbatim or close to it: _"Answer only what's actually true and something
you personally witnessed. Skip anything that doesn't apply or that you don't recall —
there's no requirement to cover every question."_

### 4. Do not follow up by drafting from their answers into "publishable" prose

If the witness answers these questions back to you in conversation, your job stops at
organizing their own words into the right form section (Section III of VA Form 21-10210) —
reorder and format, but do not rephrase their factual content, embellish it, or make it
"read better." If their phrasing is awkward, that's fine; awkward-but-genuine outperforms
polished-but-borrowed for credibility purposes, and this repo's existing guidance says so
explicitly (`CLAIM-ASSESSMENT.md`, `Spouse_Statement_Guide_Erica`).

## Example (format, not content, to be reused)

> - _Sleep:_ Have you ever heard him snore loudly, stop breathing, gasp, or choke in his
>   sleep? Roughly how often, and for how long has this been happening?
> - _[Topic]:_ Have you noticed \[specific behavior\]? What does that look like when it
>   happens? How often?
> - _[Date conflict]:_ Do you remember anything from around \[timeframe\]? What's your own
>   recollection of what happened then, if anything?

## Ethics & legal guardrails (identical in force to `/va-rating-strategy`)

- Witness statements are signed under penalty of perjury; a coached statement is the
  paradigm case of VA benefits fraud (18 U.S.C. § 1001) and cross-contaminates the whole
  claim's credibility — this is why the constraint above is non-negotiable, not merely
  cautious.
- Never tell a witness what to emphasize, omit, or align with another account.
- If the witness's own answers reveal a new inconsistency with the rest of the corpus,
  report it (via `va-corpus-sync`/`claim-consistency-checker`) rather than smoothing it
  over in the reformatting step.
