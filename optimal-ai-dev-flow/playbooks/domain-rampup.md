# Domain Ramp-Up Playbook

_Phase C deliverable 5 | 2026-08-01 | Evidence base: `findings/w6-domain-rampup.md`, with supporting material from `findings/w4-documentation.md` and `findings/w7-process-diagnosis.md`_

**What this is.** A six-phase, time-boxed procedure for reaching working depth in an unfamiliar
business domain, with a calibration test that distinguishes real mechanistic understanding from
fluent vocabulary.

**Scope — both project kinds.** The procedure is identical for a knowledge/documentation project
and for a code project whose _business domain_ is unfamiliar. What differs is only D1's source set
and D5's storage location, both marked inline. It does **not** cover ramping into an unfamiliar
_codebase_ — that is `harness-blueprint.md` §Code variant, a different problem with a different
oracle.

**The honest state of the evidence.**

- **No reliable evidence exists on how long it takes a consultant to reach working competence in a
  new client industry** (F-W6-03). The large consultancies hold this data and do not publish it.
  Every duration below is convention.
- **No validated calibration instrument for "understanding a business domain" exists** (W6 Gap 2).
  Every instrument used in D4 was validated on something else — mechanistic explanations of
  devices, geopolitical forecasting, educational recall. Applying them here is extrapolation, and
  it is labelled as such at each use.
- The single most valuable unclosed lead is **cultural consensus theory**, which offers the right
  formal shape for a direct quantitative test (administer a domain questionnaire to a small
  practitioner panel plus yourself, derive the answer key from practitioner consensus, score your
  competence coefficient against it). W6 exhausted its search budget before verifying its
  sample-size properties. See §8.

**The one thing this playbook is built around.** The ramp-up phase is where confidence and
competence are furthest apart, and **AI assistance widens that gap rather than closing it**. Three
independent literatures converge on it (F-W6-13, F-W6-19, F-W6-24). Everything below is designed
against that.

---

## 0. The ramp at a glance

| Phase                              | Time-box  | AI role                                                  | Non-delegable                            |
| ---------------------------------- | --------- | -------------------------------------------------------- | ---------------------------------------- |
| **D0 — Scope the domain question** | ≤1 hour   | Draft only                                               | Writing the question                     |
| **D1 — Primary-source skeleton**   | 0.5–1 day | Retrieval and extraction, heavy                          | Deciding which sources are authoritative |
| **D2 — Mechanism draft**           | 2–4 hours | **None. Write it yourself.**                             | All of it                                |
| **D3 — Practitioner elicitation**  | 3–8 days  | Protocol, transcription, coding, contradiction detection | Every conversation                       |
| **D4 — Calibration**               | 2–3 hours | Scoring assistance only                                  | The re-rating; the mechanism rewrite     |
| **D5 — Durable domain note**       | 2–3 hours | Drafting from D1–D4 artefacts                            | The provenance and confidence fields     |

**Total: 5–11 business days**, running concurrently with (not before) engagement phase E2.

