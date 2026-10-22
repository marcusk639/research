# Phase 4 / 4.5 — Triangulation and outline refinement

Built 2026-10-21 from `angle-A1..A6.md`, `regroup-case.md` (L), `regroup-inventory.md` (I), and `quote-check.md`.
Claim IDs are angle-local (A1-C3, etc.); global IDs are in `id-map.json`. The D-series (delta retrieval) is pending and is folded in at Phase 7.

## Ledger health after consolidation

- 168 angle source rows → **160 unique sources** after URL deduplication. 133 claims, 340 evidence rows.
- Quote fidelity, checked against raw pages independently of WebFetch: **299/340 confirmed** (220 verbatim, 64 near-verbatim, 14 confirmed by manual grep, 1 found at a different URL). 28 partial, 10 paraphrase-only, 2 unverifiable. Rule: partial and paraphrase-only rows may give context but cannot carry a number or a headline claim.
- Independent-publisher recount: 91 of 133 claims rest on a single publisher. Most are doc facts (a feature exists, a flag does X), where one primary source is enough. **Load-bearing comparative or empirical claims with a single publisher are tagged below and demoted.**
- 4 claims have no confirmed support: A1-C11, A1-C25, A2-C12, A2-C18. They are demoted to low confidence unless the D-series rescues them.

## Cross-angle findings (triangulated)

### T1. Raw LLM test output is mostly unusable; execution filtering carries the quality. **Confidence: high.**

- Meta TestGen-LLM (unit, Kotlin): per class, 75% built, 57% passed reliably, 25% added coverage; the filter chain was build → pass → 5× rerun → coverage gain [A2-C1, A2-C2].
- Cypress/BMW spec-first industrial pipelines: about a third of scripts needed regeneration or were discarded [A2-C17; E98 confirmed manually].
- A repair-loop case study: 70% converged, but with assertion weakening and deletion [A6-C12, low].
- Generated locators were 32.6–54% accurate [A2-C16].
- Independent origins: Meta, FEUP/Cypress, FEUP/BMW (same group as Cypress, so effectively 2 independent), plus the locator study. **Conclusion:** an execute–rerun–filter gate is mandatory; generation without it is not a credible design.

### T2. The oracle problem: code-derived tests encode current behaviour. **Confidence: high for the mechanism at unit level; medium for transfer to E2E.**

- Two independent unit-level studies [A2-C5, A3-C14], plus Meta's own statement that filtered tests are regression-only [A2-C3].
- Mitigation evidence: supplying a spec or intent reduces bug-encoding [A2-C6, A3-C13].
- **Conflict:** none on direction. The gap is that no E2E-level study exists.
- **Implication (H3):** stands. Every assertion needs a provenance tag, and spec-vs-code disagreements are the tool's only bug-finding channel.

### T3. Comprehension must be agentic and sliced, fed by deterministic facts. **Confidence: medium-high.**

- Long-context degradation is shown by 4 independent publishers [A3-C1].
- Structural indexes help agents (RepoGraph +32.8%; Aider repo map) [A3-C7].
- A hybrid of static extraction plus LLM refinement reached F1 91.25% on Vue SPAs [A3-C9, single preprint].
- Static GUI models are unsound and must be confirmed at runtime [A3-C8, 2 sources].
- **Regroup check (H5 test):** the route graph is statically extractable: flat, enum literals, no conditionally registered screens [I2]. Role behaviour lives inside screens (81 checks in 24 files) and the entry route is decided at runtime [I3, I4]. **H5 partly confirmed:** static extraction gives the screen set, callables, collections and rules; role-conditional behaviour needs LLM reading per screen plus runtime confirmation.
- Correction: A3-C10 guessed the dynamic v6 API → the target's JSX is still dynamic-API, but flat and literal, so the AST extraction is easy. A3-C10's "must recover from JSX/AST" holds; its difficulty prediction was too pessimistic for regroup.
- **Contested:** A3-C4 (Claude Code abandoned RAG for agentic grep) is second-hand from a blog. It is a different question from deterministic structure (embeddings, not graphs), so there's no conflict with A3-C7. Keep it as low-medium.

### T4. The backend harness is where the reference project failed; most of it is mechanically fixable. **Confidence: high for doc facts; medium for diagnoses.**

- Silent production fallback unless a `demo-` project ID is used [A4-C2, C3]; namespace-by-project-ID [A4-C4] matches L11 exactly.
- Scheduled functions don't run on cron in the emulator; they need the Pub/Sub emulator and a publish to `firebase-schedule-<name>` [A4-C6, from source code]. Regroup has 6 scheduled jobs [I8], so that applies directly.
- Triggers can be dropped silently (firebase-tools 15.30.1) [A4-C7]; there are no retries, and IAM and indexes are not enforced [A4-C8, C10].
- Triggers can be disabled during seeding via undocumented Hub endpoints [A4-C12, source only, so medium on API stability]; REST reset and OOB codes are confirmed (E164, corrected URL).
- Stripe officially recommends mocks for Checkout and Payment Element automation [A4-C20]; PaymentSheet has known Detox fragility [A4-C24]. Regroup's operator checkout is on the web, and resident rent goes through PaymentSheet [I11].
- FCM is not emulated (inferred from absence on the product list) [A4-C1].
- **H2 assessment:** strongly supported for regroup: L5–L13 and I14–I15 show harness problems blocked every run, and the missing seed script means even the June harness can't be reproduced. External: no source measures harness vs authoring effort in general. **H2 stands for Firebase+RN, but as an inference, not a measured law** (medium).

