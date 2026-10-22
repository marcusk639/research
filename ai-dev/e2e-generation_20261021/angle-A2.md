# Angle A2 — Empirical evidence on LLM-driven test generation and LLM GUI/mobile testing agents

Retrieval: built-in WebSearch + WebFetch only, 2026-10-21. Every source below was fetched (arXiv abs/html pages or conference pages). Quotes come from fetched abstracts or HTML full text. Some fetches returned paraphrase-wrapped excerpts from the fetch model, so quotes should be spot-checked against the PDF before final publication (see Conflicts & gaps).

## Sources

A2-S1 | https://arxiv.org/abs/2402.09171 (+ /html/2402.09171) | Automated Unit Test Improvement using Large Language Models at Meta (TestGen-LLM) | FSE 2024 Industry (Meta) | 2024-02-14 | primary
A2-S2 | https://arxiv.org/abs/2501.12862 | Mutation-Guided LLM-based Test Generation at Meta (ACH) | FSE 2025 Industry (Meta) | 2025-01-22 | primary
A2-S3 | https://arxiv.org/abs/2310.15780 | Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions (GPTDroid) | ICSE 2024 | 2023-10-24 | primary
A2-S4 | https://arxiv.org/abs/2311.08649 | Autonomous Large Language Model Agents Enabling Intent-Driven Mobile GUI Testing (DroidAgent) | arXiv (cs.SE) | 2023-11-15 | primary (preprint)
A2-S5 | https://arxiv.org/abs/2308.15272 | AutoDroid: LLM-powered Task Automation in Android | MobiCom 2024 | 2023-08-29 (rev. 2024-03-09) | primary
A2-S6 | https://arxiv.org/abs/2312.13771 | AppAgent: Multimodal Agents as Smartphone Users | CHI 2025 | 2023-12-21 | primary
A2-S7 | https://2024.issta.org/details/issta-2024-papers/77/Guardian-A-Runtime-Framework-for-LLM-based-UI-Exploration | Guardian: A Runtime Framework for LLM-based UI Exploration | ISSTA 2024 (conference page abstract) | 2024 | primary
A2-S8 | https://arxiv.org/abs/2407.03037 | Seeing is Believing: Vision-driven Non-crash Functional Bug Detection for Mobile Apps (formerly VisionDroid; now "Trident") | arXiv; ICSE 2026 journal-first per search listing | 2024-07-03 (rev. 2024-12-04) | primary
A2-S9 | https://arxiv.org/abs/2307.07221 | Software Testing with Large Language Models: Survey, Landscape, and Vision | IEEE TSE | rev. 2024-03-04 | primary (survey)
A2-S10 | https://arxiv.org/abs/2410.00752 | TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark | arXiv (Meta AI authors) | 2024-10-01 (rev. 2025-03-18) | primary
A2-S11 | https://arxiv.org/abs/2406.12952 | SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents | arXiv (ETH Zurich) | 2024-06-18 (rev. 2025-02-07) | primary
A2-S12 | https://arxiv.org/abs/2410.21136 (+ /html) | Can we find bugs using LLM-generated oracles? (Konstantinou, Degiovanni, Papadakis) | arXiv | 2024-10-28 (rev. 2026-10-05) | primary (preprint)
A2-S13 | https://arxiv.org/abs/2607.22883 | Evaluating and Mitigating the Misguidance Effect of Buggy Code in LLM-Generated Unit Tests | ISSTA 2026 (PACMSE) | 2026-07-24 | primary
A2-S14 | https://arxiv.org/abs/2601.08998 | On the Flakiness of LLM-Generated Tests for Industrial and Open-Source Database Management Systems | ICSE SEIP 2026 | 2026-01-13 | primary
A2-S15 | https://arxiv.org/abs/2504.01495 (+ /html) | Are Autonomous Web Agents Good Testers? | ISSTA 2025 | 2025-04-02 | primary
A2-S16 | https://arxiv.org/abs/2408.01894 | Feature-Driven End-To-End Test Generation (AutoE2E / E2EBench) | ICSE 2025 (per researchr listing) | 2024-08-04 (rev. 2025-01-06) | primary
A2-S17 | https://arxiv.org/abs/2505.10593 | LLM-Explorer: Towards Efficient and Affordable LLM-based Exploration for Mobile Apps | MobiCom 2025 | 2025-05-15 | primary
A2-S18 | https://conf.researchr.org/details/fse-2025/fse-2025-research-papers/99/LLMDroid-Enhancing-Automated-Mobile-App-GUI-Testing-Coverage-with-Large-Language-Mod | LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance | FSE 2025 (conference page abstract) | 2025 | primary
A2-S19 | https://arxiv.org/abs/2601.21253 | CovAgent: Overcoming the 30% Curse of Mobile Application Coverage with Agentic AI and Dynamic Instrumentation | arXiv | 2026-01-29 | primary (preprint)
A2-S20 | https://arxiv.org/abs/2602.19294 | Towards Automated Page Object Generation for Web Testing using Large Language Models | ICST 2026 | 2026-02-22 | primary
A2-S21 | https://arxiv.org/abs/2504.07244 | Acceptance Test Generation with Large Language Models: An Industrial Case Study | AST 2025 | 2025-04-09 | primary
A2-S22 | https://arxiv.org/abs/2510.18861 | Streamlining Acceptance Test Generation for Mobile Applications Through Large Language Models: An Industrial Case Study (AToMIC, BMW) | ASE 2025 (industry) | 2025-10-21 | primary
A2-S23 | https://arxiv.org/abs/2504.15917 | Towards Test Generation from Task Description for Mobile Testing with Multi-modal Reasoning (VisiDroid) | arXiv, **withdrawn by authors 2025-09-11** | 2025-04-22 | unreliable (withdrawn; listed only for completeness, not used for claims)
A2-S24 | https://arxiv.org/abs/2406.18181 | On the Evaluation of Large Language Models in Unit Test Generation | ASE 2024 | 2024-06-26 | primary (abstract only; no numbers extracted)

