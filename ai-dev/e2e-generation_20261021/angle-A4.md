# Angle A4: Firebase backend side of E2E and cross-platform flows

Retrieval: built-in WebSearch and WebFetch only, 2026-10-21. One exception: `gh search code` and `curl` were used to _locate_ lines in firebase-tools and react-native-firebase source. Every source quoted below was then re-fetched with WebFetch. Quotes come from WebFetch extractions. Where the extraction tool paraphrased, the text is marked (paraphrase) and is not given as a verbatim quote.

## Sources

`A4-S1 | https://firebase.google.com/docs/emulator-suite | Introduction to Firebase Local Emulator Suite | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S2 | https://firebase.google.com/docs/emulator-suite/connect_functions | Connect your app to the Cloud Functions Emulator | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S3 | https://firebase.google.com/docs/emulator-suite/connect_and_prototype | Connect your app and start prototyping | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S4 | https://firebase.google.com/docs/emulator-suite/install_and_configure | Install, configure and integrate Local Emulator Suite | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S5 | https://firebase.google.com/docs/emulator-suite/connect_firestore | Connect your app to the Cloud Firestore Emulator | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S6 | https://firebase.google.com/docs/emulator-suite/connect_auth | Connect your app to the Authentication Emulator | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S7 | https://firebase.google.cn/docs/emulator-suite/connect_auth?hl=en | Connect your app to the Authentication Emulator (official .cn mirror; REST section) | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S8 | https://firebase.google.com/docs/functions/local-emulator | Run functions locally | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S9 | https://firebase.google.com/docs/functions/schedule-functions | Schedule functions | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S10 | https://raw.githubusercontent.com/firebase/firebase-tools/master/src/emulator/functionsEmulatorShared.ts | firebase-tools source: functionsEmulatorShared.ts | Firebase (GitHub) | master @ 2026-10-21 | primary`
`A4-S11 | https://raw.githubusercontent.com/firebase/firebase-tools/master/src/emulator/functionsEmulator.ts | firebase-tools source: functionsEmulator.ts | Firebase (GitHub) | master @ 2026-10-21 | primary`
`A4-S12 | https://raw.githubusercontent.com/firebase/firebase-tools/master/src/emulator/hub.ts | firebase-tools source: hub.ts | Firebase (GitHub) | master @ 2026-10-21 | primary`
`A4-S13 | https://github.com/firebase/firebase-tools/issues/5875 | 2nd Gen Scheduler does not work correctly on the emulators | GitHub issue | 2023-05-22 (closed) | secondary`
`A4-S14 | https://github.com/firebase/firebase-tools/issues/11094 | Gen 2 auth triggers silently dropped and never fire | GitHub issue | 2026-09-17 (closed via PR #11097) | secondary`
`A4-S15 | https://github.com/firebase/firebase-tools/issues/8254 | Cloud Tasks Emulator ignores scheduleDelaySeconds/scheduleTime | GitHub issue | 2025-02-25 (open) | secondary`
`A4-S16 | https://raw.githubusercontent.com/invertase/react-native-firebase/main/packages/functions/lib/index.ts | RNFB functions module source | Invertase (GitHub) | main @ 2026-10-21 | primary`
`A4-S17 | https://raw.githubusercontent.com/invertase/react-native-firebase/main/packages/app/firebase-schema.json | RNFB firebase.json schema | Invertase (GitHub) | main @ 2026-10-21 | primary`
`A4-S18 | https://raw.githubusercontent.com/invertase/react-native-firebase/main/docs/firestore/emulator.mdx | RNFB Firestore emulator doc | Invertase | accessed 2026-10-21 | primary`
`A4-S19 | https://developer.android.com/privacy-and-security/security-config | Network security configuration | Google/Android | accessed 2026-10-21 | primary`
`A4-S20 | https://firebase.google.com/docs/emulator-suite/use_hosting?hl=en | Prototype and test web apps with the Hosting emulator | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S21 | https://firebase.google.com/docs/rules/unit-tests | Build unit tests (Security Rules) | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S22 | https://firebase.google.com/docs/functions/unit-testing | Unit testing of Cloud Functions | Google/Firebase | accessed 2026-10-21 | primary`
`A4-S23 | https://docs.stripe.com/webhooks | Receive Stripe events in your webhook endpoint | Stripe | accessed 2026-10-21 | primary`
`A4-S24 | https://docs.stripe.com/automated-testing | Automated testing | Stripe | accessed 2026-10-21 | primary`
`A4-S25 | https://github.com/stripe/stripe-mock | stripe-mock README | Stripe (GitHub) | accessed 2026-10-21 | primary`
`A4-S26 | https://docs.stripe.com/billing/testing/test-clocks | Use Simulations (test clocks) | Stripe | accessed 2026-10-21 | primary`
`A4-S27 | https://github.com/stripe/stripe-react-native/issues/1504 | Cannot access Primary Button from Payment Sheet on Android in Detox Tests | GitHub issue | 2023-09-14 (open) | secondary`
`A4-S28 | https://github.com/stripe/stripe-react-native/issues/1326 | Running E2E tests with Detox on Android | GitHub issue | 2023-03-14 (closed) | secondary`
`A4-S29 | https://www.twilio.com/docs/sendgrid/for-developers/sending-email/sandbox-mode | Sandbox Mode | Twilio SendGrid | accessed 2026-10-21 | primary`
`A4-S30 | https://mailpit.axllent.org/docs/api-v1/ | Mailpit API v1 | Mailpit (axllent) | accessed 2026-10-21 | primary`
`A4-S31 | https://mailpit.axllent.org/docs/ | Mailpit documentation | Mailpit (axllent) | accessed 2026-10-21 | primary`
`A4-S32 | https://docs.maestro.dev/advanced/javascript/make-http-s-requests | Make HTTP(S) requests | Maestro (mobile.dev) | undated, accessed 2026-10-21 | primary`
`A4-S33 | https://docs.maestro.dev/platform-support/web-desktop-browser | Web (desktop browser) | Maestro (mobile.dev) | accessed 2026-10-21 | primary`
`A4-S34 | https://www.infomazeelite.com/blog/field-service-qa-web-mobile-api-in-one-suite/ | Field service QA: web, mobile, API in one suite | Infomaze Elite (vendor blog) | undated | blog`
`A4-S35 | https://docs.cloud.google.com/firestore/docs/emulator | Use Firestore emulator locally | Google Cloud | accessed 2026-10-21 | primary`

