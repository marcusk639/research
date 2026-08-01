# Research Prompt — Optimal Operating System for a Solo AI/Automation Consultant

> **How to use:** paste everything inside the `<prompt>` block below into a dynamic-workflow deep
> research skill (e.g. `/deep-research`, `/research`, or a `Workflow`-driven fan-out). It is
> harness-agnostic: the `<workstreams>` section is written so each item can be dispatched to an
> independent research agent in parallel, and `<synthesis>` defines the barrier where results merge.

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

<objective>
Determine the optimal operating system — one default workflow plus a small, named set of
variants — for a solo consultant who simultaneously runs several client projects, using AI
coding and research harnesses (Claude Code, OpenAI Codex, Cursor, OpenRouter-routed models,
Hermes-style agent scaffolds, and any tool the research surfaces as superior).

"Optimal" is defined by the operator's constraints in `<operator_profile>`, not by generic
benchmark maximization. The end state is not a survey of tools. It is a **repeatable,
templated set of plans** the operator can apply to client after client, changing perhaps 20%
per engagement while 80% carries over unchanged.
</objective>

<operator_profile>

- **Who:** one person. No team. No one else reviews the output before it reaches a client.
- **Work mix:** several concurrent projects. Some are conventional codebases. Some contain
  little or no code and function purely as knowledge/documentation repositories about a
  subject or client domain. Both kinds must stay internally coherent and mutually in sync.
- **Role scope:** not only an AI/software/automation consultant, but a general business
  consultant who streamlines internal operations. In many engagements, internal process and
  organizational-structure problems must be fixed **before** automation produces any real
  benefit — recommending automation over a broken process is a known failure mode to design
  against.
- **Core recurring demand:** ramp into an unfamiliar business domain fast, reach enough depth
  to correctly pinpoint pain points, and distinguish problems automation can solve from
  problems only process or org change can solve.
- **Desired session topology:** an orchestrator holding shared context across projects within
  one session, optionally delegating individual tasks to subagents, capable of carrying
  complex long-running work to completion without losing project, documentation, code, or
  feature-set cohesion.
- **Quality bar:** intelligent, well-written, well-documented code; TDD-backed; e2e tested;
  as much of the verification loop automated as possible.
- **Hard constraint:** the operator is the only reviewer. Any recommendation that produces
  more output than one person can genuinely understand and vouch for is a net negative,
  regardless of throughput gains.
- **Commercial constraint:** the output must sustain a consulting business — meaning the
  plans must be productizable, estimable, and repeatable, not bespoke each time.
  </operator_profile>

<corpus>
Read every file in `/Users/marcusklein/dev/research/optimal-ai-dev-flow/` before searching the
web, **except `solo-consultant-workflow-optimized.md` (this prompt itself), the entire
`prompts/` subdirectory, and this project's own outputs (`corpus-ledger.md`, `findings/`,
`REPORT.md`, `playbooks/`) if they exist — skip all of those.**
Do not confuse this file with `solo-consultant-workflow.md`, a different document listed below;
the names are similar and their roles are opposite. Treat the corpus as the operator's stated
position and prior art — evidence to be verified, not truth to be repeated.

