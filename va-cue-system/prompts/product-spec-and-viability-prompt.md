# Prompt — VA Effective-Date & CUE Engine: Plain-Language Product Spec + Viability, Monetization & Revenue

> Run from `~/dev/research/va-cue-system/`. Produces one document:
> `va-cue-system/PRODUCT-SPEC-AND-VIABILITY-<YYYY-MM-DD>.md`.
> Recommended: Opus, high effort, web tools (Firecrawl/Exa) enabled, `citation-verifier` agent available.

---

<role>
You are a senior product manager who has shipped regulated legal-tech and B2B SaaS, writing
for a reader who is smart but knows nothing about veterans' benefits law. You think like a
skeptical investor and an engineer at the same time: every requirement must be buildable,
every claim traceable, and every revenue number derived from stated assumptions.
</role>

<context>
This research subject (`va-cue-system/`) evaluates a proposed software product, working
name the **"Effective-Date & CUE Engine."** In one sentence: a tool sold to VA-accredited
claims agents and attorneys that ingests a veteran's VA claims file, reconstructs a dated
timeline of every past VA decision and the law in force at each, tests old decisions for
"Clear and Unmistakable Error" (CUE), argues the earliest possible benefit start date, and
drafts citation-backed filings for a human professional to review.

Two deep-research passes (July 2026) already assessed feasibility, competition, market,
and revenue. Their conclusions, corrections, and open questions are your starting point —
not something to re-derive from scratch, and not something to copy uncritically. Today's
date is later than those passes, so their competitor, portal-access, and pricing facts are
snapshots that may have moved.

The existing material is written for people who already understand the domain. The gap
this document fills is a **single, self-contained, end-to-end explanation of what the
product actually is and does, in concrete product terms**, followed by a rigorous judgment
of whether it is worth building and how it would make money.

The reader: a capable product person, engineer, or investor with no VA background. After
reading the Summary and the Domain Primer, they should be able to explain to someone else
who uses the product, what problem it solves, why that problem is worth money, and what
the product does step by step. After reading the whole document, they should be able to
start building it, or decide not to.
</context>

<sources>
Read these in full before writing. They are the primary evidence base.

- `REPORT.md` — integrated synthesis; its **Corrections** (§5) and **Open items** (§6) are binding.
- `va-cue-rag-kb-system.md` — the original product spec (features F1–F10) and the revised
  phase plan in its Addendum (Phase V → 0 → 1 → 2 → 3).
- `deep-research-findings-2026-07-16.md` — feasibility, strategy, market, revenue detail and claim ledger.
- `deep-research-wedge-moat-2026-07-16.md` — competitor matrix, moat analysis, 25-claim ledger.
- `phase-V-validation-checklist.md` — the go/no-go validation sprint.

Read `va-cue-deep-research-prompt.md` only to understand what earlier passes were asked; it
is not evidence.

Do not read: this prompt file, anything under `prompts/`, `.remember/`, `.claude/`, your own
output file, or any other subject directory in the repo (notably `va-disability/`, which
holds an unrelated personal claim). This document must stand on this subject's sources plus
web research.
</sources>

<epistemic_rules>
These exist because an earlier pass in this repo had 40 of 109 legal citations misstated,
and because this document will drive a build/no-build decision.

- Trace every factual claim to a source: a file in this directory (`file.md §section`) or a
  web URL. Carry the original source through when you reuse a figure from the research files.
- Label every number by provenance: **Verified** (sourced), **Carried forward** (from the
  July 2026 research, with its as-of date), **Re-verified** (you checked it on the web
  today), **Assumption** (your input to a model), or **Estimate** (your derived output).
- Honor every correction in `REPORT.md §5` (e.g., fee pool $410.8M not $396.8M; point-in-time
  law is day-level, not annual snapshots; eFolder Express is the external access channel;
  Nehmer is not CUE; § 14.632(c)(5) is not a categorical success-fee ban; _Chisholm_ and
  _Hamill_ are real effective-date cases, not CUE cases).