## Evidence

`A4-E1 | A4-S1 | "Cloud Firestore, Realtime Database, Cloud Storage for Firebase, Authentication, Firebase Hosting, Cloud Functions (beta), Pub/Sub (beta), and Firebase Extensions (beta)" | "Which Firebase products are supported" list`
`A4-E2 | A4-S1 | "your app will still continue to communicate with production Firebase services when emulators are not available or configured." | overview, connecting apps`
`A4-E3 | A4-S2 | "A demo Firebase project has no _real_ Firebase configuration and no live resources." | "Choose a Firebase project" section`
`A4-E4 | A4-S2 | "When working with demo Firebase projects, your apps and code interact with emulators _only_." | same section`
`A4-E5 | A4-S2 | "We recommend you use demo projects wherever possible." | same section`
`A4-E6 | A4-S2 | "The Cloud Functions emulator supports background-triggered functions from the following sources: Realtime Database emulator, Cloud Firestore emulator, Authentication emulator, Pub/Sub emulator, Firebase alerts emulator." | "Instrument your app for background functions"`
`A4-E7 | A4-S2 | "The emulator automatically sets up emulated task queues based on trigger definitions, and the Admin SDK reroutes enqueued requests to the emulator if it detects that it is running via the CLOUD_TASKS_EMULATOR_HOST environment variable." | task queue functions section`
`A4-E8 | A4-S2 | Web: "connectFunctionsEmulator(functions, "127.0.0.1", 5001)"; Kotlin: "functions.useEmulator("10.0.2.2", 5001)" | callable functions instrumentation snippets`
`A4-E9 | A4-S2 | HTTP functions are served at "http://$HOST:$PORT/$PROJECT/$REGION/$NAME" | HTTPS functions section`
`A4-E10 | A4-S2 | "Contents of .env.local take precedence over .env"; "you can override secrets values by setting up a .secret.local file" | environment variables / secrets sections`
`A4-E11 | A4-S2 | the emulator "does not support retrying functions on failure"; "does not enforce memory or processor restrictions" | "How the emulator differs from production"`
`A4-E12 | A4-S3 | "For unit testing and CI workflows, you can start up emulators, run scripted tests, and shut down emulators in a single call with the exec command" | prototyping workflow step`
`A4-E13 | A4-S4 | --import: "Import data saved using the --export-on-exit startup option"; --export-on-exit: "Instruct the emulator(s) to export data to a directory when shutdown occurs" | CLI flag table for emulators:start / emulators:exec`
`A4-E14 | A4-S4 | "Local Emulator Suite issues warnings when it detects multiple project IDs in the environment"; override "by setting the singleProjectMode key to false in your firebase.json" | "Choose a Firebase project" / project ID configuration`
`A4-E15 | A4-S5 | "The emulator does not track compound indexes and instead will execute any valid query." | "How the Cloud Firestore emulator differs from production"`
`A4-E16 | A4-S5 | "When the Firestore and Cloud Functions emulators are both running, they automatically work together." | "Integrate with Cloud Functions"`
`A4-E17 | A4-S5 | "It's generally a good practice to use one project ID for all emulator invocations, so the Emulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases." | project ID note`
`A4-E18 | A4-S5 | "The Firebase Admin SDKs automatically connect to the Cloud Firestore emulator when the FIRESTORE_EMULATOR_HOST environment variable is set" | Admin SDK section`
`A4-E19 | A4-S5 | Clear data: "DELETE http://localhost:8080/emulator/v1/projects/{projectID}/databases/(default)/documents" (endpoint string; surrounding prose paraphrased) | "Clear your database between tests"`
`A4-E20 | A4-S6 | the emulator "issues _unsigned_ ID tokens, which are only accepted by other Firebase emulators, or the Firebase Admin SDK when configured." | "How the Authentication emulator differs from production"`
`A4-E21 | A4-S7 | "GET http://localhost:9099/emulator/v1/projects/{project-id}/oobCodes" ; "DELETE http://localhost:9099/emulator/v1/projects/{project-id}/accounts" ; "GET http://localhost:9099/emulator/v1/projects/{project-id}/verificationCodes" | emulator-specific REST endpoints (endpoint strings)`
`A4-E22 | A4-S8 | "the dispatch system used in production is more complex than the one implemented in the emulator, so you should not expect emulated behavior to precisely mirror production environments." | trigger behaviour caveat`
`A4-E23 | A4-S8 | "emulator output simulates deployment of functions by default in a specific region (us-central1) that may not match the actual production deployment default region." | region note`
`A4-E24 | A4-S8 | "If your code needs to be transpiled (TypeScript, React) make sure to do so before running the emulator." | "Run the emulator suite"`
`A4-E25 | A4-S8 | "Run functions on a schedule" appears only as a sidebar link; the page body does not say scheduled functions are emulated (WebFetch verification, paraphrase) | whole page`
`A4-E26 | A4-S9 | deployment creates "a scheduler job and an HTTP function"; the page has no guidance on local or emulator testing (paraphrase of absence) | onSchedule deploy section`
`A4-E27 | A4-S10 | "// TODO: This is an awkward transformation. Emulator does not understand scheduled triggers - maybe it should?" followed by def.eventTrigger = { eventType: "pubsub", resource: "" } | isScheduleTriggered branch`
`A4-E28 | A4-S11 | "In production this topic looks like "firebase-schedule-{FUNCTION_NAME}-{DEPLOY-LOCATION}", we simply drop the deploy location"; topic = "firebase-schedule-" + triggerName; returns false if Pub/Sub emulator absent | addPubsubTrigger`
`A4-E29 | A4-S12 | static PATH_DISABLE_FUNCTIONS = "/functions/disableBackgroundTriggers"; PATH_ENABLE_FUNCTIONS = "/functions/enableBackgroundTriggers"; PATH_EMULATORS = "/emulators"; PATH_EXPORT = "/_admin/export" (app.put for the two functions paths) | EmulatorHub constants and handlers`
`A4-E30 | A4-S12 | "Disabling Cloud Functions triggers, non-HTTP functions will not execute." | PUT disableBackgroundTriggers handler log`
`A4-E31 | A4-S13 | "When I start the emulators and try to execute a function with firebase functions:shell, the following error occurs" (TypeError: req.header is not a function) | reporter, 2023-05-22`
`A4-E32 | A4-S14 | Gen 2 auth triggers are "silently ignored at emulator startup. No warning or error is emitted" | issue body, firebase-tools 15.30.1`
`A4-E33 | A4-S14 | "The Auth v2 was only recently released so this might be something we may have missed." | contributor aalej`
`A4-E34 | A4-S15 | "The task will run immediately and not respect scheduleTime or scheduleDelaySeconds should you have one set." | issue body, 2025-02-25`
`A4-E35 | A4-S16 | "Mapping functions host "localhost" to "10.0.2.2" for android emulators. Use real IP on real devices. You can bypass this behaviour with "android_bypass_emulator_url_remap" flag." | useEmulator(), console.log`
`A4-E36 | A4-S17 | "On android devices, the urls of firebase emulators will be remapped from localhost to 10.0.2.2. If you don't need this behaviour set this fleg to true." | android_bypass_emulator_url_remap description (typo "fleg" is in source)`
`A4-E37 | A4-S18 | set the emulator "before any read/write operations occur to ensure it doesn't affect your Cloud Firestore data." with connectFirestoreEmulator(getFirestore(), 'localhost', 8080) | RNFB Firestore emulator doc`
`A4-E38 | A4-S19 | "Starting with Android 9 (API level 28), cleartext support is disabled by default." | "Opt out of cleartext traffic"`
`A4-E39 | A4-S20 | "By default, the emulators only respond to requests from localhost." ; config example "host": "0.0.0.0" | "Test from other local devices"`
`A4-E40 | A4-S21 | assertFails "asserts that the supplied Promise wrapping an emulator operation will be rejected with a Security Rules violation." | rules-unit-testing API`
`A4-E41 | A4-S21 | withSecurityRulesDisabled: "Run[s] a test setup function with a context that behaves as if Security Rules were disabled." | rules-unit-testing API`
`A4-E42 | A4-S22 | Offline mode is "generally not recommended if you have Cloud Firestore or Realtime Database functions." | "Online mode vs offline mode"`
`A4-E43 | A4-S23 | "stripe listen --forward-to localhost:4242/webhook" ; "The stripe listen command outputs the {{WEBHOOK_SIGNING_SECRET}}." | "Test locally without a registered URL"`
`A4-E44 | A4-S23 | "stripe trigger payment_intent.succeeded" | "Trigger test events"`
`A4-E45 | A4-S23 | "Stripe requires the raw body of the request to perform signature verification." | "Don't manipulate the raw body request"`
`A4-E46 | A4-S23 | "Stripe doesn't guarantee the delivery of events in the order that they're generated." | "Event ordering"`
`A4-E47 | A4-S24 | "Frontend interfaces, like Stripe Checkout or the Payment Element, have security measures in place that prevent automated testing, and Stripe APIs are rate limited." | intro`
`A4-E48 | A4-S24 | "you can simulate the output of our interfaces and API requests using mock data to test your application behavior" | intro`
`A4-E49 | A4-S25 | stripe-mock "is stateless. Data you send on a POST request will be validated, but it will be completely ignored beyond that." | README limitations`
`A4-E50 | A4-S25 | responses "are hardcoded, and will not necessarily represent realistic responses based on the parameters you input." | README`
`A4-E51 | A4-S26 | "Simulations use test clocks to control time." ; "use a separate sandbox for continuous integration (CI) so its test clocks and related objects don't interfere with local development." | intro`
`A4-E52 | A4-S27 | Title: "Cannot access Primary Button from Payment Sheet on Android in Detox Tests"; open, affects stripe-react-native 0.39–0.51 (paraphrase of body) | issue`
`A4-E53 | A4-S28 | "I can't figure out how to target the card fields inside the payment sheet on Android using Detox matchers." | reporter, 2023-03-14`
`A4-E54 | A4-S29 | "Sandbox mode is an optional parameter within mail_settings that validates a Mail Send request without delivering the email." | intro`
`A4-E55 | A4-S29 | sandbox requests return 200 OK instead of the 202 ACCEPTED of normal sends (paraphrase) | response section`
`A4-E56 | A4-S30 | Mailpit "provides a simple REST API to access, search and delete stored messages." | API v1 intro`
`A4-E57 | A4-S31 | "It acts as an SMTP server, provides a modern web interface to view & test intercepted emails. It also contains an API for automated integration testing." | docs intro`
`A4-E58 | A4-S32 | http.post(...) then output.appointmentTitle = data.title; flow uses "- assertVisible: ${output.appointmentTitle}" | example`
`A4-E59 | A4-S33 | web support is Beta; Chromium is "the current default and only supported browser."; "the same commands like tapOn, inputText, and assertVisible work identically on Web as they do on Android and iOS." | platform support page`
`A4-E60 | A4-S34 | "A Playwright test creates a work order on the web platform, a Detox test verifies it appears on the mobile app" | cross-platform section`
`A4-E61 | A4-S35 | "Because the emulator stores data only in memory, it will not persist data across runs." | known differences`
`A4-E62 | A4-S35 | "It might take up to 30 seconds for the emulator to release the locks" (concurrent writes to one document) | transactions difference`

