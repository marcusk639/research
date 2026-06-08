# Entrepreneurial Pursuits — Likelihood of Success & Realistic Income

> Status: synthesized (v1, B1 revised up) · Started: 2026-06-07 · Updated: 2026-06-07
> Research: 107-agent deep-research run + ~/dev/cpa-consulting prior analyses.

### Directory contents

- **`REPORT.md`** (this file) — primary synthesis: per-venture briefs, five-scenario
  income models, portfolio ranking, mission fit, next actions.
- **`research-findings.md`** — verified evidence ledger (8 findings, adversarially
  checked, with sources and caveats). All figures here trace to it or to the CPA analyses.
- **`archive/candidate-ventures-superseded.md`** — the original A–F option slate,
  superseded by the A/B/C framing below. Kept for the record; not current.

## Research Question

For a defined set of candidate entrepreneurial pursuits, assess each venture's
**realistic likelihood of success**, the **viable paths and option-sets** for getting
there, and the **annual income** it could plausibly produce. Income is modeled across
five explicitly-labeled scenarios — **unfavorable, conservative, base, optimistic,
aggressive** — under a deliberately skeptical, devil's-advocate lens that challenges
the assumptions behind every figure rather than projecting best-case outcomes.

## Method & Ground Rules

These rules govern every venture assessment below. They exist to keep the numbers
honest.

- **Devil's-advocate default.** Every claim of upside must survive an explicit
  counter-argument. State the assumption, then state what would have to be true for it
  to hold, then state why it might not.
- **Five income scenarios**, defined consistently across ventures:
  - **Unfavorable** — the idea is weak, the market is wrong, or execution stalls.
    Captures bad/unrealistic ideas and failure-to-launch. Often $0 or net-negative
    (time + capital burned). This is the modal outcome for most ventures and must not
    be omitted.
  - **Conservative** — the venture works but underperforms: slow growth, thin margins,
    heavy competition. A realistic floor for a venture that survives.
  - **Base** — the single most likely outcome given honest assumptions. This is the
    number that matters most; the others bracket it.
  - **Optimistic** — things break favorably: good timing, above-average execution,
    some tailwind. Plausible but not the expected case.
  - **Aggressive** — top-decile outcome. Explicitly flagged as low-probability; include
    the rough probability, not just the figure.
- **Income = annual, owner take-home**, net of realistic costs (COGS, tooling, ad
  spend, contractors, taxes-noted-separately where relevant). Distinguish revenue from
  take-home; revenue figures alone are misleading.
- **Probability-weight where possible.** A $500k aggressive case at 2% probability is
  worth less than a $90k base case at 50%. Note the expected value, not just the range.
- **Time-to-income and capital-at-risk** are first-class. A venture that pays $120k in
  year 3 after $60k of investment is not the same as one that pays $60k in month 6.
- **Cite sources inline** for every market size, comparable-earner benchmark, take-rate,
  CAC, or churn figure. Unsupported numbers are flagged as assumptions, not facts.

### Cross-Venture Scoring Rubric

Each venture is scored on the dimensions below so they can be ranked head-to-head.

| Dimension             | What it measures                                       |
| --------------------- | ------------------------------------------------------ |
| Likelihood of success | P(venture reaches at least the conservative case)      |
| Base-case income      | Most-likely annual owner take-home                     |
| Expected value        | Probability-weighted income across all five scenarios  |
| Time to first income  | Months until first meaningful revenue                  |
| Capital at risk       | Cash + opportunity cost required before base case      |
| Founder fit / moat    | Defensibility and match to the founder's skills/assets |
| Riskiest assumption   | The single belief that, if wrong, kills it             |

## Founder Context & Constraints (locked)

- **Profile:** Senior software engineer (Meta "Greatly Exceeds", Y-Combinator startups,
  CGI Federal, AI/LLM startups, MNTN ad-tech); USAF veteran (F-15 mechanic); CS degree
  in 3 years. Assets: high intelligence, extreme persistence/focus, authenticity,
  no-BS; high-functioning autism + high EQ. Domain assets: VA-disability corpus/RAG,
  agentic-engineering/Claude Code tooling, production LLM experience.