- Re-verify the volatile facts that most affect the verdict, using web tools: competitor
  feature sets (especially VA Claim Helper's effective-date work), whether the Accredited
  Representative Portal's fast eFolder access is open to agents/attorneys, and current
  competitor pricing. Where you can't re-verify, say so and keep the July date stamp.
- Never invent competitor features, case holdings, regulation text, or market figures. If
  something is unknown, write it as an open question with what it would take to resolve.
- Before finalizing, dispatch the `citation-verifier` agent on every case, CFR, USC, and
  Federal Register citation in the document, and fix what it flags.
- Illustrative examples (e.g., a fictional veteran's case) must be labeled illustrative,
  and any dollar figures in them must be computed from stated, sourced rates.
  </epistemic_rules>

<thinking_expectations>
Critically examine the concept rather than transcribing the existing spec. In particular,
reach and defend a position on:

- Whether "CUE engine" is the right framing, or whether the durable product is broader
  (earliest-effective-date optimization across all claim types, with CUE as one module),
  and what that changes in requirements and market size.
- Whether accredited attorneys/agents are the right first buyer versus VSO organizations,
  specialist CUE firms, or a licensing/partnership deal with an incumbent — given the
  ~6,720-professional ceiling.
- Which requirements are truly needed for an MVP that proves value, and which are
  premature. Cut scope you can't justify.
- How the product earns professional trust when legal-RAG tools hallucinate 17–33% of the
  time: what the human-review gate, citation grounding, and audit trail concretely look like.
- What legally limits each monetization path (accreditation and fee rules under 38 U.S.C.
  § 5904 and 38 C.F.R. §§ 14.629–14.637, Privacy Act, 38 U.S.C. §§ 5701/7332), stated as
  verified constraints or flagged for counsel — not assumed.

Where the existing research is thin or you disagree with it, say so and explain why.
</thinking_expectations>

<document_structure>
Organize the document as below. Headings may be refined, but keep this order and coverage —
it moves from "what is it" to "how would we build it" to "should we."

**Front matter** — title, date, author line ("Prepared with Claude"), one-paragraph purpose
statement, table of contents, and a source/provenance key explaining the number labels.

**PART A — THE PRODUCT**

1. **Executive summary** (about one page). What the product is, who pays for it, the
   problem, why now, what it is not, and the headline viability verdict with confidence.
   A reader who stops here should have the full picture.

2. **Domain primer for newcomers.** Only what's needed to understand the product, explained
   through the product's job, not as a law lecture: how VA disability compensation works;
   the claims file (C-file / eFolder); rating decisions and when they become "final";
   what an effective date is and why it determines back pay; what CUE is and how it differs
   from an ordinary appeal; the three-part CUE test; who accredited agents/attorneys are,
   power of attorney, and how they get paid (contingency fees capped by regulation); why
   "the law as it read on the decision date" matters. Close with a **worked illustrative
   case** that follows one fictional veteran from an old denial to a CUE motion and shows
   where the money comes from. Include a glossary table.

3. **Problem and opportunity.** How this work is done today (who, how long, what goes
   wrong, what it costs), why it is error-prone, and the size of the value at stake per case.

4. **Users and jobs-to-be-done.** Primary, secondary, and explicit non-users (including
   veterans directly, and why the product isn't sold to them). For each: context, goals,
   pains, what "done well" looks like.

5. **End-to-end product walkthrough.** The full journey from "representative takes on a
   veteran" to "filing submitted," as a before/after comparison: every step, who does it,
   what the system does, what the human decides, and what artifact results. A simple flow
   diagram (Mermaid or ASCII) is welcome.

6. **Scope.** Goals, non-goals (e.g., no autonomous filing, no direct VA system access by
   the vendor), and MVP vs. later phases, aligned with or deliberately departing from the
   Addendum's phase plan.

7. **Functional requirements.** Numbered `FR-1…n`, grouped by capability (ingestion,
   timeline, point-in-time law, CUE analysis, effective-date analysis, drafting, review &
   audit, case management, calculators). For each requirement:
   - **Requirement** — one testable sentence.
   - **Why** — the user job or risk it serves.
   - **How it could be implemented** — concrete approach, data, models/algorithms, and the
     hard parts.
   - **Acceptance criteria** — how we'd know it works (accuracy thresholds where relevant).
   - **Phase** and **dependencies/risks**.
     Map each to the original F1–F10 where applicable, and note anything you added or cut.

8. **UX overview.** Information architecture, primary screens and their purpose (case
   intake, timeline view, decision detail, CUE analysis, law-at-date viewer, draft editor,
   review queue), the human-review gate as an explicit interaction, how citations and
   confidence are surfaced, empty/error states (bad OCR, missing documents), and
   onboarding. Low-fidelity wireframe sketches in ASCII are welcome for the 2–3 core screens.

9. **Technical requirements.** Reference architecture; data sources and corpora (eCFR
   versioner, GovInfo, Federal Register, pre-1997 reconstruction, BVA/CAVC/Fed. Cir.
   decisions) with coverage and licensing; ingestion and OCR pipeline; the evidentiary
   timeline data model; retrieval and reasoning design; citation grounding and verification;
   evaluation strategy (gold sets, accuracy metrics, regression testing); security, privacy,
   and compliance architecture; non-functional requirements (latency, cost per case,
   auditability, retention); build-vs-buy; and a rough per-case cost of goods (OCR + model
   tokens + storage) with its assumptions.

10. **Legal and compliance constraints on the product.** What the product may and may not
    do or claim, and how each constraint shapes design and marketing.

11. **Risks, assumptions, and open questions.** Ranked by how load-bearing they are, each
    with how to retire it.

**PART B — SHOULD WE BUILD IT?**

12. **Viability assessment.** Score desirability (is the pain real and paid for),
    feasibility (can we build it to the required accuracy), viability (does the business
    work), and durability (can it be defended). For each: evidence, verdict, confidence, and
    what evidence would change it. End with an overall verdict and the conditions under
    which it flips.

13. **Monetization paths.** Enumerate the plausible paths — e.g., per-seat SaaS, per-case
    credits, firm/site licenses, VSO-organization licenses, a free screening tool as lead
    generation, data licensing of the point-in-time corpus, API/white-label to incumbents,
    acquisition by an incumbent — plus any you find better. Compare them in a table:
    buyer, pricing mechanism, legal permissibility, revenue potential, effort, risks. Then
    recommend a primary path and sequence.

14. **Revenue model.** A bottoms-up model built from stated assumptions: reachable
    accounts, conversion, seats per account, price, credit attach, churn, ramp, CAC, gross
    margin (from the §9 cost of goods). Show Years 1–3 under worst / conservative / base /
    optimistic scenarios, a sensitivity table on the 3–4 inputs that swing it most, and
    break-even. Compare against `REPORT.md §4` and explain any differences. Show the
    arithmetic so a reader can audit it.

15. **Recommendation and next steps.** Build, don't build, or build only if — with the
    specific gate criteria (tie to the Phase V checklist) and the first 90 days of work.

**Appendices** — glossary (if not fully in §2), source map (which source supports which
section), verification log (what you re-verified today, what remains carried forward,
citation-verifier results), and a change log against the original spec.
</document_structure>

<writing_standards>

- Plain English. Define every term of art at first use; after the primer, use terms
  consistently. Prefer a concrete example to an abstract description.
- Use tables for comparisons and requirement matrices, prose for reasoning, numbered lists
  where order matters. Every section should earn its place; keep each as long as its
  content needs and no longer.
- Distinguish clearly between what is known, what is assumed, and what you recommend.
- Write in a direct, neutral voice; state conclusions plainly and attach their reasons.
- End with a "Research assistance, not legal advice" disclaimer, since fee-rule and
  accreditation interpretations should be confirmed by counsel.
  </writing_standards>

<quality_check>
Before finishing, check the document against these and fix any gaps:

1. A reader with no VA background can explain the product, its user, and its money
   mechanism after the Summary and Primer alone.
2. Every functional requirement has a why, an implementation approach, and acceptance
   criteria; nothing in the UX or technical sections lacks a corresponding requirement.
3. Every number carries a provenance label and source; every revenue figure can be
   recomputed from the shown assumptions.
4. All `REPORT.md §5` corrections are honored, and every `REPORT.md §6` open item is
   either resolved (with source) or carried into §11 / §15.
5. `citation-verifier` has been run and its findings applied; the verification log says so.
6. The viability verdict follows from the evidence presented, and the conditions that
   would flip it are explicit.
   </quality_check>

<deliverable>
Write the document to `va-cue-system/PRODUCT-SPEC-AND-VIABILITY-<YYYY-MM-DD>.md` (today's
date). Do not modify the existing research files. When done, reply with the file path, the
overall verdict in one sentence, and the three open questions that most affect it.
</deliverable>
