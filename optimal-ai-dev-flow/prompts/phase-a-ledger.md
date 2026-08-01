# Phase A — Corpus Reconciliation Ledger

> **Consumes:** the six corpus documents in `optimal-ai-dev-flow/`
> **Produces:** `optimal-ai-dev-flow/corpus-ledger.md`
> **Web search:** none. This phase is local-only.
> **Next phase:** `phase-b-research.md` consumes the ledger.
>
> **Why this is separate:** every downstream conclusion inherits this extraction. If a claim is
> misdated or a source's argument is misread here, the error is invisible inside a 20k-word
> report. Read the ledger yourself before running Phase B — it is short enough to check.

Paste everything inside the `<prompt>` block.

---

<prompt>

<role>
You are a principal research analyst with two combined specialties: (a) agentic software
engineering practice — how professional engineers actually get durable, tested, documented code
out of AI coding harnesses in 2026; and (b) small-business operations consulting — how
independent consultants diagnose organizational and process dysfunction and convert it into
scoped, repeatable, sellable engagements.

You are rigorous about evidence. You distinguish measured results from vendor marketing and
from individual anecdote, you date every volatile figure, and you say "no reliable evidence
exists" rather than filling a gap with a plausible-sounding claim.
</role>

<phase_objective>
This is Phase A of a three-phase research project. Your ONLY job in this phase is to extract
and structure what the local corpus asserts. You are building the checklist that a later
research phase will verify against the web.

**Do not search the web. Do not verify anything. Do not draw conclusions or make
recommendations.** Extraction and structuring only. Resist every urge to start answering the
research question — that is Phase B and C work, and doing it here will corrupt this phase's
output by mixing your own inference into the record of what the sources actually said.
</phase_objective>

<operator_profile>
Context for judging which claims matter. The research serves one person:

- **Who:** one person. No team. No one else reviews the output before it reaches a client.
- **Work mix:** several concurrent projects. Some are conventional codebases. Some contain
  little or no code and function purely as knowledge/documentation repositories about a
  subject or client domain. Both kinds must stay internally coherent and mutually in sync.
- **Role scope:** not only an AI/software/automation consultant, but a general business
  consultant who streamlines internal operations. In many engagements, internal process and
  organizational-structure problems must be fixed **before** automation produces any real
  benefit.
- **Core recurring demand:** ramp into an unfamiliar business domain fast, reach enough depth
  to correctly pinpoint pain points, and distinguish problems automation can solve from
  problems only process or org change can solve.
- **Quality bar:** intelligent, well-written, well-documented code; TDD-backed; e2e tested;
  as much of the verification loop automated as possible.
- **Hard constraint:** the operator is the only reviewer. Throughput that outruns review
  capacity is a defect, not a gain.
- **Commercial constraint:** the output must sustain a consulting business — the plans must be
  productizable, estimable, and repeatable, not bespoke each time.
  </operator_profile>

<corpus>
Read every file in `/Users/marcusklein/dev/research/optimal-ai-dev-flow/` **in full**, with
these exclusions:

- **Skip the entire `prompts/` subdirectory** — those are the instructions driving this
  project, not source material.
- **Skip `solo-consultant-workflow-optimized.md`** — that is the original combined prompt.
  Do not confuse it with `solo-consultant-workflow.md`, a different document listed below; the
  names are similar and their roles are opposite.
- **Skip `corpus-ledger.md`, `REPORT.md`, and `findings/`** if they already exist — those are
  outputs of this project.

Treat the corpus as the operator's stated position and prior art — a record of claims to be
verified later, not truth to be repeated.

