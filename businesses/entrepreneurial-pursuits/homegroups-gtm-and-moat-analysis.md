# Homegroups — Moat Credibility & Go-to-Market Roadmap

**Generated:** 2026-06-17 via deep-research workflow `wf_f1104a43-465` (104 agents, 22 sources fetched, 25 claims adversarially verified → 24 confirmed / 1 refuted) + direct source-read of the Homegroups codebase at `/Users/marcus/dev/recovery-platform/homegroups`.
**Extends:** `research-dossier-v2.md` (§1A Layer 2, §2 EKRA, §3 GTM) and `REPORT.md` (v2), which ranked homegroups last among the recovery ventures.
**Question answered:** Is "homegroups" a credible moat for aftercare/alumni engagement vs the noted incumbents (CaredFor/ContinuumCloud, Team Recovery/Kipu), and should the functionality be approached differently? With a GTM + revenue roadmap.

**Confidence labels:** `[Verified]` primary source + adversarial vote · `[Inference]` reasoned from verified facts · `[Assumption]` plausible, unproven · `[Low-confidence]` weak/contested source · `[Time-sensitive]` may change fast.

---

## 0. TL;DR — the one thing that changes everything

**The dossier mis-filed the venture, and that misfiling produced an unfairly harsh verdict.** It judged homegroups in the _aftercare/alumni-engagement_ layer (CaredFor, Team Recovery/Kipu) and concluded "weakest, most threatened, now being bundled away by Kipu." That is correct **for a product that competes for the facility's dollar** — and the codebase confirms you have built exactly such a product (facility dashboard, engagement metrics, compliance export, **referral dashboard**). But the _app you actually built first_ is something the incumbents structurally **cannot** build: a **member-owned, fellowship-native, portable 12-step group-operations platform** (treasury, digital 7th-Tradition basket, service positions, meeting ops, intergroup service bodies).

So the answer to "is homegroups a credible moat for aftercare/alumni?" is split:

- **As an aftercare/alumni-engagement product sold to treatment centers: NO.** That battlefield is facility-tethered, consolidating into Kipu, EKRA/Part 2-exposed, and your member-ownership is irrelevant there (the facility is the buyer). `[Inference, high]`
- **As a member-owned fellowship-operations network sold to/through the 12-step service structure: YES, there is a real, structural, hard-to-copy seam** — but it is a _small, mission-bound, low-ARPU_ market with a live nonprofit competitor already in your core wedge. `[Inference, high]`

**Recommendation in one line:** Stop framing homegroups as "aftercare/alumni engagement." Reframe it as **"the digital back-office for 12-step groups and intergroups,"** cut or counsel-gate the facility/referral surface that imports EKRA risk, and treat it as a mission-driven distribution asset / flywheel for `regroup` — not a standalone revenue engine.

---

## 1. What the new research confirmed, refuted, and added

### 1.1 The incumbents are structurally facility-tethered — your differentiation is real on that axis `[Verified]`

