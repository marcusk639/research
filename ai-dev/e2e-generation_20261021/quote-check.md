# Quote-fidelity check

Each quote was matched against a raw curl (or pdftotext) fetch of its source,
independent of WebFetch. Score = share of the quote's word n-grams found in the page.

| status | count |
| --- | --- |
| verbatim | 305 |
| near-verbatim | 89 |
| partial | 38 |
| paraphrase-only | 21 |
| verbatim-manual | 14 |
| unverifiable (page not machine-readable) | 3 |
| not-found | 2 |
| verbatim-other-url | 1 |

## Not found or partial

| E | src | angle id | score | quote |
| - | - | - | - | - |
| E7 | S3 | A1-E7 | 0.73 | "If any link in that chain stalls...the whole stack enters an undefined state." |
| E10 | S4 | A1-E10 | None | Maintainer workaround `export MAESTRO_DRIVER_STARTUP_TIMEOUT=60000`; reporter said it did not fix the issue; i |
| E11 | S5 | A1-E11 | 0.73 | "When executing `inputText` to type `Lorem ipsum`, sometimes it'll actually type `Loemipsu`. The skipped chara |
| E32 | S17 | A1-E32 | None | Sync is blocked by endless animations, long timers, network polling; last-resort `device.disableSynchronizatio |
| E36 | S19 | A1-E36 | None | Tools include `appium_get_page_source`, `generate_locators`, `appium_generate_tests`; generated output is Java |
| E60 | S31 | A2-E10 | 0.5 | Applied to "10,795 Android Kotlin classes" across 7 platforms, generating "9,095 mutants and 571 privacy-harde |
| E62 | S32 | A2-E12 | 0.73 | GPTDroid "outperforms the best baseline by 32% in activity coverage, and detects 31% more bugs at a faster rat |
| E67 | S34 | A2-E17 | 0.5 | Combines LLM commonsense with "domain-specific knowledge of apps through automated dynamic analysis" |
| E68 | S35 | A2-E18 | 0.47 | "The agent learns to navigate and use new apps either through autonomous exploration or by observing human dem |
| E79 | S41 | A2-E29 | 0.5 | Anonymising names: models "dropped up to 15.30%, 15.40%, 10.20% and 6.60% respectively" |
| E84 | S43 | A2-E34 | 0.62 | "both LLMs transferred the flakiness from the existing tests to the newly generated tests via the provided pro |
| E88 | S45 | A2-E38 | 0.55 | "AutoE2E achieves an average feature coverage of 79%, outperforming the best baseline by 558%" |
| E89 | S45 | A2-E39 | 0.64 | AutoE2E "infers potential features within a web application and translates them into executable test scenarios |
| E95 | S48 | A2-E45 | 0.5 | agents inspect decompiled code and component graphs; "101.1%" higher activity coverage than LLMDroid, "116.3%" |
| E100 | S51 | A2-E50 | 0.5 | artifacts generated from "Gherkin scenarios, Page Objects, and executable UI test scripts" from JIRA tickets a |
| E120 | S63 | A3-E20 | 0.6 | "the static modeling of control/data flow due to interactions of the user with the application's GUI" |
| E121 | S64 | A3-E21 | 0.68 | "all declared screens, the user interface elements, their textual and graphical features, as well as Android A |
| E126 | S67 | A3-E26 | 0.5 | "`testPath.test()` executes each step in `testPath.segments` by: 1. Verifying that the SUT is in `segment.stat |
| E130 | S69 | A3-E30 | 0.64 | "SpecGen succeeds in generating verifiable specifications for 279 out of 385 programs, outperforming the exist |
| E136 | S72 | A3-E36 | 0.5 | "Seven specialized agents collaborate to discover user journeys, extract business rules" |
| E138 | S72 | A3-E38 | 0.5 | "Extracted rules independently corroborated against real production defect records" |
| E161 | S80 | A4-E18 | 0.73 | "The Firebase Admin SDKs automatically connect to the Cloud Firestore emulator when the FIRESTORE_EMULATOR_HOS |
| E162 | S80 | A4-E19 | 0.62 | Clear data: "DELETE http://localhost:8080/emulator/v1/projects/{projectID}/databases/(default)/documents" (end |
| E186 | S98 | A4-E43 | 0.6 | "stripe listen --forward-to localhost:4242/webhook" ; "The stripe listen command outputs the {{WEBHOOK_SIGNING |
| E189 | S98 | A4-E46 | 0.67 | "Stripe doesn't guarantee the delivery of events in the order that they're generated." |
| E215 | S111 | A5-E10 | None | [paraphrase] When a screen has no Android UI hierarchy (games, OpenGL), Robo falls back to random tapping. |
| E229 | S116 | A5-E24 | 0.17 | Tests are "YAML files in the user's repository" |
| E244 | S123 | A5-E39 | None | [paraphrase] aiBoolean, aiQuery and aiAssert results are never cached. Element-location caching is web only. E |
| E266 | S134 | A5-E61 | 0.67 | [paraphrase] Octomind took only a URL, discovered flows, and generated Playwright code that the user owned. Co |
| E271 | S137 | A5-E66 | None | [paraphrase] Each screenshot costs about 1,000-1,800 input tokens, so long loops add up fast. The reference en |
| E272 | S137 | A5-E67 | None | [paraphrase] Recommends a dedicated VM or container, keeping credentials away from the model, and human confir |
| E273 | S51 | A5-E68 | 0.6 | Generates "Gherkin scenarios, Page Objects, and executable UI test scripts directly from requirements (JIRA ti |
| E285 | S139 | A6-E10 | 0.7 | Orchestrator-workers: "well-suited for complex tasks where you can't predict the subtasks needed" |
| E302 | S142 | A6-E27 | None | Frontmatter fields listed: `name`, `description`, `disable-model-invocation`, `allowed-tools`, `user-invocable |
| E303 | S142 | A6-E28 | 0.62 | With`context: fork`: "The subagent doesn't see your conversation history, so the skill's instructions have to  |
| E306 | S59 | A6-E31 | None | Optional fields include `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServe |
| E329 | S31 | A6-E54 | None | 9,095 mutants over 10,795 Android Kotlin classes; 571 tests; engineers accepted 73%; equivalent-mutant detecto |
| E330 | S152 | A6-E55 | 0.64 | MutGen "incorporates mutation feedback directly into the prompt" and "significantly outperforms both EvoSuite  |
| E333 | S154 | A6-E58 | 0.67 | "a taxonomy of 262 types of Android faults grouped in 14 categories"; "a set of 38 mutation operators" (35 aut |
| E351 | S163 | D1-E11 | 0.43 | "This was just 'vibes' – internal vibes... It just felt better." |
| E359 | S165 | D1-E19 | None | [paraphrase] $400k+/yr saved; regression cycle cut from 2+ weeks to 1 week; 300 automated tests; the QA team w |
| E360 | S166 | D1-E20 | None | [paraphrase] Test execution time went from 7 hours to 30 minutes and 500+ manual test cases were replaced. Quo |
| E364 | S168 | D1-E24 | 0.65 | "AI-generated tests contribute to code coverage comparable to human-written tests, frequently achieving positi |
| E378 | S33 | D1-E38 | 0.62 | "On average, DroidAgent achieved 61% activity coverage, compared to 51% for current state-of-the-art GUI testi |
| E383 | S45 | D1-E43 | 0.55 | "AutoE2E achieves an average feature coverage of 79%, outperforming the best baseline by 558%" |
| E394 | S112 | D2-E11 | None | `npx playwright init-agents --loop=[option]`. Loops: Claude Code, VS Code, Codex, OpenCode. Seed file `tests/s |
| E408 | S46 | D2-E25 | 0.62 | LLM-Explorer "uses LLMs primarily for maintaining the knowledge instead of generating actions"; "over 148x low |
| E411 | S188 | D2-E28 | 0.67 | "when a web service implementation fails to thoroughly replicate input validation, it gives rise to inconsiste |
| E413 | S189 | D2-E30 | 0.47 | "finds 1.4 times to 4.5 times more unique defects than the respectively second-best fuzzer for each target" |
| E415 | S187 | D2-E32 | 0.61 | "DIFFDROID combines input generation and differential testing to compare the behavior of an app on different p |
| E419 | S182 | D2-E36 | 0.57 | The docs say Meticulous "Doesn't test... Cross-browser compatibility (tests run in Chrome)". Recording works " |
| E423 | S37 | D2-E40 | None | Trident reports precision gains of 108%–147% and recall gains of 14%–112% over the best baseline, on 590 non-c |
| E428 | S45 | D2-E45 | 0.6 | AutoE2E "achieves an average feature coverage of 79%, outperforming the best baseline by 558%" |
| E429 | S195 | D2-E46 | None | PropGen produced 985 properties, 912 of them valid, and found 25 previously unknown functional bugs. |
| E441 | S197 | D3-E11 | None | "RN0.84" |
| E444 | S17 | D3-E14 | None | `await device.setURLBlacklist(['.*127.0.0.1.*']);` … `await device.disableSynchronization();` [paraphrase: dis |
| E448 | S204 | D3-E18 | None | [paraphrase] natural-language steps (e.g. 'Click the login button') are converted to actions executed at runti |
| E451 | S4 | D3-E21 | None | [paraphrase] closed 2026-03-09 for insufficient reproduction info / inactivity, not fixed |
| E452 | S206 | D3-E22 | 0.0 | "When `ViewHierarchyHandler.fullStatusBars()` encounters a transient accessibility error (`kAXErrorInvalidUIEl |
| E457 | S208 | D3-E27 | None | [paraphrase] workaround: restart `maestro mcp` before using an erased/rebooted simulator, or one MCP process p |
| E463 | S209 | D3-E33 | None | [paraphrase] open iOS-driver issues as of 2026-10-21 include #3538, #3611, #3686 (cancelled taps reported as s |

## Unverifiable (page not machine-readable)

- S29 https://conf.researchr.org/details/saner-2026/saner-2026-workshops-tutorials-track/44
- S193 https://lucadigrazia.com/papers/ase2025.pdf
