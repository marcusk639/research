---
title: Recovery-Industry Venture — Strategic Options Memo
date: 2026-10-06
revision: 2 (post-adversarial-review)
status: private planning draft — option evaluation only
scope:
  Evaluation of options and the assumptions each depends on. Not a commitment, not a launch
  plan, not a revenue projection. No action in this document has been taken or decided.
---

# Recovery-Industry Venture — Strategic Options Memo

**Prepared:** 2026-10-06 · **Revision 2**, following an adversarial review that overturned several
conclusions in revision 1. Corrections are noted inline where a prior figure was wrong, because
the wrong figures circulated in earlier planning and should not survive quietly.

**Nature of this document:** private option-evaluation and assumption-mapping. Where it uses
numbers, they are sensitivities — what would have to hold for an outcome to occur — not forecasts.

---

## 0. Executive summary

### The finding that matters most

The corpus already records the number this decision turns on, and no prior planning document put
it next to the venture's own economics:

> "a 3–5 year path to mere income recovery (back to your prior ~$145K corporate-engineer comp)"
> — `COMPARISON-cpa-vs-recovery.md:33`

Against that benchmark, the corrected commercial model says: **at 100 paying houses — roughly 5+
years out at the growth rate this plan itself assumes — net owner income lands around $105–140K.
That is at or below the ~$145K baseline.** Revision 1 of this memo claimed "$150–250K owner income
in 2–3 years." That was wrong in three compounding ways (inflated per-house revenue, no cost
stack, and a growth rate 2–3× the one stated elsewhere in the same document). The corrected
picture is materially less attractive.

### What follows from that

The honest conclusion is not "lead commercial instead of federal." It is narrower and less
comfortable:

1. **The commercial sober-living SaaS path is a validation engine and a modest income, not a
   replacement for a staff engineering salary.** It is real, it has real customers, and its
   realistic ceiling is approximately a lateral move at best, arriving slowly.
2. **The federal (SDVOSB) channel is the only path in this analysis with a non-trivial chance of
   exceeding the prior compensation baseline** — the verified existence proof is a single
   $4,999,203 sole-source award to a solo-scale SDVOSB in exactly this category. It is also slow,
   lumpy, relationship-driven, and unvalidated by any live solicitation.
3. **Therefore the question this memo cannot answer, and which dominates everything below, is
   whether a 5-year path to approximately-prior-income is worth taking at all** versus continuing
   employment while holding these assets as options. That is a values question about autonomy,
   meaning, and risk appetite, not a spreadsheet question. The analysis can only make the price
   visible.

### What is genuinely good news

- Regroup has **five houses paying today** — the only validated willingness-to-pay in the
  portfolio. But see §1: they pay **$9.99–$19.99/mo**, not the $65–$300 the market's visible
  competitors charge, and their contractual ceiling is ~$90–103, not $129.
- Engineering is **days from a reliable private-pilot transaction**. Public paid launch is not
  days away — it is gated behind credential rotation, a HIPAA decision, and an unestimated
  app-store review.
- The actual defensible wedge is clearer than the one revision 1 chose: **incumbents explicitly do
  not integrate.** `research-dossier-v2.md:460`: "Integration + the Oxford-specific workflow is
  the defensible wedge, not price."

### The cheapest next step is unchanged and still correct

A week of conversations with the five existing operators plus two database queries settles most of
the load-bearing unknowns at zero cost. Nothing below should be built before that happens.

---

## 1. What is actually built, and what customers actually pay

| Product                         | State                                                                                                               | Revenue today                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Regroup** (sober-living ops)  | RN 0.72 + Firebase + Angular 9 web (EOL). Tier billing, server-side entitlement, mobile paywall shipped 2026-10-02. | **5 houses at $9.99–$19.99/mo**     |
| **Homegroups** (12-step groups) | Feature-complete V1–V4.3 (90 callables, 17 triggers, 14 scheduled jobs). Facility dashboard built and tested.       | $0 — intergroup/TC checkout blocked |
| **detox-recovery** (NextStep)   | Next.js 15, code-complete, unlaunched.                                                                              | Tier-2 calls + donations only       |

### The validated price is an order of magnitude below the target price

This is the correction that most changes the picture, and revision 1 omitted it entirely:

