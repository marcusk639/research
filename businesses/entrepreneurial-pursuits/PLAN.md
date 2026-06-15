# Execution Plan of Record — Entrepreneurial Portfolio

**Owner:** Marcus · **Created:** 2026-06-08 · **Horizon:** 0–24 months
**Derived from:** `REPORT.md` v2 §8 (ranking & sequencing) + §9 (open questions).
**Evidence:** `research-dossier-v2.md`. **History:** `archive/PLAN-research-v2.md` (the
research plan that produced the v2 report), `archive/REPORT-v1.md`.

> **The one rule:** sequence, don't parallelize — **the CPA engine funds everything else.**
> The binding constraint is **Marcus's delivery hours**, not demand. Every new track
> competes for the same time; this plan exists to stop parallelization from starving #1.
>
> **The single highest-leverage action in the entire plan:** _paper the verbal TWK
> revenue-share_ (Decision D1 + Task in Track 1). Until that is in writing, the income
> engine that funds the whole portfolio is an unmanaged risk.

---

## Decisions to Resolve (gate the plan — only Marcus can answer)

Each maps to `REPORT.md` §9. Resolve the **🔴 blockers** before the work they gate.

| ID    | Decision                                                                                 | Gates                            | Status                                                                                                  |
| ----- | ---------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 🔴 D1 | Will the TWK advisory revenue-share be papered, and on what split?                       | Track 1 (whole engine)           | IN PROGRESS — Marcus + brother meeting to decide split; not yet papered                                 |
| 🔴 D2 | Real weekly hours available beyond the $50k TWK base role?                               | every track's pace               | ANSWERED (yes) — now split into two numbers; see **Execution Capacity** below. Both counts still [set]  |
| D3    | Does the Oxford House World Services partnership exist **in writing**, exclusive?        | Track 3 (regroup)                | OPEN                                                                                                    |
| 🔴 D4 | Willing to fund a healthcare-regulatory attorney before any treatment-center revenue?    | Track 4, Track 9                 | CONDITIONAL — yes _iff_ Track 4 treatment-center revenue proves realistic; gated on that WTP validation |
| D5    | Appetite for federal-contracting overhead (SAM, compliance, slow cycles)?                | Track 5 rank                     | OPEN                                                                                                    |
| D6    | Will the brother **actively co-sell** (the one-sentence audit pitch) or just give names? | Track 1 ceiling ($120k vs $200k) | OPEN                                                                                                    |
| D7    | Is SDVOSB paperwork (rating docs, SAM/VetCert) actually in hand?                         | Track 5, Track 7                 | OPEN                                                                                                    |
| D8    | Risk tolerance for recovery-venture scope-of-practice / EKRA exposure?                   | Tracks 4, 6, 9                   | OPEN                                                                                                    |

---

## Execution Capacity & Automation (reframes D2)

**The setup:** two Macs — an M4 Pro (48GB) workhorse + an M5 Air (24GB) runner,
SSH-linked for dual control — running parallel Claude Code / Hermes agent workflows,
with each project automated toward an autonomous loop "to the extent possible."

**Why this changes D2 but does not dissolve it.** The plan's binding constraint
(lines 8–9) was always Marcus's _irreplaceable_ hours, not raw throughput. An agent
fleet adds throughput, so D2 is no longer one number — it is **two**:

| Capacity bucket                       | What it covers                                                                                                               | Automatable?                        | Gates                                                            |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| **C1 — Non-automatable client hours** | Discovery calls, advisory judgment, the brother co-sell relationship, regulatory-sensitive calls (§7216, EKRA), TWK delivery | **No** — this is the real ceiling   | Track 1 retainer ceiling ($120k↔$200k), all client-facing pace   |
| **C2 — Agent-supervised hours**       | Prompting, reviewing, course-correcting, integrating autonomous workflows; building/maintaining the fleet                    | Partially — supervision ≠ zero cost | The parallel low-effort tracks (5/7, 8, 7b) + Track 1 collateral |

**The number that still gates the plan is C1.** Two machines add zero C1 hours —
they can't take a client call or own the brother relationship. So the retainer
ceiling (lines 85–86) and the contractor-hire trigger (lines 117–119) are still
priced in C1, unchanged.

**What the fleet genuinely buys: leverage on C2 work.** Good fit for the tracks the
plan already tags _parallel, low-effort_ — content engine (7b), SDVOSB paperwork
drafting (5/7), McNeese outreach drafts (8), validation research — and, highest-value,
**Track 1's own automatable deliverables** (the TWK reference automation, the
before/after audit collateral, diagnostic deliverables).

**Two guardrails (load-bearing):**

