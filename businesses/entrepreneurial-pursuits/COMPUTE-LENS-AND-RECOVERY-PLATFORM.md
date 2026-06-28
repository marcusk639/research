# The Owned-Compute Lens + Recovery-Platform Fit

> **Created:** 2026-06-26 · Companion to `UNIQUELY-QUALIFIED-AI-OPPORTUNITIES.md`.
> Answers two questions: (1) where does `~/dev/recovery-platform` fit now that it's a
> live, revenue-generating asset, and (2) which opportunity best _justifies and utilizes_
> substantive owned compute (powerful workstations / GPU servers)?
>
> **Method:** codebase map of `recovery-platform` (Explore) + sourced research on
> local-LLM-vs-cloud economics, the HIPAA/Part 2 sovereignty angle, 2026 hardware tiers,
> and Section 179 / bonus depreciation.

---

## 1. What `recovery-platform` actually is (grounding)

A monorepo of four products: **Homegroups** (12-step, V4 live), **Regroup/RATS**
(sober-living operators, beta, ~5% test coverage on payment/auth paths), **NextStep/Detox**
(non-clinical individual support, deploy-ready, 96% test coverage), and **recovery-api**
(cross-product bus, untested). Stack: React Native / Next.js / Angular on
Firebase/Firestore, **Stripe Connect** for rent + product sales.

Three facts that drive the strategy:

- **Revenue is activation-gated, not build-gated.** Stripe default prices are unset
  (Homegroups checkout silently throws), Regroup payment paths are ~5% tested, Detox PDFs
  are behind an email/fulfillment migration. Your paying customers are real but **early**;
  the fastest revenue lever is _finishing activation_, not new features.
- **No LLM anywhere in the code today.** Clean slate for AI features.
- **The data is currently low-sensitivity.** Sobriety dates, meeting attendance, chores,
  meds, "phases" — anonymity-first, per-group privacy toggles, and Detox is _explicitly
  non-clinical_ with safety-referral gating. It is **not** HIPAA/Part 2-regulated as built.

**Strategic role:** `recovery-platform` is your **cash + credibility + distribution
beachhead into treatment centers** — not, in its current form, a heavy-compute AI product.
That distinction is the crux of the hardware question.

---

## 2. The honest answer on "substantive equipment"

You're reasoning that a business needing powerful computers/servers is desirable (compute
to run AI + a real capital asset to expense against revenue). That instinct is right — but
**owned GPU compute is justified by exactly one thing: high-volume inference on regulated
data where "no third-party model vendor is in the data path" is both a cost win and a
closing argument.** It is _not_ justified by services work, federal contracting, or a
B2C/anonymized app.

What the economics actually say:

- **Cloud BAA wins until you have real volume.** Below ~70% sustained GPU utilization (and
  realistically below ~200M–1B tokens/month), AWS Bedrock / Azure OpenAI beat owned
  hardware on total cost — idle GPUs are the most expensive GPUs you can own. A solo
  services business processing a few hundred docs/day sits _firmly_ in cloud-wins territory.
- **The compliance/sovereignty premium is real, though — for SUD data specifically.** No
  major cloud LLM vendor ships a product designed for 42 CFR Part 2 sub-processor /
  re-disclosure obligations; you build the consent-gate in your app layer regardless. So
  "your PHI never leaves our owned, audited infrastructure, no model vendor in the data
  path" is a _genuine_ procurement advantage with behavioral-health buyers — not marketing.
- **Open-weight models are good-enough for the work.** 70B-class open models (Llama 3.3,
  Qwen 3) hit ~91–95% on structured clinical extraction vs ~96% frontier — fine for
  templated appeal letters, claim scrubbing, and RAG with a human in the loop. Keep a
  frontier cloud model for the hardest ~10% of reasoning.