### T5. Runtime choice: genuine conflict, unresolved pending D3.

- Maestro: the best agent tooling (official MCP, live hierarchy, inline YAML, durable flows) [A1-C1, A5-C8]; EAS Workflows' documented path [A1-C21]; but a documented iOS driver failure class [A1-C2, C3] and the `inputText` dropped-character bug [A1-C4]; refuses physical iOS as of 2.11.0 [A1-C5].
- Detox: gray-box idle sync removes timing flakes [A1-C10]; breaks on never-idle screens [A1-C11, partial evidence]; officially supports RN 0.77–0.84, with 0.72 needing a pinned old release [A1-C12]. Regroup has 9 `onSnapshot` listeners, React Query `refetchInterval`s, and an offline queue [I12], which are exactly the never-idle risk.
- Neither side has independent flakiness data [A1-C9]. Device-cloud support favours Appium or BrowserStack; Test Lab and Device Farm list neither [A1-C20].
- **Working synthesis (to be red-teamed):** separate the _exploration plane_ (Maestro MCP or mobile-mcp, during generation) from the _execution plane_ (a spec rendered to a runner chosen by a local spike). Don't hard-wire the generator to one DSL.

### T6. Runtime agents vs durable scripts. **Confidence: medium-high that durable scripts are the right regression artifact; low for any cost claim.**

- Runtime agents: admitted non-determinism (Firebase) [A5-C3]; ~11–12 s per step, success falling with step count, 1–1.8K tokens per screenshot [A5-C20, 3 sources]; agent verdict accuracy ~60% with poor specificity [A2-C15].
- Convergent industry pattern: AI at authoring and heal time, deterministic replay on the green path [A5-C12, 3 OSS sources; A5-C22].
- **H4 stands** pending D1 counter-evidence. Caveat: vendors on both sides; HN practitioners split [A5-C19].

### T7. Self-healing and repair loops create false greens; guards must be mechanical. **Confidence: high.**

- Reward hacking is documented by Anthropic system cards, METR (30.4% RE-Bench / 0.7% HCAST) and a 2026 preprint [A6-C9, 3 independent].
- Self-greening is named by QA Wolf, Bug0 and Ministry of Testing [A5-C17; the first two are vendors].
- Mitigation guidance: diagnose before patching; independent verification; hook-enforced gates [A5-C18, A6-C11].
- Two angles converge independently (A5 commercial, A6 research) → high.

### T8. Cost and scale of "one command". **Confidence: medium.**

- Multi-agent ~15× chat tokens [A6-C4]; a full harness was ~20× a solo run ($200/6 h vs $9/20 min) [A6-C7, single example]; coding parallelizes less well than research [A6-C5].
- Regroup's scale: ~76 routes, 52 functions, 26 collections, 4–5 personas [I1, I8, I10]. Wall-clock time and dollar estimates for the generator must be derived (order of magnitude), not cited. Label them as estimates.

### T9. Nothing on the market does code → spec → durable RN suite with Firebase backend assertions. **Confidence: medium-high.**

- A5 landscape of ~20 products: none uses the codebase as primary input, and none asserts Firebase backend state [A5 analyst + gaps]. The closest is the AToMIC/BMW academic Flutter pipeline [A5-C21].
- Octomind's shutdown [A5-C16, medium] → business risk, not technique risk.
- Gaps: Mabl, Testim, Functionize and Rainforest weren't investigated; Autify Genesis is snippet-only. **F5 falsifier not met** on the evidence gathered, with the coverage gap disclosed.

## Conflicts register (→ Limitations unless resolved)

| #   | Conflict                                                                   | Sides                         | Status                                                                                                  |
| --- | -------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| K1  | Durable runtime: Detox vs Maestro YAML                                     | A1 analyst vs A5 analyst      | Pending D3; likely resolution is "exploration plane ≠ execution plane, decided by spike"                |
| K2  | Flakiness percentages per framework                                        | vendor claims only            | Unresolvable; excluded from body                                                                        |
| K3  | Runtime non-determinism: helps vs hurts flakiness                          | HN commenters                 | Unresolved; low-weight                                                                                  |
| K4  | "Zero-flake"/"eliminates flakes" vendor claims                             | Meticulous, QA Wolf, Momentic | Marketing; excluded                                                                                     |
| K5  | ISSTA 2025 abstract says "94% specificity"; body says sensitivity          | within one paper (A2-S15)     | Resolved: use body numbers                                                                              |
| K6  | A3-C10 predicted a hard dynamic route graph; regroup's is flat and literal | A3 inference vs I2            | Resolved for regroup; general claim stays (other RN apps vary)                                          |
| K7  | Multi-agent gains for research vs warning about coding                     | same Anthropic post           | Not a conflict; scope note: fan-out is justified for read-only per-feature comprehension, not for edits |

## Outline refinement (4.5)

- **F1/F7 merge risk:** F1 (runtime) can't be written until D3 lands. Draft F2, F3, F4, F6 first.
- **New finding to surface:** the regroup inventory exposed latent defects (deep-link config not wired, likely rules gaps on 6 collections, missing seed script, Detox scripts with no config) [I5, I10, I14, I15]. This is evidence for the novel "comprehension pass as a bug-finding by-product" idea (F8). It should go in the regroup case section as illustration, not as a general claim.
- **Gap queue (beyond D1–D3):** none added. Mabl/Testim/Functionize/Rainforest stay a disclosed gap (low expected value: web-first, no codebase input).
