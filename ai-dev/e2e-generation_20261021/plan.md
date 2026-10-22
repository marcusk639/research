# Phase 2 — Report plan

_Revised 2026-10-21 after a plan review: added F8–F10, disconfirmation controls, a consolidation step, an acceptance bar, and a section map._

## Scope note

The request covers "mobile apps backed by Firebase Functions". This run narrows to **React Native** because the reference target (regroup) is RN. The report must say so explicitly and note what changes for Flutter (e.g. Patrol) and for native Swift/Kotlin apps.

## Sections

| §   | Section (draft)                                                                                       | Angles                        | Would settle it                                                                                                                          | Would falsify it                                                                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| F1  | Mobile runtime layer: which E2E framework(s) a generator should emit                                  | A1, L                         | Independent reliability evidence; MCP/agent tooling maturity; RN compatibility                                                           | Evidence that the preferred runtime is chronically flaky on iOS, or doesn't support RN 0.72                                                                                                                                                      |
| F2  | What the research says LLMs can and can't do in test generation                                       | A2                            | Peer-reviewed numbers on pass rates, coverage, and oracle quality; the effect of filtering                                               | Strong evidence that unfiltered one-shot generation works well                                                                                                                                                                                   |
| F3  | Code → spec: comprehension strategy and spec format                                                   | A3, inventory                 | Evidence for agentic exploration beating long-context dumps; workable spec formats; intent-recovery methods                              | Evidence that whole-repo long-context reading is reliable at ~200k LOC                                                                                                                                                                           |
| F4  | The backend harness is the hard part: Firebase emulators, seeding, third parties, cross-client flows  | A4, L                         | Official emulator coverage and limits; Stripe/email/FCM strategies                                                                       | Evidence that full-fidelity emulation is turnkey                                                                                                                                                                                                 |
| F5  | Build vs buy vs compose: the commercial landscape                                                     | A5                            | What the products actually do; independent reviews                                                                                       | A product that clears the **"does it well" bar**: it emits durable test code (not only runtime agent runs), derives tests from source or spec rather than recording alone, supports RN, and has at least one independent (non-vendor) evaluation |
| F6  | Orchestration and quality gates: generate–run–repair, mutation/flake/oracle checks, human checkpoints | A6, A2                        | Documented loop patterns; reward-hacking evidence; mutation testing for E2E                                                              | Evidence that the loops converge without human review                                                                                                                                                                                            |
| F7  | Reference case: what regroup implies                                                                  | L, inventory                  | Local facts                                                                                                                              | — (see weighting rule below)                                                                                                                                                                                                                     |
| F8  | Novel approaches, each held to the same evidence bar as F1–F6                                         | A2, A3, A5, A6, Phase 7 delta | For each idea: closest published precedent and any measured result. If none exists, label it **speculative**                             | Precedent showing the idea fails, or costs more than it returns                                                                                                                                                                                  |
| F9  | Web half: E2E generation for the companion web app                                                    | A1, A5, Phase 7 delta         | Playwright (and its planner/generator/healer agents) as the web target; cost of migrating off regroup's deprecated Protractor `web/e2e/` | Evidence that the web half needs no separate runtime, e.g. one framework covers RN and Angular well                                                                                                                                              |
| F10 | Cost, time, and maintenance of "one command"                                                          | A6, A5, A2                    | Token/cost figures for multi-agent runs; wall-clock per phase; diff-aware regeneration and impacted-test selection                       | Evidence that a single run finishes in a practical budget and that suites stay valid as code changes                                                                                                                                             |
| S   | Synthesis → proposed `/generate-e2e` architecture, phased, with an honest automation ceiling          | all                           | —                                                                                                                                        | —                                                                                                                                                                                                                                                |

F8 candidate ideas (to evaluate, not assume):

- Mining specs from instrumented runs (traced exploration) instead of reading code alone.
- Firestore security rules and callable input validators used as executable oracles. They're written as intent, unlike UI code.
- Differential testing: run the same flow through web and mobile and diff the backend state.
- Sentry breadcrumbs or analytics events used as a source of real user flows and their frequencies.
- Mutation-score-guided generation: keep only tests that kill mutants (cf. Meta ACH).
- LLM-as-judge or vision-model oracles (e.g. Maestro `assertWithAI`), and the case against them.
- Record-and-replay from real sessions (e.g. Meticulous) as an alternative to comprehension.

## Hypotheses to test (not conclusions)

