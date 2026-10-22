# Angle A5: Commercial and novel AI testing products, autonomous exploration, self-healing

Worker: A5 | Run date: 2026-10-21 | Tools: built-in WebSearch + WebFetch only.

Method note: WebFetch hands page content to a small summarizer model, and the quotes below are the strings it marked as verbatim. Anything marked "[paraphrase]" was a summary, not a quote. Spot-check quotes against the live page before they go into the final report (see Conflicts & gaps).

## Sources

```
A5-S1 | https://firebase.google.com/docs/app-distribution/android/app-testing-agent | App Testing agent (Android) | Google / Firebase docs | accessed 2026-10-21 | primary
A5-S2 | https://firebase.google.com/docs/test-lab/android/robo-ux-test | Run a Robo test (Android) | Google / Firebase docs | accessed 2026-10-21 | primary
A5-S3 | https://playwright.dev/docs/test-agents | Playwright Test Agents | Microsoft / Playwright docs | accessed 2026-10-21 | primary
A5-S4 | https://playwright.dev/docs/release-notes | Release notes (v1.56, v1.62, v1.64) | Microsoft / Playwright docs | accessed 2026-10-21 | primary
A5-S5 | https://docs.maestro.dev/api-reference/commands/assertwithai | assertWithAI | mobile.dev / Maestro docs | accessed 2026-10-21 | primary
A5-S6 | https://docs.maestro.dev/get-started/maestro-mcp | Maestro MCP Server | mobile.dev / Maestro docs | accessed 2026-10-21 | primary
A5-S7 | https://maestro.dev/blog/mobile-ui-testing-with-coding-agents | Mobile UI Testing with Claude Code, Cursor and Codex | Maestro blog (A. Kharche) | 2026-09-01 | secondary (vendor)
A5-S8 | https://momentic.ai/docs/get-started/how-momentic-works | How Momentic works | Momentic docs | accessed 2026-10-21 | primary (feature description)
A5-S9 | https://momentic.ai/docs/comparisons/maestro | Momentic vs Maestro | Momentic docs | accessed 2026-10-21 | secondary (vendor comparison)
A5-S10 | https://www.meticulous.ai/ | Meticulous homepage | Meticulous | accessed 2026-10-21 | secondary (vendor marketing)
A5-S11 | https://app.meticulous.ai/docs/concepts/network-recording-and-patching | Network Recording & Patching | Meticulous docs | accessed 2026-10-21 | primary
A5-S12 | https://app.meticulous.ai/changelog/2026-07-06 | Agent Skills, custom checks, and backend record & replay | Meticulous changelog | 2026-07-06 | primary
A5-S13 | https://github.com/takahirom/arbigent | Arbigent README | GitHub (takahirom) | accessed 2026-10-21 | primary
A5-S14 | https://midscenejs.com/ | Midscene.js homepage | Midscene (open source) | accessed 2026-10-21 | primary
A5-S15 | https://midscenejs.com/caching.html | Midscene caching | Midscene docs | accessed 2026-10-21 | primary
A5-S16 | https://docs.stagehand.dev/v3/best-practices/caching | Stagehand caching | Browserbase / Stagehand docs | accessed 2026-10-21 | primary
A5-S17 | https://docs.revyl.com/ | Revyl docs home | Revyl | accessed 2026-10-21 | primary (thin)
A5-S18 | https://testrigor.com/features | testRigor Features | testRigor | accessed 2026-10-21 | secondary (vendor marketing)
A5-S19 | https://applitools.com/blog/ai-driven-testing-with-applitools-autonomous/ | AI-Driven Testing with Applitools Autonomous | Applitools blog (K. Pathak, Applitools Ambassador) | 2026-08-28 | secondary (vendor-affiliated)
A5-S20 | https://www.qawolf.com/automation-ai | Automation AI | QA Wolf | accessed 2026-10-21 | secondary (vendor marketing)
A5-S21 | https://www.qawolf.com/blog/self-healing-test-automation-types | The 6 Types of AI Self-Healing in Test Automation | QA Wolf blog (J. Gluck) | 2026-01-28 | blog (vendor)
A5-S22 | https://www.ministryoftesting.com/software-testing-glossary/self-greening | Self Greening | Ministry of Testing (R. Parwal) | 2025-11-13 | blog (community)
A5-S23 | https://bug0.com/blog/self-healing-tests-real-vs-fake-2026 | Self-healing tests are table stakes, and most of them aren't real | Bug0 blog (S. F. Rahman) | 2026-07-09 | blog (vendor)
A5-S24 | https://rywalker.com/research/ai-qa-agents | AI QA agents research | Ry Walker (CEO of Tembo, disclosed) | undated, after mid-2026 | blog (independent-ish analyst)
A5-S25 | https://news.ycombinator.com/item?id=41924787 | Launch HN: GPT Driver (YC S21) | Hacker News | 2024-10-23 | blog (HN discussion)
A5-S26 | https://news.ycombinator.com/item?id=37645376 | Show HN: Automated, hosted UI tests with AI test discovery (octomind.dev) | Hacker News | 2023-09-25 | blog (HN discussion)
A5-S27 | https://news.ycombinator.com/item?id=35629050 | Show HN: Checksum | Hacker News | 2023-04-19 | blog (HN discussion)
A5-S28 | https://blog.google/technology/google-deepmind/gemini-computer-use-model/ | Introducing the Gemini 2.5 Computer Use model | Google blog | 2025-10-07 | secondary (vendor, own product)
A5-S29 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool | Computer use tool | Anthropic docs | accessed 2026-10-21 | primary
A5-S30 | https://arxiv.org/abs/2510.18861 | Streamlining Acceptance Test Generation for Mobile Applications Through LLMs: An Industrial Case Study (AToMIC) | arXiv (Fonseca, Lima, Faria) | 2025-10-21 | academic (preprint)
A5-S31 | https://arxiv.org/html/2504.20896v1 | LELANTE: LEveraging LLM for Automated ANdroid TEsting | arXiv | 2025-04 | academic (preprint)
```

