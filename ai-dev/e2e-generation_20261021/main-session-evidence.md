# Main-session evidence (M-series)

Fetched directly by the main session through the GitHub REST API (`api.github.com/repos/mobile-dev-inc/maestro/issues/3538` and `/comments`) on 2026-10-21. Source: S206 (Maestro issue #3538). The quotes are verbatim from the API JSON.

| ID  | Quote                                                                                                                                                                              | Locator                                                                                        |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| M1  | "iOS: transient AX failure while snapshotting status bars tears down the driver; every remaining flow fails with DeviceUnreachableException"                                       | Issue title; state `open`; created 2026-08-27T09:03:28Z                                        |
| M2  | "every remaining flow of the run fails in 2–6s with `maestro.DeviceUnreachableException`** (29–33 flows lost per occurrence in our runs)"                                          | Issue body, "Actual results"                                                                   |
| M3  | "We're reworking the driver mechanism _right now_ and expect to be done in some small number of weeks."                                                                            | Maintainer comment (Fishbowler), 2026-08-27                                                    |
| M4  | "Our suite is 39 flows and each one is already a separate `maestro test` invocation (the per flow loop suggested in #3254 and #3318), and we still hit it."                        | Comment (MuadDib), 2026-09-10; Maestro 2.8.0, iOS 26.5, Xcode 26.6                             |
| M5  | "So the AX race is not rare at all. It is common and mostly harmless, and only the cached element variant is fatal."                                                               | Same comment                                                                                   |
| M6  | "Same failure on **Maestro 2.11.0**, iPhone simulator, iOS 26.5, self-hosted Apple Silicon runner."                                                                                | Comment (lsoares), 2026-10-01                                                                  |
| M7  | "Overriding `record(_:)` in `maestro_driver_iosUITests` to log the issue without calling `super` keeps the server alive. WebDriverAgent's `FBFailureProofTestCase` does the same." | Comment (arun279), 2026-10-18; Maestro 2.10.0, iOS 26.4, Xcode 26.6; links an unofficial patch |

Implications (main-session judgment):

- Per-flow invocation limits the blast radius but does **not** prevent the failure (M4). D3's suggestion that per-flow invocation is "safer" holds only for blast radius.
- Six weeks after the maintainer's "small number of weeks" estimate (M3), no fixed release was found through 2.11.0 (D3 changelog check).
- An unofficial driver patch exists (M7). It is unvetted and would mean maintaining a forked driver.

## Added after the Phase 6 red-team (2026-10-21)

| ID | Quote | Locator |
| -- | ----- | ------- |
| M8 | "CI follow-up (2026-10-16): with Maestro 2.11.0 / Java 21 / Xcode 26.3 / iOS 26.2, all 213 page flows completed successfully across four GitHub-hosted macOS arm64 runners, one Simulator per runner. We kept 20-page batches" | #3538 comment (ivan-moego), via GitHub API |
| M9 | "With `--driver-host-port 7001 --no-reinstall-driver` from the first invocation onward, both flows passed with the same port and runner PID." | same comment, local lifecycle follow-up (Maestro 2.11.0, Xcode 26.6, iOS 26.2) |

## Regroup code facts verified after the red-team (I-series additions)

- **I21:** `mobile/src/config/firebase-emulator.ts` connects only Auth (9099), Firestore (8080) and Storage (9199). There is **no Functions emulator connection** anywhere in `mobile/src`, so callables made in E2E mode target the configured production project. The file's header comment claims that "if emulators aren't running the try/catch silences the failure and Firebase falls back to production." **That comment is wrong** (Round-2 finding, main-session verified): RNFirebase `useEmulator` only validates its arguments and sets the host (`node_modules/@react-native-firebase/firestore/lib/index.js`, `useEmulator(host, port)`). It never checks reachability, so a stopped emulator makes Auth/Firestore/Storage calls fail rather than reach production. Emulator connection is gated on `__DEV__`, so non-dev builds use production by design.
- **I22:** `mobile/e2e/` contains only `screenshots.e2e.ts` plus scripts and docs. The README's dispute, verification and RBAC Detox suites (`npm run test:e2e:dispute`) have no test files in the repo, so L14 describes documentation, not existing tests.
- **I23:** `functions/src/scheduled/index.ts`: `updateDisputes` is `onSchedule`, "Runs daily at 2 AM UTC. Automatically resolves disputes that have been outstanding for more than 2 days". It loads every house (`houseCollection.get()`, "Retrieving all houses...") and processes each one. Tests touching it need backdated fixtures and a serial lane.
- **I24:** `src/config/firebase-emulator.ts` defines `checkEmulatorsRunning()` (fetches the Emulator UI at :4000), but nothing in `mobile/src` calls it.
