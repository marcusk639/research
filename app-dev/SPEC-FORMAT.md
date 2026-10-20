# Spec Format — a lightweight, schema-validated spec for agent-driven work

**Date:** 2026-09-29
**Status:** original design. Every element below is `[UNVERIFIED — author's design, needs testing]` unless
it cites a source. That label is not boilerplate: the research found **no published machine-readable spec
schema anywhere** in the spec-driven-development ecosystem, so there is no prior art to inherit
correctness from.

---

## 1. What the evidence says to build, and what to avoid

Seven spec systems were confirmed to exist and be maintained — GitHub Spec Kit [S32], AWS Kiro [S33],
OpenSpec [S34], Tessl [S35], BMAD-METHOD [S36], Agent-OS [S37], and the AGENTS.md convention [S38]. Two
findings shape this design more than any feature of those tools.

**Every one of them expresses its spec as prose Markdown; none publishes a JSON/YAML schema.** That is the
gap this format fills, and also the reason to be humble about filling it — a format with no adopters has no
evidence behind it.

**Heavyweight spec ceremony measurably costs more than it returns.** The one detailed independent
practitioner benchmark found Spec Kit took "33m30" of agent time and produced "2,577 lines of markdown"
for "689 loc", against "8m" for "1,000 loc (and no markdown!)" iteratively, with the author concluding "I
am a lot more productive without SDD, around ten times faster" [S43]. A 2026 academic taxonomy warns that
"AI frameworks run the risk of merely institutionalizing 'vibe coding' with an extra layer of terminology"
[S42] and notes "Most object-frameworks have not gone through independent academic evaluation" [S42].
Thoughtworks keeps the whole category in its "Assess" ring, calling the workflows "elaborate and
opinionated" [S44].

So the design rule is **the smallest spec that closes the ambiguity that actually matters**, not a document
suite. Concretely: one file, prose allowed everywhere, and only four required fields.

**Spec ambiguity is a correctness and security property, not a style issue.** Reward hacking in coding
agents jumps from ~0.7–2.1% on unambiguous problems to 22–44% on ambiguous ones [S60]. Tightening the spec
is the cheapest mitigation available for agents gaming their own tests.

**The agent usually cannot ask.** In a genuine unattended run with `--permission-prompts none`, "Claude
Code removes the tools that need an answer from a person, such as AskUserQuestion, so Claude can't call
them" [S8]. And the research is blunt that models are bad at this judgment anyway: "no frontier model
recovers more than a fraction of its full-information performance when deciding whether to ask" [S40].
Therefore this format does **not** rely on the agent asking well. It requires the agent to *record
assumptions in a machine-readable block* and surface them for review. Question-asking is replaced by an
audit trail.

Standing conventions (house style, stack defaults, directory layout, commit format) do **not** belong in
the spec. They belong in `AGENTS.md`/`CLAUDE.md`, the one convention with real cross-tool adoption [S38].
A spec that restates conventions is the "sea of markdown" failure [S43].

---

## 2. The schema

Two document kinds share one schema: `kind: app` and `kind: feature`. Only `meta`, `intent`,
`acceptance_criteria`, and `out_of_scope` are required. Everything else is optional and omitted when the
answer is "the repo's existing convention".