- **In motion:** internal AI/automation role at brother's ~20-person CPA firm. Comp:
  **$50k base + mediocre health insurance**, with a verbal agreement to **raise pay
  regularly against demonstrated, measured ROI**, plus a separate verbal share-of-value /
  revenue-share on the A3 advisory line. Proving ground to package and resell (analyzed
  in `~/dev/cpa-consulting`). _Risk note:_ "regularly" and "measured ROI" are undefined —
  must be pinned in writing (specific metric, measurement method, 90-day/6-month review
  cadence, raise thresholds), with upside attributed separately from base salary, and
  baseline metrics captured in the first 30 days before any changes. This is the chief
  family-business risk and a kill/pivot input for Pursuit A.
- **Goal:** comfortable life in **New Orleans, LA** (low–moderate COL), remote-first.
  Not optimizing for wealth; wants surplus to help others. **The metric that matters
  most is a reliable base case clearing ~$90–130k take-home at acceptable risk**, not
  the aggressive tail.
- **Geography (resolved):** New Orleans home base, **willing to travel for recovery
  ventures**, and holds **many recovery-industry contacts in the New Orleans area** (in
  addition to the Lake Charles network). The cold-start/customer-acquisition advantage
  for the recovery-tech cluster (B1/B2) therefore holds in **both regions**, and
  physical-presence needs (CPA on-site in Lake Charles; recovery network in either) do
  not conflict with living in New Orleans. Earlier "Lake-Charles-anchored" assumption is
  superseded.
- **Runway:** 12–18 months, likely extended by **expected severance** (FMLA-retaliation
  claim). Moderate cushion → some tolerance for ramp, but not unlimited.
- **Commitment:** **Door to conventional corporate/startup tech is closing by choice.**
  Opportunity cost is therefore measured against the _next-best realistic alternative_,
  NOT a $150k+ corporate-comp baseline. This materially improves every venture's verdict
  vs. the prior CPA analysis, whose largest drag was forgone corporate salary.
  Corollary: a purely financial optimum (e.g. fractional contract tech) may conflict
  with the explicit desire to leave that world — life-fit and money verdicts are scored
  separately where they diverge.

## TL;DR — Recommended Prioritized Path

