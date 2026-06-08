# Research Plan — Venture Viability v2 (Monetization-Aware)

**Created:** 2026-06-07
**Owner:** Marcus
**Supersedes scope of:** `REPORT.md` (v1) — which assessed the A/B/C venture slate but did
**not** ingest the current monetization/GTM docs, the treatment-industry software/AI gap, the
recovery-app→treatment-center bridge, the brother's network beyond CPA firms, or McNeese.

This plan grounds every phase in docs already extracted (see Phase 0) and targets the five gaps
v1 left open. Phases are self-contained and run consecutively; each cites its inputs.

---

## Phase 0 — Documentation Grounding (DONE — captured below)

The three venture monetization corpora and the v1 research were read and extracted in full.
Canonical figures to carry forward (do **not** re-derive):

### detox-recovery = **Next Step Recovery** (nextsteprecovery.io)

- Non-clinical peer-navigation practice + digital products + B2B consulting + veteran pathway. Solo founder.
- Pricing: $50 support call (live) · $150 nav call (Q3'26) · $450 nav package (Q2'27) · $9.99–19.99 PDFs · **B2B $4k/engagement (range $1.5k–7.5k)** · $1.5k/mo retainer · $20/mo group sub · ~$30 VA Community Care session.
- Base projection: Y1 ~$18k · Y2 ~$56k · Y3 ~$139k. Profitable Month 3–4, **no external capital**.
- Capacity ceiling on calls ~$5,100/mo → B2B, digital, grants are the uncapped levers.
- **Existential risk:** non-clinical scope-of-practice framing (consult attorney Y1).
- Veteran pathway adds +$42k cumulative/3yr (VA PSS cert, VSO speaking, SAMHSA/Woodruff/Sinise grants).

### regroup = **B2B SaaS for sober-living / Oxford House management** (a.k.a. RATS)

- Operator pays, not resident. Recommended **Option 2 (Balanced)**: Traditional $69/$129/$249, Oxford $49/$89/$299 (chapter).
- Current pricing ~$20/mo captures only 1–2% of value delivered ($900–2,000/mo).
- Projection (recommended): Y1 ~$230k rev / breakeven · Y2 ~$864k (54% net) · Y3 ~$1.79M.
- **Second revenue stream:** Stripe payment processing on resident rent (+$132k→$528k/yr by Y3 at 60% adoption) — take-rate undefined.
- Moat claims: GPS meeting verification, 300K meetings dataset, **Oxford House World Services partnership**, claimed no direct competitor.
- **Doc inconsistency to resolve:** Option-2 ARR shows $315k (detail) vs $204k (summary table). Reconcile before relying.
- No CAC/LTV anywhere. Ecosystem links to detox-recovery/homegroups absent in these files.

### homegroups = **Peer-support app** (AA/NA/SMART tracking; referral engine)

- Freemium + Institutional B2B: Free / $4.99-mo or $39-yr Premium / $9.99-mo Group-Org / **$150–500/mo Institutional**.
- Role in flywheel: crisis/relapse users → Next Step Recovery; alumni tracking → treatment-center Institutional tier.
- v1 verdict: "most ambitious, most dangerous" (B2). **Do not start Year 1** — attention black hole, EKRA/42 CFR Part 2 exposure.

### v1 founder facts (locked)

- Tinnitus SC at **10% → already SDVOSB-eligible** (no minimum % required). Pursuing 50%+ separately.
- USAF F-15 crew chief 2009–13; senior SWE (Meta "Greatly Exceeds", YC, CGI Federal, ad-tech); CS in 3 yrs; autism + high EQ; lived recovery (10+ inpatient).
- In motion: AI/automation role at brother's ~20-person CPA firm, **$50k base + verbal** raise/revenue-share on advisory line (A3). Lake Charles, LA firm; New Orleans home base.
- v1 portfolio rank: **1. A3(+A1) advisory $90–120k · 2. B1 sober-living app · 3. B3 coaching · 4. SDVOSB cert · 5. A2 · 6. B2/homegroups.** "Sequence, don't parallelize. A funds B."

