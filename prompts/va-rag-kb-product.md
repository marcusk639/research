# Deep Research → Implementation Plan: VA Disability Claims Analysis Tool

## Your Role
You are acting as a technical co-founder + research analyst. Execute this in two
distinct phases. Do NOT skip to code. Phase 1 is research; Phase 2 is a written
implementation plan. Produce both as markdown files in the repo (see Deliverables).
Stop after Phase 2 and wait for my approval before writing any application code.

## Context (treat as ground truth; verify with research where noted)
- Founder profile: solo technical founder, ~10 yrs software engineering (distributed
  systems, Kubernetes, cloud, agentic AI/RAG). U.S. Air Force veteran. Has personally
  navigated the VA secondary-service-connection process. Strong distribution into
  veteran + recovery communities.1
- Existing asset to reuse: a battle-tested Graph RAG + vector + multi-type-chunking
  knowledge-base platform built at a prior employer. Prefer to build ON this, not from
  scratch. Dev is done primarily via Claude Code.
- Strategic decision already made: do NOT sell to the VA directly (incumbent-saturated,
  e.g. the ~$485M IBM "Automated Decision Support" program; multi-year FedRAMP +
  contract-vehicle sales cycle). Target the PRIVATE-SECTOR buyer: small VA-accredited
  law firms and claims agents.
- The differentiated wedge (this is the thesis to build around — do not drift to the
  generic "find new claimable conditions" tool, which is already commoditized):
  1. RETROACTIVE-ERROR DETECTION: effective-date errors, duty-to-assist failures, and
     CUE (Clear and Unmistakable Error) vulnerabilities — i.e., money already owed,
     which drives high-value contingency fees. This is reasoning over chronology +
     regulation, which suits Graph RAG.
  2. PSYCHIATRIC + SECONDARY-CONNECTION claims as the initial niche (PTSD, depression,
     bipolar; secondary conditions), matching founder's lived experience + distribution.
- Known competitors to analyze (confirm current state, find others): Vala
  (valaclaims.com), VCH (vaclaimhelper.com), VeteranAi (veteranai.co), and the
  case-management incumbents SmartAdvocate, Wings, Bell Data Systems. Most do C-file
  ingestion + "surface claimable conditions/gaps" + form auto-fill; few rigorously hunt
  retroactive effective-date/CUE errors.
- Regulatory tripwires to respect in the design (research the specifics, don't assume):
  - VA accreditation rules (38 CFR 14.629): only accredited reps may prepare/present
    claims for a fee. Position the product as an ANALYSIS/decision-support tool for
    already-accredited professionals, NOT as a representative. Avoid the consumer
    free-tool space (occupied; regulatory risk).
  - Charging veterans fees for initial claim prep is barred; keep the product B2B.
  - Handling C-file data = PII/PHI: 38 CFR Part 1, Privacy Act, VA data-security
    expectations. v1 should use client-provided C-files WITH CONSENT, not VBMS
    integration. Ground reasoning in PUBLIC corpora (38 CFR, M21-1, BVA/CAVC decisions).

## Phase 1 — Deep Research
Use web search/fetch. Prioritize official + authoritative current (2025–2026) sources:
VA.gov, eCFR (38 CFR 3.105 (CUE), 3.156, 3.400 (effective dates), 14.629), the M21-1
manual, BVA/CAVC decisions, and reputable veterans-law sources (CCK Law, Hill & Ponton).
Track every nontrivial claim to a source; flag anything uncertain or time-sensitive.

Research and document:
1. DOMAIN / LEGAL LOGIC (the core IP):
   - The exact regulatory framework for effective dates, CUE, and duty-to-assist.
     Enumerate the concrete, checkable error patterns a tool could detect (e.g.,
     Intent-to-File date vs assigned effective date mismatch; ratings that ignore
     submitted evidence; missed secondary connections; staged-rating errors).
   - The expert C-file review methodology (what fields to extract per rating decision,
     in what chronological structure). This defines the data model.
   - Psychiatric + secondary-connection rating criteria (38 CFR 4.130, secondary
     service connection under 3.310) and common winning theories.
2. COMPETITIVE TEARDOWN: for Vala, VCH, VeteranAi, + any others found — features,
   buyer (attorney/agent/VSO/veteran), positioning, pricing model if discoverable,
   integrations (VBMS?), and most importantly GAPS in retroactive-error detection.
   Produce a comparison table and an explicit "where the wedge is open" section.
3. BUYER ECONOMICS: how accredited reps/firms make money (contingency on past-due
   benefits, 20% fee caps, etc.), how many accredited agents/firms exist, what they'd
   plausibly pay (per-seat SaaS vs per-file), and the ROI math that makes a flagged
   effective-date error worth a subscription.
4. DATA + COMPLIANCE: authoritative requirements for handling C-file PII/PHI as a
   B2B vendor; what a defensible v1 data-handling posture looks like; encryption/
   retention/consent expectations; what to explicitly keep OUT of scope for v1.
5. TECHNICAL PRIOR ART: how to parse 800–5,000-page C-file PDFs reliably (OCR, layout,
   document classification), and how Graph RAG specifically helps with chronological/
   regulatory reasoning vs plain vector RAG.

## Phase 2 — Implementation Plan (only after Phase 1)
Transform the research into a concrete, buildable plan for the MINIMUM WEDGE PRODUCT:
- Scope v1 to ONE high-value job: ingest a client-provided C-file → output an
  audit-grade chronological rating-decision index with effective-date + CUE-vulnerability
  flags AND psychiatric/secondary-connection theories, every flag cited to the exact
  page + governing M21-1/CFR provision. Explicitly EXCLUDE from v1: VBMS integration,
  form auto-fill/e-sign, case management (don't fight incumbents there).
The plan must include:
1. Product spec: user stories for the accredited-rep buyer; precise definition of each
   "flag" type and its required citation/evidence output; what "audit-grade" means.
2. Architecture: how to extend the existing Graph RAG + multi-type-chunking platform;
   ingestion/OCR pipeline; the knowledge graph schema for the C-file chronology; the
   regulatory knowledge base (CFR/M21-1/BVA) and how flags are derived and cited;
   guardrails against hallucinated legal conclusions (citation-or-abstain).
3. Tech stack recommendation with justification (reuse-first).
4. Data model + compliance design for C-file PII (consent, encryption, retention).
5. Phased roadmap: prototype → design-partner pilot → v1, with what's in/out of each.
6. Evaluation: how to measure flag precision/recall against known-outcome C-files;
   a "golden set" strategy; the accuracy bar before any rep would trust it.
7. RISKS + OPEN QUESTIONS, and a prioritized list of assumptions to validate.
8. A pre-build VALIDATION step: a 5-question discovery script to take to 5 accredited
   reps (focused on how they currently hunt effective-date/CUE errors, time spent, and
   willingness to pay), plus a clear GO/NO-GO criterion. Note the fallback: if reps say
   existing tools suffice, redirect the same platform to CPA-firm process-automation RAG.

## Deliverables (write these files)
- `research/findings.md` — Phase 1, fully cited.
- `research/competitive-teardown.md` — the comparison table + open-wedge analysis.
- `PLAN.md` — Phase 2 implementation plan.
- `research/validation-script.md` — the 5-question script + GO/NO-GO criteria.

## Working rules
- Plan before code. After delivering the four files, STOP and wait for my approval
  before scaffolding anything.
- Cite sources for factual/legal claims; explicitly flag low-confidence items.
- Distinguish verified facts from assumptions throughout.
- After drafting each deliverable, review it for internal consistency, gaps, and
  unsupported claims, and revise before moving on.