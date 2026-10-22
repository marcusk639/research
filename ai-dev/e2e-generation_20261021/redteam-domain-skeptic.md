# Red-team — Domain Skeptic (persona 2), 2026-10-21

Independent verifier agent. Checked the regroup repo at `3355a81`, live GitHub (Maestro #3538, releases, protractor, firebase-tools), the Firebase MCP prompt source, and StrykerJS docs. Result: 4 REFUTE, 13 NARROW, 7 STANDS.

| ID | Verdict | Key reason |
| -- | ------- | ---------- |
| R1 | NARROW | Partial survey; regroup's own `mobile-e2e` skill has the same pipeline shape [L4] |
| R2 | STANDS | |
| R3 | NARROW | "Mostly unusable" is a unit-level finding (~4% per test case at Meta); spec-first E2E did better (60–68% usable) |
| R4 | REFUTE ("only bug channel") | Implicit oracles (crashes, hangs, permission-denied) found real regroup bugs [L8] |
| R5 | STANDS | |
| R6 | NARROW | Needs an explicit cross-feature pass for shared state (gates, claims, webhooks) |
| R7 | NARROW | Mixed evidence; resolve rate ≠ comprehension |
| R8 | STANDS | Edges (navigate calls, gate wrapper) are runtime-only |
| R9 | NARROW | **Regroup never points the Functions client at the emulator** (`firebase-emulator.ts`), so callables in E2E target production |
| R10 | STANDS | Applies to v2 `onSchedule`, which regroup uses |
| R11 | STANDS | Caveat: S99 covers web Checkout/Payment Element, not native PaymentSheet |
| R12 | NARROW | Smoke failure was an app bug; the login wait fix was an authoring defect |
| R13 | NARROW | Intermittent; per-flow limits loss to ~one flow |
| R14 | REFUTE | Regroup's symptom was driver *start* failure; a single session reduces N−1 starts; `run-all.yaml` already exists |
| R15 | STANDS | `newArchEnabled=false`, Detox 20.47.0 installed |
| R16 | NARROW | Two driver toolchains = double harness cost; use one runner if Maestro wins the spike |
| R17 | STANDS | 2024-era models |
| R18 | NARROW | o3-only; lower bound by manual inspection |
| R19 | REFUTE ("no direct precedent") | Firebase MCP `generate_security_rules` prompt: codebase → rules + rules-unit-testing suite + run loop + stop-on-rule-failure guard. Rules-from-rules tests are circular; Admin-SDK callables bypass rules |
| R20 | NARROW | StrykerJS command runner can drive any command (full suite per mutant) |
| R21 | NARROW | At the report's own 10-rerun bar: 17–33 device-hours before mutants, resets and repairs; no basis for a token figure |
| R22 | REFUTE (as justified) | Chores > disputes in docs; the "Detox precedent" is a README for deleted files; `updateDisputes` scans every house (needs backdated fixtures and a serial lane) |
| R23 | NARROW | Five written plus one read-only (`paywall/config`); `elections` is a subcollection; kill switch inert under repo rules |
| R24 | STANDS | Angular 9 / Node 22 needs `--openssl-legacy-provider` or pinned Node |

**Architecture gaps (10):**

1. Per-SDK emulator routing check, a `demo-` E2E build variant (swap native config files), and egress denial.
2. Merge the split `firebase.json` files into a single `firebase.e2e.json`.
3. Persona sessions: custom-token sign-in via a launch argument, forced token refresh, sign-out at start; the iOS Keychain persists sessions.
4. Listener and offline-queue isolation: terminate → reset → import → launch; disable the offline queue and refetch intervals in E2E builds; unique house per test.
5. One emulator per simulator; a serial lane for scheduled jobs.
6. Path enumeration needs declared `Given` fixtures; transition coverage, not all paths; refuse paths with no fixture.
7. Clock control: an injectable `NOW` in functions under the emulator; backdated fixtures.
8. Trigger-aware fixtures (post-trigger state, or re-enable triggers and wait); bounded polling.
9. Rules oracle: derive expected allow/deny from the code access inventory × the persona matrix (not from the rules alone); add callable authorization tests.
10. Guards: hooks miss Bash edits, so make the approved `e2e/` tree read-only and check an assertion-baseline hash; extend the existing `verify-diff.sh`. CI: macOS minutes multiplier; Linux/KVM Android lane; iOS nightly.

**Prior art missed:**

- The Firebase MCP prompt; Firebase MCP tools `firebase_get_security_rules` / `firebase_validate_security_rules` (fetch deployed rules).
- StrykerJS command runner.
- XACML request generation (Martin & Xie), Margrave, AWS Zelkova (from memory; not fetched).
- Regroup's own `mobile-e2e` skill as the baseline.
