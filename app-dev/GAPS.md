# Gaps and Open Questions

**Date:** 2026-09-29

Everything this run could not answer, and what would answer it. Listed because an ultradeep run that hides
its holes is worse than a shorter one that names them.

---

## 1. Angles not completed

| Angle | State | What would close it |
|---|---|---|
| **A6 — Architecture quality** | **Now covered** (late, in Phase 7). ADR-violation detection accuracy, Nx/Turborepo/dependency-cruiser boundary enforcement, and GitClear's 623M-change maintainability data were all obtained. Residual gap: **no independent measurement of symbol-aware/LSP editing** (Serena MCP, Aider repo-maps) on edit accuracy. | A controlled comparison of agent edit accuracy with and without symbol-aware tooling on the same repo |
| **A3 — Orchestration loops** | **Now covered** (late, in Phase 7). Multi-agent debate (Anthropic vs Cognition), self-refinement gain decay, LLM-judge bias, SpecBench reward-hacking scaling, and the escalation-channel intervention were all obtained. Residual gaps: durable orchestration (Temporal/Inngest/LangGraph) and git-worktree/container parallelism were **not re-verified**; Reflexion's 91%-HumanEval figure is secondhand only and is not used. | Fetch the durable-orchestration docs and the primary Reflexion paper |
| **A12 — App-factory products** | **Now covered** (late, in Phase 7). All nine named products assessed, plus the Lovable BOLA breach and the Replit destructive-action incident. Residual gaps: Blitzy's own pricing page 403'd (pricing is secondary-sourced); no current 2026 pricing fetched for Replit, Lovable, Bolt, Devin, Cosine or Codegen; the Answer.AI Devin study was never located at a primary URL. | Fetch each vendor's current pricing page and the primary Answer.AI study |

---

## 2. Unverified numbers and claims carried in the report

| Item | Status | What would resolve it |
|---|---|---|
| SWE-Bench+ leakage/weak-test percentages (~33% leaked solutions, ~25–48% weak tests, 52%→26% after filtering) | **Excluded from the report.** PDF undecodable on two attempts | An HTML mirror or OpenReview text view of arXiv 2410.06992 |
| SWE-bench Pro: same model 93.9% Verified vs 45.9% Pro | **Excluded.** Primary leaderboard 429'd; single blog snippet only | Direct fetch of the SWE-bench Pro leaderboard |
| DORA 2026: brownfield AI gains ≤10% vs greenfield 35–40% (~100k-developer telemetry) | **Excluded**, though it would have been one of the most decisive figures for this exact question | The DORA "ROI of AI-Assisted Software Development" report and the underlying Stanford/Denisov-Blanch study |
| METR "doubling every 4.3 months" time-horizon acceleration | **Excluded** — the fetched METR page did not state it | The primary METR time-horizons paper |
| Long-horizon degradation by task-length bucket (76.3%→59.8%→50.5%→52.1%) | **Excluded** — search synthesis only | Direct fetch of arXiv 2609.01660 |
| Terminal-Bench and Aider polyglot current scores | **Excluded** | The live leaderboard pages |
| Screenshot-feedback loops improving UI fidelity | **Excluded** — arXiv PDF undecodable | An HTML version of arXiv 2604.05839 |
| `firebase login:ci` CI-auth guidance (used in `GUIDE.md` §1) | **Marked unverified** — relayed by a retrieval agent, not fetched by the orchestrator | One fetch of the Firebase emulator/CI docs section |
| Maestro CI documentation | **Unreachable** (404 after redirect) | `https://docs.maestro.dev/maestro-cloud/run-maestro-tests-in-ci` |
| Claude Code subagent `model:` field exact accepted values | **Paraphrase only** — the retrieval agent could not obtain a verbatim quote after two attempts | One fetch of the subagents doc |
| Anthropic cache-read 0.05x exception for one flagship model | **Flagged as unusual** — fetched from Anthropic docs but worth re-checking before budget math relies on it | A second fetch of the prompt-caching page |
| `npx stryker run --incremental` exact flag | **Marked unverified** in `GUIDE.md` | The StrykerJS incremental-mode doc page |
| Mutation-testing cost/reproducibility at scale | **Practitioner reports, search-only** | Run Stage 0 of `ADOPTION-PLAN.md` — this one you can answer yourself in a day |
| Approval-testing degradation quotes | **Search-only**, used as reasoning not evidence | A fetched source on approval-test practice |
| Devin ACU pricing | **Not found** — billing pages 404'd | The current Devin billing URL |
| Sentry Seer capability and accuracy | **Not found** — page 404'd | The current Seer product page plus any independent evaluation |
| LangSmith / Braintrust / AgentOps / W&B Weave | **Not researched** | A focused observability pass |