That is 31 fetched sources. One more, the Octomind shutdown letter (octomind.dev/blog/a-letter-to-our-users-customers-and-readers/), failed DNS resolution and is not used as a source. See Conflicts & gaps.

## Evidence

```
A5-E1 | A5-S1 | "The App Testing agent is a test case generation, management, and execution agent powered by Gemini in Firebase." | intro
A5-E2 | A5-S1 | "Give each step a Goal that describes what the App Testing agent should do during that step." | Create test cases
A5-E3 | A5-S1 | "Because the App Testing agent uses generative AI to test your app, it will sometimes take different actions while still following the same instructions." | Known limitations / results
A5-E4 | A5-S1 | "The App Testing agent feature is a preview release. A preview release is not subject to any SLA or deprecation policy." | preview banner
A5-E5 | A5-S1 | "During the preview, the AI-guided tests will be offered at no cost within a quota limit. The default quota limit is 200 tests per month, per Firebase project." | Pricing/quota
A5-E6 | A5-S1 | "AI-guided tests have a timeout of 5 minutes." | Limitations
A5-E7 | A5-S1 | Results distinguish "AI action" from "Replayed action"; replayed actions reuse prior successful runs but the agent "will still use AI to confirm." | Test results
A5-E8 | A5-S2 | "Robo test always simulates the same user activities in the same order when you use it to test an app on a specific device configuration with the same settings." | Overview
A5-E9 | A5-S2 | "Robo test analyzes the structure of your app's user interface (UI) and then explores it methodically, automatically simulating user activities." | Overview
A5-E10 | A5-S2 | [paraphrase] When a screen has no Android UI hierarchy (games, OpenGL), Robo falls back to random tapping. | Limitations
A5-E11 | A5-S3 | Planner "explores your app and produces a test plan for one or many scenarios and user flows" | Planner
A5-E12 | A5-S3 | Generator "uses the Markdown plan to produce executable Playwright Tests. It verifies selectors and assertions live" | Generator
A5-E13 | A5-S3 | Healer "Replays the failing steps, inspects the current UI to locate equivalent elements or flows, suggests a patch" | Healer
A5-E14 | A5-S4 | "Introducing Playwright Test Agents, three custom agent definitions designed to guide LLMs through the core process of building a Playwright test" | v1.56
A5-E15 | A5-S4 | "healer executes the test suite and automatically repairs failing tests" | v1.56
A5-E16 | A5-S5 | assertWithAI "captures a screenshot of the current screen and uploads it to an LLM along with a natural language assertion" | Description
A5-E17 | A5-S5 | "Since assertWithAI is an experimental feature, optional is set to true by default to prevent unstable AI responses from breaking your CI/CD pipelines." | Notes
A5-E18 | A5-S6 | "Use Maestro's MCP server to let your coding agent write, run, and debug mobile and web UI tests." | intro
A5-E19 | A5-S6 | run tool "Accepts exactly one of { yaml } (inline YAML, preferred for exploration), { files } (specific .yaml files), or { dir, include_tags, exclude_tags }." | Tools
A5-E20 | A5-S7 | "Have Claude Code, Cursor or Codex run a UI test on an iOS Simulator or Android emulator, then save it as a Flow and run the same test again." | intro
A5-E21 | A5-S7 | "The agent operates the running app instead of guessing from source. It opens screens, taps controls and reads what is on the device, so the Flow it saves reflects the UI as it actually behaves." | body
A5-E22 | A5-S8 | "step cache reuses successful element resolutions for fast, deterministic replay" | Step lifecycle
A5-E23 | A5-S8 | "Web tests run on Chromium, iOS tests on simulators, and Android tests on emulators. Physical devices are not supported." | Platforms
A5-E24 | A5-S8 | Tests are "YAML files in the user's repository" | Test format
A5-E25 | A5-S9 | Maestro: "Selector-based flow commands; separate experimental AI checks"; Momentic: "Cached target signals with AI re-resolution" | comparison table
A5-E26 | A5-S10 | Mocks backend by "saving and replaying the original recorded responses" for "side-effect free tests with no false positives from changing data." | homepage
A5-E27 | A5-S10 | claims to be "the only testing tool that eliminates flakes" | homepage (marketing)
A5-E28 | A5-S11 | "When a session is recorded, we store the user events and the network request/response pairs from that walkthrough. On each PR we replay the sessions...with no live backend" | How it works
A5-E29 | A5-S11 | [paraphrase] The docs say Meticulous does not test backend correctness: it answers "what will change in the UI", not whether the backend returns correct data. | Limitations
A5-E30 | A5-S11 | "prefer schema-level patching: update the response shape while keeping the original session's primitive values where possible." | Patching
A5-E31 | A5-S12 | Backend Record & Replay captures "Postgres queries and outbound HTTP calls" | 2026-07-06 entry
A5-E32 | A5-S12 | "Claude, migrate all 1000 class components to hooks. Use Meticulous to test this PR locally" | Agent Skills
A5-E33 | A5-S13 | "AI Agent for testing Android, iOS, and Web apps. Get Started in 5 Minutes." | README header
A5-E34 | A5-S13 | "Replay with fallback removes the per-step AI cost for a scenario that already passed: it replays the actions recorded on the last successful run." | Cache strategy
A5-E35 | A5-S13 | "Execute existing Maestro YAML test flows as initialization methods within Arbigent scenarios." | Maestro integration
A5-E36 | A5-S14 | "provides a vision-based GUI Agent and a natural-language E2E testing framework for web, mobile, and desktop apps." | homepage
A5-E37 | A5-S14 | "58 of 60 tasks at a total model API cost of $0.59." | homepage benchmark (vendor-run)
A5-E38 | A5-S15 | "For planning operations (such as ai, aiAct), Midscene uses the prompt instruction as the cache key to store the execution plan returned by AI" | What is cached
A5-E39 | A5-S15 | [paraphrase] aiBoolean, aiQuery and aiAssert results are never cached. Element-location caching is web only. Example run went from 51 s to 28 s with cache hits. | Caching
A5-E40 | A5-S16 | "If the page content or structure changes, the action won't get a cache HIT and the LLM will be called." | Caching
A5-E41 | A5-S16 | Cache hit: "the response is returned directly from the server with no LLM inference and no token cost." | Browserbase Cache
A5-E42 | A5-S17 | "Revyl gives your agents a runtime to run and verify software in, and keeps what it observes in Atlas for your team and your agents to query." | docs home
A5-E43 | A5-S18 | "generate tests based on your own documented test cases using Generative AI for Testing" | features
A5-E44 | A5-S18 | "50 times faster than with Selenium" | features (marketing claim, no method)
A5-E45 | A5-S19 | [paraphrase] Autonomous scans the sitemap to "automatically generate comprehensive test cases for every URL" and stresses "Deterministic control", with no LLMs at runtime. | body
A5-E46 | A5-S20 | "deterministic Appium and Playwright code behind the scenes so tests execute reliably and consistently every time." | Automation AI
A5-E47 | A5-S20 | "charges per test on the platform, with no cost for extra runs" | Pricing
A5-E48 | A5-S21 | "Selector healing creates false passes that hide real defects" | Risk section
A5-E49 | A5-S21 | "Correlating DOM diffs, network responses, console errors, and fixture state" | Diagnosis-first approach
A5-E50 | A5-S22 | "Self greening is a term used to describe a situation where AI automatically "fixes" or adjusts tests so that they pass, potentially hiding genuine problems that should have caused them to fail." | Definition
A5-E51 | A5-S23 | "A tool that repairs a locator by picking the most similar element can pick the wrong one and keep the suite green." | body
A5-E52 | A5-S23 | "A healed step still has to produce a result two models agree actually happened." | requirements
A5-E53 | A5-S24 | QA Wolf: "~$40-44/test/mo, ~$90K median ACV" | QA Wolf entry
A5-E54 | A5-S24 | Momentic: "plain-English tests interpreted at runtime by agents, no generated code to maintain" | Momentic entry
A5-E55 | A5-S24 | Octomind: "Shut down mid-2026"; "we didn't find the market validation we needed"; "deterministic Playwright output, no lock-in, portable tests" | Octomind entry
A5-E56 | A5-S24 | Momentic lock-in: "your tests live in their platform" | Momentic entry
A5-E57 | A5-S25 | GPT Driver founders: "We have to shorten instructions, action history, and screen content during runtime for better results, as handling large amounts of input tokens remains a challenge." | founder post
A5-E58 | A5-S25 | msoad: "The pain has never been in writing the tests...The biggest pain in e2e testing is that tests fail for reasons that are hard to understand and debug." | comment
A5-E59 | A5-S25 | chairhairair: "I do not want additional uncertainty deep in the development cycle" | comment
A5-E60 | A5-S25 | batikha: "being non-deterministic is actually an advantage, in practice." | comment (dissent)
A5-E61 | A5-S26 | [paraphrase] Octomind took only a URL, discovered flows, and generated Playwright code that the user owned. Commenter mirman: "what sorta moat do you have now that openai's got eyes?" | post + comment
A5-E62 | A5-S27 | Checksum: "we learn to generate assertions, run the tests and convert the model actions into proper Playwright or Cypress tests" | founder comment
A5-E63 | A5-S27 | [paraphrase] Commenter satisfice asked whether the system can "recognize a bug when it sees it" (the test-oracle problem) and noted that real-session learning needs real users, but "we test the product before it is released to any users." | comment
A5-E64 | A5-S28 | "primarily optimized for web browsers, but also demonstrates strong promise for mobile UI control tasks. It is not yet optimized for desktop OS-level control." | body
A5-E65 | A5-S28 | Deployed "for use cases including UI testing", alongside Project Mariner and Firebase Testing Agent | body
A5-E66 | A5-S29 | [paraphrase] Each screenshot costs about 1,000-1,800 input tokens, so long loops add up fast. The reference environment is a Linux desktop (Xvfb); mobile is not mentioned. | Limitations
A5-E67 | A5-S29 | [paraphrase] Recommends a dedicated VM or container, keeping credentials away from the model, and human confirmation for consequential actions. | Security
A5-E68 | A5-S30 | Generates "Gherkin scenarios, Page Objects, and executable UI test scripts directly from requirements (JIRA tickets) and recent code changes." | abstract
A5-E69 | A5-S30 | [paraphrase] On BMW's Flutter app (170+ screens, 13 issues): 93.3% of Gherkin was syntactically correct, 78.8% of PageObjects ran without edits, 100% of generated UI tests executed. | abstract
A5-E70 | A5-S31 | [paraphrase] LELANTE reached a 73% execution success rate on 390 natural-language test cases across 10 Android apps, at 11.8 s per step with GPT-4o. Success fell as cases got longer. "Ambiguous test descriptions reduced execution reliability." | abstract/results
```

