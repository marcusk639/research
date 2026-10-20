# wshobson/agents — Adoption Analysis for `~/dev/research`

> **Verdict (2026-09-15).** Marketplace snapshot: `wshobson/agents` — 94 plugins, 202 agents,
> 183 skills, 105 commands, already registered on this machine as the `claude-code-workflows`
> marketplace. This is a Markdown knowledge repository with no build, no tests, and no source
> marketplace. This is a Markdown knowledge repository with no build, no tests, and no source
> code, so roughly 90 of those 94 plugins are irrelevant by construction. Install **one**
> plugin — `avoid-ai-writing` — apply **one already-enabled** plugin — `documentation-standards`
> — and pull **three individual skills** without their parent plugins. The single highest-value
> item is the `grounded-vault` skill in `documentation-standards`: this corpus has already been
> burned once by unverifiable claims (40 of 109 citations misstated, per the root `CLAUDE.md`)
> and once by silent supersession (`va-disability/planning-docs/MASTER-STRATEGY.md` is reversed
> by the newer `RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md`, and nothing in the corpus points
> from one to the other). `grounded-vault` is a written contract for exactly those two failures.
> Total footprint added: 3 skills from plugins, 3 standalone skills, 0 new agents, 0 new
> commands, 0 hooks.

---

## 1. Repository profile

`~/dev/research` is a research and synthesis workspace, not a software project. Root
`CLAUDE.md` states it plainly: _"there is no build, lint, or test step."_ There is no
`package.json`, no `pyproject.toml`, no CI workflow, and no test runner. The deliverable is
cited Markdown.

**Structure.** One top-level directory per research subject, each self-contained, each with a
`REPORT.md` as its primary synthesis:

| Path                                      | What it is                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `va-disability/`                          | By far the largest subject. A live VA disability compensation claim: `COMPREHENSIVE-FINDINGS-2026-07.md`, `CLAIM-ASSESSMENT.md`, `NEXUS-LETTER-EVALUATION.md`, `DOCUMENT-PROVENANCE.md`, `CLAIM-CORPUS-AUDIT-2026-07-06.md`, plus `planning-docs/` (29 files), `rater-kb/` (6 files incl. `criteria-4130-caselaw.md`, `mst-adjudication.md`), `ratings/`, `supporting-docs/`, `vre/`, `document-analysis/` |
| `va-cue-system/`                          | Product research for a VA CUE (clear and unmistakable error) tool — `va-cue-rag-kb-system.md`, `deep-research-wedge-moat-2026-07-16.md`, `phase-V-validation-checklist.md`                                                                                                                                                                                                                                 |
| `va-claims-tool/`                         | A single `RESEARCH-PROMPT.md`; not yet a real subject                                                                                                                                                                                                                                                                                                                                                      |
| `short-term-disability/`, `unemployment/` | `REPORT.md` only                                                                                                                                                                                                                                                                                                                                                                                           |
| `optimal-ai-dev-flow/`                    | Meta-research on AI development workflow — `corpus-ledger.md`, `LEDGER-HIGHLIGHTS.md`, `playbooks/`, `findings/`, several superseded plan versions (`v1.md`, `v2.md`, `workflow-plan.md`, `workflow-plan-v2.md`)                                                                                                                                                                                           |
| `businesses/`                             | Venture research with its own `businesses/CLAUDE.md`. Four ventures: `addiction-recovery/`, `entrepreneurial-pursuits/`, `bh-rcm-copilot/`, `writing/`                                                                                                                                                                                                                                                     |
| `docs/`, `prompts/`                       | Repo-level meta. `docs/claude-code-config/`, `docs/superpowers/specs                                                                                                                                                                                                                                                                                                                                       | plans/`; `prompts/` holds raw user asks |

**The work that actually happens here.** Three distinct jobs, and they have different risk
profiles:

1. **Legally-consequential research.** `va-disability/` feeds documents that go to a
   VA-accredited provider (`planning-docs/NEXUS-LETTER-FEEDBACK-FOR-CHERIE-2026-07-17.md`) and
   ultimately to a VA rater. Every citation to 38 C.F.R., 38 U.S.C., or case law is load-bearing.
