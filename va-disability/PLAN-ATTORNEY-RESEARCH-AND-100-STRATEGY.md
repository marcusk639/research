# Execution Plan — Attorney/Resource Knowledge Base + Final 100% Schedular Strategy

> **Status:** active plan (v2, hardened by independent `plan-reviewer` critique) · **Created:** 2026-07-09 · **Type:** phased execution plan (produced via `make-plan`)
> **What this is:** the roadmap for a larger effort the user commissioned — (1) deep research on the veteran attorneys/firms with the best track records and the free/low-cost legal resources available, ranked and cited; (2) a cross-corpus synthesis across all three repos; (3) a single **master strategy + representation guide** aimed at **100% schedular (not TDIU)** — but honest-first, led by the committed odds, not by the target; (4) a full gap/issue register with solutions; (5) an independent critical review; (6) reusable agent/skill designs for `veteran-claims-app`.
> **This document is the plan, not the deliverables.** Deliverables come from executing Phases 1–7. Each phase is self-contained (inputs, outputs, verification, guardrails) so it can run in a fresh context.
> **Not legal or medical advice.** Executed with the veteran's accredited VSO / VA-accredited attorney and treating clinicians. No phase asks anyone to state anything untrue; the effort is documentation _timing, completeness, and representation_, never symptom-reaching. Odds are honest, non-optimistic REASONED ESTIMATES.

### v2 changelog — what the plan-reviewer critique changed

