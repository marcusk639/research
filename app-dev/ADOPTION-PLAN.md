# Adoption Plan — 30 days, falsifiable

**Date:** 2026-09-29

Five stages. Each has one falsifiable experiment, a success metric, a cost ceiling and a kill criterion.
The sequence is deliberately the reverse of the exciting order: **the gate is built before the autonomy**,
because every piece of evidence says the gate is the hard part and the autonomy is the easy part to demo.

The whole plan runs against `homegroups` or `regroup` — real brownfield repos — not a greenfield app. The
one measurement that matters more than anything in this directory is **your own pass rate on your own
repo**, because published benchmark numbers do not transfer (`RISKS.md` R14).

Cost ceilings are anchored on the official SWE-bench per-task costs of $0.07–$1.53 [S2] scaled up for
multi-surface work with a verification loop. They are **budget caps, not predictions** — no verified dollar
anchor exists for whole-feature autonomous runs (`GAPS.md`).

---

## Stage 0 (Days 1–3) — Baseline the gate, with no agent involved

**Experiment.** Add StrykerJS to one package of `homegroups` (start with `functions`, which has 256 files /
61k LOC and the richest pure logic). Run it once on human-written tests. Record the mutation score.

**Why first.** `thresholds.break` defaults to `null`, meaning Stryker "never let[s] your build fail" until
configured [S6]. And no fetched source gives a mutation score for a codebase like this — every published
figure is generic JS/TS or Angular (`GAPS.md`). You cannot ratchet from a number you have not measured.

- **Success metric:** a mutation score exists for one package, and full-run wall-clock time is known.
- **Cost ceiling:** $0 in model spend; ≤4 hours of your time.
- **Kill criterion:** if a full run on one package exceeds ~30 minutes and incremental mode cannot get a
  changed-files run under ~5 minutes, **abandon mutation testing as a gate** and record that the primary
  anti-vacuous control is unavailable for this repo. That is a genuinely plausible outcome — practitioner
  reports describe poor scaling and one found verdicts "not reproducible enough to gate on"
  (`VERIFICATION-STRATEGY.md` §2). If this happens, §3's structural separation carries the whole load and
  everything downstream gets more human review, not less.

## Stage 1 (Days 4–6) — Build the tamper gate and prove it blocks

**Experiment.** Implement the hook guards from `VERIFICATION-STRATEGY.md` §5. Then *try to break them*:
instruct an agent to delete a test file, add `it.only`, replace an assertion with `expect(true).toBe(true)`,
run `jest -u`, and run `firebase deploy`. Each must be blocked.

**Why.** "Exit 2 means a blocking error" and "PreToolUse blocks the tool call" [S9] — but the policies are
my design, unverified. Use `FileChanged`, which fires "when a specific file changes on disk, whatever wrote
it" [S9], because a hook matching only edit tools can be bypassed.
**Also build the escape hatch, in the same stage.** Expose an `escalate(reason, evidence, blast_radius)`
capability plus an explicit anti-hacking policy line in the prompt (`VERIFICATION-STRATEGY.md` §3). This is
not optional polish: it is the single best-measured behavioural intervention found, cutting reward hacking
from 23.6% to 5.3% (OR = 9.2, p < 10⁻¹²) with no measured performance cost [S108]. Count an escalation as a
**success** in your metrics from day one — if escalating is penalized, you have rebuilt the incentive to fake.


- **Success metric:** 5/5 adversarial attempts blocked, evidenced in the run log.
- **Cost ceiling:** <$10.
- **Kill criterion:** if any guard can be bypassed and you cannot fix it in a day, do not proceed to
  unattended runs at all. Attended-only is still a real, useful outcome.

## Stage 2 (Days 7–13) — One brownfield feature, attended, separated roles

**Experiment.** The reminder feature from `SPEC-FORMAT.md` §2 (or a real backlog item of similar size:
two surfaces, no new collection, one genuinely ambiguous point). Run the full §5 sequence of `GUIDE.md`
**attended** — test-author agent on a strong model first, tests committed failing, then implementer.

**Why this shape.** Role separation has measured support: 96.3% vs 90.2% pass@1 on HumanEval and 91.8% vs
78.9% on MBPP for a separated pipeline [S63] (function-level, single backbone — evidence for separating roles,
not models). Closer to this case, a controlled study across 20 full-stack web applications found TDD improves
accuracy by "15.5--23.7 percentage points" with capable backbones, and that "replacing unreliable feedback
with a stronger tester restores positive gains for a lower-capability backbone" [S66].

- **Success metrics:** (a) all acceptance criteria pass; (b) the mutation ratchet does not regress;
  (c) the implementer made **zero** edits to test files; (d) `.agent/assumptions.yaml` contains at least one
  assumption you agree with and none you consider dangerous; (e) your review time is under 90 minutes.