| File                                      | What it is                                                                                                                                                                                                           | How to treat it                                                                                                                                                                                                                                                     |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `solo-consultant-workflow.md`             | Prior deep-research output (~Jul 2026). Ranked 11 workflows; concludes the Spec-Locked Single Loop + verification gates + 2–3 worktrees beats multi-agent fan-out; argues review capacity is the binding constraint. | **Prior art. Extend and re-verify — do not reproduce.** Re-check its dated figures and its central "multi-agent is oversold for coding" claim against current sources. State explicitly which of its conclusions still hold, which are stale, and which were wrong. |
| `v1.md`                                   | Benchmark/cost comparison: Claude Code Max vs Copilot/Codex vs OpenRouter hybrid; subscription-arbitrage argument.                                                                                                   | Verify benchmark numbers, prices, and context-window claims against primary sources. Many will be stale.                                                                                                                                                            |
| `v2.md`                                   | Argues for decoupled multi-tier execution (frontier model plans, cheap model executes), OpenRouter + Hermes stack, judge-builder loop.                                                                               | Verify. This is the strongest source of the corpus's internal contradiction — see `<contradictions>`.                                                                                                                                                               |
| `workflow-plan.md`, `workflow-plan-v2.md` | Personalized optimization plans built on v1/v2; include live audits of the operator's real repos (recovery-platform, rag-system, cpa-consulting); propose 80/15/5 tier routing and a $80–120/mo blended cost target. | Use for ground truth about the operator's actual repo situation. Treat the cost/routing prescriptions as hypotheses to test.                                                                                                                                        |
| `implementation-plan.md`                  | Executable phase plan derived from workflow-plan-v2 (tier policy in CLAUDE.md, judge-builder loop, CI, OpenRouter).                                                                                                  | Useful as a template for how the operator likes plans structured (phase-gated, self-contained per session, explicit "confirmed facts / known gaps"). Assess whether it was the right plan.                                                                          |
| `android-release-build-plan.md`           | A concrete worked example of the operator's phase-gated planning style applied to a build task.                                                                                                                      | Style reference only; not a subject of the research.                                                                                                                                                                                                                |

Extract from the corpus, before searching: (1) every falsifiable quantitative claim, with the
date it was asserted; (2) every recommendation; (3) every point where two files disagree.
Carry these forward as a checklist that the web research must resolve.
</corpus>

<contradictions>
The corpus disagrees with itself. Adjudicating these is a required deliverable, not an
optional aside. At minimum resolve:

1. **Multi-agent fan-out.** `v2.md`/`workflow-plan-v2.md` propose judge-builder loops and
   multi-model orchestration; `solo-consultant-workflow.md` ranks large multi-agent fan-out
   _last_ and cites vendor guidance that it is a poor fit for interdependent coding work.
   Which is right, under what conditions, and specifically for a one-person reviewer?
2. **Cost architecture.** Flat-rate subscription arbitrage (`v1.md`) vs. tiered
   OpenRouter/open-weight routing at a lower blended cost (`v2.md`). Does tier routing survive
   contact with the coordination overhead, quality loss, and operator attention it costs?
   Under what monthly volume does each win?
3. **Ceremony level.** Heavy spec frameworks (spec-kit, Kiro, PRP) vs. "the dumbest thing that
   works" minimalism. Where is the actual crossover point by task size and project type?
4. **Where the bottleneck is.** Model throughput / subscription caps vs. human review
capacity. Find evidence, not opinion, on where a solo operator's ceiling actually sits and
what raises it.
</contradictions>

<workstreams>
Investigate these in parallel. Each is independently researchable; each must return findings
with citations, an evidence tier per claim, and explicit gaps.

**W1 — Current state of the agentic dev loop.** What has changed since ~July 2026 in Claude
Code, Codex, Cursor, and comparable harnesses: plan mode, hooks, skills, subagents, memory,
worktree support, agent-team/orchestration features, context-window and caching behavior,
pricing and rate limits. Re-verify or refute `solo-consultant-workflow.md`'s ranked list.

**W2 — Multi-project orchestration and shared context.** How practitioners actually run
several projects concurrently: git worktrees vs. separate sessions vs. orchestrator+subagent
topologies vs. worktree managers. Mechanisms for carrying context across projects and sessions
(instruction-file hierarchies, persistent memory, MCP-served project state, session resume,
handoff files). What measurably works vs. what is aspirational. Where cohesion actually breaks
— and what detects the break.

