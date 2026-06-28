# The Optimal Plan for Homegroups

**Generated:** 2026-06-18 · Built with the `recovery-app-go-to-market` skill, grounded in `homegroups-gtm-and-moat-analysis.md`, `research-dossier-v2.md`, the deep-research pass (`wf_f1104a43-465`, 24/25 claims verified), and a direct read of the codebase at `/Users/marcus/dev/recovery-platform/homegroups`.
**Scope:** This is the _optimal plan for Homegroups specifically_. RATS and the treatment-center bundle appear only as supporting levers, because the single most important strategic finding is that **Homegroups is not a standalone business — it is a network + distribution asset.**
**Confidence labels:** `[Verified]` · `[Inference]` · `[Estimate]` · `[Time-sensitive]`

---

## Executive Summary

Homegroups is a member-owned, privacy-first operations platform for 12-step groups (treasury, 7th-Tradition basket, service positions, meeting finder, governance). The optimal plan is **not** to chase the aftercare/alumni-engagement market it was tagged with (that hill belongs to facility-tethered incumbents now consolidating into Kipu, and it imports EKRA/42 CFR Part 2 risk). The optimal plan is to **own the operations layer the free AA Meeting Guide structurally refuses to build, distribute top-down through intergroups/Central Offices, monetize through transparent 7th-Tradition payment processing, and run Homegroups as the member-side flywheel that feeds RATS** (the operator-side sober-living product where the real money is). Realistic standalone 12-month revenue is **low five figures `[Estimate]`** — so the correct posture is _patient, mission-driven, self-funded from the CPA income engine_, optimizing for network density and a clean legal surface, not ARR.

---

## 1. Market Opportunity

### 1.1 Market Size

**12-step fellowship (the Homegroups TAM):**

