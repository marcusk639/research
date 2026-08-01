# W2 — Multi-project orchestration and shared context

_Phase B findings | Generated: 2026-08-01 | Sources consulted: 22 | Read in full: 13_

**Scope note.** The ledger (§5) records that W2 "has only partial coverage" in the corpus: the
corpus addresses one operator, one session, one repo, plus a two-machine batch/interactive split.
It does not address the operator_profile's desired topology — one orchestrator holding shared
context _across projects within one session_ — or session-resume/handoff mechanics. Seven claims
were assigned here. The rest of this file is open-field research, and the single most important
result is negative: **the desired topology is not a supported configuration in any harness I could
find primary evidence for, and Anthropic closed the feature request for it as "not planned."**

**Vendor-skepticism warning.** This subject area is unusually contaminated. A large fraction of
what ranks for "parallel AI agents," "multi-repo context," and "worktree orchestration" is either
(a) SEO content farms with no author accountability, or (b) vendor blogs whose case studies cite
each other in a loop. I traced one widely-quoted statistic (the "40% → <5% context drift" figure)
back through a vendor marketing post to its origin and flag the laundering explicitly in F-W2-05.

---

## Ledger Verdicts

| Claim ID | Verdict    | Current value / correction                                                                                                                                                                                                                                                                                                             | Evidence tier              | Source                                                                                                                                                                                                                                      | Notes                                                                                                                                                                                                                                                                                                                         |
| -------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C-046    | REFUTED    | No source documents a 2–3 ceiling. Nearest vendor guidance is **higher**: "Start with 3–5 teammates for most workflows"; `/batch` splits work across **5 to 30** worktree-isolated subagents                                                                                                                                           | A                          | [agent-teams](https://code.claude.com/docs/en/agent-teams), [agents](https://code.claude.com/docs/en/agents)                                                                                                                                | The embedded assertion "the documented practical ceiling" is false — nothing documents it. The prudential advice itself is separately UNVERIFIED (see C-076). Secondary content asserts 2–4 with no basis; one practitioner reports moving from 3 to "N" and reports no metrics either way.                                   |
| C-060    | STALE      | Mac-only ✓, closed-source ✓, but now drives **Claude Code, Codex _and Cursor_**, and is no longer purely free: Free $0 (BYO keys) / Pro $50/mo / Teams $60/mo/user / Enterprise custom, as of **2026-08-01**                                                                                                                           | A (pricing), B (ecosystem) | [conductor.build](https://conductor.build/), [conductor.build/pricing](https://conductor.build/pricing), [rustman.org](https://rustman.org/wiki/conductor-parallel-agents/)                                                                 | "Most practitioner-praised" is unmeasurable and now contestable: ≥7 competitors exist, several cross-platform and OSS (Superset Apache-2.0; Emdash MIT with Windows/Linux/SSH; Claude Squad; Vibe Kanban; ccswarm). **Could not verify** the "one-click PRs" and "Linear/GitHub integration" specifics from a primary source. |
| C-074    | STALE      | An external worktree orchestrator is no longer required for worktree lifecycle management. Claude Code ships `claude agents` (agent view, research preview), desktop-app auto-worktree per session, `/batch`, `isolation: worktree` subagent frontmatter, and `WorktreeCreate`/`WorktreeRemove` hooks                                  | A                          | [agents](https://code.claude.com/docs/en/agents), [worktrees](https://code.claude.com/docs/en/worktrees)                                                                                                                                    | The remaining differentiator for third-party orchestrators is cross-tool support (Codex/Cursor in one UI) and merge-review UI, not worktree management.                                                                                                                                                                       |
| C-076    | UNVERIFIED | —                                                                                                                                                                                                                                                                                                                                      | —                          | See F-W2-11                                                                                                                                                                                                                                 | No controlled study, no practitioner report with numbers, and no vendor documentation establishes an optimal lane count for a solo reviewer. Every figure found (2–4, 3–5, 5–30, "N", 10) is assertion. What would settle it: a within-operator trial measuring review latency and escaped-defect rate at 1/2/3/5 lanes.      |
| C-141    | CONFIRMED  | Pattern confirmed by three independent implementations; **filename correction**: `WORKFLOW.md` has no special status. Only `CLAUDE.md`, `./.claude/CLAUDE.md`, `.claude/rules/*.md`, `CLAUDE.local.md`, and `@path` imports auto-load                                                                                                  | A (loading), B (pattern)   | [memory](https://code.claude.com/docs/en/memory), [mabl](https://www.mabl.com/blog/how-we-built-a-system-for-ai-agents-to-ship-real-code-across-75-repos), [seylox](https://seylox.github.io/2026/03/05/blog-agents-meta-repo-pattern.html) | A root-level "active tracks / conventions / models in use" registry is exactly what mabl's Cross Repo Base and seylox's `AGENTS.md` + `repos.yaml` implement. But a file named `WORKFLOW.md` enters context only if imported or explicitly read — otherwise it is invisible to the agent.                                     |
| C-151    | REFUTED    | RAM is not the binding variable for cloud-model tiers. Worse, splitting machines has a **documented** cost: auto memory is machine-local — "Files are not shared across machines or cloud environments" — and `/usage` figures are "computed from local session history on this machine, so usage from other devices… is not included" | A                          | [memory](https://code.claude.com/docs/en/memory), [costs](https://code.claude.com/docs/en/costs)                                                                                                                                            | The mapping would hold only if a tier ran local inference. Every tier in the corpus's own routing scheme (Claude Max, OpenRouter) is cloud-hosted, so 48GB vs 24GB does not gate it. A two-machine split actively fragments accumulated project memory and usage visibility.                                                  |
| C-152    | CONFIRMED  | Checkpoint-file rule confirmed and reinforced by newly documented failure modes. **Batch size "5–10" is UNVERIFIED** — no source                                                                                                                                                                                                       | A                          | [sessions](https://code.claude.com/docs/en/sessions), [agent-teams](https://code.claude.com/docs/en/agent-teams), [worktrees](https://code.claude.com/docs/en/worktrees)                                                                    | An external progress file is now the _only_ durable handoff for unattended runs: `-p` sessions don't appear in the session picker and their worktrees are never auto-cleaned; agent teams cannot resume in-process teammates at all; `/add-dir` directories are not restored on resume.                                       |

**Counts:** 7 claims assigned, 7 verdicted — CONFIRMED 2, STALE 2, REFUTED 2, UNVERIFIED 1, SKIPPED 0.

## Contradiction Findings

**No contradiction in §3 of the ledger is assigned to W2.** X-01 → W1/W3, X-02 → W5, X-03 → W1/W4,
X-04 → W9/W5, X-05 → W5, X-06 → W1. Nothing to adjudicate here.

One adjacent tension worth flagging for Phase C without adjudicating it (it sits in W1/W9's lane):
the corpus's "cap at 2–3" and Anthropic's own "start with 3–5 teammates" are not directly
comparable — they count different objects (worktree sessions the operator drives vs. teammates a
lead drives) — but the corpus presents its number as documented, and the only actual documentation
points the other way. See C-046.

---

## Findings

### F-W2-01 — Claude Code supports multi-directory work within a live session but has no mechanism that makes a cross-project session durable; the feature request for one was closed as not planned.

- **Claim.** The operator's desired topology (one orchestrator holding shared context across
  several projects, surviving session resume) is achievable only for the lifetime of a single
  live process; every documented persistence path is scoped to one project directory or one git
  repository.
- **Evidence tier.** A (vendor documentation) + B (closed issue).
- **Support.** Read in full: [Manage sessions](https://code.claude.com/docs/en/sessions) and
  [How Claude remembers your project](https://code.claude.com/docs/en/memory). Specifics:
  - "Claude Code stores sessions per project directory." The picker shows sessions from the
    current worktree plus "sessions started elsewhere that added the current directory with
    `/add-dir`." `Ctrl+A` widens to every project on the machine — but "when you select a session
    from an unrelated project, Claude Code copies a `cd` and resume command to your clipboard
    instead" of resuming it. Cross-project resume is deliberately not in-place.
  - Resume does **not** restore `--add-dir` directories, `--mcp-config`, `--settings`,
    `--plugin-dir`, or `--fallback-model`; "directories added mid-session with `/add-dir` aren't
    restored either." So the multi-project workspace has to be reconstructed by hand on every
    resume, and nothing in the transcript records that it existed.
  - `--add-dir` does **not** load the added directory's CLAUDE.md by default; that requires
    `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`.
  - Anthropic issue [#38309](https://github.com/anthropics/claude-code/issues/38309), requesting
    an `/add-folder` command with multiple workspace roots, multiple CLAUDE.md loading, cross-folder
    Glob/Grep/Read, and multi-repo git context, is **closed as not planned**.
- **Date sensitivity.** High. Session/`--add-dir` behavior is version-gated (the docs cite
  behavior changes at v2.1.196, .198, .206, .208, .211, .212, .216). Re-check before relying on
  any specific restore behavior; verified 2026-08-01.
- **Confidence.** High for the mechanics (primary vendor docs, read in full). Medium for the
  "not planned" signal — a closed issue is weak evidence of long-run product direction.
- **Counter-evidence.** Real partial support exists and should not be dismissed: `--add-dir` /
  `/add-dir` genuinely give one session read/write reach across several repos with automatic path
  resolution; `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` pulls their instruction files in;
  the picker's `Ctrl+A` does enumerate everything on the machine. The gap is durability across
  resume, not reach within a session.

### F-W2-02 — Persistent auto memory is scoped to one git repository and to one machine, and only the first 200 lines / 25KB of its index loads.

- **Claim.** Claude Code's automatic cross-session memory does not cross project boundaries or
  machine boundaries by default, and its always-loaded portion is hard-capped.
- **Evidence tier.** A.
- **Support.** [Memory docs](https://code.claude.com/docs/en/memory), read in full: "Each project
  gets its own memory directory at `~/.claude/projects/<project>/memory/`. The `<project>` path is
  derived from the git repository, so all worktrees and subdirectories within the same repo share
  one auto memory directory." And: "Auto memory is machine-local… Files are not shared across
  machines or cloud environments." Loading: "The first 200 lines of `MEMORY.md`, or the first
  25KB, whichever comes first, are loaded at the start of every conversation. Content beyond that
  threshold is not loaded at session start." Topic files are read on demand only. Subagents do not
  inherit the main conversation's auto memory (except `/subtask` forks).
  There **is** a supported override: `autoMemoryDirectory` in settings (any scope) can point every
  project at one shared directory.
- **Date sensitivity.** Medium-high. The 200-line/25KB limits and the `modified` frontmatter
  timestamp are recent additions (v2.1.210, .211, .214). Verified 2026-08-01.
- **Confidence.** High — primary documentation, unambiguous.
- **Counter-evidence.** The `autoMemoryDirectory` override means cross-project shared memory is
  achievable without third-party tooling. But it collapses per-project isolation wholesale, which
  is a confidentiality problem for client work (see F-W2-14), and it does not solve the 200-line
  index cap — a shared index across N projects hits that cap faster, and everything past it is
  silently dropped on load.

### F-W2-03 — Every documented cross-project context mechanism in Claude Code is static file loading, not shared state, and each one costs context on every session in every project.

- **Claim.** Cross-project context is carried by files loaded at launch — user-scope CLAUDE.md,
  user-scope and symlinked rules, `@path` imports — with no runtime state shared between
  concurrently running project sessions.
- **Evidence tier.** A.
- **Support.** [Memory docs](https://code.claude.com/docs/en/memory) (read in full). The four
  mechanisms that actually reach across projects:
  1. `~/.claude/CLAUDE.md` — loaded in every project on the machine.
  2. `~/.claude/rules/*.md` — "apply to every project on this machine," loaded before project rules.
  3. Symlinks: "`ln -s ~/shared-claude-rules .claude/rules/shared`" — a maintained shared rule set
     linked into multiple projects; circular symlinks are handled.
  4. `@~/.claude/my-project-instructions.md` imports from a project CLAUDE.md — the documented
     way to share personal instructions across worktrees, since a gitignored `CLAUDE.local.md`
     exists only in the worktree that created it.
     Cost is explicit: "CLAUDE.md files are loaded into the context window at the start of every
     session"; "target under 200 lines per CLAUDE.md file. Longer files consume more context and
     reduce adherence"; and imports do not help — "imported files still load and enter the context
     window at launch." Path-scoped rules (`paths:` frontmatter) are the only documented way to
     defer loading.
- **Date sensitivity.** Low-medium. Hierarchy is stable; the `/doctor` CLAUDE.md trim check
  (v2.1.206) and `claudeMdExcludes` are newer. Verified 2026-08-01.
- **Confidence.** High.
- **Counter-evidence.** Two runtime-state mechanisms do exist, but neither crosses projects: the
  agent-team shared task list at `~/.claude/tasks/{team-name}/` (persists across resume) and the
  mailbox at `~/.claude/teams/{team-name}/inboxes/`. Both are keyed to a session-derived team name
  and the docs state "a session has exactly one team, scoped to that session. You can't create
  additional named teams or share a team across sessions." MCP servers can serve shared state
  across projects, but I found no primary-source evaluation of any of them (see Gaps).

### F-W2-04 — Worktrees isolate files; they do not isolate decisions, and the reported cross-lane failure mode is semantic, not textual.

- **Claim.** File-level isolation moves conflict from edit time to merge time and does nothing
  about divergent design decisions, duplicated helpers, and interface drift.
- **Evidence tier.** B (independent practitioner analysis) / C (unattributed aggregations).
- **Support.** João Camarate, ["Keeping context and decisions consistent across parallel AI
  agents"](https://dev.to/jcamarate/keeping-context-and-decisions-consistent-across-parallel-ai-agents-32nj)
  (read in full; independent — founder of defract.dev, not vendor content for a worktree tool).
  He decomposes drift into three kinds with different remedies: durable decisions (architecture,
  naming), current contracts (interface shapes changing during the work), and in-flight state
  (concurrent modifications). His diagnosis of the root cause: when "agent A decides 'we use the
  repository pattern for data access,' that decision exists in exactly two places: agent A's
  context, and your head. Agent B never hears about it." The highest-rated comment sharpens it
  into a rule of thumb — "prose for durable things, types for changing things, task boundaries for
  concurrent things."
  Corroborating, from the 2026 orchestrator ecosystem survey at
  [rustman.org](https://rustman.org/wiki/conductor-parallel-agents/) (read in full): "the moment
  two lanes need to modify overlapping code, worktree isolation doesn't save you — you get six
  drift-parallel solutions to the same problem," and success "requires non-overlapping task
  decomposition — a senior engineering skill, not a tool feature."
  Anthropic's own docs say the same thing for teams: "Agent teams don't isolate teammates in
  worktrees, so partition the work so each teammate owns a different set of files," and "Two
  teammates editing the same file leads to overwrites."
- **Date sensitivity.** Low — this is a structural property, not a figure.
- **Confidence.** Medium-high. Multiple independent sources converge on the same mechanism, but
  none quantifies a rate.
- **Counter-evidence.** No source measures how often this happens, how much review time it costs,
  or whether it scales with lane count. Camarate reports no metrics and no case studies; he is
  explicit that this is empirical observation. The claim that "git catches line-level conflicts
  immediately" also means a meaningful share of the damage _is_ caught mechanically.

### F-W2-05 — The only reported before/after measurement of cross-project cohesion comes from one company's self-reported internal metrics, is not solo-operator scale, and is being laundered through vendor marketing.

- **Claim.** mabl reports that a 79-repo "Repo Coordination Graph" cut context drift from ~40% of
  agent failures to <5%; the figure is internally measured, undefined, unverified, and is now
  circulating detached from its caveats.
- **Evidence tier.** B (company engineering blog with concrete architecture and dates) — **not** A.
- **Support.** Primary: mabl, ["How We Built a System for AI Agents to Ship Real Code Across 75+
  Repos, Part 1"](https://www.mabl.com/blog/how-we-built-a-system-for-ai-agents-to-ship-real-code-across-75-repos)
  (April 2026; read in full). Reported: 25 engineers, 100+ repos, an 850+-line Repo Coordination
  Graph covering 79 repositories with dependency graphs, Pub/Sub topic maps, database table
  ownership and prescribed release ordering; a "Cross Repo Base" pseudo-monorepo above the
  individual repos; git worktrees with **hooks that prevent agents editing files in the wrong
  workspace**; ~40 skills and 3 MCP servers; AI code review restricted to REQUEST_CHANGES/COMMENT
  with humans approving all merges; auto-fix agents with circuit breakers.
  Numbers with dates: AI-assisted commits ~10% (Aug 2025) → 39% overall and 60% in infra repos
  (Feb 2026); PR volume 230/month (Aug 2025) → 370+/month (pacing, April 2026); context drift
  "~40% of our failures to <5%."
  Laundering: [riftmap.dev](https://riftmap.dev/blog/ai-coding-agents-need-cross-repo-context/)
  (read in full) re-reports mabl's numbers alongside a Meta "30x token reduction" figure and a solo
  operator's 15-repo anecdote, as evidence for **Riftmap's own cross-repo dependency-graph API**.
  The article is authored by Riftmap's founder. Anyone encountering the 40%→<5% figure via search
  is likely to hit the vendor version first.
- **Date sensitivity.** High. All figures are stamped Aug 2025 – April 2026 and describe an
  organization mid-adoption; they will drift.
- **Confidence.** Medium on the architecture (specific, internally consistent, plausibly
  reproducible). **Low** on the 40%→<5% figure: no operational definition of a "context drift
  failure," no measurement method, no third-party verification, and it is a bundled intervention —
  the graph shipped alongside worktree hooks, 40 skills, AI review and circuit breakers, so no
  component's contribution is isolable.
- **Counter-evidence.** The scale is wrong for the operator: 25 engineers and 100+ repos is a
  different regime from one person and a handful of projects, and much of mabl's machinery
  (release ordering, table ownership, Pub/Sub maps) exists to coordinate _people_, not projects.
  mabl's Part 2 is titled to cover "where agents still break" — the failure inventory, which would
  be the more useful half, was not read here.

### F-W2-06 — The best-evidenced solo-operator pattern for cross-project cohesion is a "meta-repo": one entry-point instruction file plus a machine-readable repository registry.

- **Claim.** An independent single operator running six repositories reports that a dedicated
  meta-repository containing an `AGENTS.md` repo map, a `repos.yaml` machine-readable registry,
  shared conventions, workflows and scripts prevented per-session re-exploration and let a
  single change span six repos across five sessions.
- **Evidence tier.** B — reproducible detail, one individual, no metrics. **Flagged: single
  individual's experience.**
- **Support.** [The agents meta-repository pattern](https://seylox.github.io/2026/03/05/blog-agents-meta-repo-pattern.html)
  (read in full). Six repos: two native platforms (Android, iOS) and four cross-platform wrappers
  (Flutter, React Native, Cordova, .NET). Without it, agents "start over. From scratch. Exploring
  directory structures it had explored yesterday." Components: `AGENTS.md` as entry point
  containing "a repository map: a table listing every repo with its path, purpose, languages, and
  build system," plus three standing instructions (verify documented information against reality;
  update when inaccuracies surface; suggest improvements); `repos.yaml` giving paths, build
  commands and version file locations as structured data; conventions/workflows/scripts
  directories. Reported outcome: an eight-merge-request, six-repository fix completed across five
  sessions without losing context.
  Converging independently, [karun.me](https://karun.me/blog/2026/03/26/structuring-claude-code-for-multi-repo-workspaces/)
  (read in full) proposes a three-layer CLAUDE.md hierarchy — org-level at workspace root,
  team-level per directory, repo-level per repo — with service repos gitignored inside a tracked
  bootstrap repo (`orders/*` + `!orders/CLAUDE.md`), and `mani` for selective multi-repo sync.
- **Date sensitivity.** Low.
- **Confidence.** Medium. Two independent implementations converge on the same shape, and mabl's
  Cross Repo Base is a third at larger scale. But it is a design pattern with no comparative data.
- **Counter-evidence.** The seylox author's own caveats: "None of this is a silver bullet";
  documentation drift is real and the "immune system" (agents instructed to verify and update)
  "still requires discipline"; the pattern "may become obsolete as models improve"; per-repository
  documentation is still necessary. The karun.me post is weaker than it looks: it does not say what
  broke to motivate the design, gives no token-cost or session-resume analysis, and reports no
  comparative data — it is a layout proposal, not a result. Neither author addresses whether the
  registry itself drifts.

### F-W2-07 — Agent teams are the nearest built-in to "one orchestrator with shared context," and they explicitly do not provide it.

- **Claim.** In an agent team the lead's context is not shared with teammates, the team cannot span
  sessions or projects, and in-process teammates cannot survive a resume.
- **Evidence tier.** A.
- **Support.** [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)
  (read in full). Directly: "Each teammate has its own context window… The lead's conversation
  history does not carry over." A teammate loads CLAUDE.md, MCP servers and skills from its working
  directory plus the lead's spawn prompt, nothing else. Documented limitations: "**No session
  resumption with in-process teammates**: `/resume` and `/rewind` do not restore in-process
  teammates. After resuming a session, the lead may attempt to message teammates that no longer
  exist." "**One team per session**: a session has exactly one team, scoped to that session. You
  can't create additional named teams or share a team across sessions." "**No nested teams.**"
  "**Lead is fixed.**" Teams are "experimental and disabled by default"
  (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Sizing guidance: "Start with 3-5 teammates for most
  workflows… Having 5-6 tasks per teammate… Three focused teammates often outperform five
  scattered ones." Cost: teams "use approximately 7x more tokens than standard sessions when
  teammates run in plan mode" ([costs](https://code.claude.com/docs/en/costs), read in full).
  Also relevant to unattended running: "Letting a team run unattended for too long increases the
  risk of wasted effort," and "Teammates may stop after encountering errors instead of recovering."
- **Date sensitivity.** High — explicitly experimental, documented against v2.1.178–.199 behavior,
  with tool removals (`TeamCreate`/`TeamDelete`) already in the changelog. Verified 2026-08-01.
- **Confidence.** High.
- **Counter-evidence.** Teams do provide genuine shared runtime state that subagents do not: a
  shared task list with file-locked claiming, automatic dependency unblocking, and direct
  teammate-to-teammate messaging. The task list directory "persists locally and is never uploaded,
  so resumed sessions keep their tasks" — so task state, unlike teammates, does survive resume.
  Quality gates are available via `TeammateIdle`, `TaskCreated` and `TaskCompleted` hooks (exit
  code 2 to block and send feedback).

### F-W2-08 — What detects a cross-project cohesion break, on the available evidence, is deterministic machinery — hooks, types, CI, and dependency-graph queries — not prose instructions.

- **Claim.** Every cohesion-preservation mechanism in the record that has any evidence behind it is
  machine-enforced; the prose-only mechanisms are reported as insufficient by their own authors.
- **Evidence tier.** B, assembled from several sources; no single controlled test.
- **Support.**
  - Hooks over instructions, from the vendor: "Claude treats them as context, not enforced
    configuration. To block an action regardless of what Claude decides, use a PreToolUse hook
    instead" ([memory](https://code.claude.com/docs/en/memory)). And CLAUDE.md "content is
    delivered as a user message after the system prompt… there's no guarantee of strict compliance."
  - mabl's concrete instance: git worktrees "with hooks preventing agents from editing files in
    the wrong workspace" — a mechanical guard against exactly the cross-lane contamination in
    F-W2-04 ([mabl](https://www.mabl.com/blog/how-we-built-a-system-for-ai-agents-to-ship-real-code-across-75-repos)).
  - Types over prose, from the practitioner discussion: "prose for durable things, types for
    changing things, task boundaries for concurrent things" — i.e. put changing interface contracts
    in the type system and CI, not in a CLAUDE.md ([Camarate](https://dev.to/jcamarate/keeping-context-and-decisions-consistent-across-parallel-ai-agents-32nj)).
  - Graph queries for merge ordering: mabl's Repo Coordination Graph is queried by the agent "to
    determine which repos need updates and what the merge order should be" (upstream libraries
    before consumers).
  - A CI job that verifies documented paths and commands still exist is reported as an emerging
    drift-detection practice, but I found it only in aggregated secondary content, not in a primary
    implementation report — treat as C-tier and see W4's lane for doc-drift detection proper.
  - Instruction-file diagnostics that exist and are cheap: `/context` shows which memory files
    actually loaded; the `InstructionsLoaded` hook logs "exactly which instruction files are
    loaded, when they load, and why"; `/doctor` (v2.1.206+) proposes trims for a checked-in
    CLAUDE.md.
- **Date sensitivity.** Medium — the specific hooks and `/doctor` behavior are version-gated;
  verified 2026-08-01.
- **Confidence.** Medium. The direction is well-supported and the vendor states the enforcement
  gap in its own docs; but no source isolates the effect of any single mechanism, and mabl's
  improvement is a bundle of at least five interventions shipped together.
- **Counter-evidence.** Nothing found argues that prose context files are useless — seylox reports
  that a prose repo map plus an "update when you find drift" instruction was sufficient for six
  repos, and Anthropic's own remedy for the CLAUDE.md compliance gap is mostly "write more specific
  instructions," not "use hooks for everything." Hooks also cannot detect semantic duplication
  (two correct-but-redundant helpers in different repos), which is the failure mode F-W2-04
  identifies as most damaging.

### F-W2-09 — Third-party worktree orchestrators have been substantially commoditized by Claude Code's own parallelism surface.

- **Claim.** As of 2026-08-01, worktree creation, per-agent isolation, background dispatch,
  monitoring and cleanup ship natively; third-party orchestrators differentiate on cross-tool UI,
  not on the worktree mechanics the corpus credited them with.
- **Evidence tier.** A.
- **Support.** [Worktrees](https://code.claude.com/docs/en/worktrees) and
  [Run agents in parallel](https://code.claude.com/docs/en/agents), both read in full:
  - `claude --worktree <name>` / `-w`, worktrees under `.claude/worktrees/<name>/` on branch
    `worktree-<name>`; `EnterWorktree`/`ExitWorktree` tools; `--worktree "#1234"` to branch from a PR.
  - `.worktreeinclude` (gitignore syntax) copies gitignored files such as `.env` into every new
    worktree — including subagent worktrees and desktop parallel sessions.
  - Cleanup: clean unnamed worktrees auto-remove on exit; those with work prompt; a periodic sweep
    removes subagent and background-session worktrees older than `cleanupPeriodDays`, skipping any
    that hold changes; running agents get `git worktree lock`. **`-p` runs are never cleaned up.**
  - `isolation: worktree` in subagent frontmatter makes isolation permanent for that subagent.
  - `claude agents` (agent view, research preview) "moves each dispatched session into its own
    worktree automatically."
  - "In the desktop app, every new session gets its own worktree automatically."
  - `/batch` "has Claude split one large change into 5 to 30 worktree-isolated subagents that each
    open a pull request."
  - `WorktreeCreate`/`WorktreeRemove` hooks replace git logic entirely for SVN/Perforce/Mercurial.
  - Shared across worktrees of one repo: the `.git` directory, project-scope plugins (v2.1.200+),
    and permission approvals (v2.1.211+ — an approval in a worktree now saves to the main
    checkout's `.claude/settings.local.json` and survives the worktree's removal).
    Ecosystem state from [rustman.org](https://rustman.org/wiki/conductor-parallel-agents/): Superset
    (Apache-2.0, cross-platform, agent-agnostic), Emdash (MIT, macOS/Linux/Windows + SSH, Linear/Jira),
    Claude Squad (OSS, tmux + worktrees), Vibe Kanban, ccswarm, Parallel Code, Agent Orchestrator.
- **Date sensitivity.** High — agent view is a research preview; `/batch` and desktop behavior are
  recent. Verified 2026-08-01.
- **Confidence.** High for the native capabilities (primary docs). Medium for the ecosystem
  inventory (one secondary survey; I could not independently verify each tool's license/platform).
- **Counter-evidence.** Orchestrators still do things Claude Code does not: drive Codex and Cursor
  agents from the same UI, present side-by-side diff review across lanes, and give a non-terminal
  interface. Conductor supports Claude Code, Codex and Cursor together
  ([conductor.build](https://conductor.build/)).

### F-W2-10 — Conductor's commercial and platform position has changed since the corpus asserted C-060.

- **Claim.** Conductor is Mac-only, closed-source, now supports three agent CLIs, and now has paid
  tiers above a free BYO-keys tier.
- **Evidence tier.** A (vendor's own site, for its own product — marked as such).
- **Support.** [conductor.build](https://conductor.build/) — "Run parallel coding agents on your
  Mac"; "Claude Code, Codex, and Cursor agents" in isolated workspaces.
  [conductor.build/pricing](https://conductor.build/pricing), fetched **2026-08-01**: Free $0
  ("Run multiple coding agents in parallel", "Bring your own subscriptions and keys"); Pro $50/mo
  (cloud workspace, multiplayer); Teams $60/mo/user (admin controls, centralized billing);
  Enterprise custom. Closed-source, Apple-Silicon-only, Melty Labs ($22M Series A), per
  [rustman.org](https://rustman.org/wiki/conductor-parallel-agents/).
- **Date sensitivity.** Very high — pricing page, read 2026-08-01. Assume stale within a quarter.
- **Confidence.** High for platform and pricing (primary). Low for "most practitioner-praised" —
  that is not a measurable property and I found no ranking, survey, or download/star comparison
  that supports it.
- **Counter-evidence.** I **could not verify** the corpus's specific feature claims of "one-click
  PRs" and "Linear/GitHub integration" from a primary source; the homepage fetch surfaced no
  integrations section. Emdash is the tool the ecosystem survey credits with "first-class
  Linear/Jira integration," which raises the possibility the corpus attributed a competitor's
  feature to Conductor. Treat those two sub-claims as UNVERIFIED.

### F-W2-11 — No reliable evidence found for an optimal number of concurrent agent lanes for a solo reviewer.

- **Claim.** Every published number is an assertion. There is no controlled study, no
  practitioner report with a measured review-throughput or defect curve, and no vendor data.
- **Evidence tier.** C for every figure found; the finding itself is a negative result.
- **Support.** The full inventory of numbers I could locate:
  - 2–3: the corpus's own claim, presented as "documented," with no cited source (C-046/C-076).
  - 2–4: asserted by SEO content (mindstudio.ai) with no author, method or data. C-tier.
  - 3–5 teammates: Anthropic, [agent-teams](https://code.claude.com/docs/en/agent-teams) — reasoned
    from token cost, coordination overhead and diminishing returns, but no measurement offered.
  - 5–30 subagents: Anthropic's `/batch` skill range, [agents](https://code.claude.com/docs/en/agents)
    — an engineering parameter, not a review-capacity claim.
  - "N": Laurent Kempé, ["From 3 Worktrees to N"](https://laurentkempe.com/2026/03/31/from-3-worktrees-to-n-ai-powered-parallel-development-on-windows/)
    (read in full) — reports **zero** quantitative data on review time, merge conflicts or
    throughput; his actual constraint was terminal management (accidentally closing tabs running
    agents), solved with a multiplexer; his stated rule is qualitative — "Not every task needs an
    agent… a five-line config change doesn't need an autonomous agent."
  - 10 agents / 15+ repos: a dev.to post promoting the author's own tool (`ttal`) — treat as vendor.
    Its one transferable observation: "when you need cross-repo context, you need cross-repo read
    and explore, but the write should always be focused on a single repo and a single PR."
  - The one repeatedly-described qualitative failure: dispatching more overnight work than can be
    reviewed the next morning, producing a growing backlog of stale branches that conflict with
    newer work.
- **Date sensitivity.** Low — the absence of evidence is not a dated figure.
- **Confidence.** High that the evidence does not exist; medium that I found everything (search
  budget was exhausted before I could sweep academic sources).
- **Counter-evidence.** The _direction_ is broadly agreed on across independent sources: review
  capacity binds before agent capacity, and read/explore parallelizes better than write. Nobody
  disputes that. What nobody supplies is a number.

### F-W2-12 — Session resume carries substantial state across sessions, with an enumerated and non-obvious set of losses; the losses are where multi-project cohesion breaks.

- **Claim.** Resume restores conversation, model, agent, permission mode, active goal, scheduled
  tasks and worktree location, but silently drops the configuration that defines a multi-project
  workspace.
- **Evidence tier.** A.
- **Support.** [Manage sessions](https://code.claude.com/docs/en/sessions), read in full.
  Restored: full history including tool calls; model (with named exceptions for retired models,
  `availableModels`, `--model`/`ANTHROPIC_MODEL`, and provider deployment IDs); `--agent` identity
  (searched in the session's original directory _and_ the resume directory, v2.1.216+); permission
  mode except `plan` and `bypassPermissions`, which are never restored; active goal (with turn
  count, timer and token-spend baseline reset); unexpired scheduled tasks — but **not** background
  Bash or monitor tasks. Worktree location is restored for interactive resume, `--continue`,
  `--resume` under `-p`, and the Agent SDK.
  Not restored: `--mcp-config`, `--settings`, `--plugin-dir`, `--fallback-model`, and `--add-dir`
  directories — nor `/add-dir` directories added mid-session.
  Cost mechanics: on Pro/Max, resuming a session inactive >1 hour and >100,000 tokens opens a
  dialog — resume from summary (runs `/compact`: summary + recent exchanges + up to five recently
  read files), resume as-is (reprocesses and re-caches the full history), or don't ask again.
  "Whatever the summary leaves out is no longer in Claude's context." Cache lifetime is one hour on
  a subscription, five minutes on usage credits or API ([costs](https://code.claude.com/docs/en/costs)).
  Resume by name resolves across the current repository and its worktrees; sessions created with
  `claude -p` or the Agent SDK do not appear in the picker at all, and their session-ID lookup is
  "scoped to the current project directory and its git worktrees."
  Transcripts: JSONL at `~/.claude/projects/<project>/<session-id>.jsonl`; "the entry format is
  internal to Claude Code and changes between versions, so scripts that parse these files directly
  can break on any release."
- **Date sensitivity.** High — version-gated behavior at v2.1.169, .191, .196, .198, .211, .212,
  .216. Verified 2026-08-01.
- **Confidence.** High.
- **Counter-evidence.** Cheap mitigations exist and are documented: `/branch` and `--fork-session`
  copy a conversation without losing the original; `/rename` before `/clear` makes a session
  findable; `/export` and `claude -p --resume <id> --output-format json` give scriptable handoff
  output; a `SessionEnd` hook can archive the transcript via the `transcript_path` field. The
  documented instruction to parse transcripts only through `/export` or the script interfaces —
  not the JSONL — is a real constraint on building your own handoff tooling.

### F-W2-13 — The code-free knowledge-repository case is essentially unaddressed in published multi-project orchestration guidance; the only concrete evidence is single-operator and unmeasured.

- **Claim.** No published work treats a code-free knowledge repo as a first-class node in a
  multi-project agent topology; the nearest evidence is individual Obsidian/git + agent setups.
- **Evidence tier.** C — single individuals, self-reported, no metrics bearing on correctness.
- **Support.** [Kevin Davison, "How I Turned My Git Repo Into a Self-Organizing Knowledge Base"](https://www.quevin.ai/blog/2026-03-27-obsidian-agent-knowledge-base)
  (read in full). Two layers over a shared `.markdown/` directory: Obsidian as the human layer
  (graph, backlinks, tags) and a Claude Code agent defined at `.claude/agents/docs-organizer.md`
  as the organization engine. The load-bearing design decision is **type-first taxonomy over
  topic-first**: topic organization was abandoned because "a single performance issue touches
  tickets, code reviews, architecture docs, and incident reports. Where does each artifact live?
  The answer was always ambiguous." Type prefixes (JIRA, DOC, CR, ASM, INC, RB, SW) into category
  folders; topics carried in YAML frontmatter tags; auto-generated indexes at each hierarchy
  level; controlled tag vocabularies; a human approval gate on file migrations (agent proposes,
  human decides). Reported after six months: ~77 categorized documents (vs. 40 before), search
  "seconds instead of minutes."
- **Date sensitivity.** Low.
- **Confidence.** Low. One person, one vault, no comparative measurement, and the reported outcomes
  (document count, subjective search time) do not measure the property that matters for a
  consulting knowledge repo — whether its content is _correct and non-contradictory_.
- **Counter-evidence.** The author's own warning is the strongest counter-evidence available:
  "Get the agent definition wrong and you've automated the creation of a mess." He also reports
  no mechanism for contradiction detection beyond frontmatter discipline. Anthropic's memory docs
  supply the one relevant primitive — outside a git repo, "the project root is used instead" for
  the auto-memory directory, so a non-git knowledge folder does get its own memory scope — but
  every other cross-project mechanism in F-W2-03 assumes a repository. Contradiction detection
  across prose repos belongs to W4's lane; I did not research it.

### F-W2-14 — Every mechanism that shares context across projects also shares it across clients, and the harness's own safety gate does not cover the user-scope path.

- **Claim.** Shared `autoMemoryDirectory`, user-scope CLAUDE.md/rules, symlinked rule directories,
  `@~/` imports and `--add-dir` across client repos each create a path by which one client's
  material can reach another client's session; the documented approval dialog protects only the
  project-scope case.
- **Evidence tier.** A for the mechanisms; the risk characterization is inference and is flagged
  again in Implications.
- **Support.** [Memory docs](https://code.claude.com/docs/en/memory): an import in a project-level
  memory file resolving outside the working directory triggers a one-time approval dialog listing
  the files — but "imports in user-scope memory files, such as `~/.claude/CLAUDE.md` and
  `~/.claude/rules/`, are files you wrote yourself, so they load without the dialog and carry the
  same trust as the rest of your personal configuration." `~/.claude/rules/*.md` "apply to every
  project on this machine." `autoMemoryDirectory` accepts a single shared absolute path from any
  settings scope. Auto memory is written by Claude, not by the operator, so its contents are not
  reviewed before they are shared.
  Available scoping controls: `claudeMdExcludes` (glob, any settings layer, arrays merge);
  `--setting-sources` to exclude `project` or `local`; per-project `autoMemoryEnabled: false`;
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`; `autoMemoryDirectory` in a project's settings is honored
  "only after you accept the workspace trust dialog for that folder."
  Third-party orchestrators add a separate surface: Conductor is a closed-source binary
  ([rustman.org](https://rustman.org/wiki/conductor-parallel-agents/)), though it runs locally
  post-clone "with no SaaS intermediary" — and the same survey notes it identifies "no explicit
  security vulnerabilities" and does not discuss API-key management or permission scoping at all,
  which is itself a gap rather than an assurance. Conductor's Pro tier adds a **cloud workspace**,
  which would change the data-residency picture.
- **Date sensitivity.** Medium.
- **Confidence.** High that the mechanisms behave as documented. The risk assessment is my
  inference.
- **Counter-evidence.** The controls above are real and granular, and Claude Code's default
  posture is isolation — auto memory is per-repo and machine-local by default, `--add-dir`
  CLAUDE.md files are _not_ loaded by default, and cross-project session resume is deliberately
  not in-place. Every leak path in this finding requires the operator to opt in.

---

## Gaps

1. **No controlled or even self-measured study of lane count vs. solo review capacity.** Nothing
   found measures review latency, escaped-defect rate, or rework as a function of concurrent
   agent lanes for one reviewer. What would settle it: a within-operator A/B over ≥4 weeks
   logging, per lane count, time-to-first-review, review minutes per merged change, and defects
   found post-merge. Nobody has published this. Every number in circulation (2–3, 2–4, 3–5, N, 10)
   is assertion.
2. **No measurement of cross-project drift for a solo operator.** The only before/after number is
   mabl's ~40%→<5%, from 25 engineers across 79 repos, internally measured, with no operational
   definition of the metric and five interventions bundled together (F-W2-05). Nothing exists at
   one-person scale.
3. **No evidence either way on whether one orchestrator session across N projects beats N
   sessions.** No study, no practitioner report with numbers, and the product direction is against
   it — Anthropic closed the `/add-folder` multi-workspace-root request as not planned. What would
   settle it: someone running both topologies on comparable work and reporting context cost,
   cross-project error rate, and reviewer time.
4. **MCP-served cross-project state is unevaluated.** Several memory MCP servers exist (mem0,
   Neo4j-graph servers, self-hosted Qdrant/Ollama stacks) and all the material I found for them is
   vendor documentation or setup tutorials. **No reliable evidence found** on whether any of them
   improves cross-project correctness, what they cost in context, or how they behave under
   `/compact`. What would settle it: an independent evaluation measuring task success with and
   without the memory server on the same repo set.
5. **Cohesion detection for code-free knowledge repos.** No published mechanism analogous to CI
   exists for detecting contradictions across prose repositories. The one relevant source
   (F-W2-13) explicitly has none. This is partly W4's lane; flagged so Phase C does not assume W2
   covered it.
6. **Two unverified sub-claims in C-060.** Conductor's "one-click PRs" and "Linear/GitHub
   integration" could not be confirmed from any primary source, and a competitor (Emdash) is the
   tool credited with first-class Linear/Jira integration. Possible mis-attribution in the corpus.
7. **Search budget exhausted before an academic sweep.** I did not reach arXiv/ACM for work on
   multi-agent coordination cost or developer context-switching under agentic tooling. Two arXiv
   preprints surfaced incidentally in search results (on context rot in AI configuration
   artifacts, and a census of AI coding agents across 180M repositories) and were **not** read.
   They are the highest-value unopened leads for this workstream.
8. **Whether a two-machine split shares one quota.** I established that auto memory and `/usage`
   accounting are machine-local, which is enough to refute C-151's premise. Whether the plan quota
   itself pools across devices is C-030/C-066's question and belongs to W1 — I did not research it.

---

## Implications for the Operator

_My inferences, not findings. Phase C reasons over the evidence above._

- The desired topology has to be **built, not configured**. Nothing ships it. The buildable
  substitute that the evidence supports is a meta-repo (F-W2-06) — one workspace root holding an
  entry-point instruction file, a machine-readable project registry, shared conventions, and the
  per-project repos beneath it — combined with a shared `autoMemoryDirectory` if and only if the
  confidentiality problem in F-W2-14 is solved first.
- The cheapest high-value change is probably not parallelism at all. It is making the losses in
  F-W2-12 explicit: `--add-dir` sets, MCP config and plugin dirs vanish on resume, so a
  multi-project session cannot be picked up again without a written recipe. A per-project startup
  script plus a checkpoint file (C-152's confirmed half) covers this for less effort than any
  orchestrator.
- The corpus's "2–3 worktrees" number should be treated as a personal heuristic the operator may
  keep, but the justification has to change: it is not documented anywhere, and the vendor's
  nearest guidance is higher. If it is retained, retain it as a review-capacity bet, not a cited
  fact.
- Client separation and cross-project context are in direct tension, and the tension is
  structural, not a configuration detail. Any shared-memory design for a consulting practice needs
  a decision about what may cross client boundaries (patterns, conventions, tooling) versus what
  may never (facts, names, data, findings) — and auto memory writes itself, so it cannot be the
  layer where that decision is enforced.
- The two-machine split as described has no supporting mechanism and a documented cost. If a
  second machine is kept, its purpose should be re-derived (e.g. quota isolation under a second
  account, or genuinely local inference) rather than inherited.

---

## Sources

Tier in brackets. "FULL" = read in full, not from snippets.

1. **[A, FULL]** Anthropic — [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees).
   Primary vendor documentation for the exact mechanics under test. Trusted for behavior; a vendor
   describing its own product, so not trusted for comparative or fitness claims.
2. **[A, FULL]** Anthropic — [Run agents in parallel](https://code.claude.com/docs/en/agents).
   The authoritative comparison of subagents / agent view / agent teams / workflows / worktrees.
3. **[A, FULL]** Anthropic — [Manage sessions](https://code.claude.com/docs/en/sessions).
   The single most load-bearing source here: enumerates exactly what resume restores and drops.
4. **[A, FULL]** Anthropic — [How Claude remembers your project](https://code.claude.com/docs/en/memory).
   Source for auto-memory scoping (per-repo, machine-local), the 200-line/25KB cap, the CLAUDE.md
   hierarchy, symlinked rules, and the external-import approval asymmetry.
5. **[A, FULL]** Anthropic — [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams).
   Source for the 3–5 sizing guidance and the limitations that rule teams out as a cross-project
   orchestrator. Self-described as experimental — treat all specifics as short-lived.
6. **[A, FULL]** Anthropic — [Manage costs effectively](https://code.claude.com/docs/en/costs).
   Confirms the 7x agent-team-in-plan-mode figure and that `/usage` is machine-local.
7. **[B, FULL]** mabl — [How We Built a System for AI Agents to Ship Real Code Across 75+ Repos, Part 1](https://www.mabl.com/blog/how-we-built-a-system-for-ai-agents-to-ship-real-code-across-75-repos)
   (April 2026). Trusted for architecture (specific, internally consistent, reproducible);
   distrusted for the 40%→<5% figure (self-reported, undefined, bundled intervention, no third
   party). Wrong scale for the operator (25 engineers).
8. **[B, FULL]** seylox — [The agents meta-repository pattern](https://seylox.github.io/2026/03/05/blog-agents-meta-repo-pattern.html)
   (March 2026). Independent, single operator, six repos, concrete file structures, honest
   caveats, **no metrics**. Trusted as a design pattern, not as a result.
9. **[B, FULL]** João Camarate — [Keeping context and decisions consistent across parallel AI agents](https://dev.to/jcamarate/keeping-context-and-decisions-consistent-across-parallel-ai-agents-32nj).
   Independent practitioner (defract.dev), not a worktree vendor. Best available taxonomy of
   cross-lane drift. Explicitly reports no measurements.
10. **[B, FULL]** rustman.org — [Parallel coding-agent orchestrators — Conductor and the 2026 ecosystem](https://rustman.org/wiki/conductor-parallel-agents/).
    Independent survey with a license/platform table and the sharpest statement of where worktree
    isolation fails. Distrusted for quantitative claims — it contains none, and says so.
11. **[A, FULL]** [conductor.build](https://conductor.build/) and
    [conductor.build/pricing](https://conductor.build/pricing), fetched 2026-08-01. Vendor's own
    site for its own product — trusted for platform and price, nothing else. Highly volatile.
12. **[B, FULL]** Laurent Kempé — [From 3 Worktrees to N](https://laurentkempe.com/2026/03/31/from-3-worktrees-to-n-ai-powered-parallel-development-on-windows/).
    Read in full specifically to test whether it contains parallelism data. **It does not** —
    reported here as a negative result. Its real content is terminal-multiplexer tooling.
13. **[C, FULL]** Kevin Davison — [How I Turned My Git Repo Into a Self-Organizing Knowledge Base](https://www.quevin.ai/blog/2026-03-27-obsidian-agent-knowledge-base).
    Single operator, six months, no correctness metrics. The only concrete code-free-repo evidence
    found. Trusted for the type-first-taxonomy argument; not for outcomes.
14. **[C, FULL]** karun.me — [Structuring Claude Code for Multi-Repo Workspaces](https://karun.me/blog/2026/03/26/structuring-claude-code-for-multi-repo-workspaces/).
    A layout proposal. Read in full and downgraded to C: no motivating failure, no token-cost
    analysis, no session-resume analysis, no data.
15. **[B, sampled]** GitHub — [anthropics/claude-code issue #38309](https://github.com/anthropics/claude-code/issues/38309),
    `/add-folder` multi-workspace-root request, **closed as not planned**. Trusted for status;
    could not retrieve reaction counts or maintainer rationale.
16. **[C, sampled]** riftmap.dev — [AI coding agents need cross-repo context](https://riftmap.dev/blog/ai-coding-agents-need-cross-repo-context/).
    Read in full **as an object of study**, not as evidence. Vendor marketing by Riftmap's founder
    for Riftmap's cross-repo graph API; recycles mabl's, Meta's and a solo operator's numbers.
    Cited here only to document the laundering path (F-W2-05).
17. **[C, sampled]** mindstudio.ai worktree/parallel-session articles (several). Unattributed SEO
    content; source of the "2–4 parallel sessions" figure. Distrusted; recorded only to show where
    circulating numbers come from.
18. **[C, sampled]** dev.to "How I Manage 15+ Repos with Claude Code" (neil_agentic). Promotes the
    author's own tool (`ttal`); treat as vendor. One transferable observation retained
    (read/explore wide, write narrow).
19. **[C, sampled]** augmentcode.com and phparch.com worktree guides; botmonster.com orchestration
    patterns. Secondary aggregations; used only for convergence checking on F-W2-04, never as sole
    support.
20. **[C, sampled]** packmind.com context-engineering guide — source of the "CI job verifies
    documented paths and commands still exist" drift-detection idea. Downgraded to C: no primary
    implementation shown.
21. **[unread]** arXiv 2606.09090 — "Context Rot in AI-Assisted Software Development: Repurposing
    Documentation Consistency for AI Configuration Artifacts." Surfaced in search; **not read**
    (budget). Highest-value unopened lead.
22. **[unread]** arXiv 2606.24429 — "Detecting AI Coding Agents in Open Source: A Validated
    Multi-Method Census of 180 Million Repositories." Surfaced in search; **not read** (budget).
