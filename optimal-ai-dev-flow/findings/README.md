# Phase B Findings — Index and Cross-Workstream State

_All 9 workstreams complete, 2026-08-01. Input to Phase C._

| File                           | Lines | Claims | Headline                                                                                            |
| ------------------------------ | ----- | ------ | --------------------------------------------------------------------------------------------------- |
| `w1-dev-loop.md`               | 388   | 77     | Benchmark figures are real but **stale**, not fabricated — except the open-weight side              |
| `w2-orchestration.md`          | 632   | 7      | The desired cross-project session topology **is not a supported configuration**                     |
| `w3-verification.md`           | 247   | 27     | Judge-Builder ≠ multi-agent fan-out; **routing the Judge cheap reduces recall**                     |
| `w4-documentation.md`          | 1134  | 10     | Context files **increase** cost 20–23% with no success-rate gain; 6 of 10 claims refuted            |
| `w5-cost-routing.md`           | 273   | 53     | The $80–120/mo target is **arithmetically impossible**; tier routing largely moot under flat rate   |
| `w6-domain-rampup.md`          | 317   | 3      | Explanation-generation is the one validated calibration instrument; procedures show **no** illusion |
| `w7-process-diagnosis.md`      | 893   | 0      | Every automation-failure statistic traces to marketing; failure mode is **arrested scaling**        |
| `w8-productized-consulting.md` | 657   | 2      | **Residuals clauses do not cover a knowledge repository**; the 80/20 ratio has zero evidence        |
| `w9-composition.md`            | 737   | 7      | Review capacity binds — proven at n=802/196,212 PRs; the corpus **inverted its own source**         |

**Aggregate verdicts:** CONFIRMED 81 · UNVERIFIED 51 · REFUTED 15 · STALE 10 · PARTIALLY CONFIRMED 10 · SKIPPED 2 · CONTESTED 1.

The 51 UNVERIFIED (29%) is the headline number for corpus reliability: nearly a third of its
falsifiable claims could not be substantiated against current evidence.

---

## Verdict vocabulary is NOT uniform — do not merge mechanically

The Phase B spec allowed five verdicts (`CONFIRMED` / `STALE` / `REFUTED` / `UNVERIFIED` /
`SKIPPED`). W3 additionally used `PARTIALLY CONFIRMED` (10 rows) and
`CONTESTED / PARTIALLY REFUTED` (1 row).

**These were deliberately left as written rather than normalized.** Rewriting another agent's
verdict labels would mean making judgment calls about evidence this orchestrator did not gather,
and "partially confirmed" frequently encodes a real distinction (mechanism confirmed, magnitude
unchecked) that flattening to CONFIRMED or UNVERIFIED would destroy. Phase C should read the row's
Notes column, not just its label.

---

## Convergences — independent workstreams that reached the same conclusion

These are stronger than any single finding, because the agents could not see each other's work.

1. **X-01 is settled.** W1 and W3 independently concluded that Anthropic's fan-out warning targets
   _parallel decomposition across many workers_, while a Builder/Judge loop is two roles,
   sequential, bounded, on one artifact — architecturally different, and matching a Writer/Reviewer
   pattern Anthropic's own current docs recommend. Different evidence, same answer.
2. **Client separation is required by two independent layers.** W2 found every cross-project
   context-sharing mechanism is simultaneously a leak path (harness mechanics; user-scope imports
   load without an approval dialog). W8 found residuals clauses cover only _unaided memory_ and
   explicitly exclude recorded material — so a per-client knowledge repo has no contractual
   protection at all. Mechanics and contract law converge on hard structural separation with a
   one-way flow rule.
3. **Unsourced numbers propagate everywhere — five workstreams caught it.** W1 (DeepSeek V4
   resolves to no model), W2 (a vendor re-serving its own blog as third-party validation), W5
   ($1,600 was an assumption presented as data), W7 (a 2016 marketing brochure behind 10
   citations, with a population explicitly selected on failure), W9 (two cited studies that exist
   nowhere outside the pages citing them). This is a property of the wider literature, not just
   this corpus.

