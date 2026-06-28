# BH-RCM Copilot — Feasibility Assessment & Build Plan

> **Companion to** `REPORT.md` (the venture brief). This document externally
> pressure-tests that brief against current (2025–2026) sources, re-rates its
> load-bearing claims, and converts the result into a go/no-go decision plus a
> concrete path to build a successful business.
>
> **Assessment date:** 2026-06-25 · **Method:** four parallel research streams
> (denial economics, competitive landscape, regulatory/technical feasibility,
> market sizing & pricing). Sources inline; full list at end.

---

## 1. Executive summary

**Verdict: QUALIFIED GO — but the thesis must be re-pointed, and the clock is now real.**

The underlying business is feasible. The pain is genuine, the regulated-data
moat is clearable on a shoestring, and the market supports a $50–150M-ARR vertical
outcome with a credible strategic exit. **But the brief's strategic centerpiece —
"no BH-native, AI-native denial-prevention copilot exists" — is no longer true.**
Since the brief was written, at least one YC-backed startup (**Adentris**, YC P25,
$1.8M pre-seed) has shipped almost this exact product, with two named SUD customers
running on ASAM 2.5/3.5 level-of-care logic and an explicitly Part 2-compliant
architecture. A second YC startup (**Aegis**) does general AI appeal automation, and
a well-funded general-RCM player (**Thoughtful AI / Smarter Technologies**) has
publicly named behavioral health as a target vertical.

This does not kill the venture. It **changes what the moat is.** The defensible
asset is no longer "being first to an empty category." It is the combination of
(a) the **warm CPA-client + lived-recovery distribution channel**, which no
venture-funded competitor has, (b) **depth in two denial vectors nobody has
productized — MHPAEA parity-argument generation and ASAM continued-stay UR
tightening**, and (c) **outcome-based pricing** that fits cash-constrained
operators. If Marcus is not willing to move on the validation gates within ~2
quarters, the honest call flips to "no" — a generic, slow entry into a category
that now has funded, faster competitors is a bad use of founder bandwidth.

**Net:** the venture's own framing was right to gate this. The gates are clearable;
the new information is that **speed and channel — not novelty — are now the whole
game.**

---

## 2. Claim re-rating — what survived external verification

The brief's ROI narrative is **directionally correct but quantitatively inflated**;
several headline numbers trace to circular RCM-vendor marketing, not primary data.
This matters because the pitch and the pricing both lean on them — using the weak
versions in front of a sophisticated operator or CPA will cost credibility.

| Brief's claim                                | External verdict                                                                                                                                                                  | What to actually say                                                                                                                                                                      |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BH denied ~85% more often (12–20% vs 5–10%)  | **Partially supported.** Directionally true; the "85% more" figure is vendor marketing with no primary source. BH-specific denial-rate breakouts aren't in CMS data until PY2027. | "BH/SUD denials run materially higher than medical — roughly 2× on initial submission — driven by prior-auth and concurrent review." Anchor on the _mechanism_, not the precise multiple. |
| 82–85% of denials preventable                | **Partially supported.** Backed by Optum's 2024 Denials Index ("84% potentially avoidable," 441M claims) — large but vendor-run.                                                  | Usable, with attribution to Optum/Change Healthcare.                                                                                                                                      |
| ~60% never resubmitted                       | **Weak / unsourced.** Traces to a 2018 vendor blog, recycled for 6+ years.                                                                                                        | Drop as a headline stat; replace with the live audit's _actual_ facility number.                                                                                                          |
| 81.7% of appeals overturned                  | **Real but mis-scoped.** That's HHS OIG **Medicare Advantage, 2014–2016**. Commercial appeals reverse ~44% (KFF ACA) to ~54% (Premier 2025).                                      | "A large share of properly appealed denials are overturned — roughly half on commercial, higher on MA."                                                                                   |
| BH orgs lose 20–30% of revenue to RCM errors | **Weak / unsourced.** Pure vendor marketing; no primary source. A conservative 10–20% also circulates.                                                                            | Use 10–20% as the defensible range; prove the real number per-facility in the audit.                                                                                                      |
| Payers increasing automated denials          | **Strongly supported.** Kodiak: initial denial rate 10.15%→11.81% (2020→2024). AHA: commercial denials +20.2%, MA +55.7% (2022→2023). Rework cost $43.84→$57.23/claim.            | The single best-supported pillar — **lead with this.** The arms race is real and growing.                                                                                                 |

