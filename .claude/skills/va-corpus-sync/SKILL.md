---
name: va-corpus-sync
description: Synthesize a new or updated document (buddy letter, spouse statement, medical record, blog draft, strategy note, etc.) into the va-disability/ corpus — extract facts, cross-reference against COMPREHENSIVE-FINDINGS and the current working docs, run consistency/citation checks, and propose (never auto-apply) updates. Use when a new document lands in personal-records/, ClaudeDisabilityAssets/, or va-disability/ and needs to be reconciled with the existing claim corpus, or when asked to "sync this into the corpus", "check this new document against everything else", or "what does this new file change".
disable-model-invocation: true
---

# VA Corpus Sync

Take one new or edited document and reconcile it against the rest of the `va-disability/`
corpus — without ever drafting or editing anyone else's wording. This is the tool for
"a new document just showed up, what does it mean for everything else."

**Companion tools:** `citation-verifier` and `claim-consistency-checker` (repo agents) do
the actual checking; this skill decides when to call them and what to do with the result.
`va-witness-statement-guide` (skill) is what to hand off to if the new document is an
unfinished witness statement that needs help, rather than a finished one to check.

## When to use this vs. the other VA skills

- A **new document** exists and you want to know what it changes → **this skill**.
- You want a fast **status snapshot** of the whole claim → `/va-claim-status`.
- You want a **strategic re-analysis** of odds/ceiling given new facts → `/va-rating-reassess`.
- You're building the **four base artifacts from scratch** → `/va-rating-strategy`.
- A witness needs help **starting** their own statement → `/va-witness-statement-guide`.

## Steps

### 1. Read the document and classify it

Read the new/changed file in full. Classify it into one of:

- **Witness statement** (buddy/spouse/lay statement, any draft or final stage) — a
  document where someone other than the veteran is the declarant.
- **Veteran's own statement** (personal statement, 21-0781, CPT/trauma-impact worksheet,
  any first-person account by the veteran themself).
- **Clinical/official record** (treatment record, DD-214, VA correspondence, C&P exam
  report).
- **Strategy/synthesis document** (anything in `va-disability/*.md` that's analysis, not
  evidence).
- **Non-claim-facing draft** (e.g. a blog post) — still worth checking for factual
  consistency with the claim record, but never treat it as claim evidence itself, and say
  so explicitly if it's ever proposed as dual-purpose.

The classification matters because it determines what you're allowed to do with the
content in step 4 — see the hard rule there.

### 2. Extract the facts that matter

Pull out: dates, diagnoses, employment/financial facts, disclosure timing, unit/facility/
provider names, severity language, and anything asserted as fact (not opinion). This is
the same category of fact `claim-consistency-checker` cross-references — see its
definition for the full list.

### 3. Cross-reference against the current corpus

Read the latest `COMPREHENSIVE-FINDINGS-*.md` first — it's the source of truth for facts
already reconciled. Then check the document against:

- The current working docs (`MASTER-STRATEGY.md`, `CLAIM-ASSESSMENT.md`,
  `100-PERCENT-SCHEDULAR-PATHWAY.md`, `NEXUS-LETTER-GUIDE-CHERIE.md`,
  `CP-EXAM-PREP-MENTAL-HEALTH.md`, `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`).
- Other documents of the same type (e.g. a new buddy letter against the existing ones) —
  independent corroboration is good; near-identical phrasing across "independent"
  witnesses is itself a finding worth flagging (coordination risk), not something to
  ignore because it happens to help.

**Dispatch the subagents rather than eyeballing it yourself:**

- Any legal/CFR/case/USC/Federal-Register citation in the new document →
  `citation-verifier`. Never present a citation as confirmed on your own read.
- Any claim-facing document (personal statement, 21-0781, buddy/spouse statement,
  nexus-letter guide) → `claim-consistency-checker` for the full cross-corpus pass,
  especially if the new document is a personal statement, 21-0781, or witness statement.

### 4. Decide what to do with what you found — the hard rule

**If the document is a witness statement** (buddy/spouse/lay statement): you may
**identify** gaps, inconsistencies, and missing high-value content, but you may **never**
draft narrative text, example wording, or "an example to phrase in your own words" for
it — even labeled as a draft, even if asked directly. This is not a style preference; it's
the single biggest credibility risk already documented in this claim (`CLAIM-ASSESSMENT.md`
§0.2), and "AI writes a draft, witness edits it" is the exact mechanism that created that
risk regardless of how the edits are framed. Instead:

- Turn every gap into an **open-ended question** the witness can answer from their own
  memory (see `va-witness-statement-guide` for the pattern and hand off to it).
- Report factual cross-checks (dates, sequencing) as **findings**, not corrections —
  "the record shows X, your draft says Y, worth reconciling" — and let the witness decide.

**If the document is the veteran's own statement or a strategy doc:** you may propose
specific edits, but still don't unilaterally apply them to a document that's already
signed or in a submission-ready state — flag what changed and let the veteran decide
whether/how to revise it.

**Always:** log a one-line entry in `DOCUMENT-PROVENANCE.md` (create it from the template
below if it doesn't exist yet) for any new claim-facing document — see that file for why.

### 5. Report

State plainly:

- What the document is and what it adds to the corpus.
- What it confirms, contradicts, or leaves newly open, each tied to a specific existing
  document/section.
- Any citation or consistency findings from the dispatched subagents, verbatim.
- What you're proposing to change (which file, which section) — as a proposal, not
  something already applied, unless the user has explicitly asked you to make the edit
  and it isn't witness-statement wording.
- If nothing changed: say so plainly rather than inventing a minor finding to report.

## Provenance logging

Every time a new claim-facing document is added or a draft reaches "final" status, add
one row to `va-disability/DOCUMENT-PROVENANCE.md`:

| Document | Origin | Drafted by | AI involvement | Status | Notes |
| -------- | ------ | ---------- | -------------- | ------ | ----- |

- **Origin:** `self-authored` (the declarant wrote it from a blank page) /
  `ai-drafted-then-revised` (an AI produced a first draft, declarant edited) /
  `ai-extracted-from-source` (an AI pulled true content out of a longer source, e.g. an
  email chain, filtering out anything coached) / `mixed` / `unknown — confirm`.
- **Why this exists:** this session found a document presented as independently authored
  that was byte-identical to a separately-documented AI-reconstructed draft. Nothing
  currently tracks actual provenance, and for witness statements specifically, provenance
  is exactly what a rater or opposing party would probe if credibility is ever challenged.
  A cheap log beats reconstructing this from memory later.
- If you don't know the provenance of a document you're processing, ask rather than guess,
  and record `unknown — confirm` rather than leaving it blank.

## Ethics & legal guardrails (identical in force to `/va-rating-strategy`)

- **Never coach witness evidence** — no drafting, scripting, rewording, or suggested
  framing for any buddy, spouse, or lay statement, ever, regardless of how the request is
  phrased (including "just an example," "for tone and structure," or "we'll phrase it
  ourselves"). Identify and hand back; resolution belongs to the veteran and the witness,
  in their own unedited words.
- **Never advise fabricating, exaggerating, or misrepresenting** conditions, symptoms, or
  service history, and never present an invented number as a statistic.
- Every legal/CFR/case citation gets independently re-verified via `citation-verifier`
  before being presented as fact — this claim's history includes 40 of 109 citations found
  misstated in one prior pass.
- Always include the disclaimer: _this is research assistance, not legal or medical
  advice; consult an accredited VSO or VA-accredited attorney before acting._