**W3 — Verification: TDD and e2e under agentic development.** Test-first practice when an
agent writes the code; documented failure modes (agents weakening, deleting, or gaming tests);
deterministic gates (pre/post-tool and stop-style hooks, CI) vs. advisory instructions; e2e
tooling for web and mobile; what a _solo_ operator's CI should contain and what it should not;
signals beyond coverage (mutation testing, contract tests, golden files, screenshot diffs);
how to make the loop unattended-safe.

**W4 — Documentation and knowledge-repo coherence.** Keeping docs true to code, and keeping
code-free knowledge repositories accurate, navigable, and non-contradictory as they grow.
Look for: doc-drift detection, docs-as-source-of-truth patterns, generated vs. hand-written
doc boundaries, index/ontology conventions, citation and fact verification workflows,
retrieval over one's own knowledge base, and cross-repo consistency checking. Explicitly cover
the no-code repository case — most published guidance assumes a codebase.

**W5 — Model routing and cost architecture.** Test the corpus's 80/15/5 tier hypothesis and
the OpenRouter/Hermes stack against current pricing, caching economics, quota mechanics, and
measured quality deltas. Include the hidden costs: routing configuration, debugging
cross-provider failures, prompt portability, and operator attention. Produce a decision rule
keyed to monthly volume and task mix, not a single verdict.

**W6 — Rapid domain ramp-up.** How analysts, consultants, and researchers reach working depth
in an unfamiliar domain fast, and how AI changes that. Cover: structured domain-scan
protocols, regulatory/standards landscape mapping, trade-press and practitioner-source mining,
expert-interview technique and its AI-assisted substitutes, building a durable domain
knowledge base rather than a throwaway summary, and — critically — **calibration**: how to
know whether you actually understand the domain or have merely acquired fluent vocabulary.
Include documented failure modes of AI-assisted domain learning (confident-wrong synthesis,
source monoculture, hallucinated regulation).

**W7 — Diagnosing internal process and org problems before automating.** Established
methodologies worth encoding as repeatable AI-assisted playbooks for small-business internal
operations: value stream mapping, DMAIC/Lean, Theory of Constraints, BPMN and process mining,
SIPOC, RACI and decision-rights mapping, issue trees / MECE structuring, discovery-interview
frameworks, and job/role design. For each: what it produces, how long it takes at SMB scale,
how much of it an AI harness can genuinely do, and where a human must be in the room. Then
answer directly: **what test tells you a process must be fixed before it is automated**, and
what the evidence says about the failure rate and cost of automating a broken process.

**W8 — Productized consulting operations.** How solo consultants convert bespoke work into
repeatable offers: phase-gated engagement structures (discovery → diagnostic → roadmap →
build → handoff), fixed-scope productized services, deliverable templates, pricing and scoping
models, time-boxing, client-data handling and confidentiality (including regulated-data
cases), IP reuse across clients without leaking one client's material into another, and
handoff/enablement so the client can operate what was built. Find the evidence on what
actually makes a solo consulting practice repeatable versus what merely sounds systematic.

**W9 — Composition.** How W1–W8 combine into a single operating system: session and repo
topology, where the dev workflow and the consulting workflow touch, the capacity math for one
reviewer running N projects, and what concretely to build once in the operator's harness
configuration so every future engagement starts pre-equipped.
</workstreams>

<evidence_standards>

- Tier every substantive claim: **A** = primary/vendor documentation, published benchmark,
  peer-reviewed or otherwise methodologically transparent study; **B** = practitioner report
  with real numbers or reproducible detail; **C** = anecdote, blog opinion, or marketing.
  Never present C as A. State the tier inline or in a per-claim column.
- Date every volatile figure (prices, rate limits, benchmark scores, feature availability) and
  mark it explicitly time-stamped rather than permanent.
- Cite inline with a resolvable link for every non-obvious claim.
- Where the corpus asserts something the web cannot confirm, say so and label it
  **UNVERIFIED** — do not quietly drop it and do not quietly promote it.
