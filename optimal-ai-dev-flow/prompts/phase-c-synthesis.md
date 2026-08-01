# Phase C — Synthesis, Adversarial Review, and Deliverables

> **Consumes:** `optimal-ai-dev-flow/corpus-ledger.md` (Phase A) + `optimal-ai-dev-flow/findings/w1..w9-*.md` (Phase B)
> **Produces:** `optimal-ai-dev-flow/REPORT.md` + `optimal-ai-dev-flow/playbooks/*.md`
> **Web search:** only to close a specific gap that blocks a deliverable. This is a writing phase.
>
> **Split trigger:** if the playbooks come back as prose paragraphs rather than filled templates
> with all four required fields (entry criteria, artifacts, time-box, exit test), re-run this
> phase in two passes — C1 for deliverables 1–3 and 8–11, C2 for the playbooks (4–7) with the
> C1 output as input. Do not pre-split on speculation; split on that observed symptom.

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
This is Phase C, the final phase. Phase A recorded what the local corpus claims. Phase B tested
those claims and researched the open field. Your job is to reason over that evidence and produce
the deliverables.

The end state is not a survey of tools. It is a **repeatable, templated set of plans** the
operator can apply to client after client, changing perhaps 20% per engagement while 80% carries
over unchanged. Judge every page you write against that: would this still be useful on the
fourth client?

You are permitted to search the web only to close a specific gap that blocks a deliverable. If
you find yourself researching broadly, stop — that means Phase B was incomplete, and you should
say so in Open Questions rather than silently redoing it.
</phase_objective>

<input_contract>
Read, in this order:

1. `corpus-ledger.md` — the claims register, repo ground truth, and contradiction register.
2. Every file in `findings/` — the Phase B evidence.

Where a Phase B finding contradicts the corpus, the finding wins **if its evidence tier is A or
B**. Where a finding is tier C and the corpus disagrees, treat the question as open and say so.

Where two workstreams disagree, resolve it explicitly using evidence tier and recency — do not
average them into a hedge. Record the resolution and the reasoning.

`REPO-FACT` rows in ledger §2 are ground truth about the operator's actual repositories. Use
them to make the recommendations concrete — but note their audit date, and flag any
recommendation that depends on a repo fact that may have changed.
</input_contract>

<operator_profile>
Every recommendation is measured against this profile. It serves one person:

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
- **Commercial constraint:** the output must sustain a consulting business — the plans must be
  productizable, estimable, and repeatable, not bespoke each time.
  </operator_profile>

<synthesis>
Do this before writing anything, and show your work in the report where indicated.

1. **Merge.** Collapse duplicate findings across workstreams into single claims, keeping the
   strongest citation and the highest evidence tier.
2. **Resolve conflicts.** For every place two workstreams disagree, state the disagreement, the
   resolution, and the reasoning. Averaging is prohibited — pick, and say why.
3. **Settle the contradictions.** Each contradiction from ledger §3 gets a stated decision plus
   the conditions under which the decision flips. "It depends" is acceptable only when
   immediately followed by what it depends on and the threshold value.
4. **Adversarially challenge the top three recommendations.** For each: construct the strongest
   case that it is wrong for this operator specifically — not a generic caveat. Then either
   defeat that case with cited evidence or weaken the recommendation to survive it. **Report the
   surviving counterarguments in the final report; do not delete them.** A recommendation that
   survived a real attack is worth more to the reader than one that was never tested.
5. **Check the consulting/dev balance.** Before writing, confirm the engagement methodology
(W6–W8) has as much substance behind it as the tooling (W1–W5). If it does not, the report
is not ready — say so and stop rather than shipping a tooling report with a thin consulting
appendix.
</synthesis>

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
- **Templates over prose.** A paragraph describing a good discovery process is worth less than
  a discovery checklist with entry criteria, artifacts, time-box, and exit test. When you catch
  yourself writing explanatory prose inside a playbook, convert it to a table, checklist, or
  template.
- **Cite forward.** Every substantive claim in the report carries its evidence tier and source
  from Phase B. Do not launder a tier-C finding into an unqualified assertion.
</constraints>

