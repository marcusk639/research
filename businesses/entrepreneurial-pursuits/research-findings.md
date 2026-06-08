# Verified Research Findings — Evidence Ledger

> Source: deep-research harness run (107 agents, 25 sources fetched, 116 claims
> extracted, 25 adversarially verified via 3-vote, **0 killed**). Verified 2026-06-07.
> Confidence below is the harness's, with framing caveats preserved. These are the
> evidence base for `REPORT.md`; every figure there traces here or to
> `~/dev/cpa-consulting`.

## Finding 1 — CAS is the fastest-growing, highest-margin accounting segment (HIGH, 3-0)

2024 AICPA/CPA.com CAS Benchmark Survey (2023 data, ~206 self-selected CAS firms):

- **17% median CAS growth** (15% top performers); 99% three-year growth projection;
  vs. ~9.11% median firm net-client-fee growth in the 2023 AICPA MAP survey.
- **50% median CAS margin** (55.5% top performers) — **explicitly before partner
  compensation** (i.e., NOT net profit).
- Firms with significant CFO/advisory revenue earn **>30% higher MRR** than
  transactional-heavy firms.
- Sources: cpa.com CAS Benchmark 2024 (primary).
- **Caveat:** self-selected survey of firms already succeeding at CAS → **treat as a
  ceiling, not expected value; apply a conversion haircut** for the brother's firm.

## Finding 2 — CAS revenue-per-professional benchmark (HIGH, 3-0)

- **NCFPP $156,250 median** (+29% over the 2022 survey, ~2-yr span); **$248,646 top
  performers**; **$181,440 for tech-strong firms** (who also serve ~100 clients median).
- The tech-investment linkage ($181,440) directly supports the automation-as-value
  thesis for A1/A3. NCFPP is revenue/FTE, not margin.

## Finding 3 — Incumbent sober-living software prices per seat, not per bed (HIGH, 3-0)

Sobriety Hub (current 2026 vendor page):

- **$75/mo per Full Staff User** ($65 annual); **$25/mo per Client Manager User**;
  resident app **free**; **$250 one-time onboarding**; optional **$200/mo Pro tier**;
  **month-to-month, no contract**. Verbatim: "You pay only for staff users, not per
  resident or per house."
- **Implication for B1:** operators expect per-seat, low-commitment, cancel-anytime
  SaaS. This **caps B1 monetization** — no per-bed upside; small homes = 1–3 seats.

## Finding 4 — 42 CFR Part 2 Final Rule imports HIPAA obligations onto SUD data (HIGH, 3-0)

- 2024 Final Rule; **compliance deadline Feb 16, 2026 (now PAST)**. Applies the **HIPAA
  Breach Notification Rule** to Part 2 records (60-day notice); **BAA obligations attach**.
- Eases consent: **single patient consent for all future TPO** uses; HIPAA CEs/BAs may
  redisclose per HIPAA (except in proceedings against the patient); counseling notes
  keep stricter consent.
- Source: HHS fact sheet (primary).
- **Implication for B2:** any product touching **treatment-center SUD data** must
  **already be compliant** (HIPAA-grade breach controls, BAAs) — a real cost/burden for
  a solo founder. **Sober-living and 12-step group data outside Part 2 scope are lighter.**

## Finding 5 — EKRA criminally bars referral remuneration in recovery (HIGH, 3-0)

- 18 U.S.C. §220: bars soliciting/receiving **OR** paying/offering any remuneration
  (kickback/bribe/rebate; direct or indirect, cash or in-kind) for referring a patient
  to a **recovery home, treatment facility, or lab** for services covered by a health
  care benefit program in interstate commerce. **Up to $200,000 + 10 years per
  occurrence.** "Knowingly and willfully" scienter.
- Source: Cornell LII (primary statute).
- **Implication for B3:** **never accept facility-side referral payment.** Lawful path =
  **bill families/clients directly** for coaching. Enforcement is active since 2018.

## Finding 6 — SBA VetCert is now fast and low-friction (HIGH, 3-0)

- **≥51% veteran ownership** (13 CFR 128.202, direct + unconditional); processing **~12
  days (Nov 2025)**, down from 81 days; backlog cleared. Mandatory gateway to set-asides
  since self-certification was eliminated **Dec 22, 2024**.
- Sources: SBA (primary).
- **Caveat:** 12-day figure is a celebratory post-backlog snapshot; durability unproven.
- **Note added in synthesis:** SDVOSB eligibility requires a **service-connected
  disability with no statutory minimum percentage** — so the 10% tinnitus rating likely
  **already qualifies** him; the 50%+ rating drives disability _income/healthcare_, not
  SDVOSB status. **[VERIFY] but materially accelerates Track C.**

## Finding 7 — Federal/VA set-aside leverage is substantial but long-dated (HIGH, 3-0 / 7% 2-1)

- **≥5% government-wide SDVOSB goal** (raised from 3%, FY2024 NDAA; FY2025 actual
  ~4.7%, missed). **VA ≥7%** for certified VOSBs/SDVOSBs. **Mandatory Rule of Two**
  (Kingdomware v. US, 2016 — "shall" is mandatory). SDVOSB-first priority. **$5M
  sole-source** ceiling ($8.5M manufacturing).
- Sources: VAAR 819.70, SBA portal, CRS, GAO (primary/secondary).
- **Caveat:** goals are aspirational targets, not reservations; **first awards typically
  12–24+ months out** → long-dated option, not near-term income.

## Finding 8 — Documented VA demand for external digital mental-health tech (HIGH, 3-0)

- VA **Mission Daybreak $20M** grand challenge (launched May 2022): 1,300+ submissions,
  ~$11.5M to winners; **9 of 10 winners were digital/software** (NeuroFlow, Battle Buddy,
  Televeda, ReflexAI, Even Health Cabana VR, OxfordVR, etc.).
- Source: VA press release (primary).
- **Caveat:** framed as suicide-prevention/**mental-health broadly, not SUD
  specifically**; one challenge's winner mix ≠ standing procurement priority. Supports a
  **hedged** "VA buys external behavioral-health software" inference for positioning B2.

## Base rates (for probability adjustments)

- **Digital transformation: ~30% success / ~70% failure** (study of 900 transformations)
  → A1 internal-automation value-capture base rate.
- **B2B SaaS / two-sided marketplace cold-start** (chicken-and-egg) is the dominant
  failure mode → B1/B2; the founder's warm network is the specific mitigant.

## Open questions the research could NOT resolve (gate the conclusions)

1. **Brother's firm revenue, realized blended rate (~$150–200/hr?), and the verbal
   profit-share terms** — gates the entire A income model. HIGH sensitivity.
2. **Founder's final VA rating + timing** — and whether SDVOSB is already available at
   10% (likely yes). MEDIUM; accelerates C if confirmed.
3. **Treatment-center budgets / willingness-to-pay for aftercare (B2)** — must be weighed
   against Part 2 compliance cost. HIGH sensitivity for B2.
4. **Realistic Part 2 compliance cost/timeline for a solo-built B2 product** — may exceed
   near-term B2 revenue given lean operator budgets. HIGH sensitivity for B2.