## Claims

`A4-C1 | The Emulator Suite emulates Firestore, RTDB, Storage, Auth, Hosting, Functions (beta), Pub/Sub (beta) and Extensions (beta). FCM, Cloud Scheduler, Remote Config, Analytics and App Check are not on the list. | support: A4-E1 (absence inferred from the official list) | independent_sources: 1 | high`
`A4-C2 | If a product's emulator is not configured or not running, the client SDKs silently talk to production, unless the project ID is a demo- project. With a demo- project the code talks to emulators only. | support: A4-E2, A4-E3, A4-E4 | independent_sources: 1 (two pages, same publisher) | high`
`A4-C3 | Firebase officially recommends demo- projects wherever possible. | support: A4-E5 | independent_sources: 1 | high`
`A4-C4 | Emulator data is namespaced by project ID, and the CLI warns when it sees more than one project ID. If a seed script (Admin SDK) uses a different project ID than the app, the data is effectively invisible to the app. This is the likely mechanism behind the reference project's "seed data in unexpected namespace". | support: A4-E14, A4-E17, A4-E18 | independent_sources: 1 | medium (the mechanism is inferred from the docs; the reference-project diagnosis is analyst inference)`
`A4-C5 | Background triggers are emulated for Firestore, RTDB, Auth, Pub/Sub and Firebase Alerts. Storage triggers also work when both the Storage and Functions emulators run. Callables and HTTP functions are emulated. Task queues are emulated through CLOUD_TASKS_EMULATOR_HOST. | support: A4-E6, A4-E7, A4-E16, A4-E9; Storage triggers per S1 overview list | independent_sources: 1 | high`
`A4-C6 | Scheduled functions (v1 and v2 onSchedule) are NOT run on a cron by the emulator. The emulator maps them to a Pub/Sub trigger on topic "firebase-schedule-<name>". The trigger is registered only if the Pub/Sub emulator is running, so a test must publish to that topic to invoke the function. | support: A4-E27, A4-E28, A4-E25, A4-E26 | independent_sources: 1 (source code + docs silence; community posts agree but were not fetched) | high for "no cron", medium for exact invocation details on v2`
`A4-C7 | Emulator trigger support has had silent gaps. As recently as firebase-tools 15.30.1 (Sept 2026), Gen 2 auth triggers were dropped with no warning (since fixed). The Cloud Tasks emulator runs tasks immediately, ignoring scheduleTime (open since Feb 2025). | support: A4-E32, A4-E33, A4-E34, A4-E31 | independent_sources: 2 issues | medium`
`A4-C8 | The Functions emulator does not retry failed functions, does not enforce memory or CPU limits, ignores IAM, may differ in timing, and simulates us-central1 by default. Tests must not assume production retry or region behaviour. | support: A4-E11, A4-E22, A4-E23 | independent_sources: 1 | high`
`A4-C9 | The TypeScript functions source must be compiled before the emulator starts. Otherwise the emulator serves stale or missing code. | support: A4-E24 | independent_sources: 1 | high`
`A4-C10 | Firestore emulator differences: composite indexes are not enforced (any valid query runs), not all limits are enforced, concurrent transactions can take up to 30 seconds to release locks, and data lives in memory only. Index correctness therefore needs a real project. | support: A4-E15, A4-E61, A4-E62 | independent_sources: 2 (Firebase + Google Cloud docs) | high`
`A4-C11 | Deterministic reset uses emulator REST endpoints. DELETE the Firestore documents endpoint, and DELETE /emulator/v1/projects/{id}/accounts for Auth. Retrieve email OOB codes and SMS codes with GET .../oobCodes and .../verificationCodes. | support: A4-E19, A4-E21 | independent_sources: 1 | high`
`A4-C12 | The Emulator Hub exposes PUT /functions/disableBackgroundTriggers and /functions/enableBackgroundTriggers. A harness can seed data without firing triggers, then re-enable them. | support: A4-E29, A4-E30 | independent_sources: 1 (source code; not in the narrative docs fetched) | high (code), medium (API stability)`
`A4-C13 | Seed state can be snapshotted and restored with --export-on-exit / --import (and emulators:export). emulators:exec starts the emulators, runs a test command, and shuts them down in one call. | support: A4-E12, A4-E13 | independent_sources: 1 | high`
`A4-C14 | The Auth emulator issues unsigned ID tokens that only emulators or a configured Admin SDK accept. A mixed setup (some services emulated, some real) breaks auth. | support: A4-E20 | independent_sources: 1 | high`
`A4-C15 | React Native Firebase automatically remaps localhost/127.0.0.1 to 10.0.2.2 on Android, unless android_bypass_emulator_url_remap is true in firebase.json. Physical devices need the host's real IP. | support: A4-E35, A4-E36 | independent_sources: 1 (RNFB source) | high`
`A4-C16 | Android also needs two things: the emulators bound beyond localhost (host "0.0.0.0") for physical devices, and cleartext HTTP allowed for API 28+. Cleartext is often already permitted in RN debug builds, but not in release/E2E builds. Either gap is a plausible cause of "Android couldn't be pointed at emulators". | support: A4-E38, A4-E39, A4-E35 | independent_sources: 2 (Android docs, Firebase docs) | medium (the reference-project cause is inferred; the RN debug-manifest detail was not fetched)`
`A4-C17 | useEmulator must be called before any read/write. Otherwise the client may already be bound to production. | support: A4-E37, A4-E2 | independent_sources: 2 | high`
`A4-C18 | @firebase/rules-unit-testing gives authenticated and unauthenticated contexts, rules-disabled seeding, and assertSucceeds/assertFails against the emulator. It suits rules tests, not UI E2E. | support: A4-E40, A4-E41 | independent_sources: 1 | high`
`A4-C19 | For firebase-functions-test, online mode (real test project) is recommended. Offline mode is discouraged for Firestore/RTDB functions. | support: A4-E42 | independent_sources: 1 | high`
`A4-C20 | Stripe states that Checkout and the Payment Element block automated testing and that its APIs are rate-limited. It recommends mocked responses and errors for CI, with real test-mode API calls run sparingly. | support: A4-E47, A4-E48 | independent_sources: 1 | high`
`A4-C21 | Local Stripe webhook testing uses \`stripe listen --forward-to <url>\`, which prints its own whsec\_ signing secret, and \`stripe trigger <event>\`. The handler must verify against the raw body and must tolerate out-of-order and duplicate events. | support: A4-E43, A4-E44, A4-E45, A4-E46 | independent_sources: 1 | high`
`A4-C22 | stripe-mock is stateless, uses hardcoded fixtures, and does not emit webhooks. It cannot validate stateful payment flows. | support: A4-E49, A4-E50 | independent_sources: 1 | high`
`A4-C23 | Stripe test clocks control time for billing flows. Stripe recommends a separate sandbox for CI. | support: A4-E51 | independent_sources: 1 | high`
`A4-C24 | The PaymentSheet UI in stripe-react-native has long-standing Android Detox selector problems (one issue open since 2023). Driving the native sheet in E2E is fragile. | support: A4-E52, A4-E53 | independent_sources: 2 issues (same repo) | medium`
`A4-C25 | SendGrid sandbox mode validates sends without delivering (200 vs 202), so content cannot be asserted in an inbox. Mailpit captures SMTP mail and exposes a REST API for assertions. It captures only SMTP, not SendGrid's HTTP API. | support: A4-E54, A4-E55, A4-E56, A4-E57 | independent_sources: 2 | high (SMTP-only is analyst inference from "acts as an SMTP server")`
`A4-C26 | Maestro JS can call HTTP APIs and pass the results into flow assertions. This allows backend-as-bridge steps (seed or verify through REST) inside a mobile flow. Maestro web is Beta and Chromium-only. | support: A4-E58, A4-E59 | independent_sources: 1 | high`
`A4-C27 | Precedent exists for cross-client tests where a web runner (Playwright) creates state and a mobile runner (Detox) verifies it, coordinated through the shared backend. The only precedent found is a vendor case study. | support: A4-E60 | independent_sources: 1 (blog) | low`