**Conclusion:** the opportunity that best justifies owned compute is **a high-volume,
regulated-data inference product** — i.e., the **BH-RCM copilot** or the **SUD compliance
platform (EKRA + Part 2)** from the opportunities doc. `recovery-platform` _funds and
distributes_ that, but its own current workload does **not** require GPUs.

---

## 3. Compute-justification ranking across your portfolio

| Opportunity                               | Inference volume              | Data sensitivity     | "No-vendor-in-path" sells? | Owned-compute justification                  |
| ----------------------------------------- | ----------------------------- | -------------------- | -------------------------- | -------------------------------------------- |
| **BH-RCM copilot**                        | High (notes, claims, appeals) | PHI + Part 2         | Strongly                   | **Strongest**                                |
| **SUD compliance platform (EKRA/Part 2)** | Medium–High (center docs)     | PHI + Part 2         | Strongly                   | **Strong**                                   |
| **recovery-platform + AI features**       | Low (chat/match/journaling)   | Low / anonymized     | Weakly (today)             | Weak — until it handles clinical data        |
| **VA-claims AI (B2B/B2G)**                | Medium                        | PHI (vet records)    | Moderately                 | Moderate (but B2G is GovCloud, not your box) |
| **SDVOSB federal AI services**            | Low/variable                  | Cloud/GovCloud-bound | N/A (gov dictates)         | Weak — federal work runs on _their_ cloud    |
| **CPA automation**                        | Low                           | Financial, not SUD   | No                         | Weak                                         |

The pattern is clean: **compute follows regulated, high-volume PHI/Part 2 inference.** That
points at the two behavioral-health product plays — and notably _not_ at the federal
services engine, even though that's your fastest cash.

---

## 4. Where AI fits in `recovery-platform` (and why it stays cloud-cheap)

The valuable LLM features here are **low-compute** and should run on **cheap cloud models
(gpt-4o-mini / Haiku class)**, not your GPU:

- Semantic meeting/topic matching (Homegroups), smart referral routing (recovery-api),
  journaling/check-in insight summaries, group-chat content moderation / crisis-language
  detection (high safety value, ties to Detox's existing referral-trigger logic).

These add product value but **do not justify hardware.** The only path that connects
`recovery-platform` to the owned-compute thesis is the portfolio's flagged (and
attorney-gated) move: **harden it to HIPAA/Part 2 and sell the alumni/aftercare + outcomes
tooling to treatment centers** — at which point it processes real clinical data and the
self-hosted-compliance story becomes legitimate. That's a _later, regulatory-load_ step,
not a reason to buy a server now.

---

## 5. The pragmatic hardware plan (buy the right thing, at the right time)

You can act on the equipment instinct **without overbuilding** — and the existing
`recovery-platform` + CPA revenue is exactly what makes the tax treatment useful (Section
179 can't exceed active business income; bonus depreciation can create a carry-forward —
**confirm specifics with your CPA, which you conveniently have**).

**Stage 1 — now (revenue $0→~$20k/mo): one powerful workstation, not a server.**

- Buy **one** machine that triples as (a) your dev box for building LLM features across the
  whole portfolio, (b) a **Part 2-safe local inference box** for prototyping on
  _de-identified/synthetic_ data, and (c) a clean **Section 179 / 100% bonus-depreciation**
  capital expense against your real revenue.
- Best options: **Mac Studio M3 Ultra 192GB (~$5.5k)** — silent, low-power, runs 70B+
  locally, zero GPU-driver ops, ideal for a solo founder; **or RTX 6000 Ada / Blackwell
  workstation (~$7–9k)** if you want max NVIDIA throughput and CUDA tooling. After
  full expensing at your marginal rate, real out-of-pocket is roughly half the sticker.
- **Production inference still runs on AWS Bedrock** (signed BAA, ZDR enabled _per call_,
  HIPAA-eligible region, app-layer Part 2 consent gate). Use Bedrock Llama 70B for bulk
  extraction, Bedrock Claude for the hard 10%.