## Claims

```
A5-C1 | Firebase's App Testing agent (Gemini) takes natural-language test cases (step goals, hints, a final-screen assertion) and executes them with AI on each run. It does not export reusable test code; cached "replayed actions" are still AI-confirmed. | support: A5-E1, A5-E2, A5-E7 | independent_sources: 1 (A5-S28 corroborates that the product exists) | high
A5-C2 | The App Testing agent is Android-only, preview, with no SLA, a 200-tests/month/project free quota and a 5-minute per-test timeout. | support: A5-E4, A5-E5, A5-E6 | independent_sources: 1 | high (as of access date; iOS absence is from docs only)
A5-C3 | Google's own docs say the App Testing agent is non-deterministic ("will sometimes take different actions"). | support: A5-E3 | independent_sources: 1 | high
A5-C4 | Robo test (Test Lab) explores without a script and is deterministic for a fixed device/config. It does not assert business logic, and it degrades to random taps on non-native UI. | support: A5-E8, A5-E9, A5-E10 | independent_sources: 1 | medium-high (business-logic point is the summarizer's inference)
A5-C5 | Playwright v1.56 shipped "Test Agents": a planner (explores the app, writes a Markdown plan), a generator (plan to Playwright test files, verifying selectors live) and a healer (repairs failing tests). The output is durable test code in the repo, and `npx playwright init-agents` sets them up for Claude Code, VS Code and opencode. | support: A5-E11–E15 | independent_sources: 2 (docs + release notes, same publisher) | high
A5-C6 | Playwright agents are web-only. They are the closest published template for a planner, generator and healer pipeline, but they do not cover React Native native apps. | support: A5-E11–E14 (web scope implicit) | independent_sources: 1 | medium (inference: mobile is not mentioned)
A5-C7 | Maestro's AI assertion (`assertWithAI`) is experimental. It sends a screenshot plus an NL assertion to an LLM and defaults to `optional: true` because responses are unstable. | support: A5-E16, A5-E17, A5-E25 | independent_sources: 2 (Maestro docs + Momentic comparison) | high
A5-C8 | Maestro MCP lets coding agents (incl. Claude Code) inspect the screen, run inline YAML and save durable Flow files. Maestro's recommended pattern is to explore the running app and then persist the Flow. | support: A5-E18–E21 | independent_sources: 1 (vendor docs + vendor blog) | high (that it exists); medium (that it works well)
A5-C9 | Momentic stores NL tests as YAML in the repo, resolves targets with AI, caches resolutions for deterministic replay and re-resolves (auto-heals) on cache miss. It supports iOS simulators and Android emulators, not physical devices. | support: A5-E22–E25, A5-E54 | independent_sources: 2 (docs + Walker) | high
A5-C10 | Meticulous records real sessions (events plus network pairs) through a JS snippet and replays them per PR against stubbed network with no live backend. It is web-only and does not test backend correctness, although a July 2026 changelog adds backend record & replay (Postgres, outbound HTTP). | support: A5-E26, A5-E28–E31 | independent_sources: 1 (vendor) | high for mechanism; low for "eliminates flakes" (A5-E27 is marketing)
A5-C11 | Record and replay from real traffic avoids LLM comprehension entirely, but it cannot test features before users exist and has no oracle beyond visual diffs. | support: A5-E29, A5-E63 | independent_sources: 2 | medium
A5-C12 | Open-source agentic runners (Arbigent, Midscene, Stagehand) all converge on the same cost control: cache the AI's first successful plan or locator, replay it without an LLM, and call the model only on a miss or failure. | support: A5-E34, A5-E38–E41 | independent_sources: 3 | high
A5-C13 | Arbigent supports Android, iOS and web, runs AI every execution unless replay-with-fallback is on, and can call existing Maestro YAML as setup. | support: A5-E33–E35 | independent_sources: 1 | high
A5-C14 | Midscene drives Android (ADB) and iOS (WebDriverAgent) by vision. Its locator cache is web-only, and assertion and query results are never cached, so mobile runs keep paying inference for checks. | support: A5-E36, A5-E39 | independent_sources: 1 | medium-high
A5-C15 | QA Wolf generates deterministic Playwright (web) and Appium (mobile) code maintained by AI plus human engineers, sold per test (third-party estimate ~$40–44/test/month, ~$90K median ACV). | support: A5-E46, A5-E47, A5-E53 | independent_sources: 2 | medium (pricing is a third-party estimate)
A5-C16 | Octomind, which produced portable Playwright code from URL-only discovery, shut down in mid-2026 citing lack of market validation. | support: A5-E55, A5-E61 | independent_sources: 1 fetched (a search snippet of Octomind's own letter agrees, but the page was not fetched) | medium
A5-C17 | "Self-healing" can produce false greens. QA Wolf, Bug0 and Ministry of Testing each warn that selector healing can pick the wrong element or mask a real regression; the term "self greening" names it. | support: A5-E48, A5-E50, A5-E51 | independent_sources: 3 (two are vendors with competing products) | high
A5-C18 | Proposed mitigations: diagnose root cause before healing (DOM, network, console, fixtures), and require an independent assertion check (e.g., two-model agreement or human review) before accepting a heal. | support: A5-E49, A5-E52 | independent_sources: 2 (both vendors) | medium
A5-C19 | Practitioner skepticism on HN centers on non-determinism in CI and debuggability, not authoring cost. Some practitioners dissent and claim non-determinism reduces flakiness. | support: A5-E58–E60 | independent_sources: 1 thread, 3 commenters | medium
A5-C20 | Runtime agents are slow and token-heavy: LELANTE takes ~11–12 s per step and success falls with step count. Anthropic says screenshots cost ~1–1.8K tokens each. GPT Driver's founders report having to truncate context. | support: A5-E57, A5-E66, A5-E70 | independent_sources: 3 | medium-high
A5-C21 | Generating durable mobile test artifacts from requirements plus code changes is shown to work industrially: on BMW's Flutter app, 100% of generated UI tests executed and 78.8% of PageObjects needed no edits. | support: A5-E68, A5-E69 | independent_sources: 1 (preprint, not peer reviewed) | medium
A5-C22 | Several vendors pair AI authoring with deterministic, LLM-free execution (Applitools Autonomous, QA Wolf, Octomind, Autify Genesis per search snippets). Momentic, Revyl, testRigor and Firebase's agent instead interpret intent at runtime. | support: A5-E45, A5-E46, A5-E54, A5-E1, A5-E42 | independent_sources: 3+ | medium-high
A5-C23 | Gemini 2.5 Computer Use (Oct 2025) is "primarily optimized for web browsers" but shows "promise" on mobile (AndroidWorld). Google uses it internally for UI testing and in the Firebase Testing Agent. Anthropic's computer-use reference environment is desktop Linux. | support: A5-E64, A5-E65, A5-E66 | independent_sources: 2 | medium-high
A5-C24 | testRigor claims plain-English tests across native and hybrid mobile with API, email and DB checks, and "50x faster than Selenium". No independent evidence was found for the speed claim. | support: A5-E43, A5-E44 | independent_sources: 0 independent | low (marketing)
```