## Conflicts & gaps

- **Scheduled functions:** the docs never state the behaviour explicitly. S8 has only a sidebar link, S9 has no emulator guidance, and S2's trigger list leaves out "scheduled". The firebase-tools source (S10/S11) is the only authoritative signal. It shows a Pub/Sub topic mapping and a TODO admitting the emulator "does not understand scheduled triggers". In production, v2 onSchedule uses Cloud Scheduler calling an HTTP function (S9), while the emulator models it as Pub/Sub. That mismatch is unverified against a live run.
- **Firestore clear endpoint:** the path was extracted from S5 but its surrounding prose was paraphrased by the fetch tool. It needs a re-check by a live `curl -X DELETE`.
- **Storage emulator:** S1 lists Storage triggers. S5/S2 say Storage-triggered functions work with no extra setup (the latter was paraphrased). Signed URLs and resumable uploads: an early paraphrase claimed they are unsupported, but the verbatim re-fetch did not confirm this. Treat it as unknown.
- **FCM:** no official page fetched states "FCM cannot be emulated". The claim rests on its absence from the product list (A4-E1). The Admin SDK `dryRun` parameter could not be extracted from the reference page (fetch returned only the nav).
- **Eventarc:** S2 mentions an Eventarc emulator for custom extension events. The fetch did not cover whether Firestore v2 triggers (which use Eventarc in production) take a separate path in the emulator.
- **RN debug cleartext:** that React Native debug builds already permit cleartext (A4-C16) is from memory and was not fetched. Verify it in the project's AndroidManifest/network_security_config.
- **Cross-platform orchestration:** no primary-source framework was found that drives Playwright and Detox/Maestro in a single test process. The only precedent is a vendor blog. Maestro's web mode is Beta and Chromium-only.
- Community posts (Fireship, Medium) on the `firebase-schedule-*` workaround surfaced in search snippets only and were not fetched (the Fireship URL 404'd after a redirect), so they are not cited.

## Analyst assessment

The four failures in the reference project all come from config drift between three parties: the emulator processes, the app clients, and the seed/test scripts. The generator should not emit tests until it has produced and validated one **harness manifest** that pins all three together.

**1. One project ID, demo- by default.** Generate `firebase.json`/`.firebaserc` settings and a `demo-<slug>` project ID, and inject the same ID into the RN app (`firebase.json`/env), the Angular `environment.e2e.ts`, the seed script (`GCLOUD_PROJECT`), and the REST reset URLs. Demo projects fail closed instead of leaking to production (C2, C3), and a single ID removes the namespace mismatch (C4). Preflight check: query the Hub's `GET /emulators`, then read back a sentinel document written by the seeder _through the client SDK_.

**2. Start everything the backend needs, always.** Run `firebase emulators:exec --only auth,firestore,functions,storage,pubsub --import ./e2e/seed` with the functions build step before it (C9, C13). Pub/Sub is mandatory whenever the code has a scheduled function; otherwise those functions silently never register (C6). The preflight should fail loudly if the Functions emulator is missing from `/emulators`, which is the reference project's first failure. It should also grep emulator logs for "function ignored" warnings, given the silent trigger-dropping history (C7).

**3. Clients.** For RN, call `useEmulator` before first use (C17) and let RNFB's 10.0.2.2 remap work (C15). For physical devices or CI device farms, bind `host: 0.0.0.0` and inject the LAN IP. Make sure the E2E build variant allows cleartext to the emulator host (C16). Make the callable region explicit on both client and server, because the emulator defaults to us-central1 (C8).

**4. Deterministic data.** Before each test file: disable background triggers, clear Firestore and Auth through REST, seed with factories through the Admin SDK, then re-enable triggers (C11, C12). Use rules-unit-testing only for a separate rules suite (C18). Assert side-effects by polling Firestore with a timeout instead of sleeping, since trigger timing differs from production and nothing retries (C8). Invoke scheduled jobs by publishing to `firebase-schedule-<name>` from the test, not by waiting on a clock (C6).

**5. Third parties: three tiers.** (a) In CI E2E, stub the Stripe client behind an interface, and drive webhooks by POSTing locally signed fixture events to the emulated HTTP function. Stripe itself recommends mocking because Checkout and the Payment Element resist automation (C20, C22). (b) In a nightly "integration" lane, use real Stripe test mode with `stripe listen --forward-to http://127.0.0.1:5001/<id>/<region>/<fn>` and its whsec secret in `.secret.local` (C21, A4-E10), plus test clocks for subscriptions (C23). Do not have generated tests tap through the native PaymentSheet on Android (C24). (c) For email, route the transport to Mailpit SMTP in E2E, or capture the SendGrid payload at the adapter boundary; sandbox mode only proves the request validated (C25). FCM is not emulated, so assert the outbound send call or the queued-notification document, never delivery.

**6. Cross-platform flows.** Use backend-as-bridge: the Playwright step (Angular admin) commits state, and the mobile step (Maestro/Detox) asserts the UI, with an emulator poll between them to confirm the write landed (C26, C27). Run them as sequential stages in one orchestrator script, not as two simultaneous drivers.

**Must use a staging project:** composite indexes (C10), IAM and Secret Manager, real Scheduler/Eventarc dispatch, FCM delivery, and the Stripe-hosted UI.