<deliverables>
Main report at `/Users/marcusklein/dev/research/optimal-ai-dev-flow/REPORT.md`. Playbooks as
separate files under `optimal-ai-dev-flow/playbooks/`, linked from the report.

**In `REPORT.md`:**

1. **Executive summary** — the recommended operating system in under 400 words, stated as
   decisions, not options.
2. **Corpus reconciliation ledger** — the Phase A claims register with Phase B verdicts merged
   in: claim, source, asserted date, verdict, current value, citation. Plus a subsection
   resolving each contradiction with a stated decision and flip conditions.
3. **The operating system** — one default workflow, plus named variants for: (a) code project,
   (b) knowledge/documentation project, (c) new-client discovery engagement. Each variant
   specified as phases with entry criteria, activities, artifacts produced, automated gates,
   human checkpoints, and an exit test.
4. **Adoption sequence** — staged, with a bottleneck signal that triggers each stage, a
   success benchmark for advancing, and a kill criterion for backing out. No stage may be
   justified by "best practice" alone.
5. **Risk and volatility register** — what is likely to change within 6 months, what the
   recommendation depends on that could break, and which claims are anecdote-grade.
6. **Open questions** — what could not be resolved, and the cheapest experiment that would
   resolve each. Include anything Phase B left underdone.
7. **Sources** — full list, tiered, each with a one-line note on why it was trusted.

Also include a short **Surviving Counterarguments** section carrying the output of
`<synthesis>` step 4.

**As separate files in `playbooks/`:**

4. `playbooks/engagement-playbook.md` — the repeatable client-facing plan: discovery → process
   diagnosis → opportunity ranking → roadmap → build → handoff. Phase-gated, time-boxed, with
   the deliverable template for each phase and an explicit list of what changes per client
   versus what is fixed. **This is the commercial core — treat it as the most important
   artifact in the project, not an appendix.**
5. `playbooks/domain-rampup.md` — a concrete, repeatable procedure for reaching working depth
   in an unfamiliar domain, with a calibration test for determining whether depth has actually
   been reached rather than merely fluent vocabulary.
6. `playbooks/process-diagnosis.md` — the pre-automation playbook, including the decision test
   for "fix the process before automating it," and the ranked shortlist of methodologies worth
   carrying from engagement to engagement.
7. `playbooks/harness-blueprint.md` — what to configure once: repo and directory conventions,
   instruction file structure and size discipline, the minimal hook set, the minimal subagent
   roster, the minimal skill set, CI contents, and the cross-project context/handoff mechanism.
   Specify the knowledge-repo variant separately. Include an explicit **what to delete** section
   for an existing setup.

**Every playbook must contain, for every phase it defines:** entry criteria, activities,
artifacts produced, time-box, human checkpoints, and an exit test. A playbook phase missing any
of these is incomplete.
</deliverables>

<acceptance_criteria>
The report is finished only when all of the following are true. Check each explicitly and report
the results before delivering.

- [ ] Every claim in the Phase A ledger appears in the reconciliation ledger with a verdict.
- [ ] All contradictions from ledger §3 have a stated decision plus flip conditions.
- [ ] Both project kinds — code and knowledge-only — are addressed everywhere a workflow is
      recommended.
- [ ] The consulting half (W6, W7, W8 → playbooks 4, 5, 6) is developed to the same depth as
      the dev half. A report strong on tooling and thin on engagement methodology has failed.
- [ ] Every playbook phase has entry criteria, artifacts, a time-box, and an exit test.
- [ ] Every quantitative claim carries a date, a source link, and an evidence tier.
- [ ] The adoption sequence has a kill criterion for every stage.
- [ ] At least three surviving counterarguments are reported.
- [ ] Nothing recommended exceeds what one person can review, or it is flagged where it does.
- [ ] Every playbook is usable on a client engagement without editing the parts marked fixed.
      </acceptance_criteria>

<tone>
Write for a practitioner who will act on this next week. Direct, specific, quantified.
No hedging filler, no "it depends" without immediately saying what it depends on, no
enthusiasm about tools. Where you recommend, recommend — and name the condition under which
you would recommend otherwise.
</tone>

</prompt>