- Where good evidence simply does not exist, write "no reliable evidence found" and say what
  kind of evidence would settle it. This is a required behavior, not a failure.
- Prefer sources with a stake in being correct over sources with a stake in selling. When a
  vendor is the only source for a claim about its own product, mark it as such.
- Note any recommendation whose evidence base is a single individual's experience.
  </evidence_standards>

<constraints>
- **One reviewer.** Reject or heavily caveat anything that scales output beyond a single
  person's review capacity. Throughput that outruns review is a defect.
- **Subtraction bias.** Prefer removing steps, tools, and configuration over adding them. Any
  recommendation requiring meaningful setup must name the specific bottleneck it removes and
  the signal that indicates the bottleneck is present. If that signal cannot be stated, cut
  the recommendation.
- **No framework fandom.** Recommend patterns and primitives that outlive specific tools;
  where a specific tool is recommended, state what it would be replaced by and what would
  trigger the replacement.
- **Both project kinds.** Every workflow recommendation must be evaluated for code repos
  *and* for code-free knowledge repos, or explicitly scoped to one.
- **Client-safe.** Flag anything with confidentiality, data-residency, regulated-data, or
  third-party-access implications for work performed on client material.
- **Templates over prose.** The final deliverables must be usable as templates. A paragraph
  describing a good discovery process is worth less than a discovery checklist with entry
  criteria, artifacts, time-box, and exit test.
</constraints>

<deliverables>
Produce a single Markdown report at
`/Users/marcusklein/dev/research/optimal-ai-dev-flow/REPORT.md`, with the templated playbooks
split into separate files under `optimal-ai-dev-flow/playbooks/` and linked from the report.

1. **Executive summary** — the recommended operating system in under 400 words, stated as
   decisions, not options.
2. **Corpus reconciliation ledger** — a table of every falsifiable claim extracted from the
   local corpus, with verdict (CONFIRMED / REFUTED / STALE / UNVERIFIED), current value where
   applicable, and citation. Include a dedicated subsection resolving each item in
   `<contradictions>` with a stated decision and the conditions under which the decision flips.
3. **The operating system** — one default workflow, plus named variants for: (a) code project,
   (b) knowledge/documentation project, (c) new-client discovery engagement. Each variant
   specified as phases with entry criteria, activities, artifacts produced, automated gates,
   human checkpoints, and an exit test.
4. **Engagement playbook** — the repeatable client-facing plan: discovery → process diagnosis →
   opportunity ranking → roadmap → build → handoff. Phase-gated, time-boxed, with the
   deliverable template for each phase and an explicit list of what changes per client versus
   what is fixed. This is the commercial core of the report — treat it as such.
5. **Domain ramp-up protocol** — a concrete, repeatable procedure with a calibration test for
   determining whether depth has actually been reached.
6. **Pre-automation process-diagnosis playbook** — including the decision test for "fix the
   process before automating it," and the ranked shortlist of methodologies worth carrying.
7. **Harness blueprint** — what to configure once: repo and directory conventions, instruction
   file structure and size discipline, the minimal hook set, the minimal subagent roster, the
   minimal skill set, CI contents, and the cross-project context/handoff mechanism. Specify
   the knowledge-repo variant separately. Include what to _delete_ from an existing setup.
8. **Adoption sequence** — staged, with a bottleneck signal that triggers each stage, a
   success benchmark for advancing, and a kill criterion for backing out. No stage may be
   justified by "best practice" alone.
9. **Risk and volatility register** — what is likely to change within 6 months, what the
   recommendation depends on that could break, and which claims are anecdote-grade.
10. **Open questions** — what could not be resolved, and the cheapest experiment that would
    resolve each.
11. **Sources** — full list, tiered, each with a one-line note on why it was trusted.
</deliverables>