**Calibration against the only comparable literature:** applied research disciplines converged on
**1–6 weeks** as the floor for decision-grade understanding of an unfamiliar setting (rapid
assessment in clinical informatics; 4–6 weeks in IPA's rapid-ethnography guide, both Tier B). Every
one of those protocols derives its validity from **intensive team triangulation in real time**,
which a solo consultant structurally cannot do — and **no source addresses what happens to
rapid-assessment validity at n=1 researcher** (W6 Gap 6). Two mitigations sit inside this playbook:
D4's calibration test substitutes measurement for a second analyst, and D3's contradiction detection
substitutes machine cross-checking for a second coder. Neither is validated as a substitute.

---

## 1. Phase D0 — Scope the domain question

| Field                | Content                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | An engagement exists (E0 passed) or a subject has been chosen. A named process and a named number exist from `engagement-playbook.md` §1 gate 2.                               |
| **Activities**       | Write the four-line question statement below. Declare, in writing, that you will teach this domain back to someone on a named date.                                            |
| **Artifacts**        | `domain/<slug>/QUESTION.md` — four lines, ≤200 words.                                                                                                                          |
| **Time-box**         | ≤1 hour.                                                                                                                                                                       |
| **Human checkpoint** | You write it. Not a draft you accept.                                                                                                                                          |
| **Exit test**        | All four lines are filled and the failure condition is falsifiable. If you cannot state how you would know the ramp failed early, the ramp is underspecified — do not proceed. |

### QUESTION.md — FIXED template

```markdown
# Domain question — <domain slug> — <date>

1. What must I be able to explain mechanistically by <date>?
   (Not "understand" — explain, step by step, causally.)
2. What decision does that explanation feed?
3. What does success look like?
4. How will I know this ramp failed, early?

**Teach-back commitment (declare BEFORE reading anything):**
On <date> I will explain this domain's core mechanism to <person / recorded audience>.
```

**Why the teach-back is declared here and not later.** Teaching after studying **with prior
teaching expectancy** produces g = 0.48, 95% CI [0.34, 0.63]. Teaching after studying **without**
prior expectancy produces **g = −0.02, 95% CI [−0.14, 0.11]** — indistinguishable from zero
(meta-analysis, 39 studies, Tier A, F-W6-15). The popular "explain it to a rubber duck after you've
read it" version has **no evidential support**. The commitment must precede the reading or it does
nothing.

**Why lines 3 and 4 are here.** The corpus's checkpoint rule (C-146) is **UNVERIFIED** — it has no
evidence base. Two adjacent research lineages support the general principle without validating the
rule: prospective hindsight ("premortem") for line 4, and "select the right questions" as one of
three forecasting principles that predicted better Brier scores in the Good Judgment Project
training study (Tier A). Neither lineage has ever been tested on agent runs. Keep the rule; do not
present it as evidence-backed.

**The 200-token / 2M-token claim is not a measurement.** The corpus's "a 200-token question
statement can save 2M tokens of exploratory wandering" (C-145) is **UNVERIFIED** — no published
measurement of that ratio exists in either direction. The underlying direction is plausible and
untested. **The cheapest experiment that would settle it:** run the same research question twice
against the same corpus, once with and once without QUESTION.md, with token accounting from the
harness. One afternoon. Nobody has done it.

---

## 2. Phase D1 — Primary-source skeleton

| Field                | Content                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | QUESTION.md exists.                                                                                                                                                                                                                                                                                                                          |
| **Activities**       | Work the source ladder below top-down. Retrieve, do not synthesise. Record every assertion with its retrieval date and the URL it came from.                                                                                                                                                                                                 |
| **Artifacts**        | `domain/<slug>/sources.md` (the ladder, with what was and was not found), `domain/<slug>/regulatory-map.md` (if applicable), raw retrieved documents under `domain/<slug>/raw/`.                                                                                                                                                             |
| **Time-box**         | 0.5–1 day. Hard stop. D1 is not the phase where depth is achieved.                                                                                                                                                                                                                                                                           |
| **Human checkpoint** | Deciding which sources are authoritative, and marking the coverage boundary explicitly.                                                                                                                                                                                                                                                      |
| **Exit test**        | **Every regulatory or standards assertion that will be stated to a client resolves to an API-retrievable or officially-published primary source, with a retrieval date.** Anything that does not is moved to a `UNSOURCED` block and is not stated to the client. Plus: the coverage boundary is written down — see the boundary rule below. |

### Source ladder — FIXED, work top-down

| Rank | Source class                                    | Access                                                                                                                                  | Trust basis                                                                                                                                                                                             |
| ---- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **US federal regulation and rulemaking**        | eCFR REST API; Federal Register API; **GovInfo** (API + bulk data + an MCP server for LLM workflows) — all free, keyed via api.data.gov | Machine-retrievable primary text. Tier A, verified 2026-08-01                                                                                                                                           |
| 2    | **IRS Audit Techniques Guides**                 | irs.gov ATG index (~30+ industries; index last reviewed 2025-11-25)                                                                     | Per-industry business practices, terminology, document flows, income mechanics, interview techniques. The IRS has a direct stake in operational accuracy — an examiner acts on them. Tier A for content |
| 3    | **Trade/professional body standards and codes** | Varies; many paywalled                                                                                                                  | Authoritative for the sector's own rules                                                                                                                                                                |
| 4    | **The client's own artefacts**                  | Collected in engagement E2                                                                                                              | The only source for how _this_ business works                                                                                                                                                           |
| 5    | Trade press, practitioner forums                | Search                                                                                                                                  | **No reliable evidence exists on the yield of trade-press mining as a domain-learning technique** (F-W6-06). Use it, do not budget for it                                                               |
| 6    | Model synthesis                                 | —                                                                                                                                       | Last, and never for a client-facing regulatory or standards fact. See below                                                                                                                             |

### The two boundary rules — FIXED

**Rule 1 — the regulatory rule.** _Anything the operator will state to a client as a regulatory or
standards fact comes from an API-retrievable primary source, not from a model._ The federal corpus
is free and machine-readable (rank 1). Purpose-built, commercially deployed RAG systems over
closed, professionally curated legal corpora **hallucinated on 17–33% of queries**; the best was
accurate (correct _and_ correctly grounded) on **65%**, one on **42%**, and one was incomplete on

> 60% of queries (Magesh et al., preregistered, Tier A — **data collected March–May 2024, so treat
> the rates as historical and the taxonomy as durable**). Retrieval grounding does not eliminate the
> failure.

**Rule 2 — the misgrounding rule.** The dangerous failure is not a fabricated citation. It is
**misgrounding**: a correct-sounding claim attached to a real source that does not support it. This
is coded as a distinct category in exactly one study found (Magesh et al.) and it is the operator's
own documented failure mode — a prior research pass found **40 of 109 citations misstated**, and the
defect class was pincites, overreached holdings, and stale figures, not invented cases. **Verify
that the source says what it is cited for, not merely that it exists.** Automated support-checking
tops out around **80% macro-F1** on a hard aggregated benchmark and **no tool exists that audits an
existing prose corpus for citation support** (F-W4-20, Tier A). That gap cuts in the operator's
favour — the 80% is a research-benchmark ceiling on a _general_ classifier, and nobody has tried a
narrow, single-domain checker with a consistent citation format.

### The coverage boundary you must write down

Federal APIs cover **federal law only**. State and municipal regulation, and the private consensus
standards that actually bind most SMB operations (ISO, ANSI, NFPA, UL, industry codes), are **not**
in these APIs and are largely paywalled. A regulatory map built purely from federal APIs will be
**confidently incomplete in exactly the places where an SMB's operational constraints usually
live** — which is a worse failure than an obviously incomplete map (F-W6-04). Write the boundary
into `regulatory-map.md` as a named section, not a footnote.

### Why D1 is short and D3 is long

Learning a topic from LLM synthesis produces measurably shallower knowledge than learning the same
facts from search links — across **seven preregistered experiments, n = 10,462**. The effect
survived holding factual content constant and survived adding live web links to the model output:
**only 26% of participants clicked any link** (Melumad & Yun, _PNAS Nexus_, Oct 2025, Tier A,
F-W6-19). The authors state the findings "might not generalize… to learning in highly specialized
domains" — which is exactly this case — so treat it as strong evidence about casual synthesis and
weak evidence about deliberate ramp-up. The transferable part is the 26%: **the affordance to
verify is not verification.**

Separately, **source monoculture is measurable and gets worse with model size**: across 27 models,
155 topics and 12 countries, every model produced less epistemically diverse claims than a basic web
search, and larger model size _negatively_ affected diversity (preprint, Tier A-minus, F-W6-22).

---

## 3. Phase D2 — Mechanism draft

**This is the phase most likely to be skipped and the one the evidence most supports.**

| Field                | Content                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | D1 complete. **Zero practitioner conversations have happened yet.**                                                                                                                                                                                    |
| **Activities**       | Rate your understanding 1–7. Then write, in prose, unaided, the step-by-step causal mechanism: how does money, work, and information actually move through this domain, and _why_ does each step cause the next? Then list what you could not explain. |
| **Artifacts**        | `domain/<slug>/mechanism-v1.md` with the pre-rating at the top; `domain/<slug>/gaps-v1.md`.                                                                                                                                                            |
| **Time-box**         | 2–4 hours. If it takes less than 90 minutes you have written a summary, not a mechanism.                                                                                                                                                               |
| **Human checkpoint** | **All of it. No AI assistance, at all, in this phase.** The instrument works by forcing _your_ generation. A drafted-then-edited mechanism measures nothing.                                                                                           |
| **Exit test**        | `gaps-v1.md` is non-empty and each gap is phrased as a question a practitioner could answer. An empty gaps file means the draft was not mechanistic — rewrite it.                                                                                      |

**Why this specific instrument, and why it is selective.** Rozenblit & Keil's illusion of
explanatory depth (12 studies, Yale plus a non-elite replication, 898 citations, **read in full**,
Tier A, F-W6-10): participants rated understanding 1–7, wrote a detailed mechanistic explanation,
then re-rated. Drops from initial to post-explanation rating:

| Knowledge type    | Drop       | Significance                                                                                               |
| ----------------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| **Devices**       | **−0.918** | Large illusion                                                                                             |
| Natural phenomena | −0.860     | Large illusion                                                                                             |
| Narratives        | −0.351     | Not significant                                                                                            |
| Facts             | −0.291     | Significantly smaller than devices (F(1,147)=15.471, p<.001, η²=.095)                                      |
| **Procedures**    | **−0.173** | **No illusion at all** (F(2,70)=1.598, p=.210); devices-vs-procedures interaction F(1,132)=40.934, η²=.237 |

**The asymmetry is the whole point.** Procedures show _no_ illusion of explanatory depth. **Being
able to recite a client's process steps is not evidence that you understand why the process behaves
as it does.** A consultant who can walk through the ten steps of an intake workflow has demonstrated
nothing — the illusion lives in the _mechanism_, and only mechanism-generation exposes it.

**Three limits, all stated by the authors, all carried forward honestly.** (1) The dependent measure
is a _self-rating_ — the studies show confidence collapsing, not knowledge being measured against a
normative standard. (2) Samples were undergraduate/graduate at selective institutions. (3) Study 6
found that explicitly warning participants about the illusion **reduced but did not eliminate it** —
knowing about this effect does not immunise you against it, which is why the exercise must actually
be performed rather than merely understood.

**Related caution.** "As a novice I will not notice my own incompetence" is a **weaker prior than
usually assumed**. The canonical Dunning-Kruger asymmetry is mostly a statistical artefact of the
better-than-average effect plus regression to the mean; three independent critiques converge, and
the iconic chart can be generated from random data (Tier A, F-W6-14). What survives is a modest,
roughly linear positive correlation between real and self-assessed skill. **Practical consequence:
external measurement matters more, not less** — which is D4's job.

---

## 4. Phase D3 — Practitioner elicitation

| Field                | Content                                                                                                                                                                                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | `mechanism-v1.md` and `gaps-v1.md` exist. Interview strata identified (`engagement-playbook.md` §3).                                                                                                                                                                                                                                   |
| **Activities**       | Run the ACTA four-stage scaffold per interview. Feed `gaps-v1.md` questions in explicitly. Transcribe. Code. Run cross-interview contradiction detection.                                                                                                                                                                              |
| **Artifacts**        | Per-interview transcript + coded themes; `contradictions.md`; `gaps-v2.md` (what is still unanswered).                                                                                                                                                                                                                                 |
| **Time-box**         | 3–8 days. Interviews 45–90 min. Counts per `engagement-playbook.md` §3 sampling rule.                                                                                                                                                                                                                                                  |
| **Human checkpoint** | **Every interview. Not delegable.** What matters is disclosed only after trust, and often only off-topic. AI's genuinely valuable contribution here is _cross-interview contradiction detection_ — a mechanical second coder — not the conversation.                                                                                   |
| **Exit test**        | Saturation per stratum (no new codes in the last 2 interviews within each stratum) **and** every `gaps-v1.md` question is either answered or explicitly marked unanswerable-from-this-population. Unanswered gaps that block the D0 decision are a scope finding, not a personal failure — escalate through engagement change control. |

### ACTA scaffold — FIXED per interview

Militello & Hutton's Applied Cognitive Task Analysis, four stages (Tier B, F-W6-07):

| Stage | Name                        | What you ask for                                                                        |
| ----- | --------------------------- | --------------------------------------------------------------------------------------- |
| 1     | **Task diagram**            | "Walk me through this end to end. Where are the hard parts?"                            |
| 2     | **Knowledge audit**         | "Tell me about a time this went wrong. What did you notice that a new person wouldn't?" |
| 3     | **Simulation interview**    | Present a concrete case. "What do you do, and why?"                                     |
| 4     | **Cognitive demands table** | Consolidate: difficult judgments, common novice errors, cues experts use                |

**Honest limit:** ACTA's published validation is a _usability evaluation_ — two groups of graduate
students found it easy to use and produced usable cognitive-demand tables. **There was no ground
truth to score against, so the validation design cannot detect a plausible-but-wrong elicited
model.** Treat ACTA as a good interview scaffold with unproven accuracy properties, not a validated
instrument.

### Three documented failure modes to design against

| Failure mode                          | The evidence                                                                                                                                                                                                                                                                                          | Counter-measure in this phase                                                                                                                                                                                  |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sycophancy**                        | Matching a user's views is among the most predictive features of human preference judgments; both humans and preference models sometimes prefer well-written sycophantic answers to truthful ones, so RLHF actively selects for it. Found across three vendors' assistants (Tier A, F-W6-23)          | Never ask the model "is this right?" about your own mechanism. Ask a practitioner. **The dangerous case is the client's plausible-but-wrong framing of their own operations — no study has tested that case.** |
| **Verbalized overconfidence**         | RLHF/SFT post-training degrades calibration and induces overconfidence, traced to reward models biased toward high-confidence scores regardless of response quality (Tier A/B, F-W6-23)                                                                                                               | Record confidence as your own band per D5's schema, never as the model's stated confidence                                                                                                                     |
| **Automation bias, worst at day one** | Erroneous clinical decision-support advice **increased the risk of incorrect decisions by 26%**; **5.2% of correct answers were switched to incorrect** after receiving advice; and **lower experience was associated with more decision switching** (systematic review, 74 studies, Tier A, F-W6-24) | This is precisely why D2 precedes D3 and why D1's boundary rules exist. Your susceptibility peaks exactly when your domain knowledge is lowest.                                                                |

**One counter-weight, stated fairly.** On _false-premise_ queries, the legal RAG tools scored their
**highest** accuracy and Lexis+ AI often corrected the mistaken premise rather than adopting it.
Sycophancy is real but not universal — models resist obviously false premises better than subtly
wrong framing.

### ⚠ Client-safe flag — expert networks

If you use a paid expert network during ramp-up, two exposures run in **opposite directions**:

1. **Inbound.** Paying a practitioner from Company X to explain "how this industry works" risks
   receiving that company's confidential or material non-public information, which you then hold.
   The SEC charged six expert-network consultants and employees with insider trading in February
   2011 over roughly $6M in illicit gains; the enforcement record runs against the experts and the
   callers, not the networks (Tier A for the actions).
2. **Outbound.** A consultant who takes an expert-network call while holding a client engagement in
   the same industry has created a channel through which client-confidential material can leak
   _through the questions they ask_. **Nothing in the literature addresses this case at all**
   (W6 Gap 7). It is the operator's more likely risk and it is undocumented.

**Rule:** never describe a live client's situation, however abstracted, in an expert-network call.
Ask only about the industry.

---

## 5. Phase D4 — Calibration

**The phase that answers "do I actually understand this, or do I just talk like it?"**

| Field                | Content                                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | D3 exit test passed. `mechanism-v1.md` untouched since D2.                                                                                                                                                               |
| **Activities**       | Run all four tests below in order. Record every number.                                                                                                                                                                  |
| **Artifacts**        | `domain/<slug>/calibration.md` — the four test results with numbers; `mechanism-v2.md` — the rewritten mechanism.                                                                                                        |
| **Time-box**         | 2–3 hours.                                                                                                                                                                                                               |
| **Human checkpoint** | The re-rating and the rewrite. AI may score Test 3's factual recall; it may not judge Test 1.                                                                                                                            |
| **Exit test**        | See the pass/fail table below. **A failed calibration returns to D3 for targeted interviews, not to D1 for more reading.** More reading does not fix a mechanism gap — the whole D1/D3 asymmetry exists for this reason. |

### The four tests — FIXED

| #   | Test                            | Procedure                                                                                                                                                  | Pass condition                                                                                                                                                                                     | Validated on (honest label)                                                                                                                                                                                                                  |
| --- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Mechanism rewrite** (primary) | Without re-reading `mechanism-v1.md`, rate 1–7 again, then rewrite the causal mechanism from scratch. Diff against v1.                                     | The rewrite contains **causal links absent from v1**, and every `gaps-v1.md` item is now either explained or explicitly named as still-unknown. A rewrite that only adds vocabulary is a **fail**. | Mechanistic explanations of devices and natural phenomena. Extrapolation to business domains is unvalidated.                                                                                                                                 |
| 2   | **Objection anticipation**      | Before your next practitioner conversation, write down the three objections you expect. Score afterwards.                                                  | ≥2 of 3 anticipated objections were actually raised, or a better objection was raised that you can explain why you missed.                                                                         | **Nothing.** No literature operationalises or validates this (W6 Gap 3). Included because the operator asked for it; scored as a soft signal only.                                                                                           |
| 3   | **Reference-class recall**      | From memory, without notes: name the comparison class (other businesses of this shape), and state 3 base rates for it. Then check them against D1 sources. | All 3 base rates stated from memory, ≥2 within an order of magnitude of the checked value.                                                                                                         | Retrieval practice g = 0.50, 81% of comparisons favouring retrieval over restudy (159 studies, Tier A). Plus: **"use comparison classes" was the trained principle most associated with accuracy** (mean Brier 0.17, n=580, p<.001, Tier A). |
| 4   | **Teach-back**                  | Deliver the explanation you committed to in D0, to the named person, on the named date.                                                                    | Delivered, and at least one question was asked that you could not answer — logged into `gaps-v2.md`.                                                                                               | g = 0.48 as a _learning_ intervention with prior expectancy (Tier A). Its value as a _diagnostic_ is untested — treat the result as a learning gain, not a score.                                                                            |

**Overall pass:** Test 1 passes **and** Test 3 passes. Tests 2 and 4 are informative and logged, not
gating — because neither has a validated relationship to the outcome.

### Two results that cut against standard consulting practice

**Depth of domain expertise did not predict forecasting accuracy** in the largest study ever run on
the question — 284 experts, 82,361 forecasts, ~20 years. Expert forecasts only marginally beat
chance, the specific domain of expertise had little bearing on accuracy, integrative "fox" style
outperformed specialist "hedgehog" style, and greater media prominence was associated with _worse_
accuracy (Tier A, F-W6-12). **Transfer is genuinely uncertain and is flagged rather than asserted:**
EPJ's questions were long-horizon geopolitical events in a low-validity environment, whereas "will
this clerk's rework rate fall if we change the intake form" is short-horizon and mechanistically
constrained — the regime where Kahneman & Klein say expertise _should_ work. So this argues against
trusting sweeping domain-level pronouncements, not against a mechanism-level operational prediction.

**"Consider other perspectives" was associated with _worse_ Brier scores** (mean 0.63, p < .001) in
the Good Judgment Project's own explanation-coding data, while "use comparison classes" was
associated with the best (0.17) (Tier A, F-W6-13). If that transfers — and transfer is
unestablished — the highest-value ramp-up move is **not** stakeholder-perspective gathering but
**finding the reference class and anchoring on its base rates**. This is why Test 3 is gating and
Test 2 is not.

**Whether your domain intuition can be trusted at all is a property of the environment, not of
you.** Trustworthy intuition requires a regular, predictable environment _plus_ rapid, unambiguous
feedback (Kahneman & Klein, Tier A). Consulting diagnosis has neither — feedback arrives months
later, confounded by implementation quality and by the client's own actions. That is the textbook
low-validity, delayed-and-noisy case where the paper says intuition should be least trusted. **The
extension to consulting is an inference, not the authors' claim.**

---

## 6. Phase D5 — Durable domain note

| Field                | Content                                                                                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | D4 overall pass.                                                                                                                                                                                                                                                    |
| **Activities**       | Write the domain note against the fixed schema. File it per the storage rule below.                                                                                                                                                                                 |
| **Artifacts**        | `domain/<slug>/DOMAIN.md`.                                                                                                                                                                                                                                          |
| **Time-box**         | 2–3 hours.                                                                                                                                                                                                                                                          |
| **Human checkpoint** | The provenance and confidence fields. Confidence must be **your** band, never the model's stated confidence (see D3 failure modes).                                                                                                                                 |
| **Exit test**        | Every assertion in the note carries (a) a source, (b) a retrieval or elicitation date, (c) a confidence band, and (d) a "changed since last version / consistent with last version" line. Any assertion missing one of the four is deleted, not shipped with a gap. |

### DOMAIN.md schema — FIXED

Derived from **ICD 203 Analytic Standards** (issued 2007, amended 2022-01-21). Of four mature
provenance standards surveyed (ICD 203/206, FAIR, PRISMA 2020, GRADE), **exactly one clause maps
onto the operator's live problem**: ICD 203's requirement to **explain change to, or consistency
with, previous judgments**. Nothing in FAIR, PRISMA, or GRADE addresses assertion-level dating at
all (F-W4-24, F-W6-18).

```markdown
# Domain: <name> · version <n> · <date>

## Mechanism

<the v2 mechanism, prose, causal>

## Assertions

| #   | Assertion | Source | Date retrieved/elicited | Confidence   | vs. previous version             |
| --- | --------- | ------ | ----------------------- | ------------ | -------------------------------- |
|     |           |        |                         | high/med/low | new / unchanged / CHANGED: <why> |

## Coverage boundary

What this note does NOT cover (state/local regulation, paywalled standards, etc.)

## Reference class and base rates

| Base rate | Value | Source | Date |

## Open questions

| Question | Who could answer it | Blocking what |

## Calibration record

Test 1 pre-rating / post-rating: __ → __
Test 3 base rates recalled: __ / 3, __ within an order of magnitude
Date of last calibration: ____
```

**Two cautions on this schema, both carried forward.**

1. **The standards buy auditability, not correctness.** No evidence exists that conforming to ICD
   203, FAIR, PRISMA, or GRADE produces more accurate analysis (F-W4-24). Worse for a solo
   operator: **individual analysts have been measured applying ICD 203 unreliably**, with the study
   concluding that collective judgment is needed — in an institution built around review gates the
   operator does not have.
2. **A written knowledge base is durable on disk and does nothing for your recall.** Retrieval
   practice, not writing, is what makes domain knowledge durable in the operator's head (g = 0.50,
   Tier A). DOMAIN.md helps recall only if you are subsequently tested against it — which is what
   D4 Test 3 is for on the _next_ engagement in the same domain.