- **Cost ceiling:** $40 for the feature.
- **Kill criterion:** if review takes longer than writing the feature yourself would have, record it and
  stop expanding scope. This is the METR result reproducing on your own repo: that RCT found developers
  "take 19% longer to complete issues" with AI while believing they were 20% faster [S1] — so **measure the
  clock, do not trust the feeling.** Its authors explicitly do not claim it generalizes [S1], which is
  exactly why you measure locally.

## Stage 3 (Days 14–20) — Three more features, one unattended

**Experiment.** Repeat Stage 2 three times. Make the **third** one unattended: devcontainer, egress
firewall, `--permission-mode auto --permission-prompts none`, no human in the loop until the PR.

**Why the container.** "Because the container runs Claude Code as a non-root user and confines command
execution to the container, you can pass `--dangerously-skip-permissions` for unattended operation" [S18],
with `init-firewall.sh` limiting outbound traffic [S18]. And note what unattended actually means: with
`--permission-prompts none`, Claude Code "removes the tools that need an answer from a person, such as
AskUserQuestion, so Claude can't call them" [S8]. **The agent cannot ask. The assumption ledger is the
whole interface.**

- **Success metrics:** 3/3 features pass their gates; the unattended one produces a reviewable PR with an
  assumption ledger; you accept ≥2 of 3 PRs with only minor changes.
- **Cost ceiling:** $150 total.
- **Kill criterion:** if the unattended run produces a PR you would not merge even after edits, revert to
  attended-only and treat unattended as not yet viable for this repo. If 2+ of 3 features need
  more-than-minor rework, the spec format is the suspect before the agent is.

## Stage 4 (Days 21–27) — Add the mobile and rules loops

**Experiment.** Take one feature through the full three-surface loop including EAS Workflows + Maestro on
a real build, and one feature that deliberately requires a Firestore rules change.

**Why separate.** Mobile is the weakest surface — the EAS Workflows E2E path is genuinely unattended
("uses a `pull_request` trigger to run automatically when someone opens a pull request" [S76], with
`npx eas-cli build --platform all --non-interactive --no-wait` [S99]) — but agents cannot see a simulator
and RN profiling output "aren't easy for agents to interpret yet" [S78]. And rules are the single riskiest
artifact: **no evidence exists either way** on agent-authored Firestore rules (`GAPS.md`) against 439/951-line
files.

- **Success metrics:** the mobile E2E gate fails a deliberately broken build (prove the gate works, not just
  that it runs); the rules change ships with adversarial `assertFails` tests [S10] and survives your review
  unchanged.
- **Cost ceiling:** $80 plus EAS build minutes.
- **Kill criterion:** if the agent's rules diff is wrong in a way your review nearly missed, **permanently
  remove rules from agent scope.** Write them by hand. This is the one place to be inflexible.

## Stage 5 (Day 28–30) — Decide, with numbers

Compute from your own logs: features attempted, features merged, median review minutes, median cost per
feature, assumption-ledger entries per feature and how many were wrong, gate catches (how many times a
gate caught something review would have missed), and escapes (how many defects reached main).

Then pick one:

| Outcome | If | Then |
|---|---|---|
| **Adopt** | merged ≥70% with review under the time it would take you by hand | run the Recommended pipeline (`REPORT.md`) as default for features of this shape |
| **Adopt narrowly** | good on logic/backend, bad on UI or mobile | keep agents on functions/tests, hand-write UI and rules |
| **Attended only** | output good but unattended PRs unreliable | keep the gate, drop unattended mode |
| **Stop** | review cost ≥ hand-writing cost, or ≥1 escape reached main | stop; keep only the gates (Stryker, tamper hooks, rules tests), which are worth having regardless |

The last row is a real possible outcome and not a failure of the plan. The strongest independent evidence
in this whole report points that way for experienced developers on familiar code [S1], and the gates
you will have built are valuable even if no agent ever writes another line here.

---

## What this plan deliberately does not do

- **No greenfield app build.** The best model fully solves 4.5% of from-scratch program builds [S5]. A
  greenfield run belongs after Stage 5, as an experiment, not in the adoption path.
- **No new platform.** No Railway, no Devin, no Factory, no app-factory product. Railway is real and
  well-guardrailed [S13] but orthogonal to this stack; the rest are vendor-claim-only or have independent
  negative evidence (`RISKS.md` R11).
- **No heavyweight SDD.** One spec file, four required fields. The independent benchmark found the
  ceremony-heavy version ~10x slower with no measured quality gain [S43].
- **No scaling past your review capacity.** AI-authored PRs are reported to carry ~1.7x the issues of human
  ones [S25]; throughput without review capacity converts into escapes.