### NEW inputs (this session — user-supplied)

- **Brother's firm = TWK CPA Firm** (twk-cpafirm.com), Lake Charles. Stack: **Karbon (workflow) + SharePoint (docs) + Microsoft Teams (comms)**. A1 is already scoped: see `cpa-consulting/.../CPA_Firm_AI_Efficiency_Roadmap_Proposal.md` — 15 ranked initiatives, 4 phases, recommended first pilot = "Tax Season Intake & Workflow Automation" (engagement dashboard + doc intake + missing-item detection + follow-up drafts). Highest-revenue line is Bookkeeping Exception Review + Advisory Report Drafting (the A3 advisory hook).
- **Brother's network = BOTH broad+high-value AND accounting clients** — cross-industry SWLA owners with real budgets AND a concentrated CPA book. Treat as a warm B2B channel for productized AI/automation/software/consulting, not just accounting referrals.
- **McNeese (alumnus) angles to pursue:** (1) sell AI/automation/software/consulting to the university; (2) recovery/health-program partnership (nursing/counseling/campus recovery); (3) alumni credibility for regional BD; (4) **adjunct/associate professor — teach or pitch SWE/AI courses** (credibility + talent pipeline + recurring income).

### Five gaps v1 did NOT cover (this plan's targets)

1. Current monetization/GTM for the three ventures (no CAC/funnel/take-rate sizing).
2. Treatment-industry (rehab/outpatient) software & AI gaps — no incumbent teardown, no TAM.
3. Recovery-app → treatment-center bridge — named, never designed; EKRA-constrained.
4. Brother's network **beyond** CPA firms — wealthy Lake Charles business owners, low local tech competition.
5. McNeese University (alumni) channel — services, recovery/health programs, adjunct teaching.

---

## Phase 1 — Treatment-Industry Software & AI Gap (the central bet)

**Goal:** map what rehab/detox/outpatient (SUD) treatment centers actually buy, where incumbents are weak, and where an AI-native builder with lived + technical credibility can win.

