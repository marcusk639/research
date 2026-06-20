# Recovery SDVOSB Venture — Implementation Plan (Phase 0)

> Status: actionable plan · 2026-06-20 · Executes the hybrid recommendation from `COMPARISON-cpa-vs-recovery.md` and the sequencing from `REPORT.md` + `REPORT-procurement-validation.md`. Two parallel workstreams: **(A) the SDVOSB procurement moat** (long-pole paperwork, start now) and **(B) the first operator-tier product** (first revenue, direct-to-operator). Confidence labels carried from prior verified research.

## Operating principle

Run A and B **in parallel from day one**: A is mostly _passive waiting_ (certification clock), B is _active build/sell_. First revenue comes from B (HIPAA-only, no certification gate); A unlocks the higher-ceiling VA channel ~12–18 months out. Everything stays **flat-fee software, never referral-tied** (EKRA / _US v. Schena_). `[Verified]`

---

## Workstream A — The SDVOSB procurement moat (start the clock today)

**Why now:** VetCert is the long pole and its 2025–26 processing time is uncertain; the certification must be _complete_ before any sole-source/set-aside eligibility. Filing early costs almost nothing and runs in the background while B generates revenue. `[Verified]`

### A1 — Entity formation (gates everything; 1–2 weeks)

- [ ] Form the operating entity (LLC recommended for solo; confer with a tax pro re: S-corp election later).
- [ ] **Structure for the SDVOSB test up front:** Marcus must be **≥51% owner AND in control** (13 CFR 128.200/128.300) — sole owner/managing member satisfies both cleanly. Avoid any operating-agreement term that lets a non-veteran block ordinary decisions.
- [ ] EIN, business bank account, basic bookkeeping.

### A2 — Federal registration prerequisites (1–3 weeks, parallel)

- [ ] **SAM.gov** registration (free; get the UEI). Prerequisite to both VetCert and any federal award.
- [ ] Confirm/assign **NAICS codes**: primary **541511** (custom programming — the code the verified ~$5M SDVOSB mental-health-software award used), plus **541512** (systems design), **513210** (software publishing); check size standard (you qualify as small). `[Verified]`
- [ ] Pull the SBA size-standard self-cert.

### A3 — SBA VetCert (the long pole; start immediately after A1/A2)

- [ ] File **SBA VetCert** SDVOSB application (post-2023 the program lives at SBA, _not_ VA CVE / not 38 CFR part 74 / not VIP — those are outdated). `[Verified]`
- [ ] Gather documents: DD-214, VA service-connected disability letter, ownership/control evidence (operating agreement, cap table), SAM.gov UEI.
- [ ] **Verify current SBA processing time directly with SBA** — this is the single thinnest-sourced load-bearing fact in the research; do not bank a schedule on assumption. `[flag]`

### A4 — Lower-friction federal on-ramps (parallel, months 2–9; sidestep the prime+ATO wall)