- **Fixed the ordering bug (P1):** the independent review now runs on a DRAFT master guide (new Phase 5 assembles draft → Phase 6 reviews it → Phase 7 finalizes). The review no longer precedes the artifact it reviews.
- **Honesty anchor (P2):** the committed odds are now carried into the plan verbatim as the comparator, the master doc must LEAD with them + the two hard contingencies, and the deliverable is retitled away from "maximization."
- **Anti-bloat (P3):** added an explicit consolidation/retirement step and a source-of-truth hierarchy declaration.
- **Inventory fix (P4):** added `MASTER-STRATEGY.md` and `SLEEP-APNEA-SECONDARY-CLAIM.md` (Route 2's foundation) + others to the input set.
- **UPL guardrails (P5):** the public-tooling phase is design-only with accreditation/UPL guardrails.
- **Real verification (P6):** track-record claims need an _independent_ source; win-rate-as-fact is hard-banned; witness-coaching and PHI get concrete scan gates.
- **Real independence (P7):** the critic sees only deliverables + guardrails, not the authoring reasoning.
- **Parallelization (P8):** Phases 3–4 start now, parallel to the running research.

---

## Phase 0 — Discovery (COMPLETE, consolidated here)

### 0.1 The three corpora on the veteran's side (confirmed to exist)

| Corpus                | Path                                     | Role                                                                                                        |
| --------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Claim corpus**      | `~/dev/research/va-disability/`          | The live claim. Source of truth for _this_ veteran's facts.                                                 |
| **Reference library** | `~/dev/veteran-disability-ai-resources/` | General VA knowledge + templates. Not veteran-specific.                                                     |
| **Product app**       | `~/dev/veteran-claims-app/`              | Next.js app (TS, drizzle, playwright/vitest) — destination for reusable agents/skills for _other_ veterans. |

### 0.2 Reference-library files to EXTEND, not re-derive

- `veteran-disability-ai-resources/resources/representation.md`; `knowledge-base/representation-and-fees.md`.
- Other KB: `appeals-and-decision-reviews.md`, `cp-exams-and-dbqs.md`, `ratings-and-va-math.md`, `tdiu.md`, `secondary-service-connection.md`, `compensation-and-smc.md`, `presumptive-conditions-pact-act.md`, `claims-process.md`.
- `conditions/mst-personal-assault-ptsd.md`, `mental-health-ptsd-and-mood-disorders.md`, `substance-use-disorder-secondary-connection.md`.
- App design docs (read before proposing tools): `veteran-claims-app/docs/superpowers/specs/2026-07-06-veteran-claims-app-design.md`, `.../plans/2026-07-07-veteran-claims-app-phase1-knowledge-assistant.md`.

### 0.3 Claim-corpus source-of-truth inventory (reconciled against REPORT.md "Start here")

**Facts canon:** `COMPREHENSIVE-FINDINGS-2026-07.md` (authoritative reconciled facts).
**Strategy canon:** `MASTER-STRATEGY.md` (CLAUDE.md-designated current strategy) — _was missing in v1, added_.
**Route 2 foundation:** `SLEEP-APNEA-SECONDARY-CLAIM.md` — _was missing in v1; Phase 3 depends on it_.
**Also required inputs:** `PATH-TO-100-PERCENT-2026-07-07.md` (dual-route + issue register I-1…I-15), `CLAIM-COMPLETION-PLAN-2026-07-08.md` (process + effective-date gap), `VA-SUBMISSION-GUIDE-2026-07-08.md`, `ACTION-CHECKLIST-100-PERCENT.md`, `CLAIM-MASTER-BRIEF.md`, `CLAIM-ASSESSMENT.md`, `CREDIBILITY-INCONSISTENCY-RESEARCH.md`, `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`, `NEXUS-LETTER-GUIDE-CHERIE.md`, `CP-EXAM-PREP-MENTAL-HEALTH.md`, `DOCUMENT-PROVENANCE.md`.
**Before Phase 3, re-run `ls` + REPORT.md "Start here" to confirm this list is still complete.**

### 0.4 The committed odds — the honesty ANCHOR (carry verbatim; nothing may drift above these)

From `PATH-TO-100-PERCENT-2026-07-07.md` §9 / `REPORT.md`: **70% ≈ 90%+ · 90% ≈ 60–70% · 100% MH-alone (Route 1) ≈ 40–50% · 100% combined (Route 2) ≈ 50–60%.** Two hard contingencies pin these down: **Route 1's adverse married-veteran/total-social-impairment authority (≈3 adverse vs 1 favorable BVA cites)** and **Route 2's not-yet-obtained sleep study.** Any deliverable's odds must be **≤ these**; the master doc must LEAD with them.

### 0.5 Tooling (the "Allowed APIs")

- **`deep-research`** (skill → background Workflow) — **LAUNCHED for Phase 1** (Task `wymaebdpp`, run `wf_61ae64d6-fdc`).
- **`citation-verifier`** — MANDATORY before any legal cite is presented as fact (prior pass: 40/109 misstated).
- **`claim-consistency-checker`** — cross-corpus fact/date/diagnosis drift.
- **`va-claim-document-analyst`** / **`va-claim-corpus-synthesizer`** — per-doc read + multi-doc merge.
- Skills: `va-corpus-sync`, `va-claim-status`, `va-rating-strategy`, `va-rating-reassess`.
- Independent critic (Phase 6): `general-purpose` or `plan-reviewer`, given ONLY deliverables + guardrails.

### 0.6 Anti-patterns / hard rules (guard in every phase)

- **Never coach witness evidence** — no drafting/scripting/example wording for Erica's or any buddy statement, ever (`CLAIM-ASSESSMENT.md` §0).
- **Never present a legal citation as confirmed without `citation-verifier`.**
- **Never present an attorney/firm win-rate as fact** — near-universally marketing with undisclosed denominators; prefer excluding such numbers, not merely labeling them.
- **Never invent a statistic.**
- **Schedular-primary; TDIU only as a labeled, rejectable fallback** (veteran wants to retain earning capacity).
- **PHI discipline** — `personal-records/` gitignored PHI; `ClaudeDisabilityAssets/`, `ClaudeChat/` sensitive-untracked. Never `git add` them; run the PHI gate (Phase 7) before any commit.

---

## Phase 1 — Deep research: attorneys, strategies, free/low-cost resources · **RUNNING** (Task `wymaebdpp`)

**Produces:** verified, cited answer on best-track-record firms/attorneys (esp. PTSD/MST MH schedular appeals), their strategies, free-consult reality + fee structure (§ 5904, ~20% contingency, EAJA, past-due withholding), accreditation/contact/reach, the VSO-vs-attorney-vs-agent distinction, when an attorney can/can't charge, and free resources ranked (VSOs, NVLSP, clinics, Stateside Legal, pro bono, ogc.va.gov), incl. Louisiana/Gulf-Coast.

**On return:** (1) read the full workflow output — **inspect `journal.jsonl` before assuming any agent returned non-empty**; (2) save raw to `va-disability/RESEARCH-VETERAN-ATTORNEYS-2026-07-09.md` with citations intact; (3) dispatch `citation-verifier` on every legal/regulatory cite (§ 5904, 38 C.F.R. § 14.636, EAJA 28 U.S.C. § 2412, any case names).

**Verification:** ≥1 cited source per firm/resource; fee-rule section cites primary law; marketing-vs-verifiable labeled; citation-verifier logged.

**Anti-patterns:** self-reported success rate as fact; implying an attorney can charge for the _initial_ claim; omitting the free-VSO path (correct first stop for the current pre-decision stage).

---

## Phase 2 — Ranked Attorney & Legal-Resources Knowledge Base · depends on Phase 1

**Input:** Phase 1 verified report + the two reference-library representation files (extend, don't duplicate).
**Output:** `va-disability/ATTORNEY-AND-LEGAL-RESOURCES-KB.md`:

1. **Decision guide:** VSO vs attorney vs claims agent, keyed to _this_ veteran's posture (open Supplemental Claim, no decision yet → attorney generally cannot charge yet → free VSO / free consult now; attorney on contingency only if it reaches appeal).
2. **Free/low-cost resources, ranked by usefulness for this fact pattern** — what/cost/track-record basis/contact/website/source/"best for."
3. **Attorneys/firms table, ranked** — reputation basis **labeled verifiable vs marketing**, signature strategies, free consult Y/N, fee structure, accreditation **confirmed via ogc.va.gov**, contact/website, national reach, sources.
4. **Fee-rule primer** — § 5904, 20% norm, EAJA, direct-pay withholding — citation-verified.
5. **"How to run a free consult"** — what to bring, questions to ask, red flags (non-accredited "claim sharks," illegal upfront fees).

**Verification (hardened per P6):** every track-record claim cites an **independent/primary source** (BVA/CAVC decision, bar record, third-party) — a firm's own URL counts as _marketing_, not verification; **no win-rate presented as fact**; accreditation traceable to ogc.va.gov; fee section citation-verified.

**Anti-patterns:** ranking by ad spend/SEO; recommending paid counsel where a free VSO is the correct current-stage move.

---

## Phase 3 — Cross-corpus synthesis → final 100% schedular strategy · **START NOW, parallel to Phase 1** (P8)

**Method (default — the lighter pass, P8):** one focused `general-purpose` synthesis over the 0.3 input set (the corpus is largely reconciled; `COMPREHENSIVE-FINDINGS` is authoritative). Escalate to the `va-claim-document-analyst` fan-out only if the synthesis surfaces unreconciled contradictions. Fold Phase 2's representation dimension in as a late input.

**Output:** the strategy section of the draft master guide (Phase 5): the two convergent routes reconciled with latest facts (Route 2 grounded in `SLEEP-APNEA-SECONDARY-CLAIM.md`); where representation adds leverage (accredited attorney for a post-decision HLR/Board appeal on 4.126(a)/4.2/Nieves-Rodriguez); and the **committed odds from 0.4, restated verbatim as the anchor.**

**Verification:** every strategy claim traces to a corpus source; no route relies on an unverified citation; odds **equal or below** 0.4; TDIU appears only as a labeled, rejectable fallback.

**Anti-patterns:** re-deriving facts `COMPREHENSIVE-FINDINGS` already settled; odds drifting upward; any strategy needing witness coaching.

---

## Phase 4 — Full gap/issue register with solutions · **START NOW, parallel** (P8)

**Input:** `PATH-TO-100-PERCENT` I-1…I-15 + `CLAIM-COMPLETION-PLAN` Tier 0 + anything Phases 1–3 surface.
**Output:** the Issue Register section of the draft master guide — every obstacle to 100%, each with severity, why it threatens the rating, and ≥1 concrete solution (named owner/tool/action). MUST include: two-domain (occupational AND social) requirement + married-veteran adverse authority; the conflicting `PsychEval.pdf`/`MarcusKleinPsychEval.pdf` alternate-causation phrase; the effective-date/prior-decision unknown; the SI-fluctuation record; thin-records under-disclosure; sleep-study dependency (Route 2); DC 6847 NPRM status; witness-corroboration gaps; representation timing.

**Verification:** no issue without a solution; each solution names a specific owner/tool; nothing requires misrepresentation. **P10:** the effective-date unknown gets a concrete action — _have the VSO pull the prior rating decision / VA eFolder to determine whether a prior decision on this issue exists_ — not just "severity + generic solution."

**Anti-patterns:** hand-waving ("get more evidence") without a next action; omitting an inconvenient issue.

---

## Phase 5 — Assemble the DRAFT master guide (new; fixes P1)

**Input:** Phase 2 (representation), Phase 3 (strategy), Phase 4 (issue register).
**Output (draft):** `va-disability/MASTER-CLAIM-STRATEGY-AND-REPRESENTATION.md` (retitled away from "maximization," P2). It must **LEAD** with: the honest probability (0.4 odds) + the two hard contingencies, THEN the "do this next, in order" spine, strategy, representation/how-to-use-the-KB, and the issue register. Mark it **DRAFT — pending independent review.**

**Verification:** integrates all three prior phases; cites its sources; odds ≤ 0.4 and appear before any "how to reach 100%" content.

---

## Phase 6 — Independent critical review of the draft (mandatory; fixes P1/P7)

**Method:** dispatch a critic that did NOT author the draft. Feed it **ONLY the draft + KB + the 0.6 guardrail list — not this plan or the authoring reasoning** (P7). Two passes: `claim-consistency-checker` (fact/date/diagnosis drift) + a `general-purpose`/`plan-reviewer` adversarial critic attacking over-optimism, unsupported/marketing claims, unverified citations, witness-coaching slips, and any gap left without a solution. Run `citation-verifier` on every legal cite in the draft + KB.

**Concrete scan gates (P6):**

- **Witness-coaching gate:** grep deliverables for any authored buddy/spouse-statement narrative or second-person imperatives directed at a witness; **fail if found.**
- **Marketing gate:** flag any track-record claim whose only source is the firm's own site; **fail any win-rate presented as fact.**

**Output:** a findings list with each finding's disposition (fixed / accepted-risk / deferred).

**Verification:** reviewer ≠ author; every finding has a disposition; both scan gates and citation-verifier ran.

---

## Phase 7 — Finalize + reusable agent/skill designs · resolve Q2/Q3 first (P9)

**7A — Finalize the master guide:** apply Phase 6 dispositions; append a **"Critical Review — issues found"** section (per the user's explicit instruction, issues are listed in the delivered answer). **Consolidation/retirement (P3):** state the master guide's exact relationship to the facts canon (`COMPREHENSIVE-FINDINGS`) and strategy canon (`MASTER-STRATEGY`); mark any now-superseded doc as history using the corpus's existing pattern. **Do NOT edit `REPORT.md` nav until the parallel-session hold is confirmed clear (Q2).**

**7B — Reusable agent/skill designs (DESIGN-ONLY default, P5/P9):** `va-disability/REUSABLE-AGENTS-SKILLS-DESIGN.md` — one-paragraph specs (purpose, inputs, outputs, guardrails), evaluated against the app's design docs. Candidates: `representation-matcher`, `free-consult-prep`, `schedular-vs-tdiu-advisor`, `gap-and-issue-auditor`, and ports of `citation-verifier`/`claim-consistency-checker`. **UPL/accreditation guardrails (P5):** every proposed public tool must present _general educational_ information only, route users to accredited representatives, carry a not-legal-advice/UPL disclaimer, encode **no** veteran-specific PHI, and be flagged **"requires legal review before shipping."** Build nothing into `veteran-claims-app` unless the user explicitly opts in (Q3).

**PHI pre-commit gate (P6):** before any `git add` in any repo — `git status` + a name/PII grep; never stage `personal-records/`, `ClaudeDisabilityAssets/`, `ClaudeChat/`.

---

## Final verification (whole effort)

1. Every legal citation across KB + master doc passed `citation-verifier`.
2. Every attorney/resource claim has a source; marketing vs _independent_ labeled; no win-rate as fact.
3. Strategy is schedular-primary; TDIU only a labeled fallback.
4. Every register issue has ≥1 concrete, owned solution; the effective-date unknown has a real action.
5. An independent critic (fed only deliverables + guardrails) reviewed the DRAFT; findings listed in the answer.
6. Witness-coaching scan clean; PHI never staged; master doc's place in the source-of-truth hierarchy declared.
7. Odds ≤ the 0.4 anchor and lead the master doc.

## Scoping questions — resolve Q2/Q3 before Phase 7 (P9)

1. **Q1 — Commit/PR:** produce on the current branch + open/update a PR, or leave uncommitted for review? _(Default: leave uncommitted until the master doc is reviewed, then ask.)_
2. **Q2 — `REPORT.md` nav:** OK to add the master-guide pointer given `REPORT.md` is currently modified by a parallel session? _(Default: don't touch until clear.)_
3. **Q3 — Agent/skill build:** design-only this pass, or also build one into `veteran-claims-app`? _(Default: design-only; explicit opt-in required to build.)_