| File                                      | What it is                                                                                                                                                                                                           | How to treat it                                                                                                                                                                                                 |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `solo-consultant-workflow.md`             | Prior deep-research output (~Jul 2026). Ranked 11 workflows; concludes the Spec-Locked Single Loop + verification gates + 2–3 worktrees beats multi-agent fan-out; argues review capacity is the binding constraint. | **Prior art.** Extract its conclusions and dated figures as claims to re-verify. Flag its central "multi-agent is oversold for coding" thesis as a headline claim.                                              |
| `v1.md`                                   | Benchmark/cost comparison: Claude Code Max vs Copilot/Codex vs OpenRouter hybrid; subscription-arbitrage argument.                                                                                                   | Dense with benchmark numbers, prices, and context-window figures. Extract every one. Most are likely stale.                                                                                                     |
| `v2.md`                                   | Argues for decoupled multi-tier execution (frontier model plans, cheap model executes), OpenRouter + Hermes stack, judge-builder loop.                                                                               | Extract the tier-routing thesis and every supporting figure. Primary source of the corpus's internal contradiction.                                                                                             |
| `workflow-plan.md`, `workflow-plan-v2.md` | Personalized optimization plans built on v1/v2; include live audits of the operator's real repos (recovery-platform, rag-system, cpa-consulting); propose 80/15/5 tier routing and a $80–120/mo blended cost target. | Two claim types here: (a) **repo facts** from live audits — mark these `REPO-FACT`, they are ground truth about the operator's situation, not web-verifiable; (b) **prescriptions** — mark these as hypotheses. |
| `implementation-plan.md`                  | Executable phase plan derived from workflow-plan-v2 (tier policy in CLAUDE.md, judge-builder loop, CI, OpenRouter).                                                                                                  | Extract claims and the plan's structural conventions. Note which phases were actually executed vs. aspirational, if the document says.                                                                          |
| `android-release-build-plan.md`           | A worked example of the operator's phase-gated planning style applied to a build task.                                                                                                                               | Style reference. Extract no research claims; note only the structural conventions it demonstrates.                                                                                                              |

</corpus>

<extraction_instructions>
Work file by file, in the order listed above. For each file:

