# Phase 7 — Red-team Round 2 (2026-10-21)

One fresh verifier agent (no Round-1 context beyond the files) rechecked report v2. It used the live GitHub API, `node_modules` source, the raw cache, and the regroup repo.

**Round-1 fix status:** most items FIXED. PARTIAL: R9, R13, R14, R19, R21, and defects 17/18. NOT FIXED: defect 4 (S41 still cited for the spec mitigation in the Executive Summary).

**New problems found in v2, and how each was handled in v2.1** (✔ = main session independently verified before fixing):

| # | Problem | Severity | v2.1 action |
| - | ------- | -------- | ----------- |
| 1 | M8/M9 presented as "workarounds"; the reporter says they validate healthy-driver reuse, "not recovery from the fatal status-bar AX failure", and that the CI run was not controlled and had recoveries ✔ | high | Reframed as "reported mitigations, not fixes"; treated as spike variants |
| 2 | Regroup crash re-attribution over-corrected ("a different failure"); the symptoms partly overlap #3538 and Xcode is in range | med-high | Changed to "undiagnosed" in the Executive Summary, §5 and §9 |
| 3 | "Falls back to production" repeated from regroup's code comment, which is wrong: `useEmulator` never checks reachability ✔ | medium | I21 corrected; I24 added (`checkEmulatorsRunning` unused); §4, the Executive Summary and §10 rewritten, and the fix now requires a reachability probe |
| 4 | Romano (S215) misread as "not environment"; Finding 3 stresses environment configuration on mobile ✔ | medium | §4, the H2 row and the D4 notes corrected |
| 5 | "Deterministic inventory pass" overstated; I10 came from a grep-based agent plus a main-session check | medium | Executive Summary reworded |
| 6 | S213 framing incomplete: the prompt generates new rules, writes `firestore.rules`, and lets the LLM edit tests; "fetch deployed rules" was uncited ✔ | medium | Executive Summary and §10 caution added; the fetch claim removed from §9 |
| 7 | Executive Summary cites [S41, S42] for the mitigation | low | Split: the effect is S41/S42, the mitigation is S42 only |
| 8 | "Only the third catches stable-but-wrong" contradicts I10 | low-med | Reworded to "comparisons against an independent statement of intent" |
| 9 | Detox suites "lost to ignore-all-JS" is an inference | low | Labelled "likely" |
| 10 | State-management lines uncited or mis-cited (Keychain, clock, L9, "main critique") | low | Labelled as uncited or reworded |
| 11 | "Middle design … v2 adopts that" mis-maps to the phase table | low-med | Restated: all phases kept, state-model deferred, spec gate optional |
| 12 | H5 label contradicts the Phase 3 design | low | Changed to "Stands, narrowed" |
| 13 | Bookkeeping: missing round-2 file, cited count, I-range, S2/S211 duplicate | low | Fixed. S2 and S211 are the same page (S211 dropped from body; S210 no longer cited) |
| 14 | "Device time, not tokens, is binding" is unsupported | low | Changed to "the cost that can be bounded" |

Also applied: Executive Summary softened ("assembled … several key parts unproven"; guards confidence lowered to medium-high); rerun counts made consistent (10 in qualification, 20 for the Phase 0 smoke flow).

**Iteration budget:** two rounds used (the maximum). Remaining uncertainty is disclosed in report §9.
