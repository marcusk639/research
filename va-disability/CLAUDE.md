# CLAUDE.md

Subject-level guidance for `va-disability/`, extending `../CLAUDE.md`. This subject
has outgrown the generic one-`REPORT.md` pattern — read this before touching files
here.

## Start here

**`REPORT.md`**'s "Start here" section is the live navigation index and is more
current than this file for document status — read it first. In short: the current
working docs are `MASTER-STRATEGY.md` (strategy), `CLAIM-ASSESSMENT.md` (adversarial
review), `100-PERCENT-SCHEDULAR-PATHWAY.md` (legal research), and
`NEXUS-LETTER-GUIDE-CHERIE.md` / `CP-EXAM-PREP-MENTAL-HEALTH.md` (prep docs). The
most recent `COMPREHENSIVE-FINDINGS-*.md` is the source of truth for facts already
reconciled — don't re-derive something it already resolved unless a newer document
contradicts it. Everything else at the top level (`knowledge-base.md`,
`veteran-profile.md`, `strategy.md`, `CLAIM-EXECUTION-PLAN.md`, `DO-THIS-WEEK.md`,
`claim-maximization-research-2026-06.md`) is superseded and kept for history only.

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
