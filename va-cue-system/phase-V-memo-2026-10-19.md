# Phase V memo: Effective-Date & CUE Engine (interim, 2026-10-19)

**Verdict: PENDING. The gate is not cleared, and no build spend is authorized.**

Workstreams B and C passed on desk research. Workstream A (customer discovery) hasn't started. The gate is an AND gate, and A is the stop condition, so no GO/PIVOT/STOP call is possible until 8–12 interviews are complete. Tracker: `phase-V-tracker.xlsx` (Interviews / Vendors / Competitors tabs).

| Workstream        | Result                                                                                               | Confidence                           |
| ----------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **A: Pain & WTP** | **Not run** (0 of 8–12 interviews)                                                                   | n/a                                  |
| **B: Moat**       | **Pass (provisional)**: no cheap, API-grade, day-accurate pre-2017 38 C.F.R. was found               | Medium (desk only; no sales calls)   |
| **C: Wedge**      | **Pass, narrowing**: no tool does effective-date reconstruction, CUE reasoning, or point-in-time law | Medium-High; runway est. 6–12 months |

## B: Moat (commercial-CFR check)

- **Every source with pre-2017 text was annual-edition or page-image only.**
  - GovInfo: free annual XML from 1996.
  - HeinOnline and ProQuest: page-image PDFs from 1938.
  - Westlaw "CFR Historical": per-year snapshots from 1984; Regulations Compare goes back to 2005.
  - Lexis Archived Codes: per-year snapshots from 1981.
  - Sources: [Jenkins historical-CFR guide](https://guides.jenkinslaw.org/code-federal-regulations/historical-cfr), [Jenkins on Westlaw history](https://www.jenkinslaw.org/news/finding-historic-code-federal-regulations-sections-part-2).
- **Nothing returns "38 C.F.R. § X as in force on date D" before 2017.** The eCFR versioner, which does, starts around January 2017.
- **New finding: [Vaquill.ai](https://www.vaquill.ai/blog/cfr-annual-editions-point-in-time-api)** sells a credit-priced API over the GovInfo annual editions from 1996.
  - This makes the post-1996 _annual_ baseline a commodity.
  - The defensible part is now (a) pre-1996 OCR and structuring, and (b) reconciling each Federal Register amendment to its exact effective date, which day-level accuracy requires.
  - Vaquill is a possible baseline supplier, or a competitor to watch.
- **Residual risk:** an undocumented day-level feed at Thomson Reuters or Lexis. Two sales-call questions, kept in the Vendors tab, would close this:
  1. Westlaw/Lexis: "Does any product return 38 C.F.R. text as in force on an arbitrary pre-2017 date, and not just the nearest annual edition? What are the redistribution terms?"
  2. HeinOnline: "Is there bulk or API access to the 1938–1996 OCR text, with commercial derivative rights?"
- **Before building OCR,** check archive.org and Public.Resource.Org for an existing scan set covering 1938–1995.

## C: Wedge (competitor check)

- **No tool reconstructs the earliest legally correct effective date, tests final decisions for CUE, or applies the law as it read then.** Sixteen-plus tools were checked; see the Competitors tab.
- **Closest: [VBMS Reviewer](https://vbmsreviewer.com)** (professional; $79 per matter, $400/month).
  - Its copy says "rating and effective-date signals" and "Effective Date Tracking." That is chronology extraction plus flags.
  - A [LegalTechnologyHub listing](https://www.legaltechnologyhub.com/vendors/vbms-reviewer/) claims CUE evaluation, but its own site doesn't.
  - Its positioning is moving toward the wedge, so treat it as the clock.
- **VCH re-check:** dated blog posts through 2026-09-14 show forms, Clio, deadlines and discharge upgrades. Nothing on effective-date argumentation or CUE.
- **Page AI:** C-file search used by Jan Dils and CCK. "Preliminary case analysis" is marked coming soon. It already has the big-firm customers.
- **"CUE detection" is becoming a label.** The VA Claims Intel Chrome extension (free, veteran-facing, 416 users) markets 13 checklist flags with CFR cites. Expect buyers to have seen "CUE" claims that don't hold up. The demo has to show reasoning against the law in force at the time.
- **Incumbents: low-to-medium risk.**
  - No VA vertical was found at Harvey, CoCounsel, Legora, EvenUp, Supio, Lexis+ AI or Filevine.
  - The most plausible fast-follower is [Eve](https://eve.legal/practice-area/ssdi). It already serves SSDI contingency firms with chronology and brief drafting.
  - Thomson Reuters already holds point-in-time data at the content layer but shows no VA intent.
  - Not checked: Clearbrief, vLex Vincent, Darrow, Finch, and the NOVA exhibitor list.
- **Unresolved:** Caliber/Flagship (no product by that name found at vaclaims.us), plus RepScout and ClaimClam (sites unreachable; neither appears to be a VA product).

## A: Pain & WTP (not run, and the gating item)

- **Pool conflict:** the four first-wave reviewer candidates (Davis, Eagle/Radogna, Castillo, Luck) are **excluded** from interviews. Once someone has critiqued the report, they can't give clean past-behavior answers.
- **Seed list:** eight interview candidates are in the tracker. Another 25–30 solo/boutique agents and attorneys still need to be pulled from the VA OGC accreditation roster and NOVA.
- **Clinics** (e.g., Texas Tech) count for insight only, not for willingness to pay.
- **Next:** use the non-pitchy template and Mom-Test script in `phase-V-validation-checklist.md`. Contact in waves of about 10 and ask each interviewee for a referral.

## Goal lane (provisional)

**Bootstrapped / founder-scale.** The market supports about $1.0–1.3M ARR by Year 3. B and C also argue against a venture pace: the moat is real but narrow (day-level reconciliation, pre-1996 corpus), and VBMS Reviewer sets a 6–12 month clock. That means proving a thin slice fast with design partners, not raising to build broadly. Revisit at the gate.

## Biggest risk carried forward

**A is unproven.** No buyer has yet confirmed that this is a top-3 paid pain. The second risk is runway: VBMS Reviewer or Page AI adding effective-date reasoning on top of the C-file data they already ingest. If A passes, Phase 0 should lead with the piece nobody has: **point-in-time 38 C.F.R. applied to a real decision date**.

## Decision record

| Date       | Verdict             | Rationale                                                                                 |
| ---------- | ------------------- | ----------------------------------------------------------------------------------------- |
| 2026-10-19 | PENDING             | B and C pass on desk research. A not started. AND gate: no build spend until A completes. |
| _TBD_      | _GO / PIVOT / STOP_ | _Fill in after 8–12 interviews and the two sales calls_                                   |

---

_Research assistance, not legal or business advice. Competitor and vendor findings are web snapshots as of 2026-10-19 (several based on search summaries, not primary pages) and should be re-checked before committing._
