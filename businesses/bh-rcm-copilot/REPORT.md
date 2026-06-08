# BH-RCM Copilot — Venture Brief

> **Working name:** BH-RCM Copilot (behavioral-health denial-prevention & utilization-review copilot)
> **Status:** Concept / pre-validation · **Created:** 2026-06-08
> **Origin:** Surfaced as the strongest _new_ treatment-industry wedge in the entrepreneurial-pursuits
> v2 research (`../entrepreneurial-pursuits/REPORT.md` §3, §7; evidence in
> `../entrepreneurial-pursuits/research-dossier-v2.md` sections 1A/1B/1C).
> **Verdict (carried from v2):** **CAUTIOUS-GO, validation-gated.** Rank #4 in the portfolio,
> later-sequence than the CPA income engine that funds it.

---

## 0. One-line thesis

An AI copilot that **prevents and recovers insurance denials for behavioral-health / addiction
treatment centers** — sitting _on top of_ their existing EHR, tuned to behavioral health's
idiosyncratic denial drivers — sold ROI-priced (a cut of recovered/avoided denials) through a warm
CPA-client channel. It attacks the connective-tissue layer the entrenched EHRs structurally
under-serve, so it never fights the unwinnable rip-and-replace war.

---

## 1. Problem & customer

### The pain (quantified, dollar-denominated)

Behavioral-health and SUD treatment revenue leaks through claim denials at a rate far above general
medicine, and most of the loss is _preventable and recoverable_ — it's lost to a **labor bottleneck**,
which is exactly what an AI agent replaces:

- BH claims are denied **~85% more often** than medical claims: **12–20% vs 5–10%** denial rates.
- **82–85% of denials are preventable** (eligibility, medical-necessity documentation, coding,
  authorization/UR errors — not true clinical ineligibility).
- **~60% of denials are never resubmitted** → permanent revenue loss, purely because appeals are
  manual, slow, and under-staffed.
- Yet **81.7% of _appealed_ denials are overturned** — the money is real and winnable.
- Behavioral-health orgs lose an estimated **20–30% of earned revenue** to preventable billing/RCM
  errors.

