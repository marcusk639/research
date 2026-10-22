# Angle A1 — Mobile E2E frameworks and the runtime/execution layer

Fetched 2026-10-21 with built-in WebSearch/WebFetch only. Quotes come from WebFetch extractions of each page. WebFetch passes pages through a summarizer model, so check load-bearing quotes against the live page before final publication.

## Sources

A1-S1 | https://maestro.dev/blog/maestro-mcp-an-introduction | Maestro MCP: an introduction | mobile.dev (Maestro vendor) | 2026-04-14 | secondary
A1-S2 | https://docs.maestro.dev/get-started/maestro-mcp | Maestro MCP (docs) | mobile.dev | n.d. | primary (official docs)
A1-S3 | https://devicelab.dev/blog/1319-issues-data-driven | 1319 issues, data-driven (Maestro issue analysis) | DeviceLab (Om Narayan) | 2026-01-27 | blog (vendor-adjacent: sells a device lab / Maestro iOS bridge)
A1-S4 | https://github.com/mobile-dev-inc/maestro/issues/1585 | [1.34.1] MaestroDriverStartupException$IOSDriverTimeoutException | Maestro GitHub | opened 2023-11-10, closed | primary
A1-S5 | https://github.com/mobile-dev-inc/maestro/issues/395 | inputText is typing too fast and skipping characters when app stutters/jank | Maestro GitHub | opened 2022-11-14, closed 2026-10-01 | primary
A1-S6 | https://raw.githubusercontent.com/mobile-dev-inc/maestro/main/CHANGELOG.md (+ /releases) | Maestro CHANGELOG / releases (CLI 2.11.0, 29 Sep 2026) | Maestro GitHub | 2026 | primary
A1-S7 | https://devicelab.dev/blog/maestro-real-ios-complete-guide | Maestro on real iOS: complete guide | DeviceLab | 2025-12-29 | blog (vendor-adjacent)
A1-S8 | https://docs.maestro.dev/get-started/supported-platform/react-native | Maestro React Native support | mobile.dev | n.d. | primary
A1-S9 | https://docs.maestro.dev/platform-support/web-desktop-browser | Maestro web (desktop browser) support | mobile.dev | n.d. | primary
A1-S10 | https://maestro.dev/insights/detox-vs-maestro-reducing-flakiness-react-native | Detox vs Maestro: reducing flakiness in React Native | mobile.dev | 2026-03-26 | secondary (vendor about own product)
A1-S11 | https://maestro.dev/pricing | Maestro pricing | mobile.dev | n.d. | secondary
A1-S12 | https://wix.github.io/Detox/docs/articles/design-principles | Detox design principles | Wix | n.d. | primary
A1-S13 | https://wix.github.io/Detox/docs/introduction/environment-setup | Detox environment setup | Wix | n.d. | primary
A1-S14 | https://github.com/wix/Detox | Detox README | Wix | n.d. | primary
A1-S15 | https://github.com/wix/Detox/releases/tag/20.34.0 | Detox 20.34.0 release | Wix | Feb 16 (year not shown; ~2025) | primary
A1-S16 | https://github.com/wix/Detox/releases?q=0.72 | Detox 20.17.0 release ("Added support for React Native 0.72.x") | Wix | Jan 22 (year not shown; ~2024) | primary
A1-S17 | https://wix.github.io/Detox/docs/troubleshooting/synchronization | Detox troubleshooting: synchronization | Wix | n.d. | primary
A1-S18 | https://app.unpkg.com/@wix-pilot/core@3.3.4/files/README.md | @wix-pilot/core README | Wix | n.d. | primary
A1-S19 | https://github.com/appium/appium-mcp | appium-mcp | Appium project | n.d. | primary
A1-S20 | https://appium.github.io/appium-xcuitest-driver/latest/getting-started/system-requirements/ | XCUITest driver system requirements | Appium project | n.d. | primary
A1-S21 | https://github.com/mobile-next/mobile-mcp | mobile-mcp README | mobile-next | n.d. | primary (project's own repo)
A1-S22 | https://github.com/leancodepl/patrol/blob/master/README.md | Patrol README | LeanCode | n.d. | primary
A1-S23 | https://www.browserstack.com/docs/app-automate/maestro | BrowserStack App Automate: Maestro | BrowserStack | n.d. | secondary
A1-S24 | https://firebase.google.com/docs/test-lab | Firebase Test Lab overview | Google | n.d. | primary
A1-S25 | https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types.html | Device Farm test frameworks | AWS | n.d. | primary
A1-S26 | https://docs.expo.dev/eas/workflows/examples/e2e-tests/ | EAS Workflows: E2E tests | Expo | n.d. | primary
A1-S27 | https://github.com/microsoft/playwright-mcp | Playwright MCP README | Microsoft | n.d. | primary
A1-S28 | https://verygood.ventures/blog/maestro-mcp-claude-mobile-ui-test-automation/ | Using Maestro MCP with Claude | Very Good Ventures (Rafael Theni) | n.d. (2026) | blog
A1-S29 | https://conf.researchr.org/details/saner-2026/saner-2026-workshops-tutorials-track/44/... | "I Will Try to Fix You": LLMs for Mobile GUI Test Repair | SANER 2026 | 2026 | primary (peer-reviewed abstract)