Unreachable / not cited: https://people.ece.ubc.ca/mjulia/publications/Mobile_Application_Coverage_ICSE2025.pdf ("Mobile Application Coverage: The 30% Curse and Ways Forward", ICSE 2025) — fetch timed out. Its claim is cited here only second-hand through A2-S19. The arXiv abs for LLMDroid (tried 2506.05079) turned out to be a different paper (ScenGen, TOSEM), so LLMDroid is cited from the FSE page (A2-S18).

## Evidence

A2-E1 | A2-S1 | "75% of TestGen-LLM's test cases built correctly, 57% passed reliably, and 25% increased coverage" | Abstract (Instagram Reels & Stories evaluation)
A2-E2 | A2-S1 | "improved 11.5% of all classes" … "73% of its recommendations being accepted for production deployment" | Abstract (test-a-thons)
A2-E3 | A2-S1 | "TestGen-LLM discards any test case that does not pass on first execution." | HTML, filter pipeline section
A2-E4 | A2-S1 | "A test that does not pass on every one of five executions is deemed flaky." | HTML, filter pipeline section
A2-E5 | A2-S1 | "Any test that does not improve coverage is also discarded." | HTML, filter pipeline section
A2-E6 | A2-S1 | "Without an automatable test oracle, TestGen-LLM cannot automatically determine whether a failing test has found a bug, or whether it merely contains an incorrect test assertion." | HTML, filter discussion
A2-E7 | A2-S1 | "The effect of this filter is to preserve only tests that can be used for regression testing." | HTML, filter discussion
A2-E8 | A2-S1 | "TestGen-LLM guards against LLM hallucination: it submits, for human review, only test cases that it can guarantee improve on the existing code base." | HTML
A2-E9 | A2-S2 | "engineers accepted 73% of its tests, judging 36% to privacy relevant" | Abstract
A2-E10 | A2-S2 | Applied to "10,795 Android Kotlin classes" across 7 platforms, generating "9,095 mutants and 571 privacy-hardening test cases" | Abstract
A2-E11 | A2-S2 | Equivalent-mutant detector: "precision of 0.79 and recall of 0.47", rising to "0.95 and 0.96" with preprocessing | Abstract
A2-E12 | A2-S3 | GPTDroid "outperforms the best baseline by 32% in activity coverage, and detects 31% more bugs at a faster rate" | Abstract (93 Google Play apps)
A2-E13 | A2-S3 | "identify 53 new bugs on Google Play, of which 35 have been confirmed and fixed" | Abstract
A2-E14 | A2-S4 | DroidAgent "achieved 61% activity coverage, compared to 51% for current state-of-the-art GUI testing techniques" | Abstract (15 Themis apps)
A2-E15 | A2-S4 | "317 out of the 374 autonomously created tasks are realistic and relevant to app functionalities" | Abstract
A2-E16 | A2-S5 | AutoDroid task completion "71.3%", action accuracy "90.9%"; benchmark "with 158 common tasks" | Abstract
A2-E17 | A2-S5 | Combines LLM commonsense with "domain-specific knowledge of apps through automated dynamic analysis" | Abstract
A2-E18 | A2-S6 | "The agent learns to navigate and use new apps either through autonomous exploration or by observing human demonstrations." | Abstract; evaluated on "over 50 tasks in 10 different applications"
A2-E19 | A2-S7 | "LLMs struggle with following specific instructions for UI testing and replanning based on new information" | Abstract
A2-E20 | A2-S7 | Guardian on FestiVal (58 tasks, 23 apps): "48.3% success rate" (154% improvement) and "64.0% average completion proportion" | Abstract (conference page)
A2-E21 | A2-S8 | Existing GUI testing identifies mainly crashes with "obvious abnormal signals"; approach reports "14%-112% and 108%-147% boost in average recall and precision compared with the best baseline" | Abstract (590 non-crash bugs, 12 baselines)
A2-E22 | A2-S9 | Survey analyzes "102 relevant studies that have used LLMs for software testing" | Abstract
A2-E23 | A2-S10 | "models struggle to generate high-coverage test suites, with the best model, GPT-4o, achieving an average coverage of only 35.2%" | Abstract (1,210 code/test file pairs, 11 Python repos)
A2-E24 | A2-S10 | limitations stem from "models struggling to reason about execution, and their frequent assertion errors when addressing complex code paths" | Abstract
A2-E25 | A2-S11 | "Code Agents designed for code repair exceeding the performance of systems designed specifically for test generation" | Abstract
A2-E26 | A2-S11 | "generated tests are an effective filter for proposed code fixes, doubling the precision of SWE-Agent" | Abstract
A2-E27 | A2-S12 | "LLM-based test generation approaches mainly capture the actual program behavior making bug detection difficult" | Abstract
A2-E28 | A2-S12 | "LLMs' test oracle classification accuracy considerably drops in the presence of buggy code, suggesting that its predictions are derived towards the actual implementation rather than the desired one." | Section 4.1
A2-E29 | A2-S12 | Anonymising names: models "dropped up to 15.30%, 15.40%, 10.20% and 6.60% respectively" | Section 4.2 (RQ2)
A2-E30 | A2-S13 | buggy code "significantly increases 'misguided tests' that assert incorrect behavior while simultaneously suppressing the generation of effective, bug-finding tests" | Abstract
A2-E31 | A2-S13 | specification-based paradigm "effectively reduces misguided tests while substantially increasing effective tests" | Abstract
A2-E32 | A2-S14 | "generated tests have a slightly higher proportion of flaky tests compared to existing tests" | Abstract
A2-E33 | A2-S14 | most common root cause: "reliance of a test on a certain order that is not guaranteed" (72 of 115 flaky tests, 63%) | Abstract
A2-E34 | A2-S14 | "both LLMs transferred the flakiness from the existing tests to the newly generated tests via the provided prompt context" | Abstract
A2-E35 | A2-S15 | "PinATA obtains around 60% of correct verdict and up to a promising 94% specificity" | Abstract
A2-E36 | A2-S15 | "both SeeAct-ATA and PinATA exhibited a tendency to misclassify passing test cases as failing, with specificity not exceeding 57%." | Section 7 Conclusion
A2-E37 | A2-S15 | "Sonnet has a lower specificity (0.47 vs 0.57 for GPT-4o and 0.56 for Gemini)" | Section 5.2
A2-E38 | A2-S16 | "AutoE2E achieves an average feature coverage of 79%, outperforming the best baseline by 558%" | Abstract
A2-E39 | A2-S16 | AutoE2E "infers potential features within a web application and translates them into executable test scenarios" | Abstract
A2-E40 | A2-S17 | "many actions during exploration do not require, or may even be biased by the abilities of LLMs" | Abstract
A2-E41 | A2-S17 | "over 148x lower cost than the state-of-the-art LLM-based approach" | Abstract
A2-E42 | A2-S18 | "an average increase of 26.16% in code coverage and 29.31% in activity coverage" (14 Google Play apps) | Abstract
A2-E43 | A2-S18 | "LLMDroid achieves optimal performance at $4.77 per hour using GPT-4o, with a cost-effective alternative achieving 78% of optimal performance at just $0.18 per hour" | Abstract
A2-E44 | A2-S19 | "Recent studies, including the state-of-the-art, struggle to achieve more than 30% activity coverage in real-world apps." | Abstract
A2-E45 | A2-S19 | agents inspect decompiled code and component graphs; "101.1%" higher activity coverage than LLMDroid, "116.3%" than Fastbot, "179.7%" than APE | Abstract
A2-E46 | A2-S20 | LLM page objects: "accuracy values ranging from 32.6% to 54.0%"; element recognition "exceeding 70% in most cases" | Abstract (5 web apps)
A2-E47 | A2-S21 | Cypress scripts: "92% of the acceptance test cases generated by Test Flow were considered helpful"; Gherkin helpful "95% of the time" | Abstract
A2-E48 | A2-S21 | Cypress breakdown: 60% usable as generated, 8% minor fixes, 24% regenerated with additional inputs, 8% discarded | Abstract (fetch-model summary of abstract; verify)
A2-E49 | A2-S22 | "93.3%" Gherkin syntactically correct, "78.8%" PageObjects executed without manual edits, "100%" of generated UI tests ran successfully | Abstract (MyBMW, 13 issues, 170+ screens)
A2-E50 | A2-S22 | artifacts generated from "Gherkin scenarios, Page Objects, and executable UI test scripts" from JIRA tickets and code changes, Flutter | Abstract

