# Research Dossier v2 — Cited Evidence Ledger
**Generated:** 2026-06-08 via multi-agent research workflow `wf_33de57cf-dde`.
All figures carry inline sources; unverifiable items are flagged `[VERIFY]`. This is the evidence backing `REPORT.md` (v2).

---

## 1A. Treatment-Industry Incumbent Software Teardown

I have sufficient verified material across all targets. Writing the deliverable now.

---

# Treatment-Industry Incumbent Software Teardown

*Scope: software serving addiction/SUD treatment centers (detox, residential, PHP/IOP, outpatient) and sober-living/recovery-residence operators. Focus = market position + documented weaknesses + displaceable wedges relevant to an AI-native builder. Devil's-advocate lens applied throughout.*

## Market structure at a glance

The category splits into three layers, and the competitive dynamics differ sharply by layer:

1. **Clinical EHR/EMR (the entrenched core)** — Kipu, Sunwave/Lightning Step, Alleva, BestNotes, Ritten, Opus, NextGen. High switching costs (clinical records, billing config, state compliance, staff retraining). This is where displacement is *hardest* and where `regroup` should NOT try to compete head-on.
2. **Aftercare / alumni engagement (adjacent, consolidating fast)** — CaredFor/ContinuumCloud, Team Recovery (just acquired by Kipu). Directly adjacent to `homegroups`.
3. **Sober-living / recovery-residence management (fragmented, displaceable)** — Sobriety Hub, One Step, Behave Health, Sober Living App. This is `regroup`'s exact battleground, and it is the *least* defensible layer — active churn is happening right now.

**Critical signal for the portfolio thesis:** The EHR layer is consolidating under private equity (Kipu/TCV; Sunwave+Lightning Step merger) and racing to bolt on AI. That means (a) the "no AI" wedge is closing fast at the top, and (b) the incumbents are buying their way into aftercare and sober-living adjacencies — which is exactly where `regroup` and `homegroups` live. This is the single most important finding for go/no-go.

---

## Layer 1 — Clinical EHR/EMR incumbents

