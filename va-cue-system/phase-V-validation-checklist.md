# Phase V — Validation Sprint Checklist

> **Purpose:** the go/no-go gate that must clear **before any build spend** on the
> Effective-Date & CUE Engine (see `va-cue-rag-kb-system.md` §Addendum). Three
> workstreams run in parallel; each has a pass threshold; the sprint ends in one
> **GO / PIVOT / STOP** decision. Timebox: **2–4 weeks.** Cost: ~$0 (time + a few trial
> seats / sales calls).
>
> **The whole point:** two deep-research passes left three things unproven that decide
> the venture — (A) does the buyer actually feel this pain and pay, (B) is the moat
> already a cheap commercial product, (C) has a competitor already shipped the wedge.
> Answer these for near-zero cost instead of discovering them 12 months in.

## Day 0 — Setup

- [ ] **Decide the goal lane (provisional):** bootstrapped/founder-scale (verified TAM
      supports ~$1.0–1.3M ARR by Yr3 — viable) vs. venture-scale (likely too small).
      Write it down; revisit at the gate.
- [ ] **Stand up a tracker** (one spreadsheet, three tabs: Interviews, Vendors,
      Competitors). No CRM needed.
- [ ] **Draft outreach templates** (see Workstream A). Keep them non-pitchy —
      "researching how accredited reps handle effective-date/CUE work," not "want to
      buy my tool?"

---

## Workstream A — Customer discovery: is the pain real and paid-for?

