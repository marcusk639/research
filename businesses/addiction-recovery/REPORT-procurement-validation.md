# VA-Procurement Wedge — Validation of the Two Gating Questions

> Status: draft · 2026-06-20 · Evidence base: deep-research pass `wf_4d7a1aea-cfa` (105 agents, ~5.18M tokens, 23 sources, 25 claims verified → 21 confirmed / 4 killed). Companion to `REPORT.md`. Confidence: `[Verified]` · `[Inference]` · `[Estimate]` · `[Time-sensitive]`.

## Why this pass exists

`REPORT.md` concluded the founder's durable moat is the **SDVOSB "Veterans First" procurement preference** layered on AI back-office tooling, but flagged two open questions that gate the whole call. This pass answers them.

---

## Q1 — Is VA demand REAL or theoretical? → **REAL, with a specific proof point.** `[Verified]`

**The SDVOSB channel is large and the buying pattern for behavioral-health software exists:**

- **Channel size:** In FY2024 the VA awarded **$10.2B (23% of total prime dollars)** to SDVOSBs, **$8.4B (19.54%) via set-asides** — VA exceeds its own SDVOSB goals by a wide margin. ([VA OSDBU](https://www.va.gov/osdbu/programs/Empowering_Veteran-Owned_Business_Success.asp)) `[Verified, 3-0]`
- **The decisive software-specific proof:** SDVOSB **USVETSERV LLC** won a **~$5.0M ($4,999,203) sole-source** VA award under **NAICS 541511 (custom programming)** for **mental-health technology**, awarded via the §8127(c) sole-source authority. This is the existence proof that VA buys behavioral-health _software_ from a solo-scale SDVOSB at the sole-source ceiling. ([HigherGov Award 36C10X22P0109](https://www.govconwire.com/); [38 U.S.C. 8127](https://www.law.cornell.edu/uscode/text/38/8127); [GovForum](https://www.insights.govforum.io/2022/11/va-awards-targeted-mental-health-therapy-contract/)) `[Verified, 2-1 on labeling nuance]`
- **Favorable mechanics:** The **Rule of Two is mandatory** (Kingdomware) and **applies to multiple-award IDIQs** procurement-wide (GAO _Spur Design_ B-412245.3); **sole-source up to $5M** is authorized by **VAAR 819.7008**. ([smallgovcon](https://smallgovcon.com/gaobidprotests/va-rule-of-two-applies-to-multiple-award-idiqs/); [VAAR 819.7008](https://www.acquisition.gov/vaar/819.7008-sole-source-awards-verified-service-disabled-veteran-owned-small-businesses.)) `[Verified, 3-0]`
- **Big vehicle, but not for a solo prime:** VHA **IHT 2.0** is a **10-year, $14B-ceiling** multiple-award IDIQ whose scope explicitly includes health IT — but it went to **9 established SDVOSB primes**. A solo founder **cannot realistically prime** this; it is a _subcontracting_ target, not a direct path. ([GovConWire](https://www.govconwire.com/articles/va-vha-iht-2-contract-award-sdvosb)) `[Verified, 3-0]`

**Important correction (refuted claims — do not rely on these):**

- The notion that VA medical centers _routinely_ set aside software-NAICS clinical-content procurements was **refuted (1-2)**; one Minneapolis "809 SDVOSBs identified" framing was **refuted (0-3)** — **SDVOSB headcount does not equal capture.** In that very example the VA **sole-sourced to WebMD Ignite despite 809 eligible SDVOSBs.** Being certified gets you eligibility, not the award. `[Verified refutation]`

**Read on Q1:** Demand is real and proven at the ~$5M sole-source scale, but it rests on a _handful_ of concrete data points (the USVETSERV award + IHT 2.0 scope), not a deep catalog of SUD-software solicitations. Treat VA demand as **real but lumpy and relationship-driven**, not a dependable open pipeline you can count on quarter-to-quarter. `[Inference, high]`

---

## Q2 — Time-to-first-revenue: VA channel vs. direct-to-operator → **Operator is faster; VA is the slower structural-moat track.** `[Verified gates / Inference verdict]`

**The VA channel has two hard gates in series:**

- **Gate 1 — SBA VetCert (certification before eligibility).** Must be **51% owned _and controlled_** by the service-disabled veteran (13 CFR 128.200/128.300), and **a firm not listed/certified will not even have its offer considered** (VAAR 852.219-73(b)(1)). Certification is a prerequisite, and its **2025–2026 processing time is the thinnest-sourced load-bearing item** — verify current SBA timelines directly. Note the **38 CFR part 74 / VIP** framing is **outdated** — certification moved to **SBA VetCert (13 CFR 128)**. ([eCFR 13 CFR 128](https://www.ecfr.gov/current/title-13/chapter-I/part-128); [VAAR 852.219-73](https://www.acquisition.gov/vaar/852.219-73)) `[Verified, 3-0][Time-sensitive]`
- **Gate 2 — VA ATO (the real barrier for software touching VA systems/PHI).** Federal **ATO typically takes 6–18 months**; the **60-day initial-ATO target** in the Sept-2025 VA AI compliance plan (M-25-21) applies **only to scoped, sponsored pilots**, is self-reported, and has no published spec/audit. **Full FedRAMP is _not_ cleanly avoidable** — the "inherit VAEC controls, skip FedRAMP" shortcut was **refuted (1-2)**. ([VA M-25-21](https://department.va.gov/ai/department-of-veterans-affairs-compliance-plan-for-omb-memorandum-m-25-21/); [Fed News Network](https://federalnewsnetwork.com/federal-insights/2022/09/vas-enterprise-cloud-office-streamlines-ato-process/)) `[Verified, 3-0; shortcut refuted]`

**Net timing:** Direct-to-operator SaaS (private sober-living / SUD operators) carries **no certification and HIPAA-only** burden, so it **reaches first dollar materially faster**; the **VA track is floored at ~12–18+ months** once VetCert + ATO are stacked. (The operator-speed advantage is _reasoned inference_, not benchmarked — operator SaaS sales cycles still run weeks-to-months.) `[Inference, med-high]`

**Lower-friction federal on-ramps for a solo (use these instead of priming):**

- **Subcontract to an established SDVOSB/IHT 2.0 prime** — the prime carries the ATO and past performance; you supply the AI module. _(Open question: confirm whether a sub can earn revenue under the prime's ATO without its own.)_ `[Inference]`
- **SBIR/STTR (VA or DoD)** — **non-dilutive funding + credibility + a past-performance record**, well-suited to an AI/SUD product and to a solo technical founder. Strongest standalone on-ramp. `[Inference]`
- GSA Schedule / VA T4NG-type vehicles as later steps. `[Inference]`

---

## Decisive read

**The VA-procurement moat is REAL and reachable in a 12–18+ month horizon — but it is gated (VetCert → ATO) and lumpy, so it is the _slower parallel track_, not the first-revenue path.** Run **direct-to-operator now** for first dollars and reference customers, and start the VA gates in parallel so the structural moat is ready when the product is proven.

**Sequenced recommendation:**

1. **Now (weeks 0–8):** form the entity correctly for **51% veteran ownership _and control_** and **file SBA VetCert** (Gate 1 — start immediately; it's the long pole and the timeline is uncertain). In parallel, register **SAM.gov**.
2. **Months 0–4:** sell the operator-tier AI tool to **private sober-living/SUD operators** (HIPAA-only, no certification) — first revenue + outcomes evidence + the past-performance story.
3. **Months 2–9:** pursue **VA/DoD SBIR/STTR** for the SUD AI tooling (non-dilutive capital + credibility + a path to an ATO'd deployment) and **introduce yourself to IHT 2.0 SDVOSB primes** as a subcontract AI partner — both sidestep the solo-prime + ATO barrier.
4. **Months 9–18+:** once VetCert is in hand, a reference deployment exists, and (via SBIR or a prime) an ATO path is real, pursue **SDVOSB set-aside / sole-source** VA work directly.
5. **Throughout:** keep every structure **flat-fee software** — never referral-tied (EKRA, _Schena_).

---

## Residual open questions (verify before committing capital)

- **SBA VetCert processing time in 2025–2026** and what delays it (thinnest-sourced load-bearing fact).
- For a **software sub under an SDVOSB/IHT 2.0 prime**, who carries the ATO — and can the sub earn revenue **without its own** ATO?
- **Active/forecasted VA or DoD SBIR/STTR topics** for SUD/behavioral-health AI, with award sizes and timelines.
- Realistic **operator SaaS sales-cycle length and ACV** for sober-living/SUD operators vs. the VA track.

## Sources

- VA OSDBU FY2024 SDVOSB performance: https://www.va.gov/osdbu/programs/Empowering_Veteran-Owned_Business_Success.asp
- 38 U.S.C. 8127 (Veterans First / sole-source authority): https://www.law.cornell.edu/uscode/text/38/8127
- VAAR 819.7008 (sole-source up to $5M): https://www.acquisition.gov/vaar/819.7008-sole-source-awards-verified-service-disabled-veteran-owned-small-businesses.
- VAAR 852.219-73 (set-aside notice; must be certified): https://www.acquisition.gov/vaar/852.219-73
- SBA VetCert / 13 CFR 128 (ownership _and control_): https://www.ecfr.gov/current/title-13/chapter-I/part-128
- VA IHT 2.0 ($14B, 9 SDVOSB primes, health IT): https://www.govconwire.com/articles/va-vha-iht-2-contract-award-sdvosb
- VA mental-health-tech SDVOSB award (context): https://www.insights.govforum.io/2022/11/va-awards-targeted-mental-health-therapy-contract/
- Rule of Two applies to IDIQs (GAO _Spur Design_): https://smallgovcon.com/gaobidprotests/va-rule-of-two-applies-to-multiple-award-idiqs/
- VA AI compliance plan / M-25-21 (60-day pilot ATO target): https://department.va.gov/ai/department-of-veterans-affairs-compliance-plan-for-omb-memorandum-m-25-21/
- VA ATO process / VAEC (FedRAMP not fully avoidable): https://federalnewsnetwork.com/federal-insights/2022/09/vas-enterprise-cloud-office-streamlines-ato-process/ · https://www.oit.va.gov/services/cloud-software/saas/playbook
- SDVOSB 2026 VetCert changes: https://iquasar.com/blog/sdvosb-program-changes-2026-how-the-vetcert-reset-is-reshaping-federal-contracting/
