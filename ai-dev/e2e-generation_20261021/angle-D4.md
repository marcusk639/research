# D4: red-team delta retrieval (main-session verified)

Sources raised by the Phase 6 red-team personas. The main session re-fetched each one and checked it on 2026-10-21, via raw GitHub, the GitHub API, or `pdftotext` of the arXiv PDF. Only figures the main session located in the raw text are recorded. Figures a persona reported that could not be located are listed under Conflicts & gaps.

## Sources

D4-S1 | https://github.com/firebase/firebase-tools/blob/master/src/mcp/prompts/firestore/generate_security_rules.ts | Firebase MCP prompt: firestore generate_security_rules | Firebase (GitHub) | 2026-01-15 (single commit) | primary
D4-S2 | https://arxiv.org/abs/2503.09089 | LocAgent: Graph-Guided LLM Agents for Code Localization | ACL 2025 | 2025-03 | primary
D4-S3 | https://arxiv.org/abs/2103.02669 | An Empirical Analysis of UI-based Flaky Tests (Romano et al.) | ICSE 2021 | 2021-03 | primary
D4-S4 | https://stryker-mutator.io/docs/stryker-js/configuration/ | StrykerJS configuration (commandRunner) | Stryker Mutator | accessed 2026-10-21 | primary

## Evidence

D4-E1 | D4-S1 | "**Scan the entire codebase** to identify: - Programming language(s) used (for understanding context only) - All Firestore collection and document paths" | Phase-1: Codebase Analysis
D4-E2 | D4-S1 | "Generate a comprehensive **JavaScript / TypeScript** test suite using '@firebase/rules-unit-testing'." | Phase-5: Test Suite Generation
D4-E3 | D4-S1 | "If tests fail due to **rule issues**: **STOP** - report the issue to user" | test execution step
D4-E4 | D4-S1 | "Once devil's advocate testing passes: 1. Use the Firebase MCP 'firebase_validate_security_rules' tool to check syntax" | Phase-4
D4-E5 | D4-S2 | "w/o TraverseGraph 86.13 78.47 66.06" | ablation table (function-level column drops vs full model)
D4-E6 | D4-S3 | "similar root causes together into 4 main categories: Async Wait, ... Environment" | Section on root causes
D4-E7 | D4-S3 | "(W 52.0 % vs M 32.5%)" | Async Wait share, web vs mobile
D4-E8 | D4-S3 | "Total 152 83 235" | dataset table: web 152, mobile 83, total 235 flaky UI tests
D4-E10 | D4-S3 | "developers should pay more attention to the environment configuration" | Finding 3 (platform issues W 10.5% vs M 21.7%)
D4-E9 | D4-S4 | "The command test runner can be made to work in any use case, but comes with a performance penalty, as Stryker cannot do any optimizations and just runs all tests for all mutants." | commandRunner section

## Claims

D4-C1 | Firebase's own MCP server ships a prompt that scans a codebase for Firestore paths, generates rules plus a `@firebase/rules-unit-testing` suite, runs it on the emulator, and stops to report on rule failures instead of editing rules. This is direct prior art for LLM-generated rules tests from code. | support: D4-E1, D4-E2, D4-E3, D4-E4 | independent_sources: 1 | confidence: high
D4-C2 | In LocAgent, removing graph traversal lowered function-level localization accuracy (ablation), so structure gave a measurable comprehension-adjacent gain in that setting. | support: D4-E5 | independent_sources: 1 | confidence: medium
D4-C3 | Async Wait accounted for 32.5% of the 83 flaky mobile UI tests in Romano et al. (whether it is the largest mobile category was not verified in the text). | support: D4-E6, D4-E7, D4-E8 | independent_sources: 1 | confidence: medium
D4-C4 | StrykerJS's generic command test runner can drive any test command (e.g. a device E2E runner) by exit code, but runs the full suite for every mutant, so exhaustive mutation of a device E2E suite is impractical. | support: D4-E9 | independent_sources: 1 | confidence: high

## Conflicts & gaps

- The Hypothesis Attacker reported LocAgent 77.37 vs 70.07 vs 64.60 and "LocBench 59.29 vs 59.11". In the PDF text, 59.11 and 59.29 sit in the same OpenHands row (two columns), so the cross-system comparison as stated is unreliable. Only the ablation direction is used.
- Romano's other category percentages (22.9 / 20.5 / 24.1) were not located by the main session's string search. The Round-2 verifier located them in Table IV of the cached text (mobile counts 27/19/17/20 for Async Wait, Environment, Test Runner API and Script Logic). The paper's Finding 3 (main-session verified) says Android platform issues are more frequent on mobile (W 10.5% vs M 21.7%) and that "developers should pay more attention to the environment configuration". Romano's "environment" means device and OS fragmentation, not a Firebase harness.
- TESSARA, "Building to the Test", Chiral and ReproBreak (persona-reported) were not re-fetched by the main session and are not cited.