## Evidence

A1-E1 | A1-S2 | "`inspect_screen` | Get the current screen's view hierarchy as compact JSON" | MCP tools table
A1-E2 | A1-S2 | "`run` | Execute Maestro flows. Accepts exactly one of `{ yaml }` (inline YAML, preferred for exploration)" | MCP tools table
A1-E3 | A1-S2 | "`list_devices` | List all available local devices (Android emulators, iOS simulators, and Chromium for web)" | MCP tools table
A1-E4 | A1-S2 | "`cheat_sheet` | Return the Maestro cheat sheet covering common commands, flow syntax, and best practices" | MCP tools table
A1-E5 | A1-S1 | "Run the Maestro MCP Server using `maestro mcp` in your terminal" | setup section
A1-E6 | A1-S3 | "The XCTest process crashes during initialization, times out on slow CI machines, or returns stale hierarchy data." | "The Pattern Nobody Talks About"
A1-E7 | A1-S3 | "If any link in that chain stalls...the whole stack enters an undefined state." | "The Pattern Nobody Talks About"
A1-E8 | A1-S4 | "The Flow fails at Maestro iOS driver did not start up in time." | original report
A1-E9 | A1-S4 | "Generally, it works, but many times I have gotten the timeout error, which persists even after rerunning." | comment (satya164, CI)
A1-E10 | A1-S4 | Maintainer workaround `export MAESTRO_DRIVER_STARTUP_TIMEOUT=60000`; reporter said it did not fix the issue; issue closed for lack of repro steps | maintainer comment (yuseiatlas, 2023-11-22), per WebFetch summary
A1-E11 | A1-S5 | "When executing `inputText` to type `Lorem ipsum`, sometimes it'll actually type `Loemipsu`. The skipped characters are random" | first comment (Nov 2022)
A1-E12 | A1-S5 | "I am stuck with running tests on Maestro because of this. A simple option to slow down typing would already be enough" | comment (Sep 2024)
A1-E13 | A1-S6 | "iOS: stop listing physical iPhones as devices, and fail attempted runs early with 'Physical iOS devices are not yet supported'" | CHANGELOG 2.11.0
A1-E14 | A1-S6 | "iOS: fix timeout handling when stopping and starting apps" | CHANGELOG 2.7.0
A1-E15 | A1-S7 | "Maestro doesn't support physical iOS devices" | intro
A1-E16 | A1-S8 | "The best practice is to use the `testID` property, which Maestro maps to a unique `id`." | selectors section
A1-E17 | A1-S8 | "You don't need to install any npm packages (like Detox or Appium drivers) inside your app. Maestro tests the final bundled binary." | setup section
A1-E18 | A1-S8 | "On iOS, React Native sometimes 'swallows' touch events if components are deeply nested." | iOS caveat
A1-E19 | A1-S9 | "Web support is currently in Beta. It is functional for Chromium-based testing" | intro
A1-E20 | A1-S9 | "the current default and only supported browser is Chromium." | browsers
A1-E21 | A1-S10 | "Users have reported flakiness rates of less than 1%" | Maestro section
A1-E22 | A1-S10 | "continuous visual changes - like shimmer effects or video backgrounds - can trick Maestro into thinking the UI hasn't stabilized." | limitations
A1-E23 | A1-S10 | "The synchronization engine ensures UI stability by checking for settling every 200 milliseconds, with animations allowed up to 2 seconds" | zero-wait section
A1-E24 | A1-S11 | "$250/device/mo" (hosted Android, iOS and web devices; "Unlimited hosted test runs") | Cloud tier
A1-E25 | A1-S12 | "switching to gray box allows the test framework to monitor the app from the inside and delivers critical wins like fighting flakiness at the core" | "Detox does gray box, not black box"
A1-E26 | A1-S12 | "Detox times its actions, by default, to run only when your app is idle, meaning it has determined that your app has finished its work, such as animations, network requests" | "Detox synchronizes with your app's activity"
A1-E27 | A1-S13 | "RN `v0.77.x` - `v0.84.x`: Fully compatible with React Native's 'New Architecture'. Newer RN versions might work with Detox, but they've not been thoroughly tested" | Requirements
A1-E28 | A1-S14 | "Although we do not officially support older React Native versions, we do our best to keep Detox compatible with them" | README, compatibility
A1-E29 | A1-S13 | "Expo integration with Detox is entirely a community-driven effort. There is no special support for Expo projects in Detox" | Expo note
A1-E30 | A1-S16 | "Added support for React Native 0.72.x!" | Detox 20.17.0 release notes
A1-E31 | A1-S15 | "This release fully completes support for React Native's new-architecture (bridge-less and fabric) for iOS + Android, over RN v0.76" | 20.34.0 release notes
A1-E32 | A1-S17 | Sync is blocked by endless animations, long timers, network polling; last-resort `device.disableSynchronization()` with explicit `waitFor(...).withTimeout()` | troubleshooting page (paraphrase of WebFetch summary, not verbatim)
A1-E33 | A1-S18 | "A flexible plugin that drives your tests with human-written commands, enhanced by the power of large language models (LLMs)" | README intro
A1-E34 | A1-S18 | "Detox driver for React Native testing" / "Appium driver for mobile testing" / "Playwright driver for modern web testing" | drivers list
A1-E35 | A1-S19 | "MCP (Model Context Protocol) server designed to empower AI assistants with a robust suite of tools for mobile automation." | README intro
A1-E36 | A1-S19 | Tools include `appium_get_page_source`, `generate_locators`, `appium_generate_tests`; generated output is Java/TestNG | tools list (per WebFetch summary)
A1-E37 | A1-S20 | "The XCUITest driver aims to _fully support_ the latest _two_ (2) major Xcode/iOS/iPadOS/tvOS/watchOS versions." | System requirements
A1-E38 | A1-S20 | "ensure that the version of the [WebDriverAgent (WDA)] server application (which the driver installs on the device under test) is also downgraded accordingly." | System requirements note
A1-E39 | A1-S21 | "Accessibility-first — fast and cheap: drives apps from the native accessibility tree (no vision model, no image tokens), falling back to screenshots + coordinates only when needed." | Main Features
A1-E40 | A1-S21 | mobilewright is the option "when you're ready to turn agent-driven exploration into repeatable, deterministic tests for iOS and Android." | README
A1-E41 | A1-S22 | "A powerful, multiplatform E2E UI testing framework for Flutter apps that overcomes the limitations of integration_test by handling native interactions." | README intro
A1-E42 | A1-S23 | "Run your Maestro tests on real Android and iOS devices in the cloud" | page intro; framework selector also lists Appium, Espresso, XCUITest, Flutter, Detox, Mobilewright
A1-E43 | A1-S24 | Test Lab lists Android "Instrumentation test", Robo, Game Loop; iOS XCTest, Game Loop, Robo; no mention of Maestro, Appium or Detox | overview (per WebFetch summary)
A1-E44 | A1-S25 | Android: "Automatic Appium tests", "Instrumentation"; iOS: "Automatic Appium tests", "XCTest", "XCTest UI" | Testing frameworks
A1-E45 | A1-S26 | "Learn how to run end-to-end (E2E) tests on EAS Workflows using Maestro" | intro
A1-E46 | A1-S26 | "E2E tests require a built app file: **.apk** for Android or **.app** for iOS — that EAS can install and test on an emulator/simulator." | prerequisites
A1-E47 | A1-S27 | Playwright MCP uses "Playwright's accessibility tree, not pixel-based input" and gives "deterministic tool application" | README intro
A1-E48 | A1-S28 | "Natural language test generation can also produce flows that are syntactically valid but miss business logic" | limitations paragraph
A1-E49 | A1-S29 | "tests break across application versions not because of functional defects, but due to changes in the GUI structure, appearance, or properties" | abstract
A1-E50 | A1-S29 | "The LLM-based method successfully repaired 45 out of 61 tests (73.8%) after a single interaction and 56 out of 61 tests (91.8%) after multiple interactions" | abstract