- Legacy plan is **$10 + $1/resident/month** (`_shared/decisions-log.md:29`).
- "every paying operator was charged **$9.99–$19.99** instead of the $39–$99 target"
  (`regroup/docs/go-to-market/monetization.md:231`).
- `regroup-launch-readiness.md:172` calls that pricing **"unsustainable."**
- The resolved grandfather decision (D-9) locks legacy houses at **"~20–30% off the standard tier,
  locked for the lifetime"** (`monetization.md:204`) — so **those five houses top out near
  $90–103/mo, never $129.**

So "five paying customers" validates that operators will pay _something_. It does not validate the
$129 tier, and revision 1's juxtaposition of "only validated willingness-to-pay" with "competitors
charge $65–$300" implied a reachability that the data does not support. **Whether operators will
pay $129 is unvalidated and is the single highest-value question in this document.**

### detox-recovery is a liability line, not an asset line

Five paid PDFs render live buy buttons with dead links. Charging for an undeliverable product is
the only active exposure in the portfolio. Hide the buttons or ship the files.

### Engineering: days to a pilot, not days to a launch

Remaining Regroup blockers are deploy plumbing and observability, not features — and the
verification confirmed each:

- `deploy-batched.sh` hardcodes 40 functions against 53 real ones: **14 live functions never
  deploy, including the entire tier-billing and invitation surface.** A dead function name makes
  the batch hard-error while `|| echo … continuing` masks it and exits 0 regardless.
- All 12 `STRIPE_PRICE_*` vars and `TIER_BILLING_ENABLED` exist only in a gitignored local `.env`.
- Rollback is **not symmetric**: tier-less subscriptions created with the flag off cannot later add
  a house or resident without manual Stripe-side migration.
- No error visibility anywhere — `ErrorBoundary` only `console.error`s, Crashlytics plugin never
  applied, functions have zero error-reporting dependencies. **A paying operator's failure goes
  unnoticed.**
- `scheduledRentCollection` never rethrows, so Cloud Scheduler logs SUCCESS when every charge
  failed.

**Gates before any _new, public_ paid use** (not blocking a private pilot with existing houses):
three leaked service-account keys requiring a git-history rewrite — multi-day and high-risk across
a monorepo; four E2E accounts live in production; 3 critical npm vulnerabilities; un-attorney-
reviewed ToS/Privacy; an undecided HIPAA BAA, which becomes **mandatory** the moment a house bills
insurance, runs MAT, employs clinical staff, or partners with a treatment center — exactly the
upmarket direction the strategy points toward; and **an app-store review that has never been
estimated, with neither app submitted and neither holding a confirmed app ID.** That last item is
the longest-lead thing on the critical path.

---

## 2. Market reality

### Sober-living software is populated, and the incumbents are larger than assumed

| Player                               | Position                                                                | Pricing                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Behave Health / Sober Living App** | **2,000+ operators** per their site                                     | Quote-only                                                                                                                                                        |
| **One Step Software**                | Category incumbent, broadest features                                   | Quote-only                                                                                                                                                        |
| **Sobriety Hub**                     | **1,000+ homes**; built by former recovery-house managers; 5.0 Capterra | **Per-seat:** $780/yr per Full User ($65/mo) + $240/yr per Client Manager ($20/mo) + $250 onboarding + **3.9% card**, fee **rolled onto the resident by default** |
| **Oathtrack**                        | Per-bed                                                                 | $2.99–7.99/bed                                                                                                                                                    |
| **HopeLinx**                         | AI features + GPS-verified attendance + Stripe Connect rent             | Not published                                                                                                                                                     |
| **Anchor Living**                    | **GPRA/NARR-aligned outcomes reporting**, credit reporting, offline PWA | Not published                                                                                                                                                     |
| **Sober Friend**                     | Positions against generic property management                           | Not published                                                                                                                                                     |

**Correction to both revision 1 and my own first correction.** Revision 1 said Regroup's pricing
is "market-correct, no repricing needed." My first-pass correction swung to "2–4.5× above the
visible $65 anchor." Both were wrong, because **Sobriety Hub is priced per-seat, not per-house** —
a house with three full users runs ~$195/mo plus 3.9% card. Regroup's $129 is _below_ that for a
multi-user house. The accurate statement: **the subscription tiers do not need repricing; the rent
fee is mid-revision** (`regroup-pricing-revision-plan.md`, moving 2% flat → method-aware), and
`regroup-pricing-justification.md:85` names the old model's exposure directly — "2% flat rent fee
can't be justified on ACH… This is the biggest exposure."