2. **Venture evaluation.** `businesses/CLAUDE.md` specifies an investment-style rubric that each
   venture `REPORT.md` must satisfy: problem & customer, **market** (_"size, growth, segments,
   and how those numbers were derived"_), competition, business model and unit economics, risks,
   and a go / no-go verdict.
3. **Corpus maintenance.** Reconciling new documents into an existing body of work without
   creating drift — the job `/va-corpus-sync` and `claim-consistency-checker` exist to do.

**Constraints that shape every recommendation.**

- The corpus contains a veteran's psychiatric records, MST disclosure, and named clinicians.
  Nothing in it may be uploaded to a third-party service.
- Root `CLAUDE.md` documents the failure that defines this repo's quality bar: _"a prior
  `va-disability/` research pass had 109 citations checked and **40 were misstated** (wrong
  pincites, overreached holdings, stale figures)."_
- Supersession is unsignposted. `va-disability/CLAUDE.md` names `MASTER-STRATEGY.md` and
  `CLAIM-ASSESSMENT.md` as current, but `planning-docs/RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md`
  is newer and reverses positions in both. `optimal-ai-dev-flow/` has the same shape with
  `v1.md` / `v2.md` / `workflow-plan.md` / `workflow-plan-v2.md` sitting as peers.

---

## 2. Claude tooling already in place

**Repo-local** (`~/dev/research/.claude/`) — 10 skills, 2 agents, no `settings.json`, no hooks:

| Kind   | Name                         | What it covers                                                                                                                                              |
| ------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agent  | `citation-verifier`          | Adversarial check of case law / CFR / USC / Federal Register cites. Exists _because of_ the 40-of-109 finding. Tools: Read, Grep, Glob, WebSearch, WebFetch |
| agent  | `claim-consistency-checker`  | Cross-references dates, diagnoses, employment status across `va-disability/` docs. Tools: Read, Grep, Glob                                                  |
| skill  | `new-subject`                | Scaffolds `<slug>/REPORT.md`; refuses to clobber                                                                                                            |
| skill  | `source-capture`             | Fetches a URL, files it as cited Markdown in the active subject                                                                                             |
| skill  | `va-rating-strategy`         | Four-phase gated build: KB → profile → strategy+odds → resources                                                                                            |
| skill  | `va-rating-reassess`         | Ad-hoc strategic re-analysis without rebuilding the four base artifacts                                                                                     |
| skill  | `va-rating-math`             | Deterministic 38 CFR 4.25 / 4.26 combined-rating arithmetic                                                                                                 |
| skill  | `rate-claim`                 | Record-only mock VA adjudication over `va-disability/supporting-docs/`                                                                                      |
| skill  | `nexus-letter-evaluator`     | Content-grades a provider opinion against legal + rating-tier requirements                                                                                  |
| skill  | `va-claim-status`            | Overdue deadlines, next actions, open blockers                                                                                                              |
| skill  | `va-corpus-sync`             | Reconciles a new document into the corpus; proposes, never auto-applies                                                                                     |
| skill  | `va-witness-statement-guide` | Emits questions only — _"structurally incapable of producing narrative/example content by design"_                                                          |
| config | `.claudeignore`              | Excludes `.remember/logs/`, `.remember/tmp/`                                                                                                                |

**Global** (`~/.claude/`) — the relevant subset of 37 agents and ~80 skills:

| Kind  | Name                                              | Relevance                                                                    |
| ----- | ------------------------------------------------- | ---------------------------------------------------------------------------- |
| agent | `research-analyst`, `market-researcher`           | Multi-source research and synthesis; market sizing and competitive landscape |
| agent | `document-analyst`, `document-corpus-synthesizer` | Deep single-doc grading; multi-doc master synthesis                          |
| agent | `legal-advisor`                                   | **Name collision risk** — see §7                                             |
| agent | `verifier`                                        | Opus-tier adversarial re-derivation of a conclusion                          |
| skill | `deep-research`                                   | The workhorse named by root `CLAUDE.md`                                      |
| skill | `documentation-review`                            | Report-first quality review of one doc or a folder                           |
| skill | `writing-clearly-and-concisely`                   | Clarity and concision pass                                                   |
| skill | `optimizing-claude-setup`, `repo-claude-advisor`  | Config auditing                                                              |

**Already installed from this very marketplace** (`claude-code-workflows` = `wshobson/agents`):

| Plugin                    | State                   | Note                                                                          |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------- |
| `before-you-build`         | installed, **enabled**  | Already covers the pre-mortem use case for `businesses/`. Do not re-recommend |
| `code-documentation`       | installed, enabled      | Code-oriented; inert here                                                     |
| `comprehensive-review`     | installed, enabled      | Code review; inert here                                                       |
| `documentation-standards`  | installed, **enabled**  | The Tier-1 pick in §4.1 — already on; apply it, do not install it            |
| `llm-application-dev`      | installed, **enabled**  | See Tier 2                                                                    |
| `llm-finetuning`           | installed, enabled      | No fine-tuning work in this repo; inert here                                  |

**This marketplace has already been triaged once, and mostly rejected.**
`~/.claude-acct2/settings.json` — the live `$CLAUDE_CONFIG_DIR` on this machine; `~/.claude/settings.json`
is a stale, inactive mirror that disagrees — registers **56** `@claude-code-workflows` plugins
under `enabledPlugins`, and **50 of them are explicitly `false`.** Verify:

```bash
grep -o '"[a-z0-9-]*@claude-code-workflows": *\(true\|false\)' "$CLAUDE_CONFIG_DIR/settings.json" | sort
```

Six are `true`: `before-you-build`, `code-documentation`, `comprehensive-review`,
`documentation-standards`, `llm-application-dev`, `llm-finetuning`. That changes the burden of
proof for everything below. These are not unexamined offerings — they were seen and either
enabled or (for the fifty still `false`) switched off. `documentation-standards` **is** among the
56 — it is already enabled, so §4.1 is an application, not a fresh install. `avoid-ai-writing` is
**not** among the 56, so it is genuinely new rather than previously-rejected; the skills-only
picks in §6 come from plugins that **were** evaluated and disabled (`startup-business-analyst`,
`documentation-generation`), which is exactly why they are recommended as individual skills and
not as plugin re-enablements.

Other enabled plugins that matter: `document-skills@anthropic-agent-skills` (local `docx`,
`pdf`, `pptx`, `xlsx`), `voltagent-biz` (includes a `content-quality-editor` agent — see §4.2),
`voltagent-research` (includes `search-specialist` — see §7), `claude-mem`, `context-mode`,
`token-optimizer`.

**Hooks** come entirely from `~/.claude-acct2/settings.json`: PreToolUse guards on `Edit|Write` and
`Bash`, PostToolUse Prettier on `.md`, plus SessionStart / UserPromptSubmit / PreCompact / Stop
handlers. The repo adds none of its own.

---

## 3. Selection criteria

Every candidate had to answer all six. A "no" on any one is a rejection.

1. **Does it operate on prose and Markdown, or on code?** A plugin that reads ASTs, runs a test
   suite, or scaffolds an API has nothing to act on in this repo.
2. **Does it beat something already installed?** With 10 repo skills, 2 repo agents, 37 global
   agents and ~80 global skills, the default answer is "we already have that." A recommendation
   has to name what it adds over the incumbent.
3. **Does it touch the corpus's confidentiality boundary?** Anything that transmits file
   contents to a third-party service is disqualified outright — this corpus holds psychiatric
   records and a MST disclosure.
4. **Does it address a failure this repo has actually had?** Misstated citations, silent
   supersession, corpus drift. Not hypothetical risks — documented ones.
5. **What does the whole plugin cost?** The plugin is the unit of install. A plugin with five
   skills and an Opus-tier agent to get one useful skill is a bad trade; use the skills-only path.
6. **Does it survive "what specific task gets measurably better?"** Named file, named command,
   named expected output — or it's out.

---

## 4. Tier 1 — Install now

### 4.1 `documentation-standards` — already enabled

**Prior-triage status: already enabled.** It is one of the 56 registered `@claude-code-workflows`
entries in `~/.claude-acct2/settings.json` (the live `$CLAUDE_CONFIG_DIR`; `~/.claude/settings.json`
is a stale mirror that shows it absent) and is set to `true` — there is no install step here, only
the case for applying it.

**What ships with it.** Two skills, no agents, no commands, no hooks — the cheapest possible
plugin shape.

- `grounded-vault` — the `raw/` / `wiki/` / `archive/` three-layer store, per-claim provenance
  links, and `git:<sha>` fingerprints for zero-token drift detection. Ships a
  `references/details.md` for progressive disclosure.
- `hads` — the Human-AI Document Standard: four block types (`**[SPEC]**` authoritative,
  `**[NOTE]**` human context, `**[BUG]**` verified failure + fix, `**[?]**` unverified /
  inferred), plus a required H1 / version / AI-manifest header.

**Why it fits this repo.** `grounded-vault` is a written specification for the two failure modes
this corpus has already suffered.

The first is unverifiable claims. `grounded-vault`'s page-header contract requires every wiki
page to open with its `Raw:` sources, and requires every number, date, and quote in the body to
link to the source it came from. `va-disability/DOCUMENT-PROVENANCE.md` and
`CLAIM-CORPUS-AUDIT-2026-07-06.md` are hand-rolled, retrofitted versions of this — written
_after_ the 40-of-109 discovery rather than enforced from the start. The skill turns a one-time
audit artifact into a standing contract.

The second is silent supersession. `grounded-vault`'s rule is _"moved, never deleted; the header
says why."_ Apply it and `planning-docs/MASTER-STRATEGY.md` moves to `archive/` with a header
naming `RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md` as its successor — which is precisely the
pointer that does not currently exist and that a reader has to already know about to avoid
acting on a reversed position. The same treatment fixes `optimal-ai-dev-flow/v1.md` vs `v2.md`
and `businesses/entrepreneurial-pursuits/archive/` (which already exists but has no header
contract).

The `hads` half is real but weaker here: retrofitting `**[SPEC]**` / `**[NOTE]**` tags across
100+ existing Markdown files is a rewrite, not an adoption. Take one thing from it — the
`**[?]**` block for unverified or inferred claims — and apply it going forward. In a corpus where
37% of checked citations were wrong, an inline marker that says "this is inferred, not verified"
is worth more than the rest of the standard combined.

**Concrete use cases.**

1. _Situation:_ You are about to act on `va-disability/planning-docs/MASTER-STRATEGY.md` and need
   to know whether it is still the operative position.
   _Invocation:_ "Restructure `va-disability/` per the grounded-vault pattern — `rater-kb/` and
   `supporting-docs/` become `raw/` (immutable), the working strategy documents become `wiki/`
   pages with `Raw:` headers and git fingerprints, and any document a newer one reverses moves to
   `archive/` with a header naming its successor."
   _Expect back:_ A move plan naming each of the 29 `planning-docs/` files as current or
   superseded, plus header blocks. The two that must come out of that plan: `MASTER-STRATEGY.md`
   → archived, superseded by `RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md`; `CLAIM-ASSESSMENT.md`
   → same. Nothing is deleted.

2. _Situation:_ `businesses/bh-rcm-copilot/REPORT.md` cites market figures, and
   `businesses/CLAUDE.md` demands _"how those numbers were derived."_
   _Invocation:_ "Apply the grounded-vault page-header contract to
   `businesses/bh-rcm-copilot/REPORT.md` — every market figure gets a link to the file in
   `sources/` it came from, unsourced figures get flagged."
   _Expect back:_ A rewritten header plus a list of every number in the body that currently has
   no traceable source. That list is the actual finding.

3. _Situation:_ You want to know whether `va-disability/rater-kb/criteria-4130-caselaw.md` still
   reflects what `COMPREHENSIVE-FINDINGS-2026-07.md` says, without rereading both.
   _Invocation:_ "Run the grounded-vault fingerprint check on `va-disability/rater-kb/`."
   _Expect back:_ A `git diff` against each page's recorded fingerprint, and a list of pages whose
   sources moved since compilation. Cheap, and it does not read the pages.

**Overlap / conflict.** `grounded-vault`'s scope is provenance and drift on a durable store. It
does _not_ overlap `/va-corpus-sync` (which reconciles one incoming document against the corpus)
or `claim-consistency-checker` (which finds factual contradictions between documents).
`grounded-vault` is the layout and the contract; those two are the checks that run on top of it.
The skill body says this itself: session state and continuity are _"a different problem; use the
context-management or conductor plugins for those."_ No name collisions — neither skill name
exists locally or globally.

### 4.2 `avoid-ai-writing`

**Prior-triage status: never evaluated.** Also absent from the 56 registered entries. No prior
decision is being overturned.

**What ships with it.** Exactly one skill, no agents, no commands. The skill carries three
reference files (`references/pattern-catalog.md`, `references/profiles.md`,
`references/word-tiers.md`) loaded only on demand.

Three modes: **detect** (flag only, no changes), **rewrite** (return a clean version),
**edit** (change a file in place). Context profiles include `docs`, `blog`, `technical-blog`,
`investor-email`, `linkedin`, `casual`.

**Why it fits this repo.** Two distinct needs, both real.

`businesses/writing/` is an actual venture whose entire premise is voice —
`positioning-comedic-anti-self-help.md`, `playbook.md`, `launch-and-growth-plan.md`,
`case-studies.md`, and a `sources/founder-writing-sample-the-beginning.md` that exists to record
what the author's voice sounds like. A venture positioned on comedic anti-self-help writing
cannot ship prose that reads as machine-generated; that is not a style preference, it is the
product failing.

Separately, `va-witness-statement-guide` already encodes this repo's position on machine voice in
lay evidence — it is _"structurally incapable of producing narrative/example content by design,"_
because a buddy statement that reads as generated is a credibility liability in front of a VA
rater. `avoid-ai-writing`'s **detect** mode is the read-only counterpart: it audits a witness's
own draft and flags tells without rewriting a word of someone else's statement.

**Concrete use cases.**

1. _Situation:_ A draft chapter or launch post under `businesses/writing/` needs a voice check
   before it goes out.
   _Invocation:_ "Run avoid-ai-writing in rewrite mode with `--context blog` on
   `businesses/writing/launch-and-growth-plan.md`."
   _Expect back:_ Quoted offending spans, a rewrite, and a change summary. The rhythm check
   (step 4 of the skill's pass — uniform sentence and paragraph length, weighted highest) is the
   part a vocabulary-swap tool misses.

2. _Situation:_ A buddy or spouse has returned a first-draft 21-10210 statement and you need to
   know whether it reads as written by them.
   _Invocation:_ "Run avoid-ai-writing in **detect** mode on the draft — flag only, do not
   rewrite."
   _Expect back:_ A flag list split into clear problems and judgment calls. Detect mode is the
   only correct mode here; the skill's own rule is that published text or text belonging to
   someone else gets flagged, not rewritten. This composes with `va-witness-statement-guide`:
   detect finds the tells, the guide produces the questions that let the witness fix them in their
   own words.

**Overlap / conflict.** Two incumbents, and both need addressing:

- `voltagent-biz`'s `content-quality-editor` agent (enabled) does overlapping work, but it shells
  out to an external `unslop` binary and is aimed at dev-adjacent content — _"blog posts, READMEs,
  release notes, commit messages, PR descriptions."_ `avoid-ai-writing` adds three things it does
  not have: a detect-only mode, context profiles (`investor-email`, `docs`), and an explicit rule
  never to rewrite quoted material, code blocks, tables, or text attributed to someone else. For a
  witness statement or a draft that quotes a clinician, those three are the whole point.
- The global `writing-clearly-and-concisely` skill targets clarity and concision. Different axis:
  a sentence can be perfectly concise and still read as machine-generated. Keep both; they do not
  collide.

---

## 5. Tier 2 — Install when the trigger fires

### `llm-application-dev` — **trigger: `va-cue-system/` or `va-claims-tool/` starts being built**

Already **enabled** from this marketplace — one of the six `true` entries in
`~/.claude-acct2/settings.json` (the live `$CLAUDE_CONFIG_DIR`), not one of the fifty declined.
There is nothing to flip; the trigger below is about when its skills have something to act on, not
about re-enabling anything.
Ships `ai-engineer`, `prompt-engineer`, `vector-database-engineer` agents; `ai-assistant`,
`langchain-agent`, `prompt-optimize` commands; and the `rag-implementation`,
`embedding-strategies`, `hybrid-search-implementation`, `llm-evaluation`,
`similarity-search-patterns`, `vector-index-tuning` skills.

`va-cue-system/va-cue-rag-kb-system.md` and `va-claims-tool/RESEARCH-PROMPT.md` currently describe
a RAG system that does not exist. While they remain design documents, this plugin has nothing to
act on — research about RAG is not RAG. The moment a repo appears with an actual index in it, reach
for it; `llm-evaluation` in particular matters for a tool whose wrong answers have legal
consequences. Note the overlap with the global `prompt-engineer` agent and `llm-application-dev`
skill (both already present).

### `pptx-deck-creation` — **trigger: a venture needs a deck rather than a report**

Ships one agent (`pptx-deck-creation-builder`, `model: inherit` — runs at the session model, which
is `opus[1m]` here) and five skills (`pptx-deck-context`, `pptx-slide-specification`,
`pptx-quality-gates`, `pptx-reference-deck-analysis`, `pptx-visual-assets`). That is the heaviest
plugin considered for this repo, and there is not a single `.pptx` in it today.

The plausible trigger is concrete:
`businesses/entrepreneurial-pursuits/VRE-SELF-EMPLOYMENT-FUNDING-STRATEGY.md` describes a VR&E
self-employment track, which requires submitting a business plan to a VA counselor, and
`homegroups-gtm-and-moat-analysis.md` is the kind of material that becomes a deck. When a
specific deck is actually due, install it. Not before — `document-skills@anthropic-agent-skills`
already provides a local `pptx` skill that handles the simple cases without the extra agent.

---

## 6. Skills-only picks

Install these **without** their parent plugins. Both commands work; pick one.

```bash
# from startup-business-analyst — for businesses/ ventures
gh skill install wshobson/agents market-sizing-analysis
gh skill install wshobson/agents competitive-landscape

# from documentation-generation — fixes the supersession-pointer problem
gh skill install wshobson/agents architecture-decision-records

# npx equivalent
npx skills add wshobson/agents --skill market-sizing-analysis
```

**`market-sizing-analysis` + `competitive-landscape`** — these two map almost line-for-line onto
`businesses/CLAUDE.md`'s required report sections. `market-sizing-analysis` covers TAM/SAM/SOM via
top-down, bottom-up, and value-theory methods, which is the answer to the rubric's _"and how those
numbers were derived"_; `competitive-landscape` covers Porter's Five Forces, Blue Ocean, and
positioning maps, which is the rubric's _"Competition — direct and indirect players, their
positioning and gaps."_

Why not the whole `startup-business-analyst` plugin: it also ships `startup-financial-modeling`,
`startup-metrics-framework` (CAC/LTV/burn multiple, board reporting), `team-composition-analysis`
(headcount, equity allocation, hiring budget aligned to funding milestones), three commands, and
the `startup-analyst` agent at `model: inherit`. Three of those assume a funded company with
employees and revenue. Every venture in `businesses/` is a solo, pre-revenue investigation —
`addiction-recovery/`, `entrepreneurial-pursuits/`, `bh-rcm-copilot/`, `writing/`. There is no
cap table to model and no burn multiple to benchmark. And `startup-analyst` overlaps the global
`market-researcher` agent directly while costing session-tier tokens. Take the two skills; leave
the rest.

**`architecture-decision-records`** — this looks like a code-repo skill and is not being
recommended as one. ADR format carries an explicit **Status** field with a `Superseded by`
pointer, which is the exact missing link described in §1: `MASTER-STRATEGY.md` has no forward
reference to the plan that reverses it, and `optimal-ai-dev-flow/` has four peer plan files with
no ordering. `grounded-vault` handles this at the file-layout level (move to `archive/`); ADRs
handle it at the document level for decisions that are recorded in place — e.g.
`optimal-ai-dev-flow/WORKFLOW-DECISION.md` and
`businesses/entrepreneurial-pursuits/homegroups-strategic-decision.md`. One skill, no plugin.
The rest of `documentation-generation` (`openapi-spec-generation`, `changelog-automation`, and
five agents including a Haiku-tier `reference-builder`) is for shipping software.

---

## 7. Considered and rejected

Fourteen candidates evaluated and rejected. The near-misses are the important rows.

| Offering                                          | Why it looked relevant                                                                                                                                                      | Why it is not                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`file-conversion`**                             | Real need — `planning-docs/` already holds `.docx` renders (`NEXUS-LETTER-FEEDBACK-FOR-CHERIE-2026-07-17.docx`, `NEXUS_V2_EVAL_RESULTS.docx`) alongside their `.md` sources | **Disqualified on confidentiality.** The skill base64-encodes the file and POSTs it to `changethisfile.com`. This corpus holds psychiatric records, an MST disclosure, and named clinicians. Criterion 3 is absolute. `document-skills@anthropic-agent-skills` is already enabled and converts `.md` → `.docx` / `.pdf` locally                                                    |
| **`content-marketing`** (for `search-specialist`) | `search-specialist` is described as a deep web-research agent; this repo is a research repo                                                                                 | `model: haiku`. A cheap-tier search agent is the wrong instrument for a corpus where 40 of 109 legal citations were misstated. Overlaps `deep-research` (global skill), `research-analyst` and `market-researcher` (global agents), and `voltagent-research`'s own `search-specialist` (already enabled). The plugin also drags in `content-marketer`, also Haiku, also irrelevant |
| **`hr-legal-compliance`**                         | Keyword match on "legal." Ships a `legal-advisor` agent                                                                                                                     | Wrong body of law entirely. Its `legal-advisor` drafts privacy policies, ToS, cookie policies and DPAs; `gdpr-data-handling` is EU data processing; `employment-contract-templates` is employer-side HR documentation. None of it touches 38 C.F.R., VA adjudication, or disability law. Also a **name collision**: `~/.claude/agents/legal-advisor.md` already exists globally    |
| **`before-you-build`**                            | Genuinely fits `businesses/` pre-mortem work                                                                                                                                | **Already installed and enabled** from this marketplace. Nothing to do                                                                                                                                                                                                                                                                                                             |
| **`startup-business-analyst`** (full plugin)      | `businesses/` is venture research with an investment-style rubric                                                                                                           | Two of five skills fit; three assume a funded company with headcount and revenue. Plus a `model: inherit` agent duplicating global `market-researcher`. Taken as skills-only instead — see §6                                                                                                                                                                                      |
| **`business-analytics`**                          | "Business" keyword; `businesses/` exists                                                                                                                                    | `kpi-dashboard-design` is for live operational dashboards (MRR, churn, service health). There is no dashboard, no product, and no telemetry in this repo. `data-storytelling` is closer but is aimed at executive presentation decks, which is Tier-2 territory at best                                                                                                            |
| **`documentation-generation`** (full plugin)      | "Documentation" is the whole job here                                                                                                                                       | Everything except `architecture-decision-records` targets shipping software: `openapi-spec-generation`, `changelog-automation`, `api-documenter`, `docs-architect` (analyzes codebases), `reference-builder` (Haiku), `mermaid-expert`. One skill taken standalone — see §6                                                                                                        |
| **`code-documentation`**                          | Already enabled                                                                                                                                                             | `docs-architect` and `tutorial-engineer` produce documentation _from a codebase_. There is no codebase. Inert, not harmful — leave it                                                                                                                                                                                                                                              |
| **`comprehensive-review`**                        | Already enabled                                                                                                                                                             | `architect-review`, `code-reviewer`, `security-auditor` — all code. Inert here                                                                                                                                                                                                                                                                                                     |
| **`superself`**                                   | Session-state continuity across research sessions                                                                                                                           | Requires `npm install -g superself` and a `<!-- superself:begin` block in `CLAUDE.md`. This repo already has `.remember/` session memory wired into a SessionStart hook, documented in root `CLAUDE.md`, plus `claude-mem` enabled globally. Third continuity system, no added capability                                                                                          |
| **`conductor`**                                   | "Context → Spec & Plan → Implement" sounds like research phasing                                                                                                            | It is a code-project tracker: `track-management` produces `spec.md`/`plan.md` per feature, `workflow-patterns` is a TDD workflow with git commits per task. Nothing to implement here. The gated-phase need is already served by `/va-rating-strategy`'s four gated phases                                                                                                         |
| **`skill-forge-essentials`**                      | `session-guard` addresses compaction amnesia                                                                                                                                | `ai-debt-detector` and `visual-edit-precision` are code/UI-specific. `session-guard` overlaps `claude-mem` and `context-mode`, both enabled. Not worth a third layer                                                                                                                                                                                                               |
| **`security-compliance`**                         | This corpus holds protected health information                                                                                                                              | The plugin validates SOC2/HIPAA compliance _of systems you are building_ — `compliance-check` command, `security-auditor` agent. There is no system here, only files. The confidentiality control this repo needs is "do not upload," which is a rule, not a plugin                                                                                                                |
| **`agent-teams`** / **`agent-orchestration`**     | Multi-agent research fan-out                                                                                                                                                | `deep-research` already fans out and adversarially verifies. `agent-teams` ships 4 agents and 7 commands aimed at parallel _code_ review and debugging                                                                                                                                                                                                                             |

---

## 8. Installation plan

The marketplace is already registered on this machine as `claude-code-workflows`.

> **Never run `/plugin marketplace add wshobson/agents`.** The same upstream repo is already
> registered under the `claude-code-workflows` alias; adding it again registers it a second time
> under a different alias and produces duplicate entries in the plugin picker, with two
> independently-updating copies of every plugin. Always install with the existing alias.

```bash
# 1. Confirm the alias, and see what was already evaluated
/plugin marketplace list                 # expect: claude-code-workflows -> github:wshobson/agents
grep -o '"[a-z0-9-]*@claude-code-workflows": *\(true\|false\)' "$CLAUDE_CONFIG_DIR/settings.json" | sort
#   expect 56 lines, 50 false. documentation-standards SHOULD appear as true (already enabled);
#   avoid-ai-writing should NOT appear — it is new, not a re-enablement.
```

```bash
# 2. One install. documentation-standards is ALREADY enabled — nothing to install for it;
#    apply it directly (see §4.1). Only avoid-ai-writing needs installing.
/plugin install avoid-ai-writing@claude-code-workflows
```

**This install is user-scope, i.e. global** — and `documentation-standards` is already enabled
the same way. Both load in every Claude session on this machine, not only in `~/dev/research`.
Both picks are small and prose-oriented so the blast radius is low, but if you want them confined
to this repo, do not install globally — create `~/dev/research/.claude/settings.json` with a
repo-scoped `enabledPlugins` entry instead, or take the skills-only route in §6 and drop the skill
directories where you want them.

Verify: run `/plugin` and confirm both show as enabled. Then, in a session opened at
`~/dev/research`, ask _"what does the grounded-vault pattern require in a page header?"_ — if the
skill activated, the answer names `Raw:` and `Fingerprint:`. Ask _"what are the HADS block
types?"_ — the answer must be `[SPEC]`, `[NOTE]`, `[BUG]`, `[?]` and nothing else.

```bash
# 3. Skills-only picks — no parent plugins
gh skill install wshobson/agents market-sizing-analysis
gh skill install wshobson/agents competitive-landscape
gh skill install wshobson/agents architecture-decision-records
```

Verify: `ls ~/.claude/skills/` should now show the three new directories, and `/plugin` should
show **no** new plugin entry for `startup-business-analyst` or `documentation-generation`. If
either appears, the skills-only path was not used — uninstall and retry.

```bash
# 4. Do NOT install these. Listed so a future session does not re-litigate them.
#    file-conversion       — uploads file contents to changethisfile.com
#    content-marketing     — haiku-tier search agent, duplicates deep-research
#    hr-legal-compliance   — wrong body of law; collides with global legal-advisor
```

```bash
# 5. Tier 2 — nothing to flip; use it when the trigger fires.
#    llm-application-dev is already installed and enabled (true) in
#    ~/.claude-acct2/settings.json — it just has nothing to act on in this repo yet.
#    When va-cue-system/ or va-claims-tool/ gets an actual RAG index, start using
#    ai-engineer / llm-evaluation / rag-implementation directly. No settings change needed.
```

**First real exercise, to prove value before committing further.** Run the `grounded-vault`
restructure as a _plan only_ over `va-disability/planning-docs/` — 29 files. If it correctly
identifies `MASTER-STRATEGY.md` and `CLAIM-ASSESSMENT.md` as superseded by
`RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md` without being told, the pattern is earning its
place. If it does not, the adoption is manual-only and the skill is just a reference document.

---

## 9. Risks and caveats

**Plugin enablement is global, and there are two settings files.** A `/plugin install` writes a
user-scope entry in `~/.claude-acct2/settings.json` (the live `$CLAUDE_CONFIG_DIR`), so anything
enabled for this repo loads in every session on this machine — including the CPA-firm repos,
where a research plugin is pure context cost. Prefer a repo-scoped
`~/dev/research/.claude/settings.json` (this repo currently has none) when a pick is only wanted
here. Second hazard, verified: `~/.claude/settings.json` and `~/.claude-acct2/settings.json` are
**different files with different enablement maps** — 3 `@claude-code-workflows` plugins `true` in
the former, 6 in the latter (`~/.claude-acct2` is the live one). Do not source an "already
enabled" claim from whichever one you happen to open; run `/plugin` in a live session and treat
that as the authority.

**Context-window cost.** Small, by design. Three skills from plugins plus three standalone skills
adds six skill descriptions to the always-loaded listing; the bodies (capped ~8KB, with
`references/` loaded on demand) only load when a skill activates. No new agents means no new agent
descriptions. This is deliberate — the `optimizing-claude-setup` and `context-auditor` tooling
already in this setup exists because the global roster is large, and a 94-plugin marketplace is
exactly how that gets worse.

**Agent-name collisions.** None introduced, because none of the Tier-1 picks ship agents. The one
live collision is a rejection, not an install: `hr-legal-compliance` ships `legal-advisor`, and
`~/.claude/agents/legal-advisor.md` already exists. wshobson agents are namespaced on install
(`hr-legal-compliance-legal-advisor`), so the conflict would be ambiguity in a request for "the
legal advisor," not a hard failure — but that ambiguity in a repo doing VA claims research is a
real way to get technology-law advice when you asked for disability-law advice.

**Opus-tier and inherit-tier cost.** No Tier-1 item carries an agent. Two rejected/deferred ones
do: `startup-analyst` and `pptx-deck-creation-builder` are both `model: inherit`, which in this
setup resolves to `opus[1m]` (`~/.claude-acct2/settings.json` → `"model": "opus[1m]"`). Anything
`inherit` in a wshobson plugin should be read as "runs at your most expensive tier" here.

**External-service dependencies.** `file-conversion` requires `changethisfile.com` — rejected
above on confidentiality, and it would also be a live network dependency and a single point of
failure. `superself` requires a global npm install. Neither Tier-1 pick requires anything beyond
git, and `grounded-vault` says so explicitly: _"It needs a git repository and nothing else."_

**Prose in this repo will be reformatted.** The global PostToolUse hook runs Prettier on every
`.md` write. `grounded-vault` headers and `hads` block tags are plain Markdown and survive it,
but do not hand-align tables — the formatter will redo them.

**Third-party marketplace drift.** `wshobson/agents` is one maintainer's repository. It is not
pinned: `~/.claude-acct2/plugins/installed_plugins.json` records a `gitCommitSha` per plugin, but
`/plugin update` moves it. Skills can change content or be renamed between updates. Two
mitigations: re-read a skill's `SKILL.md` before relying on a specific rule after an update, and
treat skills-only installs (§6) as the safer path, since they copy a skill into `~/.claude/skills/`
rather than tracking the upstream plugin.

**The honest limit of all of this.** Neither Tier-1 pick verifies a citation, and neither knows
anything about 38 C.F.R. The repo's own `citation-verifier` agent is still the thing standing
between this corpus and another 40-of-109 result. `grounded-vault` makes the verification
_checkable_ — it does not do the verifying.