## Claims

A1-C1 | Maestro ships an official MCP server (`maestro mcp`) that lets an agent list devices, read the view hierarchy as JSON, take screenshots and run inline YAML. | support: A1-E1, A1-E2, A1-E3, A1-E5 | independent_sources: 1 (vendor docs + vendor blog) | confidence: high (official docs, features not independently benchmarked)
A1-C2 | Maestro's iOS simulator driver has a long, documented history of startup timeouts and XCTest-runner failures, and the main issue (#1585) was closed without a root-cause fix. | support: A1-E6, A1-E7, A1-E8, A1-E9, A1-E10 | independent_sources: 2 (GitHub issue; DeviceLab analysis) | confidence: high
A1-C3 | The reference project's "driver crashes every 2–4 runs" fits a known Maestro iOS failure class. Not a local misconfiguration. | support: A1-E6, A1-E9 | independent_sources: 2 | confidence: medium (no exact rate published anywhere)
A1-C4 | Maestro `inputText` has dropped characters at random on both iOS and Android, especially when the app janks. This would explain flaky Formik field input. | support: A1-E11, A1-E12 | independent_sources: 1 (multi-reporter GitHub thread) | confidence: high for the bug; medium that it causes the reference project's Formik flakes
A1-C5 | As of CLI 2.11.0 (Sep 2026), Maestro refuses to run on physical iOS devices. | support: A1-E13, A1-E15 | independent_sources: 2 | confidence: high
A1-C6 | Maestro works with a React Native app without any in-app instrumentation, and maps RN `testID` to its `id` selector. | support: A1-E16, A1-E17 | independent_sources: 1 | confidence: high
A1-C7 | Maestro web support is Beta and runs on Chromium only. It is a weak substitute for Playwright on the Angular companion app. | support: A1-E19, A1-E20 | independent_sources: 1 | confidence: high
A1-C8 | Maestro is black-box. It infers UI stability by polling, and continuous animations can defeat that check. | support: A1-E22, A1-E23 | independent_sources: 1 (vendor admission) | confidence: medium
A1-C9 | The head-to-head flakiness figures (Maestro <1%, Detox <2%) are vendor claims with no independent measurement and should not carry weight. | support: A1-E21 | independent_sources: 0 | confidence: low (as a fact about flakiness)
A1-C10 | Detox is gray-box. By default it holds each action until the app is idle (animations, network, RN load), which removes a whole class of timing flakes. | support: A1-E25, A1-E26 | independent_sources: 1 (Wix docs) | confidence: high for the mechanism; medium for real-world flakiness reduction
A1-C11 | Detox's gray-box sync breaks on apps that never go idle (endless animations, long timers, polling). The fallback is to disable sync and wait explicitly, which brings back black-box timing risk. | support: A1-E32 | independent_sources: 1 | confidence: high
A1-C12 | Current Detox officially supports only RN 0.77–0.84. RN 0.72 support was added in Detox 20.17.0, so an RN 0.72 app needs a pinned older Detox release or an RN upgrade. | support: A1-E27, A1-E28, A1-E30, A1-E31 | independent_sources: 1 (Wix, several pages) | confidence: high
A1-C13 | Detox has no official Expo support. | support: A1-E29 | independent_sources: 1 | confidence: high (does not matter for a bare RN 0.72 app)
A1-C14 | Wix Pilot (formerly Detox Copilot) runs natural-language test steps through an LLM. Drivers exist for Detox, Appium, Playwright and Puppeteer. | support: A1-E33, A1-E34 | independent_sources: 1 | confidence: high (exists); low (maturity is unverified: alpha tags seen)
A1-C15 | Appium has an official MCP server. It exposes page source, locator generation and test generation, but generates Java/TestNG, which does not fit a JS/TS RN repo. | support: A1-E35, A1-E36 | independent_sources: 1 | confidence: high
A1-C16 | Appium's iOS XCUITest driver is tied to Xcode versions and fully supports only the latest two majors, with WDA versions locked to the driver. New Xcode releases mean driver/WDA upgrades. | support: A1-E37, A1-E38 | independent_sources: 1 | confidence: high
A1-C17 | mobile-next/mobile-mcp is a framework-neutral MCP that drives iOS and Android from the native accessibility tree, with screenshots as fallback. It explores; it does not emit a test suite. | support: A1-E39, A1-E40 | independent_sources: 1 | confidence: high
A1-C18 | Patrol is Flutter-only, so it does not apply to React Native. | support: A1-E41 | independent_sources: 1 | confidence: high
A1-C19 | BrowserStack runs Maestro on real iOS and Android devices and also supports Detox, Appium, Espresso and XCUITest. | support: A1-E42 | independent_sources: 1 (vendor) | confidence: medium
A1-C20 | Firebase Test Lab and AWS Device Farm do not natively list Maestro or Detox. FTL takes instrumentation/Espresso/XCTest/Robo; Device Farm takes Appium, instrumentation and XCTest/XCUITest. | support: A1-E43, A1-E44 | independent_sources: 2 | confidence: high
A1-C21 | EAS Workflows' documented E2E path is Maestro on emulator/simulator, using a prebuilt .apk/.app. | support: A1-E45, A1-E46 | independent_sources: 1 | confidence: high
A1-C22 | Maestro Cloud costs $250 per device per month. | support: A1-E24 | independent_sources: 1 | confidence: high
A1-C23 | Playwright MCP drives web through the accessibility tree and has no native-app support, so it suits the Angular half only. | support: A1-E47 | independent_sources: 1 | confidence: high
A1-C24 | LLM-generated flows can be syntactically valid and still miss business logic. | support: A1-E48 | independent_sources: 1 | confidence: medium
A1-C25 | Most GUI test breakage comes from UI structure changes rather than defects, and LLMs repaired 73.8% of broken tests in one pass (91.8% with several passes) in one Android study. | support: A1-E49, A1-E50 | independent_sources: 1 (peer-reviewed) | confidence: medium (small n=61, Android only)