- AA's published SMF-53 estimate: **~69,812 US groups / ~1.44M US members; ~1.56M US+Canada** `[Verified-source, re-source caveat — this exact figure failed an independent verification vote because it is PDF-gated; treat as AA's own estimate]`. NA, Al-Anon, CMA, etc. add a meaningful multiple on top. `[Estimate]`
- Digital reach is already proven: AA's free **Meeting Guide app = 150,000+ weekly meetings, 768,500+ monthly users, 500+ service entities** ([aa.org](https://www.aa.org/meeting-guide-app)) `[Verified]`.
- **SAM (paying group admins):** if even 1–3% of ~70k US AA groups pay a small admin/treasury tier, that's **~700–2,100 paying groups** `[Estimate]` — before NA/other fellowships or intergroups.
- **Institutional buyers (intergroups/Central Offices):** order of **400–600 in the US** `[Estimate]` — small N, but the highest-value, most defensible buyer.

**Adjacent (for the flywheel, not Homegroups' own TAM):**

- US recovery residences / sober-living homes: estimates vary widely, commonly cited in the **tens of thousands (~17,000–50,000)** `[Estimate]` — this is RATS' market, reachable _through_ Homegroups' member network.

**Honest read:** This is a **small, shallow-pocket TAM**. The fellowship's 7th Tradition (self-supporting; declines outside contributions), anonymity culture, and volunteer treasurers cap per-unit revenue. Do not size Homegroups as venture-scale SaaS. `[Inference, high]`

### 1.2 Competitive Landscape

| Player                                            | What they own                                                                                               | Threat to Homegroups                                                                                                   |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **AA Meeting Guide (free, AA-run)**               | The meeting **directory** at massive scale; 7th-Tradition funded → **can't monetize, won't build ops**      | Owns your top-of-funnel; **integrate it, don't fight it**. Leaves treasury/positions/check-in wide open. `[Verified]`  |
| **Homegroup.Online (501c3)**                      | Electronic **7th-Tradition donations + group treasury** — _your origin wedge_                               | **Direct competitor**; can out-Tradition and undercut you (nonprofit). Beat on breadth + intergroup + UX. `[Verified]` |
| **Transparency Technologies**                     | Near-clone: "Home groups" feature, GPS attendance, Claude 4th-step journaling, 4-tier pricing (no public $) | Proves the moat features are commoditized. `[Verified]`                                                                |
| **Team Recovery / Kipu, CaredFor/ContinuumCloud** | Facility-tethered alumni apps (white-label, per-facility)                                                   | Only a threat **if** you fight for the facility dollar. Irrelevant to member-owned ops. `[Verified]`                   |

**Whitespace:** _Member-owned, multi-fellowship group operations + intergroup back-office_, with treasurer-handoff continuity as the lock-in. No incumbent occupies all of it: the directory is free-but-feature-bare, the treasury competitor is single-purpose, the clones lack distribution, the facility apps can't be member-owned. `[Inference, high]`

### 1.3 Tailwinds & Headwinds

**Tailwinds:** (1) Gold-standard evidence the category _works_ — Cochrane 2020: AA/TSF beats CBT for abstinence, **RR 1.21 @12mo**, holds to 36mo, probable cost savings ([Cochrane](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012880.pub2/full)) `[Verified]`. (2) AA already normalized a free official app → fellowships are digitally adopting. (3) Intergroups want modernization but have no good tooling.

**Headwinds:** (1) **7th Tradition + anonymity** structurally suppress willingness-to-pay and data use. (2) A **nonprofit already holds your core wedge** (Homegroup.Online). (3) All differentiating features (GPS, directory, AI) are **commoditized**; moat must come from distribution + data continuity, which take years to build. `[Verified/Inference]`

---

## 2. Most Marketable Features

### 2.1 Homegroups — Hook & Sticky

| Feature                                                               | Why marketable                                              | Hook or Sticky        |
| --------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------- |
| Meeting finder (directory parity / Meeting Guide ingest)              | Table-stakes entry; what members actually open the app for  | **Hook**              |
| Digital 7th-Tradition basket (Stripe)                                 | Solves the weekly cash-handling pain; Traditions-aligned    | **Hook**              |
| **Treasurer handoff + 12-month categorized history**                  | The one workflow that makes a _new_ rotating treasurer stay | **Sticky (the moat)** |
| Service-position rotation/elections + business-meeting minutes/voting | Group governance no free app touches                        | **Sticky**            |
| Sobriety tracker / milestones                                         | Engagement + retention for individual members               | Hook (member-side)    |
| Intergroup dashboard + SSO + rollup (V4.4)                            | The institutional sale; top-down distribution               | **Sticky (B2B)**      |

**Table-stakes, not differentiating:** chat/DMs, announcements, sobriety counter — expected, won't drive purchase.
**Impressive but won't sell:** GPS/QR check-in and AI journaling — commoditized; keep as parity, don't lead with them. `[Inference]`

### 2.2 The flywheel value Homegroups has that nothing else does

Homegroups is the **member/fellowship-side network**; RATS is the **operator-side sober-living system**. A person in recovery uses Homegroups for its own merits (best free ops + meeting finder) → their sober-living house runs on RATS → warm, EKRA-clean, _non-steered_ adjacency. Homegroups is the cheapest possible top-of-funnel and brand for the portfolio. **This is its highest strategic value — higher than its own P&L.** (Keep the two products free of any _paid referral_ between them — see Risk table.) `[Inference, high]`

---

## 3. Monetization Strategy

**Principle:** Lead with revenue that is (a) Traditions-aligned, (b) EKRA-safe (no patient flow), (c) defensible. Rank: **donation processing → intergroup SaaS → admin subscription → (gated) facility tier.**

### 3.1 Stream A — Digital 7th-Tradition processing (the volume engine) `[Inference, med]`

Stripe Connect platform fee on group baskets/donations. Per dossier §3, this is **thin-margin pass-through, not spread** — but at fellowship scale, _volume of small recurring contributions_ is the realistic dollar engine, and it only earns when groups collect (Traditions-aligned). **Be radically fee-transparent** to survive the "not to profit" scrutiny Homegroup.Online will weaponize. Benchmark: Sobriety Hub passes **3.9% card / 1.2% ACH** to the payer at ~zero profit ([dossier §3.1](research-dossier-v2.md)); model a **small explicit platform fee (e.g., ~1% or a flat cents-per-transaction)**, ACH-first to protect margin.

### 3.2 Stream B — Intergroup / Central Office SaaS (the defensible B2B moat) `[Inference, med]`

Tier A/B already built. Sell the **intergroup dashboard + SSO + group rollup + broadcast + anonymized aggregate reporting** to regional service bodies as a **flat annual nonprofit-friendly fee**. Benchmark: nonprofit/association SaaS, **~$500–$3,000/yr** per intergroup depending on size `[Estimate]`. Small N, long volunteer-committee cycles — but each adoption pulls its member groups onto the ops layer top-down (network effect).

### 3.3 Stream C — Group admin subscription (retention layer, not engine) `[Inference]`

Current code prices ~**$8–$12/yr** — keep it **freemium and low**; a nonprofit competitor is free, and a high price signals "profiting off anonymity." Free for members always; admin tier unlocks treasury/positions/invite controls. Add an optional **$0 onboarding** (don't copy Sobriety Hub's $250 — wrong audience). This is a retention/qualification layer, not the revenue engine.

### 3.4 Stream D — Facility tier (gated upside only) `[Inference, high]`

Pursue **only** behind the attorney gate (dossier §2): **flat-fee, no per-patient/per-bed pricing, no identified-lead delivery, anonymized aggregates only, BAA in enterprise.** It competes with Kipu-bundled alumni tools and carries the most legal risk. **Never** the load-bearing revenue.

### 3.5 Revenue model at scale `[Estimate — all figures illustrative, labeled assumptions]`

| Scenario (12-mo) | Paying admin groups | Intergroups | Donation volume processed | Illustrative gross revenue |
| ---------------- | ------------------- | ----------- | ------------------------- | -------------------------- |
| **Conservative** | ~150 @ $10/yr       | 2 @ $1k     | $300k @ ~1% net           | **~$4.5k**                 |
| **Base**         | ~500 @ $10/yr       | 6 @ $1.5k   | $1.5M @ ~1% net           | **~$29k**                  |
| **Optimistic**   | ~1,500 @ $10/yr     | 15 @ $2k    | $6M @ ~1% net             | **~$105k**                 |

**Read:** Even the optimistic standalone case (~$105k) requires fellowship-scale density and barely clears one CPA-consulting client's revenue. **This confirms: Homegroups is not the income engine. Its ROI is distribution + the RATS flywheel, not its own ARR.** `[Inference, high]`

---

## 4. Optimal Feature Set for Growth

### 4.1 Ship next (ranked by leverage)

1. **Treasurer-handoff continuity + 12-mo treasury history export** — _the_ lock-in; low complexity; unblocks retention + the "why switch back to a spreadsheet" objection. `[Inference, high]`
2. **Meeting Guide directory ingest/parity** — removes the "no local meetings = bad UX" cold-start; medium complexity; unblocks member adoption.
3. **Intergroup onboarding + anonymized rollup polish (V4.4)** — unblocks the B2B moat + top-down distribution; medium-high complexity.
4. **Transparent donation-fee UX + ACH-first rails** — unblocks Stream A; low-medium complexity.

### 4.2 De-emphasize / cut

- **Referral dashboard + facility engagement metrics** as currently built — **cut or counsel-gate**; they import EKRA/Part-2 risk for revenue you shouldn't lead with. `[Verified legal basis: dossier §2]`
- GPS/QR check-in and AI journaling — keep as parity, stop treating as differentiators.

### 4.3 Missing features that would move the needle

- **Multi-fellowship support depth** (NA/Al-Anon/CMA templates) — expands TAM beyond AA and differentiates from single-fellowship competitors. `[Inference]`
- **Offline-first reliability** for meeting schedules/treasury — the README flags it; volunteers in spotty venues need it; raises trust.
- **A clean "claim your group / import from spreadsheet" flow** — collapses switching cost from the incumbent (paper/Excel/Homegroup.Online).

---

## 5. GTM Motion & Sales Strategy

### 5.1 Primary motion

- **Homegroups (member/admin):** **Product-led growth** — free for members, freemium admin tier, viral via deep-link group invites. CAC must be ~$0; the fellowship won't tolerate ads/outbound.
- **Intergroup tier:** **Warm, relationship-led B2B** — credibility (lived recovery + service history) into service committees; not cold sales.
- **Facility tier:** **Do not actively sell** until gated; inbound-only, flat-fee.

### 5.2 Audience priority

1. **Group admins/treasurers (PLG beachhead)** — fastest, single-threaded, no committee, no compliance gauntlet.
2. **Intergroups/Central Offices (distribution moat)** — once you have group density to show.
3. **Treatment centers (gated upside)** — last, clean, never load-bearing.

### 5.3 First 90 days

1. **De-risk:** disable referral-to-facility/patient-steering; scope the attorney gate (EKRA/Part 2/LA brokering). `[from dossier §2]`
2. **Reframe:** rewrite store/site copy from "aftercare/alumni" → "the digital home for your 12-step group & intergroup"; fix the member-ownership-vs-facility-features contradiction on the /about page.
3. **Decide the entity question** (for-profit fee-transparent vs nonprofit/fiscal-sponsor — see §7).
4. **Ship the handoff/history lock-in** + Meeting Guide ingest.
5. **Land 5–15 design-partner groups** free via the SWLA/lived-recovery network for references.
6. **Line up 1–2 friendly intergroups** for a V4.4 pilot.

---

## 6. Risks & Mitigation

| Risk                                                                  | Severity                   | Mitigation                                                                                    |
| --------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------- |
| Referral/facility features = **EKRA/42 CFR Part 2 criminal exposure** | **High**                   | Cut/counsel-gate now; flat-fee only; no patient flow; attorney sign-off before any facility $ |
| 7th Tradition / anonymity suppress WTP                                | **High**                   | Member-free PLG; revenue from processing + institutions, not per-head; fee transparency       |
| Homegroup.Online (501c3) owns the treasury wedge & can undercut       | **Med-High**               | Win on breadth + intergroup + UX; consider nonprofit/fiscal-sponsor posture (§7)              |
| Kipu free-bundles alumni engagement                                   | **Med** `[Time-sensitive]` | Don't depend on facility revenue; verify bundling status before any TC build                  |
| Features commoditized (GPS/dir/AI)                                    | **Med**                    | Compete on distribution + handoff lock-in, not features                                       |
| Standalone TAM too small to fund itself                               | **High**                   | Run as RATS flywheel + mission asset; fund from CPA income engine; don't expect ARR           |
| Cold-start (no local meetings = bad UX)                               | **Med**                    | Ingest the free Meeting Guide feed for instant directory density                              |

---

## 7. Recommendation (no hedging)

**Reframe Homegroups from an "aftercare/alumni app" into "the member-owned digital back-office for 12-step groups and intergroups," cut the referral/facility surface that imports EKRA risk, and run it as the free, mission-driven, PLG member network that distributes the portfolio and feeds RATS — not as a standalone revenue engine.** Ship the **treasurer-handoff + treasury-history lock-in** and **Meeting Guide directory ingest** first (they are the only durable moat and the cold-start fix), monetize through **transparent 7th-Tradition processing** and a **flat-fee intergroup tier**, and fund the whole thing patiently from the CPA income engine (REPORT.md #1).

Concretely, **make the entity decision in the first 90 days**: a **nonprofit or fiscally-sponsored fellowship-facing Homegroups** (monetized only by transparent processing fees + intergroup support) neutralizes the Homegroup.Online "we don't profit" attack, unlocks RCO/grant partnerships (SAMHSA BCOR is RCO-only — [SAMHSA TI-24-003](https://www.samhsa.gov/grants/grant-announcements/ti-24-003)), and aligns with the Traditions — while the **for-profit upside stays in RATS and a counsel-gated, flat-fee facility tier.** That structure is the single clearest lever: it resolves the positioning contradiction, the legal exposure, and the competitive threat at once.

---

### Sources

- AA Meeting Guide scale: [aa.org/meeting-guide-app](https://www.aa.org/meeting-guide-app) `[Verified]` · AA SMF-53 estimate: [aa.org/estimates](https://www.aa.org/estimates-aa-groups-and-members) `[re-source caveat]`
- Direct competitors: [homegroup.online/about](https://homegroup.online/about/) · [transparencytechnologies.ai/pricing](https://transparencytechnologies.ai/pricing)
- Facility incumbents: [Kipu/Team Recovery (PRNewswire)](https://www.prnewswire.com/news-releases/kipu-health-acquires-team-recovery-technologies-to-expand-patient-engagement-capabilities-and-complete-behavioral-health-platform-302751229.html) · [caredfor.com](https://www.caredfor.com/)
- Outcomes: [Cochrane CD012880.pub2](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012880.pub2/full)
- Grant path: [SAMHSA BCOR TI-24-003](https://www.samhsa.gov/grants/grant-announcements/ti-24-003)
- Pricing/legal basis: `research-dossier-v2.md` §2 (EKRA + ATTORNEY GATE), §3 (Sobriety Hub $65 flat / 3.9% card / 1.2% ACH), `homegroups-gtm-and-moat-analysis.md`
