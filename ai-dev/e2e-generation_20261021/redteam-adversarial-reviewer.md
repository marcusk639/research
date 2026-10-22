# Red-team — Adversarial Reviewer (persona 1), 2026-10-21

Independent verifier agent, fresh context. The reviewer re-checked S30, S44, S76/S77, S85/S86, S99, S13, S112, S141, S146, S148, S161, S174, S178–S180 and S50 against the raw cache or live pages, re-read #3538 through the live GitHub API, and read regroup's reports and source.

| ID | Verdict | Key reason |
| -- | ------- | ---------- |
| R1 | NARROW | Absence claim from a partial survey; must say "among those surveyed" |
| R2 | NARROW | Confidence should be medium-high; no study tests one-shot generation on RN |
| R3 | NARROW | S30's figures are per-class "at least one test"; S50 shows 60% usable as generated, so "mostly unusable" overstates it |
| R4 | REFUTE (last clause) | "Only bug channel" is contradicted by L8 (smoke runs found app bugs) and by implicit oracles (S32, S161) |
| R5 | STANDS | |
| R6 | NARROW | "Right strategy" is an inference; 212k LOC wouldn't fit in one context at all |
| R7 | REFUTE | S174 misread: within-harness, the index gave large localization and resolve gains at lower cost. Evidence is mixed |
| R8 | STANDS | Spot-check: 76 route values; 72 role checks in 20 screen files |
| R9 | NARROW | Sources don't say "silently"; non-emulated products talk to production; L10 shows callables failing, not reaching production |
| R10 | STANDS | Verified in S86 source; label "no cron" as an inference |
| R11 | NARROW | S99 doesn't say "for CI" and covers web Checkout/Payment Element, not native PaymentSheet |
| R12 | NARROW | Blockers included app launch bugs and testID gaps, not only harness problems |
| R13 | NARROW | Intermittent (~1.5% per driver launch in one report). Per-flow invocation limits loss to 1–2 flows. A fixed-port reuse setup has one positive CI report (2026-10-16 comment) |
| R14 | REFUTE (for regroup) | Regroup ran Maestro 2.6.0 with startup-failure symptoms, a different class from #3538 (2.8.0+, mid-run). `run-all.yaml` may reduce exposure to regroup's observed failure |
| R15 | STANDS | |
| R16 | STANDS | The spike must test current Maestro; thresholds are defaults |
| R17 | NARROW | S44 is web-only; "go rogue" and "work around" are separate statements in S171 |
| R18 | NARROW | METR's 30.4% is o3 on RE-Bench with a visible scorer; the 3.7 card says "occasionally" |
| R19 | STANDS | But §8 lists rules-oracle generation as "automated with confidence", which contradicts this |
| R20 | NARROW | StrykerJS's command runner can drive a device runner by exit code (full suite per mutant, so impractical) |
| R21 | NARROW | Cost unanchored; reruns inconsistent (5 vs 10 vs 20); 20 features uncited; 8–33 device-hours |
| R22 | NARROW | Chores (100) outranks disputes (91) in doc mentions; "two personas" uncited |
| R23 | NARROW | Five written plus one read-only (`paywall/config`); under repo rules the kill-switch read is denied and the gate fails closed |
| R24 | STANDS | Node-version caveat: Angular 9 `ng serve` needs old Node; Playwright needs Node 18+ |

Additional problems flagged:

1. The Executive Summary conflates the #3538 crash with its blast radius. Add the 2026-10-16 fixed-port comment as M8.
2. Regroup's attribution to #3538 is weaker than stated (2.6.0, startup failures).
3. **Quote fidelity is not claim fidelity.** S174 (direction inverted), S148 (o3 omitted) and S30 (per-class) passed the verbatim checks but were misread.
4. The §4 silent-fallback framing contradicts L10.
5. The §6 Duolingo sentence merges two separate statements.
6. The §8 automation ceiling contradicts the "promising" and open-bug labels.
7. S89 is closed (fixed in #11097).
8. §2's "similar shrinkage" is not similar.