Verified evidence in `research-findings.md`; CPA internal-role economics in
`~/dev/cpa-consulting`. Income figures are **reasoned estimates** (labeled `[est]`)
built on **verified** market data (labeled with finding #). All are **annual owner
take-home, New Orleans COL, judged vs. your next-best realistic alternative** (you are
leaving corporate tech by choice, so the old $150k+ opportunity-cost drag mostly
does not apply).

1. **The income engine is Pursuit A — specifically A3 (advisory) layered on A1 — not the
   recovery apps.** CAS/advisory is the fastest-growing, ~50%-margin (pre-partner-comp)
   accounting segment [F1], and tech-strong CAS firms bill ~$181k revenue/professional
   [F2]. That is the one track that simultaneously pays the bills, scales by employing
   people (your mission), and rests on a warm channel (the brother). **This is the bet.**
2. **The single most important decision: convert the verbal comp deal into a written,
   metric-based agreement before you do real work** — defined ROI metric, measurement
   method, 90-day/6-month review cadence, raise thresholds, and the A3 advisory
   profit-share attributed _separately_ from base salary. Capture baseline firm metrics
   in the first 30 days. Everything in A's income model floats on this; it is also the
   chief family-business risk.
3. **Sequence, don't parallelize. A funds B.** Your runway (~$50k cash, $50k base) means
   ~18–24 months of savings drawdown before raises/advisory close the gap. You cannot
   afford to split focus onto a regulated, two-sided, healthcare-sales recovery product
   in year one. Recovery-tech is **year-2+ money funded by A's stability.**
4. **Within recovery, the ranking is B3 ≳ B1 ≫ B2 for near-term, and B2 only with eyes
   open.** B3 coaching is fast cash + meaning but unscalable and off-mission. B1 is a
   modest, low-ceiling business your network can actually seed. **B2 is the most
   ambitious and the most dangerous** — the aftercare pivot triggers 42 CFR Part 2 +
   HIPAA-grade obligations [F4] that are brutal for a solo founder; the 12-step side has
   no payer and anonymity/branding constraints. Pick **one** B-track, not the ecosystem.
5. **SDVOSB (C) is a real but long-dated multiplier — and likely available to you NOW.**
   SDVOSB eligibility needs only a _service-connected_ disability with **no minimum
   percentage** [F6 + synthesis note], so your 10% tinnitus rating probably already
   qualifies you; the 50%+ rating you're pursuing drives disability _income/healthcare_,
   not SDVOSB status. Federal awards are 12–24+ months out [F7] — treat as optionality
   layered on a standalone software/advisory entity, not as income you plan around.
6. **Mission fit and money converge on the same answer: build A3 into a standalone
   fair-wage automation/advisory firm.** Services scale by hiring people; SaaS (A2/B1/B2)
   and solo coaching (B3) do not employ many. The path that best realizes "employ people,
   pay fair wages" is also the highest-probability income path. That is unusual and worth
   acting on.

---

## Per-Venture Briefs

Probabilities are P(reaches ≥ the _conservative_ row within ~3 years). Base-rate logic
shown. Income = your annual take-home at ~Year 2–3 steady state unless noted.

### A1 — Internal efficiency & automation (the foundation, not the paycheck)

- **Reality:** Real, validated pain (document chasing, Karbon/Onvio/SharePoint
  under-configuration) per the prior firm analysis. But A1 is **firm value, not your
  income** — it only pays you indirectly by justifying ROI-linked raises. Value is
  captured **only if freed capacity converts to billings/margin**, which requires the
  brother to sell, not just you to build.
- **Base rate:** digital-transformation success ~30% [F-baserate]. **Adjusted up** to
  ~High for _delivering some measurable value_ (embedded access, real skill, validated
  pain, willing employer); **left at moderate** for _full value-capture_ (depends on
  partner-led billing conversion, outside your control).
- **Your income from A1 alone:** the $50k base + whatever raises the demonstrated ROI
  justifies. Realistically $50k → $65–75k over 18–24 months.
- **Kill/pivot:** if by Month 6 no baseline-vs-after metric improved and the brother
  won't commit ~1–2 hrs/week to review + client conversations, A1's ROI is theoretical —
  renegotiate scope or treat the role as a stepping stone only.

### A2 — Productize & resell to other CPA firms (the weak link of A)

- **Reality:** vertical SaaS against **entrenched, funded incumbents** — Karbon, TaxDome,
  Canopy, Financial Cents. Building a _product_ to out-feature them is a losing solo bet;
  these are the same caution the prior analysis rated "Low / 3–5 years / do not plan
  around." The realistic version is a **productized service** (repeatable engagement +
  templates), not SaaS.
- **Income scenarios `[est]`:**
  | Scenario | Income | Why |
  | --- | --- | --- |
  | Unfavorable | $0 | most likely 2–3 yrs; no external firm pays a solo vendor |
  | Conservative | $5–15k | 1–2 productized engagements via brother's referrals |
  | Base | $15–40k | a few firms, project-priced, slow |
  | Optimistic | $50–90k | a small repeatable service line to ~5–8 firms |
  | Aggressive (P≈5%) | $120k+ | genuine product traction |
- **Riskiest assumption:** that internal success transfers to firms with no warm tie.
- **Verdict: defer.** A2 is a Year-3 _output_ of A3 succeeding, not a Year-1 venture.

### A3 — Advisory/automation service line to the client network (the real prize)

- **Reality:** **highest-margin path in the whole portfolio.** CAS/advisory is the
  fastest-growing accounting segment, ~50% margin pre-partner-comp, >30% higher MRR than
  transactional work [F1]; tech-strong firms reach ~$181k revenue/FTE [F2]. The brother's
  wealthy mid-tier business clients are reachable warm — directly attacking the only
  thing that kills consulting (no pipeline). Lake Charles industrial/LNG mega-money goes
  to national firms, so target **mid-tier local owners**, not the majors.
- **Economics `[est]`, your take from a profit-shared service line:** if A3 lands even
  3–6 advisory/automation clients at $1.5–4k/mo and you profit-share, your slice is
  ~$20–60k/yr on top of base — and it grows with each client and any staff you add.