**Stage 2 — at product-market fit (revenue ~$20–60k/mo, 200M–1B tokens/mo on regulated
data): add a serious inference card.** One **A100 80GB (~$5–9k refurb)** or **RTX PRO 6000
Blackwell 96GB (~$8.5k)**. Now owned compute is _both_ an economics win (you've eliminated
per-token cost on the bulk workload) _and_ a closing argument ("zero model-vendor in your
SUD data path"). This is the point where "substantive equipment" is genuinely warranted.

**Stage 3 — multi-client scale ($60k+/mo, 1B+ tokens/mo): multi-GPU + colo**, dedicated to
the BH-RCM / compliance-platform inference load, written into your SOC 2 as a single-tenant,
air-gapped-from-vendor architecture.

**Do not** jump to A100/H100 servers now. At your current volume it's idle capex; the
single workstation captures the dev value, the compliance-prototyping value, _and_ the tax
write-off without the waste.

---

## 6. How this updates the recommendation

Nothing in the prior ranking changes — it sharpens:

1. **Engine stays SDVOSB AI services** (fastest cash; runs on gov cloud, needs no hardware).
2. **`recovery-platform` = fund + finish + beachhead.** Treat its near-term value as
   _activation_ (turn on Stripe prices, test Regroup payment paths → capture the revenue you
   already have demand for) and as your **warm doorway into treatment centers** — the same
   buyers the compliance platform and BH-RCM need. Add the _cheap-cloud_ AI features for
   stickiness; don't put it on your GPU.
3. **The owned-compute play is the SUD compliance platform / BH-RCM** — the regulated,
   high-volume inference products. Buy **one workstation now** (dev + Part 2-safe
   prototyping + write-off against recovery-platform/CPA income), and scale to real
   inference hardware only when those products hit Stage-2 volume.

**One-line answer to your question:** the business that best supports "substantive
equipment" is a **high-volume, Part 2-regulated inference product (SUD compliance platform
or BH-RCM)** — `recovery-platform` is the revenue and the distribution that _funds and
justifies_ the first machine, not the workload that needs it. Start with a single
$5–9k workstation expensed against your existing revenue; graduate to GPU-server compute
only at proven inference volume.

---

## Open questions

1. What's the **actual current MRR** on `recovery-platform`, and from which product
   (Homegroups vs Regroup vs Detox)? Determines how much real income exists to expense
   hardware against this tax year.
2. Are you willing to **finish the activation work** (Stripe prices, Regroup payment-path
   tests) before adding AI features? That's the highest-ROI near-term engineering.
3. Do you want the workstation primarily as a **dev/prototyping box** (then Mac Studio wins
   on simplicity) or as a **CUDA/training rig** (then NVIDIA)?
4. Is the **treatment-center hardening of recovery-platform** (HIPAA/Part 2 + alumni/outcomes
   B2B) something you'd pursue — the only path that makes recovery-platform itself a
   compute-justifying, regulated-data product? (Attorney-gated per `REPORT.md` §4.)

## Sources

Local-LLM economics & hardware: Spheron (on-prem vs cloud break-even; GPU cheat sheet 2026),
Clanker Cloud (inference breakeven 2026), Braincuber (self-hosted vs API). Compliance:
AWS HIPAA GenAI guidance; Tactionsoft BAA guide (OpenAI/Anthropic/Bedrock); Foley Hoag &
HHS on 42 CFR Part 2; AccountableHQ addiction-medicine data security. Open-model capability:
PMC/ScienceDirect LLM clinical-extraction benchmarks; Digital Applied open-weight 2026
retrospective. Tax: Landmark CPAs & Block Advisors on OBBBA Section 179 / bonus depreciation;
LegalClarity on the §179 business-income limitation. Codebase: `recovery-platform/ANALYSIS.md`,
`/CLAUDE.md`, `/docs/go-to-market/`, product READMEs and `firestore.rules`.