1. **Point the fleet _at_ Track 1, not away from it.** Tracks 3/4/6/9 are
   validate-only / gated / deferred (lines 94–125). Pouring even _automated_
   engineering into them builds what the plan says not to build yet. Highest leverage
   is accelerating Track 1's collateral, not spreading the fleet across deferred bets.
2. **"Autonomous" is not "free" — supervision is paid in C2, which competes with C1.**
   Managing a fleet across many projects can become its own time sink that starves the
   CPA engine — the exact failure mode "sequence, don't parallelize" (line 8) exists to
   prevent. Automation lowers a parallel track's _marginal_ cost; it does not zero it.

**Security gate (TWK = real financial PII):** an SSH-linked, multi-machine,
autonomous-agent setup over §7216-covered client data is a live exposure (data
governance was load-bearing in the back-office offer). Sandbox the agents, scope their
filesystem/network permissions, and keep client data off any box running unattended
workflows.

**Net:** the two-machine fleet is a force-multiplier on **C2** and on Track 1's
automatable collateral — treat it as _how the parallel tracks get executed cheaply_,
not as permission to violate sequence-don't-parallelize. The plan still owes a **C1
number** (non-automatable client hours/week) before it can pace anything.

---

## Phase 1 — Months 0–6: Stand up the income engine

**Theme:** ship proof inside TWK, paper the deal, convert the warm channel to first retainers.
**Success = first 2–3 advisory retainers signed + revenue-share in writing.**

### Track 1 — CPA advisory/automation engine (RANK 1) — _primary focus_

- [ ] **Paper the verbal revenue-share** (D1). Written split, what counts as attributable
      revenue, review cadence, separate from $50k base. **Do this first.**
- [ ] **Capture TWK baseline metrics** (week 1) before changing anything: document-chase
      hours, blocked engagements, extension rate, time-to-ready-for-prep.
- [ ] **§7216 data-path gate (pre-build, blocking):** confirm the automation processes
      taxpayer return information **inside the firm's existing M365 tenant**; do NOT pipe
      client docs to an external LLM API unless the firm signs off and the architecture
      qualifies under §7216's auxiliary-service-provider exception. Resolve the data path
      _before_ writing code, not after.