---

## 3. Genuine evidence gaps in the field, not just in this run

These are not retrieval failures. Dedicated searching found nothing either way.

1. **Agent-authored Firestore security rules.** No positive or negative measured evidence exists on whether
   LLM agents write correct rules in Firestore's bespoke DSL. For this operator that is 439 and 951 lines of
   rules plus 21 and 59 composite indexes. This is the single most consequential gap in the report, and it
   is why rules carry a mandatory human gate rather than a confidence score.
2. **Composite index correctness and Cloud Functions v2 authoring by agents.** Not researched at all; no
   queries were run.
3. **No validated vacuous-test detector.** Beyond mutation testing and generic test-smell tools, no product
   or published detector was found with measured precision/recall for identifying assert-true, tautological,
   or mocked-to-death tests — specifically none evaluated against LLM-authored tests.
4. **No measured clarifying-question behaviour inside a shipped harness.** All A10 evidence is academic
   benchmarks (HiL-Bench, AskBench, Ask-or-Assume). Nobody has published what Claude Code, Cursor or Copilot
   actually do about ambiguity on a large brownfield repo.
5. **No head-to-head on ask-up-front vs assume-and-record.** The report's assumption-ledger design rests on
   a mechanical constraint (unattended mode cannot ask) plus research on question-asking calibration, not on
   a comparison of the two strategies.
6. **No cost anchor for whole-feature or whole-app autonomous runs.** The only verified per-task figures are
   the official SWE-bench board's $0.07–$1.53 for ~1-hour single-function tasks. Every larger figure in this
   directory is an explicitly labelled extrapolation.
7. **No brownfield trial at this repo scale.** Nothing in the literature runs an agent against a ~195k-LOC
   three-surface TypeScript product and reports a pass rate. The closest is a single self-published case
   study on a 717k-LOC TypeScript app, which is not independent.
8. **ProgramBench-to-product-app transfer.** ProgramBench measures reimplementing mature programs (SQLite,
   FFmpeg). Nobody has published the equivalent for greenfield product applications, which is the operator's
   actual greenfield case. The 4.5% figure is therefore a hard bound on a harder task, not a prediction.
9. **Whether the 2014 coverage-effectiveness result transfers to LLM-generated suites.** A 2026 replicability
   study reportedly disagrees for that specific context; not fetched, so unresolved.
10. **Mutation-score norms for RN / Firebase Functions / Drizzle codebases.** Every published mutation score
    found is generic JS/TS or Angular. There is no benchmark to ratchet against except your own baseline.

---

## 4. Questions the operator can answer faster than research can

Cheap, local, and worth more than any further literature search:

1. What is the mutation score and full-run wall-clock of `homegroups/functions` today? (`ADOPTION-PLAN.md`
   Stage 0 — and it may kill the primary gate.)
2. Can the tamper hooks actually be bypassed? (Stage 1, five adversarial attempts.)
3. On your repo, does a separated test-author/implementer run produce a mergeable PR, and does review take
   less time than writing it yourself? (Stage 2 — the local replication of the METR question.)
4. Does the agent's Firestore rules diff survive your review unchanged? (Stage 4 — and if it nearly doesn't,
   the answer is permanent: hand-write rules.)
5. What does a feature actually cost you in dollars, from `total_cost_usd` in the result metadata?