### Kipu Health — the market leader
- **What it does:** All-in-one EHR + CRM + RCM purpose-built for SUD/behavioral health; residential and detox are its core strength. ([kipuhealth.com](https://www.kipuhealth.com/))
- **Segment:** Residential / detox / PHP/IOP treatment centers. The default "serious facility" choice.
- **Market position:** Clear category leader by installed base — company/aggregator data cites **~4,000–6,000 facilities, ~140,000 users, ~4M episodes of care/year** [VERIFY exact figure — sources disagree between 4,000 and 6,000]. ([ehrsource.com](https://www.ehrsource.com/vendors/kipu/), [6sense](https://6sense.com/tech/electronic-health-records-ehr/kipu-market-share))
- **Ownership/strategy:** Backed by **TCV** (growth-equity; CEO Paul Joiner installed). Acquired **Hatch Compliance**, and in **April 2026 acquired Team Recovery Technologies** (alumni/patient engagement) — its largest deal to date. ([bhbusiness.com](https://bhbusiness.com/2026/04/22/exclusive-kipu-health-acquires-team-recovery-technologies-its-largest-deal-yet/), [mobihealthnews](https://www.mobihealthnews.com/news/kipu-health-acquires-hatch-compliance-expand-behavioral-health-offerings))
- **Pricing (public-ish):** ~$600/mo entry, scaling to **~$10,000/mo** for a ~400-patient facility with the full stack; layered/tiered subscriptions. ([ehrsource.com](https://www.ehrsource.com/articles/kipu-problems-2026/))
- **Documented weaknesses (G2/Capterra/EHR Source):**
  - **Scheduling does not auto-sync to clinical documentation** — staff manually bridge calendar and chart fields. Most-cited workflow complaint. ([ehrsource.com](https://www.ehrsource.com/articles/kipu-problems-2026/))
  - **No built-in task management; extra clicks for PRN/med-pass** workflows.
  - **Escalating, opaque, layered cost** — repeatedly called unsustainable for small practices; "not as effective as cheaper alternatives." ([capterra](https://www.capterra.com/p/156391/Kipu-EMR/))
  - **Support degraded since ~2021** — shift to ticket-based, slower, less personal (a classic PE-rollup tell).
  - **Over-engineered for outpatient/solo** — friction outside residential.
- **Devil's advocate:** Despite all complaints, Kipu is sticky because it's the compliance-trusted default. Weaknesses are *irritation-level*, not *switch-now* level, for residential clients.

### Sunwave Health + Lightning Step (merged 2025) — the AI-native challenger to Kipu
- **What it does:** EMR + CRM + RCM + telehealth + alumni in one platform; markets itself as **"AI-native"** with auto-generated progress notes/session summaries. ([sunwavehealth.com](https://sunwavehealth.com/))
- **Segment:** SUD/behavioral health treatment centers; strong on admissions CRM and reporting.
- **Position:** **Sunwave and Lightning Step merged in 2025** (Lightning Step acquired Oct 2025) — a deliberate roll-up to challenge Kipu. ([behavehealth.com](https://behavehealth.com/blog/sunwave-health-vs-behave-health-behavioral-health-ehr-comparison), [lightningstep.com](https://www.lightningstep.com/))
- **Claimed metrics:** "40% reduction in admin time, 25% fewer billing errors, 12.5 hrs/clinician/month recovered" — **vendor-stated, unverified** [VERIFY]. ([ehrsource.com](https://www.ehrsource.com/vendors/sunwave/))
- **Pricing:** Not public; negotiated/quote-based. ([capterra](https://www.capterra.com/p/172475/Sunwave/))
- **Documented weaknesses (Lightning Step side, Capterra):** "UI is clunky, server is slow, customer service is appalling"; **billing charges not auto-dropping**, **appointment reminders not delivering**, weeks-long support resolution; difficult initial setup needing more technical expertise than expected. Post-merger integration risk is real. ([behavehealth.com](https://behavehealth.com/lightning-step-issues), [capterra](https://www.capterra.com/p/223862/Lightning-Step-Suite/))
- **Devil's advocate:** Sunwave is the most direct evidence that "AI-native behavioral-health software" is *already being built and funded*. The AI wedge at the EHR layer is contested, not open.

### Ritten — the well-funded AI-native upstart (watch closely)
- **What it does:** Unified EMR + practice management for behavioral health/addiction; markets "Simple Software for Complex Treatment," AI-powered. ([ritten.io](https://www.ritten.io/))
- **Position/funding:** **Raised $35M Series B in Dec 2025** (Five Elms Capital lead; Threshold, 8VC, Bienville). This is the best-capitalized recent entrant and explicitly "AI-powered." ([hitconsultant.net](https://hitconsultant.net/2025/12/16/ritten-raises-35m-to-scale-ai-powered-behavioral-health-platform/))
- **Strengths (reviews):** Ease of use, intuitive UI, smoother migrations than expected, built *by* behavioral-health-listening IT pros. ([softwareadvice](https://www.softwareadvice.com/product/508591-Ritten/))
- **Weaknesses:** Thin public review corpus (newer product, fewer Capterra/G2 reviews) — the main "weakness" is unproven scale, not documented complaints. ([capterra](https://www.capterra.com/p/276907/Ritten/))
- **Devil's advocate:** Ritten is the clearest proof that VCs are funding *exactly* the "AI-native, better-UX, easy-migration" thesis a solo builder might pursue. A senior engineer with $0 funding competing on the EHR core against a $35M-funded AI-native EHR is a losing fight.

### BestNotes — the bootstrapped value option
- **What it does:** Cloud EHR + CRM for SUD/behavioral health; admissions pipeline + clinical + e-prescribing + telehealth + med management. ([bestnotes.com](https://www.bestnotes.com/behavioral-health-ehr/))
- **Differentiator:** **Bootstrapped since 2003 (Twin Falls, ID)** — no PE/VC/corporate parent, pitched as pricing stability. ([ehrsource.com](https://www.ehrsource.com/vendors/bestnotes/))
- **Weakness:** Older platform; competes on price/stability rather than modern UX or AI. Vulnerable on the AI/UX axis precisely because it won't take capital to modernize aggressively.

### Alleva — SMB-friendly
- **What it does:** Behavioral health/addiction EHR aimed at small-to-mid practices; "best value for money" per Software Advice verified users. ([selecthub](https://www.selecthub.com/p/mental-health-software/alleva/), [softwareadvice](https://www.softwareadvice.com/medical/mental-health-emr-billing-software-comparison/))
- **Pricing:** Not posted; demo-gated, reportedly value-tier. ([capterra](https://www.capterra.com/p/180899/Alleva/))
- **Weakness:** Limited public detail on AI; positioned on value, not innovation.

### Opus EHR & NextGen
- **Opus:** Integrated EHR suite targeting behavioral health/addiction; mid-tier player, limited differentiated public review data. ([softwarefinder.com](https://softwarefinder.com/emr-software/opus))
- **NextGen:** This is **NextGen Healthcare** — a large *general* ambulatory EHR, not a SUD-specialist. It shows up in behavioral-health lists but is the generalist incumbent that specialists like Kipu beat on workflow fit. There is no distinct "NextGen Behavioral Health" product; treat as a generalist competitor, not a vertical incumbent. ([ehrsource.com sources above])

---

## Layer 2 — Aftercare / alumni engagement (relevant to `homegroups`)

### CaredFor / ContinuumCloud
- **What it does:** Patient/alumni/family engagement app for treatment programs — private community, micro-interactions, and a **"relapse indicator"** that analyzes in-app behavior to flag at-risk users and alert staff. ([caredfor.com](https://www.caredfor.com/), [continuumcloud.com](https://continuumcloud.com/behavioral-health-software/caredfor/))
- **Position:** Widely adopted by "top" treatment programs; part of the larger ContinuumCloud behavioral-health suite.
- **Weakness / opening:** It's a closed, facility-sponsored community tethered to the program that pays for it — *not* a portable, member-owned recovery network. The relapse-prediction is interaction-heuristic, not clinically validated [VERIFY].
- **Devil's advocate for `homegroups`:** **Kipu just bought Team Recovery (April 2026)** — the EHR leader is now bundling alumni engagement into its core platform. ([bhbusiness.com](https://bhbusiness.com/2026/04/22/exclusive-kipu-health-acquires-team-recovery-technologies-its-largest-deal-yet/)) A standalone aftercare app now competes against *free-with-your-EHR* bundling. This materially weakens `homegroups`' B2B "Institutional tier" distribution thesis.

---

## Layer 3 — Sober-living / recovery-residence (the displaceable layer — `regroup`'s arena)

This is the **only layer with active, documented incumbent churn**, which is exactly why it's the most credible wedge.

### Sobriety Hub — the momentum leader
- **What it does:** Sober-living management — residents, automated payments, compliance, outcomes tracking; resident mobile app. ([sobrietyhub.com](https://www.sobrietyhub.com/))
- **Position:** Claims **1,000+ recovery residences**; explicitly winning switchers. ([sobrietyhub.com](https://www.sobrietyhub.com/))
- **Key signal:** Per Sobriety Hub's own (self-interested) data, **operators switched from One Step to Sobriety Hub ~3:1 in 2025**, accelerating into 2026 — citing more intuitive UI, faster support, and the resident mobile app. ([behavehealth/sobrietyhub blog](https://www.sobrietyhub.com/our-blog/2026-buyers-guide-the-big-3-of-sober-living-software)) **Discount this number — it's the winner's own marketing — but the direction is corroborated.**

### One Step Software — the incumbent losing ground
- **What it does:** "Software made for sober livings and recovery coaches"; claims **2,000+ organizations**; rent/fee tracking, peer-support documentation. ([capterra](https://www.capterra.com/p/195924/One-Step-Software/))
- **Rating:** **4.6 Capterra** (vs Behave Health 4.9). ([capterra/behavehealth, Jan 2026](https://behavehealth.com/recovery-residences))
- **Documented weaknesses:** Switchers cite **less intuitive interface, slower/less-responsive support, and a weaker resident mobile app** — the exact three reasons given for defection. This is a textbook displaceable incumbent: large base, dated UX, support complaints, losing on mobile. ([sobrietyhub blog](https://www.sobrietyhub.com/our-blog/2026-buyers-guide-the-big-3-of-sober-living-software))
- **Pricing:** Custom/quote-only. ([capterra](https://www.capterra.com/p/195924/One-Step-Software/))

### Behave Health
- **What it does:** All-in-one for sober living/halfway/transitional housing — bed tracking, resident mgmt, billing, **NARR compliance**; also sells full EHR/CRM/RCM. ([behavehealth.com](https://behavehealth.com/recovery-residences))
- **Rating:** **4.9 Capterra** (Jan 2026); NARR-affiliate discounts. ([behavehealth.com](https://behavehealth.com/recovery-residences))
- **Note:** Behave Health publishes most of the comparison content cited here — treat its competitive claims as marketing, well-organized but self-serving.

### Sober Living App / others
- Additional fragmented players (Sober Living App, etc.) confirm the layer is crowded but *commoditized on features* and *differentiated on UX/support/mobile* — not on defensible data or compliance moats. ([soberlivingapp.com](https://soberlivingapp.com/blog/sober-living-software-comparison))

**Bottom line for `regroup`:** No single dominant, defensible incumbent. The leaders win on UX, support responsiveness, and resident mobile app — all *executional*, not structural, advantages. That is good news (displaceable) and bad news (your claimed moats below may not hold).

---

## Where the leaders are genuinely weak / displaceable

| Weakness | Who it hits | Displaceability |
|---|---|---|
| Scheduling↔documentation gaps, extra-click med workflows | Kipu | Medium — irritation, not switch-trigger |
| Degraded, ticket-based support post-PE | Kipu, Lightning Step | **High** — most-cited switch reason across layers |
| Clunky UI / slow servers / billing config failures | Lightning Step/Sunwave | Medium-High (but merger may fix) |
| Dated UX + weak resident mobile app | One Step | **High — active churn happening now** |
| Bootstrapped, slow-to-modernize | BestNotes | Medium (AI/UX axis) |
| Closed, facility-tethered aftercare communities | CaredFor | Medium — but Kipu/Team Recovery bundling closes this |

The consistent, cross-vendor weak point is **support responsiveness and modern UX/mobile**, not features and not AI per se. AI is already being funded aggressively at the top (Sunwave "AI-native," Ritten's $35M).

---

## The 3–4 most credible wedge gaps for an AI-native, lived-recovery, senior-engineer builder

**1. Sober-living management with a genuinely best-in-class resident mobile app + responsive support (the `regroup` wedge — strongest).**
This is the only layer with documented, active churn, no defensible incumbent moat, and the winning axis (UX + support + resident app) is exactly where a senior engineer with lived credibility can out-execute. **Caveat:** your claimed moats (GPS meeting verification, 300K-meeting dataset, OHWS partnership) are not matched by any incumbent's claims — which is *suspicious*. Either they're real differentiators (verify defensibility) or competitors don't have them because operators don't value them enough to pay [VERIFY demand for GPS verification specifically].

**2. The compliance/operations layer the EHRs under-serve: state licensing, NARR/recovery-residence compliance, audit-readiness — AI-automated.**
Kipu bought Hatch Compliance because this is painful and unsolved well. ([mobihealthnews](https://www.mobihealthnews.com/news/kipu-health-acquires-hatch-compliance-expand-behavioral-health-offerings)) An AI agent that keeps a small facility/sober-living audit-ready is a wedge that (a) the big EHRs treat as a bolt-on and (b) plays to a senior engineer's strength. Lower regulatory risk than clinical scope.

**3. The "scheduling↔documentation↔billing glue" + support that incumbents fail at — sold as integration/automation, not a rip-and-replace EHR.**
Every EHR's top complaints are connective-tissue failures (Kipu's calendar↔chart gap; Lightning Step's charges-not-dropping). An AI-native middleware/automation layer that sits *on top of* existing EHRs sidesteps the unwinnable EHR-replacement fight while monetizing their weaknesses. This is also the most natural bridge to the CPA-advisory/automation income engine — same "AI automation over an entrenched system of record" pattern.

**4. Portable, member-owned aftercare/peer network (the `homegroups` wedge — weakest, now threatened).**
CaredFor's facility-tethered model leaves room for a member-owned network — *but* Kipu's Team Recovery acquisition means alumni engagement is becoming a free EHR add-on. This wedge is closing. Pursue only as a flywheel/distribution feature of #1, not as a standalone B2B product.

## What it takes to displace an entrenched EHR (the hard truth)
You **cannot** displace Kipu/Sunwave/Ritten on the clinical EHR core as a solo, unfunded builder — switching costs (records migration, billing reconfig, state compliance, staff retraining) plus $35M-funded AI-native competitors make it a capital and trust war you lose. Displacement of the *core* requires either (a) 10x lower switching cost via automated migration + parallel-run, (b) a regulatory/compliance capability they structurally lack, or (c) a beachhead segment they over-serve (solo/outpatient/sober-living) where you win on UX+support+mobile, then expand. **The defensible strategy is to attack the adjacencies and connective tissue (wedges 1–3), not the system of record** — which aligns with the portfolio's "sequence, don't parallelize; sober-living first" thesis. The biggest threat to that thesis is timing: PE-backed incumbents are consolidating the exact adjacencies (`regroup`, `homegroups`) right now.

---

### Sources
- Kipu problems/pricing/support: https://www.ehrsource.com/articles/kipu-problems-2026/ · https://www.capterra.com/p/156391/Kipu-EMR/ · https://www.ehrsource.com/vendors/kipu/ · market share https://6sense.com/tech/electronic-health-records-ehr/kipu-market-share
- Kipu PE/acquisitions: https://bhbusiness.com/2026/04/22/exclusive-kipu-health-acquires-team-recovery-technologies-its-largest-deal-yet/ · https://www.mobihealthnews.com/news/kipu-health-acquires-hatch-compliance-expand-behavioral-health-offerings
- Sunwave/Lightning Step: https://sunwavehealth.com/ · https://www.ehrsource.com/vendors/sunwave/ · https://www.lightningstep.com/ · https://behavehealth.com/lightning-step-issues · https://www.capterra.com/p/223862/Lightning-Step-Suite/
- Ritten: https://www.ritten.io/ · https://hitconsultant.net/2025/12/16/ritten-raises-35m-to-scale-ai-powered-behavioral-health-platform/ · https://www.capterra.com/p/276907/Ritten/
- BestNotes/Alleva/Opus/NextGen: https://www.ehrsource.com/vendors/bestnotes/ · https://www.bestnotes.com/behavioral-health-ehr/ · https://www.selecthub.com/p/mental-health-software/alleva/ · https://www.capterra.com/p/180899/Alleva/ · https://softwarefinder.com/emr-software/opus · https://www.softwareadvice.com/medical/mental-health-emr-billing-software-comparison/
- CaredFor/ContinuumCloud: https://www.caredfor.com/ · https://continuumcloud.com/behavioral-health-software/caredfor/
- Sober-living layer (Sobriety Hub, One Step, Behave Health): https://www.sobrietyhub.com/ · https://www.sobrietyhub.com/our-blog/2026-buyers-guide-the-big-3-of-sober-living-software · https://www.capterra.com/p/195924/One-Step-Software/ · https://behavehealth.com/recovery-residences · https://soberlivingapp.com/blog/sober-living-software-comparison

[VERIFY] flags: exact Kipu facility count (4,000 vs 6,000); Sunwave's vendor-claimed efficiency metrics; CaredFor relapse-indicator clinical validation; real-world demand/willingness-to-pay for GPS meeting verification; defensibility of `regroup`'s claimed 300K-meeting dataset and OHWS partnership vs incumbents who don't advertise these.

---

## 1B. AI-Adoption Gap + Market Sizing (TAM)

Relapse-risk prediction is heavily academic (research papers, not commercial products) — confirming a buildability/weak-incumbent gap, but also a hard-to-monetize/clinical-liability one. I have enough to synthesize a strong, well-cited deliverable. I'll stop searching to respect cost. Let me note the HHS ASPE adoption stat is in the meritalk source already (38% state-government facilities). I have sufficient data.

Here is the deliverable.

---

# AI-Adoption Gap + Market Sizing — SUD / Behavioral-Health Treatment Software

*Scope: US substance-use-disorder (SUD) and behavioral-health (BH) treatment facilities and the EHR / RCM / utilization-review / aftercare software they run on. Devil's-advocate lens throughout. Verified figures carry inline sources; estimates marked [est]; unconfirmed marked [VERIFY].*

## (b) Market sizing — do this first; it frames the gap

### How many facilities, and the outpatient/residential split

SAMHSA's 2023 N-SUMHSS (the successor to N-SSATS) is the authoritative count. It is based on self-reported data from **20,681 unique treatment facilities, of which 14,620 provide substance-use (SU) treatment**, 9,856 provide mental-health treatment, and 3,795 do both. ([SAMHSA 2023 N-SUMHSS Annual Report PDF](https://www.samhsa.gov/data/sites/default/files/reports/rpt53012/2023-nsumhss-annual-report.pdf))

Care-setting split **among the 14,620 SU facilities** (facilities offer multiple settings, so these are not mutually exclusive — Table A in the report):

| Setting | SU facilities | % of 14,620 |
|---|---|---|
| Outpatient | 12,166 | **83.2%** |
| Residential (non-hospital 24-hr) | ~3,572 | **~24.4%** [VERIFY exact N] |
| Hospital inpatient | 1,068 | **7.3%** |

Source: [SAMHSA 2023 N-SUMHSS Annual Report](https://www.samhsa.gov/data/sites/default/files/reports/rpt53012/2023-nsumhss-annual-report.pdf). Ownership: **91% of SU facilities are privately operated** (43.7% private for-profit, the rest private non-profit) — i.e., the buyers are private businesses, not government, which matters for a self-serve sales motion. On the census-pain point, **designated-bed utilization for SU facilities was 96%** (MH 104%), confirming bed/occupancy management is a live operational metric (same report).

Point-in-time client volume: **1,592,193 people in SUD treatment** on the March 31, 2023 reference date (1,924,541 in MH treatment) (same report). Note this is a single-day snapshot, not annual throughput — annual unique patients are far higher.

**Devil's advocate:** 14,620 is the *total* universe. The privately-operated, mid-sized residential/IOP/PHP operators who actually buy software and feel billing pain are a smaller slice — realistically a few thousand viable accounts, not 14,620. Do not size a business off the headline number.

### Software & EHR market size / growth

Estimates vary widely by analyst and by how "behavioral health" is scoped — treat any single number skeptically:

- **US Behavioral Health EHR**: USD **286.74M (2024) → ~519M (2030), 10.37% CAGR** ([Grand View Research](https://www.grandviewresearch.com/industry-analysis/us-behavioral-health-ehr-market-report)). A second analyst puts it at **$316.5M (2024) → $849.7M (2034)** ([Nova One Advisor](https://www.novaoneadvisor.com/report/us-behavioral-health-ehr-market)).
- **Global BH EHR**: **$1.56B (2025) → $2.74B (2030), 11.87% CAGR** ([Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/behavioral-health-ehr-market)).
- **Mental-health software (broader)**: **$6.7B (2025) → $19.4B (2032), 16.4% CAGR** ([Persistence Market Research](https://www.persistencemarketresearch.com/market-research/mental-health-software-market.asp)).

**Devil's advocate:** The pure US BH-EHR TAM (~$287M) is *small* — a solo founder cannot win by being "another EHR." Grand View lists 15 incumbents already (Netsmart, Valant, TherapyNotes, Kipu/Opus, NextStep, ICANotes, Streamline, etc. — [Grand View](https://www.grandviewresearch.com/industry-analysis/us-behavioral-health-ehr-market-report)). The opportunity is a **wedge layer on top of incumbents**, not a rip-and-replace.

### EHR adoption lag (the structural reason AI is absent)

BH/SUD providers were excluded from the HITECH "meaningful use" EHR incentives, so adoption historically trailed medical providers badly: **only ~38% of state-government treatment facilities had adopted EHRs** per ONC, with adoption higher among private for-profits ([MeriTalk summarizing HHS/ONC](https://www.meritalk.com/articles/ehr-adoption-lags-in-some-treatment-facilities-as-need-grows-hhs-says/)); HHS ASPE similarly found BH EHR use "lags behind" general medical ([HHS ASPE report](https://aspe.hhs.gov/sites/default/files/documents/b9f858a38ff71660528cf1e4b8df00fa/HIT-adoption-utilization-bh-settings.pdf)). By 2026 trade press reports the gap has largely closed on *basic* EHR adoption, but **~25% of providers still run EHR + paper in parallel** and data-sharing/interoperability remains "stuck in the past" ([Behavioral Health Business, Apr 2026](https://bhbusiness.com/2026/04/23/behavioral-health-has-caught-up-on-ehrs-but-data-sharing-is-still-stuck-in-the-past/)). Implication: incumbents won the *records* layer recently; almost none have layered *AI* on top yet.

IT-spend norms: I could not find a clean per-facility BH IT-spend benchmark. **[VERIFY]** — treat any IT-budget figure as unverified.

### RCM / denial pain (the dollar wound)

This is the most concrete, quantified pain in the whole space:

- **BH claims are denied ~85% more often than general medical claims; 2026 BH denial rates run 12–20% vs 5–10% medical** ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial)).
- **82–85% of BH denials are preventable** (front-end / documentation / authorization). ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial))
- **~60% of denied claims are never resubmitted** → permanent revenue loss; rework costs $25–$181/claim. ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial); industry-wide "~half of denials never reworked" corroborated by [Waystar 2024 via LinkedIn summary](https://www.linkedin.com/posts/john-peter-49577219b_rcm-denialmanagement-healthcarerevenuecycle-activity-7349373744483627008-gYmw))
- **81.7% of *appealed* BH denials get overturned** — i.e., the money is recoverable; the bottleneck is labor to fight denials. ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial))
- Top denial drivers are BH-idiosyncratic: per-session medical-necessity justification, psychotherapy CPT time mismatches (90832/34/37), MHPAEA parity, **IOP/PHP/residential authorization gaps**, and **SUD-specific coding + 42 CFR Part 2 issues** ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial)).
- Cross-industry baseline: initial denial rate rose to **11.81% in 2024**, ~50% front-end driven ([Becker's / Waystar 2024](https://www.beckerspayer.com/payer/claims-denial-rates-up-prior-auth-denials-down-in-2024-report/)).

## (a) Where AI is missing today — gap-by-gap

| Function | State of AI today | Incumbent coverage | Verdict |
|---|---|---|---|
| **AI clinical documentation / ambient notes** | **Already solved & competitive.** Eleos Health (BH-specific ambient scribe), Commure Scribe (75k+ clinicians, BH support) | **Strong** — funded, BH-native players | **Avoid — too late** ([Eleos](https://eleos.health/), [Commure](https://www.commure.com/blog-scribe/ai-therapy-notes)) |
| **Intake / admissions automation** | Emerging in general medical (Elion lists intake/eligibility AI agents), little BH-native | Medium (general-purpose, not BH) | Possible, but crowded by horizontal players ([Elion](https://elion.health/categories/prior-authorization/products)) |
| **Utilization review & prior-auth / level-of-care** | AI prior-auth is booming on the **payer** side and the **general-medical provider** side (Cohere, Innovaccer, OmniMD, Develop Health). **No BH/SUD-native provider-side UR tool surfaced** for ASAM level-of-care continued-stay reviews. | **Weak in BH** — all vendors are general-medical claim submission, not BH concurrent UR | **STRONG GAP** ([Cohere](https://coherehealth.com/blog/five-emerging-trends-in-prior-auth/), [Innovaccer](https://innovaccer.com/resources/blogs/top-5-ai-vendors-for-prior-authorization-2025), [MACPAC](https://www.macpac.gov/wp-content/uploads/2025/02/07_February-Slides_Automation-in-the-Prior.pdf)) |
| **Documentation-compliance / audit** | Eleos has launched an "AI documentation integrity / compliance" product | Medium — Eleos moving in | Contested ([Eleos](https://eleos.health/)) |
| **Denial-rate reduction / RCM** | Horizontal AI denial tools exist; ~50% of denials never reworked industry-wide. **No surfaced BH-native pre-bill scrubber** tuned to BH denial drivers (parity, ASAM auth, 42 CFR Part 2, CPT-time) | **Weak in BH** | **STRONG GAP** ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial)) |
| **Census/occupancy & no-show prediction** | Almost entirely **academic** (medRxiv dropout/no-show models); no commercial BH product surfaced | **Weak/none commercial** | Buildable but monetization-soft ([medRxiv 2025](https://www.medrxiv.org/content/10.1101/2025.07.10.25331331v1.full.pdf)) |
| **Relapse-risk scoring** | Purely **research-stage** (Nature Medicine, PMC, Drexel models; smartphone digital-phenotyping) | **None commercial** | **Avoid as primary** — clinical-liability + reimbursement-unclear; weak willingness-to-pay ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10700303/), [public-health AI handbook](https://publichealthaihandbook.com/applications/substance-use.html)) |

## Conclusion — best gap for a solo, AI-native founder

**Winner: AI-driven utilization-review + denial-prevention for SUD/IOP/PHP/residential billing — i.e., a "BH revenue-rescue / pre-bill + concurrent-UR copilot" layered on top of existing EHRs.** It uniquely maxes all three filters:

1. **Acute, quantified pain.** 12–20% BH denial rates (85% above medical), 82–85% preventable, 60% never reworked, but 81.7% of appeals win. The money is real, recoverable, and currently lost to a *labor* bottleneck — exactly what an AI agent replaces. ([BlueBrix](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial))
2. **Weak incumbent coverage.** Every AI prior-auth/denial vendor found is general-medical or payer-side; none is tuned to BH's idiosyncratic denial drivers (ASAM level-of-care continued-stay UR, MHPAEA parity, 42 CFR Part 2, psychotherapy CPT-time). The well-funded BH-AI players (Eleos, Commure) sit in *documentation*, not *RCM/UR* — and documentation is already lost. ([Cohere](https://coherehealth.com/blog/five-emerging-trends-in-prior-auth/), [Innovaccer](https://innovaccer.com/resources/blogs/top-5-ai-vendors-for-prior-authorization-2025))
3. **Buildable solo, AI-native.** It is a text/document problem (clinical notes → medical-necessity justification, CPT/time/parity checks, ASAM criteria mapping, draft appeal letters) — pure LLM territory, no proprietary clinical dataset or device required. It sits *on top of* the EHR (no rip-and-replace against 15 incumbents) and is **ROI-priced**: charge a % of recovered/denial-avoided revenue, which is trivially justifiable when 60% of denials are otherwise abandoned.

**Why not the others:** Ambient documentation is already won. Relapse-risk and no-show/census prediction are research-stage with weak willingness-to-pay and clinical-liability exposure — operators won't pay for a risk score, but they *will* pay for recovered cash.

**Key risks / unknowns to validate next:**
- **Payer-side AI arms race:** insurers are deploying AI to *deny* faster ([Health Law](https://healthlaw.org/federal-ai-policy-threatens-prior-authorization-reform/), [PMC Medicare Advantage](https://pmc.ncbi.nlm.nih.gov/articles/PMC12979811/)). This *strengthens* a provider-side counter-tool but means racing a moving target.
- **42 CFR Part 2 + HIPAA** constrain feeding SUD records to LLMs — architecture (BAA-covered models, de-identification) is a real constraint, not a blocker. [VERIFY] viable model/BAA path.
- **Buyer concentration:** real SAM is a few thousand private IOP/PHP/residential operators, not 14,620. [VERIFY] willingness-to-pay via Marcus's brother's CPA-client network (treatment-center clients) before building.
- **Distribution fit:** this slots directly into the v1 thesis — it's a sellable wedge into the same treatment-center buyers `homegroups`/`detox-recovery` already target, and complements (doesn't compete with) `regroup`'s sober-living focus.

**Sources** (primary): [SAMHSA 2023 N-SUMHSS](https://www.samhsa.gov/data/sites/default/files/reports/rpt53012/2023-nsumhss-annual-report.pdf) · [Grand View US BH EHR](https://www.grandviewresearch.com/industry-analysis/us-behavioral-health-ehr-market-report) · [Mordor BH EHR](https://www.mordorintelligence.com/industry-reports/behavioral-health-ehr-market) · [Nova One BH EHR](https://www.novaoneadvisor.com/report/us-behavioral-health-ehr-market) · [BlueBrix BH denials](https://bluebrix.health/blogs/the-top-reasons-behavioral-health-claims-denial) · [Becker's/Waystar 2024 denials](https://www.beckerspayer.com/payer/claims-denial-rates-up-prior-auth-denials-down-in-2024-report/) · [MeriTalk/ONC EHR adoption lag](https://www.meritalk.com/articles/ehr-adoption-lags-in-some-treatment-facilities-as-need-grows-hhs-says/) · [BH Business 2026 adoption](https://bhbusiness.com/2026/04/23/behavioral-health-has-caught-up-on-ehrs-but-data-sharing-is-still-stuck-in-the-past/) · [Eleos](https://eleos.health/) · [Commure](https://www.commure.com/blog-scribe/ai-therapy-notes) · [Cohere prior-auth](https://coherehealth.com/blog/five-emerging-trends-in-prior-auth/) · [Innovaccer AI prior-auth vendors](https://innovaccer.com/resources/blogs/top-5-ai-vendors-for-prior-authorization-2025) · [MACPAC PA automation](https://www.macpac.gov/wp-content/uploads/2025/02/07_February-Slides_Automation-in-the-Prior.pdf) · [medRxiv SUD no-show/dropout](https://www.medrxiv.org/content/10.1101/2025.07.10.25331331v1.full.pdf) · [PMC AI SUD outcomes](https://pmc.ncbi.nlm.nih.gov/articles/PMC10700303/)

---

## 1C. Treatment-Center Buyer, Budget & Sales Motion

I have sufficient evidence to synthesize. Here is the deliverable.

---

## Treatment-Center Buyer, Budget & Sales Motion (SUD Behavioral-Health SaaS)

### 1. Who actually buys — and it depends on facility size

Authority splits by org structure, and the homegroups/regroup "Institutional tier" thesis needs to internalize this:

- **Small SUD outpatient / IOP / sober-living (1–3 sites):** the **owner-operator is the buyer, user, and check-signer in one person.** No committee. This is the single most important fact for a first logo. Owners "juggle patient care, administrative duties, billing, compliance" themselves and only later consider hiring a clinic director ([BreezyBilling](https://www.breezybilling.net/blog/finding-behavioral-health-locations-j3lbr)). Decision is fast and emotional/ROI-driven.
- **Mid-size (multi-site, 50+ beds):** the **clinical director** becomes the functional buyer/champion — they "manage personnel, workflows, budgets, compliance, and strategic planning" and must be "adept at the software used for patient care, billing, performance" ([CareRev](https://www.carerev.com/blog/what-is-the-role-of-a-clinical-director); [APOS](https://careers.apos-society.org/career/behavioral-health-director)). But the owner/CEO still controls budget sign-off.
- **The hidden economic buyer at any size: whoever owns the money leak.** For a clinical EHR/RCM purchase, that is the **billing/RCM manager or CFO**, because behavioral-health orgs "lose up to 20–30% of earned revenue to preventable billing errors" ([PIMSY](https://pimsyehr.com/addiction-treatment-revenue-cycle-management/)). RCM pain is the loudest budget-unlocking pain in the category.

> Devil's advocate for the portfolio: **regroup and homegroups are NOT clinical-EHR purchases** — they're operations/peer-support tools. That means they do NOT get to ride the RCM-pain budget. They compete for discretionary operational spend, which is a thinner, more skeptical wallet. The buyer you can actually reach cheaply (the sober-living owner-operator) is also the one with the least money. Hold that tension.

### 2. Willingness-to-pay benchmarks (verified)

**Clinical behavioral-health EHR (per-user/month):**
- Small/mid-market: **$35–200/user/mo**; enterprise **$200–500+/user/mo** ([ICANotes EHR cost guide](https://www.icanotes.com/2025/06/18/mental-health-ehr-costs/)).
- ICANotes: **$35 notes-only → $55 → $75 non-prescribing → $213 prescribing** ([ICANotes](https://www.icanotes.com/2025/06/18/mental-health-ehr-costs/)).
- CharmHealth: **$0.50/encounter ($25/mo min)** or **$200/provider/mo** ([same source]).
- Implementation fees: **~$5k (small) to $100k+ (enterprise)** — a real switching-cost moat for incumbents ([ICANotes](https://www.icanotes.com/2025/06/18/mental-health-ehr-costs/)).

**Sober-living / recovery-residence software (the regroup comp set):**
- **Sobriety Hub: $65/mo flat, priced by team size, NOT per-bed or per-resident** — the only one with public pricing ([Sober Living App comparison](https://soberlivingapp.com/blog/sober-living-software-comparison); [SobrietyHub buyer's guide](https://www.sobrietyhub.com/our-blog/2026-buyers-guide-the-big-3-of-sober-living-software)).
- **Behave Health: quote-only, no public price**, bundles CRM+EHR+RCM ([Behave Health recovery residences](https://behavehealth.com/recovery-residences)).
- **KIPU: "over-engineered and overpriced" for non-clinical sober-living operators** — i.e., the incumbent enterprise EHR is a bad fit for the low end, which is the gap regroup targets ([Behave Health Kipu comparison](https://behavehealth.com/blog/kipu-versus-behave-health-which-emr-is-best-for-behavioral-health)).

> Hard read on regroup pricing: your recommended Option-2 ($69/$129/$249 traditional; $49/$89/$299 Oxford) sits **roughly at or above** the only transparent competitor in the space (Sobriety Hub at $65 flat). The market signal is that sober-living operators expect **flat, sub-$100, not-per-bed** pricing. Per-bed framing will trigger sticker-shock anchoring against the $65 flat benchmark. Sobriety Hub explicitly markets "you pay the same regardless of beds" as a selling point — meaning **per-bed is a known objection the competition already weaponizes against you.** [VERIFY whether your $249/$299 top tiers can be justified by GPS verification + Stripe rent rails as distinct value, because on price alone they're exposed.]

### 3. Sales cycle & switching cost

- **SMB SaaS under ~$15k ACV closes in 14–30 days** ([Optifai](https://optif.ai/learn/questions/sales-cycle-length-benchmark/); [Growthspree](https://www.growthspreeofficial.com/blogs/b2b-saas-sales-cycle-length-benchmarks-2026-by-acv-vertical)). A $49–299/mo sober-living tool is firmly in this bucket → **days-to-weeks if you reach the owner directly.**
- Broader B2B SaaS median is **84 days (mean 134)**, and cycles **lengthened 22% since 2022** from budget scrutiny and committee buying ([Ziellab](https://ziellab.com/post/b2b-sales-cycle-length-shorten-2026-guide); [Cleanlist](https://www.cleanlist.ai/glossary/b2b-sales)). That penalty hits the moment you sell to a multi-site org with a committee — another reason to start at the owner-operator end.
- **Security questionnaires / SOC 2 / vendor risk now add 2–4 weeks even at mid-market** ([Cleanlist](https://www.cleanlist.ai/glossary/b2b-sales)). For homegroups' treatment-center "Institutional" tier this is worse: PHI + 42 CFR Part 2 means a **BAA + security review is mandatory**, pushing that motion toward the 84+ day median, not the 14–30 day SMB lane.
- **Switching cost off an installed clinical EHR is high:** $5k–100k+ re-implementation plus data migration plus staff retraining ([ICANotes](https://www.icanotes.com/2025/06/18/mental-health-ehr-costs/)). Translation: **do not try to rip-and-replace an EHR.** Sell into the gap the EHR doesn't cover (sober-living ops, peer support, rent collection) where there is no incumbent to switch from. regroup's "no direct competitor / over-engineered KIPU" framing is the *right* wedge precisely because it avoids switching cost.

### 4. Buying triggers (ranked by budget-unlock power)

1. **Denial losses / RCM bleed — strongest.** 20–30% revenue lost to billing errors; **65% of denied SUD claims are never reworked, but 54.3% of appeals get overturned** ([PIMSY](https://pimsyehr.com/addiction-treatment-revenue-cycle-management/); [Simitree](https://simitreehc.com/simitree-blog/most-important-kpis-for-substance-abuse-rcm/)). Money-back-today is the easiest budget to unlock — but it's a clinical/RCM sale, not regroup's lane.
2. **Compliance deadlines (hard dates = forced buying).**
   - **42 CFR Part 2 final rule compliance deadline: Feb 16, 2026** (now passed — late/unprepared centers are in remediation mode) ([OmniMD](https://omnimd.com/blog/hipaa-42-cfr-part2-compliance-behavioral-ehr/)).
   - **CARF: as of Jan 1, 2026, accreditation requires documented outcome-data collection procedures** ([BestNotes](https://www.bestnotes.com/carf-compliant-addiction-treatment-ehr-features-essential-checklist/)). Accreditation cycles are recurring forced-buying events.
3. **Census pressure** — empty beds = no revenue; anything that fills beds or proves outcomes (for referral relationships) is a live trigger. This is where homegroups' referral-flywheel pitch has legs, but it collides with EKRA.
4. **Joint Commission / CARF accreditation prep** generally — pre-built compliant templates and audit trails are explicit purchase criteria ([Behave Health Joint Commission](https://behavehealth.com/compliance/joint-commission); [Adentris](https://blog.adentris.com/maximize-compliance-with-behavioral-health-carf-documentation-software/)).

> Note for regroup/homegroups: 42 CFR Part 2 and CARF outcome-data are triggers that pull buyers toward **clinical EHRs**, not operations/peer apps. Don't claim a trigger your product can't actually relieve — a sober-living operator does not buy software to pass CARF; the licensed treatment center does.

### 5. Lowest-friction wedge + the offer most likely to land a first logo

**Wedge segment: single-site / small sober-living & recovery-residence operators (incl. Oxford House affiliates).** Rationale, all evidence-backed:
- **One buyer (owner-operator), no committee, no security-review gauntlet** → 14–30 day cycle ([Optifai](https://optif.ai/learn/questions/sales-cycle-length-benchmark/)).
- **No incumbent to switch off** — KIPU is overbuilt/overpriced here, enterprise EHRs ignore the segment → near-zero switching cost ([Behave Health](https://behavehealth.com/blog/kipu-versus-behave-health-which-emr-is-best-for-behavioral-health)).
- **Operator pays, not resident** (matches regroup's model) and **avoids the clinical scope-of-practice and EKRA/Part-2 minefield** that threatens detox-recovery and homegroups.
- Founder fit: brother's SWLA network + lived recovery credibility lets you reach these owners warmly, collapsing CAC — and there's no CAC/LTV in your docs, so a warm-intro motion is how you *avoid* needing one.

**The offer: a flat-priced, per-house (not per-bed) "operations + rent rail" bundle, sold as a money-and-time guarantee, not a feature list.**
- **Price at or just under the transparent benchmark to neutralize the objection: a single flat tier ≈ $59–79/house/mo** (anchors to Sobriety Hub's $65 flat) ([SobrietyHub](https://www.sobrietyhub.com/our-blog/2026-buyers-guide-the-big-3-of-sober-living-software)). Reserve per-bed/usage upside for the **Stripe rent-processing stream**, which is value-aligned (you get paid more only when they collect more) and doesn't trip the per-bed sticker-shock.
- **Lead with the two pains the owner feels weekly:** (a) chasing resident rent → "rent collected automatically via Stripe, you stop being a bill collector"; (b) bed-fill/compliance documentation for referral relationships → GPS meeting-attendance verification as the differentiated hook (your moat claim).
- **First-logo close mechanic:** free white-glove migration + first 60–90 days free for one or two design-partner houses in the brother's network, in exchange for a public reference and a testimonial. This converts the high-switching-cost dynamic in your favor (you eat the migration cost at the low end where it's cheap) and produces the reference asset that shortens every subsequent SMB cycle.

**One-line verdict:** Sell to the **sober-living owner-operator** (fast, single-threaded, no incumbent), **price flat and per-house near $65** to defuse the per-bed objection the competition already exploits, monetize upside through **Stripe rent rails**, and use **free migration for a network design-partner** to land logo #1 in weeks — *not* months. Keep the 42 CFR Part 2 / CARF / RCM triggers reserved for the clinical-EHR-adjacent products, because the operations wedge cannot honestly claim them.

**Gaps to close ([VERIFY]):** exact KIPU and Behave Health per-bed/per-house quotes (both quote-gated); whether GPS verification + 300K-meeting dataset are defensible enough to justify your $249/$299 top tiers above the $65 flat benchmark; and category-specific CAC/LTV, which no public source provides and which only your design-partner motion will reveal.

---

## 2. EKRA-Safe Recovery-App → Treatment-Center Bridge

I have enough primary and secondary sourcing to write a rigorous, defensible answer. I'll synthesize now rather than spend more.

---

# EKRA-Safe Recovery-App → Treatment-Center Bridge: Legal Architecture

> **Scope note.** This is a research synthesis for venture planning, not legal advice. It identifies the structure most likely to survive scrutiny and flags exactly where a licensed healthcare attorney must sign off before launch. **See the bolded ATTORNEY GATE at the end — do not launch the paid bridge without it.**

## 1. What the statute actually prohibits (the trap)

EKRA, 18 U.S.C. § 220(a), makes it a federal crime to **knowingly and willfully** (1) *solicit or receive* remuneration "in return for referring a patient or patronage to" a recovery home, clinical treatment facility, or laboratory, or (2) *pay or offer* remuneration "**to induce a referral**" or "**in exchange for an individual using the services**" of such a facility. Penalty: **up to $200,000 and 10 years per occurrence** ([18 U.S.C. § 220, Cornell LII](https://www.law.cornell.edu/uscode/text/18/220)).

Three definitional facts that bear directly on this portfolio ([§ 220(e)](https://www.law.cornell.edu/uscode/text/18/220)):

- **"Clinical treatment facility"** = a non-hospital medical setting providing detox / outpatient / residential treatment for SUD, *pursuant to licensure or certification under State law.* This is the treatment center you want to connect to.
- **"Recovery home"** = "a shared living environment that is, or purports to be, free from alcohol and illicit drug use and centered on peer support." **This squarely captures the sober-living / Oxford houses that `regroup` serves.** EKRA therefore reaches `regroup`'s customers directly, not just treatment centers.
- EKRA is **all-payor** (any "health care benefit program," public or private) and **does not preempt state law** (§ 220(d)(2)); state patient-brokering statutes stack on top — e.g., New Jersey's Aug-2025 amendment now criminalizes referral payments to labs/facilities independent of EKRA ([Mintz, Jan 2026](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments)). Louisiana has its own patient-brokering exposure to check [VERIFY: LA-specific statute not researched here].

**The core danger for all three apps:** any arrangement where money flows *as a function of bodies, admissions, or claims billed* between an app and a treatment center is presumptively a referral kickback. The famous trap is "marketing fee per lead," "per warm intro," or revenue-share on admitted patients.

## 2. EKRA-SAFE vs UNSAFE monetization (decision table)

| Model | EKRA status | Why |
|---|---|---|
| **Flat-fee SaaS license** the center pays (per-seat or per-facility, fixed, set in advance, FMV) | **SAFE** | Payment is for *software*, not for patients. It does not vary by referrals, tests, or amounts billed — the exact condition § 220(b)(2) requires for the employee/contractor exception, and the structural logic courts apply. |
| **Bill families / individuals direct** (consumer pays for the app or coaching) | **SAFE** | No facility is paying anyone "to induce a referral." This is `detox-recovery`'s $50/$150/$450 consumer pricing — pure D2C. |
| **Grant-funded / SAMHSA / state-block-grant** seats | **SAFE** | Payor is a grantor, not a referral-interested facility. |
| **Per-engagement B2B consulting** at fixed FMV scope (the $4k/$1.5k–$7.5k `detox-recovery` engagements) | **SAFE if structured as a personal-services/management contract** meeting 42 CFR § 1001.952(d) — which EKRA *expressly* imports as an exception at § 220(b)(4) ([statute](https://www.law.cornell.edu/uscode/text/18/220)). Aggregate compensation fixed in advance, FMV, not volume-based. | Compensation for *defined deliverables*, not bodies. |
| **Per-referral / per-admission / per-"warm lead" fee** | **UNSAFE — felony core** | This *is* the §220(a) offense. |
| **Revenue-share / % of resident rent or % of center revenue tied to placements** | **UNSAFE** | Varies by "amount billed/received" and by individuals using the service — fails §220(b)(2)(A)–(C). Note: `regroup`'s Stripe-on-rent stream is fine *as a processing fee on the operator's own residents*; it becomes radioactive the instant it is framed as compensation for placing a discharged patient into that home. |
| **"Marketing" fee from a center that scales with how many alumni the app drives back** | **UNSAFE** | Classic patient brokering. |
| **Tiered SaaS where the tier price is secretly calibrated to referral volume** | **UNSAFE (sham)** | Form over substance fails; DOJ/courts look at whether the "license fee" is a disguised per-head payment. |

**Critical nuance from current case law (do not over-rely on it).** The Ninth Circuit in *United States v. Schena* (July 2025) held that percentage-based marketing compensation is **not a *per se* EKRA violation** absent "wrongful inducement" (fraud/undue influence on referral decisions); DOJ appeared to concede this at oral argument ([Mintz, Jan 2026](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments)). **This is thin ice, not a green light:** (a) it is one circuit, Schena's conviction was still *affirmed*, and a cert petition is pending ([same source](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments)); (b) DOJ has issued **no regulations** clarifying the exceptions despite years of industry requests ([Mintz](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments)); (c) EKRA has **far fewer safe harbors than the AKS** and no broad employee-comp shield ([Oberheiden P.C., "5 Things You Must Know About EKRA in 2026"](https://federal-lawyer.com/5-things-you-must-know-about-ekra/); [Maynard Nexsen](https://www.maynardnexsen.com/publication-New-All-Payor-Anti-Kickback-Law-in-Opioid-Bill-Impacts-Clinical-Laboratories) noting the EKRA employee exception applies *only if* pay doesn't vary by referrals/tests/billings). **Architect to the flat-fee rule, not to the Schena loophole.** The loophole is a litigation defense; the flat fee is a business model.

## 3. The Post-Discharge Continuity Package (the defensible design)

**Product framing:** Sell the treatment center a **continuity-of-care software suite** it *operates itself*, for a **fixed annual/monthly license fee set in advance at fair market value** — not a fee that moves with any patient.

- **`homegroups` (alumni / aftercare tracking)** → licensed to the center as its *own* alumni-engagement and outcomes-tracking tool. The center's staff use it to follow their discharged patients' meeting attendance and recovery milestones. The center pays the Institutional tier ($150–$500/mo per the portfolio) **as a flat software subscription**, decoupled from how many alumni enroll or whether any return.
- **`regroup` (sober-living placement / management)** → licensed to (a) the sober-living *operators* (who already pay per the recommended $49–$299 tiers — the operator-pays-not-resident model is itself EKRA-aligned because the payor isn't buying referrals) and (b) optionally to the treatment center as a *discharge-planning* tool its case managers use to see bed availability. The center pays a **flat license**, never a placement bounty.
- **`detop-recovery` / Next Step Recovery (peer navigation)** → stays **D2C (families pay) or fixed-scope B2B consulting** to the center under a § 1001.952(d)-compliant personal-services contract. Peer navigators are paid **salary, not per-placement.**

**Why this is defensible, stated precisely:**

1. The treatment center is buying **a tool, not a patient pipeline.** The fee is fixed in advance, does not vary by the number of individuals referred, tests performed, or amounts billed — directly tracking the §220(b)(2) condition and the §220(b)(4) personal-services exception ([18 U.S.C. § 220](https://www.law.cornell.edu/uscode/text/18/220)).
2. **The software is bidirectional/neutral.** `homegroups`/`regroup` do not steer a discharged patient *to* the paying center; they track and place patients into independent sober-living and meetings. The app must not preferentially route patients *toward* facilities that pay you — that directionality is what converts a tool into a brokering scheme.
3. **No money flows in the referral direction.** The center pays you for software; you pay the center nothing; you receive nothing per-patient. There is no remuneration "to induce a referral" or "in exchange for an individual using the services."

**Guardrails that keep it defensible (these are load-bearing, not optional):**
- License fee **fixed in a written contract, set before any patient volume is known, documented as FMV** (get a valuation memo). Re-pricing tiers must track *software value* (seats, features, support), never patient counts.
- **No "preferred provider" placement logic** in `regroup`/`homegroups` that favors paying centers. If a center pays for placement priority, that is a per-referral inducement.
- **No payment from the app to peer navigators, sober-living operators, or anyone that varies with placements.** Salary or fixed contract only.
- **No reciprocal money loop** (center pays SaaS *and* app sends patients *and* app gets anything back tied to volume).
- Keep `detox-recovery`'s existing **non-clinical scope-of-practice** firewall intact — that's a separate existential risk flagged in the portfolio, and blurring into "treatment" would also pull it into EKRA's "clinical treatment facility" definitional orbit.

## 4. 42 CFR Part 2 + HIPAA data/consent architecture

Any record that identifies someone as an SUD patient — which is the *entire dataset* these apps touch — is protected under 42 CFR Part 2 (42 U.S.C. 290dd-2). **The compliance deadline for the 2024 Final Rule is February 16, 2026** ([HHS Fact Sheet, updated Jan 30, 2026](https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html); [Snell & Wilmer](https://www.swlaw.com/publication/42-cfr-part-2-and-privacy-rule-compliance-action-required-by-february-16-2026/)) — i.e., **already in effect as of this writing (June 2026)**. Build to the *new* rule, not the old one.

**What the Final Rule changed and how to use it ([HHS Fact Sheet](https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html)):**
- **Single consent for all future TPO** (treatment, payment, health care operations). One properly drafted patient consent can authorize ongoing record-sharing across the continuity package — you no longer need a fresh consent per disclosure.
- **Redisclosure**: A HIPAA covered entity / business associate receiving Part 2 records under that consent may **redisclose per HIPAA rules** — but **never for legal proceedings against the patient** without specific consent or court order (more stringent than HIPAA).
- **Breach notification now mirrors the HIPAA Breach Notification Rule** — Part 2 breaches trigger the same notification obligations. Penalties are now aligned with HIPAA civil/criminal enforcement (criminal Part 2 penalties replaced).
- **SUD counseling notes** require a **separate, specific consent** and cannot ride the broad TPO consent (analogous to psychotherapy notes). If any app stores navigator/counseling session notes, wall them off behind separate consent.
- **Segregation of Part 2 data is *not* required** — you may commingle, but then the whole store inherits Part 2 protections, so design accordingly.

**Concrete data architecture:**
1. **Determine each app's role.** If a treatment center (a Part 2 program / covered entity) uses `homegroups`/`regroup` to handle patient records on its behalf, **your company is a Business Associate** → a **BAA is mandatory** with each center, and Part 2's Final Rule now binds business associates that receive records under the single consent.
2. **Sign a BAA with every treatment-center and operator customer** before any PHI/Part 2 data flows. Mirror Part 2 obligations into the BAA explicitly (the BAA must carry forward the redisclosure and proceedings-use restrictions, not just generic HIPAA terms).
3. **Single TPO consent at intake** — patient-signed, app-presented, authorizing the named continuity-of-care participants. Each disclosure must include a copy of the consent or a clear explanation of its scope (new Final Rule requirement).
4. **Separate consent toggle** for SUD counseling notes and an explicit **opt-out for fundraising** (both new rights).
5. **Patient rights plumbing**: accounting-of-disclosures log, restriction-request handling, complaint pathway to HHS — build these as features, not afterthoughts.
6. **Breach response runbook** aligned to HIPAA Breach Notification timelines, covering all three apps' shared/commingled stores.
7. **Encryption, access controls, audit logging, de-identification pipeline** (Part 2 permits unconsented public-health disclosure only of HIPAA-de-identified data — relevant if `regroup` ever monetizes its meeting/outcomes dataset; de-identify to HIPAA standard first).
8. **Crucial intersection with EKRA:** the consent/data plumbing must **not** double as a covert referral-tracking-and-billing mechanism. If your "consent + outcomes dashboard" is secretly the instrument by which a center pays you per converted patient, the data layer becomes evidence of an EKRA scheme. Keep data flows (clinical continuity) and money flows (flat SaaS) architecturally and contractually separate.

## 5. Sequencing implication for the portfolio

This bridge **does not change the v1 rank order** — the CPA advisory line remains the income engine and the safe first dollar; the recovery bridge is later-sequence, higher-regulatory-load. The continuity package is only safe to *sell to centers* once (a) flat-fee contracts + FMV memo, (b) BAAs, and (c) Part 2-compliant consent are all in place. Until then, run `detox-recovery` D2C and `regroup` operator-pays, which carry the lowest EKRA exposure.

---

## ⚖️ ATTORNEY GATE — REQUIRED BEFORE LAUNCH

**Do not collect a single dollar from a treatment center, and do not move Part 2 data between any two parties, until a licensed healthcare-regulatory attorney (EKRA + AKS + 42 CFR Part 2 + Louisiana patient-brokering competent) has, in writing:**
1. Reviewed and blessed the **flat-fee SaaS license agreement** and confirmed FMV documentation.
2. Confirmed the **personal-services/management contract** for any B2B consulting meets 42 CFR § 1001.952(d).
3. Drafted/approved the **single TPO consent**, the **separate counseling-notes consent**, and **BAA** templates.
4. Vetted that no app's placement/routing logic preferentially steers patients to paying facilities.
5. Checked **Louisiana** (and any other operating state's) patient-brokering and licensing statutes, which stack on top of EKRA and are *not* preempted (§ 220(d)(2)). [VERIFY: LA-specific statute and any LA SUD-facility licensing rules — not researched in this pass.]

The cost of this sign-off is trivial next to **$200,000 + 10 years per occurrence** under § 220.

---

### Sources
- **18 U.S.C. § 220 (statute text, exceptions, definitions, penalties)** — https://www.law.cornell.edu/uscode/text/18/220 ; official: https://uscode.house.gov/view.xhtml?req=(title:18%20section:220%20edition:prelim)
- **Mintz, "The Eliminating Kickbacks in Recovery Act in 2025: New Developments" (Jan 20, 2026)** — *Schena*, DOJ silence on regs, NJ patient-brokering expansion — https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments
- **Oberheiden P.C., "5 Things You Must Know About EKRA Law in 2026"** — EKRA has fewer/no broad safe harbors vs AKS — https://federal-lawyer.com/5-things-you-must-know-about-ekra/
- **Maynard Nexsen** — EKRA employee/contractor exception applies only if pay doesn't vary by referrals/tests/billings — https://www.maynardnexsen.com/publication-New-All-Payor-Anti-Kickback-Law-in-Opioid-Bill-Impacts-Clinical-Laboratories
- **Troutman Pepper** — enumerates EKRA safe harbors (disclosed discounts, bona fide employee, §1001.952(d) personal services) — https://www.troutman.com/insights/eliminating-kickbacks-in-recovery-act-what-in-office-laboratories-need-to-know/
- **HHS/SAMHSA/OCR Fact Sheet, 42 CFR Part 2 Final Rule (Feb 8, 2024; updated Jan 30, 2026)** — single TPO consent, HIPAA-aligned breach notification, penalties, counseling-notes carve-out, **Feb 16, 2026 compliance date** — https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/fact-sheet-42-cfr-part-2-final-rule/index.html
- **42 CFR Part 2 Final Rule (Federal Register, Feb 16, 2024)** — https://www.federalregister.gov/documents/2024/02/16/2024-02544/confidentiality-of-substance-use-disorder-sud-patient-records
- **Snell & Wilmer, "42 CFR Part 2 and Privacy Rule Compliance: Action Required by February 16, 2026"** — https://www.swlaw.com/publication/42-cfr-part-2-and-privacy-rule-compliance-action-required-by-february-16-2026/

[VERIFY] items: Louisiana patient-brokering statute and LA SUD-facility licensing; cert outcome of *Schena* (pending as of Jan 2026 Mintz article).

---

## 3. Monetization / GTM Stress-Test (three ventures)

I have all the benchmarks needed. Here is the deliverable.

---

## Monetization / GTM Stress-Test (External Benchmark Reconciliation)

Devil's-advocate read of the three ventures against published competitor pricing and industry funnel/SaaS norms. Every doc projection is labeled **confirmed** (benchmark supports it), **optimistic** (achievable but above median), or **unsupported** (no external evidence / contradicted).

### 1. regroup (RATS) — sober-living / Oxford House SaaS

#### a) Pricing vs. the real market

The single most important finding is that the brief's stated Sobriety Hub model is **wrong/stale**, and the correction makes regroup's pricing look *high*, not competitive.

| Item | regroup doc (Option 2) | Sobriety Hub (actual, verified) | Read |
|---|---|---|---|
| Per-staff seat | $69 / $129 / $249 per **month** (traditional tiers) | $65/mo per **Full User** (annual); $20/mo per Client Manager (annual) | Sobriety Hub charges **per seat**, regroup tiers read as **per-account/house**. Different axis — see below. |
| Oxford tier | $49 / $89 / $299 | (no Oxford-specific tier exists at Sobriety Hub) | regroup's Oxford segmentation is a genuine differentiator, but unproven WTP. |
| Onboarding | not specified in brief | **$250 one-time** | regroup leaves a recurring revenue/setup-fee lever on the table. |
| Per-bed/house surcharge | none | **none** ("You pay only for staff users, not per resident or per house") | Flat-rate is the market-validated model. |
| Card processing passed to resident | brief assumes regroup captures spread | **3.9% card / 1.2% ACH, rolled onto the resident by default** | Critical — see (c). |

Sources: Sobriety Hub FAQ confirms "$780 per Full User per year ($65/month) and $240 per Client Manager per year ($20/month)… one-time $250 Onboarding Fee… 3.9% per credit card and 1.2% for ACH… By default, Sobriety Hub rolls the processing fee onto the resident" (https://www.sobrietyhub.com/faqs). Behave Health's own comparison confirms Sobriety Hub is the *only* one of the "big 3" that publishes price, at "$65 to $75 per month… regardless of how many houses you operate" (https://soberlivingapp.com/blog/sober-living-software-comparison). Behave Health and OneStep are **quote-only / custom-priced** — meaning the market's two larger players hide price, and the only transparent competitor is at the low end.

**Verdict on WTP realism: regroup's pricing is OPTIMISTIC-to-aggressive.** The market reference point an operator will Google is "$65/mo flat, all houses" (Sobriety Hub). regroup's mid-tier $129 and Oxford $299 sit 2–4.5x above that *visible* anchor. That can be defended only if regroup's moat features (GPS meeting verification, the 300K-meeting dataset, Oxford House World Services partnership) are legible to a buyer at the point of sale — but a sober-living operator or Oxford House treasurer is one of the most price-sensitive SMB buyers in existence (often a volunteer-run nonprofit house). The "no direct competitor" moat claim in the brief is **contradicted by the evidence**: Sobriety Hub (1,000+ homes per its FAQ), Behave Health/Sober Living App (2,000+ operators per their site), and OneStep are all direct competitors with overlapping feature matrices including drug-test tracking, bed boards, rent collection, and outcome reporting. Treat "no direct competitor" as **unsupported**.

One real edge regroup has: incumbents explicitly **do not integrate** (Sobriety Hub: "does not currently offer direct integrations… standalone solution"). Integration + the Oxford-specific workflow is the defensible wedge, not price.

#### b) Reconciling the $315k vs $204k Year-1 ARR discrepancy

The discrepancy is almost certainly a **house-count vs. tier-mix** modeling difference, and the math only closes under optimistic assumptions either way. Working it backward against the *flat-per-account* model the market actually uses:

- If tiers are **per house/account per month**, blended ARPA matters. Take a blended ~$110/mo (mix of $69/$129/$249 traditional + $49/$89 Oxford):
 - **$204k / $110 / 12 ≈ 155 paying houses** by year-end.
 - **$315k / $110 / 12 ≈ 239 paying houses.**
- The 111k gap ≈ **~84 houses**, i.e. one document assumes ~50% more logos, OR assumes a richer tier mix (more $249/$299 accounts), OR the $315k "detail" figure includes **Stripe processing revenue** while the $204k "summary" is subscription-only. That last interpretation is the most likely source of the inconsistency and is the one to verify in the source docs.

**Reality check on logo count:** acquiring 155–239 paying recovery houses in Year 1, cold, against three incumbents, with no CAC budget defined, is **unsupported** by any benchmark. For context on difficulty: Sobriety Hub took years to reach 1,000+ homes. A realistic Y1 for a solo/founder-led GTM into a niche vertical is **low tens of logos**, not 150–240. Both ARR figures should be treated as **optimistic at best; the $315k figure as unsupported** until the house-acquisition assumption is shown.

#### c) Stripe rent-processing as a second stream — how much is *actually* capturable

This is the weakest monetization assumption in the portfolio. Plain card economics: Stripe's standard rate is **2.9% + $0.30** per transaction. To earn a spread, regroup must charge the payer *more* than its own processor cost and pocket the difference (the "payfac/surcharge" model). Three problems:

1. **Thin-to-negative spread.** The incumbent already passes **3.9% card / 1.2% ACH** to the *resident* and keeps ~0 as profit — Sobriety Hub explicitly frames it as "no net cost to accept electronic payments," not a profit center (https://www.sobrietyhub.com/faqs). If regroup tries to keep, say, 1% on top of Stripe's 2.9%, the all-in card cost to the resident hits ~4%+, above the visible competitor. On ACH the spread is even thinner — Stripe ACH is ~0.8% (capped), leaving almost nothing to capture against a 1.2% retail rate.
2. **Legality/normalcy of surcharging rent is jurisdiction-specific and tightening.** Credit-card *surcharges* are outright restricted in several states and the rules are actively changing — e.g., California historically **prohibited surcharges** (Civil Code 1748.1, per https://oag.ca.gov/consumers/general/credit-card-surcharges) and only in 2025 did **SB 611 specifically authorize a "convenience fee" for rent** (https://www.riversideevictions.com/new-laws-2025/...). Massachusetts prohibits convenience fees on card purchases (consumer reports, r/Renters). So "charge a markup on rent payments" is **not uniformly legal** and is a per-state compliance burden — a real risk, not a clean revenue line. Card-brand rules also forbid surcharging on *debit* entirely.
3. **What's actually capturable:** realistically near-zero net margin if regroup wants to stay at/below the incumbent's resident-facing rate. The only legitimate version of this stream is **interchange-plus markup as a registered payfac** (think Stripe Connect platform fee, e.g. +0.25–0.5%), which requires underwriting, KYC, and dispute liability that a pre-revenue solo venture should not take on in Year 1.

**Verdict:** Stripe rent processing as a *profit* stream is **unsupported / optimistic**. Model it as a **pass-through convenience (retention feature), not net revenue**, in Year 1–2. Any contribution to the $315k figure from processing should be stripped out — which conveniently also explains the $315k-vs-$204k gap.

---

### 2. Next Step Recovery — organic-only solo funnel

| Funnel stage | Doc assumption | External benchmark | Label |
|---|---|---|---|
| Lead-magnet opt-in | **4%** | Industry average **~8.66%**; "most lead magnets get 10–20% if crushing it" (https://focus-digital.co/lead-magnet-conversion-rate-by-industry/; LinkedIn/dbusta) | **Confirmed / conservative.** 4% is *below* average — good, it's defensible. The catch: 4% of *organic* traffic, and organic traffic volume is the unmodeled bottleneck. |
| Fit-call → paid | **35%** | Sales-call close averages **13–25%** by industry (https://focus-digital.co/average-sales-call-conversion-rate-by-industry/); coaching specifically "**average coaches close 1 in 6–7 calls**" (~14–17%), top performers 1 in 3–4 (~25–33%) (LinkedIn/Daniel Botero, 200+ tracked calls) | **OPTIMISTIC.** 35% close on a *qualified fit-call* is at/above the top-performer band. Plausible for a warm, pre-qualified, founder-with-lived-experience pitch — but it is a best-case, not a base-case. Base case is ~15–20%. |

**The structural problem is volume, not conversion rates.** The funnel is mathematically fine; the input — *organic* traffic with **no paid acquisition and no CAC line** — is the unvalidated assumption. Lead-to-*sale* end-to-end conversion industry-wide runs **<1% (≈0.81%)** from the same source. At 0.81% lead→customer, hitting meaningful revenue requires large top-of-funnel volume that organic-only, solo, rarely produces in 12 months.

**Is Y3 ~$139k plausible solo? CONDITIONALLY YES, but optimistic.** $139k from a blend of $50–$450 calls, $9.99–19.99 PDFs, and $1.5–7.5k B2B engagements is achievable for an established solo coach by Year 3 — but it **leans on the B2B consulting line (4 figures/engagement, $1.5k/mo retainers), not the organic coaching funnel.** The coaching-call funnel alone, at realistic 15–20% close and organic volume, supports a fraction of that. So: Y1 ~$18k **confirmed/plausible**; Y3 ~$139k **optimistic and B2B-dependent** — and the existential scope-of-practice risk (non-clinical framing) is the real ceiling, not the funnel math.

---

### 3. General — CAC/LTV & sales-cycle for SMB behavioral-health SaaS (the gap both docs leave blank)

Use these to backfill regroup's missing unit economics:

- **SMB SaaS CAC:** median **$200–$500 per customer** (https://ltvcacbook.com/blog/cac-benchmarks-2026). Self-serve/PLG can be lower; sales-assisted higher.
- **LTV:CAC target:** **3:1 minimum**, top quartile **4:1–6:1**; cross-segment median **~3.2:1** (https://www.saashero.net/strategy/saas-cac-benchmarks-2026/; https://optif.ai/learn/questions/b2b-saas-ltv-benchmark/; https://www.saasmag.com/saas-capital-efficiency-metrics/). A ratio **below 3:1 signals broken unit economics.**
- **SMB SaaS LTV:** **$15k–$40k** per customer for healthy SMB B2B (Optifai, 939 companies). regroup at ~$110/mo blended ARPA implies, at a generous 30-month retention, **~$3.3k LTV** — *well below* the $15k SMB benchmark. That means regroup must keep CAC **under ~$1,100** to hit even 3:1, i.e. it cannot afford a real outbound sales motion at current price. **This is the binding constraint the docs omit.**
- **Sales cycle:** SMB SaaS typically **2–4 weeks** self-serve to **~1–2 months** sales-assisted; the relevant proxy here is onboarding/switching friction — Behave Health quotes **4–6 weeks** single-facility migration, 8–12 weeks multi-facility (https://soberlivingapp.com/blog/sober-living-software-comparison). Switching cost is high, which **helps retention but lengthens the sell** and slows the Y1 logo ramp that the $204k/$315k figures depend on.

**Implication for regroup:** with ~$3.3k LTV against a market that wants 3:1, the viable motions are **low-CAC channels only** — the Oxford House World Services partnership (channel/embedded distribution) and Marcus's brother's network, *not* paid acquisition or a sales team. The entire Y1 ARR thesis lives or dies on that one partnership converting to actual installs. Raise ARPA (add the $250 onboarding fee the market already accepts; push the $249/$299 tiers) to improve LTV before scaling spend.

---

### Bottom line (labels)

- **regroup pricing:** OPTIMISTIC — sits 2–4.5x above the only transparent competitor anchor ($65/mo flat). "No direct competitor" = **unsupported** (3 named incumbents). 
- **regroup $315k vs $204k:** the gap ≈ 84 houses or, more likely, **Stripe revenue baked into the $315k**. Both **optimistic**; **$315k unsupported** without a defended logo-count.
- **regroup Stripe spread:** **unsupported as profit** — incumbent runs it at ~zero net, surcharging rent is state-restricted; model as pass-through retention feature.
- **Next Step 4% opt-in:** **confirmed/conservative** (vs ~8.66% avg). **35% fit-call close:** **optimistic** (vs 13–25% industry / ~15% avg coach). **Y3 $139k:** **optimistic & B2B-dependent**, funnel volume (not rate) is the risk.
- **Missing unit economics:** regroup's ~$3.3k implied LTV vs $15k SMB benchmark forces CAC <~$1.1k and **mandates partnership-led, not paid, GTM** — the single most important number absent from the docs.

**Key sources:** Sobriety Hub FAQ (https://www.sobrietyhub.com/faqs); Behave Health "Sober Living Software Comparison 2026" (https://soberlivingapp.com/blog/sober-living-software-comparison); Focus Digital lead-magnet & sales-call benchmarks (https://focus-digital.co/lead-magnet-conversion-rate-by-industry/, /average-sales-call-conversion-rate-by-industry/); Daniel Botero coaching close-rate data (LinkedIn); CAC/LTV (ltvcacbook.com/blog/cac-benchmarks-2026, saashero.net, optif.ai, saasmag.com); CA surcharge law (oag.ca.gov/consumers/general/credit-card-surcharges; riversideevictions.com SB 611). [VERIFY] regroup's own source docs to confirm whether $315k includes Stripe revenue — that is the fastest way to close the ARR discrepancy.

---

## 4. SWLA / Lake Charles Economy + Brother's Network

I have comprehensive data across all dimensions. Here is the deliverable.

---

# SWLA / Lake Charles Economy + Brother's Network as an AI/Automation/Consulting Channel

## 1. The SWLA economic base — concentrated, capital-heavy, tech-thin

Southwest Louisiana (the 5-parish region: Calcasieu, Cameron, Allen, Beauregard, Jeff Davis) is one of the most capital-intensive economies in the U.S. per capita, anchored by LNG/petrochemical export infrastructure, with healthcare, gaming/hospitality, port/logistics, and construction as the secondary pillars.

**Energy / petrochemical (the apex tier — mostly NOT the target buyer, but the demand driver):**
- The region is in the middle of a historic capex wave. Woodside's **Louisiana LNG** (formerly Driftwood) reached a **$17.5B final investment decision in April 2025 — the largest foreign direct investment in Louisiana history**; ~1,800 workers on site, first production 2029. ([LED / opportunitylouisiana.gov](https://www.opportunitylouisiana.gov/news/historic-investment-woodside-energy-announces-17-5-billion-final-investment-decision-for-lng-facility-in-southwest-louisiana-becomes-largest-foreign-direct-investment-in-state-history))
- **Commonwealth LNG** (Cameron Parish) took a **$13B FID**, pushing Louisiana past **$100B in announced capital projects** since Jan 2024. ([LED](https://www.opportunitylouisiana.gov/news/louisiana-surpasses-100-billion-in-new-investment-following-commonwealth-lng-final-investment-decision))
- **Lake Charles Methanol II** = $3.24B low-carbon methanol plant. ([LED via search](https://www.opportunitylouisiana.gov/))
- Major anchor employers named for the region: **CITGO, ConocoPhillips, PPG Industries, Sasol, Phillips 66, Trunkline LNG**. Petrochemical/energy generates ~**26,620 jobs, $2.3B in earnings, ~$9B added value** in SWLA. ([citytowninfo](https://www.citytowninfo.com/places/louisiana/lake-charles/work); [BIC Magazine](https://www.bicmagazine.com/industry/refining-petrochem/energy-super-regions-foster-economic-resiliency-in-louisiana/))

**Healthcare (a prime mid-market target):**
- **Lake Charles Memorial Health System** — largest community-owned full-service system (multiple hospitals + Memorial Medical Group physician network). ([Chamber SWLA](https://www.allianceswla.org/news/2021/10/13/general-news/lake-charles-memorial-health-system-supports-growth))
- **CHRISTUS Ochsner Lake Area Hospital / Southwest Louisiana** — second major system. ([Chamber SWLA](https://events.allianceswla.org/members/member/christus-ochsner-lake-area-hospital-377))
- Health Care & Social Assistance is the **#1 employer in Calcasieu Parish at 13,902 people (2024)**. ([Data USA / Census](https://datausa.io/profile/geo/calcasieu-parish-la))

**Other pillars:** Gaming/hospitality (L'Auberge, Golden Nugget, Horseshoe casinos), the **Port of Lake Charles** (top-tier U.S. tonnage port / logistics), and a large industrial-construction/fabrication services economy feeding the plants.

**Skeptic's note:** Despite the capex headlines, the "boom = jobs" narrative is contested — a 2026 analysis argued the energy boom under-delivered on net job creation ([Verite News](https://veritenews.org/2026/04/22/louisiana-energy-boom-jobs-data-center/); [Louisiana Illuminator](https://lailluminator.com/2026/04/23/louisiana-energy-jobs/)). This matters for Marcus: the **mega-projects mostly buy from national EPC/IT vendors, not a New Orleans solo consultant.** The real opportunity is the **mid-market firms in the supply chain and the local service economy**, not the LNG trains themselves.

## 2. How many mid-market firms actually exist — and is the tech market a vacuum?

**Establishment base (Calcasieu Parish, 2024, Data USA / Census):**
- **~92,600 employed**; median household income **$67,564** ([Data USA](https://datausa.io/profile/geo/calcasieu-parish-la)).
- Establishment counts by sector: **Retail 315, Professional/Scientific/Technical Services 297, Other Services 254** — these are *sector samples*, not a parish total; Data USA does not surface a clean all-sector establishment total, and the underlying **County Business Patterns** 2024 data isn't released until later in 2026 ([Census CBP](https://www.census.gov/programs-surveys/cbp.html)). **[VERIFY]** the precise count of $5–50M-revenue firms via CBP / Census data.census.gov firm-size tables when 2024 CBP publishes.

**Sizing the target tier (reasoned estimate):**
- A useful national rule of thumb: roughly **3–4% of all employer establishments fall in the ~20–500 employee band** that maps to ~$5–50M revenue. Calcasieu has on the order of **~4,000–5,000 employer establishments** [est] across all sectors; the mid-market tier is plausibly **~200–400 firms** in Calcasieu, and **~400–600 across the 5-parish SWLA region** [est]. Marcus does not need the whole tier — capturing **8–15 logos over 24 months** would saturate his realistic delivery capacity as a solo/with-contractors operator.
- These are concentrated in: **industrial services/fabrication, specialty construction, healthcare clinics & multi-site practices, gaming/hospitality back-office, logistics/trucking, and professional services (incl. the CPA-client book itself)** — exactly the segments that run on QuickBooks/Karbon/Excel/SharePoint and have **no internal software team.**

**Competitive density — is it a vacuum? Mostly yes, with a caveat:**
- Local supply is **thin and low-altitude.** A Yelp + directory scan of "software development / IT consulting in Lake Charles" returns mostly **managed-IT / break-fix / web-design shops**, not AI/automation or custom-software engineering: **NeighborTechs** (managed IT, web design), **Techware Consulting** (cloud/telecom/network/server support), **Southern Technologies** (IT consulting/design). ([Yelp](https://www.yelp.com/search?find_desc=Software+Development&find_loc=Lake+Charles,+LA); [NeighborTechs](https://neighbortechs.com/la/lake-charles/system-digitization/); [Southern-Tech](https://www.southern-tech.net/consulting); [Techware via Yelp](https://www.yelp.com/biz/techware-consulting-lake-charles))
- The "software development" listings that *do* surface for Lake Charles are largely **out-of-market national/offshore SEO pages targeting the geo** (LimeUp, Build in Motion, Concetto Labs, Protologic, 247 Virtual Solution) — i.e., they have **no local presence, no warm relationships, no SWLA references.** ([LimeUp](https://soft.limeup.io/louisiana/lake-charles/); [Build in Motion](https://buildinmotion.com/local/la/lake-charles))
- **Caveat / devil's advocate:** "no local custom-software competitor" is *not* the same as "no competitor." The real competition is (a) the incumbent **managed-IT shops upselling**, (b) **horizontal SaaS** the business already pays for (the buyer's default is "isn't this just a Zapier/Make/Copilot thing?"), and (c) **doing nothing.** Marcus's edge is not "I can code" — it's **Meta-grade engineering + a trusted, warm, CPA-introduced relationship**, which the offshore SEO shops and local break-fix vendors structurally cannot match. That combination *is* the moat in this market.

## 3. What these firms buy — and at what price

**What "money businesses with little tech competition" actually purchase:**
1. **AI ops automation** — document/email triage, quoting, scheduling, RFP/bid response drafting, customer-comms automation. Entry workflow projects run **$5,000–$8,000** each. ([Latenode](https://latenode.com/blog/industry-use-cases-solutions/enterprise-automation/17-top-ai-automation-agencies-in-2025-complete-service-comparison-pricing-guide); [Arsum](https://arsum.com/blog/posts/ai-automation-agency-pricing/))
2. **Internal tools / line-of-business apps** — replacing spreadsheet-and-email processes (job tracking, dispatch, compliance logging, inventory). Mid-sized custom business tools run **$80k–$200k**; small apps/MVPs **$30k–$100k+**. ([FullStack 2025 price guide](https://www.fullstack.com/labs/resources/blog/software-development-price-guide-hourly-rate-comparison); [Spdload](https://spdload.com/blog/custom-software-development-cost/))
3. **Data / RCM / document automation** — healthcare revenue-cycle, AR/AP automation, OCR + extraction over PDFs/contracts/invoices (directly in Marcus's wheelhouse and the CPA book's pain).
4. **Advisory retainers** — ongoing AI/automation management.

**Price points (verified ranges):**
| Engagement type | Market range | Source |
|---|---|---|
| AI/automation **project** | $2,500–$15,000 | [AI Business](https://aibusiness.vc/solo/how-to-charge-ai-automation-services), [Latenode](https://latenode.com/blog/industry-use-cases-solutions/enterprise-automation/17-top-ai-automation-agencies-in-2025-complete-service-comparison-pricing-guide) |
| Single workflow automation | $5,000–$8,000 | [Latenode](https://latenode.com/blog/industry-use-cases-solutions/enterprise-automation/17-top-ai-automation-agencies-in-2025-complete-service-comparison-pricing-guide) |
| Monthly **retainer** (advisory/ongoing) | $2,000–$8,000/mo (light); $8k–$15k+ (intensive) | [Moxo](https://www.moxo.com/blog/ai-automation-consulting-services-cost), [Arsum](https://arsum.com/blog/posts/ai-automation-agency-pricing/) |
| Custom **mid-market app** | $80,000–$200,000 (small MVPs $30k–$100k) | [FullStack](https://www.fullstack.com/labs/resources/blog/software-development-price-guide-hourly-rate-comparison), [Spdload](https://spdload.com/blog/custom-software-development-cost/) |
| Mid-market consulting **hourly** | $120–$250/hr (small-firm $90–$160) | [Brightworks](https://brightworksgroup.net/blog/what-are-typical-it-consulting-fees/), [FullStack](https://www.fullstack.com/labs/resources/blog/software-development-price-guide-hourly-rate-comparison) |
| AI consultant **day rate (US)** | $600–$1,200/day | [Nicola Lazzari](https://nicolalazzari.ai/guides/ai-consultant-pricing-us) |

**Conversion economics that favor this play:** Clutch 2025 data cited that **62% of SMBs prefer project-based pricing for their first AI engagement, but 71% convert to retainers within 6 months** once they see results; average AI-automation retainer client stays **11 months (~$22k–$33k LTV)** ([Latenode](https://latenode.com/blog/industry-use-cases-solutions/enterprise-automation/17-top-ai-automation-agencies-in-2025-complete-service-comparison-pricing-guide)). This is the land-and-expand engine: small paid pilot → retainer → bigger build. **[VERIFY]** the underlying Clutch survey directly.

## 4. Realistic revenue Marcus can capture in 12–24 months (warm channel)

**Why the warm channel changes the math:** the brutal part of this business is CAC — the SEO/offshore shops spend heavily to acquire strangers. Marcus's CAC is effectively **a warm CPA introduction**, which converts at multiples of cold outbound and lets him **skip the "do I trust this person with my business data" objection** that kills most local deals. The brother's firm is simultaneously (a) the **first reference customer** (TWK runs Karbon + SharePoint + Teams — a textbook automation target), and (b) a **distribution channel into both a concentrated accounting-client book and a broad high-value SWLA owner network.**

**Capacity reality (devil's advocate):** Marcus has a $50k base + verbal rev-share role at TWK *and* three recovery ventures. This channel competes for his hours. The constraint is **delivery bandwidth, not demand.** Revenue projections must assume part-time delivery, not a full agency.

**Modeled outcomes (reasoned estimates built on the verified price points above):**

- **Conservative (12 mo):** 4–6 project engagements at ~$6k–$15k avg + 2–3 retainers at ~$3k/mo ramping in H2 → **~$60k–$90k** annualized. This is essentially the v1 portfolio thesis ("$90–120k advisory/automation engine") *de-risked downward* for part-time delivery.
- **Base (12–24 mo):** Brother's network yields 8–12 logos; mix of ~$10k–$40k builds + a stable book of **4–6 retainers at $3k–$5k/mo (~$150k–$300k recurring run-rate)** plus project work → **~$120k–$220k** in year-2 revenue.
- **Upside (24 mo, if he pulls in 1–2 contractors and lands one $80k–$150k custom build):** **$250k–$400k+**, but this crosses from "warm side-channel" into "real agency" and collides hard with the recovery ventures' time.

**Most credible 12–24 month capture from the warm channel alone: ~$120k–$200k**, weighted toward recurring retainers. This is consistent with — and slightly more aggressive than — the v1 rank-#1 "$90–120k income engine," with the upside coming from retainer stacking rather than one-off builds.

## 5. Highest-value productized offering to lead with

**Lead with a productized "AI Back-Office Audit + Automation Sprint," not custom software.**

- **Structure:** A fixed-fee **$2,500–$5,000 paid diagnostic** ("AI Operations Audit") → a **$6k–$15k automation sprint** delivering 1–2 working workflows → a **$3k–$5k/mo retainer**. This matches the verified land-and-expand pattern (project-first, 71% retainer conversion) and keeps each engagement inside part-time delivery capacity.
- **Why productized, not hourly custom builds:** custom $80k–$200k apps are higher revenue per deal but (a) blow Marcus's time budget, (b) carry delivery risk, and (c) scare first-time SMB buyers. A productized audit-to-retainer ladder is **repeatable, referenceable, and sellable by the brother in one sentence** ("he'll audit your operation for $X and show you what AI can save").
- **Beachhead vertical: the CPA-client book + healthcare RCM.** Start with **document/email/invoice automation for TWK's own accounting clients** (homogeneous pain, brother can co-sell, QuickBooks/Karbon data), then expand into **healthcare revenue-cycle and clinic document automation** (Memorial / CHRISTUS Ochsner ecosystem of independent clinics) where document volume and dollar stakes are highest. The first paid case study should be **TWK itself** — automate the firm's Karbon/SharePoint workflows, then sell that exact story to its clients.
- **Pricing anchor:** position at the **top of the local market but below national agencies** — $150–$200/hr equivalent, productized into fixed fees so the buyer never sees an hourly clock. Local competition (break-fix IT at managed-services rates) cannot credibly deliver AI/custom automation, so there is **room to price on value, not on the local IT-shop comp.**

## Verdict

The warm CPA channel is a **genuine, defensible niche** — the local market is thin on real AI/automation/custom-software supply, the buyer tier exists (~400–600 SWLA mid-market firms [est], **[VERIFY] via 2024 CBP**), and the price points support a **$120k–$200k 24-month outcome** that is gated by Marcus's *time*, not by demand. Lead with a **productized AI audit → sprint → retainer ladder**, beachhead on the **CPA client book + healthcare document/RCM automation**, and use **TWK as the first reference build.** The two biggest risks are (1) **delivery bandwidth** against the recovery ventures, and (2) treating "no local competitor" as a moat when the real competitor is the buyer's inertia and incumbent managed-IT upsell — the moat is the warm relationship + senior engineering, and it only holds if Marcus actually ships referenceable wins fast.

**Files / paths:** This is a standalone research deliverable returned as text; no files were written (plan-mode constraints). It is ready to drop into the venture REPORT.md under a "SWLA / Brother's Network Channel" section.

---

## 5. McNeese University Channel

I have comprehensive, well-sourced material across all four angles. Writing the deliverable now.

---

# McNeese State University Channel — Entry Points (4 Angles)

Marcus is a McNeese alumnus and SWLA-based. Below are concrete, sourced entry points per angle, a devil's-advocate read on each, and a ranked first-contact path. McNeese is governed by the **University of Louisiana System** and accredited by **SACSCOC** — both facts shape the procurement and adjunct-credential answers below.

---

## Angle 1 — Sell AI/automation/admin-efficiency services TO the university

**Procurement thresholds (verified, current).** McNeese's own Purchase Guidelines, updated to reflect **Governor's Executive Order JML 25-104**, set these tiers ([mcneese.edu/business-affairs/purchasing/purchase-guidelines](https://www.mcneese.edu/business-affairs/purchasing/purchase-guidelines/)):
- **≤ $30,000** — non-competitive, **no bids required**. Buyable on the open market from a "suggested vendor." *This is the single most important number for a small AI-services vendor.*
- **$30,000.01–$60,000** — three telephone/fax quotes (24-hr response window).
- **> $60,000** — sealed bid, 5 qualified bidders, public notice on the state **LaPAC** site, ~21-day bid period, advertised at the requesting department's expense.

**The software loophole.** Computer **software under $150,000** is explicitly listed as a **Competitive Purchase Exception** — i.e., exempt from bidding ([same page](https://www.mcneese.edu/business-affairs/purchasing/purchase-guidelines/)). A SaaS/automation license can therefore be bought far above the $30k services threshold without a bid, if structured as software. **Sole-source** is also available but narrow: it requires a single-supplier justification and a signed sole-source letter from the vendor; "a requirement for a particular brand name item does not justify a sole source procurement if there is more than one potential bidder" ([same page](https://www.mcneese.edu/business-affairs/purchasing/purchase-guidelines/)).

**How to get in the door / vendor onboarding.**
- McNeese Purchasing is the front door ([mcneese.edu/purchasing](https://www.mcneese.edu/purchasing/)). Requisitions originate **inside departments**, not with Purchasing — so the real sale is to a department head (e.g., a dean, the Registrar, IT) who then enters the requisition. Purchasing only executes it.
- State-level vendor registration: **LaGov Supplier Portal** (self-registration) ([lagoverpvendor.doa.louisiana.gov](https://lagoverpvendor.doa.louisiana.gov/irj/portal/anonymous?guest_user=self_reg)). Bids are posted on **LaPAC**, filterable by department ("University – McNeese State University") ([wwwcfprd.doa.louisiana.gov/osp/lapac](https://wwwcfprd.doa.louisiana.gov/osp/lapac/dspBid.cfm?search=department&term=52)).
- **State-contract piggyback:** the university may buy off existing State Purchasing contracts with no bid ([purchase-guidelines](https://www.mcneese.edu/business-affairs/purchasing/purchase-guidelines/)).

**SDVOSB/veteran leverage at the state level.** Federal SDVOSB does **not** transfer to Louisiana state purchasing. The state-side analog is LED's **Veteran Initiative / Veteran-Owned Small Entrepreneurship** certification (and the parallel **Hudson Initiative** for small businesses), administered by **Louisiana Economic Development** ([doa.la.gov Hudson and Veteran Initiatives](https://www.doa.la.gov/doa/osp/vendor-resources/hudson-and-veteran-initiatives/); [opportunitylouisiana.gov/program/hudson-initiative](https://www.opportunitylouisiana.gov/program/hudson-initiative)). Caveat (skeptic's note): these are "good-faith effort," **goal-oriented, race/gender-neutral** programs that encourage agencies and prime contractors to use certified small/veteran firms — they are **not a set-aside and carry no guaranteed award or hard bid preference** ([same DOA page](https://www.doa.la.gov/doa/osp/vendor-resources/hudson-and-veteran-initiatives/)). Worth getting (free, fast, and it stacks with the brother's-firm/SBDC story), but do not overweight it. [VERIFY whether LA still applies any reciprocal price preference for veteran firms — not confirmed on the current DOA page.]

**Devil's advocate.** A university is a slow, low-margin, RFP-shaped customer relative to the brother's private CPA-client network ($90–120k engine). The ≤$30k no-bid lane is real but small, and "AI pilot at a regional public university" usually means an unpaid or token-paid pilot before any real budget appears. Treat McNeese sales as **credibility/logo and pipeline**, not near-term revenue.

**First contact:** Email the **ENCS Department Head, Dr. Srinivasan Ambatipati** (sambatipati@mcneese.edu, 337-475-5862) AND McNeese **IT/Business Affairs Purchasing** ([mcneese.edu/purchasing](https://www.mcneese.edu/purchasing/)) — but lead with a department sponsor, not Purchasing. Pitch a ≤$30k admin-automation pilot (e.g., document/workflow automation) that fits the no-bid lane.

---

## Angle 2 — Recovery / health programs as a partner & channel

**Relevant academic units (all live):**
- **Psychology & Counseling**, within the **College of Nursing and Health Professions** ([mcneese.edu/nursing/psychology](https://www.mcneese.edu/nursing/psychology/)).
- **MS in Clinical Mental Health Counseling** — an 8-semester, 3-year master's that "prepares master's-level" counselors ([catalog.mcneese.edu](https://catalog.mcneese.edu/preview_program.php?catoid=102&poid=61811)). This is a CACREP-style pipeline of future counselors — a natural fieldwork/practicum and lived-experience-speaker channel.
- **Kaufman Drug & Crime Clinic (KDCC)** runs a **Counseling Services Program** (low-cost counseling) and the **McNeese Gambling Treatment Program** ([catalog.mcneese.edu College of Nursing entity page](https://catalog.mcneese.edu/preview_entity.php?catoid=102&ent_oid=5500&returnto=8472)). An on-campus addiction-adjacent clinic is the most direct programmatic match for the recovery ventures.
- **MSN** with a **Psychiatric Mental Health Nurse Practitioner** concentration ([facebook.com/McNeeseStateU post](https://www.facebook.com/McNeeseStateU/posts/1277459521081515/)) — referral-source relevance for the apps.

**Collegiate Recovery Community (CRC).** I found **no evidence of an established collegiate recovery program at McNeese** on .edu sources — only generic CRP literature ([PMC8986624](https://pmc.ncbi.nlm.nih.gov/articles/PMC8986624/)). [VERIFY directly with the Dean of Students / Counseling Center.] Skeptic's read: this is a **gap, not a partner** — meaning there's a "help us stand one up" angle (lived-experience programming, peer-navigation curriculum) rather than a ready-made channel. That's higher-effort, lower-certainty, and bumps squarely into Next Step Recovery's **non-clinical scope-of-practice** existential risk — be careful pitching anything that looks like counseling near a CACREP program and a licensed clinic.

**First contact:** Email the **Department of Psychology & Counseling / College of Nursing and Health Professions** ([mcneese.edu/nursing/psychology](https://www.mcneese.edu/nursing/psychology/)) proposing (a) a lived-experience guest lecture to CMHC students and (b) exploring a peer-recovery student group — explicitly framed as **peer support, not clinical counseling**.

---

## Angle 3 — Adjunct / Associate Professor in CS (ENCS)

**Department reality.** McNeese has **no standalone CS department**; CS sits inside the **Department of Engineering & Computer Science (ENCS)**, headed by **Dr. Srinivasan Ambatipati** (chemical eng.), and the faculty roster is overwhelmingly EE/ME/Civil ([mcneese.edu ENCS directory](https://www.mcneese.edu/engineering-and-sciences/directory/engineering-and-computer-science/)). CS instruction appears thin — the visible CS-teaching faculty is **Rhonda Anderson, M.S.** (a **Visiting Assistant Professor** with a **Master's in MIS**, teaching "hardware, operating systems, web development, computer ethics, and computer programming") ([same directory](https://www.mcneese.edu/engineering-and-sciences/directory/engineering-and-computer-science/)). **This is the most important signal in this section:** McNeese already credentials CS teaching with a **master's degree**, not a PhD.

**Credential requirement (the key question).** Two distinct bars:
- **Tenure-track Assistant Professor** of CS: the current posting **requires a PhD** ([LinkedIn job](https://www.linkedin.com/jobs/view/assistant-professor-of-computer-science-at-mcneese-state-university-4421111694)). Not Marcus's lane.
- **Adjunct / instructor:** governed by **SACSCOC faculty-credential standards**, which the UL System and McNeese follow. The SACSCOC norm for teaching undergraduate courses is a **master's degree in the discipline OR a master's plus at least 18 graduate semester hours in the teaching discipline** ([SACSCOC 2024 Resource Manual](https://sacscoc.org/app/uploads/2024/02/2024-POA-Resource-Manual.pdf); representative LA-system credential form: [ladelta.edu faculty credentials](https://www.ladelta.edu/faculty-and-staff/human-resources/files/documents/Faculty%20Credentials%20Application%20Fillable%202024%20(2).pdf)). The standard allows institutions to justify faculty via **"other qualifications and experience"** (tested experience) when the degree doesn't line up — the named exception path for industry hires ([SACSCOC manual](https://sacscoc.org/app/uploads/2024/02/2024-POA-Resource-Manual.pdf)).
- **Industry-experience exception (Marcus's actual path).** Marcus has a **bachelor's in CS**, not a master's. To teach for-credit CS he'd need the department to credential him under the **"tested experience / other qualifications"** justification (Meta, YC, federal). That is at the **department head's + dean's discretion** and is **plausible but not guaranteed** — it's exactly how regional schools fill applied courses (cybersecurity, software engineering, AI) they can't staff. [VERIFY McNeese's specific tested-experience policy with HR/ENCS.] Skeptic's note: without a master's, a credit-bearing appointment is discretionary and could be denied; the safer near-term ask is **guest lecturer / industry capstone mentor / advisory-board member**, which carries the credibility without the credential hurdle.

**Pay (Louisiana adjunct, the unglamorous truth).** No McNeese-specific rate was published. Benchmarks:
- National median adjunct pay is **~$1,166/credit hour, ~$4,998/term** ([CUPA-HR](https://www.cupahr.org/resource/adjunct-faculty-in-the-higher-education-workforce/)).
- Louisiana indicative average **~$30/hour** ([Indeed LA](https://www.indeed.com/career/adjunct-instructor/salaries/LA)); UL-system adjunct scales exist per course ([UL Lafayette compensation](https://louisiana.edu/firstyear/first-year-seminar/instructors/teaching-univ-100/compensation)). [est] Expect roughly **$2,000–$3,500 per 3-credit course** at a regional LA public — i.e., **financially negligible** for Marcus.

**Why do it anyway.** The value is **not the pay** — it's (a) the **title** ("Adjunct Professor of Computer Science, McNeese") as a credibility multiplier for the CPA-advisory line and SDVOSB/state work, (b) a **talent pipeline** of CS students for the recovery apps and automation work, and (c) a warm institutional relationship that feeds Angles 1 and 4.

**First contact:** Email **Dr. Srinivasan Ambatipati, ENCS Department Head** (sambatipati@mcneese.edu, 337-475-5862) offering to teach/guest-lecture an **applied AI or software-engineering course** as an alumnus + industry practitioner; cc McNeese HR ([schooljobs.com/careers/mcneese](https://www.schooljobs.com/careers/mcneese/)) and ask directly about the tested-experience credentialing path for a bachelor's-holder.

---

## Angle 4 — Alumni + SBDC (the CPA-advisory referral channel)

**This is the strongest McNeese angle and ties directly to the income engine.**

**LSBDC at McNeese** — the hosted Small Business Development Center:
- Location: **Henning SEED Center, 4310 Ryan St, Ste 162, Lake Charles, LA 70605**; **337-475-5529**; **lsbdc.msu@louisianasbdc.org** ([louisianasbdc.org LSBDC at McNeese](https://louisianasbdc.org/lsbdc-at-mcneese-state-university); [lsbdc.org center 18004](https://www2.lsbdc.org/center.aspx?center=18004)).
- Provides **no-cost confidential consulting** + low-cost workshops in business-plan development, market analysis, sources of capital ([same](https://louisianasbdc.org/lsbdc-at-mcneese-state-university)). Serves the **5-parish SWLA region**: Allen, Beauregard, Calcasieu, Cameron, Jefferson Davis ([same](https://louisianasbdc.org/lsbdc-at-mcneese-state-university)) — **identical geography to the brother's CPA book.**
- The network is **hosted by LSU**, with state credibility (the center recently won an award) ([mcneese.edu news](https://www.mcneese.edu/news/louisiana-sbdc-at-mcneese-receives-award/)).
- **New director: Dean Day, effective Feb 1, 2026** ([mcneese.edu news](https://www.mcneese.edu/news/dean-day-named-director-for-louisiana-sbdc-at-mcneese/)) — a fresh relationship to build, with no incumbent loyalty. Actively running **2026 SWLA entrepreneur workshops** ([facebook.com/McNeeseStateU](https://www.facebook.com/McNeeseStateU/posts/1359529886207811/)).

**Why this is the referral goldmine.** SBDC counselors meet a constant stream of **early-stage businesses that need bookkeeping, tax structuring, and advisory** — exactly the brother's CPA firm's product. A **referral relationship runs both ways**: the firm refers pre-revenue clients to SBDC for free planning; SBDC refers graduating clients who need a CPA/advisory to the firm. Marcus, as a veteran alumnus offering **free workshops** (AI for small business, automation), becomes a recurring SBDC-stage presence that channels leads into the advisory line — the #1 venture.

**Co-location ecosystem.** The SBDC sits inside the **Henning SEED Center** (Southwest Louisiana Entrepreneurial & Economic Development center, Calcasieu Parish-run) ([calcasieu.gov SEED Center](https://www.calcasieu.gov/services/planning-development/seed-center); [kplctv.com naming](https://www.kplctv.com/2025/03/11/seed-center-named-honor-local-family/)) — a one-stop economic-dev hub for the 5-parish area, plus the **Business Incubator of Southwest Louisiana** and **Chamber SWLA** ([allianceswla.org](https://www.allianceswla.org/starting-a-business-incubator-programming/)). One physical building concentrates SBDC + incubator + chamber + economic dev — a dense, walkable network.

**Veteran + alumni hooks:**
- **McNeese Veterans Services** ("Military and Veteran Friendly campus") ([mcneese.edu/registrar/veterans_services](https://www.mcneese.edu/registrar/veterans_services/)) — credibility/community, not a sales channel.
- McNeese **Alumni/Community** portal ([mcneese.edu/alumni-friends](https://www.mcneese.edu/alumni-friends/)) — [VERIFY whether a searchable alumni-business directory exists; not confirmed].

**Devil's advocate.** SBDC's mandate is **free** help to pre-revenue founders — many are not yet able to pay for CPA advisory, so the referral cohort skews early and low-value. The payoff is a **slow drip of future clients**, not immediate revenue, and it depends on a genuine relationship with the new director rather than a transactional ask. Still, it's the lowest-cost, highest-fit, warm-network move on this list.

**First contact:** Email **lsbdc.msu@louisianasbdc.org** / call **337-475-5529** to introduce yourself to **new director Dean Day** as a McNeese alumnus + USAF veteran + AI/automation practitioner offering to run a **free "AI for SWLA small business" workshop**, and propose a **two-way referral relationship** with the brother's CPA firm.

---

## Ranked verdict — single most promising angle

**#1 (do first): Angle 4 — LSBDC at McNeese.** It is the only McNeese channel that **directly feeds the #1 venture** (the CPA-advisory income engine), matches the brother's exact 5-parish geography, costs nothing, leverages the new-director timing (Feb 2026), and compounds via free workshops. Lowest cost, highest strategic fit.

**#2: Angle 3 — adjunct/guest CS lecturer at ENCS.** Negligible pay, but the **title is a credibility multiplier** for everything else and the **talent pipeline** is real; master's-credentialed CS teaching already exists at McNeese, and the tested-experience exception is the route for a bachelor's-holder. Start as guest lecturer to de-risk the credential question.

**#3: Angle 1 — sell services to the university.** Real but slow; exploit the **≤$30k no-bid lane** and **software-under-$150k exemption**, get the free **LED Veteran Initiative** cert to stack the story — treat as logo + pipeline, not near-term cash.

**#4: Angle 2 — recovery/health programs.** Most uncertain (no existing collegiate-recovery program found) and most exposed to the non-clinical scope-of-practice risk; pursue only as low-commitment lived-experience guest lectures into the CMHC program.

**One contact to make this week:** the **LSBDC at McNeese** — email **lsbdc.msu@louisianasbdc.org**, 337-475-5529, Henning SEED Center, Lake Charles.

### Key unverified items flagged
- [VERIFY] Whether Louisiana still applies any reciprocal price preference for the Veteran Initiative (not on current DOA page).
- [VERIFY] McNeese's specific "tested experience"/credentialing policy for a bachelor's-degree CS adjunct (confirm with ENCS + HR).
- [VERIFY] Existence of any McNeese collegiate recovery community and any searchable alumni-business directory.
- [est] McNeese adjunct per-course pay (~$2,000–$3,500/3-credit) is a Louisiana-regional estimate, not a published McNeese rate.

---

## Adversarial Verification

### Verdict — regroup "no direct competitor" claim

I have enough evidence to write a decisive verdict. Behave Health explicitly markets to Oxford House networks, refuting the "Oxford House niche is unserved" implication. Let me synthesize now rather than spend further.

---

## Adversarial Verification: regroup's "No Direct Competitor" Claim

**VERDICT: REFUTED (and the moat is largely commoditized).** Every pillar of the claim fails under scrutiny. The sober-living/recovery-residence software market is crowded, several incumbents predate regroup by 5–10 years, and the three asserted moats (GPS meeting verification, the 300K-meeting dataset, the Oxford House World Services partnership) are either already shipped by competitors, of dubious defensibility, or both. There is even a name collision: an app literally called "Regroup" already exists in the App Store in this exact category.

### 1. "No direct competitor" is false — this is a saturated category

Named direct competitors, all operator-pays B2B SaaS for sober living / recovery residences:

| Competitor | Founded | Notes | Source |
|---|---|---|---|
| **One Step Software** | 2017 | Self-styled "#1"; drug-court functionality, autopay rent, curfew/check-ins, multi-house | onestepsoftware.com |
| **Behave Health** (Sober Living App) | 2015 | EHR + RCM + recovery-residence module; **explicitly markets to Oxford House networks** | behavehealth.com/recovery-residences, behavehealth.com/glossary/oxford-house |
| **Sobriety Hub** | 2022 | $65/mo flat; resident app w/ GPS meeting verification; hired former Rep. Patrick Kennedy | sobrietyhub.com |
| **Transparency Technologies** | recent | **Near-clone of the entire regroup + homegroups thesis** (see §3) | transparencytechnologies.ai |
| **Oathtrack** | recent | "All-in-one" billing, tasks, meetings, resident tracking | oathtrack.com |
| **SoberFriend** | recent | UA/curfew/meeting-attendance compliance trail | soberfriend.io |

A competitor (Sobriety Hub) even publishes a "Big 3 of Sober Living Software" buyer's guide — the category is mature enough to have a recognized incumbent set, head-to-head comparison content, and documented switching between vendors (sobrietyhub.com/our-blog/2026-buyers-guide). "No direct competitor" is not an overstatement; it is contradicted by the first page of search results.

### 2. The moats, individually

**GPS meeting verification — REFUTED, fully commoditized.**
- Sobriety Hub ships "Meeting Attendance with GPS Verification" today (sobrietyhub.com/features/resident-mobile-app).
- Transparency Technologies ships "GPS-Verified Meeting Attendance… GPS geofencing. Clock in and out of meetings with real-time tracking," plus a live member map with in-zone/out-of-zone/in-meeting status (transparencytechnologies.ai/organizations).
- Sober Living App lists "GPS tracking integrated with compliance workflows… Meeting attendance verification" (soberlivingapp.com/blog/sober-living-software-comparison).
This is now a checkbox feature, not a differentiator. It is also trivially spoofable (location-spoofing apps) and raises 42 CFR Part 2 / consent issues that competitors are already navigating — no technical barrier exists for a competitor to add it; multiple already have.

**300K-meeting dataset — weak moat [VERIFY].** Meeting directories are largely public/community-maintained; the in-app "Regroup" competitor already advertises "meeting lists for the majority of towns and cities in the United States" with check-in (apps.apple.com/us/app/regroup-sober-living-app/id1502040260). A meeting list is a commodity data layer, not proprietary IP, and accuracy decays without constant upkeep. I could not find evidence that 300K verified meetings confers pricing power or lock-in [VERIFY].

**Oxford House World Services partnership — overstated and structurally fragile.**
- The Oxford House model is by charter "self-run, self-supported… each Oxford House is autonomous" with no central operator (oxfordhouse.org, oxfordhouse.org/model). The decentralized model is the opposite of the "operator pays, not resident" SaaS thesis — in a true Oxford House, residents collectively pay Equal Expense Share and there is no operator to be the paying customer (oxfordhouse.org; vaoxfordhouse.org "What Makes OH Work"). The economic buyer regroup's model assumes often does not exist in canonical Oxford Houses.
- Behave Health already markets tooling "that support[s] the operational needs of Oxford House networks" (behavehealth.com/glossary/oxford-house) — so even the Oxford House niche is not virgin territory.
- A World Services "partnership" (if it exists — I did not find public confirmation [VERIFY]) is a non-exclusive relationship with a nonprofit, not a contractual moat; OHWS could endorse multiple vendors or none.

### 3. The most dangerous finding: Transparency Technologies is building regroup AND homegroups at once

Transparency Technologies (transparencytechnologies.ai) already combines, in one shipped product, nearly every element of the founder's recovery portfolio:
- Operator-pays org plan: **$39.99/mo + $14.99/member**, self-service signup (directly comparable to regroup's $49–$249 tiers, and arguably cheaper at small house sizes).
- GPS geofencing + meeting clock-in/out + house-manager read-only role.
- A feature literally named **"Home groups"** (collides with the *homegroups* venture name).
- AI journal/Fourth-Step analysis "powered by Anthropic Claude," a Recovery Transparency Index, sponsor-sponsee connections.
- Explicit "**Built for compliance with 42 CFR Part 2**" positioning — the exact regulatory risk flagged as existential for homegroups, which a competitor is already addressing head-on.

This single competitor refutes the "no direct competitor" claim for *both* regroup and homegroups simultaneously, and demonstrates the GPS/AI moat is replicable by a small team.

### 4. Name collision risk

An iOS app named **"Regroup: Sober Living App"** (App Store id1502040260) already exists in this category and offers meeting check-in. This is a trademark/SEO/brand-confusion problem independent of the competitive analysis. [VERIFY current ownership/status, but the listing is live.]

### What it means for the venture plan

1. **Kill the "no competitor / category creator" narrative.** It is factually false and will not survive due diligence with any informed buyer or investor. Reposition around *specific* wedges (e.g., a particular state's NARR/certification workflow, deep Stripe-rent integration, the SWLA/regional GTM via the brother's network) rather than category novelty.
2. **Drop GPS verification and "300K meetings" from the moat slide.** Both are commoditized or community-data. If a moat exists, it must come from distribution (warm regional channel), switching costs (data lock-in once billing runs through you), or a genuinely exclusive Oxford House World Services arrangement in writing — none of which are established yet.
3. **Re-examine the Oxford House SKU economics.** The Oxford pricing tier ($49/$89/$299) assumes a paying operator that the canonical self-run model lacks. Validate who actually holds the credit card in target houses before building for that segment; Behave Health is already there.
4. **Treat Transparency Technologies as the benchmark competitor**, not a hypothetical. Pull its pricing, reviews, and traction before any further build. It validates demand but also caps differentiation and pricing power.
5. **Resolve the "Regroup" name collision** before spending on brand.
6. **Reinforces the v1 portfolio sequencing thesis.** This stress-test strengthens the existing ranking that put the CPA-advisory income engine first and regroup second-with-caveats: regroup is a real but contested market (good — demand is proven by 6+ funded-enough competitors), not the uncontested greenfield the docs imply. Fund it from advisory cash flow; do not bet the sequence on a moat that competitors have already crossed.

**Unverified items to close:** existence/terms of any OHWS partnership [VERIFY]; provenance and defensibility of the 300K-meeting dataset [VERIFY]; current status/ownership of the conflicting "Regroup" App Store listing [VERIFY]; Transparency Technologies' actual traction [VERIFY]. No CAC/LTV figures exist in the regroup docs, which is itself a red flag given the now-documented competitive density.

---

### Verdict — EKRA-safe flat-SaaS-license bridge

I have sufficient primary and secondary sourcing to deliver a well-grounded adversarial verdict. Writing the deliverable now.

---

## EKRA-Safety of a Flat-License "Continuity Package": Adversarial Verdict

**Verdict: PARTIALLY SUPPORTED — and dangerously oversimplified as stated.** A flat, fixed-fee SaaS license is the *least* risky payment structure under EKRA, but "flat license" alone does NOT immunize the arrangement. EKRA is an *intent-based* statute, so the legal exposure turns on **what the software does and how it is sold**, not on the label "flat SaaS license." Several plausible designs of a recovery-app→treatment-center "continuity package" would trip EKRA, AKS, or 42 CFR Part 2 even if billed as a flat fee.

### Why the structure matters more than the price tag

EKRA (18 U.S.C. § 220) criminalizes paying *or receiving* remuneration to **induce a referral** to, or in exchange for an individual *using the services of*, a recovery home, clinical treatment facility, or laboratory. Penalties are up to **$200,000 and 10 years per violation** ([Baker Donelson, Aug 4 2025](https://www.bakerdonelson.com/ekras-application-to-marketing-arrangements-laboratories-and-other-providers); [18 U.S.C. § 220](https://uscode.house.gov/view.xhtml?req=(title:18%20section:220%20edition:prelim))). Critically, EKRA is **broader than AKS in one direction** (it reaches *commercial/private-pay* patients, not just Medicare/Medicaid — [Health Law Diagnosis, Feb 2026](https://www.healthlawdiagnosis.com/2026/02/eliminating-kickbacks-in-recovery-act-2025-updates-and-looking-to-2026/)) and **narrower in another** (its safe harbors are stingier than AKS — see below).

The flat-fee theory rests on the principle that payment unconnected to referral *volume or value* lacks the inducement intent EKRA requires. That principle is real and now has appellate backing: in **United States v. Schena, No. 23-2989 (9th Cir. July 11, 2025)** and the companion **S&G Labs Hawaii, LLC v. Graves (9th Cir. July 11, 2025)**, the Ninth Circuit held that even *percentage-based* compensation is "not automatically a violation" — there must be *wrongful causation*, i.e., intent to "improperly influence" a provider's referral judgment ([Health Law Diagnosis](https://www.healthlawdiagnosis.com/2026/02/eliminating-kickbacks-in-recovery-act-2025-updates-and-looking-to-2026/); [Baker Donelson](https://www.bakerdonelson.com/ekras-application-to-marketing-arrangements-laboratories-and-other-providers)). A flat fee, *a fortiori*, sits even further from inducement than the commission the Ninth Circuit tolerated.

### The strongest counter-evidence — structures a flat fee does NOT save

**1. The label is not dispositive; the function is.** *Schena* explicitly held a person can "induce a referral" by **paying an intermediary who in turn effects referrals**, even if that intermediary cannot directly order tests or refer patients — because the statute reaches *"indirectly"* inducing referrals ([Baker Donelson](https://www.bakerdonelson.com/ekras-application-to-marketing-arrangements-laboratories-and-other-providers)). If the "continuity package" routes *warm patient leads* from the recovery app to a paying treatment center, the flat fee is plausibly recharacterized by DOJ as a fixed-price referral conduit. A fixed price does not cure that — it just makes the *intent* question fact-dependent. **DOJ would look at substance over form.**

**2. The Ninth Circuit is only the Ninth Circuit, and Schena is heading to SCOTUS.** The favorable "flat/commission ≠ automatic violation" reading is **binding only in the 9th Circuit**; Baker Donelson expressly warns national operators to structure for a possible **circuit split** ([Baker Donelson](https://www.bakerdonelson.com/ekras-application-to-marketing-arrangements-laboratories-and-other-providers)). Schena has petitioned the **Supreme Court** to decide whether paying marketers a commission is "remuneration…to induce a referral" — cert is undecided ([Health Law Diagnosis](https://www.healthlawdiagnosis.com/2026/02/eliminating-kickbacks-in-recovery-act-2025-updates-and-looking-to-2026/)). The legal ground under any "marketing payment is fine" theory is actively shifting. Louisiana sits in the **5th Circuit**, which in *U.S. v. Marchetti*, 96 F.4th 818 (5th Cir. 2024) and *U.S. ex rel. Thompson v. Apollo Path* (N.D. Tex. 2025) took an intent-focused approach but has *not* adopted Schena — relying on the 9th Circuit's pro-defendant gloss in Marcus's home circuit is unproven.

**3. EKRA's safe harbors will NOT cleanly cover a third-party app.** EKRA has *no* AKS-style "personal services / management contract" safe harbor that neatly fits arm's-length SaaS, and its employee exception is narrower in practice. Note the trap flagged by counsel: EKRA's employee/contractor exception **prohibits paying employees or contractors based on number of referrals, patients referred, or revenue generated** — *stricter* than the AKS bona fide employee safe harbor ([Stites & Harbison](https://www.stites.com/resources/client-alerts/providers-and-laboratories-beware-of-ekra/); [Chapman Law Group](https://www.chapmanlawgroup.com/practice_areas/ekra-law-eliminating-kickbacks-in-recovery-act/)). A vendor selling to a treatment center is neither its employee nor contractor, so the exception is largely unavailable — meaning the arrangement must survive on **lack of inducement intent**, which is exactly what a referral-flavored package undermines. [VERIFY exact safe-harbor text against 18 U.S.C. § 220(b) before relying.]

**4. Specific designs that WOULD trip the statutes (flat fee notwithstanding):**
- **Per-patient / per-active-bed / per-admission pricing** dressed as "SaaS metering" — this is volume-of-referral pricing in disguise; closest to a classic kickback. (Even commission survived Schena only on intent; per-admission pricing tied to *the app sending that patient* is far worse.)
- **The app delivering identified patient leads** to the paying center (lead-gen / "warm handoff" sold as a feature). This is the *patient-brokering* core EKRA targets; 2025 indictments hit exactly this — *U.S. v. Patton* (C.D. Cal. 2025, marketing co. referring insured patients to SUD facilities) and *U.S. v. Simons* (S.D. Cal. 2025, paying entities for "marketing services") ([Health Law Diagnosis](https://www.healthlawdiagnosis.com/2026/02/eliminating-kickbacks-in-recovery-act-2025-updates-and-looking-to-2026/)).
- **Tiered/discounted license priced to track referral value** (e.g., "free if you admit 10 patients/mo from the app").
- **Bundling the SaaS with any steering of clinical judgment** — the *undue influence* element from Schena.
- **State patient-brokering overlay:** New Jersey (P.L. 2025 c.121) just *expanded* its brokering statute to cover SUD facilities and labs; many states (FL, etc.) have brokering laws with **no commercial-payor carve-out and no Schena gloss** ([Health Law Diagnosis](https://www.healthlawdiagnosis.com/2026/02/eliminating-kickbacks-in-recovery-act-2025-updates-and-looking-to-2026/); [Mintz, Jan 2026](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments)). A flat-fee defense under EKRA does nothing against a per-se state brokering charge. [VERIFY Louisiana patient-brokering statute specifically.]

**5. 42 CFR Part 2 is a wholly separate landmine the flat fee never touches.** The "continuity" mechanic implies the app *transmits SUD patient information* to a treatment center. Part 2 restricts use/disclosure of SUD patient records and requires **patient consent** for disclosures ([42 CFR Part 2](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2)). If the app holds Part 2-protected records and shares them to enable continuity, you need a compliant consent and likely a QSOA/BAA — pricing structure is irrelevant. Improper disclosure is an independent violation regardless of EKRA.

### What it means for the venture plan (homegroups / detox-recovery continuity)

- **The flat-license claim is directionally correct but is being used as a shield it cannot be.** A *true* flat, fixed-dollar, per-seat-or-per-org SaaS license **decoupled from any patient flow** is the strongest defensible structure — but its safety comes from the *absence of referral mechanics and inducement intent*, not from the fee being flat. The moment the "continuity package" actually moves patients toward the paying center, "flat" stops protecting you.
- **Concrete guardrails to make the claim true:** (a) price strictly on org/seat/feature, never on patients, beds, or admissions; (b) the app must NOT deliver identified leads to paying centers — patient must independently choose any facility; (c) document that the fee reflects fair market value of software services, not referral value (FMV memo); (d) implement Schena-style policies governing any human "marketing" interaction to avoid undue-influence allegations ([Baker Donelson](https://www.bakerdonelson.com/ekras-application-to-marketing-arrangements-laboratories-and-other-providers)); (e) build Part 2-compliant consent flows before any record sharing; (f) check the **Louisiana** patient-brokering statute and the 5th Circuit posture, since the favorable Schena precedent is *not* controlling here. [VERIFY]
- **Risk rank confirmation:** this corroborates the v1 portfolio note that homegroups is "most ambitious, most dangerous." The continuity-package monetization is the single feature most likely to convert a benign SaaS into a criminal-exposure SaaS. It should be **gated behind specialized health-care counsel and probably an OIG-style structuring memo before launch**, not shipped on the assumption that "flat fee = safe."

**Bottom line:** Flat SaaS licensing is necessary but not sufficient for EKRA safety. The claim survives only if "continuity package" is genuinely software-for-money with no patient-steering and no Part 2 leakage. As a treatment-center-facing "continuity" *referral* product, a flat fee does **not** reliably escape EKRA/AKS/state brokering/Part 2 — it merely shifts the fight to the intent and patient-flow facts, in a circuit (5th) that has not adopted the defense-friendly reading.

Sources: [18 U.S.C. § 220](https://uscode.house.gov/view.xhtml?req=(title:18%20section:220%20edition:prelim)) · [Baker Donelson, "EKRA's Application to Marketing Arrangements," Aug 4 2025](https://www.bakerdonelson.com/ekras-application-to-marketing-arrangements-laboratories-and-other-providers) · [Health Law Diagnosis, "EKRA 2025 Updates," Feb 2026](https://www.healthlawdiagnosis.com/2026/02/eliminating-kickbacks-in-recovery-act-2025-updates-and-looking-to-2026/) (Schena, S&G Labs, Marchetti, Apollo Path, Patton, Simons, NJ P.L.2025 c.121) · [Stites & Harbison EKRA alert](https://www.stites.com/resources/client-alerts/providers-and-laboratories-beware-of-ekra/) · [Chapman Law Group, EKRA safe harbors](https://www.chapmanlawgroup.com/practice_areas/ekra-law-eliminating-kickbacks-in-recovery-act/) · [42 CFR Part 2 (eCFR)](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2) · [Mintz, "EKRA in 2025," Jan 13 2026](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-eliminating-kickbacks-recovery-act-2025-new-developments).

---

### Verdict — treatment incumbents displaceable by a solo founder

I have enough to render a verdict. The evidence strongly favors refutation of the broad claim.

---

# Adversarial Verification: "Treatment-software incumbents are weak enough that a solo AI-native founder could win a wedge"

## Verdict: REFUTED (as stated for the EHR core) / PARTIALLY-SUPPORTED (only for a narrow non-EHR adjacency)

The claim that incumbents are "weak enough" to displace is **refuted** for the EHR/clinical-system core. Kipu and Sunwave are not weak — they are consolidating, well-capitalized, and structurally moated. A solo founder cannot realistically win the EHR wedge. The claim survives only in a heavily narrowed form: a non-clinical adjacency that sits *beside* the EHR rather than trying to replace it — which is materially different from "displacing the incumbents."

## Strongest counter-evidence

**1. Kipu is a dominant, well-funded incumbent — not weak.**
- 6,000+ facilities, ~150,000 active users, 5M+ episodes of care/year, ~$108M total funding including a 2021 growth investment from TCV (the firm behind Netflix/Spotify). Described independently as the "undisputed market leader" and "gold standard." [ehrsource.com/vendors/kipu, 2026; prnewswire Discovery Behavioral Health release]
- Self-reinforcing network effect explicitly documented: centers pick Kipu *because* other centers use it — staff moving between facilities already know it, and referral partners/labs/clearinghouses are pre-integrated. That is a demand-side moat a solo founder cannot replicate. [ehrsource.com/vendors/kipu]

**2. The incumbents are actively consolidating — the window is closing, not opening.**
- Kipu acquired **Team Recovery Technologies** (patient engagement / alumni — "its largest deal yet," closed April 2026) and **Hatch Compliance** (compliance management). [bhbusiness.com, 2026-04-22; kipuhealth.com/news]
- **Sunwave merged with Lightning Step** and took a strategic growth investment from **BVP Forge** (plus existing investors Level Equity). [finance.yahoo.com, Sunwave/Lightning Step merger]
- Critically, Kipu's Team Recovery and Hatch buys mean the incumbent is *buying up exactly the adjacent wedges* (patient engagement, alumni programs, compliance) that an AI-native founder would target. The whitespace is being absorbed in real time.

**3. Switching cost / ecosystem lock-in is real and acknowledged even by Kipu's own reviewers.**
- "Ecosystem lock-in is a concern… all-in-one approach (EMR, billing, CRM, payments, prescribing) creates significant switching costs." EHR-to-EHR migration in healthcare is "near ubiquitous" but painful — patient record migration, historical data validation, clinical template reconfiguration, billing/payer setup. [ehrsource.com/vendors/kipu; PMC7657707 NIH on EHR transitions; valant.io on switching costs]
- Implementation alone runs **6–12 weeks single-site, 3–6+ months multi-site.** A center mid-stream on Kipu will not rip out its system of record for a solo founder's tool.

**4. Integration depth is the actual moat, not UI.** Kipu binds census → clinical documentation → per-diem billing → EPCS e-prescribing → eMAR → labs natively, so billing survives payer audits. Replicating that integration depth — not "being AI-native" — is the barrier. A solo founder cannot build EPCS-capable controlled-substance prescribing, ONC certification, and audit-grade RCM alone.

**5. Compliance is a capital and time barrier.** SUD software carries HIPAA + **42 CFR Part 2** + (for enterprise sales) HITRUST/SOC 2. HITRUST timelines are quoted at **6–12 months minimum, often 18–24 months**, with readiness-assessment fees before the audit even starts. [workstreet.com; insightassurance.com; complyjet.com] Enterprise treatment networks (e.g., Discovery Behavioral Health choosing Kipu as *exclusive* EMR) will not buy from an uncertified solo vendor.

## Where the claim survives (the only defensible version)
- Reviewers do note genuine incumbent *softness*: post-PE **support quality decline**, **dated UI**, **opaque quote-based pricing**, and **repeated sale-process churn risk** around Kipu in 2025–2026. [ehrsource.com/vendors/kipu] These are real seams.
- But these justify a **complementary, non-EHR wedge** (a tool that reads from / sits beside Kipu, not one that replaces it) — which is exactly the regroup thesis (sober-living operations, *not* clinical EHR). A solo founder competing on UI/support in a category the incumbent doesn't serve well is plausible; a solo founder displacing the system of record is not.

## What this means for the venture plan
1. **Kill any framing of "winning a wedge against Kipu/Sunwave" in the clinical/EHR layer.** That is refuted. regroup's strength is precisely that it targets *sober-living/Oxford House operations* — a segment Kipu's residential-clinical DNA underserves — and bills the *operator*, not the clinical center. Keep it there; do not drift toward EHR feature parity.
2. **The consolidation finding is a direct threat to homegroups and the recovery-platform adjacencies.** Kipu just bought Team Recovery (patient engagement/alumni) — the same space homegroups occupies. Treat "Kipu builds or buys this" as a live, near-term competitive risk, not a tail risk. This reinforces the v1 rank putting homegroups last.
3. **Integration/compliance reframed as the moat to *acquire*, not assume.** "AI-native solo founder" is not a moat against these incumbents. If pursuing regroup seriously, the defensible edge is the data/partnership assets already claimed (GPS meeting verification, 300K-meeting dataset, Oxford House World Services partnership) — none of which Kipu has. Those should carry the moat, and each needs independent verification [VERIFY: Oxford House partnership, dataset claims].
4. **Reinforces "sequence, don't parallelize."** The portfolio's #1 (CPA advisory income engine) does not touch this market and is unaffected. Fund from there; do not bet early capital on out-executing PE-backed, consolidating incumbents in their core.

**Bottom line:** Incumbents are strong and getting stronger via M&A. The realistic play is an *adjacency the incumbents underserve* (operator-side sober-living ops), defended by proprietary data/partnerships — not displacing the EHR core, and not relying on "AI-native solo founder" as the moat.

---

### Verdict — SWLA low-competition / warm-network revenue

I have enough to render a verdict. The single most damaging finding: Lake Charles had the highest out-migration rate of any US city in 2025. Synthesizing now.

## Adversarial Verdict: "SWLA is a low-competition AI/consulting market Marcus can win via his brother's network in 12-24 months"

**VERDICT: Partially supported — with one materially under-priced macro risk and an over-stated "blue ocean" framing.** The *low-competition* half is broadly true for net-new AI/automation work. The *meaningful revenue in 12-24 months* half is plausible **only** because it rides the warm CPA network, not because SWLA is a fertile market — and the local macro is actively deteriorating.

### 1. The strongest counter-evidence

**a) SWLA is a shrinking market, not a stable one. This is the headline refutation.**
- Lake Charles had **the single largest out-migration rate of any US city in 2025 — 5.3% — on a population of ~210,362** ([NOLA.com / The Advocate, 2025](https://www.facebook.com/NOLAnews/posts/1340207198135354/)). A market losing population faster than anywhere else in the country is the opposite of where you want a place-based service business.
- Calcasieu Parish is among the LA parishes **still declining** even as the state overall posted gains ([KPLC, Mar 2026](https://www.kplctv.com/2026/03/19/louisiana-sees-population-gains-second-straight-year-some-parishes-still-declining/)).
- The macro overhang is structural: back-to-back Hurricanes Laura/Delta (2020), then a freeze and flood, drove a multi-year "compounding disaster" recovery; SBA disaster lending topped **$300M** ([Cameron PJ / SBA](https://cameronpj.org/sba-to-open-business-recovery-center-in-lake-charles-to-help-businesses-impacted-by-hurricane-laura-sba-tops-300-million-in-disaster-assistance-loans/)), and **~50% of SWLA lives month-to-month** ([United Way of SWLA](https://unitedwayswla.org/hurricanes)). Louisiana statewide GDP grew only ~1.5% annualized over five years ([IBISWorld](https://www.ibisworld.com/united-states/economic-profiles/louisiana/)). The customer base is financially fragile and contracting.

**b) "Low competition" is real for AI specifically, but the adjacent IT spend is already locked up by entrenched MSPs.** Lake Charles has a deep bench of established managed-service providers — InfoTECH Solutions, Server At Work (SOC 2, downtown LC), Rapid I.T., SAVIT Solutions, plus statewide players (General Informatics, Puryear IT, In-Telecom) that cover SWLA ([Cortavo 2026 guide](https://cortavo.com/cortavo-guides/managed-it-services-in-lake-charles-la), [DesignRush LA MSPs](https://www.designrush.com/agency/managed-service-providers/louisiana), [Server At Work](https://www.saw.it/lake-charles)). These firms own the trusted-vendor relationship and budget line for "tech help," and several are actively repositioning into AI/security. They are the real competitor — not other AI consultants — because they'll cross-sell AI to clients Marcus would target.

**c) AI consulting in Louisiana is also less of a vacuum than implied.** New Orleans/Metairie already have positioned players — AutomateNexus claims "150+ Louisiana businesses" and "$50K+ saved" ([AutomateNexus Metairie](https://automatenexus.com/locations/louisiana/metairie)), plus Clutch-listed NOLA AI shops ([Clutch](https://clutch.co/developers/artificial-intelligence/louisiana)) and remote-national firms (Paro, Opinosis, Layer3Labs) that sell into SMBs everywhere for $5K–$75K engagements ([Layer3Labs](https://www.layer3labs.io/ai-consulting-for-small-business)). Geography is not a moat for AI work — it's delivered remotely — so "no local competition" overstates the defensibility. Notably, even the regional org **Alliance SWLA / LA.IO is running small-business AI focus groups** ([Facebook, AllianceSWLA](https://www.facebook.com/AllianceSWLA/posts/1219997603491034/)) — meaning institutional players are already moving to organize this exact demand.

**d) Demand-side caution: SMB AI adoption is shallow and price-sensitive.** SBA/BTOS data shows small-business AI use only rose from **6.3% to 8.8%** in six months — single digits ([USM Systems](https://usmsystems.com/small-business-ai-adoption-statistics/)). "96% plan to adopt" is intent, not budget. For a place where half the region is month-to-month, willingness to pay a consultant $4K–$7.5K (the recovery-platform B2B band) is the binding constraint, not awareness.

### 2. What genuinely supports the claim
- The thesis does **not actually rest on the SWLA market** — it rests on a **warm, concentrated channel**: the brother's ~20-person CPA firm with both a broad SWLA owner network and a captive client book. That bypasses the weakest part of any consulting business (CAC/cold trust), which the source docs admit is unquantified.
- The tailwind is real and independently sourced: **CAS/advisory revenue at accounting firms is expected to roughly double in three years** ([4impactdata](https://4impactdata.com/blog/scaling-client-advisory-services-with-ai-why-clarity-outperforms-hustle-for-cpa-firms/)), and solo AI advisors are credibly billing **$200–$500/hr** ([Digital Applied](https://www.digitalapplied.com/blog/ai-micro-consulting-premium-rates-solo-guide), [Layer3Labs $5K–$75K](https://www.layer3labs.io/ai-consulting-for-small-business)). A handful of warm referrals at those rates clears the v1 $90–120k target without needing market breadth. The income engine is channel-driven, not market-driven — and on that basis it is realistic.

### 3. What it means for the venture plan
- **Re-frame the thesis honestly:** this is a **warm-channel arbitrage**, not a low-competition geographic land-grab. The defensibility is the brother's trust and the CPA book — *not* the absence of competitors. Drop any "no local competition / blue ocean SWLA" language from the report; it won't survive diligence and it leads to the wrong strategy (geo-marketing instead of channel-deepening).
- **Treat the verbal revenue-share as the single largest risk.** The entire "income engine" leans on an unwritten advisory-line split with the brother in a declining local economy. Get it in writing before sequencing anything else.
- **Watch the macro as a hard ceiling.** A market with #1-in-nation out-migration and a fragile SMB base caps how far the *local* book scales. Mitigation: the same skill set sells remotely (like Paro/AutomateNexus do), and SDVOSB cert opens federal/out-of-region demand — so plan to **outgrow SWLA, not saturate it.**
- **De-risk demand assumptions:** validate willingness-to-pay with 3–5 actual paid CPA-client engagements before modeling Y2/Y3 ramps. Single-digit SMB AI adoption + month-to-month regional finances mean the funnel will be thin even with warm intros.
- **Reposition against MSPs, not AI shops.** The incumbents who will eat this lunch are the local MSPs cross-selling AI to their existing accounts. Marcus's edge is the CPA's financial-process intimacy (where MSPs are weak) — pitch *workflow/advisory automation tied to the books*, not generic "AI help," to avoid head-to-head with InfoTECH/Server At Work on their turf.

**Net:** The plan survives, but for a different reason than stated. It works *despite* the SWLA market (shrinking, fragile, adequately served on IT), purely *because of* the warm CPA channel. Bank the channel, paper the revenue-share, validate WTP, and architect for remote/federal expansion beyond a contracting region.

---