**Two hard consequences:**

1. **The wedge revision 1 chose is occupied.** "One-click NARR/funder-ready outcome report" was
   picked for maximum reuse of the existing data model. Anchor Living already ships NARR/GPRA-
   aligned outcomes reporting. Execution quality still differs, but it is not a differentiator.
2. **The lived-experience advantage is not unbuyable — a competitor already holds it.** Sobriety
   Hub was built by former recovery-house managers and is the fastest-growing player with the best
   reviews. Revision 1's claim that operator credibility is "genuinely hard for a funded
   competitor to buy" is retracted. It is a real sales advantage; it is not a moat, and it is not
   unique.

### The AI-documentation wedge is closed

Eleos Health raised $60M Series C and shipped **Eleos Compliance**, a clinical-documentation-
improvement product built with regulatory counsel retained by the National Council for Mental
Wellbeing, explicitly expanding into SUD. Ritten bundles claim generation, billing census, and a
dedicated UR module. Alleva ships an "Echo" scribe. **Do not build an SUD scribe or a BH
denial-prevention/RCM copilot.** The sibling `bh-rcm-copilot/` brief is retired.

### Homegroups: thinly contested, not unoccupied — and a structurally weak buyer

Revision 1 called this niche "a real gap." **Retracted.** `homegroups-strategic-decision.md`:

- `:56` — "Our treasury is better and more integrated than the standalone nonprofit
  (**Homegroup.Online**)" — a direct competitor doing exactly group treasury.
- `:67` — "'Better than Homegroup.Online _today_' is an **execution lead, not a structural moat**
  — they're a nonprofit that can hire a designer, and treasury features aren't proprietary."
- `:179` — also names `transparencytechnologies.ai`.
- `:20`, `:60` — the buyer is "a **structurally weak buyer**"; treasury-as-paid-SaaS has a
  "**hard ceiling, quality-independent**" because the payer is "a rotating volunteer treasurer
  spending **7th-Tradition funds**."

A 501(c)(3) competitor that can undercut indefinitely is a _worse_ competitor for a bootstrapper
than a venture-funded one. Modeled group-tier ARR is **~$2,892/yr** — and that is the group tier
specifically, not Homegroups total. Treatment-center sales, the theoretical upside, carry a
**3–12 month cycle** with explicit guidance: "**Don't plan revenue from TC sales in Year 1**"
(`homegroups-launch-readiness.md:279`).

There is also an unresolved **entity conflict**: `homegroups-strategic-decision.md:89` recommends
a **nonprofit or fiscally-sponsored** vehicle for the fellowship-facing product, which is not the
same entity as an SDVOSB LLC at ≥51% veteran ownership. These are two separate formation
decisions, and prior planning treated formation as one mechanical step.

### Market size: use the lower, physically-verified count

Revision 1 wrote "Use bottom-up house counts, not TAM" and then, ninety lines later, used a TAM
penetration argument. Both the instruction and the violation are instructive.

The ~17,900 residences / ~275,000 beds figure is rated **"weak" confidence** in its own source
(`recovery-ecosystem-validation.md:98`). RTI/NSTARR **physically identified ~10,358–10,558**
recovery residences (2020–21) (`docs/research/_work/verdicts.md:512`). Against that, Behave Health's
claimed 2,000+ operators and Sobriety Hub's 1,000+ homes represent a substantial share of the real
addressable base already served.

**"Low required penetration" is not evidence of achievability.** Market share is an output of a
sales process, not an input to one. Any volume target must be built bottom-up from named,
reachable houses.

---

## 3. The federal channel: slow, unvalidated — and the only path with real upside

**What is verified:**

- VA directed ~$10.2B (23% of prime dollars) to SDVOSBs in FY2024, exceeding its own goals.
- Kingdomware "Rule of Two" set-aside is mandatory; SDVOSB sits first in VA's priority order;
  sole-source authority runs to $5M (VAAR 819.7008, `REPORT-procurement-validation.md:70`).