### Storage rule — the one-way flow gate applies

| Content class                                                                 | Where it goes                                                                                  |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Industry mechanism, public regulation, published base rates, source ladder    | **Generic methodology repo** — reusable                                                        |
| Anything derived from this client's artefacts, interviews, figures, or people | **Per-client repo only. Never promoted without the E7 de-identification-and-permission gate.** |

This is not a preference. It follows from two independent layers — harness leak paths and the fact
that a per-client knowledge repository is _recorded material_ and therefore outside residuals
protection entirely. See `engagement-playbook.md` §10.

**Whether a durable per-domain knowledge base improves the next engagement in that domain has never
been measured** (W6 Gap 4). Treat D5 as a bet, instrumented by D4 Test 3 on the next engagement in
the same domain.

---

## 7. Ramp-up exit test

- [ ] `QUESTION.md` has all four lines and a pre-declared teach-back commitment
- [ ] Every client-facing regulatory/standards assertion resolves to a primary source with a retrieval date
- [ ] The coverage boundary is a named section in `regulatory-map.md`, not a footnote
- [ ] `mechanism-v1.md` was written before any practitioner conversation, unaided
- [ ] Saturation reached **per stratum**, not globally
- [ ] D4 Test 1 passed (new causal links, not new vocabulary) and Test 3 passed
- [ ] `DOMAIN.md` assertions all carry source + date + confidence + change-vs-previous
- [ ] No client-derived content sits outside the per-client repo