- **Team Recovery** (acquired by **Kipu Health, April 2026** — "its largest deal yet") sells **fully white-labeled, per-facility apps** ("your own App, with your logos"), claiming **150+ US treatment centers** and **110+ partner apps launched** (i.e., separate per-facility instances). Its alumni tools were **integrated directly into the Kipu EHR platform in 2025** before the acquisition. ([PRNewswire](https://www.prnewswire.com/news-releases/kipu-health-acquires-team-recovery-technologies-to-expand-patient-engagement-capabilities-and-complete-behavioral-health-platform-302751229.html), [teamrecovery.io](https://teamrecovery.io/), [BH Business](https://bhbusiness.com/2026/04/22/exclusive-kipu-health-acquires-team-recovery-technologies-its-largest-deal-yet/))
- **CaredFor / ContinuumCloud** sells **per-facility branded apps** (e.g., Rosecrance Alumni published under bundle `com.caredfor.rhn`); buyer = the behavioral-health org. Feature set: HIPAA messaging, peer community, contingency-management rewards, possible relapse indicator, telehealth, surveys, virtual events. ([caredfor.com](https://www.caredfor.com/))
- **Key structural fact:** these apps are _owned by the facility that pays_, branded to it, and the alumni relationship dies (or goes dark) when the facility stops paying. A member-owned, portable network is the **inverse** model — and an incumbent whose entire business is "sell a branded app to the facility" cannot become member-owned without destroying its own revenue model. That is a genuine, durable axis of differentiation. `[Inference, high]`

### 1.2 …but "aftercare/alumni" is the wrong hill, and Kipu is closing it `[Verified / Time-sensitive]`

- Kipu explicitly framed the deal as extending it "beyond clinical treatment and billing into **referral growth and long-term recovery support**." The EHR leader is absorbing alumni engagement into the system of record. `[Verified]`
- **Not confirmed:** that Kipu will give alumni engagement away _free_ with the EHR — sources show integration + partnership, not free bundling. Treat "free-with-EHR" as a **live near-term risk, not a fact.** `[Time-sensitive]`
- Implication: any homegroups revenue that depends on **selling alumni engagement to a treatment center** is competing against the buyer's existing EHR vendor, on the EHR vendor's turf, with PHI/BAA/security-review friction (84+ day sales cycle per dossier §1C) and EKRA exposure. This is the single weakest place to plant a flag.

### 1.3 The dominant consumer incumbent owns the directory but leaves your operations layer wide open `[Verified]`

- **AA's official Meeting Guide app** is **free, AA-operated, funded by Seventh-Tradition contributions**, with **150,000+ weekly meetings**, **768,500+ monthly users**, synced from **500+ AA service entities**. ([aa.org](https://www.aa.org/meeting-guide-app))
- Crucially, its feature set is **strictly directory/search + Daily Reflections + local contact info**. It has **no treasury, no donations, no service positions, no attendance check-in** — and it routes corrections _back to service entities_ rather than letting groups self-administer. Because it is funded by the 7th Tradition, it is **structurally precluded from a paid/B2B model**. `[Verified]`
- **This is the most important strategic gift in the whole report:** the incumbent that owns your distribution channel (the directory) is permanently barred from monetizing and has deliberately not built the operations layer you target. The directory is commoditized and free; **group operations are not.** Don't try to out-directory AA — _integrate/parity the directory and own the operations the directory refuses to touch._ `[Inference, high]`

### 1.4 Your core wedge is NOT unoccupied — two direct competitors `[Verified]`

- **Homegroup.Online** — a **US 501(c)(3) nonprofit** — already lets 12-step groups collect **7th-Tradition donations electronically** and manage **group treasury + treasurer rotation**, and self-describes as a "National Central Office" with an about page literally titled "Group Treasury Made Simple." This is a **direct competitor in your origin wedge**, and being a nonprofit it can credibly claim the Traditions high ground and undercut you on price (free/donation-funded). ([homegroup.online](https://homegroup.online/about/)) `[Verified]`
- **Transparency Technologies** — the near-clone the dossier already flagged — confirmed to ship a **"Home groups" feature**, **GPS-verified attendance with geofencing/real-time tracking**, **AI 4th-Step / character-defect journaling powered by Anthropic Claude**, and a **four-tier model (Free / Gold / Platinum / Organization)** with separate org pricing for sober-living homes and treatment programs. **No public dollar pricing** anywhere. ([transparencytechnologies.ai/pricing](https://transparencytechnologies.ai/pricing)) `[Verified]`

### 1.5 Your headline technical features are commoditized `[Verified]`

GPS-verified attendance with geofencing is "a standard feature across modern sober-living software" (Transparency, One Step, Sober Living App, Sobriety Hub). Meeting directories are owned, free, by AA. AI journaling is already shipped by Transparency on the same model (Claude) you'd use. **None of these can carry a moat.** ([transparencytechnologies.ai/pricing](https://transparencytechnologies.ai/pricing), [aa.org](https://www.aa.org/meeting-guide-app)) `[Verified]`

### 1.6 The willingness-to-pay _outcome_ exists — but not for any app `[Verified]`

The **2020 Cochrane review** (Kelly et al., CD012880.pub2; 27 studies, 10,565 participants) found **high-certainty** evidence that manualized **AA/Twelve-Step Facilitation beats CBT** for continuous abstinence — **RR 1.21 (95% CI 1.03–1.42) at 12 months**, holding at 24 and 36 months — and **probably produces substantial healthcare cost savings** (4 of 5 economic studies). ([Cochrane](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012880.pub2/full)) **Caveat:** this validates 12-step _participation_, **not any app**, and the advantage does not extend to drinking-intensity outcomes. So the category's value is real; no vendor (including you) can yet attribute an outcome to its software. `[Verified]`

### 1.7 The B2B grant path is narrow `[Verified]`

**SAMHSA FY2024 Building Communities of Recovery (BCOR, TI-24-003):** up to **$6M total / ~20 awards / up to $300k/yr over 3 yrs**, but **eligibility is RCO-only** — independent nonprofits _wholly/principally governed by people in recovery_ with 2+ years of certified RCO status. ([SAMHSA](https://www.samhsa.gov/grants/grant-announcements/ti-24-003)) You are not the grantee; RCOs are. This matters for _who you sell to / partner with_, not a check you receive. `[Verified]`

### 1.8 Refuted / unresolved

- **Refuted (1-2 vote):** the AA "69,812 US groups / 1.56M US+Canada members (Dec 2020)" figures failed verification — **re-source fellowship size before using it in any TAM math.** `[Low-confidence]`
- **Not recovered:** facility per-alumnus pricing; consumer recovery-app ARPU/conversion/retention; current AA/NA fellowship size & intergroup count. These remain open (see §6). `[Assumption]`

---

## 2. The moat verdict (direct answer)

**Is member-ownership a credible moat for aftercare/alumni engagement vs the incumbents? — Partly, but you're pointing it at the wrong target.**

| Moat candidate                                                                 | Verdict                                                    | Why                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Member/fellowship ownership + portability**                                  | **Real & durable — but only off the facility battlefield** | Incumbents can't follow without killing their facility-paid model. Worthless as an "alumni app sold to a center"; valuable as a "fellowship-owned network." `[Inference, high]`                             |
| **GPS/QR attendance verification**                                             | **Not a moat**                                             | Commoditized across ≥4 competitors. `[Verified]`                                                                                                                                                            |
| **Meeting directory / dataset**                                                | **Not a moat**                                             | Owned free by AA Meeting Guide at 150k+ meetings. `[Verified]`                                                                                                                                              |
| **AI (4th-step journaling, etc.)**                                             | **Not a moat**                                             | Transparency ships it on the same Claude stack. `[Verified]`                                                                                                                                                |
| **Treasury + 7th-Tradition donations (your origin wedge)**                     | **Contested — a 501(c)(3) is already here**                | Homegroup.Online occupies it and can out-Tradition and undercut you. `[Verified]`                                                                                                                           |
| **Intergroup / Central Office distribution (already built: SSO + dashboards)** | **The single most defensible asset you have**              | The service structure is a real institutional buyer the consumer apps ignore and the facility apps can't reach; landing it creates top-down distribution to every affiliated group. `[Inference, med-high]` |
| **Treasury-history + treasurer-handoff data lock-in**                          | **The only true switching cost in this market**            | Volunteer treasurers rotate annually; whoever holds the continuous financial record + handoff workflow owns the account. This is your one credible lock-in. `[Inference, med]`                              |

**Bottom line:** The moat is **distribution (intergroups) + continuity data (treasury/handoff)**, not features and not "alumni engagement." Member-ownership is the _positioning_ that makes those defensible; it is not itself the moat.

---

## 3. Should you approach the homegroups functionality differently? — Yes. Specific changes.

### 3.1 Cut or counsel-gate the facility/referral surface (de-risk first) `[Inference, high]`

The codebase ships `getFacilityEngagementMetrics`, `getFacilityStats`, `exportFacilityComplianceReport`, and a **referral dashboard** (`generateReferralCode` / `applyReferralCode` / `ReferralDashboardScreen`). Per dossier §2 and the EKRA adversarial verdict (§"What it means…"), **the referral mechanic + facility engagement metrics are precisely the features that convert a benign fellowship app into criminal-exposure SaaS** under EKRA (intent-based; Louisiana is 5th Circuit, which has _not_ adopted the defense-friendly _Schena_ gloss) and 42 CFR Part 2 (any SUD-record flow to a facility). **Action:** disable the referral-to-facility flow and any patient-steering by default; if the facility tier stays, it must be **flat-fee, no per-patient/per-bed pricing, no identified-lead delivery, with a written FMV memo and an attorney sign-off** before a single dollar changes hands. Do not ship facility revenue on "flat fee = safe." `[Verified legal basis: dossier §2]`

### 3.2 Reposition from "aftercare/alumni engagement" → "digital back-office for 12-step groups & intergroups" `[Inference, high]`

This is the honest, defensible category. It (a) avoids the Kipu/CaredFor collision, (b) avoids the EHR sales-cycle and PHI gauntlet, (c) plays to member-ownership as a _feature_, and (d) targets the buyer (intergroups) the incumbents ignore.

### 3.3 Win the layer AA Meeting Guide refuses to build, and integrate (don't fight) the directory `[Inference, high]`

Parity the free directory (or ingest the public Meeting Guide feed), then own treasury, 7th-Tradition basket, service-position rotation/handoff, business-meeting minutes/voting, and announcements — the operations AA structurally won't monetize. Make **treasurer handoff continuity** the flagship: it is the one workflow that creates real switching cost.

### 3.4 Differentiate from Homegroup.Online on institution + breadth, not on "treasury" alone `[Inference, med]`

A single nonprofit already does electronic 7th-Tradition + treasury. You won't beat its Traditions credibility on donations alone. Beat it on **the full group OS + intergroup tier + multi-fellowship (NA/Al-Anon/etc.) breadth + better mobile UX** — and consider whether a **nonprofit or fiscally-sponsored structure** for the fellowship-facing product would neutralize their "we don't profit" advantage (see §5).

### 3.5 Treat homegroups as a portfolio flywheel, not a standalone P&L `[Inference, med]`

Its strongest strategic value is as the **member/fellowship-side network** that feeds `regroup` (operator-side sober-living): a recovering person uses homegroups → their sober-living house runs on regroup → warm, EKRA-clean, non-steered adjacency. Keep the two products clean of any paid referral between them, but let homegroups be the top-of-funnel brand and data network that makes regroup's GTM cheaper.

---

## 4. Go-to-Market & Revenue Roadmap

**Framing reality (read first):** The 12-step fellowship is one of the **hardest places on earth to monetize** — the 7th Tradition mandates self-support and _declining outside contributions_, anonymity caps virality and data use, treasurers are rotating volunteers, the dominant app is free-forever, and your closest wedge competitor is a nonprofit. The codebase prices reflect this (group subs at ~**$8–$12/yr**, $1/mo donation-fee tiers). **Do not model homegroups as a venture-scale SaaS.** Model it as a **mission-driven, low-ARPU network whose revenue is (1) payment-processing volume and (2) institutional/intergroup subscriptions**, funded patiently from the CPA income engine (REPORT.md #1). `[Inference, high]`

### Phase 0 (0–60 days) — De-risk & reframe

1. **Legal:** Disable referral-to-facility + patient-steering; draft the attorney-gate scope (EKRA/Part 2/LA brokering) before any facility revenue. `[from dossier §2 ATTORNEY GATE]`
2. **Positioning:** Rewrite store/site copy from "alumni/aftercare" to "the digital home for your 12-step group & intergroup." Resolve the member-ownership-vs-facility-features contradiction the research flagged on your /about page.
3. **Decide the entity question** (§5): for-profit vs nonprofit/fiscal-sponsor for the fellowship-facing product.

### Phase 1 (2–6 months) — Own group operations + land the donation rail

4. **Product:** Ship the operations moat — treasurer handoff continuity, business-meeting tools, full treasury reporting — and directory parity (ingest Meeting Guide feed). Make handoff the headline (switching cost).
5. **Revenue stream A — digital 7th-Tradition processing (volume play):** Stripe Connect platform fee on group donations/basket. Per dossier §1/§3, model this as **thin-margin pass-through, not spread** — but at fellowship scale, _volume_ of small recurring contributions is the realistic dollar engine, and it is Traditions-aligned (you only earn when groups collect). Be explicit and transparent about the fee to survive the "not to profit" scrutiny Homegroup.Online will weaponize. `[Inference, med]`
6. **Beachhead:** Use lived-recovery credibility + the SWLA/brother network to land **5–15 design-partner homegroups** free, in exchange for references. (Same warm-channel logic that carries the CPA line.)

### Phase 2 (6–18 months) — Land intergroups (the real B2B moat)

7. **Revenue stream B — intergroup/Central Office SaaS (Tier A/B already built):** Sell the **intergroup dashboard + SSO + group rollup + announcement broadcast + aggregate (anonymized) reporting** to regional service bodies. This is the defensible buyer: it has a (small) budget, it _is_ the distribution channel to every affiliated group, and neither consumer apps nor facility apps serve it. Price as **flat annual nonprofit-friendly tiers**; expect price-sensitivity and long volunteer-committee cycles. `[Inference, med]`
8. **Distribution flywheel:** Each intergroup that adopts pulls its member groups onto the operations layer top-down — the cheapest possible CAC and the closest thing to a network effect in this space.
9. **Grant-adjacent partnerships:** Partner with **RCOs** (the BCOR-eligible entities) and Central Offices as channel/credibility, not as your grantee — position homegroups as the tooling an RCO deploys. `[Inference, low-med]`

### Phase 3 (18+ months) — Only-then facility, only-if-clean

10. **Revenue stream C — facility/treatment-center tier:** Pursue _only_ behind the completed attorney gate, _only_ as flat-fee software decoupled from patient flow (anonymized aggregate engagement, no referral, no per-patient pricing), and accept it competes with Kipu-bundled alumni tools. Treat as upside, **never** as the plan's load-bearing revenue. `[Inference, high]`

### Revenue streams ranked by defensibility × EKRA-safety

| Stream                                         | Defensibility                                   | EKRA/Part 2 risk           | Verdict                          |
| ---------------------------------------------- | ----------------------------------------------- | -------------------------- | -------------------------------- |
| Digital 7th-Tradition processing (Connect fee) | Med (volume + Traditions fit)                   | **None** (no patient flow) | **Lead with it**                 |
| Intergroup / Central Office SaaS               | **High** (institutional distribution)           | None                       | **The B2B moat**                 |
| Group/admin subscription (freemium)            | Low (ARPU ~$8–12/yr; nonprofit competitor free) | None                       | Retention layer, not engine      |
| Facility / alumni tier                         | Low (Kipu collision)                            | **High**                   | Gate behind counsel; upside only |
| Any per-referral / per-patient mechanic        | n/a                                             | **Disqualifying**          | **Cut entirely**                 |

---

## 5. The entity decision you should make deliberately `[Inference, med]`

Your sharpest competitor in the core wedge (Homegroup.Online) is a **501(c)(3)**, and the dominant app (Meeting Guide) is **7th-Tradition-funded** — i.e., the fellowship rewards _non-profit_ posture and punishes visible profit-taking from anonymity. Two coherent paths:

- **(a) Mission/nonprofit (or fiscal-sponsorship) for the fellowship-facing product**, monetized only by transparent processing fees + institutional intergroup support, with the for-profit upside reserved for `regroup`/facility tooling. Neutralizes the "not to profit" attack and unlocks grant/RCO partnerships.
- **(b) For-profit but radically fee-transparent**, competing on product breadth + intergroup distribution, accepting the Traditions-optics headwind.
  Path (a) aligns better with the evidence and with treating homegroups as a flywheel rather than a profit center. Decide before you spend on brand.

---

## 6. Open questions to close before committing capital

1. **Facility alumni-engagement pricing & Kipu bundling** — does Kipu now ship Team Recovery alumni tools free/cheap with the EHR? Determines whether a facility tier is dead on arrival. `[Time-sensitive]`
2. **Real fellowship size & intergroup count** — the Dec-2020 AA figures failed verification; re-source AA/NA group/member counts and the number of intergroups/Central Offices (your actual B2B TAM). `[Low-confidence today]`
3. **Consumer recovery-app benchmarks** — ARPU, free→paid conversion, retention for I Am Sober / Reframe / Sober Grid; needed only if you ever pursue a consumer-subscription tier (currently not recommended as the engine). `[Assumption]`
4. **Homegroup.Online traction** — install base, fellowship coverage, and whether they have intergroup features; they are the competitor to benchmark, not a hypothetical. `[Assumption]`
5. **Louisiana patient-brokering statute** (5th Circuit) — required input to the attorney gate before any facility/referral revenue. `[from dossier §2]`

---

## 7. How this updates the v2 REPORT ranking

The v2 REPORT put homegroups **last** ("most ambitious, most dangerous") on the assumption it competes in aftercare/alumni. **That ranking holds for the venture as the dossier framed it, and this analysis sharpens _why_:** the aftercare framing is both un-winnable (Kipu consolidation) and legally hazardous (EKRA/referral). **But it also surfaces a narrower, more defensible identity** — fellowship-native group/intergroup operations — that the dossier never evaluated because it never separated the two products. Recommend: **keep homegroups last as a revenue bet, but reclassify it as a mission-driven distribution/flywheel asset for `regroup`,** de-risked per §3.1, and funded patiently from the CPA income engine rather than expected to stand alone.

---

### Sources (this analysis)

- Kipu/Team Recovery acquisition: [PRNewswire](https://www.prnewswire.com/news-releases/kipu-health-acquires-team-recovery-technologies-to-expand-patient-engagement-capabilities-and-complete-behavioral-health-platform-302751229.html) · [BH Business](https://bhbusiness.com/2026/04/22/exclusive-kipu-health-acquires-team-recovery-technologies-its-largest-deal-yet/) · [HIT Consultant](https://hitconsultant.net/2026/04/23/kipu-health-acquires-team-recovery-technologies/) · [teamrecovery.io](https://teamrecovery.io/)
- CaredFor/ContinuumCloud: [caredfor.com](https://www.caredfor.com/) · [ContinuumCloud blog](https://continuumcloud.com/blogs/mobile-first-patient-engagement-app-improves-outcomes-bonus-reimbursement)
- AA Meeting Guide app: [aa.org/meeting-guide-app](https://www.aa.org/meeting-guide-app)
- Direct wedge competitors: [homegroup.online/about](https://homegroup.online/about/) · [transparencytechnologies.ai/pricing](https://transparencytechnologies.ai/pricing)
- Homegroups own positioning: [homegroups-app.com/about](https://homegroups-app.com/about)
- Outcomes evidence: [Cochrane CD012880.pub2 (Kelly et al. 2020)](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012880.pub2/full) · [NIAAA continuing-care](https://arcr.niaaa.nih.gov/recovery-aud-part-2/impact-continuing-care-recovery-substance-use-disorder) · [PMC12811009](https://pmc.ncbi.nlm.nih.gov/articles/PMC12811009/) · [PMC12104978](https://pmc.ncbi.nlm.nih.gov/articles/PMC12104978/)
- Grant path: [SAMHSA BCOR TI-24-003](https://www.samhsa.gov/grants/grant-announcements/ti-24-003)
- Consumer benchmark fragments: [ChoosingTherapy — I Am Sober](https://www.choosingtherapy.com/i-am-sober-app-review/) · [Adapty — I Am Sober paywall](https://adapty.io/paywall-library/i-am-sober/) · [MedCity — Sober Sidekick funding](https://medcitynews.com/2025/12/funding-sober-sidekick-app/)
- Legal basis for §3.1 / §4 Phase 3: `research-dossier-v2.md` §2 (EKRA-Safe Bridge + ATTORNEY GATE), §1C (sales cycle / PHI friction)

**Refuted / re-source before use:** AA group & member counts (Dec 2020) — failed verification ([aa.org/estimates](https://www.aa.org/estimates-aa-groups-and-members)).
