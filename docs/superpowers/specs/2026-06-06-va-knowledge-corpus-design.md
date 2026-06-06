# VA Knowledge Corpus — Design Spec

> Date: 2026-06-06 · Status: approved (pending spec review)

## Problem

The `va-rating-strategy` skill re-researches all VA domain knowledge (claims
process, VASRD criteria, compensation tables, benefits, presumptives) from scratch
for every veteran. That knowledge is identical across veterans and mostly stable, so
re-deriving it each time is wasteful, slow, and risks inconsistent or contradictory
facts between engagements.

## Goal

Extract the shared domain knowledge into a persistent, cited, **RAG-ready** Markdown
corpus that the operator maintains and reuses across all veterans. The corpus
compounds in value: every engagement makes the next faster and more consistent. It
must be embeddable into a vector store later (to back a product) with zero retrieval
infrastructure today.

## Non-Goals (v1)

- No self-serve application, accounts, or UI. Operator-run from Claude Code only.
- No vector database, embeddings, or retrieval service. Markdown is the source of
  truth; RAG indexing is a future step.
- No standalone corpus-refresh tooling. Staleness is caught check-on-use.
- **No changes to the existing skills or prompts.** The original `va-rating-strategy`
  skill and both `prompts/va-rating-strategy-skill*.md` files are preserved
  unchanged. The corpus-aware behavior ships as a NEW skill.

## Decisions

| Decision          | Choice                                                     |
| ----------------- | ---------------------------------------------------------- |
| End-goal          | Shared knowledge base, operator-run; product-capable later |
| Storage/retrieval | Curated Markdown corpus, RAG-ready (no infra now)          |
| Freshness         | Per-doc freshness metadata + check-on-use                  |
| Corpus directory  | `va-knowledge-base/`                                       |
| Refresh tooling   | None in v1 (caught during skill Phase 1)                   |
| Existing skills   | Preserved unchanged; new skill added                       |

## Architecture

Two clearly-bounded layers:

1. **Shared corpus** — `va-knowledge-base/`. Curated, cited domain facts. Built once,
   maintained over time, reused for every veteran.
2. **Per-veteran subjects** — `<veteran-slug>/`. Profile, strategy, resources. These
   **cite** corpus docs rather than re-deriving domain facts.

The new corpus-aware skill is the consumer: it reads the corpus, fills gaps, writes
improvements back, then proceeds with the per-veteran work.

### Corpus structure

```
va-knowledge-base/
  INDEX.md                  # map of the corpus + freshness dashboard table
  process/                  # claims lifecycle, C&P exams, appeals, effective dates
  vasrd/                    # rating schedule, one file per body system
  compensation/             # comp rate tables, VA math (38 CFR 4.25), bilateral factor
  benefits/                 # by tier (10-100%), TDIU, SMC, healthcare, dependents, state
  presumptives/             # PACT Act, presumptive conditions
  evidence/                 # nexus letters, DBQs, lay/buddy statements
  representation/           # VSOs, VA accreditation, fee law (38 CFR 14.636)
```

### Document contract

Every corpus doc carries frontmatter plus inline citations on every claim:

```yaml
---
topic: compensation-rates-2026
last_verified: 2026-06-06
volatility: annual # stable | annual | volatile
sources:
  - https://www.va.gov/disability/compensation-rates/veteran-rates/
---
```

- `stable` — 38 CFR rating criteria, process. Trust ~1 year+.
- `annual` — compensation tables, income thresholds. Re-verify if past the current
  benefit year.
- `volatile` — presumptives, legislation-driven items. Re-verify on every use.

Frontmatter + clean Markdown + inline citations make each doc trivially chunkable and
embeddable later, with provenance preserved. This is the RAG-ready payoff.

### INDEX.md

Doubles as a freshness dashboard: a table listing each doc, its `last_verified`
date, and `volatility`, so stale areas are visible at a glance. Maintained by the
skill as docs are added/updated.

## New Skill: `va-rating-strategy-kb`

A copy of `va-rating-strategy` whose **Phase 1** is replaced with "Consult & Extend
Corpus." All other phases (2 profile, 3 strategy+odds, 4 resources) and the ethics
guardrails are unchanged. The original skill remains available untouched.

### Phase 1 — Consult & Extend Corpus

1. Read `va-knowledge-base/INDEX.md`; identify which corpus docs this veteran's
   strategy will need.
2. For each needed doc: check `last_verified` against its `volatility` shelf life.
   - Fresh → use as-is, cite it.
   - Stale or missing → re-verify/research via `deep-research`, then write the
     new/updated doc back into the corpus with refreshed `last_verified` and sources.
3. Update `INDEX.md` for any added/changed docs.
4. Gate: proceed to Phase 2 only when every needed domain is covered by a fresh,
   cited corpus doc and confidence is HIGH.

### Phases 2-4

Identical to the original skill, except domain facts are cited from the corpus rather
than re-stated. Per-veteran subjects reference corpus docs by path + source.

## Data Flow

```
INDEX.md ──read──> identify needs ──stale?──> deep-research ──write──> corpus docs
                                  │                                       │
                                  └──fresh──────────────> cite ──> strategy.md / resources.md
```

## Error / Edge Handling

- **Missing corpus** — if `va-knowledge-base/` does not exist, the skill scaffolds it
  (INDEX.md + topic dirs) on first run, then proceeds as all-gaps.
- **Conflicting sources** — record both with citations; prefer primary (va.gov / eCFR)
  and mark secondary as such, per existing accuracy controls.
- **Unverifiable claim** — mark `UNVERIFIED`; never promote to a corpus fact.
- **Stale volatile data at strategy time** — always re-checked on use, so a cached
  volatile doc cannot silently feed a strategy.

## Testing / Validation

Lightweight, content-and-prompt nature:

- Frontmatter validity: every corpus doc has `topic`, `last_verified`, `volatility`,
  `sources`.
- Freshness logic: a doc past its shelf life triggers re-verification in Phase 1
  (verify by walking the skill against a deliberately stale doc).
- Citation discipline: spot-check that strategy/resources outputs reference corpus
  paths and primary sources.
- Original skills unchanged: confirm `va-rating-strategy/SKILL.md` and both prompt
  files are byte-identical to pre-change.

## Future (out of scope)

- Embedding pipeline + vector store over the Markdown corpus.
- `corpus-refresh` skill that batch-scans and reports staleness.
- Self-serve product surface for veterans.