- [ ] **SBIR/STTR scan** (VA + DoD) for SUD/behavioral-health AI topics — non-dilutive funding + credibility + an ATO path. Strongest solo on-ramp. _(Open item: confirm active topics, award sizes, timelines.)_ `[Inference]`
- [ ] **Identify IHT 2.0 / VA behavioral-health SDVOSB primes** to approach as a **subcontract AI partner** (the prime carries the ATO; you supply the module). _(Open item: can a sub earn revenue under the prime's ATO without its own?)_ `[Inference]`
- [ ] Defer full prime contracting + own-ATO (6–18 mo, FedRAMP not cleanly avoidable) until a reference deployment + SBIR/prime path exists. `[Verified]`

---

## Workstream B — First operator-tier product (first revenue)

### B1 — The wedge (chosen)

**AI Compliance & Outcomes Assistant for sober-living operators** — the operator tier _below_ the EMR, where funded EMR/scribe incumbents (Ritten/Alleva/Eleos) do **not** play. `[Verified: the open differentiation crack]`

- **Buyer:** sober-living / recovery-residence operators (the RATS buyer that genuinely pays). EKRA-safe: flat-fee software to the operator, zero referral remuneration. `[Verified]`
- **The pain (acute, recurring, fundable):** operators must document resident check-ins, incidents, drug-test logs, and house-rule compliance **and** produce **outcome reports** for NARR certification, funders, and referral partners — today done by hand in spreadsheets. This is the unglamorous, high-frequency burden AI removes.
- **Why AI wins here specifically:** it turns unstructured check-in notes / incident logs into structured compliance records and auto-drafts the periodic outcome/occupancy reports operators currently dread — a documentation-automation job, not a clinical/diagnostic one (keeps it out of FDA SaMD and §-criminal territory).
- **Founder edge that matters:** lived-recovery credibility with operators (warm, trust-based sales at ~$0 CAC) + AI specialty (the product) + the existing codebase (speed).

### B2 — MVP scope (the data model already exists — this is an AI _layer_, not a new platform)

**Key finding (verified against the code):** regroup already models the entire spine — `House`, `Guest`, `Phase`, `Room`, `DrugTest`, `Meeting` (AA/NA attendance), `Chore`, `StaffNote`, `Complaint`, `Issue`, an `activities` event collection with `week-summaries` rollups, and `OperatorSubscription` + Stripe per-house/per-guest billing. So the MVP is **the thin AI/reporting layer that monetizes the data regroup already collects** — not a platform build. `[Verified: regroup/functions/src/entities, mobile/src/entities, firestore-data-model.md]`

**Component 1 — Outcome & Occupancy Report Generator (the headline; build FIRST).** One-click, NARR/funder-ready report (per house, per period) from existing data: `Guest` move-in/out → length-of-stay; `Phase` → completion/progression; `DrugTest` → compliance; `Meeting` → attendance; `activities`/`week-summaries` → engagement; `House`/`Room` → occupancy. LLM writes the narrative summary. _Pure read + aggregate + LLM-narrative — no new write paths._

**Component 2 — AI staff-note structuring.** LLM reads free-text `StaffNote`/`Complaint`/`Issue` → extracts structured fields (incident type, residents, rule violated, follow-up) + flags compliance items, writing back into the existing activity/issue model. Cuts manual logging; feeds clean data into Component 1.

**Component 3 — Compliance dashboard.** Per-house operator view over existing data: overdue drug tests, missed check-ins/meetings, phase status, open incidents.

**Slice 1 (smallest shippable, build this first):** Component 1 over existing data, **one house, in the Angular web portal** — the buyer-facing "wow," zero new write paths or mobile work, and it produces the outcomes-proof artifact that anchors both operator sales and the VA/SBIR story.

**Billing:** reuse existing `OperatorSubscription`/Stripe — gate AI reports behind a subscription tier.

**Explicitly OUT of scope (de-risk):** anything clinical/diagnostic (FDA), any referral-to-treatment routing or referral-tied remuneration (EKRA), any PHI to external AI without a HIPAA-compliant/BAA path. `[Verified red lines]`

**One real dependency to validate first:** the report is only as good as the data operators actually enter. Confirm with the design-partner operator that `DrugTest`/`Meeting`/`Phase`/move-in-out are _actually populated_ in practice; if sparse, Slice 1 shifts toward making capture frictionless before reporting on it.

### B3 — Compliance posture (build it in, not bolt-on)

- [ ] **HIPAA**: BAA with any LLM/cloud vendor that touches resident PHI; PHI-safe logging (the recovery-platform CLAUDE.md already mandates "never log PII"). `[Verified in-repo rule]`
- [ ] **42 CFR Part 2**: sober-living _operations_ data is lower-exposure than clinical SUD records, but treat resident identifiers as sensitive; _do not_ market Part 2 segmentation as the product's moat (that differentiator was refuted in research). `[Verified refutation]`
- [ ] **EKRA**: pricing is a flat operator subscription only. No per-resident-referral fees, ever. `[Verified]`

### B4 — Pricing & first-revenue motion

- [ ] **Flat operator SaaS subscription**, per-house or per-bed tier (validate ACV; prior research flags operator SaaS sells in weeks-to-months, ACVs modest). `[Estimate — validate]`
- [ ] **Land 1–2 design-partner operators** from the warm lived-recovery network (free/discounted pilot → reference + outcomes evidence). CAC ≈ $0.
- [ ] Goal: first paid operator within **the first build window**; use pilots to produce the outcomes-report proof that later anchors both wider operator sales **and** the VA/SBIR story.

---

## Near-term sequence (first ~90 days) & the traction gate

| Window         | Workstream A (moat)                                    | Workstream B (product)                                                       |
| -------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Weeks 0–2**  | Form entity (51% owned+controlled); EIN/bank           | Confirm wedge with 2–3 operators; finalize MVP scope vs RATS code            |
| **Weeks 2–6**  | SAM.gov + NAICS; **file VetCert**; verify SBA timeline | Build MVP slice 1: check-in/compliance log + census on RATS                  |
| **Months 2–3** | SBIR topic scan; map SDVOSB primes                     | Build the **auto-outcome-report** feature; sign 1–2 design-partner operators |
| **Months 3–9** | Pursue SBIR / prime-sub conversations                  | Convert design partners to paid; iterate; gather outcomes proof              |

**12–18 month traction gate** (from `COMPARISON`): if by then there are **paying operators + (an SBIR award OR a credible VA/sub path)** → shift weight to this venture as the primary wealth vehicle. If still near $0 with no signal → the CPA consulting practice is the proven fallback; keep this lean. `[Inference]`

---

## Open items to resolve (cheap validation before heavy build)

- [ ] SBA VetCert current processing time (call SBA). `[load-bearing]`
- [ ] Active VA/DoD SBIR/STTR SUD-AI topics + award sizes/timelines.
- [ ] Operator SaaS realistic ACV + sales-cycle length (ask the 2–3 design-partner operators directly).
- [ ] Whether a software sub earns revenue under a prime's ATO without its own.

## Cross-references

- `REPORT.md` (wedge ranking + #1 rationale) · `REPORT-procurement-validation.md` (VA gates, on-ramps) · `COMPARISON-cpa-vs-recovery.md` (hybrid + traction gate) · code: `~/dev/recovery-platform/regroup` (RATS), `recovery-api`.
