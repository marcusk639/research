# Phase 6 red-team log and verdict tally

Four independent verifier agents ran in fresh contexts on 2026-10-21. Personas: A = Adversarial Reviewer, Q = Source-Quality Auditor, S = Domain Skeptic. **2-of-3 kill rule over A/Q/S**; the Hypothesis Attacker (H) ruled on H1–H5 separately. The main session independently re-verified every REFUTE before acting on it.

| ID  | A | Q | S | Outcome | Main-session verification / action |
| --- | - | - | - | ------- | ---------------------------------- |
| R1  | N | N | N | Narrowed | "Among products surveyed" |
| R2  | N | S | S | Stands | Confidence lowered to medium-high |
| R3  | N | N | N | Narrowed | Per-class metric; unit vs E2E split |
| R4  | **R** | N | **R** | **Refuted clause removed** | Implicit oracles found regroup bugs [L8]; "only bug channel" removed |
| R5  | S | N | S | Stands | Quote re-attributed to S151 (verified) |
| R6  | N | N | N | Narrowed | Inference labelled; cross-feature pass added |
| R7  | **R** | N | N | Narrowed and rewritten | S174 re-read: within-harness localization and resolve gains verified; S214 ablation added |
| R8  | S | S | S | Stands | Edges noted as runtime-only |
| R9  | N | N | N | Narrowed | Reframed per-service; regroup Functions not routed to emulator (I21, verified) |
| R10 | S | S | S | Stands | Cite S86 only; "no cron" labelled inference |
| R11 | N | S | S | Stands | Web Checkout/Payment Element scope noted |
| R12 | N | N | N | Narrowed | App bugs and authoring defects included |
| R13 | N | N | N | Narrowed | Intermittent; per-flow limits loss; M8/M9 workarounds (verified) |
| R14 | **R** | N | **R** | **Refuted, rewritten** | Regroup ran Maestro 2.6.0 with startup-class failures (verified in handoff doc); decide in spike |
| R15 | S | N | S | Stands | Fabricated "best effort" quote replaced with "we do our best" (verified in S13) |
| R16 | S | S | N | Stands | Two-toolchain cost added |
| R17 | N | N | S | Narrowed | Web-only; averages; Duolingo statements split |
| R18 | N | N | N | Narrowed | o3-specific; "self greening" attributed to one glossary |
| R19 | S | S | **R** | Survives the vote; **narrowed on new primary evidence** | Firebase MCP prompt verified (S213); novelty narrowed to rules × code-access × persona cross-check for app E2E |
| R20 | N | N | N | Narrowed | Stryker command runner noted |
| R21 | N | N | N | Narrowed | Token figure dropped; 17–33 device-hours at the 10-rerun bar |
| R22 | N | N | **R** | Narrowed | L14 false (I22, verified); chores > disputes; serial lane and backdated fixtures needed |
| R23 | N | N | N | Narrowed | Five written plus one read (verified) |
| R24 | S | S | S | Stands | Node/OpenSSL caveat added |

**Totals:** 2 claims had a refuted clause or conclusion by majority (R4, R14). 15 were narrowed. 7 stand. No claim was removed entirely. Every refuted or narrowed item is corrected in report v2, and the residual disagreements are recorded in Limitations.

**Hypothesis Attacker:** no hypothesis refuted. H2, H3 and H5 weakened; H1 standing but gate placement weakened; H4 standing. These are applied to §8 in v2.

**Methodology finding adopted:** quote fidelity ≠ claim fidelity. v2 adds a "claim-interpretation check" for every load-bearing claim (direction, subject, unit), which caught S30, S44, S56, S62, S148 and S174.

**Round 2:** a targeted re-check of the changed sections is recorded at the end of report v2's Methodology Appendix.