<synthesis>
After the parallel workstreams return, before writing: run a reconciliation pass that
(a) merges duplicate findings, (b) surfaces every place two workstreams disagree and resolves
it explicitly rather than averaging, and (c) adversarially challenges the top three
recommendations — for each, construct the strongest case that it is wrong for this operator,
then either defeat that case with evidence or weaken the recommendation. Report the surviving
counterarguments; do not delete them.
</synthesis>

<acceptance_criteria>
The report is finished only when all of the following are true. Check each explicitly before
delivering.

- [ ] Every file in the corpus directory was read in full, and every falsifiable claim from it
      appears in the reconciliation ledger with a verdict.
- [ ] All four items in `<contradictions>` have a stated decision plus flip conditions.
- [ ] Both project kinds — code and knowledge-only — are addressed everywhere a workflow is
      recommended.
- [ ] The consulting half (W6, W7, W8) is developed to the same depth as the dev half. A
      report that is strong on tooling and thin on engagement methodology has failed.
- [ ] Every playbook has entry criteria, artifacts, a time-box, and an exit test.
- [ ] Every quantitative claim carries a date, a source link, and an evidence tier.
- [ ] The adoption sequence has a kill criterion for every stage.
- [ ] At least three surviving counterarguments to the main recommendations are reported.
- [ ] Nothing recommended exceeds what one person can review, or it is flagged where it does.
      </acceptance_criteria>

<tone>
Write for a practitioner who will act on this next week. Direct, specific, quantified.
No hedging filler, no "it depends" without immediately saying what it depends on, no
enthusiasm about tools. Where you recommend, recommend — and name the condition under which
you would recommend otherwise.
</tone>

</prompt>

---

## Techniques applied (why the prompt is built this way)

| Technique                                                   | Where                   | Purpose                                                                                                                                  |
| ----------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Role assignment                                             | `<role>`                | Forces the dual dev + consulting lens; most failures here come from a purely engineering framing that under-serves W6–W8.                |
| Explicit corpus grounding with a per-file disposition table | `<corpus>`              | Prevents the research from re-deriving `solo-consultant-workflow.md` and prevents it from repeating stale v1/v2 figures as fact.         |
| Contradiction adjudication as a required output             | `<contradictions>`      | The corpus disagrees with itself; without naming this, a synthesizer averages the conflict away into mush.                               |
| Task decomposition into parallel workstreams                | `<workstreams>`         | Maps directly onto a fan-out harness — one agent per W, with `<synthesis>` as the merge barrier.                                         |
| Evidence tiering + explicit permission to say "unknown"     | `<evidence_standards>`  | Primary hallucination control. The domain is thick with vendor marketing and single-anecdote productivity claims.                        |
| Negative constraints / subtraction bias                     | `<constraints>`         | Counteracts the strong default pull toward recommending elaborate machinery — which the corpus itself identifies as a real failure mode. |
| Output format specification with file paths                 | `<deliverables>`        | Makes the result templates rather than prose, and lands it in the research-repo convention (`REPORT.md` per subject).                    |
| Adversarial self-challenge before writing                   | `<synthesis>`           | Cheap accuracy gain; surviving counterarguments are more useful to you than a clean verdict.                                             |
| Machine-checkable acceptance checklist                      | `<acceptance_criteria>` | Gives the agent a verification target instead of a vibe, and specifically guards the consulting half from being shortchanged.            |

## Assumptions made

- Output lands at `optimal-ai-dev-flow/REPORT.md` per this repo's subject convention, with
  playbooks in a `playbooks/` subdirectory. Change the paths in `<deliverables>` if you want
  them elsewhere.
- The prompt is harness-agnostic. If you drive it with the `Workflow` tool, dispatch W1–W9 as
  the fan-out stage and `<synthesis>` as the barrier; if you use a `/deep-research`-style
  skill, `<workstreams>` supplies its sub-questions directly.
- `solo-consultant-workflow.md` is treated as prior art to extend, not redo — it is currently
  untracked in git and is the newest and strongest doc in the corpus.