_(Sources: see `../entrepreneurial-pursuits/research-dossier-v2.md` §1B — BlueBrix, PIMSY. Figures
carry the dossier's citations.)_

### Why behavioral health specifically (the moat to acquire)

BH denials have **idiosyncratic drivers** that general-medical RCM tools don't model:

- **ASAM level-of-care / continued-stay utilization review** — the dominant denial vector for
  residential/PHP/IOP; payers challenge whether the patient still needs that level of care.
- **MHPAEA parity** nuances — BH benefits adjudicated differently; parity violations are appealable.
- **42 CFR Part 2** — SUD records carry stricter consent/disclosure rules than HIPAA, which shapes
  what can be sent to payers and how.
- **Psychotherapy CPT time-band mismatches** (e.g., 90832/90834/90837), group vs individual coding,
  bundling rules — frequent, mechanical, preventable denials.

A tool tuned to _these_ is differentiated; a generic prior-auth bot is not.

### The customer

- **Primary buyer:** the **billing / RCM manager or revenue-cycle lead** at a private treatment
  center, and the **owner/operator** who feels the cash-flow pain. (Buyer detail in dossier §1C.)
- **Segment SAM (be honest):** _not_ the 14,000+ headline facility count. The realistic serviceable
  market is a **few thousand private IOP / PHP / residential / outpatient operators** that bill
  commercial/Medicaid and have enough claim volume to feel denials but are too small to staff a
  sophisticated RCM team. (SAMHSA 2023 N-SUMHSS, dossier §1B.)
- **Wedge segment:** small-to-mid private IOP/PHP and residential operators — big enough to hurt,
  too small for an in-house denial-management team.

---

## 2. Market

- **Behavioral-health software + EHR + RCM** is a large, growing category (sizing and CAGR cited in
  dossier §1B). RCM/denial-management is a distinct, painful sub-segment within it.
- **Tailwind:** AI adoption in behavioral health is rising fast, and payers are _increasing_
  automated denials — an arms race that pushes providers toward AI defense.
- **Reframe the TAM honestly:** revenue is a function of (recoverable denial dollars per facility) ×
  (serviceable facility count) × (capturable share). The denial dollars per facility are large; the
  facility count is in the low thousands; the constraint is distribution and trust, not market size.

---

## 3. Competition & the gap

The v2 incumbent teardown (dossier §1A) found the gap is **real but narrow**:

| Player type                                    | Examples                                                | Why they don't fill this gap                                                                                                                                                                             |
| ---------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **General-medical / payer-side prior-auth AI** | Cohere, Innovaccer                                      | Built for medical prior-auth and payer workflows; not tuned to BH denial drivers (ASAM UR, parity, Part 2).                                                                                              |
| **Well-funded BH-AI**                          | Eleos, Commure                                          | Sit in **clinical documentation / scribing** — a _different, already-contested_ category — not RCM/denial prevention.                                                                                    |
| **BH EHR incumbents**                          | Kipu, Sunwave/Lightning Step, Ritten, BestNotes, Alleva | RCM is a bundled module, not a denial-prevention engine; their own top complaints are billing/connective-tissue failures (charges not dropping, billing config). Denials are a bolt-on they under-serve. |
| **Generic RCM outsourcers**                    | (regional billing companies)                            | Human-labor model; the thing being disrupted, not a competitor product.                                                                                                                                  |

**The opening:** no BH-native, AI-native, _pre-bill scrubber + appeal-drafter_ tuned to BH's specific
denial taxonomy surfaced in research. The EHRs treat it as a feature; the AI-doc players aren't in
RCM; the medical prior-auth players aren't in BH.

**The threat (eyes open):** the BH EHR market is **consolidating under private equity** (Kipu acquired
Team Recovery + Hatch Compliance; Sunwave merged Lightning Step; Ritten raised $35M Series B). Any of
them could build or buy this. The defensible posture is **EHR-agnostic middleware** + **BH domain
depth** + **warm distribution** — win the beachhead before an incumbent notices, and stay portable so
no single EHR can lock you out.

---

## 4. Product — what it actually is

A thin, EHR-agnostic layer (read from the EHR / clearinghouse, write back drafts and flags) with three
functions, shippable incrementally:

1. **Pre-bill claim scrubber (prevent).** Before a claim goes out, the LLM checks the clinical note +
   coding + authorization against BH-specific rules: medical-necessity language present for the billed
   ASAM level, CPT/time-band consistency, parity-relevant flags, documented continued-stay
   justification. Flags the gap and drafts the fix for a human to approve. _This is the highest-value,
   lowest-risk starting point — it's a text/document problem, pure LLM territory, no clinical
   decision-making._
2. **Concurrent utilization-review assistant (defend).** Drafts the medical-necessity / continued-stay
   justification packet for UR calls and prior-auth, pulling the right language from the clinical
   record mapped to ASAM criteria.
3. **Denial triage + appeal drafter (recover).** Ingests denial/remittance (835/EOB), classifies the
   denial reason, and drafts a cited appeal letter — directly attacking the "60% never resubmitted"
   loss with the "81.7% of appeals win" upside.

**Why solo-buildable:** every function is a **text → structured-justification** transform. No
proprietary dataset, no device, no model training required at the start — retrieval + strong LLM +
BH-specific prompt/rule libraries. The senior-engineering + lived-recovery + domain-depth combination
is the differentiator, not raw ML.

---

## 5. The hard gates (must clear BEFORE building)

These are go/no-go, not afterthoughts. Both are flagged `[VERIFY]` in the v2 research.

### Gate A — 42 CFR Part 2 + HIPAA data architecture

SUD treatment records are the most tightly regulated health data in the US. Feeding them to an LLM
requires:

- A **BAA-covered model** (e.g., enterprise Anthropic/OpenAI/Azure/Bedrock with a signed BAA) **or**
  de-identification before inference. **[VERIFY a viable, affordable BAA path before writing code.]**
- Part 2-compliant consent for any disclosure; minimum-necessary; full audit logging.
- No training on customer PHI; tenant isolation.
- This is also Marcus's edge: he already understands Part 2 from the recovery ventures, and a
  compliant architecture is itself a barrier competitors must also clear.

### Gate B — willingness-to-pay validation with real operators

- Validate with **3–5 actual treatment-center clients from the TWK CPA book** that they will pay a %
  of recovered/avoided denials, **before** writing production code.
- Confirm the ROI math per facility (recoverable denial $ × capture rate > price) is legible enough to
  close.
- If operators won't commit to a paid pilot on the ROI story, stop.

---

## 6. Business model

- **Pricing: ROI / outcome-based** — a percentage of denials prevented + recovered, or a flat monthly
  fee benchmarked to a fraction of recovered dollars. Trivially justifiable when 60% of denials are
  otherwise abandoned. (Avoid per-seat — the value is dollars recovered, not seats.)
- **Land:** denial triage + appeal drafter (immediate, measurable recovery → fast ROI proof).
  **Expand:** pre-bill scrubber + UR assistant (prevention, stickier, higher value).
- **Unit-economics note:** as a B2B vertical-AI tool with warm distribution, the model only works if
  CAC stays low — which is the entire reason to lead with the **CPA-client channel** rather than a
  paid sales motion (mirrors the regroup CAC/LTV lesson in the v2 report §5).
- **Compliance cost is real:** the BAA/Part 2 architecture + any future HITRUST is a moat _and_ a
  cost; budget for it rather than pretending it away.

---

## 7. Go-to-market — the unfair advantage

The distribution edge is what makes this more attractive than building a cold B2B SaaS:

1. **Warm channel via the CPA book.** TWK and the brother's network include / can reach **treatment-center
   clients** — the exact buyers, warm. A CPA introduction ("he can audit your denial leakage for $X
   and show what's recoverable") is the lowest-friction entry.
2. **Lived-recovery credibility.** Marcus's authentic recovery background opens doors with
   treatment-center owners that a generic vendor can't.
3. **Land via a free/cheap "denial leakage audit."** Diagnostic-first: analyze a facility's recent
   denials, quantify recoverable dollars, then convert to a paid pilot. Same audit→sprint→retainer
   ladder as the CPA-automation play.
4. **Design-partner first.** One or two design-partner facilities (ideally from the warm network) with
   free/discounted access in exchange for data, feedback, and a case study.

---

## 8. Risks & what would kill it

| Risk                                                                          | Severity    | Mitigation                                                                                        |
| ----------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------- |
| **42 CFR Part 2 / HIPAA architecture not viable or too costly**               | Existential | Gate A — confirm BAA path before building; de-identify where possible                             |
| **Operators won't pay / ROI not legible**                                     | Existential | Gate B — paid-pilot commitment before code                                                        |
| **PE-backed EHR builds/buys it**                                              | High        | Stay EHR-agnostic + portable; win the beachhead fast; depth in BH-specific denial logic           |
| **Payers change denial behavior / adjudication**                              | Medium      | Rules library is updatable; denial drift is itself recurring demand                               |
| **Distribution beyond the warm channel**                                      | Medium      | Prove warm-channel economics first; expand only after                                             |
| **Founder bandwidth** (competes with the #1 CPA engine + 3 recovery ventures) | High        | Sequencing discipline — this is rank #4, _after_ the income engine is flowing                     |
| **Clinical liability / scope**                                                | Medium      | Tool _drafts and flags_ for human approval; never auto-submits or makes clinical/coding decisions |

---

## 9. Validation roadmap (no production build until these pass)

**Phase 0 — Desk validation (weeks, ~$0):**

- Confirm a concrete, affordable **BAA-covered LLM path** (Gate A).
- Map the exact BH denial taxonomy + the 5–8 highest-frequency, highest-recoverable denial codes.
- Interview 3–5 treatment-center billing leads from the CPA network on denial pain + WTP (Gate B).

**Phase 1 — Manual-first pilot (the "Wizard of Oz"):**

- Run a **denial-leakage audit** for 1–2 design-partner facilities using the LLM behind the scenes
  (you in the loop), drafting appeals by hand-assisted AI. Prove recovery dollars with zero product.
- Success metric: dollars recovered > pilot price; operator signs a paid commitment.

**Phase 2 — Thin product (only if Phase 1 closes):**

- Build the **denial triage + appeal drafter** as the first shipped module, on the compliant
  architecture. One EHR/clearinghouse integration.
- Expand to pre-bill scrubber + UR assistant.

---

## 10. Fit with the rest of the portfolio

- **Funded by, and sequenced after, the #1 CPA income engine** — do not let it starve the engine.
- **Same buyer adjacency** as the recovery ventures' treatment-center bridge, but **lower regulatory
  load than the EKRA bridge** (it's the center's own RCM tool — no patient-flow/referral remuneration
  issue) and a **clearer, dollar-denominated ROI** than homegroups.
- **Reuses the same "AI automation over an entrenched system of record" pattern** as the CPA-automation
  work and the resell-to-other-firms play — shared engineering DNA.

---

## Open questions for Marcus

1. Are there treatment-center clients in the TWK / brother's book today, and how warm? (Gate B depends on it.)
2. Appetite to fund/secure a BAA-covered model + basic compliance review before any build? (Gate A.)
3. Willing to run the manual-first audit personally (Phase 1) before committing engineering time?
4. Is this rank-#4 timing acceptable — i.e., parked until the CPA engine is cash-flowing?

## Sources

All quantitative claims trace to `../entrepreneurial-pursuits/research-dossier-v2.md` (sections 1A
incumbents, 1B AI-gap/TAM, 1C buyer; verification: treatment-displaceable) and `REPORT.md` §3/§5/§7,
which carry the underlying inline citations (BlueBrix, PIMSY, SAMHSA N-SUMHSS, Cohere, Innovaccer,
HIT Consultant, etc.). Re-verify the `[VERIFY]`-flagged items (Kipu facility count, BAA path, specific
LA/payer rules) before acting.
