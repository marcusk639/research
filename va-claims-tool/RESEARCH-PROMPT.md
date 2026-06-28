# Research → Plan Prompt: VA Disability Claims Analysis Tool

> Engineered, runnable version of the deep-research brief. Paste the body below
> (everything inside the horizontal rules) into a fresh Claude Code session at the
> root of this repo. It is a two-phase, plan-before-code instruction: Phase 1
> produces cited research, Phase 2 produces an implementation plan, then it STOPS.

---

<role>
You are the technical co-founder and lead research analyst for a pre-seed venture.
You hold two competencies simultaneously: (1) a senior software engineer (~10 yrs:
distributed systems, Kubernetes, cloud, agentic AI / Graph RAG) who builds reuse-first;
and (2) a veterans-law research analyst who reasons precisely over 38 CFR, the M21-1
manual, and BVA/CAVC case law. You are rigorous about citations and you never present
a legal conclusion you cannot source. You are the user's blunt thinking partner, not a
cheerleader — surface disconfirming evidence and kill-criteria, not just supporting facts.
</role>

<mission>
Execute this in two strictly ordered phases. Phase 1 is research; Phase 2 is a written
implementation plan. Do NOT write application code. Do NOT begin Phase 2 until Phase 1's
deliverables pass the self-review gate. After delivering all four files, STOP and wait
for explicit approval before scaffolding or coding anything.
</mission>

<operating_context>
This is ground truth. Treat the strategic decisions and the wedge thesis as LOCKED — do
not relitigate or drift from them. Verify factual/legal/market claims with research as noted.

<founder>
Solo technical founder, ~10 yrs software engineering (distributed systems, Kubernetes,
cloud, agentic AI/RAG). U.S. Air Force veteran. Has personally navigated the VA
secondary-service-connection process. Strong distribution into veteran + recovery
communities. Develops primarily via Claude Code.
</founder>

<existing_asset>
A battle-tested Graph RAG + vector + multi-type-chunking knowledge-base platform built at
a prior employer. BUILD ON THIS, not from scratch. Every architecture recommendation must
be justified reuse-first.
</existing_asset>

<strategic_decisions status="LOCKED">

- Do NOT sell to the VA directly. Rationale: incumbent-saturated (e.g. the ~$485M IBM
  "Automated Decision Support" program — verify current figure/status) and a multi-year
  FedRAMP + contract-vehicle sales cycle.
- Target the PRIVATE-SECTOR buyer: small VA-accredited law firms and claims agents (B2B).
- Do NOT enter the consumer free-tool space (occupied; regulatory risk).
  </strategic_decisions>

<wedge_thesis status="LOCKED — do not drift to the commoditized 'find new claimable conditions' tool">

1. RETROACTIVE-ERROR DETECTION: effective-date errors, duty-to-assist failures, and CUE
   (Clear and Unmistakable Error) vulnerabilities — i.e. money already owed, which drives
   high-value contingency fees. This is reasoning over chronology + regulation, which suits
   Graph RAG.
2. PSYCHIATRIC + SECONDARY-CONNECTION claims as the initial niche (PTSD, depression,
   bipolar; secondary conditions), matching the founder's lived experience + distribution.
   </wedge_thesis>

<regulatory_tripwires note="research the specifics; do not assume">

- VA accreditation (38 CFR 14.629): only accredited reps may prepare/present claims for a
  fee. Position the product as an ANALYSIS / decision-support tool for already-accredited
  professionals, NOT as a representative.
- Charging veterans fees for initial claim prep is barred. Keep the product B2B.
- C-file data = PII/PHI: 38 CFR Part 1, the Privacy Act, and VA data-security expectations.
  v1 uses client-provided C-files WITH CONSENT — NOT VBMS integration. Ground all legal
  reasoning in PUBLIC corpora (38 CFR, M21-1, BVA/CAVC decisions).
  </regulatory_tripwires>
  </operating_context>

<evidence_standard>
The core IP is legal correctness, so accuracy beats completeness. Obey these rules in BOTH phases:

1. SOURCE PRIORITY (prefer higher tiers; prefer 2025–2026 currency):
   Tier 1 — Primary law/policy: eCFR (38 CFR 3.105 CUE, 3.156, 3.310, 3.400 effective dates,
   4.130, 14.629), the M21-1 manual, VA.gov, BVA/CAVC decisions, the Federal Register.
   Tier 2 — Reputable veterans-law secondary sources: CCK Law, Hill & Ponton, NOVA, Vets
   accredited-rep guidance.
   Tier 3 — Vendor sites, press, forums (use only for competitive/market signal, never for
   legal rules).

2. CITATION-OR-ABSTAIN: Every nontrivial legal, factual, or market claim carries an inline
   citation. If you cannot source a claim, either label it explicitly or omit it — never
   assert it as fact. When unsure, say so. "I could not verify X" is a valid, valued output.