- **Existence proof:** SDVOSB USVETSERV LLC won a **$4,999,203** sole-source VA award under NAICS
  541511 for mental-health technology (`REPORT-procurement-validation.md:16`). A solo-scale SDVOSB
  can win at the sole-source ceiling in this exact category.

**What is refuted and must not be relied on:** VA does not routinely set aside SUD/BH software
procurements. **Certification buys eligibility, not awards** — in one studied case VA sole-sourced
to WebMD Ignite despite 809 eligible SDVOSBs. The "inherit VAEC controls, skip FedRAMP" shortcut
does not work; realistic VA ATO is 6–18 months. IHT 2.0 ($14B/10-yr) went to nine established
primes — a subcontracting target, not an entry path.

**What was never validated:** no confirmed active VA/VHA solicitation in this category, from any
industry contact. The channel rests on a handful of data points.

**Timeline:** VetCert estimates conflict (~12 days post-backlog-clearance vs. 60–90+ days as the
conservative baseline). **Plan 90 days.** SAM.gov/VetCert data mismatches are the main controllable
cause of delay.

**Operational verdict (unchanged):** file it — a few hours and free — then build as though it will
never pay off. **Strategic verdict (new, and it cuts against revision 1's framing):** because the
commercial path's corrected ceiling sits at or below the ~$145K baseline, the federal channel is
the only route here with a non-trivial chance of clearing that bar. It should not _lead_ the plan,
and it cannot be _depended_ on — but describing it as merely "a cheap option" understates what it
is carrying.

**Also a correction to revision 1's framing of novelty:** June's plan already sequenced
commercial-first — "Convert to the VA channel (**months 3–12**): once VetCert-certified and demand
is confirmed, pursue… with the **proven tool**" (`addiction-recovery/REPORT.md:90`); "**Months
9–18+:** once VetCert is in hand, a reference deployment exists, and… an ATO path is real"
(`REPORT-procurement-validation.md:54`). Revision 1 claimed to "invert the center of gravity."
What actually changes is narrower: the federal channel should stop carrying the _narrative_ weight,
and the **Oxford House bulk-acquisition growth assumption underneath the commercial leg is
retired** (see §6, H2 risk).

---

## 4. The CPA arrangement as income floor — recalibrated

|                           | June assumption                               | Verified 2026-10-06                                                                                                                        |
| ------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Terms                     | $50K base + 20% revshare on net-new recurring | **Unsigned.** Only the $50K base is "confirmed." Revshare deferred: "worth a separate conversation once we're further in"                  |
| Firm scale                | ~20-person firm, $2.5M revenue                | ~30 across three firms sharing space; real unit is 11 core + 6 shared. Revenue corrected $3.5M → $2.5M → **$2.3M**                         |
| Modeled 3-yr ROI          | 245% base case                                | **59%**; conservative case **net-negative (−$84,250)**                                                                                     |
| Headline automation value | $279K/yr                                      | **$113,400/yr** (repo instructs to stop quoting the higher figure)                                                                         |
| Role                      | Non-CPA, influence-only                       | Redefined 2026-07-30 to "Integrator/Chief Strategy Manager" with real authority — enforcement provisions a first draft, **not yet agreed** |

**The variable-comp structure is close to unreachable on the model the firm is actually running.**
`_kickoff-2026-10-03/10-ARITHMETIC-VERIFIED.md:22-30`: gainshare break-even is **$2,511,144**
(revised $2,531,307) against ~$2.3M actual — **+9.2% revenue growth before a single dollar pays
out**. At $2,350,000, _above_ current revenue, "operating contribution is 588,855.50, below the
750,000 hurdle, so the pool is [zero]."

**Stated honestly:** that gainshare covers ten named staff and
`D1-CORRECTNESS-VERIFICATION.md:165` confirms "**Marcus is not among them**" — so it is not
directly a fact about the deferred revshare. But it is the firm's demonstrated posture on variable
compensation, and it reframes the conclusion from "upside is uncertain" to **"upside above $50K is
structurally improbable on the model in use."** The concrete negotiating ask that follows: a
revenue-share base that does **not** sit behind a ~10% growth hurdle.

**Timing.** A full active kickoff corpus exists at
`cpa-consulting/twk/operating-model/_kickoff-2026-10-03/`, dated 2026-10-01/02/03.
`00-RUN-STATE.md` derives: start ~Oct 16, plus the model's own "baseline first, 8–12 weeks" ⇒
**baseline completes mid-December to early January — at the Jan–Apr blackout edge.** (Revision 1
said "early December"; the source is later and lands _on_ the blackout, which sharpens rather than
softens the case for papering terms early.)

The family dimension is a real risk. Unsigned compensation plus newly granted authority over staff
including the brother who owns the book is a structure that generates conflict under stress. Paper
it while relations are easy — and before January, when both leverage and attention vanish for four
months.

---

## 5. Options, scored

### Option A — Federal-first

Lead with SDVOSB; commercial SaaS funds the wait.
**For:** the only path with a credible shot above ~$145K; $4,999,203 existence proof; legal
mechanics competitors cannot replicate. **Against:** 12–18 months minimum to first dollar; 6–18
month ATO wall; one proof point; no validated live solicitation; certification ≠ capture.
**Verdict:** do not _lead_ with it; do not _dismiss_ it. File, and let it mature.

### Option B — Commercial SaaS, distribution-led

Convert existing houses, sell through warm network, federal in background.
**For:** validated customers exist; near-zero CAC through warm network; engineering nearly done.
**Against:** no moat — a sales-and-service business in software clothing; seven real competitors,
two with 1,000–2,000+ accounts; the credibility advantage is already held by the fastest-growing
competitor; structurally high churn as houses themselves close; **corrected ceiling ~$105–140K net
at 100 houses, 5+ years out, at or below baseline.**
**Verdict:** the right _validation_ path and a legitimate modest business — but not, on these
numbers, a path back to prior compensation on a useful timeline.

### Option C — CPA automation primary, recovery secondary

**For:** simplest; immediate partial income. **Against:** unsigned; ROI collapsed 245%→59%;
upside above $50K structurally improbable; no equity; family-relationship risk; abandons five
paying customers.
**Verdict:** the correct answer if §7's validation comes back negative. Not obviously worse than
Option B on a risk-adjusted basis, which is itself a finding.

### Option D — Continue employment; hold the assets as options

Keep the apps in low-maintenance operation; file VetCert; do the week-one validation; decide later
with better information.
**For:** preserves the ~$145K+ baseline; costs almost nothing; every option above stays open; the
validation work is cheap and does not require leaving anything.
**Against:** indefinite deferral has its own cost in motivation and momentum; the apps decay
(Angular 9 is EOL).
**Verdict:** **this was absent from revision 1 and should not have been.** On the corrected
numbers it is the strongest risk-adjusted option, and the fact that revision 1 omitted the
status-quo baseline from a set of "options" was a framing failure, not an oversight.

### Option E — Sell or wind down

**Verdict:** premature. Solo pre-scale assets fetch 3–5× realized ARR, not the 8–15× health-tech
band. At five houses paying ~$15/mo there is nothing to sell.

---

## 6. Sensitivity model — what volume would be required

Revision 1's model used a single best-case house and called the output "replacement income." Both
were wrong. This is the corrected version, presented as sensitivity rather than projection.

### Per-house revenue is a tier-mix question

The Professional tier is capped at **≤20 residents, ≤3 properties** (`monetization.md:55`), so
revision 1's "mid-size 20-bed house at $129" was modeling the _ceiling_ of the band as the
average. The real distribution runs lower: average ~15.4 beds on the weak-confidence figures, and
the 4,324 Oxford Houses average **8.3 beds**, landing on the **$49** Oxford Standard tier
(`pricing.md:35`).

An illustrative mix — 20% × 20-bed Professional, 35% × 15-bed Professional, 25% × 10-bed Starter
($69), 20% × 8-bed Oxford ($49) — blends to roughly **$130–158/mo**, not $180–220.

### The rent-fee line depends on a rail the product deliberately discourages

The documented model is method-aware: **ACH flat $2/txn, card 0.75%** — and the repo's own
annotation says ACH is "Cheap, **to nudge bank payments**," while card is "a **resident-borne
disclosed convenience fee**" (`monetization.md:172-173`).

| Card share (20-bed house)      | Rent-fee revenue | Blended total |
| ------------------------------ | ---------------- | ------------- |
| 100% (revision 1's assumption) | $90/mo           | $219          |
| 50%                            | $65/mo           | $194          |
| 0% — all ACH                   | **$40/mo**       | **$169**      |

Revision 1 took the maximum _and_, in the same paragraph, recommended driving ACH adoption hard —
which halves the line it was justifying. A defensible planning assumption is **25–40% card**, not
100%. Note also that the competitive norm (Sobriety Hub) pushes processing fees onto residents, so
an operator-paid fee is a competitive disadvantage, and 0.75% gross is not 0.75% net of Stripe.

### Gross is not income

| Line                                                      | At 100 houses                |
| --------------------------------------------------------- | ---------------------------- |
| Blended gross                                             | **$156–190K/yr**             |
| Stripe on subscriptions (~3%)                             | −$4–5K                       |
| Hosting/Firebase at scale, tools, monitoring              | −$8–20K                      |
| Insurance (E&O / cyber, health-adjacent)                  | −$3–6K                       |
| Legal (BAA, ToS, ongoing), accounting                     | −$7–19K                      |
| **App-store fees — 15–30% on store-routed subscriptions** | **−$0–21K (D-11 undecided)** |
| Pre-tax net                                               | **~$120–165K**               |
| After self-employment tax                                 | **~$105–140K**               |

The source repo already carries a cost line revision 1 ignored: "$60K/year at 250 houses vs.
**$170K/year in estimated costs**" (`regroup-launch-readiness.md:213`). The in-app-purchase
decision (D-11, still open per `ecosystem/project-management.md:112`) is a major swing factor and
is unresolved. Chargebacks and solo support labor are unmodeled.

### The timeline arithmetic, made visible

At the growth rate this plan itself assumes — **3–5 houses per quarter** from a base of 5 —
reaching 100 houses takes:

| Rate      | Houses at 3 yrs | Time to 100 |
| --------- | --------------- | ----------- |
| 3/quarter | 41              | ~8 years    |
| 5/quarter | 65              | ~5 years    |

Revision 1's "100 houses in 2–3 years" requires **8–16 houses/quarter**, two to three times its own
stated assumption, with no justification. The corpus benchmark is slower still: "a 3–5 year path
to mere income recovery (back to your prior ~$145K)" (`COMPARISON-cpa-vs-recovery.md:33`).

**So: ~$105–140K net, arriving in roughly 5–8 years, against a ~$145K baseline.**

### What must be true

0. **Operators actually route rent through the platform, by card.** This is ~25–40% of modeled
   per-house revenue and was entirely unvalidated and unlisted as a risk in revision 1.
1. Operators will pay $129+. **Validated price today is $9.99–$19.99/mo**; the five legacy houses
   are contractually capped near $90–103.
2. The five houses migrate without churning — against a lifetime-locked 20–30% discount.
3. Warm-network referral produces 3–5 houses/quarter, sustained, as the **sole** growth channel.
4. Churn stays under ~3%/mo, in a market where customer businesses themselves close.
5. `DrugTest`/`Meeting`/`Phase` fields are actually populated. If sparse, **the outcomes-reporting
   wedge has no data to run on** and the first build becomes frictionless capture instead.
6. Solo support load at 100 B2B accounts remains survivable — unmodeled anywhere.

Assumptions 0, 1, 3, and 5 are all answerable in one week at zero cost. That is §7.

---

## 7. Lowest-cost ways to reduce uncertainty, in order of cost

Framed as experiments, not instructions — each is reversible and none commits to a path.

### Week 1 — customer truth (zero cost, settles the most)

1. Talk to all five operators: what they'd pay for that they lack; what would make them leave;
   whether $129 is conceivable; whether they'd accept moving off legacy pricing; what they use
   alongside Regroup.
2. **Query actual rent volume and the card/ACH split** across the five houses. Assumption 0 is
   ~25–40% of the revenue model and has never been checked.
3. Query field-population rates for `DrugTest`/`Meeting`/`Phase`. Check the database, not the
   self-report.
4. Confirm in Stripe that all five are in fact still active and paying — current belief rests on
   documentation, not a billing query.
5. Write down, in advance, what result would falsify the commercial path.

**Gate:** if operators won't move materially above ~$20/mo and compliance data is sparse, Option B
is not viable as written, and Options C and D become primary.

### Weeks 1–2 — stop the bleeding (mechanical, low risk)

6. Hide or fix the detox-recovery dead buy buttons — the one active liability.
7. Fix Homegroups' missing default Stripe prices (~20 min; unblocks **intergroup/treatment-center**
   checkout specifically, not all checkout).
8. Fix `deploy-batched.sh` (40→53) and remove the `|| echo … continuing` mask.
9. Commit `.env.phoenix-cleanhouse` so deploys are not laptop-bound.
10. Wire error reporting; make `scheduledRentCollection` rethrow. A paying customer's silent
    failure is the fastest way to lose the only validated revenue in the portfolio.

### Weeks 2–6 — cheap options, capacity permitting

11. File SBA VetCert and SAM.gov (NAICS 541511/541512/513210). Free; plan 90 days; then stop
    thinking about it.
12. **Two entity decisions, not one:** an SDVOSB-eligible LLC at ≥51% veteran ownership/control
    (13 CFR 128.200/128.300) for the operator and federal products, _and_ separately whether the
    fellowship-facing product belongs in a nonprofit or fiscally-sponsored vehicle per
    `homegroups-strategic-decision.md:89`. These are incompatible structures for one entity.
13. **Paper the CPA revenue-share definition before January**, with the explicit ask that it not
    sit behind a ~10% growth hurdle.
14. Credential hygiene: rotate the three leaked service-account keys (history rewrite — multi-day,
    high-risk, schedule deliberately), purge the four production E2E accounts, triage the 3
    critical npm vulnerabilities.

### Legal gates — before, not after

15. **Consult healthcare-regulatory counsel on EKRA and 42 CFR Part 2 before any referral-adjacent
    feature or revenue.** Flagged as blocking in every prior document; no evidence it has happened.
    Not tracked in the CPA repo (out of scope there) and confirmed nowhere else.
16. Decide the HIPAA BAA question before onboarding any operator who bills insurance, runs MAT, or
    partners with a treatment center.
17. Attorney-review ToS and Privacy.

### A capacity constraint that governs all of the above

The CPA engagement starts ~Oct 16 with a baseline completing **mid-Dec to early Jan**. That
consumes precisely the window items 6–14 occupy. Revision 1 scheduled five engineering fixes, a
git-history rewrite, certification filings, two entity formations, a compensation negotiation, a
new product build, five customer migrations, and 3–5 new sales into the same quarter as a new
full-time-shaped role. **That is not a schedule; it is a wish.** Items 1–5 (one week, zero cost)
and item 6 (one hour, liability-stopping) are the only things that credibly fit before January.

---

## 8. Risk register

| Risk                                                             | Severity     | State                             | Note                                     |
| ---------------------------------------------------------------- | ------------ | --------------------------------- | ---------------------------------------- |
| Operators won't pay $129+ (validated price is $10–20/mo)         | **Critical** | Unvalidated                       | Gates the entire commercial model        |
| Rent not routed through platform / ACH-heavy mix                 | **High**     | Unvalidated                       | 25–40% of modeled per-house revenue      |
| Net ceiling at/below ~$145K baseline, 5–8 yrs out                | **High**     | Confirmed by corrected model      | The central strategic problem            |
| Tier-mix dilution toward $49/$69 houses                          | **High**     | Structural                        | Oxford Houses avg 8.3 beds               |
| Wedge occupied (Anchor Living, HopeLinx)                         | **High**     | Confirmed                         | Re-pick from customer evidence           |
| Compliance data sparse in practice                               | **High**     | Unvalidated                       | Would void the outcomes wedge            |
| EKRA exposure on referral features                               | **High**     | Counsel never consulted           | Flat-fee only; $200K/10yr per occurrence |
| Author time capacity vs. CPA engagement                          | **High**     | Confirmed conflict                | Oct–Dec fully consumed                   |
| Solo support burden at 100 B2B accounts                          | **High**     | Unmodeled                         | Binding constraint on a service business |
| App-store review, unestimated, on critical path                  | **High**     | Neither app submitted             | No confirmed app IDs                     |
| Channel concentration — Oxford retired, warm network sole engine | **High**     | Confirmed                         | LTV ~$3.3k vs. 3:1 norm ⇒ low-CAC only   |
| Silent production failure for a paying customer                  | **High**     | Open                              | Weeks 1–2 fix                            |
| CPA terms unsigned; upside structurally improbable               | **High**     | Confirmed                         | Paper before January                     |
| Legacy migration churns the five houses                          | Medium       | Lifetime-locked 20–30% discount   | Relationship-led, not automated          |
| Structural churn (customer businesses close)                     | Medium       | Market characteristic             | Favor multi-house operators              |
| Leaked service-account keys                                      | Medium       | Latent                            | History rewrite required                 |
| Homegroup.Online (501c3) undercuts treasury                      | Medium       | Confirmed                         | Execution lead, not moat                 |
| Entity-structure conflict (SDVOSB LLC vs. nonprofit)             | Medium       | Unresolved                        | Two decisions, not one                   |
| Federal channel never converts                                   | Medium       | Likely on 12–18mo horizon         | Plan does not depend on it               |
| Family-relationship conflict at the firm                         | Medium       | Authority granted, terms unagreed | Paper while relations are easy           |
| Angular 9 web EOL                                                | Low-Med      | Confirmed                         | Not revenue-blocking                     |

---

## 9. Verify before relying

1. **The ~$145K baseline itself.** Taken from `COMPARISON-cpa-vs-recovery.md:33`. If actual prior
   total compensation was materially higher, every conclusion here gets worse, not better. This is
   the most load-bearing number in the memo and it came from a document, not from the user.
2. **Whether the five houses are still active and paying** — documentation, not a billing query.
3. **Whether Oct 3–5 commits closed the Android build break** — inferred from commit messages
   (AGP 7.4.2→8.1.1, minSdk 34→23), not from a successful store build.
4. **App-store review lead time** — entirely unestimated; longest-lead item on the critical path.
5. **Competitor feature depth** — Anchor Living and HopeLinx assessed from 2026 buyer's-guide
   summaries, not hands-on trials. Run trials before conceding or contesting the wedge.
6. **VetCert processing** — sources conflict (~12 vs. 60–90+ days). Confirm with SBA.
7. **VA SDVOSB spending and the IHT 2.0 roster** — FY2024-era, not re-verified at source.
8. **The ~17,900 residence count** — rated "weak" in its own source; NSTARR physically identified
   ~10,358–10,558. Prefer the lower figure.
9. **EKRA posture** — the Ninth Circuit's _Schena_ holding (percentage comp not per se unlawful
   absent "wrongful inducement") binds only the Ninth Circuit; a Supreme Court petition is
   pending; criminal enforcement continued through 2025. Needs counsel, not a memo.