- H1: A single "one-command, fully comprehensive, fully working" run is unrealistic. A resumable, multi-phase pipeline with a human spec checkpoint is the realistic ceiling.
- H2: The environment (build, emulators, seeding, third-party stubs, driver stability) costs more than authoring the tests, so the generator should produce the harness first.
- H3: Code-derived oracles assert what the app currently does, not what it should do, so intent sources and human review are needed for the parts that matter.
- H4: Durable generated scripts plus a run–repair loop beat runtime agents for regression suites. Runtime agents are better suited to exploration and smoke tests.
- H5: Deterministic static extraction (routes, callables, collections, roles) should feed the LLM, instead of the LLM rediscovering those facts by reading. **Direct test:** the regroup inventory's answer on whether the React Navigation route graph is statically extractable. If it isn't, H5 narrows to callables, collections, and rules.

## Disconfirmation controls (confirmation-bias guard)

The hypotheses mirror regroup's prior failures, and the A1/A4 agent prompts were primed with those failures. To counter this:

1. **Queued disconfirming searches (Phase 7).** Each targets one hypothesis:
   - H1: case studies of fully automated, one-shot LLM E2E suites working at scale; "autonomous QA agent replaced manual E2E".
   - H2: evidence that environment setup is cheap or turnkey for Firebase + RN (e.g. templates, EAS + emulator recipes).
   - H3: evidence that LLM-generated oracles catch real intent violations without a human spec.
   - H4: production reports of runtime-agent testing (Firebase App Testing Agent, Momentic, QA Wolf) being cheaper or more reliable than scripted suites.
   - H5: evidence that pure LLM reading matches or beats tool-assisted extraction on repo comprehension.
2. **A fourth red-team persona, the "Hypothesis Attacker".** It reviews only H1–H5 and the sections built on them, and its sole job is to argue each is wrong. A hypothesis it refutes on the evidence is reported as refuted or as contested in Limitations. The other three personas keep the 2-of-3 rule for ordinary claims.
3. **Weighting rule for L-series evidence.** Regroup is one codebase, and its previous attempt used the user's own `mobile-e2e` skill. L-claims may illustrate a general claim but can't be its only support. Every general claim needs at least one external `[Sn]` source, and L-only claims are phrased as "in regroup…".

## Consolidation step (between Phase 3 and Phase 4)

Merge the per-angle ledgers (`angle-A*.md`) into the global `sources.jsonl`, `evidence.jsonl`, and `claims.jsonl`:

- Renumber to global `S`/`E`/`C` IDs, and keep a mapping from angle IDs to global IDs in `id-map.json`.
- Deduplicate by URL first, then by publisher and origin. Syndicated or vendor-repeated material counts as one independent source.
- Recount `independent_sources` per claim after deduplication. Claims that drop below the floor are demoted to `confidence: low`.
- Merge duplicate claims across angles, and record any cross-angle conflicts for Phase 4.

## Acceptance bar for the report (definition of done)

The synthesis is done when someone could write the `/generate-e2e` skill from it without further research:

- **Named phases**, each with its inputs, outputs (artifact files), the tool or agent type that runs it, and its stop condition.
- **Quality gates with explicit thresholds**, e.g. N reruns for the flake check, a mutation-score floor, and a required oracle-origin tag on each assertion. Thresholds the evidence doesn't support are labeled as starting defaults, not as findings.
- **Human checkpoints**: where they sit and what the human approves.
- **An honest automation ceiling**: what stays manual, stated with a confidence level.
- **A build order for regroup**: the first slice to implement and how it would be validated.
- **Cost and time estimates** at order-of-magnitude level, labeled with confidence.

## Section map to the required package (Phase 8)

| Package section                                  | Source                                                                                                                 |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Executive Summary                                | S, plus headline confidence for H1–H5                                                                                  |
| Introduction (scope / methodology / assumptions) | run_manifest.json, scope note, disconfirmation controls                                                                |
| Findings 1–8                                     | F1 · F2 · F3 · F4 · F5+F8 (landscape & novel) · F6 · F9 (web) · F7+F10 (regroup case, cost & maintenance)              |
| Synthesis                                        | S: proposed architecture, measured against the acceptance bar                                                          |
| Limitations & Open Questions                     | Refuted or unverified claims, conflicts, contested hypotheses, the RN-only scope, L-series caveat, unreachable sources |
| Recommendations                                  | Build order for regroup, what not to build, buy/compose options                                                        |
| Bibliography                                     | Global sources.jsonl (URL + quality tier)                                                                              |
| Methodology Appendix                             | Mode, source counts before and after dedup, red-team outcomes per persona, number of rounds                            |