## Landscape table

| Product                                            | Input                                                                               | Output (durable code vs runtime agent)                                                   | Mobile / RN support                                                                 | Notable technique                                                                                            |
| -------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Firebase App Testing agent                         | NL test cases (step goals, hints, final-screen assertion), APK via App Distribution | Runtime agent (Gemini). Replays cached actions but still AI-confirms; no exportable code | Android only (preview); RN works as an APK, not specifically documented             | Gemini Computer Use under the hood; 200 free tests/mo; admits non-determinism                                |
| Firebase Robo test                                 | APK; optional Robo scripts, credentials                                             | Runtime crawler, deterministic per config; crawl graph, video, logs                      | Android (an iOS variant exists in docs); RN renders native views, so it's crawlable | Scriptless exploration; no business-logic oracle                                                             |
| Playwright Test Agents (v1.56+)                    | NL request + seed test (+ optional PRD); live app                                   | Durable Playwright test code + Markdown plans in repo                                    | Web only                                                                            | Planner → generator → healer; generator verifies selectors live; Claude Code supported                       |
| Playwright MCP                                     | Agent tool calls on a live browser                                                  | Neither by itself; the substrate agents use                                              | Web only                                                                            | Bundled in Playwright 1.62+; WebMCP in 1.64                                                                  |
| Maestro MCP + coding agent                         | Live device/simulator via MCP (`inspect_screen`, `run`)                             | Durable Maestro YAML Flows saved to `.maestro/`                                          | iOS sim, Android emu, web; RN/Expo is Maestro's core audience                       | Explore inline YAML, then persist the working Flow                                                           |
| Maestro `assertWithAI`                             | Screenshot + NL assertion                                                           | Runtime LLM check inside a durable flow                                                  | Mobile + web                                                                        | Experimental, `optional: true` by default                                                                    |
| Momentic                                           | NL steps in YAML in repo                                                            | Hybrid: runtime AI resolution + step cache for deterministic replay                      | Web, iOS sims, Android emus (no physical devices)                                   | Cache multi-signal locators; AI re-resolve on miss; "memory" across runs                                     |
| QA Wolf                                            | Managed service; human QA + AI                                                      | Durable Playwright/Appium code                                                           | Web, iOS, Android                                                                   | Diagnosis-first healing; per-test pricing (~$40–44/test/mo est.)                                             |
| Octomind (shut down mid-2026)                      | App URL                                                                             | Durable Playwright code (portable)                                                       | Web                                                                                 | URL-only flow discovery; failed commercially                                                                 |
| Checksum                                           | Real user sessions (<200)                                                           | Durable Playwright/Cypress code                                                          | Web                                                                                 | Learns paths from production sessions, then generates code + assertions                                      |
| Meticulous                                         | JS recorder on dev/staging/prod sessions                                            | Replayed sessions with visual diffs (not hand-editable tests)                            | Web only                                                                            | Network stubbing from recordings; schema-aware response patching; 2026 backend record & replay; Agent Skills |
| Applitools Autonomous / Eyes                       | Sitemap crawl, NL authoring, recordings                                             | Deterministic steps, no LLM at runtime (per vendor)                                      | Claims native mobile                                                                | Visual AI diffs                                                                                              |
| Autify Genesis                                     | Requirements docs (PDF/Jira/Figma) + live app                                       | Durable Playwright code (search snippets only, not fetched)                              | Not verified                                                                        | Requirements → Gherkin → agent grounds real locators                                                         |
| testRigor                                          | Plain-English steps; generates from documented test cases                           | Runtime interpretation of English                                                        | Native + hybrid iOS/Android (claimed)                                               | API, email and DB checks in-test                                                                             |
| Revyl                                              | PR/intents via coding agents or Revyl agent; NL or YAML                             | Runtime agent on Revyl infra; evidence stored in "Atlas"                                 | iOS, Android, RN, Expo, Flutter, KMP                                                | Verification of changes; MCP for coding agents                                                               |
| Arbigent (OSS)                                     | NL goals, YAML, UI; dependent scenarios                                             | Runtime agent; optional replay-with-fallback cache                                       | Android, iOS, web, TV                                                               | Scenario dependency graph; Maestro YAML as setup; multi-LLM                                                  |
| Midscene.js (OSS)                                  | NL `aiAct`/`aiAssert`/`aiQuery` in JS or YAML                                       | Runtime vision agent; plan cache                                                         | Android (ADB), iOS (WDA), HarmonyOS, web, desktop                                   | Pure vision; cheap VLMs (e.g., Qwen, Doubao); locator cache web-only                                         |
| Stagehand / Browserbase                            | NL `act`/`observe` in TS                                                            | Hybrid: `observe()` yields replayable actions with selectors; cache                      | Web only                                                                            | Cache key = instruction + page content; miss triggers inference                                              |
| GPT Driver (MobileBoost)                           | NL mobile tests                                                                     | Runtime, "command-first", AI only when commands fail                                     | iOS/Android                                                                         | Custom object-detection models; caching to get <4 s per loop                                                 |
| Gemini 2.5 Computer Use                            | Screenshot + goal                                                                   | Model API (substrate)                                                                    | Web; "promise" on Android                                                           | Powers Firebase agent and Google-internal UI testing                                                         |
| Anthropic computer use                             | Screenshot + goal                                                                   | Model API (substrate), GA on Claude API                                                  | Desktop/Linux reference env; no mobile mention                                      | 1–1.8K tokens per screenshot; injection classifiers                                                          |
| Mabl, Testim/Tricentis, Functionize, Rainforest QA | not investigated in fetched sources                                                 |                                                                                          |                                                                                     |                                                                                                              |