## Claims

A2-C1 | In Meta's industrial deployment, most LLM-generated tests are discarded: only 75% built, 57% passed reliably and 25% increased coverage (measured per test class) | support: A2-E1 | independent_sources: 1 | confidence: high (for Meta/Kotlin unit tests; not for E2E)
A2-C2 | TestGen-LLM's filter chain (build → pass → 5× rerun to reject flaky → must add coverage) is what makes the output acceptable; humans then accepted 73% of surviving recommendations | support: A2-E2, A2-E3, A2-E4, A2-E5, A2-E8 | independent_sources: 1 | confidence: high
A2-C3 | Build/run filtering only yields regression tests: they lock in current behaviour and cannot tell a real bug from a wrong assertion | support: A2-E6, A2-E7 | independent_sources: 1 | confidence: high
A2-C4 | Steering generation with a concern-specific target (mutants of a fault class) gives high acceptance (73%) on Android Kotlin code at Meta scale | support: A2-E9, A2-E10, A2-E11 | independent_sources: 1 | confidence: medium (one vendor, privacy domain)
A2-C5 | LLM oracles tend to encode the code's actual behaviour, bugs included, rather than intended behaviour | support: A2-E27, A2-E28, A2-E30 | independent_sources: 2 | confidence: high
A2-C6 | Giving the model a specification instead of (buggy) code, or meaningful names and docs, reduces bug-encoding tests and improves oracle accuracy | support: A2-E29, A2-E31 | independent_sources: 2 | confidence: medium (unit-level Java/Python; not shown for E2E)
A2-C7 | LLM-generated tests are slightly flakier than human ones, mostly from assumed ordering, and the flakiness of existing tests carries over through the prompt context | support: A2-E32, A2-E33, A2-E34 | independent_sources: 1 | confidence: medium (DBMS domain)
A2-C8 | Even strong models get low coverage on realistic unit-test generation (GPT-4o 35.2% average on TestGenEval), with assertion errors a main cause | support: A2-E23, A2-E24 | independent_sources: 1 | confidence: medium
A2-C9 | General code agents beat purpose-built test generators at reproducing real issues, and generated tests are useful as a filter on fixes | support: A2-E25, A2-E26 | independent_sources: 1 | confidence: medium
A2-C10 | LLM GUI agents report better coverage and bug-finding than pre-LLM Android tools, with gains of roughly 10 points to 32% relative in activity coverage | support: A2-E12, A2-E14, A2-E42 | independent_sources: 3 | confidence: medium (Android-only, small app sets of 14–93, authors' own baselines)
A2-C11 | Activity coverage in real apps stays low for both classic and LLM explorers (about 30%) | support: A2-E44 | independent_sources: 1 (the ICSE 2025 primary was unreachable) | confidence: medium
A2-C12 | Using source or decompiled code alongside the GUI beats exploration-only tools on coverage | support: A2-E45 (code inspection plus instrumentation), A2-E17 (dynamic-analysis memory) | independent_sources: 2 | confidence: low-medium (CovAgent is a preprint; instrumentation is not a black-box E2E test)
A2-C13 | Calling the LLM at every step costs too much and is not needed; hybrid designs keep or raise coverage at much lower cost | support: A2-E40, A2-E41, A2-E43 | independent_sources: 2 | confidence: medium
A2-C14 | Task-directed LLM agents complete only about 48–71% of feature-level tasks, and instruction-following and replanning are documented weaknesses | support: A2-E16, A2-E19, A2-E20 | independent_sources: 2 | confidence: medium
A2-C15 | LLM agents judging natural-language E2E test verdicts get about 60% right and often flag passing tests as failing (specificity ≤57%) | support: A2-E35, A2-E36, A2-E37 | independent_sources: 1 | confidence: medium
A2-C16 | Generating selectors/locators is error-prone: page-object accuracy was only 32.6–54.0% | support: A2-E46 | independent_sources: 1 | confidence: medium
A2-C17 | Spec-first pipelines (requirements/user stories → Gherkin → page objects → scripts) give high usability in industry, but a large share of scripts still need fixes or regeneration | support: A2-E47, A2-E48, A2-E49, A2-E50 | independent_sources: 2 | confidence: medium (both by the same FEUP group, practitioner-rated)
A2-C18 | Feature-inference-first E2E generation gives much higher feature coverage than prior web test generators | support: A2-E38, A2-E39 | independent_sources: 1 | confidence: medium (its own benchmark)
A2-C19 | Crash-only oracles miss most functional bugs; vision/MLLM oracles improve recall and precision on non-crash bugs | support: A2-E21 | independent_sources: 1 | confidence: medium

## Conflicts & gaps

- **Specificity vs sensitivity mislabel (A2-S15).** The abstract says "up to a promising 94% specificity", but Section 5.2 reports Sonnet's 0.94 as sensitivity, with specificity 0.47. The body is consistent with the conclusion ("specificity not exceeding 57%"), so read the abstract figure as sensitivity. Cite the body numbers.
- **Metric units differ.** TestGen-LLM's 75/57/25% are counted per test class ("at least one test case" that builds, passes or adds coverage), not per test (HTML). Without that caveat, readers will overstate the per-test success rate.
- **Baselines are self-selected and not comparable across papers.** GPTDroid, DroidAgent, LLMDroid and Guardian each use their own app sets (93, 15, 14 and 23 apps) and metrics (activity coverage, task success, completion proportion). No independent head-to-head of LLM agents against Monkey, APE, Stoat or Humanoid was fetched. The ICSE 2025 "30% curse" study, which would be the closest neutral comparison, was unreachable.
- **Android-native only.** Every mobile GUI agent here (S3–S8, S17–S19) targets native Android, usually through UIAutomator view hierarchies or decompiled APKs. No fetched study evaluates React Native or iOS. The only cross-platform evidence is AToMIC (Flutter, S22), and it is spec-driven script generation, not exploration. Whether results transfer to RN (accessibility-ID/testID-based trees, JS-driven navigation, Firebase back-end state) is untested.
- **The oracle evidence is unit-level.** A2-S12 and A2-S13 study Java/Python unit tests. That E2E assertions behave the same way (encoding current UI behaviour) is plausible but extrapolated.
- **Contamination.** TestGenEval and SWT-Bench use popular public repos. Their papers' contamination discussion was not extracted here. Industrial studies (S1, S2, S21, S22) avoid contamination but cannot be reproduced.
- **Same-group and practitioner-rated results.** S21 and S22 share authors (Lima, Faria) and rely on practitioner judgments ("helpful"), not mutation or fault-detection measures.
- **Withdrawn paper.** VisiDroid (S23) reported 87.3% accuracy for task-description-to-test generation but was withdrawn. It is excluded from claims.
- **VisionDroid renamed.** arXiv 2407.03037 is now titled "Seeing is Believing…" (approach "Trident"). The earlier "VisionDroid" figure of 29 bugs found / 19 fixed appears only in search snippets of v1 and is not cited.
- **Fetch-model caveat.** Some quotes came through a summarising fetch layer (notably A2-E48's percentage breakdown). Verify against the PDFs before quoting in the final report.
- **Not found / not fetched:** a direct study of hallucinated selectors in generated Playwright or Detox tests, and a controlled comparison of code-reading against exploration-only generation of E2E scripts (as opposed to coverage-driven exploration).

## Analyst assessment

The strongest and most transferable finding is from Meta (S1, S2): **raw LLM test output is mostly unusable, and a mechanical execute-and-filter loop makes it shippable.** Per test class, a quarter or fewer of candidates both pass reliably and add value, and the filters (build, pass, five reruns, measurable gain) carry the quality. Meta itself says the price is that survivors are only regression tests: a passing filter certifies "the code does what it does", not "the code does what it should". Two independent unit-level studies (S12, S13) confirm the mechanism. Shown buggy code, LLMs write assertions that encode the bug and write fewer bug-revealing tests. Supplying a specification, or meaningful names and docs, partly reverses this.

For `/generate-e2e` this points to a deliberate two-track design:

1. **Behavioral spec first, drawn mainly from product intent** (docs, tickets, UI copy, route and feature names), with code as a secondary source. Code-derived expectations should be marked as observed behaviour, and spec items that disagree with the code should be raised to a human as possible bugs, not silently turned into assertions. That disagreement queue is the only place the tool can find real bugs. Everything else is a regression net.
2. **A hard execution filter on generated tests**: compile/lint, run on emulator and simulator against Firebase emulators, run N times (Meta used 5) to reject flaky tests, and keep only tests that add a measured behaviour or coverage delta. S14 adds that the generator copies the patterns of existing tests, flakiness included. Curate the few-shot examples, and ban order-dependent assertions on Firestore query results, which is the RN/Firebase analogue of S14's "unordered collection" cause.

On exploration agents: the Android literature (S3, S4, S7, S17, S18) shows real but modest gains over Monkey/APE-class tools. Those gains come from small, author-chosen app sets, and coverage stays near 30% in real apps (S19). Task success for feature-directed agents is about 48–71% (S5, S7), and replanning is a known weakness. Per-step LLM control is also expensive, and hybrid designs cut cost by orders of magnitude (S17, S18). So an exploration agent should be **a discovery and verification aid**, not the test runtime. Use it once per feature to confirm reachable flows and capture real selectors, then emit deterministic scripts (Detox/Maestro for RN, Playwright for Angular). LLM-as-runtime-verdict is unreliable: about 60% of verdicts were correct and false alarms were frequent (S15).

Selector generation is a documented weak point (S20: 32.6–54% page-object accuracy). The tool should prefer, and if needed add, stable `testID`s found in source rather than inferring locators from rendered trees, and should reject any locator not seen in a live run.

Evidence that reading source code helps is suggestive (S19 code inspection, S5 app-specific memory, S22 code changes plus tickets) but not controlled. Spec-first industrial pipelines (S21, S22) report high practitioner usefulness. Even there, about a third of scripts in S21 needed regeneration or were discarded, which again argues for the execution filter.

Transfer caveat: almost none of this evidence is React Native, iOS or multi-surface (mobile + Cloud Functions + Angular). Treat every number as an Android or unit-level prior, and plan to measure the tool's own build-pass-stable-useful funnel per feature.