- [ ] **Ship the first TWK automation — narrowed wedge (not the full 5-part bundle):**
      **Missing-Item Detection + Client Follow-Up Draft Generator, scoped to individual
      1040s**, draft-only with human approval, on the existing SharePoint + Karbon. Chosen
      because it removes the staff's #1 daily drudgery (so adoption is _pull, not push_), needs
      no accounting-system integration, and is shippable solo inside the C1 ceiling. Source:
      `~/dev/cpa-consulting/docs/CPA_Firm_AI_Efficiency_Roadmap_Proposal.md` (initiatives #2 + #3).
- [ ] **Fast-follow (not first):** the **engagement dashboard** (roadmap exec-priority #1) is
      the strategic backbone but its value accrues to partners, not line staff — weaker first
      adoption. Let a thin "what's blocked" view fall out of the wedge above; build the full
      dashboard only after the wedge earns trust.
- [ ] **Produce one shareable before/after result** by Day 60 ("40 blocked engagements → 12").
- [ ] **Launch the A3 advisory line:** the "AI Back-Office Audit + Automation Sprint" ladder
      ($2.5–5k diagnostic → $6–15k sprint → $3–5k/mo retainer). Highest-revenue hook =
      Bookkeeping Exception Review + Advisory Report Drafting.
- [ ] **Brother co-sells 3–5 client audits** (D6) — one-sentence intro to the CPA book.
- **Advance trigger:** first paid advisory engagement. **Kill/pivot:** zero advisory
  traction by Month 12 → treat TWK as an internal ops job, reassess.

### Track 5/7 — SDVOSB (RANK 5 + 7, cross-cutting) — _parallel, low-effort_

- [ ] Confirm SDVOSB paperwork in hand (D7); **register SAM.gov + complete SBA VetCert**
      (~12-day processing). Stack the LED Veteran Initiative / Hudson cert (free; not a
      hard set-aside — don't overweight).

### Track 8 — McNeese credibility flywheel (RANK 8) — _parallel, low-effort_

- [ ] Email **Dr. Srinivasan Ambatipati** (sambatipati@mcneese.edu, ENCS Dept Head) offering
      a guest CS/AI lecture — de-risks the adjunct credential question (SACSCOC
      "tested-experience" path).
- [ ] Email/call **LSBDC at McNeese** (lsbdc.msu@louisianasbdc.org / 337-475-5529), introduce
      to new director **Dean Day** — two-way referral channel into Track 1. _Best McNeese angle._

### Track 7b — Content engine — _cheap, compounding_

- [ ] Start the lived-recovery + AI content engine (solves the unmodeled organic-traffic
      problem for Track 6; doubles as recovery-product distribution). Keep it time-boxed.

---

## Phase 2 — Months 6–12: Stack retainers, validate the next bets

**Theme:** reach the $120–200k run-rate; validate (don't build) the expansion tracks.
**Success = run-rate ≥ $120k + ≥1 validated expansion track.**

### Track 1 (continue)

- [ ] Stack project clients into retainers (62% of SMBs convert project→retainer within 6 mo).
      Watch the **time collision** — this is the bandwidth ceiling (D2).

### Track 2 — Productize CPA AI-roadmap for other firms (RANK 2)

- [ ] **Validate WTP with 2–3 non-TWK firms** using TWK as the live reference build. Do not
      build a product until WTP is confirmed. **Kill:** no firm will pay for productized
      (vs. bespoke) by end of window.

### Track 3 — regroup / sober-living SaaS (RANK 3) — _only if Track 1 cash is flowing_

- [ ] **Gate:** start only if advisory cash is flowing **and** OHWS partnership is in writing (D3).
- [ ] Resolve the "Regroup" iOS **name collision**; reposition off "no competitor."
- [ ] Reprice to **flat per-house ~$59–79** (drop per-bed framing; anchor vs Sobriety Hub $65 flat).
- [ ] Land **one design-partner house** in the brother's network with free migration.
- [ ] Model Stripe rent-processing as a **pass-through retention feature, not net revenue.**
- **Reality:** contested market (6+ incumbents), realistic Y1 = low tens of logos (~$30–60k),
  **not** the $204k/$315k docs. GTM must be partnership/warm-network-led (LTV ~$3.3k → CAC < ~$1,100).

### Track 4 — BH RCM/denial-prevention copilot (RANK 4) — _validate only, no build_

- [ ] Validate WTP with **3–5 treatment-center clients from the CPA book** (% of recovered revenue).
- [ ] **[VERIFY] 42 CFR Part 2 + HIPAA LLM architecture** — confirm a viable BAA-covered /
      de-identified model path _before_ any code (D4).
- **Do not write code this phase.** Best wedge found, but validation-gated.

---

## Phase 3 — Months 12–24: Scale what's validated

**Theme:** scale #1/#2; build only what cleared its gate.

- [ ] **Track 1/2:** scale with 1–2 contractors **only if** an $80–150k custom build appears
      (the first move toward the fair-wage, people-employing mission). Mind the time collision.
- [ ] **Track 5:** pursue first SDVOSB **subcontract-to-prime** on-ramp (no past-performance solo).
- [ ] **Track 4:** if WTP validated **and** Part 2 architecture cleared → build the MVP.
- [ ] **Track 6 — Next Step Recovery (RANK 6):** keep **strictly D2C / operator-pays**;
      non-clinical scope-of-practice firewall intact (D8); attorney-reviewed.
- [ ] **Track 9 — homegroups / aftercare bridge (RANK 9):** remains **deferred / gated behind
      counsel** (D4). Treat as a flywheel feature, not a standalone B2B line. Incumbents
      (Kipu, Ritten $35M) are consolidating this adjacency — do not fight the EHR core solo.

---

## Attorney Gate (load-bearing — blocks all treatment-center revenue)

Before **any** dollar from a treatment center or **any** Part 2 data moving between parties
(Tracks 4 & 9): a licensed healthcare-regulatory attorney (EKRA + AKS + 42 CFR Part 2 +
**Louisiana** patient-brokering) must bless, in writing: the flat-fee license + FMV memo, the
§1001.952(d) consulting contract, the TPO + counseling-notes consent + BAA templates, and
confirm no routing logic steers patients to payers. EKRA is **intent-based**; Louisiana is in
the **5th Circuit** (has _not_ adopted the defense-friendly _Schena_ reading); penalty
$200k + 10 yr per occurrence. This gate is D4.

---

## Mission Check (revisit each phase)

The fair-wage, people-employing goal is best realized by **Track 1 → a standalone
automation/advisory firm that hires** (Phase 3 contractors are the first step). SaaS (Tracks
2/3/4) and solo coaching (Track 6) employ few. Fastest income and best mission vehicle are the
same track — the only tension is patience.

---

## Scoreboard (update monthly)

| Metric                            | Target         | Current |
| --------------------------------- | -------------- | ------- |
| Revenue-share papered (D1)        | Yes            | —       |
| TWK reference automation shipped  | Day 60         | —       |
| Advisory retainers signed         | 2–3 by Mo 6    | —       |
| Annualized run-rate               | $120k by Mo 12 | —       |
| SAM.gov + VetCert                 | Mo 3           | —       |
| Validated expansion track (2 / 4) | ≥1 by Mo 12    | —       |
| Weekly C1 client hours (D2)       | [set]          | —       |
| Weekly C2 agent-supervised hours  | [set]          | —       |