## Conflicts & gaps

- **Determinism claims conflict.** Meticulous calls itself "the only testing tool that eliminates flakes" (A5-E27), QA Wolf offers a "zero-flake guarantee" (A5-S24), and Momentic claims "deterministic replay" (A5-E22). None of these has independent measurement. On HN one practitioner says non-determinism _reduces_ flakiness (A5-E60) and others reject it outright (A5-E59). There is no neutral benchmark.
- **The Gemini Computer Use latency figure is unreliable.** The fetch summary said "~225 seconds of latency on benchmarks", which is probably a misread chart, so it is excluded from the claims. Re-check it against the chart before use.
- **Octomind shutdown** rests on one fetched third-party source (A5-S24) plus a search snippet of Octomind's own letter. The letter page failed DNS, so its exact date and wording are unverified.
- **Autify Genesis** details come only from search snippets (the TestGuild page returned no body), so they are not counted as evidence.
- **The App Testing agent's iOS status** comes from the Android doc only. There may be a separate iOS page or roadmap; none was found.
- **Not investigated:** Mabl, Testim/Tricentis, Functionize, Rainforest QA, and Maestro Studio's AI/"MaestroGPT" (the docs index showed no such feature, and it may have been retired or renamed). `assertNoDefectsWithAI` was not found on the fetched page, so its current existence is unconfirmed.
- **Backend assertions:** apart from testRigor (DB/API, claimed) and Meticulous's new backend record & replay, no product in this set documents asserting on Firestore/Firebase backend state. That is a real gap for an RN + Firebase target.
- **React Native specifically:** only Revyl and Maestro (by audience) name RN/Expo. Everyone else is "native iOS/Android", which RN satisfies at the accessibility-tree level, but testID/accessibility-label quality is the hidden dependency.
- **Quote fidelity:** quotes passed through WebFetch's summarizer, so re-verify the load-bearing ones (A5-E3, E12, E17, E21, E48, E50) on the live pages.
- **Vendor bias:** most self-healing criticism (A5-S21, A5-S23) comes from vendors selling the "right" kind of healing. Ministry of Testing (A5-S22) is the only neutral source on that point.