- **Income scenarios (A1+A3 combined, your take-home) `[est]`:**
  | Scenario | Income | Key assumptions | Why it might NOT happen |
  | --- | --- | --- | --- |
  | Unfavorable | $50k | role survives, no raises, advisory never launches | brother disengages; ROI undemonstrated |
  | Conservative | $60–75k | modest ROI raises, ~1–2 advisory clients | slow partner-led sales |
  | Base | $90–120k | raises to $65–75k + advisory share $20–45k | **most likely if comp is in writing** |
  | Optimistic | $130–170k | strong advisory line + early A2 productization | requires brother selling actively |
  | Aggressive (P≈10%) | $180–250k | advisory scales as a real service line you staff | multi-year; needs hiring |
- **Expected value `[est]`:** ~$95–110k/yr by Year 3 (probability-weighted), the highest
  risk-adjusted figure in the portfolio.
- **Likelihood ≥ conservative: High (~75–80%).** Base rate for the _internal role_ is
  high (prior analysis); advisory adoption is the swing factor.
- **Riskiest assumption:** that the brother will _actively sell_ advisory services, not
  just let you build tools. Mitigant: write the profit-share so his incentive aligns.
- **Devil's-advocate:** the CAS figures are from a **self-selected survey of firms
  already winning at CAS** [F1 caveat] — treat as a ceiling, haircut hard for a firm just
  starting. A "fast-growing segment" can still mean _the firm_ grows slowly.

### B1 — Sober-living management app + directory ⬆️ UPGRADED

- **Demand is partly validated (founder evidence, 2026-06-07):** a prior MVP — few
  features, minimal compliance — **took on paying customers with no real marketing.**
  That is the most valuable single signal in this portfolio: it answers the question that
  kills these apps ("will lean operators actually pay?") with a _yes_, via the founder's
  warm network/word-of-mouth. \*\*[VERIFY: how many paid, at what price, did they retain
  > 6 months?]\*\* — early word-of-mouth buyers can be a small ceiling, not proof of a
  > scalable market, so size this before over-weighting it.
- **Revised monetization — per-house, not per-seat (founder's new model):**
  | Tier | Price | Features |
  | --- | --- | --- |
  | Starter (free) | $0 | 1 house, ≤6 guests, basic activity log |
  | House | $49/house | unlimited guests, payments, chat, reporting |
  | Oxford | $79/house | House tier + Oxford governance suite |
  | Network | custom | multi-house orgs, bulk billing, API access |
  Per-house **undercuts** the per-seat incumbent (a 2-seat house ≈ $100/mo on Sobriety Hub
  [F3] vs. $49–79 here) — easier to land, but **lower ACV → more houses per dollar.** The
  free Starter tier is a funnel but can cannibalize small paying houses; the ≤6-guest cap
  is the right gate.
- **Three real differentiators competitors lack** (the actual moat, not features):
  1. **Oxford House wedge** — no app targets the Oxford model's governance (weekly
     business meetings, officer roles, EES/equal-expense-share, chapter structure); a
     large, underserved, self-governed network (~3,000+ houses). _Caveat:_ Oxford culture
     is famously **frugal/anti-spend** (self-supporting tradition) — confirm houses pay
     $79, and check Oxford House Inc. trademark/partnership posture before branding on it.
  2. **Directory + in-app applications** — prospective residents search free and apply;
     a genuine **two-sided flywheel** (residents fill beds → houses adopt → directory
     grows), the thing that turns a tool into a network.
  3. **Homegroups + treatment-center ties** — cross-product distribution no competitor has.
- **Revised math `[est]`:** blended ~$55–65/house/mo → to net ~$90k take-home (solo, low
  cost) ≈ ~$9–11k MRR ≈ **~150–200 paying houses** (~1% of US recovery residences). With
  prior paid traction + warm network + Oxford wedge + directory flywheel, a few hundred
  houses over 2–3 years is **credible, not heroic.** The **payments take-rate** is the real
  upside lever — a small fee across houses × residents × ~$500–900/mo rent compounds far
  faster than per-house SaaS and is what could push B1 to salary-replacement.
