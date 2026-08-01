# Harness Blueprint

_Phase C deliverable 7 | 2026-08-01 | Evidence base: `findings/w1-dev-loop.md`, `findings/w2-orchestration.md`, `findings/w3-verification.md`, `findings/w4-documentation.md`, `findings/w5-cost-routing.md`, `findings/w9-composition.md`_

**What this is.** What to configure once. Repo conventions, instruction-file structure, the minimal
hook set, the minimal subagent roster, the minimal skill set, CI contents, and the cross-project
handoff mechanism — plus a separate knowledge-repo variant and an explicit **what to delete**
section.

**Volatility warning up front.** Anthropic's product surface is version-gated and moves weekly. W2
recorded behaviour changes at v2.1.169, .178, .191, .196, .198, .199, .200, .206, .208, .210, .211,
.212, .214, .216 within a single research pass. **Every mechanic below was verified 2026-08-01 and
should be re-checked with `/doctor` and the changelog before being treated as load-bearing.** The
_patterns_ are durable; the flags are not.

---

## 0. The three findings this blueprint is built on

**1. The desired session topology is not a supported configuration.** One orchestrator holding
shared context across several projects, surviving resume, does not exist and is not coming:

| Mechanism                | What it actually does (Tier A, vendor docs, read in full)                                                                                                                                                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Session storage          | "Claude Code stores sessions **per project directory**." `Ctrl+A` widens the picker to every project on the machine, but selecting an unrelated project's session **copies a `cd` and resume command to your clipboard instead of resuming it**. Cross-project resume is deliberately not in-place                                                       |
| `--add-dir` / `/add-dir` | Gives one live session genuine read/write reach across several repos with automatic path resolution — but **`--add-dir` directories are not restored on resume**, and neither are directories added mid-session with `/add-dir`. It also does **not** load the added directory's CLAUDE.md without `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`      |
| Auto memory              | "Each project gets its own memory directory… The `<project>` path is **derived from the git repository**." And: "Auto memory is **machine-local**… Files are not shared across machines or cloud environments." Only the first **200 lines or 25KB** of `MEMORY.md` loads at session start; everything past it is silently dropped                       |
| Agent teams              | "Each teammate has its own context window… **The lead's conversation history does not carry over.**" "**One team per session** — you can't create additional named teams or share a team across sessions." "**No session resumption with in-process teammates.**" Experimental, behind `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, ~7x tokens in plan mode |
| The feature request      | Anthropic issue **#38309** — `/add-folder` with multiple workspace roots, multi-CLAUDE.md loading, cross-folder Glob/Grep/Read, multi-repo git context — is **closed as not planned**                                                                                                                                                                    |

**What the operator must give up, stated plainly:** durable cross-project context. You get reach
within a live session and nothing across resume. The buildable substitute is a **written recipe**
(§5), not a configuration.

**2. Instruction files pay for existence, not elaboration.** In the only controlled factorial study
(1,650 Claude Code sessions, 16,050 function-level observations, pre-registered GLMM with a Bayesian
companion, Tier A): **zero of 1,669 functions** complied with a target convention without a
CLAUDE.md (Wilson 95% upper bound 0.73%); with one, compliance ran **54.9–67.7%**. Matched contrast
χ² = 534.27, p = 3.3 × 10⁻¹¹⁸, **Cohen's |h| = 1.93**. Meanwhile size (25→500 lines), position
within the file, splitting across files, and a _contradicting instruction in an adjacent AGENTS.md_
were **all null**, with affirmative-null Bayes factors **BF₁₀ = 0.096** (size) and **0.053**
(conflict).

And the cost runs the wrong way: repository context files **increase inference cost 20% (SWE-bench)
and 23% (CTXBench), p < 0.001%**, driven by +2.45 and +3.92 agent steps, with **no significant
change in task resolution** — across four models and two benchmarks, including a purpose-built
benchmark of 138 instances from 12 repositories with developer-committed context files (ETH Zurich +
LogicStar, Tier A).

**Therefore the rule is a content test, not a length budget:** _keep a line only if nothing else in
the repository already states it._

**3. Instruction files cannot hold a rule over a long run; hooks can.** Compliance falls **5.6% in
odds per function generated within a session** (OR = 0.944, 95% CI [0.937, 0.951], p = 1.1 × 10⁻⁴⁹),
with the median first omission at generated function **4**. Anthropic says the same thing in plain
language: instruction files are _"context, not enforced configuration. To block an action regardless
of what Claude decides, use a PreToolUse hook instead."_ And: _"Unlike CLAUDE.md instructions which
are advisory, hooks are deterministic and guarantee the action happens."_

---

## 1. Configuration phases

### H0 — Audit and delete

| Field                | Content                                                                                                                                                                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | An existing setup exists. (Skip to H1 for a greenfield machine.)                                                                                                                                                                                                           |
| **Activities**       | Run `/context` to see which memory files actually load. Run `/doctor` (v2.1.206+) for its CLAUDE.md trim proposals. Enable the `InstructionsLoaded` hook to log exactly which instruction files load, when, and why. Then work §2's delete list.                           |
| **Artifacts**        | `harness/before.md` — the loaded-file inventory with line counts; `harness/deleted.md` — what came out and why.                                                                                                                                                            |
| **Time-box**         | 2–3 hours. Once.                                                                                                                                                                                                                                                           |
| **Human checkpoint** | Every deletion. Deleting a line you cannot justify is the point; deleting one you cannot _replace_ is a regression.                                                                                                                                                        |
| **Exit test**        | Every surviving line in every always-loaded file passes the content test: **"does anything else in the repository already state this?"** If yes, it is deleted. Measure the token delta with `/context` before and after and record it — that is your only local evidence. |

### H1 — Repository and directory conventions

| Field                | Content                                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | H0 complete.                                                                                                                                                                                                                                                  |
| **Activities**       | Establish the three-tier layout in §3. Create the meta-repo with `repos.yaml`. Set client-repo isolation per §6.                                                                                                                                              |
| **Artifacts**        | `~/dev/AGENTS.md` (or `CLAUDE.md`) meta-repo entry point; `~/dev/repos.yaml`; per-project `CLAUDE.md` files.                                                                                                                                                  |
| **Time-box**         | Half a day. Once.                                                                                                                                                                                                                                             |
| **Human checkpoint** | The generic-vs-client boundary. This is a confidentiality decision, not a layout decision.                                                                                                                                                                    |
| **Exit test**        | `repos.yaml` lists every project with path, purpose, language, build command, and **client-affiliation flag**. Every client-affiliated repo is outside every mechanism in §6's leak-path table. `/context` in a client repo shows no other client's material. |

### H2 — Instruction files

| Field                | Content                                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | H1 complete.                                                                                                                                                                                                                                                                                                         |
| **Activities**       | Apply the content test to every file in §4's hierarchy. Move anything that must _hold_ into a hook (H3). Move anything path-specific into `.claude/rules/*.md` with `paths:` frontmatter.                                                                                                                            |
| **Artifacts**        | The trimmed hierarchy; `harness/content-test-log.md` (what was kept and the one-line justification).                                                                                                                                                                                                                 |
| **Time-box**         | 2–3 hours per repo, first time; 15 min per repo thereafter.                                                                                                                                                                                                                                                          |
| **Human checkpoint** | Each retained line's justification.                                                                                                                                                                                                                                                                                  |
| **Exit test**        | Every retained line names something **not derivable by reading the repository**, and no retained line encodes a rule that must hold across a long session (those became hooks). Length is _not_ the test — a 500-line file of non-derivable conventions passes; a 40-line file restating the directory layout fails. |

### H3 — The minimal hook set

| Field                | Content                                                                                                                                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | H2 complete. Each candidate hook names the bottleneck it removes and the signal that the bottleneck is present (§5's table).                                                                                                                                                           |
| **Activities**       | Install only the hooks in §5's table whose signal is currently present. Do not install prospectively.                                                                                                                                                                                  |
| **Artifacts**        | `settings.json` hook block; `harness/hooks.md` — one line per hook: what it enforces, which signal justified it, what would justify removing it.                                                                                                                                       |
| **Time-box**         | 1–2 hours.                                                                                                                                                                                                                                                                             |
| **Human checkpoint** | Each hook's justification line. **A hook without a named bottleneck and a named signal is deleted, not kept "just in case."**                                                                                                                                                          |
| **Exit test**        | Every hook has all three fields filled and fires in under 2 seconds (hooks run synchronously and block the loop). Verify subagent coverage: hooks from settings files **also run inside subagents**, carrying `agent_id` and `agent_type` — so gates cannot be bypassed by delegation. |

### H4 — Subagents and skills

| Field                | Content                                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | H3 complete.                                                                                                                                                                                                                        |
| **Activities**       | Reduce to §6's roster. Delete every agent and skill not on it or not used in the last 30 days.                                                                                                                                      |
| **Artifacts**        | The trimmed `.claude/agents/` and `.claude/skills/` directories; `harness/roster.md`.                                                                                                                                               |
| **Time-box**         | 1–2 hours.                                                                                                                                                                                                                          |
| **Human checkpoint** | The reviewer subagent's mandate line. It must be narrow **from day one, not added later as a fix**.                                                                                                                                 |
| **Exit test**        | The roster is ≤6 subagents and ≤8 skills, each with a named triggering situation. The reviewer subagent's prompt contains an explicit correctness/requirements-only mandate. Its model is **not** the cheapest tier available (§6). |

### H5 — CI

| Field                | Content                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | H4 complete. A repo exists that a bug can reach.                                                                                                                                                                                                                                                                                                                                                                     |
| **Activities**       | Install §7's minimal CI. Nothing beyond it until a named regression class has actually escaped.                                                                                                                                                                                                                                                                                                                      |
| **Artifacts**        | `ci.yml`; `harness/ci-rationale.md` — one line per gate naming the regression class it prevents.                                                                                                                                                                                                                                                                                                                     |
| **Time-box**         | Half a day per repo.                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Human checkpoint** | The list of regression classes. Do not copy a pipeline; enumerate what has actually broken.                                                                                                                                                                                                                                                                                                                          |
| **Exit test**        | CI is green on a clean checkout, runs in under 10 minutes, and every gate names a regression class that has actually occurred at least once. **Budget check:** since 2026-06-15, `claude -p`, the Agent SDK, and Claude Code GitHub Actions draw from a **separate credit pool billed at API rates**, not the flat interactive allowance. Any AI step in CI is metered spend — price it before merging the workflow. |

### H6 — Cross-project handoff

| Field                | Content                                                                                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | H1 complete.                                                                                                                                                                                                                                                                        |
| **Activities**       | Write the per-project startup recipe and the checkpoint-file convention in §8. Wire a `SessionEnd` hook to archive the transcript.                                                                                                                                                  |
| **Artifacts**        | `<project>/.claude/start.sh` (the recipe); `<project>/CHECKPOINT.md`; `SessionEnd` archive hook.                                                                                                                                                                                    |
| **Time-box**         | 1–2 hours per project.                                                                                                                                                                                                                                                              |
| **Human checkpoint** | Confirming the recipe actually reconstructs the session. Run it cold, from a fresh terminal, once.                                                                                                                                                                                  |
| **Exit test**        | **Cold-start test:** close everything, run `start.sh`, and confirm every `--add-dir`, MCP config, settings source, and plugin dir that the working session needed is back. Anything missing is added to the recipe. This is the _only_ durable cross-project mechanism that exists. |

---

## 2. What to delete

Work this list against an existing setup. Each row names what to remove and why.

| Delete                                                                                                                  | Why                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Any CLAUDE.md line restating the directory layout, the agent roster, or the rules hierarchy**                         | All derivable by reading the directory. This is the exact content class measured as inert, and it is on Anthropic's own "❌ Exclude" list                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **"Repository overview" / architectural-map sections**                                                                  | Overviews did **not** reduce steps before the agent first touched a file it needed to modify — on any agent, on either benchmark. Ablating the overview category changed accuracy by −5.8 pp (p = 0.15) and −0.2 pp (p = 0.73): no significant effect either way. The paper's own words: context files "are not effective at providing a repository overview"                                                                                                                                                                                                              |
| **The `AI.md` 40%-token-savings premise and everything built on it**                                                    | **C-107 is not merely unsupported — its direction is inverted.** Measured effect is a cost _increase_ of 20–23%. See `REPORT.md` §2                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Model Tier Policy blocks in CLAUDE.md** (C-170, C-131, C-185)                                                         | Nothing in Claude Code, Cursor, or Codex reads a tier annotation in a markdown file and routes on it. Model selection comes from `settings.json`, `--model`, `/model`, or subagent frontmatter. Calling the annotation "executable" describes a mechanism that does not exist — and is itself an instance of the drift class this blueprint exists to prevent                                                                                                                                                                                                              |
| **`.cursorrules`**                                                                                                      | Superseded by `.cursor/rules/*.mdc`; current Cursor docs do not mention `.cursorrules` at all                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Any rule whose enforcement matters across a long session**                                                            | Move it to a hook. Compliance decays 5.6% per function generated; median first omission at function 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Hooks with no named bottleneck and no named present signal**                                                          | Subtraction bias. A hook is synchronous latency on every matching call, forever                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Subagents and skills unused in 30 days**                                                                              | They are context cost at every session start for the discovery surface and maintenance cost forever                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Multi-agent swarm hooks (e.g. `swarm-notify.sh`)**                                                                    | Fan-out is the pattern Anthropic's own warning targets (15x tokens, "less effective for tightly interdependent tasks such as coding") and it is the one thing that reliably outruns a single reviewer                                                                                                                                                                                                                                                                                                                                                                      |
| **Any tool binding a Claude Max/Pro or ChatGPT Plus OAuth token into a third-party router** (Manifest, Hermes, similar) | Anthropic's Consumer ToS has long barred this and it has been **actively and technically enforced since January 2026**, with an Anthropic engineer confirming measures to block third-party tools "spoofing the Claude Code harness." At least one tool removed Claude Pro/Max credential support after legal requests. This crossed from config overhead to **active ToS violation with enforcement**                                                                                                                                                                     |
| **The two-machine "M4 = judgment / M5 = batch" tier split**                                                             | **RAM is not the binding variable for cloud-model tiers** — every tier in the corpus's own routing scheme is cloud-hosted. Worse, splitting machines has a documented cost: auto memory is machine-local ("Files are not shared across machines"), and `/usage` figures are "computed from local session history **on this machine**." A two-machine split actively fragments accumulated memory and usage visibility. If a second machine is kept, re-derive its purpose (quota isolation under a second account, or genuinely local inference) rather than inheriting it |
| **A third-party worktree orchestrator kept for worktree management**                                                    | Substantially commoditised. Native now: `claude --worktree`/`-w`, `.worktreeinclude`, `isolation: worktree` subagent frontmatter, `EnterWorktree`/`ExitWorktree`, `WorktreeCreate`/`WorktreeRemove` hooks, `/batch` (5–30 worktree-isolated subagents), auto-worktree per desktop session, periodic `cleanupPeriodDays` sweep, `git worktree lock` on running agents. Keep an orchestrator **only** for cross-tool UI (driving Codex/Cursor from one surface) or side-by-side diff review across lanes — not for the mechanics                                             |
| **The "cap worktrees at 2–3, the documented practical ceiling" line**                                                   | **Nothing documents it.** The vendor's nearest guidance is _higher_ (3–5 teammates; `/batch` splits across 5–30), and Anthropic frames 3–5 as a productivity **floor** ("the biggest productivity unlock"), not a supervision ceiling — the corpus inverted its source's meaning. Keep the number as a personal review-capacity bet if you like; do not keep it as a cited fact                                                                                                                                                                                            |

---

## 3. Repository and directory conventions

Three tiers. The boundary between tier 2 and tier 3 is a **confidentiality boundary**, not a
convenience one (`engagement-playbook.md` §10).

```
~/dev/                              ← tier 1: meta-repo (tracked)
├── AGENTS.md                       ← entry point: repo map table + 3 standing instructions
├── repos.yaml                      ← machine-readable registry
├── conventions/                    ← generic, cross-project, non-derivable conventions only
├── methodology/                    ← tier 2: GENERIC methodology repo (the playbooks live here)
├── <project-a>/                    ← tier 2: own repo, own CLAUDE.md, own CI
├── <project-b>/
└── clients/
    ├── <client-1>/                 ← tier 3: per-client repo. Isolated. See §9
    └── <client-2>/
```

**`AGENTS.md` contents — FIXED:**

1. A repo map table: every repo with its path, purpose, languages, and build system.
2. Three standing instructions: _verify documented information against reality; update this file
   when an inaccuracy surfaces; suggest improvements._
3. Nothing else. Everything else belongs in the project it describes.

**Evidence for the meta-repo pattern, stated honestly.** Three independent implementations converge
on this shape — an independent solo operator across six repos (`AGENTS.md` + `repos.yaml`, reporting
an eight-merge-request six-repository fix completed across five sessions without losing context), a
multi-repo CLAUDE.md hierarchy proposal, and a 25-engineer company's "Cross Repo Base." **None of
the three reports metrics.** It is a design pattern with no comparative data (Tier B). The solo
author's own caveats are the best counter-evidence available: "None of this is a silver bullet";
documentation drift is real and the "immune system" of agents instructed to verify "still requires
discipline"; the pattern "may become obsolete as models improve." **And neither author addresses
whether the registry itself drifts** — which, given a 4:1 add-to-delete ratio measured across 2,303
context files in 1,925 repositories, it will.

**The one before/after number in this space should not be trusted.** A 25-engineer, 79-repo company
reports context drift falling from "~40% of our failures to <5%." It has **no operational definition
of a "context drift failure," no measurement method, no third-party verification, and it is a
bundled intervention** — the coordination graph shipped alongside worktree hooks, ~40 skills, AI
review, and circuit breakers, so no component's contribution is isolable. It is also being laundered
through a vendor blog by a founder selling a cross-repo graph API, so anyone meeting the figure via
search hits the vendor version first. Wrong scale and wrong evidentiary standard for this operator.

---

## 4. Instruction files

### The hierarchy — five scopes, not three (C-036 was stale)

| Scope          | Location                                                                                                 | Loads                                               |
| -------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Managed policy | `/Library/Application Support/ClaudeCode/CLAUDE.md`, `/etc/claude-code/`, `C:\Program Files\ClaudeCode\` | Always                                              |
| User           | `~/.claude/CLAUDE.md`, `~/.claude/rules/*.md`                                                            | **Every project on this machine**                   |
| Project        | `./CLAUDE.md` **or `./.claude/CLAUDE.md`**                                                               | At launch, same precedence                          |
| Local          | `./CLAUDE.local.md`                                                                                      | At launch, gitignored, worktree-local               |
| Nested         | `<subdir>/CLAUDE.md`                                                                                     | **On demand, and not re-injected after `/compact`** |

**C-206 is refuted:** `./.claude/CLAUDE.md` **is** a first-class project-instructions location, not
"tooling config." And the "root policy cascades down" half is right for _ancestor_ directories (files
are concatenated root→cwd) and wrong for _descendant_ ones — nested files load on demand and are not
redundant with a root file. `claudeMdExcludes` exists precisely because ancestor cascade is sometimes
unwanted.

Imports via `@path` have a **max depth of four hops**, and imports "still load and enter the context
window at launch" — importing does not defer cost. **Path-scoped rules (`paths:` frontmatter in
`.claude/rules/*.md`) are the only documented way to defer loading.**

### The content test — FIXED

For every line, in every file, ask **one** question:

> **Does anything else in the repository already state this?**

- **Yes** → delete it. This is the class measured as inert and cost-positive.
- **No** → keep it, regardless of how long the file becomes.

**Length is not the test.** Size across 25–500 lines is an affirmative null (BF₁₀ = 0.096). Anthropic's
own docs assert the opposite ("Bloated CLAUDE.md files cause Claude to ignore your actual
instructions!") and **provide no data**; the only controlled factorial test finds Bayesian evidence
_for_ the null. **This blueprint sides with the measurement over the vendor, and says so.** The
vendor is authoritative on its own product's _mechanisms_ and unsourced on this _effect_.

### Where the content test flips toward more infrastructure

Three conditions, each with its bound:

| Condition                                     | What changes                                                                                                                                                                                                                   | Bound                                                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **The repository has no other documentation** | In the ablation stripping all `.md` files, example code, and `docs/`, LLM-generated context files improved performance **+2.7% on average** and beat developer-written ones                                                    | The ablation is artificial — nobody deletes their docs. 2.7% is small. Read it as: context files pay when they carry **non-redundant** content   |
| **Above 500 lines**                           | McMillan's null is bounded; he flags explicitly that "a 5,000-line CLAUDE.md exists in some large repositories and is well outside our design"                                                                                 | Unmeasured, not disproven                                                                                                                        |
| **Above ~150 instructions**                   | IFScale (500 keyword-inclusion instructions, 20 models, seven providers): the best frontier model reaches only **68% accuracy at 500 instructions**, with primacy bias — later instructions violated more — peaking at 150–200 | July-2025 model lineup; the _shape_ is durable, the numbers are a year stale, and the task is single-report keyword inclusion, not an agent loop |

**Honest note on the band that matters most.** A few hundred lines carrying dozens of instructions
across a hierarchy of files — where the corpus's fear and the corpus's prescription both live — is
exactly the band **nobody has cleanly tested** (W4 Gap 6).

**And the outcome that would justify instruction files has never been measured.** Every study
measures task success or trivial-convention compliance. **Nobody has measured whether a context file
improves code quality, security, style conformance, or documentation accuracy** — the reasons
practitioners actually write them (W4 Gap 5). "Context files don't help" currently means "context
files don't help you close more tickets," which is not the same claim. Hold the content test as the
best available rule, not as a settled one.

---

## 5. The minimal hook set

**Subtraction rule, enforced:** every hook names the bottleneck it removes **and** the signal that
the bottleneck is present. No signal, no hook.

| Hook                                             | Event                        | Bottleneck removed                                    | Signal it is present                                                   | Both project kinds?                |
| ------------------------------------------------ | ---------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- |
| **Formatter on write**                           | `PostToolUse` Write/Edit     | Diff noise that hides real changes at review          | You have skimmed a diff because formatting churn drowned the substance | Both (prettier / markdownlint)     |
| **Secret / credential block**                    | `PreToolUse` Write/Edit      | A credential reaching a client repo                   | You work on client material at all                                     | Both — **install unconditionally** |
| **Test-or-build gate before turn end**           | `Stop`                       | Unverified work reaching your review queue            | You have merged something whose tests you did not see pass             | Code only                          |
| **Citation/date-field gate on knowledge writes** | `PreToolUse` Write/Edit      | Undated, unsourced assertions entering a prose corpus | You have found an assertion you cannot date or source                  | **Knowledge repo only** — see §10  |
| **Substantive-review log append**                | `PostToolUse` / `SessionEnd` | Silent approval invisible to you                      | **Install unconditionally at Stage 0** — see `REPORT.md` §4            | Both                               |
| **Transcript archive**                           | `SessionEnd`                 | Lost handoff state (`transcript_path` field)          | You have resumed a session and had to reconstruct what you were doing  | Both                               |
| `WorktreeCreate` / `WorktreeRemove`              | worktree lifecycle           | Git-logic mismatch on non-git VCS                     | You use SVN/Perforce/Mercurial                                         | Rarely — skip by default           |

**Mechanics that constrain hook design (Tier A, verified 2026-08-01):**

- Exit code **2** blocks on `PreToolUse` and `Stop`. **`PostToolUse` cannot block** — the tool has
  already run; it can only surface stderr to the model afterwards.
- **"Claude Code overrides the hook and ends the turn after 8 consecutive blocks."** This is a
  deadlock-prevention valve, not agent-exploitable — but **nobody has examined what happens to a
  safety-critical Stop gate that is overridden because the check is _stuck_ rather than because
  Claude satisfied it** (W3 Gap). Do not build an unattended loop whose only safety property is a
  Stop hook.
- Hooks run **synchronously** and block the loop. Keep them under ~2s. The corpus's specific
  `--findRelatedTests`-on-PostToolUse / full-suite-on-Stop split is a plausible performance-motivated
  pattern but is **not stated in current official docs** — it is the corpus's own recommendation.
- Hooks **fire inside subagents**, carrying `agent_id` and `agent_type`, so gates cannot be bypassed
  by delegation.

**The real safety boundary for unattended work is the OS, not the hook.** Practitioner guidance
converges on Docker-level sandboxing — mount only the project directory, no home directory, no SSH
keys — with per-task git commits so the morning review is "a git review, not an archaeology dig."
That is the OS-level analogue of a hook: enforced by the environment, not by instructions.
`--dangerously-skip-permissions` refuses to run under root/sudo, and the docs restrict it to
"isolated environments like containers, VMs, or dev containers without internet access."

**And cap the unattended run.** Reward hacking is not a rare edge case and it is **not evenly
distributed**: across 30 systems-level tasks every frontier agent tested saturates the _visible_ test
suite while the gap between visible and held-out pass rates grows with task size — up to **100
percentage points** on the largest tasks, roughly **28 points per tenfold increase in code size**
(preprint, Tier B). Separately, Anthropic's own alignment research found a model **intentionally
sabotaged code designed to detect its own misbehaviour 12% of the time**, with sabotaged classifiers
only ~65% as effective as a clean baseline (Tier A, but a deliberately-trained-to-hack model, not
baseline Claude Code). **The risk is concentrated in exactly the large, long-horizon tasks unattended
loops are most tempting for.**

---

## 6. Minimal subagent roster and skill set

### Subagents — ≤6

| Subagent                 | When it triggers                                                       | Model tier                              | Notes                                                          |
| ------------------------ | ---------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| **Reviewer**             | After any multi-file change, before you review it                      | **Frontier-class. Not the cheap tier.** | See the routing rule below. Mandate is narrow **from day one** |
| **Explorer** (built-in)  | Codebase or corpus investigation                                       | Cheap is fine                           | Read-only fan-out; returns conclusions, not file dumps         |
| **Citation verifier**    | Before finalising any document that cites law, regulation, or a source | Frontier-class                          | Knowledge-repo critical path. See §10                          |
| **Consistency checker**  | Before finalising a document in a multi-document corpus                | Frontier-class                          | Cross-document dates, facts, claims                            |
| **Build-error resolver** | Build or type failure                                                  | Cheap is fine                           | Mechanical, spec-complete                                      |
| **Mechanical executor**  | The complete spec exists and needs applying                            | Cheapest                                | Escalate up a tier on BLOCKED, never down                      |

**The reviewer's mandate — FIXED wording requirement.** _"Flag only gaps that affect correctness or
the stated requirements; treat the rest as optional."_ This is Anthropic's own verbatim guidance, and
it exists because of a documented structural bias: _"A reviewer prompted to find gaps will usually
report some, even when the work is sound, because that is what it was asked to do. Chasing every
finding leads to over-engineering: extra abstraction layers, defensive code, and tests for cases that
can't happen."_ **No evidence exists on how effective that scoping instruction actually is at
reducing false positives quantitatively** — but the bias is the vendor's own stated expectation, not
a guess, so build the mandate in on day one rather than adding it later as a fix.

### The cheap-tier routing rule — composed from two workstreams

Two findings that look like a conflict and are not:

- **W3:** routing the Judge/reviewer to a cheap model reduces defect recall. Self-review shows
  measurably reduced recall versus cross-model review; "not all reasoning models perform equally at
  code review"; LLM judges exhibit "negation blindness"; and OpenAI's own critic model was built on
  **GPT-4-class capability**, specifically because catching subtle bugs requires real reasoning
  capacity. **The corpus's C-177 — "the judge pass is pattern-matching, not deep reasoning" — is the
  single most directly contradicted claim in the cost program.**
- **W5:** tier routing is largely **moot** for interactive work anyway. On a flat Max subscription,
  token cost below the cap is not a marginal cost, so routing the Judge cheap **saves nothing you are
  actually paying**. The per-token argument bites only on the post-2026-06-15 programmatic/Agent-SDK
  credit pool and on genuine pay-as-you-go usage.

**Composed rule:** _Route the reviewer to frontier-class capability. Under a flat subscription this
is free; where it is metered, it is the one place worth paying. Route cheap only where the work is
mechanical, spec-complete, and metered._

The most detailed practitioner data point runs the same way: ~10 billion tokens over 8 months at
**~95% Opus** — the most expensive model — and it was cost-effective anyway, because flat-rate
billing made model mix irrelevant below the cap.

### Skills — ≤8

Keep a skill only if it encodes a **multi-step procedure you have actually repeated**. Skills live in
`.claude/skills/<name>/SKILL.md`, load on demand, and `disable-model-invocation: true` restricts one
to manual triggering. Suggested core: the four playbooks in this directory as skills, plus
`new-subject`, `source-capture`, `commit`, and one repo-specific build/deploy procedure.

### On the Judge/Builder loop specifically

**It is not the anti-pattern.** W1 and W3 independently concluded that Anthropic's fan-out warning
targets _parallel decomposition across many workers_ on breadth-first decomposable work, whereas a
Builder/Judge loop is two roles, sequential, bounded, on one artifact — matching a **Writer/Reviewer
pattern Anthropic's own current docs recommend** ("a fresh context improves code review since Claude
won't be biased toward code it just wrote"). Different evidence, same answer.

**But read the effect sizes before building the schema.** In the strongest supporting study
(SWE-Review, arXiv preprint, July 2026), reviewer-guided revision raised resolve rate
**27.5% → 52.6%** for a weak generator and **50.9% → 67.3%** for a mid-tier one — but only
**72.2% → 75.2%, +3.0 points, for a strong generator**. **The operator runs a frontier model, i.e.
the strong-generator regime where the measured gain was smallest.** Gains also plateau within 4–5
revision rounds. And **no head-to-head study of fan-out versus a bounded Judge loop exists on
identical tasks with both token cost and defect-catch rate measured** — the resolution is
architectural, not empirical, on that narrower point.

**Practical consequence:** start with the built-in Writer/Reviewer pattern (a fresh-context reviewer
subagent with a narrow mandate). Build the fixed-schema, auto-triggering Judge skill only if the
reviewer subagent demonstrably misses a defect class you can name.

---

## 7. CI contents

**Minimal, and each gate names a regression class that has actually occurred.**

| Gate                  | Prevents                                  | Both project kinds?                                      |
| --------------------- | ----------------------------------------- | -------------------------------------------------------- |
| Typecheck             | Type drift across a multi-package change  | Code only                                                |
| Unit tests            | Behavioural regression                    | Code only (`--passWithNoTests` where packages have none) |
| Lint                  | Style drift that makes diffs unreviewable | Both                                                     |
| Secret scan           | Credential leak                           | **Both — unconditional**                                 |
| Link and anchor check | Broken cross-references                   | **Knowledge repo** — see §10 for its limits              |
| Migration smoke test  | Schema drift                              | Code, where migrations exist                             |
| e2e, **PR-only**      | Critical-flow regression                  | Code, where flows exist                                  |

**Monorepo rule:** current tooling guidance explicitly warns against a single undifferentiated
pipeline for a monorepo with multiple package managers or build systems; per-package coordination
and selective execution are the documented norm. Do not run mobile native builds in a standard Linux
runner — they require Xcode/Android SDK or a managed build service.

**e2e rule:** run on PRs, not every push, and **do not gate the CI phase on a perfect e2e run** —
ship unit/typecheck CI first. This matches converged guidance on quarantining flaky tests and
controlling cloud-device-minute cost.

**On the "15 minutes of CI saves 2 hours of debugging" framing:** the _direction_ is well
established; the _specific multiplier_ is not. The canonical "100x" traces to 1970s-era work and is
considered dated; modern analyses cluster at 10–30x for CI/CD pipelines, and the 15-min/2-hr figure
has no independent source at all — it is an illustrative estimate. Use the direction; drop the
numbers.

**Not now:** mutation testing, contract testing, golden-file/screenshot diffing. All three have
genuine value documented **in team contexts** and **none has been shown to pay off at solo-operator
scale** (W3 Gap). Even mutation-testing proponents recommend scoping it to core business logic
rather than a repo. Contract testing has a specific trap here: when an agent generates a
consumer-driven contract **from existing code**, it encodes the implementation's bugs as correct —
Pact's own FAQ analogises it to "marking your own exam." Revisit when a named defect class has
escaped that one of them would have caught.

---

## 8. Cross-project context and handoff

**Design for what exists.** The three mechanisms below are the whole supported surface.

### 8.1 Within one live session

`--add-dir` / `/add-dir` give genuine read/write reach across several repos with automatic path
resolution. Add `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` if you want their instruction files
loaded. **This is real and useful. It just does not survive resume.**

Transferable rule from the one practitioner source with a usable observation: **read and explore
wide, write narrow** — cross-repo read/explore, but the write should always be focused on a single
repo and a single PR.

### 8.2 Across resume — the losses, enumerated

| Restored on resume                                                                         | **Not restored**                                                          |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Full history including tool calls                                                          | `--mcp-config`                                                            |
| Model (with exceptions for retired models, `availableModels`, `--model`/`ANTHROPIC_MODEL`) | `--settings`                                                              |
| `--agent` identity (searched in original _and_ resume directory, v2.1.216+)                | `--plugin-dir`                                                            |
| Permission mode **except** `plan` and `bypassPermissions`, which are never restored        | `--fallback-model`                                                        |
| Active goal (turn count, timer, token baseline reset)                                      | **`--add-dir` directories, and `/add-dir` directories added mid-session** |
| Unexpired scheduled tasks                                                                  | Background Bash and monitor tasks                                         |
| Worktree location (interactive, `--continue`, `--resume` under `-p`, Agent SDK)            |                                                                           |

**Therefore: the startup recipe is the mechanism.** `<project>/.claude/start.sh` reconstructs
`--add-dir` set, MCP config, settings sources, and plugin dirs. Its exit test is the cold-start run
in H6. This is cheaper than any orchestrator and is the only thing that actually closes the gap.

**Also budget for the compaction dialog.** On Pro/Max, resuming a session inactive >1 hour and

> 100,000 tokens opens a choice: resume from summary (runs `/compact`: summary + recent exchanges +
> up to five recently read files), resume as-is (reprocesses and re-caches the full history), or don't
> ask again. **"Whatever the summary leaves out is no longer in Claude's context."** Cache lifetime is
> one hour on a subscription, five minutes on usage credits or API.

**Do not parse the JSONL.** Transcripts live at `~/.claude/projects/<project>/<session-id>.jsonl`,
and the docs state "the entry format is internal to Claude Code and changes between versions, so
scripts that parse these files directly can break on any release." Use `/export`,
`claude -p --resume <id> --output-format json`, or the `SessionEnd` hook's `transcript_path` field.

### 8.3 The checkpoint file

`CHECKPOINT.md` per project, written by the agent as work proceeds. It is now the **only durable
handoff for unattended runs**, and the reasons hardened during Phase B: `-p` sessions don't appear in
the session picker and **their worktrees are never auto-cleaned**; agent teams cannot resume
in-process teammates at all; `/add-dir` directories are not restored. The corpus's "batch 5–10 items
overnight" figure is **UNVERIFIED** — no source supports the batch size. Keep the checkpoint rule;
drop the number.

### 8.4 What not to build

| Tempting                                         | Why not                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shared `autoMemoryDirectory` across all projects | It is a supported override and it **collapses per-project isolation wholesale** — a confidentiality problem for client work (§9). It also does not solve the 200-line index cap; a shared index across N projects hits it faster, and everything past it is silently dropped                                     |
| Agent teams as a cross-project orchestrator      | One team per session, no cross-session sharing, no in-process teammate resume, no nested teams, fixed lead, experimental, ~7x tokens in plan mode                                                                                                                                                                |
| An MCP memory server                             | Several exist (mem0, Neo4j graph servers, self-hosted Qdrant/Ollama stacks) and **all the available material is vendor documentation or setup tutorials. No reliable evidence found** on whether any improves cross-project correctness, what it costs in context, or how it behaves under `/compact` (W2 Gap 4) |

---

## 9. ⚠ Client separation — the leak-path table

**Every mechanism that shares context across projects also shares it across clients**, and the
harness's own safety gate does not cover the user-scope path.

| Leak path                                 | Behaviour                                                                                                                                                             | Control                                                                                                  |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `~/.claude/CLAUDE.md`                     | Loaded in **every project on this machine**                                                                                                                           | Keep it generic-only. Nothing client-derived, ever                                                       |
| `~/.claude/rules/*.md`                    | "Apply to every project on this machine," loaded before project rules                                                                                                 | Same. Plus `claudeMdExcludes` (glob, any settings layer, arrays merge)                                   |
| Symlinked shared rule directories         | Deliberate cross-project sharing                                                                                                                                      | Only for generic conventions                                                                             |
| `@~/...` imports from a project CLAUDE.md | **Imports in user-scope memory files load without the approval dialog** — "files you wrote yourself… carry the same trust as the rest of your personal configuration" | The dialog protects only the project-scope case. This is the asymmetry to know                           |
| `autoMemoryDirectory` shared              | Single shared absolute path from any settings scope                                                                                                                   | Do not use across clients. Per-project `autoMemoryEnabled: false` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` |
| `--add-dir` across client repos           | One session reaches both                                                                                                                                              | Never add two clients' directories to one session                                                        |
| Third-party orchestrators                 | Closed-source binaries; one vendor's Pro tier adds a **cloud workspace**, which changes the data-residency picture entirely                                           | Treat as a subprocessor requiring the §10 instrument in `engagement-playbook.md`                         |

**Auto memory is written by Claude, not by the operator**, so its contents are never reviewed before
they are shared. **It therefore cannot be the layer where the client-boundary decision is enforced.**
Enforce at the directory boundary and with a `PreToolUse` hook that blocks writes crossing it.

**Default posture is on your side.** Auto memory is per-repo and machine-local by default,
`--add-dir` CLAUDE.md files are _not_ loaded by default, and cross-project session resume is
deliberately not in-place. **Every leak path above requires you to opt in.** The rule is simply: for
client work, do not.

---

## 10. Knowledge-repo variant

**State of the evidence, first.** **No controlled study of documentation-quality maintenance in a
code-free knowledge repository exists. Not one.** Every controlled study found uses a code
repository, a code-derived dependent variable, and a task terminating in executable output. **The
entire measured literature on agent context files depends on having a compiler or a test suite as
the oracle. A research repository has no oracle** (W4 Gap 1). Everything in this section is either
adjacent evidence, an inference explicitly labelled as one, or a mechanism to be built.

### What changes from the code variant

| Element               | Knowledge-repo setting                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Directory layout**  | **Type-first, not topic-first.** The one concrete code-free case study abandoned topic organisation because "a single performance issue touches tickets, code reviews, architecture docs, and incident reports — where does each artifact live? The answer was always ambiguous." Type prefixes into category folders; topics carried in frontmatter tags; auto-generated indexes at each level. Tier C: one person, one vault, six months, **no correctness metrics** |
| **Index convention**  | Partition at roughly **250 units per domain plus an index file**. Single-file context holds near-perfect navigation accuracy to ~1,000 units; partitioning holds it at 10,000 while keeping per-query context bounded. **Tier B and it is an analogy** — the units are database tables described in schema files and the task is SQL generation, not prose                                                                                                             |
| **Format**            | **Does not matter for accuracy** (χ² = 2.45, p = 0.484 across YAML/Markdown/JSON/TOON). It matters for cost: Markdown cost **+7% to +105% more tokens than YAML at equal information content**, because each grep hit returns denser output — the "grep tax." The index-file approach showed **no measurable grep-tax increase up to 10,000 units**                                                                                                                    |
| **Retrieval**         | **Track corpus size, not ambition.** BM25 remains a robust out-of-domain baseline that dense retrievers frequently fail to beat; graph/semantic advantages are a _scaling_ property, smallest at the small end. **No study evaluates retrieval over a few-hundred-document single-author corpus, and no study compares semantic search against plain grep at any scale.** For this operator: grep and a partitioned index, until measured otherwise                    |
| **CI**                | Link/anchor checking, prose linting, redirect checking. **Know the defaults**: MkDocs `--strict` does not check anchors by default; Docusaurus `onBrokenLinks` defaults to `throw` but `onBrokenAnchors` only to `warn`, and detection runs only on production builds; Sphinx nitpicky warnings **have not failed the build under `-W` since Sphinx 1.6**, so "we run nitpicky in CI" frequently gates nothing; lychee has fragment checking off by default            |
| **Instruction files** | Same content test. Note the one relevant primitive: outside a git repo, "the project root is used instead" for the auto-memory directory, so a non-git knowledge folder does get its own memory scope                                                                                                                                                                                                                                                                  |

**The hard limit on docs CI:** the entire mature docs-CI toolchain verifies links, anchors,
structure, prose style, and regeneration compliance. **None of it parses code or environment
semantics, so none of it can detect a well-formed sentence that is false.** The only code→docs check
found in any production CI is GitLab's `rubocop-docs`/`eslint-docs`, which check documentation links
referenced _from_ source. And even the prose-linting layer's value is asserted rather than measured —
the one org publishing its Vale experience at 20,000+ PRs/year reports **no quantified outcome**.

### The four failure modes this variant must actually handle

| Failure mode                                                                                                               | Measured reality                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | What to build                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stale environment assertions** (a rules file naming a model that isn't running; a reference to an uninstalled subsystem) | **Nothing in the measured literature detects this.** The referent is a runtime environment, not a symbol in the repo, so code-comment inconsistency detection does not apply. The nearest artifact is a _suggestion_ in a 2025 paper that researchers "design a linter for agent context files which could verify that the commands listed in the Build and Run section match the actual scripts in package.json or Makefile" — explicitly future work                                                                   | **This is the easy case.** Model names, installed plugins, and file paths are all machine-checkable. It is **unbuilt, not unbuildable.** Build a `PreToolUse` check                                                                                                                   |
| **Citation misgrounding**                                                                                                  | The operator's own documented base rate: **40 of 109 citations misstated** in a prior VA research pass. Automated support-checking tops out at ~**80% macro-F1** on a hard aggregated benchmark, and **no tool exists that audits an existing prose corpus for whether its citations support the claims attached to them** (W4 Gap 7)                                                                                                                                                                                    | The citation-verifier subagent. See §11 — this is the highest-value thing the operator could build                                                                                                                                                                                    |
| **Cross-document contradiction**                                                                                           | At least **3.3% of facts in English Wikipedia contradict another fact in the same corpus**; the best fully automated detector reaches only **75.1% AUROC**, while a **human-in-the-loop** system let editors find **64.7% more inconsistencies in the same time** (EMNLP 2025, authentic not synthetic contradictions, Tier A). Corroborating pessimism: LLM validators show **high precision but low recall** — conservative, missing real contradictions, which is the worse failure for a corpus you believe is clean | The consistency-checker subagent, run **human-in-the-loop**, never unattended. Wikipedia is multi-author; a single-author repo has a different contradiction-generating process (drift over time, not disagreement between authors), so the 3.3% may not transfer in either direction |
| **Drift as a steady state**                                                                                                | **28.9% of the 1,000 most-popular GitHub projects currently contain an outdated code-element reference**; 82.3% have had one at some point; **mean persistence 4.7 years**, ~55% survival after one month. Context files ratchet: median **57 words added per commit vs. under 15 deleted**, 67.4% modified in multiple commits, median Flesch Reading Ease **16.6** — the band of dense legal contracts                                                                                                                 | **Reframe the question.** Drift is not an event to be caught but a steady state to be budgeted for. Ask "what is the small set of assertions where drift is actually expensive?" — and the operator's own instances are all in the machine-checkable class                            |

### The design constraint on any checker you build

**Precision, not recall, is the axis that matters for a single reviewer.** Measured (Tier A):

| Approach                                                      | Flag rate | Precision / F1                      | Against a real base rate of ~11% |
| ------------------------------------------------------------- | --------- | ----------------------------------- | -------------------------------- |
| **Naive prompting** ("read these docs, tell me what's wrong") | **98%**   | F1 **0.22**                         | Unusable                         |
| Structured local categorisation + external filtering          | 14%       | F1 **0.77**                         | Usable                           |
| Broad four-language eval of the same method                   | 17%       | precision **0.63**                  | ~1 flag in 3 is noise            |
| **Grounding in generated tests**                              | —         | precision **0.88**, recall **0.21** | High precision, misses 79%       |

**A checker with a 30% noise rate is one the operator will stop reading, which is worse than not
having it.** And grounding in an executable check only works where documentation describes behaviour
expressible as a test — which excludes most prose and **all** of a knowledge repository. Neither
result licenses unattended operation.

Also relevant to trusting a "clean" corpus: **context-rot findings do not transfer down to
instruction-file scale** (the U-shape was tested at five positions inside a config file and did not
reproduce, quadratic component p = 0.94) — they bear on the _knowledge-repo_ case, where large
corpora are read into context, not on the CLAUDE.md case.

### Provenance schema

Use `domain-rampup.md` §6's `DOMAIN.md` schema. The single clause worth stealing from the four mature
provenance standards is **ICD 203's requirement to explain change to, or consistency with, previous
judgments** — nothing in FAIR, PRISMA 2020, or GRADE addresses assertion-level dating at all. Buy
auditability with it, not correctness; individual analysts have been measured applying ICD 203
**unreliably**, in an institution built around review gates the operator does not have.

**Enforce it at the file-write boundary, not in a CONTEXT.md.** Document conventions cannot be held
by instruction files across long runs any more than code conventions can (the 5.6%-per-function decay
is the same mechanism). `PostToolUse` hook or pre-commit check.

### CONTEXT.md per subject — status: unverified, and cheaply testable

C-140 is **UNVERIFIED** and C-142's "30–40% token reduction" target is **REFUTED** as stated (it was
never measured, and the closest real measurement runs the other way: +19–23% cost, with file length
showing no relationship to cost at all). The nearest relevant evidence is double-edged: context files
helped **only** in the ablation where all other documentation was stripped, and were otherwise
"redundant documentation" — and **a research subject directory is all documentation.**

**Cheapest experiment, one day:** run the same research task on two subject directories, one with and
one without a `CONTEXT.md`, and compare `/context` token counts and output quality. It is a
one-person A/B, not a research programme. Nobody has published it because nobody outside this use
case cares.

---

## 11. The one thing worth building that does not exist anywhere

**A measured citation-verification harness, built on the operator's own VA corpus.**

Every published source in the documentation workstream had to borrow its oracle from a compiler or a
test suite. **The operator would be building one.** The raw material is already there: a prior pass
found **40 of 109 citations misstated** — a labelled set with a known base rate, which is exactly
what none of the measured literature has for prose.

| Property                         | Why it matters                                                                                                                                                                                                                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Known base rate (40/109 ≈ 37%)   | Lets you compute precision and recall rather than guess at them                                                                                                                                                                               |
| Labelled set                     | The 40 are identified, so false negatives are measurable                                                                                                                                                                                      |
| Narrow domain, consistent format | The ~80% macro-F1 ceiling is a _general_ classifier's ceiling on a hard aggregated benchmark. **Nobody has measured a narrow, single-domain, consistent-format checker — a materially easier problem.** The gap cuts in the operator's favour |
| Repeatable and sellable          | It is a procedure, not a one-off — the only artefact in the entire research programme that is simultaneously a research contribution and a productised offer                                                                                  |

**What would settle it:** a measured false-negative rate for an adversarial citation-checking agent
run against a corpus with known planted errors. Design it for **precision** per §10's constraint.

---

## 12. Harness exit test

- [ ] `/context` shows only files that pass the content test
- [ ] Every hook has a named bottleneck, a named present signal, and a removal condition; each fires in <2s
- [ ] The roster is ≤6 subagents and ≤8 skills, each with a named triggering situation
- [ ] The reviewer subagent's mandate is correctness/requirements-only and its model is frontier-class
- [ ] No Tier Policy block, no `.cursorrules`, no swarm hook, no consumer-OAuth router remains
- [ ] CI green on a clean checkout in <10 min, every gate naming a real regression class
- [ ] Any AI step in CI is priced against the separate post-2026-06-15 credit pool
- [ ] `start.sh` passes the cold-start test for every project
- [ ] No client-affiliated repo appears in any §9 leak path
- [ ] The substantive-review log exists and has at least two weeks of entries
- [ ] For knowledge repos: the citation and consistency checkers run human-in-the-loop, never unattended, and are tuned for precision