## Analyst assessment

(Analyst judgment, separate from the sourced claims above.)

**Buy vs build.** Nothing found does what `/generate-e2e` proposes: read an RN + Firebase codebase, write a behavioral spec, and emit a durable mobile E2E suite with backend assertions. The products split into two camps. _Runtime-agent_ tools (Firebase App Testing agent, Momentic, Revyl, testRigor, Arbigent, Midscene, GPT Driver) re-interpret intent on every run. That costs about 10 s per step and tokens per screenshot, and Google itself admits its agent takes different actions on the same instructions. _Durable-code_ tools (Playwright Test Agents, QA Wolf, Checksum, the late Octomind, Autify Genesis, Applitools) produce deterministic scripts but are web-first. QA Wolf is the only one with mobile (Appium) code, and it is a ~$90K/yr managed service. None of them uses the codebase as a primary input; they work from the running UI, sessions, a URL or requirements docs. The AToMIC BMW study (requirements plus code diffs → Gherkin → PageObjects → scripts) is the closest analogue, and it is academic and Flutter-based.

The Octomind shutdown is a warning about the business, not the technique: portable generated code removes lock-in, and with it the vendor's moat (the HN "moat" question in A5-E61 aged well). For an internal tool that is a feature, not a bug.

**Recommendation: compose, don't buy.** Build `/generate-e2e` as a Claude Code skill on top of **Maestro MCP**. It already handles RN/Expo, iOS and Android, has a Claude Code integration, and Maestro's own guidance (explore live, then save a Flow) is exactly the generator step. Output plain Maestro YAML (durable, CI-deterministic, no vendor runtime). Optionally evaluate Firebase's App Testing agent as a free exploratory smoke layer (Android, 200 runs/month), never as the regression gate.

