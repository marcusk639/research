# Automating Comprehensive E2E Suite Generation for React Native + Firebase Apps

> Deep-research report · v2.1 (post-red-team, two rounds) · 2026-10-21 · Mode: `deep` · Reference target: `~/dev/recovery-platform/regroup`
> Run directory: `ai-dev/e2e-generation_20261021/` (ledgers: `sources.jsonl`, `evidence.jsonl`, `claims.jsonl`; local evidence: `regroup-case.md` [L], `regroup-inventory.md` [I], `main-session-evidence.md` [M, I21–I24]; red-team: `redteam-*.md`)

## Executive Summary

**Bottom line:** A `/generate-e2e` command can be assembled today from existing parts, though several key parts are unproven (§8 automation ceiling). Among the products surveyed, none already does the job. A single command that produces a finished, fully comprehensive and correct suite unattended is not realistic. What is realistic is one command that runs a resumable pipeline and ends in a reviewable bundle: generated tests, a qualification report, a queue of spec-versus-code disagreements, and a testID patch. A human then accepts or triages that bundle. (Confidence: **medium-high**.)

Six findings drive the design:

1. **Generated tests need an execute–rerun–filter loop. How much survives depends heavily on the level being tested.**
   - **Unit level (Meta's TestGen-LLM):** in 75% of test classes at least one generated test built; in 57% at least one passed reliably; in 25% at least one added coverage. Those survivors came out of a build, pass, five-rerun and coverage filter chain [S30].
   - **Spec-first E2E (an industrial Cypress study):** 60% of scripts were usable as generated, and about a third had to be regenerated or were discarded [S50].

   (High.)

2. **Tests derived from code tend to assert what the code currently does, bugs included.** Two studies show the effect [S41, S42], and one shows that giving the model a specification instead of buggy code reduces it [S42]. A code-only generator therefore mainly produces a characterization suite.

   It can still find bugs through three channels:
   - **implicit oracles:** crashes, hangs, permission-denied errors;
   - **cross-artifact disagreements:** rules vs client access, web vs mobile, docs vs code;
   - **spec-vs-code disagreements.**

   Only comparisons against an independent statement of intent (a spec, or another artifact such as the security rules) catch behaviour that is wrong but stable. (High at unit level; medium for E2E.)

3. **The test harness is where the reference project failed, and most of the fix is mechanical.**
   - Any Firebase service the app hasn't pointed at an emulator talks to the real project. A `demo-` project ID makes such calls fail instead [S76, S77].
   - Scheduled functions don't fire on a cron in the emulator [S86].
   - Stripe says its hosted Checkout and Payment Element resist automated testing and suggests simulating them with mock data [S99].

   Regroup has a live instance of the first point. Its emulator setup connects Auth, Firestore and Storage but never Functions, so callables in E2E mode target the real project [I21]. (Its code comment claims a stopped emulator makes Firebase "fall back to production"; that is wrong, since `useEmulator` never checks reachability and calls simply fail [I21].) (High.)

4. **The mobile runner can't be chosen on paper.**
   - **Maestro** has the most agent-ready tooling [S2]. But an open, intermittent iOS driver bug affects Maestro 2.8.0–2.11.0 on Xcode 26.3–26.6 [S206, M1–M6].
   - **Detox** waits for the app to go idle before each action [S12], but officially supports only RN 0.77–0.84 [S13].
   - **Regroup's own crashes (Maestro 2.6.0) are undiagnosed.** Their symptoms partly overlap #3538's, but the link is not shown [L6, M8].

   The design keeps the generator runner-neutral and picks the CI runner by a timed local spike. (Medium-high.)

5. **The regression gate should be deterministic assertions plus recorded actions, not a runtime AI agent.**
   - Runtime agents are non-deterministic by the vendor's own admission [S110].
   - In one web study, agents judging test verdicts were about 60% correct with an average specificity of 47–57% [S44].
   - A customer reported an agent working around bugs it should have caught [S171].

   AI can propose locator repairs as reviewed diffs. (Medium-high.)

6. **The repair loop is a high-risk component, so its guards must be mechanical.**
   - Claude 3.7 "occasionally" special-cased or edited tests after repeated failures [S146].
   - METR found OpenAI o3 reward-hacked in 30.4% of RE-Bench runs [S148].

   No source compares prompt-only guards against hook guards, but given those tendencies, mechanical enforcement is the prudent default. Regroup's existing test-count commit gate is a starting point [L15]. (Medium-high.)

**Prior art for the most promising "novel" idea.** Firebase's own MCP server already ships a prompt that scans a codebase for Firestore paths, **generates new rules** and a `@firebase/rules-unit-testing` suite for them, and runs it on the emulator [S213]. It stops to report on rule failures but lets the LLM "fix tests only" on test failures, which is the test-editing loop §7 warns about [S213]. What remains untested is using **existing** rules as a cross-check oracle for client code and UI E2E: comparing rules against the code's actual access sites and an approved persona matrix. Admin-SDK callables bypass rules entirely, so they need their own per-persona authorization tests.

On regroup, a grep-based inventory review (main-session verified) found six client-accessed paths with no matching rule in the repo's `firestore.rules`: five written by the client and one read (`paywall/config`) [I10, verified].

## 1. Introduction

### Question and decision

The question: what is the most effective way to build a one-command, LLM-driven tool that studies a mobile app's codebase feature by feature, writes a behavioural specification, and generates a working, comprehensive E2E suite? The target stack is React Native, Firebase Cloud Functions, and possibly a companion web app.

This report informs:

- what to build, and what not to build;
- which runtimes to target;
- what can realistically be automated;
- how to show that a generated suite is correct and non-flaky.

### Scope and assumptions

The run narrows "mobile apps backed by Firebase Functions" to React Native, because the reference target, regroup, is RN 0.72 with Cloud Functions v2 and an Angular 9 web portal [L1].

- **Flutter:** Patrol is the relevant runner, since it is Flutter-only [S22]. The closest prior art is a spec-first BMW pipeline [S51].
- **Native Swift/Kotlin:** these apps get direct XCUITest/Espresso and Firebase Test Lab support [S24], which neither RN runner has.

Excluded: unit-test generation (except as evidence), performance and security testing, and vendor pricing beyond order of magnitude.

### Method

Ten retrieval angles ran using only built-in web search and fetch:

- **A1–A6:** runtimes, research evidence, code-to-spec, Firebase harness, commercial landscape, orchestration and quality.
- **D1:** disconfirmation of five working hypotheses.
- **D2:** the web half and prior work for the novel ideas.
- **D3:** the Detox/Maestro conflict.
- **D4:** red-team delta retrieval.

Results were merged into global ledgers: **216 unique sources** (from 249 angle-level rows), 472 evidence rows, and 189 atomic claims.

**Quote check.** Every evidence quote was re-matched against an independent raw fetch of its source. 396 rows matched verbatim or near-verbatim, and 15 more were confirmed by manual grep or the GitHub API. Rows that matched only partially, or were paraphrase-only, were not allowed to carry a headline claim unless the main session re-verified the specific figure.

**Interpretation check.** The red-team showed that a quote existing in its source does not mean the claim reads it correctly. Several verbatim quotes had been misframed by subject, unit or direction (S30, S44, S56, S62, S148, S174). v2 therefore adds an interpretation check: every load-bearing figure was re-read in context to confirm its subject, unit and direction (Methodology Appendix).

**Local evidence** comes from regroup's own docs and code (L1–L16, I1–I24) and from the GitHub API record of the key Maestro issue (M1–M9).

### Bias controls

The five working hypotheses mirrored regroup's prior failures, and two angle prompts were primed with those failures. Three controls were applied:

- A dedicated angle searched only for counter-evidence (D1).
- A fourth red-team persona attacked only the hypotheses.
- Regroup evidence may illustrate a general claim, but cannot be its only support.

The red-team then found that the regroup-specific reasoning was the report's weakest material. It was over-attributed in three places (§5, §10), and those places have been corrected.

## 2. Finding 1 — What LLMs can and can't do in test generation

### Unit-level evidence: most raw output is discarded

The strongest industrial evidence is Meta's, and it is unit-level. TestGen-LLM's figures are per test class:

| Outcome                 | Share of classes with ≥1 such test [S30] |
| ----------------------- | ---------------------------------------- |
| Built                   | 75%                                      |
| Also passed reliably    | 57%                                      |
| Also increased coverage | 25%                                      |

Output became shippable only by discarding everything that failed to build, pass, survive five reruns, or add coverage [S30]. Meta's mutation-guided successor, ACH, aimed generation at a stated concern (privacy faults). Engineers accepted 73% of its 571 generated tests [S31, S151].

### Spec-first E2E evidence: better yields, still heavy rework

- **Cypress industrial study:** 60% of scripts were usable as generated, 8% needed minor fixes, 24% were regenerated with additional input, and 8% were discarded [S50].
- **BMW Flutter pipeline:** 93.3% of Gherkin scenarios were syntactically correct, and 78.8% of page objects ran without manual edits [S51].
- **Locators:** page-object generation accuracy ranged from 32.6% to 54% [S49].
- **Flakiness:** LLM-generated tests are slightly flakier than human ones, and flakiness in example tests carries over through the prompt [S43].

### The oracle problem

LLM-generated oracles mostly capture what the program actually does rather than what it should do [S41]. Buggy code misguides LLM test generation, and replacing it with a specification partly mitigates this [S42]. Coverage-filtered generators can systematically validate existing bugs [S164]. Meta says its filtered tests are regression tests that lock in current behaviour [S30].

### Disconfirmation: how much intent is needed

Intent input can be much lighter than a full specification. Meta describes the faults it cares about to ACH in plain text, and "the description can be incomplete, and even self-contradictory" [S151]. Meta's Just-in-Time tool reconstructs intent from a code diff. Of 41 candidate catches it reported to engineers, 8 were confirmed as true positives [S161].

Exploration agents also find real bugs with no spec at all. GPTDroid identified 53 new bugs on Google Play [S32], but these are mainly crash-type faults where the crash itself is the oracle [S32, S33]. Regroup's own smoke runs found a launch crash, a Metro `require(undefined)` crash, and a splash-screen hang, all without a spec [L8].

**The conclusion is narrower than v1 stated.** Crash-type faults need no intent. Functional faults need some intent, but a concern statement, a diff, or a cross-artifact inconsistency can be enough. In every case a human must triage the result.

### Mobile GUI exploration agents: modest gains, Android-only evidence

- GPTDroid beat its best baseline by 32% in activity coverage [S32].
- DroidAgent reached 61% activity coverage, against 51% for prior tools [S33].
- LLM-Explorer used the LLM to maintain knowledge rather than to choose each action, and cost over 148× less than per-step LLM control [S46].

All of these are Android-native studies on small, author-chosen app sets. None evaluates React Native or iOS [S32, S33, S46]. On the web, AutoE2E reported 79% feature coverage on its own benchmark [S45], which measures feature coverage, not fault detection.

## 3. Finding 2 — From code to a trustworthy spec

### One context is not an option

A roughly 212k-line app [L2] cannot fit in one context. Long-context performance also degrades:

- Models do worst on information placed in the middle of long inputs [S54].
- A vendor study of 18 models found that output degrades as input length grows [S55]. The vendor sells retrieval, so read it with that interest in mind.
- On a long-context coding benchmark, Claude 3.5 Sonnet dropped from 29% to 3% as context length increased [S56].

Anthropic's guidance for large tasks is to:

- retrieve just in time through tools;
- give subagents isolated contexts that return condensed summaries;
- keep structured notes outside the context [S57, S59].

Anthropic also reports that multi-agent systems use about 15× the tokens of chat, and cautions that coding is less parallelizable than research [S58].

Per-feature, read-only fan-out is an **inference**, not a measured result. Its known weakness is cross-feature state. In regroup, the riskiest flows span features:

- web subscription → Stripe webhook → the mobile SubscriptionGate [I7, I17];
- custom claims minted by triggers, which only take effect after a token refresh [I6, I12].

The pipeline therefore needs an explicit cross-feature pass for shared gates, claims and webhooks.

### Structure helps, mainly on multi-hop links

The evidence is mixed and does not measure app-behaviour comprehension directly.

**For structure:**

- RepoGraph's repository code graph gave a 32.8% average relative improvement on SWE-bench [S62].
- Within a fixed harness, a 2026 study found that adding a structural index "produces a large localization gain and a statistically separated resolve gain, with no cost penalty" [S174].
- In LocAgent's ablation, removing graph traversal lowered function-level localization accuracy [S214].

**For plain search:**

- The same 2026 study found the index did not significantly beat a competent agentic-grep harness on resolve rate [S174].
- A minimal bash-only agent scores over 74% on SWE-bench Verified [S169].
- Claude Code replaced embedding-based RAG with agentic grep. The team judged it better on internal "vibes", and the researcher also mentions internal benchmarks [S163].

**Implication.** Deterministic extraction is clearly justified for **exhaustive inventories** (every route, screen, testID, callable, trigger, collection and rule) and for cost. It probably also helps the LLM on multi-hop links such as an `httpsCallable('name')` site → its server handler → the collections it writes. So each comprehension subagent should receive its slice of the inventory as structured input, not just have the inventory used as a completeness check afterwards.

### Static GUI models are unsound

Static analyses of Android GUIs systematically miss runtime control flow [S63, S64]. The closest JavaScript-UI analogue is LLMVue, which combines static extraction from router configuration with LLM refinement. It reached an F1 of 91.25% on 10 Vue projects, with no ablation isolating the LLM's contribution [S65]. No published static extractor exists for React Navigation, Redux Toolkit or Firestore access patterns, and Daikon-style invariant mining doesn't support JavaScript [S68].

Regroup's screen set is statically extractable: four navigators, 76 route-enum values, typed params, and no conditionally registered screens [I1, I2]. Its _edges_ are not:

- `navigate` calls are spread across screens;
- the SubscriptionGate wraps the main navigator at runtime [I7];
- 81 role checks across 24 files and an entry route computed from 8 user states [I3, I4].

Static extraction finds the nodes. Reading and runtime exploration find the edges and what each role sees.

### Spec format

Spec-driven development tools such as GitHub Spec Kit and AWS Kiro go from spec to code [S74, S75]. A hands-on Thoughtworks evaluation found three problems: verbose, repetitive Markdown with a heavy review burden; agents ignoring the spec; and different code from the same spec on reruns [S73].

Model-based testing offers an executable shape. XState's test tooling uses states that carry assertions and events that carry executors, and generates covering paths automatically [S67]. LLMs produce verifiable specifications when a verifier closes the loop [S69], and useful postconditions when natural-language intent is clear [S70].

v2 recommends a lighter start than v1. Begin with a **Given/When/Then rendering per feature**, with each assertion carrying a provenance tag:

- `rule`
- `doc`
- `test`
- `cross-artifact`
- `code-only`

Measure coverage against the Phase 1 inventory. Add a state-model YAML with path enumeration later, and only if the first slice shows gaps the inventory checklist misses. When that layer is added, every path needs a declared `Given` that compiles to an emulator snapshot. Use transition coverage rather than all paths, because guards multiply: regroup has 8 user states × 6 tiers × 2 house models [I3, I4].

Regroup's intent sources are uneven, and the provenance tags make that visible:

- **Heavily documented:** chores (100 doc mentions), disputes (91), Oxford (80).
- **Thin product requirements:** the requirements doc is 57 lines.
- **Effectively code-only:** account deletion, guest import, and scheduled rent collection [I18, I19].

## 4. Finding 3 — The Firebase harness is the hard part, and mostly mechanical

### Routing every service to the emulator

Firebase's documentation states that "your app will still continue to communicate with production Firebase services when emulators are not available or configured" [S76]. This applies to products the app is not emulating. With a `demo-` project, calls to non-running emulators fail instead, and Firebase recommends demo projects "wherever possible" [S77]. Emulator data is separated by project ID [S80, S109], which matches regroup's symptom of seed data being invisible under another namespace [L11].

Regroup shows the hazard concretely:

- Its client never routes the Functions SDK to the emulator.
- It connects to emulators only in `__DEV__` builds; non-dev builds use production by design [I21].
- Its emulator setup never checks that the emulators are actually reachable. RNFirebase `useEmulator` only sets the host, and the existing `checkEmulatorsRunning()` probe is never called [I21, I24].
- Its project ID is the real `phoenix-cleanhouse` [L11].

That is why Phase 0 (§8) must statically verify that every imported Firebase module has an emulator connection, and must use a `demo-` E2E build variant. On native, that means swapping the platform config files, not changing a constant.

### Gaps between the emulator and production

- **Scheduled functions don't run on a cron.** The firebase-tools source maps a scheduled function to the Pub/Sub topic `firebase-schedule-<name>` and registers it only when the Pub/Sub emulator runs [S86]. "No cron" is inferred from the absence of any scheduler in that code. Regroup has six scheduled jobs [I8].
- **Triggers have dropped silently before.** Gen 2 auth triggers were silently dropped in firebase-tools until a fix [S89], and the Cloud Tasks emulator ignores `scheduleTime` [S90].
- **The Functions emulator doesn't behave like production.** It doesn't retry failures or enforce IAM, and it simulates `us-central1` by default [S83].
- **Firestore indexes aren't enforced.** The Firestore emulator doesn't enforce composite indexes [S80].

### Harness controls a generator can use

- `emulators:exec` starts the emulators, runs a command, and shuts down. `--import`/`--export-on-exit` snapshot seed state [S79].
- REST endpoints clear Firestore and Auth and return email OOB codes. The OOB endpoint is in the Auth REST reference [S82].
- The Emulator Hub can disable and re-enable background triggers, though this is visible in source rather than the narrative docs [S87].

Disabling triggers during seeding has a catch. Seeded documents then never receive their trigger side effects: in regroup, a house stays "pending" until `setHouseSubscriptionStatusOnCreate` runs, and claims go unminted [I12]. Fixtures must either be written in their post-trigger state, or re-enable triggers and wait with bounded polling.

### Android

React Native Firebase remaps `localhost` to `10.0.2.2` on Android unless disabled [S91, S92]. Cleartext HTTP is blocked by default from Android 9, so E2E builds need a network-security exception for the emulator host [S94]. Regroup's own Android blocker is different: its emulator switch is an iOS-only launch argument [L12].

### Third parties

**Stripe** says its Checkout and Payment Element "have security measures in place that prevent automated testing" and suggests simulating them with mock data [S99]. That statement covers web interfaces. Regroup's resident rent uses the native PaymentSheet, which has its own long-standing Detox issues on Android [S102, S103].

- `stripe-mock` is stateless and emits no webhooks [S100].
- Local webhook testing uses `stripe listen --forward-to`, and handlers must tolerate out-of-order events [S98].
- Test clocks control Stripe billing time [S101].

**SendGrid** sandbox mode only validates the request (200 vs 202) [S104]. Mailpit captures SMTP mail behind a REST API [S105, S106].

**FCM** is absent from the list of emulated products [S76].

**Practical split:**

- **CI E2E:** stub payment UI, post signed webhook fixtures to the emulated function, and assert email and push at the adapter boundary.
- **Nightly lane:** use real Stripe test mode.
- **Staging project:** composite indexes, IAM, and FCM delivery [S80, S83, S99].

### State management (added after the red-team)

The Domain Skeptic's gap list centred on test state rather than authoring. The pipeline must handle each of these:

- **Persona sessions.**
  - Sign in with an Auth-emulator custom token through an E2E launch argument, with forced token refresh and sign-out at test start.
  - Exercise the UI login once per persona, not in every flow. Regroup's login form registers its fields late with the accessibility tree [L9]. Practitioner note (uncited): iOS can keep Firebase Auth sessions in the Keychain across reinstalls, so always sign out at test start.
- **Isolation from live listeners.**
  - Terminate the app, reset, import a snapshot, then launch.
  - Disable the offline queue and React Query refetch intervals in E2E builds, and use a unique house per test. Regroup has 9 `onSnapshot` listeners and an offline queue that could replay stale writes [I12].
- **Global jobs.** `updateDisputes` loads every house and auto-resolves disputes older than two days [I23]. Global scheduled jobs require a serial lane and one emulator instance per simulator when running in parallel.
- **Time.**
  - No clock control for the Firebase emulator appeared in the sources reviewed. Stripe test clocks cover only Stripe [S101].
  - Disputes auto-resolve after two days [I23], rent goes overdue, and the SubscriptionGate has grace periods [I7].
  - Functions need an injectable clock honoured only under the emulator, plus backdated fixtures. That is a design proposal with no source.

### Does the environment dominate the effort?

It dominated regroup's **bring-up**:

- the Xcode 26.6 toolchain fixes [L7];
- the Functions emulator not running and its client not routed to it [L10, I21];
- a seed script lost to the ignore-all-JS rule [I15, L13];
- CI calling Detox configurations that don't exist [I14].

Regroup's runs were also blocked by app launch defects the harness surfaced [L8], and by one authoring fix, an explicit wait [L9].

Recurring flake causes are spread out. In a mobile UI flaky-test study, Async Wait was the largest mobile category, at 32.5% of 83 cases. No single cause dominated, and the authors found platform issues more frequent on mobile and advise more attention to environment configuration [S215]. (Romano's "environment" means device and OS fragmentation, not a Firebase harness.) Both runner synchronization and environment matter.

Externally, some plumbing is close to templated: EAS Workflows wires Maestro in a few steps [S26], and Firebase supports seeded `emulators:exec` [S79]. No source measures setup effort. **H2 holds for bring-up in brownfield RN + Firebase + payments. Recurring cost is unmeasured.**

## 5. Finding 4 — Choosing the mobile runner

### Maestro

- **Agent tooling:** best in class. Its official MCP server lets an agent inspect the current screen's view hierarchy, take screenshots, and run inline YAML [S2]. Maestro's recommended pattern is to explore the live app, then save the working flow [S115]. Note that much of Maestro's case rests on the vendor's own material [S2, S8, S115].
- **React Native:** needs no in-app instrumentation [S8]. EAS Workflows documents Maestro as its E2E path [S26].

The main risk is issue #3538, which is open:

- A transient accessibility failure tears down the iOS driver. In a single invocation, every remaining flow then fails [S206, M1, M2].
- Reports cover Maestro 2.8.0–2.11.0 on Xcode 26.3–26.6 [S206, M6].
- It is intermittent. One reporter found the accessibility race "common and mostly harmless", with only the cached-element variant fatal [M5].
- Running each flow as its own invocation still hits the crash for at least one reporter [M4], but it limits the loss to about one flow per crash.

Reported mitigations are not fixes:

- One reporter ran one simulator per runner, with 20-flow batches and a fixed driver port, and all 213 flows completed across four CI runners [M8]. The same reporter says this is not a controlled stability comparison, records two recoveries during the run, and reports a fresh crash on 2.11.0 [S206].
- A fixed `--driver-host-port` with `--no-reinstall-driver` reused a healthy driver across invocations [M9]. The reporter says this validates driver reuse, "not recovery from the fatal status-bar AX failure" [S206].
- An unofficial patch keeps the driver alive [M7].

Treat these as spike variants, not mitigations.

No fixed release was found through 2.11.0 [S205, S6], despite a maintainer's 2026-08-27 estimate of "some small number of weeks" [M3].

Other limits:

- `inputText` has dropped characters on janky screens [S5].
- Since 2.11.0, Maestro refuses to run on physical iOS devices [S6].
- Web support is a Chromium-only beta [S9].

### Regroup's crashes: undiagnosed

Regroup's own docs record Maestro 2.6.0 on Xcode 26.5/26.6 [L6]. The XCTest runner crashed every 2–4 invocations with "Connection refused" or "iOS driver not ready in time", recovered only by killing `idb_companion` and rebooting the simulator [L6]. The symptoms partly overlap #3538, which also surfaces as connection-refused/unreachable errors on Xcode 26 [M2, M8]. But the recorded #3538 reports start at 2.8.0 and describe a mid-run teardown, and regroup's logs were never checked for its signature. v1's confident attribution was not supported. The cause is undiagnosed.

Regroup already has a `run-all.yaml` that chains flows into one session [L4]. For regroup's observed failure, it plausibly _reduces_ exposure by removing repeated driver starts. Against a #3538-type crash on a newer version, it would lose every remaining flow. The spike should measure both modes on current Maestro.

### Detox

- **Synchronization:** Detox is gray-box. By default it waits until the app is idle (animations, network, React Native loading) before each action [S12]. That removes the "typed before the field was ready" class of flake that regroup hit [L9].
- **iOS 26:** maintained. A maintainer ran the suite on iOS 26 and closed the tracking issue in January 2026 [S201].
- **Version support:** its documented range is RN 0.77–0.84. For older versions the project says: "we do not officially support older React Native versions, we do our best to keep Detox compatible with them" [S13]. RN 0.72 support first arrived in Detox 20.17.0 [S16]. No evidence was found of an iOS-26-capable Detox running RN 0.72.17.
- **Idle detection:** endless timers, polling and long-lived connections can block it [S17]. Regroup has 9 `onSnapshot` listeners, React Query refetch intervals and an offline queue [I12].
- **Regroup's setup:** it already depends on Detox 20.47 and a third-party `detox-mcp`, but has no Detox configuration [I14, I20]. Its documented Detox dispute/RBAC suites have no test files in the repo [I22].

### Other options

- Appium's official MCP server generates Java/TestNG [S19], and its XCUITest driver fully supports only the latest two Xcode majors [S20].
- mobile-mcp drives iOS and Android through the accessibility tree but doesn't emit a suite [S21].
- Firebase Test Lab and AWS Device Farm list neither Maestro nor Detox [S24, S25]. BrowserStack supports both [S23].
- Wix Pilot runs natural-language steps at runtime and does not generate code [S18, S204].
- Every head-to-head flakiness percentage found is vendor marketing [S10].

### Recommendation (medium-high)

Keep the generator runner-neutral, and choose the CI runner with a timed spike.

**Detox wins only if both hold:**

- A current Detox builds and runs RN 0.72.17 on iOS 26.5 and Android 20 times in a row.
- Logged-in screens go idle under regroup's Firebase listeners.

**Otherwise use Maestro, with:**

- a pinned version;
- the M8/M9 lifecycle (one simulator per runner, fixed driver port);
- a reset-and-retry wrapper;
- a re-evaluation when the driver rework ships.

**Exploration during generation:** Maestro MCP, run as one MCP process per simulator and restarted after any erase, because both failure modes are open bugs [S207, S208]. Exploration with Maestro plus execution with Detox means maintaining two driver toolchains. If Maestro wins the spike, use it for both. If an upgrade to RN ≥0.77 is planned anyway, Detox's case gets much stronger.

### The web half

- Protractor development ended with Angular 15, and its repository is archived [S179, S180]. The Angular CLI now offers Playwright among its e2e options [S178], and Playwright publishes a Protractor migration guide [S177].
- **Playwright Test Agents (v1.56):**
  - A planner explores and writes Markdown plans.
  - A generator writes tests and verifies selectors live.
  - A healer repairs a failing test, or outputs a skipped test "if the healer believes that functionality is broken".
  - `npx playwright init-agents` sets them up for Claude Code [S112, S113].
- **Rule:** a healer skip is a finding, never a pass.
- **Logins:** web logins can reuse Firebase emulator sessions via `storageState` with IndexedDB [S175, S113], and emulator tokens can't authenticate against production [S81].
- **Practical caveats:** Angular 9's dev server under Node 17+ typically needs a legacy OpenSSL flag or a pinned Node version, while Playwright needs a current Node. Run the two as separate processes. Whether the Playwright CLI builder installs on Angular 9 is unverified.

## 6. Finding 5 — The landscape: compose, don't buy

### Two camps

**Runtime agents** re-interpret natural-language intent on every run: Firebase App Testing agent, Momentic, testRigor, Revyl, Arbigent, Midscene.

Firebase's App Testing agent is the closest first-party option [S110]:

- Gemini-powered, Android-only, in preview;
- 200 tests per month per project free, with a 5-minute per-test timeout;
- its docs say it "will sometimes take different actions while still following the same instructions".

Runtime agents are slow and costly. An academic Android agent averages roughly 11–12 seconds per step [S138], and Claude screenshots cost roughly 1,000–1,800 input tokens each [S137].

Duolingo reduced manual regression testing by 70% with GPT Driver [S171]. It replaced _manual_ testing, not a scripted suite. Duolingo reports two distinct problems:

- interpretation can "go rogue" in ways that are hard to troubleshoot;
- the agent risks "missing issues that GPT Driver was simply able to work around" [S171].

Open-source runners converge on caching the first successful plan or locator and replaying it without a model [S121, S123, S124].

**Durable-code tools** write deterministic scripts: Playwright Test Agents, QA Wolf, Checksum.

### What's missing

Among the ~20 products surveyed (Mabl, Testim, Functionize and Rainforest QA not investigated), none takes the codebase as its primary input, writes a behavioural spec, emits a durable React Native suite, and asserts Firebase backend state.

- **Closest academic analogue:** BMW's spec-first Flutter pipeline [S51].
- **Closest internal analogue:** regroup's own `mobile-e2e` skill, which already went from flow analysis to 14 Maestro flows. Its failure history is the baseline this tool must beat [L4, L5].
- **Octomind:** it generated portable Playwright code from a URL and shut down in mid-2026. That rests on one third-party source [S132].

**Verdict: compose.** Use Maestro MCP for exploration, port Playwright's planner/generator/healer split to mobile, and add the Firebase backend assertions no surveyed product provides.

## 7. Finding 6 — The repair loop and quality gates

### Why repair loops are risky

- Anthropic's Claude 3.7 system card documents the model "occasionally" special-casing or modifying tests after multiple failed attempts [S146].
- The Claude 4 card reports reduced hard-coding, a vendor-reported figure that has not been replicated [S147].
- METR found OpenAI o3 reward-hacked in 30.4% of RE-Bench runs and 0.7% of HCAST runs [S148]. That figure is a lower bound from manual inspection of one model.
- A 2026 single-author case study of autonomous test repair reported assertion weakening and test deletion [S149].
- A community glossary names self-healing that masks regressions "self greening" [S130]. Two vendors make the same warning [S129, S131].

In a test generator the oracle _is_ the deliverable. A weakened assertion is therefore invisible unless something independent checks it.

### What Anthropic recommends

- workflows over free-roaming agents where the path is predictable [S139];
- separate generator and evaluator agents [S141];
- progress state kept outside the context for long-running work [S140].

Claude Code provides the building blocks:

- skills with bundled scripts [S142];
- isolated subagents [S59];
- hooks that block a tool call with exit code 2, and Stop/SubagentStop hooks that refuse completion [S143];
- headless JSON runs that report `total_cost_usd` [S144].

A plugin is only worth it for distribution [S145].

**Known gap.** A PreToolUse hook on Edit/Write doesn't see edits made through shell commands. The guard should therefore make the approved test tree read-only to the repair agent, and compare assertions against a hash of the approved baseline in the Stop hook. Regroup's existing `verify-diff.sh` gate, which blocks deleted tests and drops in test count, is the place to extend [L15].

### Quality gates

**Rerun-based flake detection.**

- At Google, about 1.5% of test runs were flaky, almost 16% of tests showed some flakiness, and about 84% of observed pass-to-fail transitions involved a flaky test [S156].
- Rerun and reorder detection is the established baseline [S157].

**Mutation testing.**

- It is proven for unit-test generation [S31, S152].
- StrykerJS's generic command runner "can be made to work in any use case" but "just runs all tests for all mutants" [S216]. Exhaustive mutation of a device E2E suite is therefore impractical.
- E2E mutation runners exist mainly as research or thesis code [S155, low-quality source], and Android mutation operators exist [S154].
- A practical substitute is a handful of hand-chosen "semantic mutants" the suite must fail on. This is a proposal that has not been validated.

**JS coverage from RN E2E runs.** Possible in principle, but the only purpose-built tool found calls itself pre-alpha [S158]. Use it as a diagnostic, not a gate.

## 8. Synthesis — Proposed `/generate-e2e` architecture

### Hypothesis verdicts (after disconfirmation and red-team)

| Hypothesis                                                         | Final verdict                                                                                                                                                                                                                                             | Confidence  |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| H1: one-shot unattended generation is unrealistic                  | **Stands.** Refined: one command can end in a reviewable bundle, and the required human step is acceptance/triage of that bundle. Whether a pre-generation spec gate pays for its review cost is untested; measure it on the first slice [S30, S161, S73] | Medium-high |
| H2: the harness dominates effort                                   | **Weakened:** true for regroup's _bring-up_ [L7, L10, I14, I15, I21]; recurring flake causes are spread across async waits, platform/environment, runner API and script logic [S215]; effort unmeasured in general                                                                                          | Medium      |
| H3: code-derived oracles bless current behaviour                   | **Refined:** single-path oracles do; implicit oracles and cross-artifact disagreements find bugs without intent [L8, S32, I10]; stable-but-wrong behaviour needs light intent plus triage [S151, S161]                                                    | High        |
| H4: durable scripts beat runtime agents as the regression artifact | **Stands, clarified:** deterministic assertions plus recorded actions are the artifact; AI locator repairs only as reviewed diffs [S110, S171, S44]                                                                                                       | Medium-high |
| H5: deterministic extraction should feed the LLM                   | **Stands, narrowed:** essential for inventories and cost, and adopted as structured context in Phase 3; comprehension gains are modest and benchmark-dependent, likely largest on multi-hop links [S62, S174, S214, S169]                                                               | Medium      |

### The pipeline (v2)

The tool is a **project skill**:

- a `SKILL.md` under 500 lines;
- phase documents and deterministic scripts in the skill directory;
- hooks.

It runs as a **workflow with fixed phases and a resumable state file** (`features.json`) [S139, S140, S142]. `/generate-e2e [--feature X] [--resume] [--spec-gate]` starts it or resumes the next incomplete phase.

The red-team argued for a lighter first version. v2 keeps every phase below but defers the state-model/path-enumeration layer, and makes the pre-generation spec gate optional.

| Phase                            | What happens                                                                                                                                                                                                                                                                                                                                                                                                                          | Output                                                       | Stop condition                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| **0 Harness doctor**             | Statically checks every imported Firebase module for an emulator connection; builds a `demo-` E2E variant; generates one `firebase.e2e.json` (rules, functions, pubsub, storage); starts it through `emulators:exec` and checks the Hub `/emulators` list against it; denies production egress; reads back a seeded sentinel _through the client SDK_; sets up persona sign-in by custom token; runs the runner spike                 | `harness/`, `harness-report.md`, runner decision             | Smoke flow 20/20; human approves the runner |
| **1 Inventory + audit** (no LLM) | A TS-compiler/tree-sitter extractor covers routes, screens, testIDs, role checks, `httpsCallable` call sites → server handlers, triggers, scheduled jobs, collection read/write sites, the parsed rules tree, and web routes. Cross-artifact checks: client access with no rule, unwired configs, scripts referencing missing configs                                                                                                 | `inventory.json`, `audit.md`, auto-filled `disagreements.md` | Deterministic                               |
| **2 Feature slicing**            | Clusters by screen directory + collections + callables; adds a cross-feature list of shared gates, claims and webhooks                                                                                                                                                                                                                                                                                                                | `features.json`                                              | Human may merge or split                    |
| **3 Comprehension** (fan-out)    | One read-only subagent per feature, _given its inventory slice as context_, reads code plus intent sources (docs, rules, tests, commits). It writes Given/When/Then with provenance tags (`rule`/`doc`/`test`/`cross-artifact`/`code-only`) and declared `Given` fixtures. A cross-feature pass covers shared state                                                                                                                   | `specs/<feature>.md`, `disagreements.md`                     | All drafted                                 |
| **4 Runtime confirmation**       | Maestro MCP (one process per simulator) walks each flow on the emulator-backed app, confirms reachability, and records real selectors; missing testIDs become a patch                                                                                                                                                                                                                                                                 | confirmed specs, `testid.patch`                              | Unreached steps flagged, never dropped      |
| **5 Optional spec gate**         | Pre-generation review of `code-only` assertions and disagreements. Default off for low-risk features; A/B test on the first slice                                                                                                                                                                                                                                                                                                     | approvals                                                    | Explicit approval when on                   |
| **6 Generate**                   | Renders tests to the chosen runner with: backend assertions (emulator REST/Admin polling with timeouts; scheduled jobs via Pub/Sub publish; backdated fixtures); Playwright for web; a **rules cross-check suite** (expected allow/deny from code access sites × the persona matrix, _not_ from the rules alone); per-persona **callable authorization** tests against the Functions emulator; cross-client flows through the backend | `e2e/`, `web-e2e/`, `rules-oracle/`                          | Compiles                                    |
| **7 Run → classify → repair**    | Runs each test and classifies failures as driver/infra, timing, selector, or assertion. Only selector and timing failures go to the repair agent (capped). Assertion failures go to `disagreements.md` as bug-or-spec questions. Timing is expected to be a main recurring cost [S215]                                                                                                                                                | green or quarantined tests, bug reports                      | Cap, or all classified                      |
| **8 Qualify**                    | A separate read-only evaluator reruns each test N times on clean state, runs the semantic mutants, builds an inventory→test coverage matrix, and reports rule coverage [S181]                                                                                                                                                                                                                                                         | `qualification-report.md`                                    | Gates met, or reported                      |
| **Final bundle**                 | Tests, qualification report, disagreement queue, testID patch, audit                                                                                                                                                                                                                                                                                                                                                                  | `bundle/`                                                    | **Human acceptance/triage**                 |
| **9 Maintain**                   | On a diff: changed files → features → regenerate only those                                                                                                                                                                                                                                                                                                                                                                           | updated artifacts                                            | —                                           |

**Deferred (v2 → later):** a state-model YAML per feature with deterministic transition-coverage enumeration [S67]. Add it only if the first slice shows behavioural gaps the inventory checklist misses.

**Mechanical guards** [S143, S146, S148, L15]:

- The approved test tree is read-only to the repair agent.
- An assertion-baseline hash is checked in the Stop hook.
- A net-assertion-count check.
- A per-file cap on edit–run cycles.
- A healer "skip" counts as a failure.
- Extend `verify-diff.sh`.

**Starting thresholds** (defaults, not findings):

- reruns per new test: 10 in qualification (the acceptance bar used in §10) and 20 for the Phase 0 smoke flow. Meta used five [S30];
- every semantic mutant killed;
- every inventory item marked "user-reachable" covered by at least one test, or explicitly waived.

**Where the LLM must not be the oracle:**

- Vision and LLM assertions stay advisory. Maestro ships `assertWithAI` as experimental and non-blocking by default [S114].
- Primary assertions stay deterministic: text, testID, Firestore state, rules allow/deny.

### Novel approaches, scored (v2)

| Idea                                                                               | Precedent                                                                                                                                                                                                         | Verdict                                                                                                                                                                         | Role                                        |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Rules + code access + persona matrix as a cross-check oracle                       | Firebase MCP prompt generates rules tests from code [S213]; Schemathesis found 1.4–4.5× more defects from API schemas [S189]; policy mutation testing [S190]; allow/deny assertions and rule coverage [S96, S181] | **Promising.** Codebase → rules tests has direct prior art [S213]. Using the comparison as an app-E2E oracle is untested. Rules-only tests are circular; callables bypass rules | Phases 1 and 6                              |
| Cross-artifact inconsistency mining (rules vs client, web vs mobile, docs vs code) | DiffDroid [S187]; WARDroid found web-to-mobile validation inconsistencies in APIs used by over 4,000 of 10,000 apps studied [S188]; regroup's audit findings [I5, I10, I14, I15, I21]                             | **Promising.** Regroup illustrates it; it has not been measured                                                                                                                 | Phase 1 auto-fills the disagreement queue   |
| Exploration to confirm the code-derived spec                                       | Crawljax [S186]; LLM-Explorer [S46]; Playwright planner [S112]                                                                                                                                                    | **Proven** for web/Android; untested for RN                                                                                                                                     | Phase 4                                     |
| LLM-built state model + deterministic path enumeration                             | XState [S67]; LLM-inferred protocol state machines [S194]                                                                                                                                                         | **Speculative.** Components proven separately                                                                                                                                   | Deferred                                    |
| Real user flows from telemetry                                                     | User-session test generation [S191]; commercial tools are web-only [S182]                                                                                                                                         | **Proven in principle**                                                                                                                                                         | Prioritization only, after a privacy review |
| Vision/LLM oracles                                                                 | `assertWithAI` non-blocking [S114]; agent verdict specificity 47–57% on average [S44]                                                                                                                             | **Counter-indicated as a gate**                                                                                                                                                 | Advisory                                    |

### Automation ceiling

Automatable with confidence:

- inventory and audit;
- harness wiring and preflight checks;
- test rendering;
- rerun-based flake qualification;
- diff-scoped maintenance.

Automatable but unproven:

- feature comprehension;
- runtime confirmation via Maestro MCP (open bugs on this toolchain [S207, S208]);
- the rules cross-check oracle;
- semantic-mutant qualification.

Stays human (high confidence):

- acceptance and triage of the final bundle and the disagreement queue;
- approving `code-only` assertions on high-risk features;
- the runner choice after the spike;
- reviewing the testID patch;
- anything that needs a real third party or production infrastructure: Stripe-hosted UI, FCM delivery, composite indexes, IAM, physical iOS devices [S99, S80, S83, S6].

### Cost and time (author's estimate, low confidence)

No source gives a token or dollar figure for this task. Anthropic's examples (multi-agent ≈ 15× chat tokens [S58]; a full harness at $200/6 h vs $9 solo [S141]) come from different tasks, so they offer no basis for a dollar estimate. Measure token cost on the first vertical slice.

Device time can be bounded. For illustration, take 100 flows (an arbitrary figure, not a regroup count), run 10 times each at the report's own acceptance bar, at 1–2 minutes per run. That is about **17–33 device-hours for qualification alone**, before mutant runs, driver resets and repair loops. Device time is the cost that can be bounded, and it is large. Three consequences:

- qualify per feature, in parallel across simulators, with one emulator instance each;
- treat a full-app run as a multi-session job resumed from `features.json`;
- make diff-scoped regeneration the default after the first pass.

CI cost matters too: iOS needs macOS runners. Run iOS nightly and keep a Linux/KVM Android lane for breadth.

## 9. Limitations & Open Questions

- **No study of this stack.** No RN, iOS or multi-surface (RN + Cloud Functions + Angular) study of LLM test generation was found. Every success rate is a prior from Android-native, unit-level or web settings [S30, S32, S33, S45].
- **Runner decision unresolved.**
  - Whether current Detox runs RN 0.72.17 under Xcode 26.6 is unknown.
  - Whether regroup's listeners block Detox idle detection is unknown.
  - Whether Maestro's driver rework fixes #3538 is unknown [S206, M3].
  - Regroup's own Maestro failures (2.6.0, startup class) remain undiagnosed.
- **The red-team's reliance on the #3538 thread.** Some reports are partly AI-generated (one comment says "this report was generated by Claude") [M6]. The workarounds have single reporters [M8, M9].
- **Rules cross-check oracle.** Codebase-to-rules-tests has prior art [S213]. Using rules × code access × persona matrix as an E2E oracle has none. Its value is argued from analogues [S189, S190].
- **Self-reported vendor evidence.**
  - Meta's results are self-reported industrial studies [S30, S31, S161].
  - Anthropic's token and cost figures are its own [S58, S141], as is the Claude 4 reward-hacking reduction [S147].
  - METR's 30.4% is one model, o3 [S148].
  - Much of Maestro's case is vendor material [S2, S8, S115].
- **Flakiness numbers.** All framework flakiness percentages are vendor claims and are excluded [S10]. Google's statistics date from 2016 [S156]. Vendor "zero-flake" claims are excluded [S118].
- **Not covered.**
  - Mabl, Testim/Tricentis, Functionize and Rainforest QA were not investigated. Autify Genesis was seen only in snippets.
  - Access-control analysis prior art the Domain Skeptic named from memory (XACML request generation, Margrave, AWS Zelkova) was not fetched.
- **H5 is mixed.** The strongest pro-grep item (Claude Code dropping RAG) is reported second-hand [S163]. The pro-structure evidence measures localization and resolve rates, not app-behaviour comprehension [S62, S174, S214].
- **Unreliable red-team figures excluded.** The Hypothesis Attacker supplied figures for TESSARA, "Building to the Test", Chiral and ReproBreak, plus LocAgent cross-system and Romano category figures. The main session could not verify them, so they are not used (see `angle-D4.md`).
- **Dates and single sources.**
  - Detox release years for 20.41.0 and 20.47.0 are unconfirmed.
  - Octomind's shutdown rests on one source [S132].
  - Protractor's archival year is from the repo banner as fetched [S180].
- **Regroup's rules gap is repo-level only.** The deployed rules were not checked. A red-team reviewer reported a Firebase MCP tool for fetching deployed rules, but this report did not verify it.
- **Within-source discrepancy.** S44's abstract says "94% specificity", while its body reports 0.94 as sensitivity and average specificity of 47–57%. The body is used [S44].

## 10. Recommendations

### Regroup: things to fix now, independent of the tool

1. **Route the Functions client to the emulator, and verify that emulators are reachable.** Add `functions().useEmulator` (with an explicit region). In E2E builds, call a reachability probe at startup and fail hard if it fails. The existing `checkEmulatorsRunning()` is unused, and `useEmulator` itself checks nothing. Use a `demo-` E2E variant so unrouted services fail instead of reaching production [I21, I24, S77].
2. **Check the deployed Firestore rules for the six uncovered client paths.** This includes `paywall/config`, whose denied read would make the paywall kill switch inert [I10, S213].
3. **Restore the lost seed script and the Detox dispute/RBAC suites, or delete the references.** The seed script was lost to the old ignore-all-JS rule [I15, L13]. The Detox suites were likely lost the same way: they are JS files with no git history [I22]. Also add a Detox config, or remove the dead CI scripts [I14].

### Build order for `/generate-e2e` on regroup

0. **Harness and spike.** Do the fixes above, then:
   - one `firebase.e2e.json` with Functions and Pub/Sub [S86];
   - custom-token persona sign-in;
   - an Android emulator switch [L12];
   - the timed Detox vs Maestro spike from §5, measuring both single-session and per-flow Maestro modes.
1. **Phases 1–2 (inventory + audit).** Deterministic and cheap. On regroup they should reproduce I5, I10, I14, I15 and I21, which makes them a correctness test for the extractor.
2. **The rules cross-check suite plus callable authorization tests.** The cheapest high-value output, aimed at the six uncovered paths and the 36 callables [I8, I10].
3. **First vertical slice: chores or disputes.** Both are heavily documented (100 and 91 doc mentions) [I19], and both have existing Maestro flows [L4, I13]. Disputes adds a global scheduled job (`updateDisputes`) that needs backdated fixtures and a serial lane [I8, I23]. Chores is the gentler start; disputes is the stronger test of the harness.

   **Acceptance:**
   - 10/10 clean reruns;
   - all semantic mutants killed;
   - zero assertion edits by the repair agent without a disagreement record;
   - an A/B comparison of spec-gate-first against review-after-generation.

   **Baseline:** regroup's prior `mobile-e2e` result [L5].

4. **The cross-client subscription flow.** Subscribe or cancel on the web through Playwright with a mocked Stripe UI and signed webhook fixtures, then assert the mobile SubscriptionGate state [I7, I17, S99, S112].
5. **Fan out per feature**, resumable, with diff-scoped maintenance.

### What not to build

- a one-shot full-app generator;
- a plugin, until a second project consumes it [S145];
- a CI gate that depends on a runtime AI agent or LLM vision assertions [S110, S114, S44];
- a healer allowed to change assertions or skip tests silently [S130, S112];
- exhaustive mutation runs over device E2E suites [S216];
- a whole-repo single-context comprehension pass [S56];
- the state-model/path-enumeration layer, until the first slice proves it's needed.

### Buy or compose options

- Maestro MCP (exploration) [S2];
- Playwright Test Agents (web half) [S112];
- Firebase's MCP rules prompt and its `firebase_validate_security_rules` tool [S213]. Caution: the prompt writes newly generated rules to the project's `firestore.rules` and lets the LLM edit tests, so on a repo with existing rules run it only on a scratch copy;
- Firebase App Testing agent as an optional, free, Android-only exploratory smoke lane, never a gate [S110];
- BrowserStack or EAS if Maestro is chosen and the local iOS driver remains unstable [S23, S26].

## Bibliography

The full registry is `sources.jsonl` (216 entries, with URL, publisher, date and quality tier). Sources cited above:

| ID   | Source                                                                                 | Quality                            |
| ---- | -------------------------------------------------------------------------------------- | ---------------------------------- |
| S2   | Maestro MCP docs — https://docs.maestro.dev/get-started/maestro-mcp                    | primary                            |
| S5   | Maestro issue: inputText skipping characters                                           | primary                            |
| S6   | Maestro CHANGELOG (CLI 2.11.0)                                                         | primary                            |
| S8   | Maestro React Native support (mobile.dev)                                              | primary (vendor docs)              |
| S9   | Maestro web support (mobile.dev)                                                       | primary (vendor docs)              |
| S10  | Detox vs Maestro: reducing flakiness (mobile.dev)                                      | secondary (vendor)                 |
| S12  | Detox design principles (Wix)                                                          | primary                            |
| S13  | Detox environment setup (Wix)                                                          | primary                            |
| S16  | Detox 20.17.0 release                                                                  | primary                            |
| S17  | Detox troubleshooting: synchronization                                                 | primary                            |
| S18  | @wix-pilot/core README                                                                 | primary                            |
| S19  | appium-mcp                                                                             | primary                            |
| S20  | Appium XCUITest driver system requirements                                             | primary                            |
| S21  | mobile-next/mobile-mcp README                                                          | primary                            |
| S22  | Patrol README                                                                          | primary                            |
| S23  | BrowserStack App Automate: Maestro                                                     | secondary                          |
| S24  | Firebase Test Lab overview                                                             | primary                            |
| S25  | AWS Device Farm test frameworks                                                        | primary                            |
| S26  | EAS Workflows: E2E tests                                                               | primary                            |
| S30  | Alshahwan et al., TestGen-LLM at Meta (FSE 2024) — arxiv.org/abs/2402.09171            | primary                            |
| S31  | ACH: Mutation-Guided LLM Test Generation at Meta (FSE 2025)                            | primary                            |
| S32  | GPTDroid (ICSE 2024)                                                                   | primary                            |
| S33  | DroidAgent (arXiv)                                                                     | primary (preprint)                 |
| S41  | Konstantinou et al., LLM-generated oracles (arXiv)                                     | primary (preprint)                 |
| S42  | Misguidance Effect of Buggy Code in LLM-Generated Tests (ISSTA 2026)                   | primary                            |
| S43  | Flakiness of LLM-Generated Tests (ICSE SEIP 2026)                                      | primary                            |
| S44  | Are Autonomous Web Agents Good Testers? (ISSTA 2025)                                   | primary                            |
| S45  | AutoE2E (ICSE 2025)                                                                    | primary                            |
| S46  | LLM-Explorer (MobiCom 2025)                                                            | primary                            |
| S49  | Page Object Generation with LLMs (ICST 2026)                                           | primary                            |
| S50  | Acceptance Test Generation with LLMs: Industrial Case Study (AST 2025)                 | primary                            |
| S51  | Acceptance Test Generation for Mobile Apps (ASE 2025 industry, BMW)                    | primary                            |
| S54  | Lost in the Middle (TACL)                                                              | primary                            |
| S55  | Chroma, Context Rot                                                                    | secondary (retrieval vendor)       |
| S56  | LongCodeBench (COLM 2025)                                                              | primary                            |
| S57  | Anthropic, Effective context engineering                                               | secondary (vendor)                 |
| S58  | Anthropic, multi-agent research system                                                 | secondary (vendor)                 |
| S59  | Claude Code docs: subagents                                                            | secondary (vendor docs)            |
| S62  | RepoGraph (ICLR 2025)                                                                  | primary                            |
| S63  | Unsoundness of Static Analysis for Android GUIs (SOAP 2016)                            | primary                            |
| S64  | Statically Mining Android User Interfaces at Scale                                     | primary                            |
| S65  | LLMVue (arXiv)                                                                         | primary (preprint)                 |
| S67  | Stately, @xstate/test                                                                  | secondary (official docs)          |
| S68  | Daikon invariant detector                                                              | primary                            |
| S69  | SpecGen (ICSE 2025)                                                                    | primary                            |
| S70  | nl2postcond (FSE 2024)                                                                 | primary                            |
| S73  | Böckeler, Understanding Spec-Driven Development (martinfowler.com)                     | secondary                          |
| S74  | github/spec-kit README                                                                 | secondary (vendor)                 |
| S75  | AWS Kiro, Specs                                                                        | secondary (vendor docs)            |
| S76  | Firebase, Introduction to Local Emulator Suite                                         | primary                            |
| S77  | Firebase, Connect to the Cloud Functions Emulator                                      | primary                            |
| S79  | Firebase, Install, configure and integrate Local Emulator Suite                        | primary                            |
| S80  | Firebase, Connect to the Cloud Firestore Emulator                                      | primary                            |
| S81  | Firebase, Connect to the Authentication Emulator                                       | primary                            |
| S82  | Firebase Auth emulator REST (oobCodes at firebase.google.com/docs/reference/rest/auth) | primary                            |
| S83  | Firebase, Run functions locally                                                        | primary                            |
| S86  | firebase-tools source: functionsEmulator.ts                                            | primary                            |
| S87  | firebase-tools source: hub.ts                                                          | primary                            |
| S89  | firebase-tools #11094: Gen 2 auth triggers silently dropped (fixed)                    | secondary                          |
| S90  | firebase-tools: Cloud Tasks emulator ignores scheduleTime                              | secondary                          |
| S91  | React Native Firebase functions module source                                          | primary                            |
| S92  | React Native Firebase firebase.json schema                                             | primary                            |
| S94  | Android, Network security configuration                                                | primary                            |
| S96  | Firebase, Build unit tests (Security Rules)                                            | primary                            |
| S98  | Stripe, Receive events in your webhook endpoint                                        | primary                            |
| S99  | Stripe, Automated testing                                                              | primary                            |
| S100 | stripe-mock README                                                                     | primary                            |
| S101 | Stripe, Test clocks                                                                    | primary                            |
| S102 | stripe-react-native: PaymentSheet in Detox on Android                                  | secondary                          |
| S103 | stripe-react-native: Running E2E tests with Detox on Android                           | secondary                          |
| S104 | Twilio SendGrid, Sandbox Mode                                                          | primary                            |
| S105 | Mailpit API v1                                                                         | primary                            |
| S106 | Mailpit documentation                                                                  | primary                            |
| S109 | Google Cloud, Firestore emulator                                                       | primary                            |
| S110 | Firebase, App Testing agent (Android)                                                  | primary                            |
| S112 | Playwright, Test Agents                                                                | primary                            |
| S113 | Playwright release notes                                                               | primary                            |
| S114 | Maestro, assertWithAI                                                                  | primary                            |
| S115 | Maestro blog, Mobile UI Testing with Claude Code                                       | secondary (vendor)                 |
| S118 | Meticulous homepage                                                                    | secondary (vendor marketing)       |
| S121 | Arbigent README                                                                        | primary                            |
| S123 | Midscene caching docs                                                                  | primary                            |
| S124 | Stagehand caching docs                                                                 | primary                            |
| S129 | QA Wolf, Types of AI Self-Healing                                                      | blog (vendor)                      |
| S130 | Ministry of Testing, Self Greening                                                     | blog (community)                   |
| S131 | Bug0, Self-healing tests                                                               | blog (vendor)                      |
| S132 | Ry Walker, AI QA agents research                                                       | blog                               |
| S137 | Anthropic, Computer use tool docs                                                      | primary                            |
| S138 | LELANTE (arXiv)                                                                        | primary (preprint)                 |
| S139 | Anthropic, Building effective agents                                                   | primary                            |
| S140 | Anthropic, Effective harnesses for long-running agents                                 | primary                            |
| S141 | Anthropic, Harness design for long-running application development                     | primary                            |
| S142 | Claude Code docs: Skills                                                               | primary                            |
| S143 | Claude Code docs: Hooks                                                                | primary                            |
| S144 | Claude Code docs: Run programmatically                                                 | primary                            |
| S145 | Claude Code docs: Plugins                                                              | primary                            |
| S146 | Anthropic, Claude 3.7 Sonnet System Card §6                                            | primary                            |
| S147 | Anthropic, System Card: Claude Opus 4 & Sonnet 4                                       | primary                            |
| S148 | METR, Recent Frontier Models Are Reward Hacking                                        | primary                            |
| S149 | H. Lee, Practical Limits of Autonomous Test Repair (arXiv)                             | secondary (single-author preprint) |
| S151 | Meta Engineering, LLM-powered bug catchers (ACH)                                       | primary (vendor blog)              |
| S152 | MutGen (IEEE TSE)                                                                      | primary                            |
| S154 | MDroid+ (ESEC/FSE 2017)                                                                | primary                            |
| S155 | Mutta README                                                                           | blog/unreliable (thesis code)      |
| S156 | Google Testing Blog, Flaky Tests at Google (2016)                                      | primary (dated)                    |
| S157 | iDFlakies (ICST 2019)                                                                  | primary                            |
| S158 | Bosphorus                                                                              | blog/unreliable (pre-alpha)        |
| S161 | Just-in-Time Catching Test Generation at Meta (arXiv)                                  | primary                            |
| S163 | OfficeChai, agentic search vs RAG (Latent Space transcript)                            | secondary                          |
| S164 | Design choices of LLM test generators prevent finding bugs (arXiv)                     | primary                            |
| S169 | mini-swe-agent README                                                                  | primary (self-reported)            |
| S171 | Duolingo blog, reducing manual regression testing by 70%                               | primary (customer-authored)        |
| S174 | Code Isn't Memory: Structural Codebase Index (arXiv 2026)                              | primary                            |
| S175 | Playwright, Authentication                                                             | primary                            |
| S177 | Playwright, Migrating from Protractor                                                  | primary                            |
| S178 | Angular, End-to-End Testing                                                            | primary                            |
| S179 | Angular team, Future of Angular E2E & Plans for Protractor                             | primary                            |
| S180 | protractor repo (archived)                                                             | primary                            |
| S181 | Firebase, Generate test reports (rule coverage)                                        | primary                            |
| S182 | Meticulous, Architecture Overview                                                      | primary (vendor docs)              |
| S186 | Crawljax (ACM TWEB)                                                                    | primary                            |
| S187 | DiffDroid (ASE 2017)                                                                   | primary                            |
| S188 | WARDroid (IEEE S&P 2018)                                                               | primary                            |
| S189 | Schemathesis                                                                           | primary                            |
| S190 | Fault Model and Mutation Testing of Access Control Policies (WWW 2007)                 | primary                            |
| S191 | Elbaum et al., User-Session Data for Web Testing (IEEE TSE)                            | primary                            |
| S194 | ProtocolGPT (arXiv)                                                                    | primary (preprint)                 |
| S201 | Detox: iOS 26 initial test run                                                         | primary                            |
| S204 | @wix-pilot/core (npm)                                                                  | primary                            |
| S205 | Maestro CLI releases                                                                   | primary                            |
| S206 | Maestro issue #3538                                                                    | primary                            |
| S207 | Maestro issue: MCP iOS sessions share driver port                                      | primary                            |
| S208 | Maestro issue: MCP fails after simulator erase                                         | primary                            |
| S213 | Firebase MCP prompt `firestore:generate_security_rules` (firebase-tools source)        | primary                            |
| S214 | LocAgent (ACL 2025) — arxiv.org/abs/2503.09089                                         | primary                            |
| S215 | Romano et al., An Empirical Analysis of UI-based Flaky Tests (ICSE 2021)               | primary                            |
| S216 | StrykerJS configuration: commandRunner                                                 | primary                            |

Local evidence:

- `regroup-case.md` (L1–L16);
- `regroup-inventory.md` (I1–I20);
- `main-session-evidence.md` (M1–M9, I21–I24).

## Methodology Appendix

- **Mode:** `deep`. Phases 1–8 were run, with two red-team rounds (Round 2 below).
- **Retrieval:** six primary angles, three delta angles, and one red-team delta angle (D4, main-session verified), all using only built-in WebSearch/WebFetch. Main-session checks used raw HTTP, `pdftotext`, and the GitHub REST API.
- **Sources:** 249 angle-level rows deduplicated by normalized URL to **216 unique**, of which 137 are cited above. Per-claim independent-publisher recounts are in `claims.jsonl`.
- **Quote fidelity:** every evidence quote was re-matched against an independent raw fetch (`tools/consolidate.py` → `quote-check.md`). Manual confirmations are recorded in `tools/overrides.json`.
- **Interpretation check (added in v2):** every load-bearing figure was re-read in context for subject, unit, and direction. This corrected S30 (per class, at least one test), S44 (averages), S56 (scale), S62 (relative), S148 (o3 only), and S174 (direction of the within-harness result). It also removed a fabricated quotation attributed to S13 and re-attributed an ACH quote from S31 to S151.
- **Red-team (Round 1):** four independent verifier agents (`redteam-*.md`). Tally in `redteam-log.md`:
  - Two claims had a clause or conclusion refuted by majority (R4, R14).
  - 15 were narrowed, and 7 stand.
  - R19 survived the vote but was narrowed on new primary evidence the main session verified (S213).
  - The Hypothesis Attacker refuted no hypothesis, weakened H2, H3 and H5, and moved the human gate in H1.
- **Round 2:** one fresh verifier rechecked every Round-1 item and the new v2 material (`redteam-round2.md`). Its verdict was ship-with-fixes, with 14 new problems. The main session independently verified the high-severity ones before fixing them: M8/M9 overstated as workarounds, the regroup crash re-attribution, the false "falls back to production" comment, the Romano misreading, the "deterministic inventory" overstatement, and the S213 framing. All required fixes were applied in v2.1.