- **Income scenarios (revised up) `[est]`:**
  | Scenario | Income | Why |
  | --- | --- | --- |
  | Unfavorable | $0–5k | churn; free tier cannibalizes; ~70% SaaS base rate still applies |
  | Conservative | $10–25k | 50–100 houses (warm network + returning prior customers) |
  | Base | $30–60k | 150–300 houses; Oxford wedge + directory pulling adoption |
  | Optimistic | $80–130k | 500+ houses + payments take-rate + treatment-center referral deals |
  | Aggressive (P≈10%) | $150–250k+ | category leader in Oxford/independent segment; payments + directory monetized |
- **Likelihood ≥ conservative: High (~70–75%)** given validated prior paid demand; **≥
  base: Moderate-High.** (Up from Moderate.)
- **Regulatory:** **light** — sober-living operational/resident data is largely outside
  42 CFR Part 2 [F4 contrast]. Keep payments PCI-scoped via Stripe (don't store cards);
  anonymized resident handles keep you clear of the heavy regime. **Do not let the
  directory/applications quietly pull clinical or treatment-linked data into scope** —
  that's the line between B1 (light) and B2 (heavy).
- **Riskiest assumption:** that prior word-of-mouth paid traction _scales_ past the warm
  network at the per-house price, and that the payments take-rate (the real upside) gets
  built and adopted.
- **Verdict: the B-track to ship.** A partly-validated, on-mission (can employ a small
  team), low-regulation small business with a genuine network wedge — still **funded by A
  and sequenced after the A3 income inflection**, but no longer a "maybe."

### B2 — "Homegroups" / treatment-center aftercare (most ambitious, most dangerous)

- **Reality:** two fused products with opposite economics. The **12-step ops side** has a
  strong cold-start asset (100k+ meetings, 50k+ groups seeded) but **no payer** (groups
  are broke) and real **AA anonymity-tradition + AA World Services trademark** constraints
  on "claim your meeting/group" branding. The **aftercare side** has a real payer
  (treatment centers, behavioral-health software with players like CaredFor) **but
  triggers the heavy regulation.**
- **Demand for the aftercare payer is partly validated (founder evidence, 2026-06-07):**
  the founder has direct industry confirmation that **treatment centers actively want
  post-discharge contact** to monitor alumni progress and re-engage them on relapse
  (which is frequent). This is real and well-known — it strengthens the _payer-exists_
  side of the thesis. **Two hard caveats remain:** (1) "wanting a capability" ≠ budget +
  procurement + adopting a solo vendor's tool, so the willingness-to-_pay_ at a real
  price is still **[VERIFY]**; (2) a tool whose explicit purpose is alumni monitoring and
  **re-admission** is squarely **SUD treatment data → full 42 CFR Part 2 + HIPAA**, and
  the re-entry framing carries optics risk (it resembles the for-profit-readmission
  criticism of the industry) — structure it as _patient-benefiting continuity of care_,
  not a readmission funnel, and keep any money flows clear of EKRA [F5].
- **Regulatory (decisive) [F4]:** any product touching treatment-center SUD data inherits
  **42 CFR Part 2 + HIPAA-grade** obligations — **HIPAA Breach Notification (60-day),
  BAAs with every center, audit controls.** Compliance deadline (Feb 16, 2026) is
  **already past**, so you must be compliant _before_ selling, not "on a runway." For a
  solo founder this is **$10–40k+ `[est]` and months** of setup before first dollar.
- **Income scenarios `[est]`:**
  | Scenario | Income | Why |
  | --- | --- | --- |
  | Unfavorable | $0 | most likely; compliance cost or no payer sinks it |
  | Conservative | $0–10k | one pilot center, post-compliance |
  | Base | $20–60k | a few centers paying for aftercare |
  | Optimistic | $80–150k | CaredFor-like positioning + VA angle [F8] |
  | Aggressive (P≈5%) | $200k+ / acquisition | category traction |
- **Likelihood ≥ base: Low-Moderate, and only after the compliance investment.**
- **VA angle [F8]:** VA _does_ buy external digital behavioral-health tech (Mission
  Daybreak, 9/10 winners digital) — a real positioning option, but mental-health-broad,
  not SUD-specific, and long-dated. Pairs with SDVOSB (C).
- **Riskiest assumption:** that you can carry Part 2/HIPAA compliance solo _and_ sell into
  slow healthcare buyers _and_ not starve Pursuit A. **This is the portfolio's biggest
  attention sink.**
- **Verdict: do not start in Year 1.** If pursued later, **split the products** — ship the
  _non-regulated_ 12-step/community piece if it ever finds a payer, and treat aftercare as
  a separate, compliance-funded, VA-positioned bet only once A is paying you.

### B3 — Early-withdrawal recovery coaching/consulting

- **Reality:** fastest-to-cash in B, near-zero capital, deep authentic fit. Recovery-coach
  rates run ~$50–150/hr; premium "recovery concierge"/family-retainer positioning can
  reach $150–400/hr or monthly retainers `[est, market-rate range]`. Your network + lived
  experience + resources are a genuine edge.
- **Regulatory (decisive) [F5]:** **EKRA** criminalizes any facility-side referral
  payment (up to $200k/10 yrs per occurrence). **Lawful structure = bill families/clients
  directly; never take money from a treatment center for sending them clients.** Stay
  explicit about not being a licensed clinician; for dangerous withdrawal, refer to
  medical care (you already do this).
- **Income scenarios `[est]`, part-time alongside A:**
  | Scenario | Income | Why |
  | --- | --- | --- |
  | Unfavorable | $0–5k | sporadic, unpriced |
  | Conservative | $10–25k | a few family-retainer clients, part-time |
  | Base | $25–50k | steady part-time coaching |
  | Optimistic | $60–100k | premium positioning, near-full-time |
  | Aggressive (P≈10%) | $120k+ | concierge/interventionist niche |
- **Likelihood ≥ conservative: Moderate-High** (low overhead, warm demand).
- **Riskiest assumption / verdict:** **it doesn't scale and it's off-mission** — it's
  _you_ selling hours, which can't "employ people at fair wages." Best framed as a
  **meaning-and-supplemental-income activity**, and a referral/credibility feeder for
  B1/B2, **not** the business you build.

### C — SDVOSB as cross-cutting leverage (multiplier, not a venture)

See the dedicated section below.

---

## SDVOSB Leverage Analysis (Cross-Cutting)

- **Eligibility is likely available now.** SDVOSB requires a _service-connected_
  disability with **no minimum rating** [F6 + synthesis]; your 10% tinnitus rating
  probably already qualifies. **[VERIFY this with SBA — it could move the whole C
  timeline forward by months.]** The 50%+ rating you expect matters for disability
  income/healthcare, not SDVOSB status.
- **Mechanics are now easy:** SBA VetCert, ≥51% veteran ownership, ~12-day processing,
  backlog cleared, mandatory gateway since self-cert ended Dec 2024 [F6].
- **Value is real but long-dated [F7]:** ≥5% government-wide + ≥7% VA set-aside goals,
  mandatory Rule of Two (Kingdomware), SDVOSB-first priority, $5M sole-source. **First
  awards 12–24+ months out** — a layered option, not near-term income.
- **Best synergy:** wrap your standalone software/advisory work (the A3 firm, or a
  B2 aftercare product) in an SDVOSB entity and position toward **VA behavioral-health**
  demand [F8]. Credibility credential when selling to CPA firms and treatment centers is a
  minor but free bonus.
- **Honest needle-moving vs. hype:** SDVOSB does **not** create demand or income on your
  runway timeline. It is a **medium-term moat** for a software entity that already has a
  product and the appetite for federal sales cycles. Get certified early (cheap, fast),
  but **do not let "federal contracts" become a reason to build B2** — that's the hype
  trap.

---

## Portfolio Synthesis — Risk-Adjusted Prioritization

| Rank | Track                            | Base income `[est]` | P(≥conservative) | Time-to-income             | Capital at risk                | Mission fit          |
| ---- | -------------------------------- | ------------------- | ---------------- | -------------------------- | ------------------------------ | -------------------- |
| 1    | **A3 (+A1)** advisory/automation | **$90–120k**        | **High ~75–80%** | now (base), 12–24mo (full) | low (salaried)                 | **High** (staffs up) |
| 2 ⬆️ | **B1** sober-living app          | **$30–60k**         | **High ~70–75%** | 6–18mo                     | low-med (your time)            | Med (small team)     |
| 3    | **B3** coaching                  | $25–50k             | Mod-High         | fast (months)              | ~$0                            | Low (solo)           |
| 4    | **C** SDVOSB                     | $0 direct           | n/a (multiplier) | 12–24mo+                   | low (cert cheap)               | enables #1/#5        |
| 5    | **A2** productize                | $0–15k              | Low-Mod          | 24mo+                      | med                            | Med                  |
| 6    | **B2** aftercare                 | $0–20k              | Low              | 12–24mo+ (post-compliance) | **high** ($10–40k+ compliance) | Med-High if scaled   |

> **Update (2026-06-07):** B1 promoted from #3 to #2 on validated prior paid demand
> (no-marketing customers), the per-house pricing model, the Oxford-governance wedge, and
> the directory flywheel. It now outranks B3 because it is on-mission (can employ a team),
> partly demand-validated, and has a real network moat — whereas B3 is a solo hours-for-
> dollars practice. A3 is still #1 and still the bet; B1 is the recovery track to ship.

**Sequencing tied to runway:**

- **Months 0–6:** Land Pursuit A properly. Written comp/profit-share + baseline metrics +
  the 3 highest-ROI internal fixes. File SDVOSB (cheap, parallel). **Do not build
  recovery products.** Optionally take a _handful_ of B3 coaching clients (near-zero
  setup) for cash + meaning + market signal.
- **Months 6–18:** Launch the A3 advisory line (the income inflection). If it's working,
  this is where raises + profit-share close the runway gap. Begin **one** B-track on
  nights/weekends — **B1** is the sane choice (light regulation [F4], warm network,
  shippable). Prioritize B1's **payments rails** over per-seat pricing [F3].
- **Months 18–36:** If A3 is paying, decide whether to spin it into a standalone
  fair-wage firm (mission path). Re-evaluate B2 **only** if (a) A is stable, (b) you've
  confirmed real treatment-center budgets, and (c) you'll fund Part 2 compliance. Layer
  SDVOSB/VA positioning on whichever software entity is real.

**Shared infrastructure (genuine reuse):** a reusable RAG/automation/agent stack built
for A1 transfers to A3 advisory delivery and to B1/B2 features; your VA-disability corpus
and SDVOSB status feed the VA-behavioral-health positioning of B2. The _engineering_ is
reusable; the _go-to-market and regulation_ are not — don't let tech reuse fool you into
thinking the businesses are one effort.

**Focus-conflict warnings:** B2 is the attention black hole — healthcare compliance +
two-sided marketplace + slow enterprise sales, the three hardest go-to-markets at once.
Running B2 in Year 1 is the most likely way to under-deliver on A and burn the runway with
nothing paying. **The portfolio's main failure mode is not picking a bad venture — it's
running too many at once.**

---

## Mission Fit — The Fair-Wage, People-Employing Goal

The configuration that best realizes "run my own business, employ people, pay fair wages"
is **A3 grown into a standalone automation/advisory firm.** Reasoning:

- **Services scale by hiring.** An advisory/automation firm adds people to add capacity —
  that _is_ the employ-people model, and CAS margins [F1] can fund fair wages.
- **SaaS (A2/B1/B2) employs few** even when it works — that's the point of software
  leverage, but it's the opposite of your stated mission.
- **Coaching (B3) is you selling your own hours** — meaningful, but structurally a
  solo practice.
- **Tension vs. speed-to-income:** none, for once. The fastest reliable income (A3) is
  also the best mission vehicle. The only real tension is _patience_ — building a firm
  that employs people is a 3–5 year arc, and B3/B1 may pay sooner per-dollar-of-effort
  while employing no one. Don't let the quick-cash tracks quietly become the whole plan.

---

## Recommended Next Actions (sequenced, with triggers)

1. **[Week 1–2] Put Pursuit A's comp in writing.** Metric, measurement, review cadence
   (90-day/6-month), raise thresholds, and the A3 advisory profit-share **separate** from
   base. _Trigger to proceed:_ signed one-pager. _Kill signal:_ brother won't define
   "measured ROI" → treat the role as a temporary stepping stone, not a venture.
2. **[Month 1] Capture baseline firm metrics** before changing anything (document-chasing
   hours, blocked engagements, extension rate, time-to-ready-for-prep). Without this, no
   raise conversation can be evidence-based.
3. **[Month 1, parallel] File SBA VetCert** — and **verify SDVOSB eligibility at your
   current 10% rating** (likely yes). Cheap, fast, unlocks the C optionality early.
4. **[Months 2–6] Ship the 3 highest-ROI internal fixes** (per prior analysis: template
   standardization, SharePoint→practice-mgmt intake, exception alerts). Produce **one
   shareable before/after result** by Day 60.
5. **[Months 4–6] Stand up the A3 advisory offer** with the brother actively introducing
   2–3 mid-tier client owners. _Trigger to scale:_ first paid advisory engagement.
   _Kill/pivot:_ zero advisory traction by Month 12 → A is an internal ops job, reassess.
6. **[Optional, low-effort] Take 2–4 B3 coaching clients**, billed **directly to
   families/clients** (EKRA-safe [F5]), for cash, meaning, and market signal. Keep it a
   side activity.
7. **[Months 6–18] Begin ONE recovery track — default B1.** Prioritize payments rails
   [F3]; keep data out of Part 2 scope [F4]. _Trigger to invest more:_ 15–20 paying homes
   from the warm network. _Kill:_ <10 homes after 6 months of real outreach.
8. **[Month 18+] Decide the firm.** If A3 is paying, formalize the standalone fair-wage
   firm. Reconsider B2 **only** against the three preconditions above.

---

## Key Assumptions, Unknowns & Sensitivity

The conclusions are **most sensitive** to four unverified items (from
`research-findings.md` open questions):

1. **Brother's firm revenue + realized rate (~$150–200/hr?) + profit-share terms** —
   gates the _entire_ A income model. **If the profit-share is vague or the firm is
   smaller/less advisory-ready than assumed, A3's base case slides toward conservative
   ($60–75k).** Highest-leverage thing to nail down. **[VERIFY]**
2. **VA rating/timing + SDVOSB-at-10% eligibility** — if (as expected) you're already
   eligible, Track C accelerates ~6–12 months. Doesn't change income near-term. **[VERIFY]**
3. **Treatment-center budgets / willingness-to-pay for aftercare (B2)** — unquantified;
   if low, B2 collapses to Unfavorable regardless of compliance. **[VERIFY before any B2
   spend]**
4. **Solo Part-2/HIPAA compliance cost & timeline for B2** — if it exceeds near-term B2
   revenue (likely, given lean budgets), B2 is a net-negative Year-1 move. **[VERIFY]**

**Standing caveats:** CAS economics [F1/F2] come from a self-selected survey of
_successful_ CAS firms — a ceiling, not your expected value; apply a haircut. CAS margin
is **pre-partner-comp**, not net profit. Sober-living pricing [F3] is one incumbent's
page, not a market study. SDVOSB processing speed [F6] is a self-reported government
snapshot. Mission Daybreak [F8] shows mental-health (not specifically SUD) demand and one
challenge's mix ≠ standing procurement policy. None of these refute the figures; they
bound how hard you should lean on each.

---

## Sources

Full citations with verification votes in **`research-findings.md`** (8 findings, all
HIGH confidence, 3-0 or 2-1, zero refuted). Prior CPA viability and ROI analyses:
`~/dev/cpa-consulting/cpa-consulting/docs/strategy-eval/` (venture-viability-analysis.md,
venture-worthiness-assessment.md). Primary sources cited inline by finding number (F1–F8):
AICPA/CPA.com 2024 CAS Benchmark Survey; Sobriety Hub pricing; HHS 42 CFR Part 2 Final
Rule fact sheet; 18 U.S.C. §220 (Cornell LII); SBA VetCert + VAAR 819.70; VA Mission
Daybreak press release.