**Techniques worth borrowing:**

1. **Playwright's planner → generator → healer split**, ported to mobile. The planner writes a Markdown spec (here grounded in code plus live exploration); the generator writes Maestro YAML and _verifies each selector live_ before saving; the healer handles failures.
2. **The healer must diagnose before it patches, and it must not touch assertions.** Self-greening is the main documented failure mode. The healer may change locators and waits, but any change to an assertion or a removed step goes to human review. Classify failures first using network, console, Firestore-emulator state and fixtures, as QA Wolf describes.
3. **Cache-then-replay.** Spend LLM calls at generation and heal time, never on the green path (Arbigent replay-with-fallback, Stagehand/Midscene caches). Generated YAML is the ultimate cache.
4. **Backend oracles via the Firebase emulator.** Assert Firestore/Auth state after flows, which no surveyed product does for Firebase. Meticulous-style network stubbing is the wrong model here because it explicitly skips backend correctness.
5. **Keep LLM visual assertions non-blocking** (Maestro's `optional: true` default is the honest setting) and use them for triage, not gating.
6. **Robo-style scriptless crawling** as a cheap coverage-discovery input to the planner, for screens the code analysis missed.

The biggest open risk is not authoring. As HN commenters note, it is whether the generated tests fail for understandable reasons. Design for debuggability (one behavior per flow, testID-based selectors, explicit backend checks) over raw coverage counts.
