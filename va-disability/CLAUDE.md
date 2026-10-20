# CLAUDE.md

Subject-level guidance for `va-disability/`, extending `../CLAUDE.md`. This subject
has outgrown the generic one-`REPORT.md` pattern — read this before touching files
here.

## Start here

**`REPORT.md`**'s "Start here" section is the live navigation index and is more
current than this file for document status — read it first. In short: the current
working docs are `planning-docs/MASTER-STRATEGY.md` (strategy), `CLAIM-ASSESSMENT.md`
(adversarial review), `planning-docs/100-PERCENT-SCHEDULAR-PATHWAY.md` (legal research),
and `planning-docs/NEXUS-LETTER-GUIDE-CHERIE.md` /
`planning-docs/CP-EXAM-PREP-MENTAL-HEALTH.md` (prep docs). The most recent
`COMPREHENSIVE-FINDINGS-*.md` is the source of truth for facts already
reconciled — don't re-derive something it already resolved unless a newer document
contradicts it. `knowledge-base.md`, `veteran-profile.md`,
`claim-maximization-research-2026-06.md`, and `planning-docs/strategy.md` /
`planning-docs/CLAIM-EXECUTION-PLAN.md` / `planning-docs/DO-THIS-WEEK.md` are
superseded and kept for history only.

> **⚠️ Document-precedence trap — read before trusting the list above.**
> `planning-docs/RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md` is **newer than**
> `MASTER-STRATEGY.md` (2026-07-06) and `CLAIM-ASSESSMENT.md` (2026-07-05) and **reverses
> positions in both** — most consequentially, its `[CORRECTION 2]`/`[CORRECTION 3]` open
> § 4.16 **TDIU development** and list VA Form 21-8940 as a filing action, contradicting
> MASTER-STRATEGY's "not pursuing TDIU." It also supplies a corrected occupational history
> (Dec 2024 job loss; June 2026 loss for performance/PIP resolved by negotiated severance).
> Likewise, both files carry internal `[SUPERSEDED]` markers pointing at
> `planning-docs/PATH-TO-100-PERCENT-2026-07-07.md` §9 for odds.
> **Reading only the documents named above produced three CRITICAL errors in a 2026-09-13
> drafting pass** (see `vre/CONSISTENCY-AUDIT-2026-09-13.md`). Always check the remediation
> plan and §9 before treating any strategy position as settled. Also note the newest-dated
> passage in `MASTER-STRATEGY.md` is a **2026-07-31** update buried in §3.

## Folder layout (reorganized 2026-07-15)

- **`planning-docs/`** — all internal plans, strategies, checklists, worklists, and
  prep guides (never submitted to VA; see `planning-docs/CLAIM-MASTER-BRIEF.md` §2.6).
- **`supporting-docs/`** — claim-facing/support material tracked in this repo: the
  nexus-letter Markdown transcriptions and suggested-language drafts. **Not to be
  confused with the gitignored `personal-records/supporting-docs/`**, which holds the
  actual signed PHI evidence (statements, PDFs, the signed nexus letter).
- Root — navigation (`REPORT.md`, this file, `DOCUMENT-PROVENANCE.md`), research,
  audits/assessments, and reference KBs.
- **`vre/`** — **VR&E / Chapter 31** (Veteran Readiness & Employment). A **separate benefit
  track** from the compensation claim: different statute (38 U.S.C. ch. 31), different
  regulations (38 C.F.R. part 21 subpart A), different decision-maker (a VRC, not an RVSR),
  different appeal posture. Self-contained — start at `vre/README.md`. Holds the appointment
  prep doc, a citation-verified Chapter 31 legal KB, a benefits/tracks/rates/forms KB, and a
  consistency audit. Shares only the C-file with the compensation claim, which is where the
  cross-claim risk lives.
- `document-analysis/` — per-document deep-analysis reports.

## Subject-specific tools

- **`/va-claim-status`** skill — fast status snapshot (deadlines, next actions,
  blockers) from the existing synthesis docs, without re-reading the full corpus.
- **`/va-rating-strategy`** skill — the gated four-phase deep-research workflow
  (knowledge base → veteran profile → strategy+odds → resources) this subject's
  strategy docs were built from.
- **`/rate-claim`** skill — record-only mock VA adjudication of the
  `supporting-docs/` markdown evidence (intake → C&P examiner → RVSR →
  adversarial reviewer), producing a dated rating report in `ratings/` where
  every finding carries a suggested remediation. Blind to all strategy docs by
  design. Requires `rater-kb/` (STATUS: KB COMPLETE) and explicit user request —
  never auto-run. For strategy/odds questions use `/va-rating-reassess`.
- **`citation-verifier`** agent (repo-level, `../.claude/agents/`) — run before
  finalizing any document here that cites case law or regulation.
- **`claim-consistency-checker`** agent (repo-level) — run after editing the
  personal statement, any buddy/spouse statement, or the nexus-letter guides.

## Sensitive data handling

- `personal-records/` (DD-214, clinical records, the Erica email chain,
  supporting-docs) is real PHI/PII and is gitignored — never remove it from
  `.gitignore` or copy its contents elsewhere.
- `ClaudeDisabilityAssets/` and `ClaudeChat/` also contain PII (real name, spouse
  statement drafts, rating strategy tied to specific medical facts) but are
  currently **untracked, not gitignored** — treat them as sensitive as
  `personal-records/` until that's fixed; don't `git add` them without checking
  with the user first.
- Do not draft or edit wording for a witness's own buddy/spouse statement — flag
  inconsistencies and let them resolve it in their own words (see
  `claim-consistency-checker`'s hard rule). A prior coached-statement email thread
  is treated in `CLAIM-ASSESSMENT.md` Part 0 as the single biggest credibility risk
  to this claim.