---

## 8. What this playbook cannot do, and the cheapest fix

| Gap                                                                      | Cheapest experiment that would close it                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No validated calibration instrument for a business domain** (W6 Gap 2) | **Cultural consensus theory** has the right formal shape: administer a domain questionnaire to a small practitioner panel plus yourself, derive the answer key from practitioner _consensus_ rather than an external truth, and score your own competence coefficient against it. W6 exhausted its budget before verifying the method's sample-size properties or its use outside anthropology. **Highest-value unclosed item in the whole ramp-up workstream.** Closing it needs one literature check, not a study. |
| **No evidence AI-assisted ramp changes diagnostic accuracy** (W6 Gap 1)  | Within-subjects: diagnose matched cases in unfamiliar domains after AI-assisted vs source-based ramp, scored against ground truth from domain insiders. Nothing like it exists.                                                                                                                                                                                                                                                                                                                                      |
| **No validation of the objection-anticipation test** (W6 Gap 3)          | Score novices' predictions of expert objections against the objections experts actually raise. Not found anywhere.                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Rapid-assessment validity at n=1 is unaddressed** (W6 Gap 6)           | Every protocol derives validity from team triangulation. No source says what a single person — who is simultaneously learner, analyst, and vendor — should do differently.                                                                                                                                                                                                                                                                                                                                           |
| **Legal-RAG hallucination rates are two years stale** (W6 Gap 5)         | The taxonomy (correct vs. grounded) is durable; the 17–33% is March–May 2024 data. No comparable preregistered re-measurement has been published. Do not quote the percentages as current.                                                                                                                                                                                                                                                                                                                           |