10. **Whether the CPA role changed after 2026-10-03**, the newest kickoff document.

---

## 10. The bottom line

Revision 1 of this memo concluded there was "a realistic path to $150–250K owner income over 2–3
years." That conclusion does not survive its own arithmetic once per-house revenue is modeled on a
realistic tier mix, the rent-fee rail is set to what the product actually encourages, a cost stack
is included, and the growth rate is held to the one the plan itself states. The corrected figure is
**roughly $105–140K net at 100 houses, arriving in about 5–8 years, against a ~$145K baseline.**

That reframes the decision. The question is not "which venture?" — the prior research answered
that adequately. The question is **whether a five-plus-year path back to approximately the prior
income is worth the risk**, when the alternative is continuing to earn that income while holding
these assets as options, filing a free certification, and spending one week finding out what five
existing customers actually want.

What this is not: a venture-scale opportunity, a defensible technology moat, a path that works
because of the federal channel, or a plan that fits in the next quarter alongside a new role.

What it plausibly is: a modest, real, slow-growing niche business with genuine early customers and
a sales advantage that is helpful but neither unique nor durable — plus one low-probability,
high-ceiling federal option that costs almost nothing to hold.

The validation work in §7 items 1–5 costs a week and nothing else, requires leaving nothing, and
settles four of the six assumptions the whole commercial case rests on. **Whatever the eventual
decision, that week is worth spending first** — it is the only step in this document that is
clearly correct under every option, including the option of changing nothing.