**Target:** 8–12 completed interviews; **≥5 must confirm** the pain is top-3 AND that
they already spend money/time on this work. **Interview accredited _agents/attorneys_
who charge fees — not VSO reps** (they can't pay fee-based pricing).

### Sourcing (build a list of 30–40, contact in waves)

- [ ] **VA OGC accreditation search** (the authoritative roster) — filter to attorneys/
      agents; prioritize **solo + boutique** (the beachhead), skip the CCK-class mega-firms
      for now.
- [ ] **NOVA** (vetadvocates.org) — member directory + the two annual CLE conferences;
      the single best watering hole (~850 members).
- [ ] **LinkedIn** — search "VA accredited attorney/agent," "veterans disability appeals";
      note anyone posting about effective dates / CUE / back pay.
- [ ] **Warm referrals** — ask each interviewee for 1–2 intros (compounds fast).

### Outreach template (non-pitchy)

> "I'm researching how accredited reps handle effective-date and CUE work — the
> retroactive/back-pay side, not the initial claim. Not selling anything; I'd value
> 20 minutes on how you actually do it today and where it's painful. Could I ask you a
> few questions this week?"

### Interview script (Mom-Test style — ask about PAST BEHAVIOR, never pitch, never ask "would you buy")

Ask these; let them talk; capture verbatim where possible:

1. **Last one:** "Walk me through the last time you worked an earliest-effective-date or
   CUE issue. What was the case?" _(specific > hypothetical)_
2. **Workflow:** "How did you actually do it — what did you open, in what order, to
   figure out the record and the law in effect at the time?"
3. **Time:** "Roughly how many hours did that take? Who did it — you or staff?"
4. **The hard part:** "What was the most tedious or error-prone step?" _(listen for:
   finding the regulation as it read then; reconstructing what evidence was of record;
   the 2,000-page C-file slog.)_
5. **Tools:** "What tools did you use? Which do you pay for today, and roughly what?"
   _(anchors WTP to actual spend, not hypothesis.)_
6. **Frequency & value:** "How often do these come up? What's a typical back-pay / fee
   outcome when you win one?"
7. **Misses:** "Ever realize later you missed an earlier effective date? What happened?"
8. **Point-in-time law:** "When you need the regulation as it read in, say, 2003 — how do
   you get it today?" _(directly tests the moat's user-side pain.)_
9. **Open:** "If a tool could reliably do one thing here, what would move the needle
   most?" _(don't pitch — just listen.)_
10. **Referral:** "Who else does a lot of this work that I should talk to?"

### Capture per interview (tracker columns)

`Name/firm · solo|boutique|firm · pain rank (1–5) · hrs per workup · tools paid-for + $ ·
frequency/yr · typical win $ · how they get historical law today · killer feature quote ·
would look at a demo? (Y/N) · referral given`

### Pass threshold (Workstream A)

- [ ] ≥5 rate effective-date/CUE work a **top-3** pain **AND** already pay for adjacent
      tooling or bill meaningfully for this work.
- [ ] ≥3 independently name **"getting the law as it read then"** or **"reconstructing
      what was of record"** as a hard step (validates F2/F3, not just F1).
- [ ] Provisional price reaction: the $150–400/seat + credits band is not laughed off by
      the solo segment. _(Signal only — don't hard-sell.)_

---

## Workstream B — Commercial-CFR check: is the moat already sold?

**The decisive question:** can a startup cheaply license **day-accurate, pre-2017,
point-in-time 38 C.F.R. retrieval** off the shelf? If yes, the technical moat collapses
to the reasoning/timeline layer. (Baseline already known: eCFR is free day-level ≥2017;
GovInfo is free _annual_ ≥1997; pre-1997 needs OCR + Federal Register reconciliation.)

### Vendors to check (one tracker row each)

- [ ] **HeinOnline** — GovInfo names it as the paid historical-CFR source (1938–present).
      _Confirm:_ point-in-time retrieval? day-level or page-image annual? API/bulk export?
      startup licensing + cost?
- [ ] **Westlaw** (Edge/Precision) — historical CFR / "versions" / point-in-time?
      API/CLEAR access? cost?
- [ ] **LexisNexis** — historical/archived CFR by date? API? cost?
- [ ] **vLex / Fastcase** — point-in-time regulation coverage + API (vLex has a large
      regulatory corpus; confirm historical depth + licensing).
- [ ] **Bloomberg Law** — historical CFR / point-in-time?
- [ ] **Casetext / CoCounsel (Thomson Reuters)** — any point-in-time CFR primitive?
- [ ] **Baseline (free) re-confirm:** eCFR versioner (≥2017 day-level) + GovInfo bulk CFR
      (≥1997 annual) — already verified; note the pre-1997 gap is the real work.

### How to check (fastest → slowest)

- [ ] **Law-library research guides** (Jenkins Law Library, Georgetown, Cornell LII, HLS
      libguides) — they document exactly which vendor has historical/point-in-time CFR and
      how far back. Fastest signal.
- [ ] **Vendor product/API docs** — search "[vendor] historical CFR API point in time."
- [ ] **Ask a law librarian** (email a VA/veterans-law or federal-docs librarian) — often
      a same-day authoritative answer.
- [ ] **Sales call / trial** for the 1–2 most likely (Hein, vLex) — ask directly about
      **API access, date granularity, earliest year, and per-seat/API licensing cost**.

### Pass threshold (Workstream B)

- [ ] **Moat SURVIVES** if: no vendor offers _cheap, API-accessible, day-accurate,
      pre-2017_ 38 C.F.R. point-in-time retrieval licensable to a startup. (Page-image
      annual PDFs behind a $$$$ seat license do **not** kill the moat — they can't be
      wired into an engine.)
- [ ] **Moat WEAKENS/COLLAPSES** if: an affordable API delivers day-accurate pre-2017
      CFR → pivot value to the reasoning + evidentiary-timeline layer (which no one sells).

---

## Workstream C — Wedge check: has a competitor shipped effective-date/CUE reasoning?

**The bar:** _extraction ≠ reasoning._ A tool that pulls effective dates already in the
C-file (VCH does) does **not** occupy the wedge. The wedge = **reconstructing the
earliest legally-correct effective date and/or testing prior final decisions for CUE.**

### Competitors to close (deep-verify — the prior passes only confirmed VCH/Vala/VeteranAi/Dodonai)

- [ ] **Caliber / Flagship** (used by vaclaims.us)
- [ ] **claim.vet** (deep, beyond the blog)
- [ ] **ClaimClam**
- [ ] **VetClaims.ai**
- [ ] **Vetlex / VetLex**
- [ ] **RepScout**
- [ ] **VCH — re-check:** has it moved from effective-date _extraction/Q&A_ to _earliest-
      date argumentation or CUE_? (It's the closest; watch its changelog.)
- [ ] **Legal-AI VA verticals** — Harvey, CoCounsel/Thomson Reuters, Legora, Clearbrief,
      EvenUp: any announced/shipped VA or veterans-disability vertical with point-in-time
      retrieval? _(The most credible well-capitalized fast-follow.)_

### Per competitor, capture (tracker)

`Tool · professional|veteran-facing · effective-date reconstruction? (Y/N/unk) · CUE
analysis? · point-in-time law? · pricing · evidence source (URL/demo/sales call) ·
last-shipped date`

### How to check

- [ ] Product page **full feature list** (not just the landing page) + **changelog/blog**
      (recent launches — this space ships fast).
- [ ] **Demo or free trial** where available; **sales call** if gated (ask directly: "do
      you do earliest-effective-date or CUE analysis?").
- [ ] **G2 / Capterra / Product Hunt** reviews + **LinkedIn** launch posts.
- [ ] Searches: "VA CUE software," "clear and unmistakable error tool," "VA earliest
      effective date analyzer," "[competitor] effective date / CUE."

### Pass threshold (Workstream C)

- [ ] **Wedge SURVIVES** if no competitor has shipped effective-date _reconstruction_ or
      CUE _reasoning_ (extraction/appeal-deadline tracking doesn't count).
- [ ] **Wedge NARROWING** if VCH or another is visibly one release away → note the runway;
      it compresses the window, doesn't kill the plan.
- [ ] **Wedge CLOSED** if a funded player already ships it → stop or find a sharper niche.

---

## The Gate — Go / No-Go (end of sprint)

**All three must pass to GO** (this is an AND gate):

| Workstream     | Pass condition                                                                                   | Result        |
| -------------- | ------------------------------------------------------------------------------------------------ | ------------- |
| A — Pain & WTP | ≥5 confirm top-3 pain + real spend; ≥3 name the law-as-it-read-then / record-reconstruction pain | ☐ pass ☐ fail |
| B — Moat       | No cheap API-grade pre-2017 point-in-time CFR on the market                                      | ☐ pass ☐ fail |
| C — Wedge      | No competitor has shipped effective-date/CUE _reasoning_                                         | ☐ pass ☐ fail |

**Decision matrix:**

- **GO** — all three pass → proceed to Phase 0 (corpus thin-slice + accreditation + design
  partners, in parallel). Lock the goal lane (bootstrapped vs venture).
- **PIVOT** — A passes but B or C fails → the _market_ is real but the _moat/wedge_
  shifted. Re-anchor value on the evidentiary-timeline + reasoning layer (unsold by
  anyone) and/or a sharper sub-niche; re-run the failed workstream.
- **STOP** — A fails → the pain/WTP isn't there; no technical moat rescues a market that
  won't pay. Kill it cheaply, here, before the build.

- [ ] **Record the decision:** date · verdict (GO/PIVOT/STOP) · one-paragraph rationale ·
      goal lane · the single biggest remaining risk carried into Phase 0.

## Deliverable

A **1-page Phase V memo** with: the three workstream verdicts (with evidence links), the
go/no-go decision, the chosen goal lane, and the top risk to watch. File it as
`va-cue-system/phase-V-memo-<date>.md`. That memo is the artifact that authorizes (or
kills) the build.

---

_Research assistance, not legal or business advice. Fee-model and accreditation questions
should be confirmed with counsel / VA OGC before committing._