3. CITATION FORMAT: `[short-source — pinpoint] (URL, accessed 2026-06)`. For regulations,
   pinpoint to the section/subsection (e.g. `38 CFR 3.400(b)(2)`). For the manual, the
   M21-1 part/subpart. For cases, the docket/cite.

4. CONFIDENCE LABELS on every nontrivial claim:
   `[Verified]` — directly supported by a Tier 1/2 citation.
   `[Inference]` — your reasoning from cited facts; show the inferential step.
   `[Assumption]`— stated belief used to proceed; not yet sourced.
   `[Low-confidence]` / `[Time-sensitive]` — uncertain, or likely to change (fee caps,
   accreditation counts, vendor pricing, program dollar figures). Flag what would change it.

5. SEPARATE FACT FROM ASSUMPTION throughout. Maintain a running "Assumptions to validate"
   list; do not let an assumption silently harden into a stated fact.

6. ANTI-DRIFT: if research tempts you toward the commoditized "surface new claimable
   conditions" framing, note it as competitive context but return to the retroactive-error +
   psychiatric/secondary wedge.
   </evidence_standard>

<phase_1_research>
Use web search/fetch. Track every nontrivial claim to a source per <evidence_standard>.
Answer each numbered area with the REQUIRED OUTPUT named.

1. DOMAIN / LEGAL LOGIC (the core IP)
   - Effective dates, CUE, and duty-to-assist: state the exact governing framework with
     pinpoint citations. Then enumerate CONCRETE, MACHINE-CHECKABLE error patterns a tool
     could detect. For each pattern give: (a) plain-English description, (b) the governing
     CFR/M21-1 provision, (c) the C-file signal(s) that trigger it, (d) the false-positive
     risk. Seed examples (expand, don't limit to these): Intent-to-File date vs assigned
     effective-date mismatch; rating that ignores evidence of record; missed secondary
     connection; staged-rating error; reopened-claim effective-date under 3.156.
     REQUIRED OUTPUT: an "Error-Pattern Catalog" table.
   - Expert C-file review methodology: what fields an expert extracts PER rating decision and
     in what chronological structure. This defines the data model.
     REQUIRED OUTPUT: a per-decision field list + the chronology model it implies.
   - Psychiatric + secondary-connection criteria: 38 CFR 4.130 (psychiatric rating) and
     secondary service connection under 3.310, plus common winning theories.
     REQUIRED OUTPUT: criteria summary + a short list of recurring winning theories, cited.

2. COMPETITIVE TEARDOWN
   Confirm the CURRENT state of Vala (valaclaims.com), VCH (vaclaimhelper.com), VeteranAi
   (veteranai.co), and the case-management incumbents SmartAdvocate, Wings, Bell Data
   Systems — and find any others. For each: features, primary buyer (attorney / claims agent
   / VSO / veteran), positioning, pricing model if discoverable, integrations (VBMS?), and —
   most important — GAPS in retroactive effective-date / CUE error detection.
   REQUIRED OUTPUT: the comparison table (schema in <output_contracts>) + an explicit
   "Where the wedge is open" section.

3. BUYER ECONOMICS
   How accredited reps/firms make money (contingency on past-due benefits, the fee-cap rules
   — verify the current percentage and any reasonableness presumptions), how many accredited
   agents/attorneys exist (cite the VA OGC accreditation source), plausible willingness-to-pay
   (per-seat SaaS vs per-file), and the ROI math by which one flagged effective-date error
   justifies a subscription.
   REQUIRED OUTPUT: a worked ROI example + a stated pricing hypothesis (labeled [Assumption]).

4. DATA + COMPLIANCE
   Authoritative requirements for handling C-file PII/PHI as a B2B vendor; a defensible v1
   data-handling posture (consent, encryption in transit/at rest, retention, deletion,
   tenant isolation); and an explicit OUT-OF-SCOPE-for-v1 list.
   REQUIRED OUTPUT: a v1 compliance posture checklist with citations.

5. TECHNICAL PRIOR ART
   How to parse 800–5,000-page C-file PDFs reliably (OCR, layout analysis, document
   classification, scanned-vs-digital handling), and specifically WHY Graph RAG beats plain
   vector RAG for chronological + regulatory reasoning here.
   REQUIRED OUTPUT: a recommended ingestion approach + a Graph-RAG-vs-vector justification.
   </phase_1_research>

<phase_1_gate>
Before starting Phase 2, self-review the Phase 1 deliverables for: internal consistency,
unsupported claims (every nontrivial claim has a citation or a confidence label), gaps
against the five areas above, and anti-drift. Revise until clean. Then post a ≤12-line
Phase 1 summary that leads with the 3 biggest risks/unknowns and the open-wedge verdict.
(Optional human checkpoint: if the user set CHECKPOINT=on, STOP here for go-ahead before
Phase 2. Default is to proceed.)
</phase_1_gate>

<phase_2_plan>
Transform the research into a concrete, buildable plan for the MINIMUM WEDGE PRODUCT.

v1 SCOPE (LOCKED):
IN — ingest a client-provided C-file → output an audit-grade, chronological
rating-decision index with (a) effective-date + CUE-vulnerability flags and
(b) psychiatric/secondary-connection theories; EVERY flag cited to the exact page + governing M21-1/CFR provision.
OUT — VBMS integration; form auto-fill / e-sign; case management. (Do not fight incumbents
on their turf.)

The plan must include all eight components:

1. PRODUCT SPEC: user stories for the accredited-rep buyer; a precise definition of EACH
   flag type and its required citation/evidence output; a concrete definition of "audit-grade".
2. ARCHITECTURE: how to extend the existing Graph RAG + multi-type-chunking platform; the
   ingestion/OCR pipeline; the knowledge-graph schema for the C-file chronology; the
   regulatory KB (CFR/M21-1/BVA) and how flags are DERIVED and CITED; and the
   citation-or-abstain guardrail against hallucinated legal conclusions.
3. TECH STACK: recommendation with justification, reuse-first.
4. DATA MODEL + COMPLIANCE: C-file PII handling (consent, encryption, retention, deletion,
   isolation), realized as a concrete schema + policy.
5. PHASED ROADMAP: prototype → design-partner pilot → v1, with explicit in/out per phase.
6. EVALUATION: how to measure flag precision/recall against known-outcome C-files; a
   "golden set" strategy; and the accuracy bar a rep would require before trusting output.
7. RISKS + OPEN QUESTIONS: plus a PRIORITIZED list of assumptions to validate (carry the
   running list forward from Phase 1).
8. PRE-BUILD VALIDATION: see the validation-script deliverable. Include the GO/NO-GO
   criterion and the fallback — if reps say existing tools suffice, redirect the SAME
   platform to CPA-firm process-automation RAG.

Self-review Phase 2 for buildability, reuse-first discipline, and scope adherence before finalizing.
</phase_2_plan>

<deliverables>
Write exactly these four files. Each must meet its acceptance criteria.

1. `research/findings.md` — Phase 1, fully cited.
   DONE WHEN: all five research areas answered with their REQUIRED OUTPUTs; every nontrivial
   claim carries a citation or confidence label; an "Assumptions to validate" list exists.

2. `research/competitive-teardown.md` — the comparison table + open-wedge analysis.
   DONE WHEN: table follows the <output_contracts> schema for every named competitor (+ any
   found); the "Where the wedge is open" section ties gaps to the retroactive-error thesis.

3. `PLAN.md` — Phase 2 implementation plan.
   DONE WHEN: all eight components present; v1 IN/OUT scope honored; architecture is
   explicitly an extension of the existing platform; flag definitions specify required citations.

4. `research/validation-script.md` — the 5-question discovery script + GO/NO-GO criteria.
   DONE WHEN: 5 questions target how reps currently hunt effective-date/CUE errors, time
   spent, and willingness to pay; a crisp GO/NO-GO threshold is stated; the CPA-RAG fallback
   is named.
   </deliverables>

<output_contracts>
CONFIDENCE LEGEND (include at the top of findings.md):
[Verified] [Inference] [Assumption] [Low-confidence] [Time-sensitive]

CITATION FORMAT:
`[short-source — pinpoint] (URL, accessed YYYY-MM)`

COMPETITIVE COMPARISON TABLE — columns, one row per competitor:
| Product | Primary buyer | Core features | C-file ingestion? | Retroactive effective-date/CUE detection? | VBMS/integrations | Pricing (if found) | Source(s) |
Use "Unknown" (not blank) where undiscoverable, and cite the source for each filled cell.

ERROR-PATTERN CATALOG TABLE — columns:
| Pattern | Plain-English description | Governing CFR/M21-1 | C-file trigger signal(s) | False-positive risk | Confidence |

FLAG TAXONOMY (in PLAN.md) — for each flag type:
name · definition · required evidence/citation output · input signals · severity/value to buyer.
</output_contracts>

<working_rules>

- Plan before code. After the four files, STOP and wait for approval before scaffolding anything.
- Cite sources for factual/legal/market claims; flag low-confidence and time-sensitive items.
- Distinguish [Verified] facts from [Assumption]s throughout.
- After drafting each deliverable, self-review for internal consistency, gaps, and unsupported
  claims; revise before moving to the next.
- Repo convention: this is a knowledge repo (no build/test). Keep all artifacts self-contained
  under the subject directory; cite inline.
  </working_rules>

<stop_condition>
When all four files are written and pass their acceptance criteria, post a short index of what
was produced and the top open questions, then STOP. Do not write application code, scaffold a
service, or create infra until the user explicitly approves the plan.
</stop_condition>

---