## Conflicts & gaps

- **Flakiness numbers conflict and are unverified.** Maestro's own page claims under 1% for Maestro and under 2% for Detox (A1-S10). Search snippets from AI-testing vendors (autosana, drizz, getpanto) claimed about 15% Appium flakiness and a "25% login failure" anecdote. None of these were fetched and verified, so none are cited. No independent, peer-reviewed flakiness benchmark comparing Maestro, Detox and Appium on React Native turned up.
- **DeviceLab (A1-S3, A1-S7) is vendor-adjacent.** It sells device-lab infrastructure and an open-source Maestro iOS bridge, so it has a motive to stress Maestro iOS fragility. Its issue numbers check out against the GitHub sources (A1-S4, A1-S5).
- **Issue #1585 summary.** The WebFetch summary mentions "Xcode 26.3" in a CI run in the thread, which suggests the timeout failure class continued into 2026 despite the 2023 open date. Confirm against the raw thread. I found no dedicated Maestro issue for Xcode 26 build breakage. Searches returned only general Xcode 26 simulator boot-freeze notes from CircleCI changelogs, which I did not fetch.
- **Detox release years.** The release pages show "Jan 22" (20.17.0) and "Feb 16" (20.34.0) without a year. My best estimate is 2024 and 2025, unconfirmed.
- **Detox and RN 0.72 reliability today.** I found no data on how stable a pinned Detox 20.17-era release is with current Xcode 26 and iOS 26 simulators. That is a real risk, and a spike should test it directly.
- **Unreachable:** life.jupiter.money "Choosing between Maestro and Detox" (HTTP 403). The Detox "how-detox-works" URL returned 404. A Maestro `hierarchy` CLI docs page was not found, so the `inspect_screen` MCP tool (A1-E1) is the verified hierarchy route.
- **Not checked:** Android-specific blockers in the reference project. AWS Device Farm custom environments may run arbitrary shell commands (and so possibly Maestro or Detox), but the page did not say so for those frameworks. Maestro Cloud's device type (real vs simulator) was not stated on the pricing page.
- **No primary evidence** that any framework has been tested at scale with LLM-generated suites. The practitioner posts (A1-S28) are guides, not measured reports.