**Tasks (copy the question framing, don't assume):**

- Incumbent teardown: Kipu, Sunwave, BestNotes, Ritten, Alleva, NextGen/behavioral, Lightning Step, CaredFor (aftercare), Sobriety Hub (sober-living, $75/staff user). For each: what it does, pricing if public, segment, and stated weaknesses (G2/Capterra complaints, review counts, last-meaningful-update signals).
- AI-adoption gap: where SUD/behavioral EHR + RCM + aftercare tooling lacks AI (intake automation, clinical note generation, utilization review/auth, census/occupancy prediction, relapse-risk, documentation compliance).
- Market sizing: # of US SUD treatment facilities (SAMHSA N-SSATS/NSUMHSS), outpatient vs residential split, behavioral-health IT spend, RCM denial-rate pain.
- Buyer & budget: who signs (owner/operator vs clinical director vs billing), willingness-to-pay, switching cost off an EHR.

**Verification:** every incumbent claim cited to a review platform or vendor page; every market number cited to SAMHSA or a named market report. Flag anything unverifiable as `[VERIFY]`.

**Anti-patterns:** do not assume a product gap exists because incumbents "look dated" — corroborate with review complaints. Do not size TAM from a single blog.

---

## Phase 2 — Recovery-App ↔ Treatment-Center Bridge (legally)

**Goal:** design the mechanism connecting homegroups/regroup/detox-recovery to treatment centers without tripping EKRA (§220, up to $200k + 10yr) or 42 CFR Part 2 (post Feb 2026 HIPAA-aligned breach rules).

**Tasks:**

- Map lawful models: SaaS-license-to-center (center pays flat, no per-referral) vs bill-families-direct vs grant-funded. Confirm which of regroup/homegroups Institutional tiers are EKRA-safe.
- Aftercare-continuity package: treatment center licenses homegroups for alumni tracking + regroup for sober-living placement as a **post-discharge product the center pays for** (not referral fees).
- Consent/data architecture under 42 CFR Part 2 + BAAs.

**Verification:** cite EKRA statute text + a healthcare-attorney secondary source; cite 42 CFR Part 2 Final Rule. Mark the "needs an attorney sign-off" line explicitly.

---

## Phase 3 — Monetization/GTM Stress-Test (the three ventures)

**Goal:** pressure-test the doc projections against external benchmarks; fill the missing CAC/LTV/take-rate.
**Tasks:** benchmark regroup's Option-2 ARR vs Sobriety Hub per-staff-user economics; size the Stripe rent-processing take-rate (typical 2.9%+30¢ → net spread); reconcile the $315k vs $204k discrepancy; sanity-check Next Step Recovery's organic-only funnel (4% lead-magnet, 35% fit→paid) vs published norms; verify EHR/SaaS B2B sales-cycle length for SMB behavioral health.
**Verification:** each benchmark cited; each doc number marked confirmed / optimistic / unsupported.

## Phase 4 — Brother's Network Beyond CPA + Local Tech Vacuum (Lake Charles / SWLA)

**Goal:** size the warm-channel opportunity the brother's relationships open beyond accounting clients.
**Tasks:** Lake Charles / SWLA economic base (LNG, petrochemical, healthcare, construction); count of mid-market firms ($5–50M rev) that buy custom AI/automation/software; local tech-services competition density; what "money business with little tech competition" actually buys (AI ops automation, internal tools, data/RCM). Frame A3 advisory as the delivery vehicle.
**Verification:** cite regional economic-development / Census County Business Patterns data for firm counts.

## Phase 5 — McNeese University Channel

**Goal:** find concrete alumni/partnership entry points across the four user-named angles.
**Tasks:**

- **Sell to the university:** McNeese IT/procurement, vendor onboarding, any AI/automation/admin-efficiency pilots; Louisiana higher-ed purchasing norms.
- **Recovery/health programs:** McNeese nursing, counseling/psychology, social-work, and any collegiate-recovery community — partnership/channel for the recovery apps or lived-experience programming.
- **Adjunct/associate professor:** McNeese Dept. of Computer Science / Engineering & Computer Science — adjunct hiring path, qualifications (MS typically required; industry-experience waivers?), pitching a SWE/AI course, typical adjunct pay, and the credibility + talent-pipeline value of the title.
- **Alumni + SBDC:** Louisiana SBDC at McNeese (client referrals to A3 advisory), alumni-business directory, entrepreneurship/veteran-services programs, any incubator/innovation hub.
  **Verification:** cite McNeese .edu pages, the CS/ECE department page, Louisiana SBDC, and any HR/adjunct posting.

## Phase 6 — Synthesis & Opportunities Not Yet Considered

**Goal:** integrate Phases 1–5 into a revised portfolio ranking + surface adjacent opportunities matched to the founder's edge (SDVOSB + AI + lived recovery + brother's network + military network).
**Deliverable:** update `REPORT.md` with a v2 verdict and a ranked, sequenced opportunity set; keep `research-findings.md` as the cited evidence ledger.
**Verification:** every recommendation traces to a phase finding; flag remaining `[VERIFY]`s and user-only facts (brother's network specifics, military network, McNeese contacts).

---

## Open questions only the user can answer

- Brother's network: **named** sectors/companies and how warm each intro actually is (breadth confirmed as broad+high-value AND accounting clients; specifics still needed for targeting).
- Specific McNeese contacts/alumni ties; whether he holds (or can earn) the credential an adjunct post requires.
- Military network composition (who, where, what they'd buy/refer).
- Treatment-center contacts already in the NOLA/Lake Charles recovery network.