```yaml
# REQUIRED
meta:
  kind: feature              # app | feature
  id: hg-meeting-reminders   # stable slug, used for branch/PR naming
  title: Meeting reminders
  target_repo: ~/dev/recovery-platform/homegroups
  surfaces: [mobile, functions]   # mobile | web | functions | any subset
  spec_version: 1

intent: |
  Free prose. What this is for, who it serves, and what changes for them.
  The one field where verbosity is welcome, because it is what the agent
  reasons from when a detail is missing.

acceptance_criteria:           # REQUIRED, and the contract the pipeline is graded against
  - id: AC1
    given: a member belongs to a group with a weekly meeting
    when: the meeting starts in 30 minutes
    then: they receive one push notification, and only one
    verify: e2e-mobile       # unit | integration | rules | e2e-web | e2e-mobile | manual
  - id: AC2
    given: a member has disabled reminders
    when: the same meeting approaches
    then: no notification is sent
    verify: integration

out_of_scope:                  # REQUIRED, even if it is a single line
  - email or SMS reminders
  - changes to the meeting scheduling UI

# OPTIONAL BELOW THIS LINE
actors:
  - name: member
    can: [view own groups, toggle own reminder preference]
  - name: group_admin
    can: [set the group meeting schedule]

data:
  collections:
    - name: meetings
      changes: none
    - name: group_members
      changes: add field `reminders_enabled: boolean, default true`
  access_rules: |
    A member may read and write only their own group_members document.
    No client may write notification records; functions only.
  indexes: |
    Existing composite indexes are expected to cover this. If a new index
    is required, add it to firestore.indexes.json and say so in the PR.

flows:
  - name: toggle reminder preference
    steps: [open group detail, tap Reminders, toggle off, confirm persisted after reload]

design:
  follow: existing        # existing | described below
  notes: |
    Use the app's current settings-row pattern. No new colors, no new
    component library. Mobile only; no web surface in this feature.

non_functional:
  - no additional cold-start cost on existing callable functions
  - reminder delivery within +/- 2 minutes of target

constraints:
  forbidden:
    - editing firestore.rules without a paired rules test
    - new third-party dependencies
  human_gate:              # things that must stop for a person
    - firestore rules changes
    - any scheduled-function schedule change

assumptions_policy:
  on_ambiguity: assume_and_record   # assume_and_record | stop
  max_questions: 0                  # 0 in unattended runs; the tool cannot ask anyway [S8]
  record_to: .agent/assumptions.yaml
```

### The assumption ledger the agent writes back

This is the mechanism that replaces clarifying questions. The agent appends, the human reviews, and a
resolved ledger becomes spec amendments on the next run.

```yaml
# .agent/assumptions.yaml — written by the agent, reviewed by the human
- id: A1
  about: AC1 "only one" notification
  assumed: dedupe key is (meeting_id, user_id, scheduled_occurrence)
  because: the repo's existing notifications collection already keys on occurrence
  confidence: high
  blast_radius: low        # low | medium | high — high means a wrong guess is expensive
  reversible: yes
  evidence: functions/src/notifications/send.ts:41
- id: A2
  about: reminder lead time
  assumed: fixed 30 minutes, not user-configurable
  because: spec says "30 minutes" with no configuration requirement
  confidence: medium
  blast_radius: medium
  reversible: yes
  evidence: none — spec silent
```

`blast_radius: high` plus `reversible: no` is the one combination that must halt an unattended run even
under `max_questions: 0`, because the cost asymmetry is what justifies stopping — not the agent's
uncertainty, which the evidence says it judges poorly [S40].

---

## 3. Completeness checklist — what justifies stopping

Run before any implementation. The point is to make "should I ask?" a **property of the spec**, not a
judgment call by the model, since the model is measurably bad at that judgment [S40] and cannot ask at all
in unattended mode [S8].

| Check | Missing ⇒ |
|---|---|
| `meta.kind`, `meta.target_repo`, `meta.surfaces` present | **STOP** — cannot route the work |
| At least one `acceptance_criteria` entry with `given/when/then/verify` | **STOP** — nothing to grade against |
| `out_of_scope` present | **STOP** — unbounded scope is the main cause of agent sprawl |
| Every AC maps to a `verify` method the repo can actually run | **STOP** — an ungradeable criterion is a fiction |
| A data change is named but no `access_rules` given, on a repo with security rules | **STOP** — rules are 439–951 lines here and no evidence exists on agent-authored Firestore rules [`GAPS.md`] |
| Auth, payments, or migrations touched | **STOP** for human design sign-off, regardless of clarity |
| `design.follow` absent on a UI change | assume `existing`, record assumption |
| `actors` absent | infer from repo, record assumption |
| `non_functional` absent | assume existing budgets, record assumption |
| Naming, file layout, commit style absent | never ask — `AGENTS.md` owns this [S38] |

Only six conditions stop the run, and five are structural rather than judgment-based. That is deliberate:
it is the difference between a checklist and an interrogation.

---

## 4. App-level example (a Homegroups-class product)

Deliberately short. An app spec's job is to fix the domain model, the surfaces and the acceptance
criteria for a *first vertical slice* — not to describe the finished product. The measured bar for a
product of this class is ~194k LOC, 100+ screens and a 951-line rules file (`ledger/run_manifest.json`),
and the evidence says an agent cannot produce that in one run: the best model on from-scratch program
building fully solves **4.5%** of tasks [S5]. So an app spec is a sequence of feature specs behind a
shared domain, and this document is only the first one.