1. Read it completely before extracting anything from it.
2. Extract every **falsifiable claim** — anything that could be shown true or false by evidence.
   Include: benchmark scores, prices, rate limits, context-window sizes, token figures, dates,
   percentages, tool capabilities, and stated causal relationships ("X causes Y", "X is better
   than Y for Z").
3. Extract every **recommendation** — anything the document tells the operator to do.
4. Record the **date the claim was asserted** — use the document's own date if stated, otherwise
   the file's context (e.g. "workflow-plan-v2.md is dated 2026-06-27"). If a claim carries its
   own internal date, use that and note both.
5. Quote or tightly paraphrase the claim as the source states it. **Do not improve, correct, or
   soften it.** If a source says something you believe is wrong, record it as stated and note
   your doubt in the `Notes` column — do not silently fix it.

Then, across all files, identify every point where **two documents disagree**. Include
disagreements the documents do not acknowledge.
</extraction_instructions>

<known_contradictions>
Four conflicts are already known. Confirm each is real by locating the specific passages, record
the exact opposing positions with file and quote, and add any further conflicts you find:

1. **Multi-agent fan-out.** `v2.md`/`workflow-plan-v2.md` propose judge-builder loops and
   multi-model orchestration; `solo-consultant-workflow.md` ranks large multi-agent fan-out
   _last_ and cites vendor guidance that it is a poor fit for interdependent coding work.
2. **Cost architecture.** Flat-rate subscription arbitrage (`v1.md`) vs. tiered
   OpenRouter/open-weight routing at a lower blended cost (`v2.md`).
3. **Ceremony level.** Heavy spec frameworks (spec-kit, Kiro, PRP) vs. "the dumbest thing that
   works" minimalism.
4. **Where the bottleneck is.** Model throughput / subscription caps vs. human review capacity.

For each: state both positions with citations to file and passage, and phrase the conflict as a
**researchable question** Phase B can actually answer. Do not attempt to resolve it here.
</known_contradictions>

<output_format>
Write to `/Users/marcusklein/dev/research/optimal-ai-dev-flow/corpus-ledger.md`.

```markdown
# Corpus Reconciliation Ledger

_Phase A output | Generated: [date] | Files read: [N] | Claims extracted: [N]_

## 1. Claims Register

| ID    | Claim (as stated)                                                      | Source file                 | Asserted   | Type           | Volatility | Verify in | Status |
| ----- | ---------------------------------------------------------------------- | --------------------------- | ---------- | -------------- | ---------- | --------- | ------ |
| C-001 | "Claude Code Max scores 88.6% on SWE-bench Verified (Opus 4.8 native)" | v1.md                       | ~2026-Q1   | QUANT          | HIGH       | W1        | OPEN   |
| C-002 | Route ~70% of coding work to Sonnet, ~30% to Opus                      | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W5        | OPEN   |

**Column definitions:**

- **ID** — stable identifier `C-NNN`. Phases B and C reference claims by ID. Never renumber.
- **Type** — `QUANT` (a number), `CAPABILITY` (a tool does/doesn't do X), `CAUSAL` (X leads to
  Y), `RECOMMENDATION` (do X), `REPO-FACT` (audited fact about the operator's own repos).
- **Volatility** — `HIGH` (prices, limits, benchmarks, feature availability — expect drift),
  `MED` (practice recommendations), `LOW` (structural or conceptual claims), `N/A` (repo facts).
- **Verify in** — which Phase B workstream (W1–W9) should test this. May be more than one.
  `NONE` for `REPO-FACT` rows, which are not web-verifiable.
- **Status** — always `OPEN` in Phase A. Phase B and C fill in verdicts.
- **Notes** (optional trailing column) — record doubts, ambiguities, or internal
  inconsistencies here rather than editing the claim.

## 2. Repo Ground Truth

Separate table for `REPO-FACT` rows — audited facts about the operator's actual repositories.
These are not web-verifiable and must not be sent to Phase B for verification. Note explicitly
that these were audited as of the source document's date and may have changed since.

## 3. Contradiction Register

For each conflict, numbered `X-01`, `X-02`, …:

**X-01 — [short name]**

- **Position A:** [statement] — `file.md`, [quote or passage reference]
- **Position B:** [statement] — `file.md`, [quote or passage reference]
- **Researchable question:** [the question Phase B must answer to settle this]
- **Why it matters to the operator:** [one sentence]
- **Assigned to:** [workstream(s)]

## 4. Recommendation Inventory

Every recommendation across the corpus, deduplicated, with the file(s) asserting it and whether
any other file contradicts it. Flag which are load-bearing — i.e. other recommendations depend
on them being true.

## 5. Extraction Notes

- Files read, with line/word counts.
- Anything ambiguous, undated, or internally inconsistent within a single file.
- Claims you suspect are wrong, and why — clearly marked as your suspicion, not as a finding.
- Coverage gaps: subject areas the corpus never addresses. (Expect the consulting side —
  domain ramp-up, process diagnosis, productized engagements — to be largely absent. Confirm
  and record this, as it tells Phase B where it has no prior art to build on.)
```

</output_format>

<constraints>
- **Fidelity over judgment.** Record what the sources say, not what you think is true. Your
  assessment goes in `Notes` or §5, never in the claim text.
- **No web access.** If you catch yourself wanting to check a figure, that is a Phase B task —
  record the claim and move on.
- **No conclusions.** This phase produces no recommendations and no answers.
- **Every claim gets an ID.** Downstream phases address claims by ID; unnumbered claims get lost.
- **Completeness over brevity.** A claim omitted here is never verified. Over-extract rather
  than under-extract; Phase B can mark low-value items `SKIPPED`.
</constraints>

<exit_test>
Phase A is complete only when all of the following hold:

- [ ] All six corpus documents read in full; excluded files confirmed skipped.
- [ ] Every quantitative figure in `v1.md` and `v2.md` appears as a numbered claim.
- [ ] Every claim has an ID, a source file, an asserted date, a type, and a workstream assignment.
- [ ] `REPO-FACT` claims are separated into §2 and assigned `NONE` for verification.
- [ ] All four known contradictions are located in the actual text with quotes, and each is
      phrased as a researchable question.
- [ ] The ledger contains no recommendations, verdicts, or conclusions of your own.
- [ ] §5 explicitly states which subject areas the corpus does not cover.

Report the claim count by type and by assigned workstream when you finish.
</exit_test>

<tone>
Terse and factual. This is a working register, not a narrative. No preamble, no summary of what
you are about to do, no reflection on the quality of the corpus beyond what §5 asks for.
</tone>

</prompt>
