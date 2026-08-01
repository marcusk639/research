# Corpus Ledger — Highlights

_Digest of `corpus-ledger.md` §3 (contradictions) and §5 (extraction notes) | 2026-08-01_
_Phase A output: 211 claims (`C-001`–`C-211`) across 7 files, 6 contradictions, 0 verdicts._

---

> **PHASE B VERDICT (2026-08-01): the fabrication hypothesis below was TESTED AND MOSTLY
> REFUTED.** W1 resolved the core Claude/GPT/Copilot figures (88.6%, 80.0%, 69.2%, 78.9%, 83.4%)
> to real, dated, independently-tracked leaderboard entries, cross-corroborated across llm-stats,
> vals.ai, and snorkel.ai. **The defect is staleness, not fabrication** — every figure was
> superseded within weeks to months, and the Terminal-Bench comparison was already stale the day
> it was written. The hypothesis survives only for the open-weight side: **"DeepSeek V4" resolves
> to no model at any benchmark score anywhere**, and the cited Copilot SWE-bench Pro figure
> (41.0%) matches no current data (~55.6% found). The section below is retained as the Phase A
> record of why this was investigated first — it was the right question, and the answer was no.

## The headline (as of Phase A): the corpus may be citing numbers that don't exist

The single most consequential finding is not a contradiction — it's a credibility problem
flagged in §5. Four separate signals, all pointing the same way:

| Signal                                             | Detail                                                                                                                                                                                                                           |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Benchmark figures look fabricated**              | 88.6% / 69.2% / 78.9% appear precise to a tenth of a point across two independently-styled documents **with no shared citation**. §5: "a pattern more consistent with fabricated-plausible figures than sourced benchmark runs." |
| **v1.md contradicts its own table**                | The 59.0% SWE-bench Pro score is attributed to "MiniMax M3 / GLM-5.1 orchestration" while that column's header and every other row say "DeepSeek V4."                                                                            |
| **Same competitor, 2.5× different context window** | Copilot/Codex is 200k tokens in v1.md (C-095) and 512k in v2.md (C-119), never reconciled.                                                                                                                                       |
| **Model names are from different eras**            | v2.md's benchmark table says "Opus 4.8" but its own setup instructions use `anthropic/claude-3.5-sonnet` — the setup half was never updated with the benchmark half.                                                             |

**Why this dominates everything else:** the corpus's central decision — stay on Claude Code Max —
rests on a benchmark comparison. If those numbers don't resolve to a real leaderboard entry, the
tool-choice rationale is unfounded regardless of how the contradictions below resolve. **W1 must
check whether any of these figures are citable at all before anything downstream trusts them.**

Neither `v1.md` nor `v2.md` carries an internal date. The only dating evidence in the entire
corpus is `workflow-plan-v2.md`'s own characterization of them as "2026 Q1" and "2026 Q2" — which
is itself a claim, not a fact.

---

## The six contradictions

**Four known, two discovered.** Compressed; full positions with quotes in §3.

| #        | Conflict                                                                                                                                       | Why it matters                                                                                                                                                                            | →      |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **X-01** | Multi-agent fan-out ranked _worst of 11_ for coding vs. Judge-Builder as the corpus's _flagship_ recommendation                                | Determines whether `workflow-plan-v2.md`'s Phase 3 judge-review skill is sound practice or the exact anti-pattern ranked dead last                                                        | W1, W3 |
| **X-02** | Flat-rate arbitrage vs. tiered routing — **and three unreconciled ratios for the same operator**: 70/30, 80/15/5, and a separate A/B/C mapping | The $80–120/mo blended target depends entirely on 80/15/5 holding                                                                                                                         | W5     |
| **X-03** | "Dumbest thing that works" vs. mandatory AI.md / Definition-of-Done / judge schemas                                                            | Quality bar pulls toward ceremony; review capacity pulls toward minimalism. The corpus argues both without reconciling                                                                    | W1, W4 |
| **X-04** | Review capacity vs. cost/throughput as the binding constraint                                                                                  | **A disagreement of omission** — four cost-focused docs never once name review capacity. A cost program that raises velocity may violate the stated hard constraint without ever checking | W9, W5 |
| **X-05** | _(discovered)_ Same anecdote, two subscription totals: **$800 / 93%** vs **$1,600 / 89%**                                                      | Sits directly under the corpus's most load-bearing proof of subscription arbitrage                                                                                                        | W5     |
| **X-06** | _(discovered)_ Benchmark winner flips by benchmark: Claude leads SWE-bench Pro by 28 pts; Codex leads Terminal-Bench by 4.5                    | `workflow-plan-v2.md` picks SWE-bench Pro as "more relevant" without verification                                                                                                         | W1     |

X-02's third wrinkle is worth restating: **`workflow-plan-v2.md` adopts 80/15/5 as policy without
ever addressing the 70/30 split or the earlier A/B/C mapping.** Three routing schemes, one
operator, no reconciliation.

---

## Coverage gaps — what the corpus never addresses

Confirmed against a full read of all seven files, not a sampling artifact.

- **The entire consulting side is absent (W6, W7, W8).** Zero prior art on domain ramp-up,
  process/org diagnosis before automating, or productized-consulting mechanics — pricing, scoping,
  phase gates, IP reuse, client-data confidentiality as general practice. The corpus is purely a
  software/AI-tooling optimization exercise.
- **Knowledge-repo coherence (W4) appears only as token-cost optimization** — never as
  documentation quality, doc-drift detection, or fact verification. Nothing on keeping a
  code-free repository internally consistent as it grows, despite that being half the work mix.
- **Multi-project shared context (W2) is unaddressed.** The corpus assumes one session against
  one repo. The desired topology — one orchestrator holding context _across_ projects — has no
  prior art beyond a single checkpoint-file mention.
- **Verification beyond unit/typecheck CI (W3).** No mutation testing, contract tests, golden
  files, or screenshot diffs.
- **Solo-operator capacity math (W9).** No WIP limits or context-switching cost, beyond the
  review-capacity thesis that the rest of the corpus ignores.

---

## Claim distribution

```
W1 (dev loop)      77  ██████████████████
W5 (cost/routing)  53  ████████████
W3 (verification)  27  ██████
W4 (docs)          10  ██
W2 (multi-project)  7  █
W9 (composition)    7  █
W6 (domain ramp)    3  ▌
W8 (productized)    2  ▌
W7 (process diag)   0
```

**W1 + W5 = 70% of the corpus.** The consulting half is 5 claims out of ~187. W7 is empty.

By type: RECOMMENDATION 70 · QUANT 51 · CAUSAL 33 · CAPABILITY 32 · REPO-FACT 25.

---

## What this means for Phase B

1. **W1 and W5 are verification-heavy** (130 claims between them) and will dominate wall-clock.
   Both also carry the forensic work — the fabricated-benchmark check (W1) and the $800/$1,600
   reconciliation (W5).
2. **W6, W7, W8 are pure open-field.** Nothing to verify; they build from zero. W7 has literally
   no assigned claims. Their findings files should be judged on research quality, not verdict
   counts.
3. **Expect a high REFUTED/STALE rate on QUANT claims.** Given the credibility signals above,
   treat every unsourced benchmark figure as guilty until cited.

---

## Known minor defect in the ledger

§5's sanity check reports "187 in §1, 24 in §2"; the run summary reported 186/25. Both total 211,
and all 211 IDs are unique and gap-free, so the handoff contract is intact — but the split between
the two tables is off by one somewhere. Harmless for Phase B, which addresses claims by ID.