```yaml
meta:
  kind: app
  id: homegroups
  title: Homegroups — 12-step recovery group management
  target_repo: ~/dev/recovery-platform/homegroups-next
  surfaces: [mobile, web, functions]
  spec_version: 1

intent: |
  A platform for 12-step recovery groups to manage themselves: find and follow
  meetings, hold group business meetings with votes and elected officers, keep
  minutes, and let members track personal milestones. Members are often in
  early recovery; privacy and low-friction UX matter more than feature depth.
  Anonymity is a first-class requirement, not a setting.

actors:
  - name: member
    can: [find meetings, join a group, view group announcements, track own milestones]
  - name: group_officer
    can: [edit group details, schedule meetings, publish minutes, open votes]
  - name: intergroup_admin
    can: [administer many groups, publish intergroup reports]

data:
  collections:
    - name: groups
    - name: group_members
    - name: meetings
    - name: meetingInstances
    - name: announcements
    - name: group_conscience_votes
    - name: group_elections
    - name: minutes
    - name: milestones
  access_rules: |
    Group content is readable by members of that group. Officer-only writes for
    group settings, meetings, minutes and votes. A member reads and writes only
    their own membership and milestone documents. No cross-group reads.
    Personal identity fields are never readable by other members by default.

acceptance_criteria:
  - id: AC1
    given: a signed-in member
    when: they search meetings by day and distance
    then: matching meetings appear with time, format and location
    verify: e2e-mobile
  - id: AC2
    given: a group officer
    when: they open a group conscience vote with three options
    then: only members of that group can cast one vote each, and results are hidden until close
    verify: integration
  - id: AC3
    given: a non-member
    when: they attempt to read a group's minutes directly
    then: the read is denied by security rules
    verify: rules

out_of_scope:
  - payments and donations
  - literature content and bookmarks
  - intergroup reporting (later slice)

design:
  follow: described below
  notes: |
    Calm, low-stimulation, high-contrast. Large touch targets. No streak
    gamification or social-comparison mechanics. Mobile-first; the web surface
    is an officer/admin console, not a second consumer app.

constraints:
  human_gate:
    - firestore.rules (all changes)
    - auth configuration
    - anything that could expose member identity across groups

assumptions_policy:
  on_ambiguity: assume_and_record
  max_questions: 3          # app-level greenfield: a batched round is allowed before work starts
  record_to: .agent/assumptions.yaml
```

Note `max_questions: 3` here versus `0` in the feature spec. A greenfield app spec is the one place where
a single batched clarification round is defensible, because the cost of a wrong domain-model guess is high
and irreversible. This is a judgment, not a finding — the research offers no measured comparison of
batched-up-front versus assume-and-record in a shipped harness [`GAPS.md`].

---

## 5. Feature-level example (brownfield, the recommended starting point)

The feature example at the top of §2 is the canonical one, targeting the real `homegroups` repo and using
collection names measured from it (`meetings`, `group_members`). Two properties make it a good first
autonomous experiment:

- it touches two surfaces but adds no new collection;
- it has one genuinely ambiguous point (dedupe semantics for "only one" notification), so it exercises the
  assumption ledger rather than trivially succeeding.

---

## 6. Honest assessment of this format

- **No adoption evidence.** This schema has never been run. Spec-driven development as a category sits in
  Thoughtworks' "Assess" ring [S44], and the only independent benchmark found the heavyweight version
  ~10x slower [S43]. The mitigation is the design's minimalism, not a claim of correctness.
- **Drift is unsolved.** Spec-to-code drift is a named, open risk in the literature, with Spec Kit's own
  remedy being an iterative "implement → converge" loop [S32] rather than an automated diff or schema
  gate [S42]. This format has the same weakness. The only real defence here is that
  `acceptance_criteria` are compiled into executable tests (`VERIFICATION-STRATEGY.md` §6), so a subset
  of the spec is mechanically checkable — the prose is not.
- **The assumption ledger is untested.** A peer-reviewed scaffold reports 69.40% task resolution with
  calibrated, cost-aware information seeking [S39], which is encouraging for the general approach, but
  that is a research prototype and no shipped coding agent implements it [S42, S40]. The ledger here is a
  hand-rolled substitute.
- **Start with `kind: feature`.** The app-level example is included because it was requested and because
  it shows the format scales, not because the evidence supports pointing an agent at it.