**Bottom line on the economics:** retire the unsourced stats, anchor the pitch on
(1) the documented rising-denial / rising-rework-cost trend, (2) the documented
systemic MHPAEA parity-violation findings (DOL/EBSA, CMS, OIG), and (3) a **live,
audited per-facility denial-leakage number** from Phase 1. The ROI case is real;
it just has to be _earned per customer_ rather than asserted from a deck.

---

## 3. The competitive picture has changed — this is the decisive update

The brief's competitor table (Cohere/Innovaccer, Eleos/Commure, Kipu et al.) was
accurate as a _teardown of incumbents_ but **missed the startup layer that has since
emerged directly in the wedge.**

**The threat that matters — Adentris (YC P25, $1.8M pre-seed, three second-time YC
founders):** five-module AI platform including "Denial Fightback" (appeal
automation). Two named SUD customers — Resilient Recovery (LA multi-site, claims 62%
denial reduction, 7.6× ROI in 4 months) and Sobrius Health (VA, ASAM 2.5/3.5, 100+
patients under continuous AI review). Website explicitly claims **ASAM-level-specific
logic and 42 CFR Part 2 architecture** — the exact two pillars the brief treated as
proprietary differentiators. No HL7/API required (reads EHR UIs directly), 60-day
deploy. ([adentris.com](https://www.adentris.com))

**Other movement:**

- **Aegis** (YC X25) — general AI appeal generation, 2h→2min, 80% cost cut. Not
  BH-tuned, but the appeal-drafting primitive is now commoditizing.
- **Thoughtful AI / Smarter Technologies** — general RCM agents, has **publicly named
  BH as a target vertical**; has engineering capacity to move.
- **Eleos Health** — closest incumbent; April 2026 launched Coding Agent + Quality
  Assist (genuine pre-bill BH denial prevention) but serves _community/outpatient
  mental health_, not residential/SUD, and has no appeal-drafting or ASAM logic yet.
- **Waystar AltitudeAI / Commure / Adonis / Candid** — real, mature AI denial
  prevention **and** appeal drafting, but aimed at hospitals/health systems, not
  20–40-bed SUD centers, and with no Part 2 architecture.

**What still nobody has productized (the genuine remaining white space):**

1. **MHPAEA parity-argument generation in appeals** — letters that invoke NQTL
   comparative-analysis / parity-law enforcement rights. High-leverage, unoccupied.
2. **ASAM continued-stay UR tightening** — mapping clinical status to ASAM dimensions
   1–6 and generating concurrent-review packets from that mapping.
3. **Outcome-based pricing for treatment centers** — no current player sells the SUD
   SMB on % of recovered/prevented denials.
4. **A warm, trust-based distribution channel** — everyone else is running cold or
   enterprise sales.

**Verdict on the gap:** REAL but NARROWING — call it a **12–18 month window**. The
full-stack position (BH-native scrubber + ASAM UR + MHPAEA appeals + Part 2
architecture + outcome pricing + warm channel) is still unoccupied as an integrated
product. But "we'll be the only one" is gone. The bet is now a **race won on channel
and depth**, not a land-grab of empty territory.

---

## 4. The two hard gates — both clearable

### Gate A (42 CFR Part 2 + BAA-covered LLM): **CLEARABLE, on a shoestring — and the regulation just moved in your favor.**

- **BAA-covered LLM at $0 contract floor exists today.** Cleanest path: build inside
  **AWS, sign the self-serve AWS BAA via Artifact (no minimum spend), use Amazon
  Bedrock** (Claude or other) — the model provider never sees the data, no training on
  your data, everything stays inside one AWS trust boundary. OpenAI (free email BAA,
  ZDR on request) and Azure OpenAI are alternatives.
- **The Feb 2024 Part 2 Final Rule is a tailwind, not a barrier.** It aligns Part 2
  with HIPAA: a **single TPO consent** now covers treatment/payment/operations
  disclosures (including to a BA vendor), redisclosure for TPO is permitted, and
  record-segregation is no longer required. Your three use cases (appeals, UR packets,
  pre-bill scrub) all map to payment/operations. Enforcement date Feb 2026.
- **You need BAA _plus_ QSOA.** A standard HIPAA BAA is necessary but not sufficient
  for SUD data — you (the startup) carry a Qualified Service Organization Agreement
  obligation to the treatment center, flowed down to subprocessors. This is a
  contract-drafting line item (a few $k of healthcare counsel), not a technical gate.
- **One real design constraint:** broad TPO consent does **not** cover SUD
  psychotherapy/counseling notes — those need specific consent. Detect and gate that
  data class in the product.
- **Attestations, staged:** **SOC 2 Type II + BAA + QSOA is enough to start**
  (~$30–50k, 6–12 mo observation). Defer **HITRUST r2** ($100k–500k) until enterprise
  / direct-EHR-integration demand justifies it.

_Marcus's Part 2 familiarity from the recovery ventures is a genuine edge here — the
compliant architecture is itself a barrier every competitor must also clear, and most
general-RCM players have **not** confirmed Part 2 compliance._

### Gate B (willingness-to-pay): **Unvalidated — and this is now the real gate.**

The brief is right that this is go/no-go. Two things make it tractable:

- **The pricing model is already understood by buyers.** Treatment centers pay
  outsourced billers 4–8% of collections today; denial-recovery contingency at 15–25%
  of recovered dollars is an established adjacent model. No buyer education on
  _structure_ is needed — only on _trust and baseline measurement_.
- **Recommended pricing = hybrid** (modest flat SaaS, e.g. ~$2.5k/mo, + 10–15% of
  recovered/prevented denials above an audited baseline). Pure contingency
  under-captures prevention value and invites baseline disputes; pure SaaS throws away
  the "we only win when you win" trust advantage. Hybrid de-risks the buyer and still
  captures upside.

Gate B is now where the venture lives or dies, because Gate A is solved and the
competitive novelty is gone. **If 3–5 warm operators won't commit to a paid pilot on
a real audited ROI number, stop.**

---

## 5. Market scale — venture-grade, not decacorn

- **Serviceable facilities:** SAMHSA 2023 N-SUMHSS gives ~14,600 SU + 3,795 dual
  SU/MH facilities; ~91% private; ~77% accept commercial/Medicaid. After removing
  public, self-pay-only, sub-scale solo, and enterprise-RCM-covered facilities, the
  **defensible SAM is ~8,000–12,000 facilities**; the realistic near-term target is
  **~5,000–7,000 private for-profit multi-level operators.**
- **Recoverable denial dollars/facility:** ~$150k (small IOP) to ~$1.4M (large
  multi-level); ~$450k for a mid-size $4–5M-collections center _(estimate, triangulated
  — treat as ±2×)._
- **Revenue ceiling:** ~8,000 facilities × ~$450k recoverable × 15% take ≈ **$537M
  theoretical TAM**; at hybrid pricing (~$75k/facility/yr), **10% SAM ≈ $60M ARR, 25%
  SAM ≈ $150M ARR.**
- **Market context:** US denial-management market $5.1B (2024, 9.7% CAGR); BH software
  $1.5B US / growing ~12–15%; target industry is fragmented (no firm >5% share),
  ~$33B revenue, ~5% CAGR — **no consolidation risk to the SMB customer base.**
- **Exit:** strategic acquisition by a BH EHR (Kipu, Sunwave), a general RCM platform
  (Waystar went public ~$2.3B), or a payer-tech company is the realistic path. **A
  $200–500M outcome at 15–25% SAM penetration is plausible; a standalone IPO is not the
  base case.**

**Classification: solid venture-scale OR an excellent bootstrapped/lifestyle business**
— and notably, the warm-channel + outcome-pricing model makes the _bootstrapped_ path
unusually viable, because CAC can stay near zero and revenue is self-funding from
recovered dollars. That fits the portfolio framing (funded by the CPA engine, low
outside capital) better than a venture-blitz would.

---

## 6. The build path — how to actually win this

Sequenced to **prove demand before spending engineering, and to convert the warm
channel and BH-specific depth into the moat** the competition can't copy.

### Phase 0 — Desk validation (2–4 weeks, ~$0). _Go/no-go on Gate B._

1. **Confirm the channel is real.** Count the actual treatment-center clients in the
   TWK / brother's CPA book and rank by warmth. This is the load-bearing assumption —
   if there are <3 warm operators, the unfair advantage evaporates and the answer is no.
2. **Lock the compliant architecture on paper:** AWS Bedrock + BAA, draft combined
   BAA/QSOA template with healthcare counsel, design the counseling-notes gate.
3. **Build the BH denial taxonomy:** the 5–8 highest-frequency, highest-recoverable
   denial codes for SUD/PHP/IOP, and the MHPAEA parity + ASAM continued-stay logic that
   will be the differentiation. (Behave Health's published BH denial-code library and
   ASAM dimensions are a starting reference.)
4. **Interview 3–5 warm billing leads** on denial pain and WTP for the hybrid model.

### Phase 1 — Manual-first "Wizard of Oz" pilot (4–8 weeks). _Prove dollars, zero product._

- Run a **denial-leakage audit** for 1–2 design-partner facilities from the warm
  network — you in the loop, LLM behind the scenes drafting appeals. **Produce a real,
  audited per-facility recoverable-dollar number** (this replaces every borrowed stat
  in §2).
- **Lead with the "recover" wedge** (denial triage + appeal drafting) — immediate,
  measurable, fast ROI proof — including **MHPAEA parity arguments**, your sharpest
  unoccupied edge.
- **Success metric:** dollars recovered > pilot price AND the operator signs a paid
  commitment. If not → stop.

### Phase 2 — Thin product (only if Phase 1 closes; ~1–2 quarters).

- Ship the **denial triage + appeal drafter** as module 1 on the compliant
  architecture, one EHR/clearinghouse integration first (pick the one your design
  partners use — likely Kipu, Sunwave, or Behave).
- Stand up **SOC 2 Type II** controls in parallel (start the observation clock early).
- **Then expand to prevention:** pre-bill scrubber + ASAM UR assistant — stickier,
  higher-value, harder to rip out.

### Phase 3 — Channel-led scale.

- Productize the **"denial-leakage audit" as the repeatable top-of-funnel** (same
  audit→pilot→retainer ladder as the CPA-automation play); each CPA intro becomes a
  near-zero-CAC audit.
- Defer HITRUST r2 until an enterprise/EHR-integration deal demands it.

### What makes it _win_ (not just exist), given the new competition:

1. **Move now or don't.** The window is 12–18 months. Phase 0–1 must run this quarter.
2. **Own the two unoccupied vectors** — MHPAEA parity generation and ASAM UR depth —
   not the commoditizing "generic appeal letter." Make these the product's identity.
3. **Weaponize the channel.** Adentris and Aegis are running cold/VC-sales; the
   CPA-introduction + lived-recovery credibility is the one asset they can't buy.
4. **Outcome pricing as a wedge**, not just a model — it's how you displace incumbents
   on cash-constrained operators who can't risk a flat SaaS spend.
5. **Stay EHR-agnostic and portable** — the PE-backed EHRs (Kipu, Sunwave) could build
   or buy this; middleware that no single EHR can lock out is the structural defense.

---

## 7. Risks & caveats (updated)

| Risk                                                     | Severity            | Change since brief                                             | Mitigation                                                                           |
| -------------------------------------------------------- | ------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Funded competitor (Adentris) is already in the wedge** | **High** _(new/up)_ | The "empty category" premise is gone                           | Win on channel + MHPAEA/ASAM depth + speed; treat 12–18mo window as hard             |
| Operators won't pay / ROI not legible (Gate B)           | Existential         | Now the _primary_ gate                                         | Phase 1 audited-dollar proof before any production code                              |
| Inflated/borrowed stats undermine credibility            | Medium _(new)_      | Several headline figures are unsourced                         | Replace deck stats with live per-facility numbers; cite Optum/Kodiak/AHA only        |
| Part 2 / BAA architecture                                | Low _(down)_        | Confirmed clearable at ~$0; Feb-2024 rule is a tailwind        | AWS Bedrock + BAA/QSOA; gate counseling notes                                        |
| PE-backed EHR builds/buys it                             | High                | Unchanged                                                      | EHR-agnostic middleware; warm-channel beachhead                                      |
| Founder bandwidth (rank #4 vs CPA engine + recovery)     | High                | Window pressure now conflicts with "park until CPA cash-flows" | **Decision forced:** either run Phase 0–1 now, or formally shelve — do not slow-walk |
| Payers adapt denial logic                                | Medium              | Unchanged                                                      | Rules library updatable; denial drift = recurring demand                             |
| Clinical liability / scope                               | Medium              | Unchanged                                                      | Tool drafts/flags for human approval; never auto-submits                             |

**The one genuine strategic tension the new data creates:** the brief sequenced this
as rank-#4, "parked until the CPA engine is cash-flowing." The competitive window
(12–18 months) now **conflicts** with that patience. The decision is binary — commit
to Phase 0–1 _this quarter_ on the warm channel, or accept that by the time the CPA
engine frees up bandwidth, the category may be defensibly held by funded incumbents
and the right call is to not enter. A slow, half-committed entry is the worst option.

---

## 8. Recommendation

**QUALIFIED GO, validation-gated and time-boxed.** The business is feasible: pain is
real, Gate A is solved cheaply with a regulatory tailwind, the market supports a
$50–150M-ARR vertical with a clean strategic exit, and the warm CPA + lived-recovery
channel is a genuine, uncopyable advantage. **The brief's caution was correct; the new
information is that the competitive clock now overrides the "park it" sequencing.**

Concretely:

- **Run Phase 0 + Phase 1 this quarter** (low cost, ~$0–few-$k, mostly Marcus's time).
  The only two questions that matter — _are there warm operators, and will they pay on
  an audited number_ — get answered for almost nothing.
- **Re-point the thesis** from "first to an empty category" to "**warm-channel + MHPAEA/
  ASAM depth + outcome pricing, executed fast.**"
- **Decide explicitly by end of Phase 1:** if 3–5 warm operators commit to paid pilots
  on real recovered dollars → fund Phase 2. If not, or if the warm channel is thinner
  than assumed → **no-go, and redeploy the bandwidth to the higher-ranked portfolio
  bets** rather than fight funded competitors on cold distribution.

The single highest-value next action is the cheapest one: **count and qualify the warm
treatment-center clients in the CPA book.** That one fact determines whether this is a
GO or a NO.

---

## Sources

**Denial economics:** KFF ACA Marketplace Denials 2023/2024; HHS OIG Medicare
Advantage Appeal Outcomes (2018); AHA Payer Denial Tactics (2024) & Skyrocketing
Admin Costs (Sept 2024); Kodiak Solutions denial-rate data (BusinessWire 2025);
Premier Claims Adjudication report (2025); Optum 2024 Revenue Cycle Denials Index;
DOL/EBSA 2024 MHPAEA Report to Congress; Milliman Parity Track.

**Competitive landscape:** Adentris (adentris.com; Sobrius/Resilient deployment
posts); Aegis (YC X25 launch); Eleos Health agentic AI launch (HIT Consultant, Apr
2026); Kipu, Sunwave/Lightning Step (BVP Forge merger), Behave Health, VerifyTx;
Waystar AltitudeAI; Commure; Adonis ($40M Series C, Mar 2026); Candid Health;
Thoughtful AI / Smarter Technologies; Anomaly; Tennr; Fathom; Cohere Health.

**Regulatory/technical:** HHS 42 CFR Part 2 Final Rule fact sheet; Troutman & Morgan
Lewis client alerts; SAMHSA QSO/HIE FAQs; Anthropic/OpenAI/AWS Bedrock/Azure OpenAI
BAA documentation; HITRUST Alliance r2; SOC 2 cost references (BrightDefense,
IntuitionLabs).

**Market sizing/pricing:** SAMHSA 2023 N-SUMHSS Annual Report (PEP24-07-027) & KFF
facilities analysis; Grand View Research (BH software); Arizton (denial management);
IBISWorld NAICS 6215; Ardent Practice Partners & Haven Health Management (billing
pricing norms); Scope Research (SUD M&A multiples).

_Full URLs are preserved in the research-stream outputs underlying this assessment.
Re-verify the `[VERIFY]`-flagged items (Adentris funding stage, specific payer/LA
rules, per-facility denial dollars) before acting on them._