## Analyst assessment

**Sourced core.** The two leading RN runtimes fail in opposite ways. Maestro is black-box, needs no instrumentation and uses YAML. It has the most agent-ready tooling: an official MCP with hierarchy inspection, inline-YAML execution and a cheat-sheet tool. Its weak spots are exactly the ones the reference project hit: the iOS XCTest driver lifecycle (startup timeouts, crashes, stale hierarchy) and an `inputText` that drops characters on janky screens. Detox is gray-box and waits for idle, so it removes the Formik-style "typed before ready" class of flakes at the source. But it needs a native test build and Jest harness, it breaks on apps that never go idle, and its official support window (RN 0.77–0.84) excludes RN 0.72. You would pin an older Detox release (0.72 support arrived in 20.17.0) and then deal with today's Xcode yourself. Appium is the most cloud-portable option (Device Farm, BrowserStack) and has an official MCP. However, its XCUITest/WDA stack has the same Xcode-churn exposure, it is black-box like Maestro, and its MCP generates Java, which fits poorly in a TS repo. Patrol is Flutter-only and out of scope.

**Recommendation (analyst judgment).** Make the generator target-agnostic: one behavioral spec, rendered into backends. Do not marry it to one DSL.

1. **Primary mobile backend: Detox (TS), pinned to an RN-0.72-compatible release.** Hold it to that only if a one-day spike shows it builds and runs under the current Xcode on simulators. Gray-box sync addresses the reference project's dominant failure (timing flakes), and TS output can import shared fixtures (Firebase emulator seeding, Stripe test clocks) that YAML cannot express cleanly. If the spike fails, upgrading RN is the real fix, and that is a product decision, not a tooling one.
2. **Exploration plane: Maestro MCP or mobile-mcp, used only while generating.** The agent explores live UI through the accessibility tree, discovers testIDs and confirms screens. It then emits Detox code (or Maestro YAML as a smoke tier). This splits "agent sees the app" from "suite runs in CI", so Maestro's driver instability costs exploration retries rather than suite reliability.
3. **Optional Maestro smoke tier** on EAS or BrowserStack, where someone else runs the iOS driver. Add `waitForAnimationToEnd` or character-wise input around forms.
4. **Web half: Playwright (+ Playwright MCP).** Maestro web is Chromium-only Beta.
5. **Instrumentation as a generator step.** The skill should add stable `testID`s (Maestro and Detox both key on them) as a reviewed code diff before generating tests. Text and visual selectors are what breaks (A1-E49).

**Failure modes to design for:** never-idle screens that break Detox sync (the generator must flag looping animations and polling listeners such as Firestore `onSnapshot`); hallucinated business assertions (A1-E48), so require each assertion to trace back to a spec line; Xcode upgrades breaking any XCTest-based driver, so pin the Xcode version in CI; and repair loops. LLM repair is credible for locator drift (73.8–91.8%, A1-E50), but a run that has only been repaired should not count as green without a rerun.

**Novel idea:** quarantine flakes by layer. Run every generated test N times at generation time, and classify failures as driver (process/timeout), timing (passes on retry) or assertion. Only assertion failures go back to the LLM. Driver failures go to infrastructure retries. That keeps the agent from "fixing" tests to work around runtime bugs, which is likely the reference project's main problem.