---

## Collisions — Phase C must adjudicate, not average

1. **X-03 (ceremony) — W1 and W4 disagree on whether it resolves.** W1: unresolved, no controlled
   comparison exists, and the load-bearing "40% token reduction from AI.md" could not be
   corroborated. W4: resolves on an axis neither corpus position considered — **existence vs.
   elaboration**. Existence pays enormously (0% → ~65% compliance, Cohen's h = 1.93); elaboration
   pays nothing (size, position, architecture, inter-file conflict, overviews all measured null;
   files ratchet ~4:1 additions to deletions). **W4 carries the stronger sources** (ETH
   Zurich/LogicStar purpose-built benchmark; a 1,650-session factorial with affirmative-null
   BF₁₀ = 0.096). Recommend adopting W4's axis and recording W1's null as consistent with it.
2. **C-107's direction is inverted, not merely unsupported.** W1 could not corroborate "AI.md cuts
   tokens 40%." W4 found evidence for the _opposite_: repository context files **increase**
   inference cost 20–23% (p < 0.001) with no significant success-rate change, across four models
   and two benchmarks. Phase C should state the inversion explicitly — this figure underwrites
   much of the corpus's structural prescription.
3. **W4 contradicts Anthropic's own documentation on CLAUDE.md size**, and flagged the tension
   rather than deferring to the vendor. Phase C should preserve that framing.
4. **Cheap-tier routing, two angles.** W3: routing the Judge/reviewer to a cheap model reduces
   defect recall (self-review and same-family review degrade; OpenAI's critic needed
   frontier-class capability). W5: tier routing is largely moot for interactive work under a flat
   subscription anyway. Not contradictory — compose them.

---

## Contradiction register status

| ID                                            | Status                                                                                                          | Owner         |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------- |
| X-01 multi-agent fan-out                      | **RESOLVED** — not the same pattern                                                                             | W1 + W3 agree |
| X-02 cost architecture                        | **TESTED** — decision rule delivered, not a verdict (as specified). 80/15/5 ties to no measured result anywhere | W5            |
| X-03 ceremony level                           | **CONTESTED** — see Collisions #1                                                                               | W1 vs W4      |
| X-04 bottleneck location                      | **RESOLVED** — review capacity binds; Position B is unfalsifiable as written                                    | W9            |
| X-05 $800 vs $1,600                           | **RESOLVED** — $800/93% correct; $1,600 was v1.md's own assumption. C-099, C-100, C-139 refuted                 | W5            |
| X-06 benchmark flip                           | **PARTIALLY RESOLVED** — different constructs; neither cited config is current                                  | W1            |
| _(new)_ fix-first vs. automate-the-happy-path | **SURFACED, uncharacterized**                                                                                   | W7            |

---

## Known limits of this phase

- **Five workstreams exhausted their web-search budget** (W1, W2, W5, W6, W8) and marked the
  remainder UNVERIFIED rather than guessing. Each lists specifics in its Gaps section. The
  highest-value unclosed items: Jørgensen's software-estimation literature (W8, for time-boxing),
  cultural consensus theory's sample-size properties (W6, the only formal shape for a
  business-domain calibration instrument), and two arXiv preprints on context rot (W2).
- **No controlled study exists for the code-free knowledge repository** (W4) — every measured
  source in that field borrows its oracle from a compiler or test suite. W4 flagged the operator's
  own VA corpus (40 of 109 citations misstated — a labelled set with a known base rate) as the one
  place they could generate evidence that does not currently exist anywhere.
- **No quantitative anchor exists for a solo reviewer's ceiling** in the operator's units (W9).
  The closest transferable number is from knowledge work, not code: single-reviewer screening
  misses a median 5% of relevant material vs. dual review.
