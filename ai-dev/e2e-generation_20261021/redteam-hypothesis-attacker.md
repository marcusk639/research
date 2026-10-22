# Red-team — Hypothesis Attacker (persona 4), 2026-10-21

Independent verifier agent, fresh context. Summary of verdicts as returned (full reasoning preserved below).

| H | Verdict | Corrected wording | Design decision affected |
| - | ------- | ----------------- | ------------------------ |
| H1 | STANDS (ceiling) / WEAKEN (gate placement) | "One-shot unattended is unrealistic. One-command to a reviewable bundle is realistic. The required human step is acceptance/triage of produced artifacts. Whether a pre-generation spec gate pays for its review cost is untested. Comprehensiveness is only measurable against an inventory the LLM didn't produce." | Make the Phase 5 pre-generation spec gate optional; A/B test it on the disputes slice; measure coverage against the Phase 1 inventory, not the LLM-built model |
| H2 | WEAKEN | "For brownfield RN+Firebase+payments, harness repair dominates *bring-up* effort; recurring cost is unmeasured, and general UI-flake evidence points to timing and script logic." | Weight idle-sync and flake behaviour on listener-heavy screens in the runner spike; treat "timing" as a main recurring cost in Phase 7 |
| H3 | WEAKEN (narrow) | "Oracles derived from a single code path bless current behaviour; oracles mined from disagreements between independent artifacts (rules vs client writes, web vs mobile, sibling paths, docs vs code) can surface bugs with no human intent, at ~30% precision, so triage is mandatory." | Add a `cross-artifact` provenance tag; populate `disagreements.md` automatically from inconsistency mining in Phases 1 and 3 |
| H4 | STANDS (clarified) | "Deterministic assertions and recorded actions are the regression artifact; AI may propose locator repairs, but only as reviewed diffs, never at CI runtime." | None |
| H5 | WEAKEN | "Extraction is essential for inventory completeness and cost, and gives modest, benchmark-dependent comprehension gains, largest on multi-hop dependency questions and with cheaper models." | Pass each Phase 3 subagent its inventory slice as structured context; consider a cheaper model tier |

**Simpler-design challenge, judged fairly by the persona.** A pure Maestro-MCP explore-and-save design is roughly what regroup already tried [L4, L5], and it failed on harness problems. The middle design delivers most of the value at lower complexity: Phases 0, 1, 4, 7 and 8, the guards, the rules oracle, and backend helpers, but *without* the flow-model YAML and path enumeration. Defer the flow model until the disputes slice shows gaps that the inventory checklist misses.

**New sources the persona fetched** (not in sources.jsonl; two PDF-text checked, the rest summarizer figures):

- Romano et al., ICSE 2021, arXiv 2103.02669 (PDF-checked): 83 mobile flaky UI tests. Async Wait 27 (32.5%), Environment 19 (22.9%), Test Runner API misuse 17 (20.5%), Test Script Logic 20 (24.1%).
- LocAgent, ACL 2025, arXiv 2503.09089 (PDF-checked): function Acc@10 77.37 vs 70.07 (OpenHands) and 64.60 (SWE-agent) on SWE-bench Lite. On LocBench, 59.29 vs 59.11. Ablation without TraverseGraph: 71.53 → 66.06.
- TESSARA, arXiv 2610.25601: 51.9–59.3% oracle satisfaction; 59.8–78.2% script executability (summarizer figures).
- "Building to the Test", arXiv 2606.28430: agents with the oracle in the loop scored 221–222 of 222 by gaming it, vs 148–189 without (summarizer figures).
- Chiral analysis, arXiv 2607.17987: 13 real issues from 44 validator positives (~30% precision; summarizer figure; smart contracts).
- ReproBreak, arXiv 2605.12158: 449 locator breaks in 4 projects with no functional change (summarizer figure).
