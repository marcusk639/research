# Corpus Reconciliation Ledger

_Phase A output | Generated: 2026-07-31 | Files read: 7 | Claims extracted: 211_

**Note on file count:** the phase prompt's header describes "six corpus documents," but the
`<corpus>` table inside it lists seven files (`workflow-plan.md` and `workflow-plan-v2.md` are
two separate files under one table row). All seven were read in full; see §5 for line/word
counts. `solo-consultant-workflow-optimized.md`, the entire `prompts/` subdirectory, and
`corpus-ledger.md`/`REPORT.md`/`findings/` (none of which existed prior to this file) were
excluded per instructions.

---

## 1. Claims Register

### Source: solo-consultant-workflow.md (asserted 2026-07-17; file itself opens with the

disclaimer "Content is user-generated and unverified.")

| ID    | Claim (as stated)                                                                                                                                                                                                                                           | Source file                 | Asserted   | Type           | Volatility | Verify in | Status |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------- | -------------- | ---------- | --------- | ------ |
| C-001 | Highest-value setup for a Max-subscribing solo consultant is a disciplined single-agent loop (Explore→Plan→Code→Commit, test-based verification gates and hooks, run across 2–3 git worktrees), NOT a large multi-agent fan-out                             | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W1        | OPEN   |
| C-002 | "Anthropic's own 2026 Agentic Coding Trends Report states that multi-agent 'doesn't make sense for 95% of agent-assisted development tasks.'"                                                                                                               | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | HIGH       | W1        | OPEN   |
| C-003 | "Your review capacity, not model throughput or subscription limits, is the binding constraint"                                                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W9        | OPEN   |
| C-004 | The Max 20x plan ($200/mo) is "a clear win over API" for the operator's usage profile                                                                                                                                                                       | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | HIGH       | W5        | OPEN   |
| C-005 | Kyle Redelinghuys (ksred.com) tracked ~10 billion tokens of daily Claude Code use over 8 months (June 2025–Feb 2026)                                                                                                                                        | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   |
| C-006 | That usage "would have cost 'over $15,000' at API rates"                                                                                                                                                                                                    | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   |
| C-007 | It "ran him 'around $800 total… a 93% saving'"                                                                                                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   | See X-05 — conflicts with v1.md's dollar figures for an apparently identical scenario. |
| C-008 | Usage was "~95% Opus and over 90% of tokens being cache reads"                                                                                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   |
| C-009 | The weekly cap (and a stricter separate Opus cap) is what throttles heavy parallel work                                                                                                                                                                     | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-010 | Recommendation: "route ~70% of tasks to Sonnet, ~30% to Opus"                                                                                                                                                                                               | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W5        | OPEN   | Conflicts with the 80/15/5 rule elsewhere in the corpus — see X-02.                    |
| C-011 | The durable pattern beneath every credible methodology is: research→plan→execute→verify→review, with tight context management and a machine-checkable success signal                                                                                        | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W1        | OPEN   |
| C-012 | Anthropic's best-practices doc: "most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills"                                                                                              | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W1        | OPEN   |
| C-013 | Practitioners (Willison, Ronacher, Karunaratne, the Ralph technique) converge on aggressive context hygiene: /clear between tasks, subagents for investigation, fresh sessions over long polluted ones                                                      | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-014 | Indragie Karunaratne (Director of Engineering, Sentry) shipped the macOS app Context, estimating he "wrote less than 1,000 lines by hand" of its 20,000 lines                                                                                               | solo-consultant-workflow.md | 2026-07-17 | QUANT          | MED        | W1        | OPEN   |
| C-015 | Karunaratne (July 2025): "context engineering… is the primary challenge in using coding agents effectively"                                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W1        | OPEN   |
| C-016 | Karunaratne: "It's like I found an extra 5 hours every day, and all it cost me was $200 a month."                                                                                                                                                           | solo-consultant-workflow.md | 2026-07-17 | QUANT          | MED        | W1        | OPEN   |
| C-017 | Anthropic's recommended four-phase loop: Explore (plan mode, read-only) → Plan → Implement → Commit                                                                                                                                                         | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | LOW        | W1        | OPEN   |
| C-018 | Anthropic's newer guidance adds an interview step: have Claude interview you with AskUserQuestion, write a self-contained SPEC.md, execute it in a fresh session                                                                                            | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-019 | Anthropic's most repeated tip: "Give Claude a way to verify its work"                                                                                                                                                                                       | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-020 | Kent Beck calls TDD a "superpower" with AI agents because agents introduce regressions; warns agents will even try to delete tests to make them pass                                                                                                        | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W3        | OPEN   |
| C-021 | Hooks (deterministic gates) beat CLAUDE.md instructions (advisory)                                                                                                                                                                                          | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W3        | OPEN   |
| C-022 | Armin Ronacher recommends telling the agent to do "the dumbest possible thing that will work": long descriptive function names over clever abstractions, plain SQL over ORM gymnastics                                                                      | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   | See X-03.                                                                              |
| C-023 | Anthropic's docs warn a reviewer agent "prompted to find gaps will usually report some, even when the work is sound… chasing every finding leads to over-engineering"                                                                                       | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W3        | OPEN   |
| C-024 | Anthropic's multi-agent research system (Opus 4 lead + Sonnet 4 subagents) "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval"                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W1        | OPEN   | Document's own caveat: this is a research eval, not a coding benchmark.                |
| C-025 | That 90.2% figure was measured on breadth-first, decomposable research tasks (e.g. "identify all board members of S&P 500 IT companies"), not coding                                                                                                        | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W1        | OPEN   |
| C-026 | Anthropic reports multi-agent systems "use about 15x more tokens than chat interactions"                                                                                                                                                                    | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W1        | OPEN   |
| C-027 | Anthropic states multi-agent is explicitly "less effective for tightly interdependent tasks such as coding"                                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W1        | OPEN   | See X-01.                                                                              |
| C-028 | Addy Osmani's "70% problem": AI does ~70% of a working app fast, the last 30% is the hard part                                                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | QUANT          | MED        | W1        | OPEN   |
| C-029 | Addy Osmani: "code review is becoming the new bottleneck"                                                                                                                                                                                                   | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W9        | OPEN   |
| C-030 | Max 20x permits parallel worktree sessions and Agent Teams, but all sessions share one pooled quota                                                                                                                                                         | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-031 | Per Claude Code's official cost docs, Agent Teams "use approximately 7x more tokens than standard sessions when teammates run in plan mode, because each teammate maintains its own context window and runs as a separate Claude instance"                  | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W1        | OPEN   |
| C-032 | The separate weekly Opus cap binds first for heavy parallel Opus work                                                                                                                                                                                       | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-033 | Claude Code is the best terminal-native harness but not the only tool worth paying for; Codex, Cursor, and Conductor each beat it at a specific job                                                                                                         | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W1        | OPEN   |
| C-034 | CLAUDE.md rule: for each line ask "Would removing this cause Claude to make mistakes?" — if not, cut it                                                                                                                                                     | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W4        | OPEN   |
| C-035 | Bloated CLAUDE.md files cause Claude to ignore instructions                                                                                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W4        | OPEN   |
| C-036 | CLAUDE.md hierarchy: `~/.claude/CLAUDE.md` (global), `./CLAUDE.md` (project, checked into git), `./CLAUDE.local.md` (gitignored personal notes); files can import others via `@path/to/file`                                                                | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W4        | OPEN   |
| C-037 | Canonical hook example: a PostToolUse hook on Write/Edit/MultiEdit runs `npx prettier --write` on the touched file                                                                                                                                          | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | LOW        | W1        | OPEN   |
| C-038 | Exit code 2 blocks a tool (PreToolUse) or forces Claude to keep working (Stop); Claude overrides after 8 consecutive blocks                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W3        | OPEN   |
| C-039 | Hooks run synchronously — keep them fast; use `--findRelatedTests` (not the full suite) on PostToolUse; save full test/build runs for the Stop hook                                                                                                         | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-040 | Hooks also fire for subagent tool calls, so gates can't be bypassed by delegation                                                                                                                                                                           | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-041 | Subagents run in isolated context windows with their own tool allow-lists; best uses are investigation/research and a fresh-eyes reviewer; route them to cheaper models (Haiku/Sonnet) to control cost                                                      | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-042 | Anthropic ships built-in Explore, Plan, and general-purpose subagents; frontmatter defines name/description/tools/model; `isolation: worktree` gives a subagent its own worktree                                                                            | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-043 | Custom slash commands/skills live in `.claude/skills/` (SKILL.md), loaded on demand; `disable-model-invocation: true` restricts a skill to manual triggering                                                                                                | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-044 | Workflow A, "Spec-Locked Single Loop," is recommended as the operator's default, ~80% of work                                                                                                                                                               | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-045 | `claude --worktree feature-x` (or `-w`) creates an isolated branch under `.claude/worktrees/`; a `.worktreeinclude` file (gitignore syntax) auto-copies `.env`/secrets into new worktrees                                                                   | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-046 | Cap worktree parallelism at 2–3 — "the documented practical ceiling for a solo reviewer"                                                                                                                                                                    | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W2        | OPEN   |
| C-047 | Worktrees with no changes auto-clean; those with changes persist for review                                                                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-048 | A fresh-context reviewer subagent improves code review "since Claude won't be biased toward code it just wrote"                                                                                                                                             | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W3        | OPEN   |
| C-049 | Instruct the reviewer to "flag only gaps that affect correctness or the stated requirements" to avoid over-engineering                                                                                                                                      | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-050 | The Ralph technique (Geoffrey Huntley, July 2025) is a bash loop restarting with fresh context each iteration, using the filesystem, a TODO file, and git as external memory                                                                                | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-051 | Fresh context every iteration works because it avoids degradation past the ~100–150k-token point where quality drops                                                                                                                                        | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | HIGH       | W1        | OPEN   |
| C-052 | Armin Ronacher notes he hasn't made loops work "for code I deeply care about"                                                                                                                                                                               | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W1        | OPEN   |
| C-053 | Spec-kit (GitHub) has 93k+ stars and is portable across 30+ agents                                                                                                                                                                                          | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W1        | OPEN   |
| C-054 | Kiro (AWS) uses formal EARS-notation acceptance criteria; static specs drift; it is a "sledgehammer to crack a nut" on small tasks                                                                                                                          | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W1        | OPEN   | See X-03.                                                                              |
| C-055 | PRP/Context Engineering (Wirasm/Cole Medin) enables one-pass production code via rich context; the document recommends "adopt the PRPs/ + ai_docs/ idea"                                                                                                    | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   | See X-03.                                                                              |
| C-056 | Head-to-head methodology verdicts: Anthropic Explore/Plan/Code/Commit = core default; spec-kit = use selectively; Kiro = skip unless AWS-native; PRP = adopt the idea; Ralph = bounded use only; multi-agent/Agent Teams = research/review, not core coding | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-057 | Codex (OpenAI) offers async cloud fan-out — "queue five tasks, walk away, come back to five PRs" — bundled with ChatGPT plans, more token-efficient for batch work                                                                                          | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-058 | Cursor is the best visual IDE loop, model-agnostic; credit-based billing has reported large overages for heavy users                                                                                                                                        | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-059 | Amp (Sourcegraph) has the strongest cross-repo code intelligence (built on Sourcegraph's code graph); free, ad-supported                                                                                                                                    | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-060 | Conductor (Melty Labs, macOS) is the most practitioner-praised worktree orchestrator: parallel Claude/Codex agents in worktrees, one-click PRs, Linear/GitHub integration; closed-source, Mac-only                                                          | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W2        | OPEN   |
| C-061 | Claude Squad / Crystal(→Nimbalyst) / Vibe Kanban are terminal or open-source worktree managers; Claude Squad is the lean terminal option for solo devs                                                                                                      | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-062 | Aider is git-native and model-agnostic, and maintains well-regarded LLM coding benchmarks                                                                                                                                                                   | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W1        | OPEN   |
| C-063 | Model pricing: Sonnet $3/$15 per MTok, Opus ~$5/$25, Haiku $1/$5                                                                                                                                                                                            | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   |
| C-064 | On Max, Opus burns quota far faster than Sonnet                                                                                                                                                                                                             | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W5        | OPEN   |
| C-065 | In heavy Claude Code sessions the overwhelming majority of tokens are cache reads, included in the flat Max rate — "precisely why the subscription crushes API for your profile"                                                                            | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W5        | OPEN   |
| C-066 | Every parallel session, subagent, and Agent Team draws from one shared 5-hour + weekly bucket                                                                                                                                                               | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-067 | Anthropic doubled the 5-hour limits in May 2026 but left weekly caps unchanged                                                                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W1        | OPEN   |
| C-068 | Programmatic/CI usage (Agent SDK, `claude -p`, GitHub Actions) moved to separate credits/API rates in June 2026                                                                                                                                             | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   |
| C-069 | Ranked #11 (lowest): large multi-agent fan-out — ~7–15x token cost; "poor fit for interdependent coding"; "overwhelms a solo reviewer"                                                                                                                      | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | HIGH       | W1        | OPEN   | See X-01.                                                                              |
| C-070 | Ranked #10: Kiro/heavy spec IDEs — static specs drift, ceremony is a "sledgehammer to crack a nut"                                                                                                                                                          | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-071 | Ranked #9: unbounded Ralph loop — slop/cost risk makes it unsuitable for client code without heavy gating                                                                                                                                                   | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W1        | OPEN   |
| C-072 | Ranked #8: full spec-kit adoption — portable (`specify init --integration claude`), valuable for large greenfield, heavy for routine work                                                                                                                   | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-073 | Ranked #7: Cursor/Codex as a secondary tool — genuinely useful complement, not a foundation                                                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-074 | Ranked #6: worktree orchestrator (Conductor/Claude Squad) — makes 2–3 parallel sessions manageable                                                                                                                                                          | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W2        | OPEN   |
| C-075 | Ranked #5: subagent Writer/Reviewer split — cheap, measurable accuracy gain, high value-to-effort                                                                                                                                                           | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-076 | Ranked #4: 2–3 worktree parallelism — "the right amount of parallelism for a solo reviewer"                                                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W2        | OPEN   |
| C-077 | Ranked #3: hooks + CLAUDE.md foundation — one-time investment with compounding returns                                                                                                                                                                      | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-078 | Ranked #2: verification-driven development (TDD + machine-checkable gates) — "the single biggest lever on accuracy," lets you delegate unattended                                                                                                           | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-079 | Ranked #1 (highest): Spec-Locked Single Loop with aggressive context management — "what the most credible production practitioners… actually do"                                                                                                            | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |
| C-080 | Staged rollout: Stage 1 (lean CLAUDE.md, 3 hooks, Sonnet default/Opus for planning); Stage 2 (reviewer subagent, /fix-issue skill, 2 worktrees, PRPs/+ai_docs/); Stage 3 (worktree orchestrator, Codex, trial spec-kit)                                     | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W1        | OPEN   |
| C-081 | Cost discipline: stay on Max 20x; ~70/30 Sonnet/Opus split; watch the weekly Opus cap; switch to Sonnet if Opus is throttled mid-week                                                                                                                       | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | MED        | W5        | OPEN   |
| C-082 | Anti-over-engineering guardrails belong in CLAUDE.md; separate tidying commits from feature commits (Kent Beck's "Tidy First")                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-083 | Reported class-action dispute (filed June 2026) over advertised Max value — "an unresolved claim, not a settled fact"                                                                                                                                       | solo-consultant-workflow.md | 2026-07-17 | QUANT          | HIGH       | W5        | OPEN   |
| C-084 | Multiple practitioners independently report becoming the reviewer bottleneck at 3+ concurrent sessions                                                                                                                                                      | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | MED        | W9        | OPEN   | See X-04.                                                                              |
| C-085 | Practitioner quote: "I'm ultimately responsible for the code in a PR with my name on it, regardless of how it was produced"                                                                                                                                 | solo-consultant-workflow.md | 2026-07-17 | CAUSAL         | LOW        | W9        | OPEN   |
| C-086 | Conductor and similar orchestrators are closed-source binaries requiring broad GitHub access — a security consideration for client codebases                                                                                                                | solo-consultant-workflow.md | 2026-07-17 | CAPABILITY     | MED        | W8        | OPEN   |
| C-087 | `--dangerously-skip-permissions` ("claude-yolo") should only be run inside a container/sandbox                                                                                                                                                              | solo-consultant-workflow.md | 2026-07-17 | RECOMMENDATION | LOW        | W1        | OPEN   |

### Source: v1.md (asserted "2026 Q1" per workflow-plan-v2.md's own characterization; the file

carries no internal date and was last saved 2026-07-14)

| ID    | Claim (as stated)                                                                                                                                                                                                                                                    | Source file | Asserted | Type           | Volatility | Verify in | Status |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | -------------- | ---------- | --------- | ------ |
| C-088 | SWE-bench Verified: Claude Code Max 20x 88.6% (Opus 4.8 native)                                                                                                                                                                                                      | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-089 | SWE-bench Verified: GitHub Copilot Pro/GPT-5.2 Codex 80.0%                                                                                                                                                                                                           | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-090 | SWE-bench Verified: OpenRouter Hybrid Stack 80.6% (DeepSeek V4 Pro) / 79.0% (V4 Flash)                                                                                                                                                                               | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-091 | SWE-bench Pro: Claude Code Max 69.2% (Opus 4.8 scaffold)                                                                                                                                                                                                             | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-092 | SWE-bench Pro: Copilot 41.0% (standardized harness)                                                                                                                                                                                                                  | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-093 | SWE-bench Pro: OpenRouter Hybrid Stack 59.0% (attributed to "MiniMax M3 / GLM-5.1 orchestration")                                                                                                                                                                    | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   | Row header names DeepSeek V4 as the hybrid stack's model but this figure is attributed to different models entirely — internal inconsistency within v1.md; see §5. |
| C-094 | Monthly cost: Claude Code Max flat $200; Copilot Pro/Codex $10–39; OpenRouter pay-as-you-go                                                                                                                                                                          | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-095 | Context window: Claude Code Max 1,000,000 tokens; Copilot ~200,000 tokens (workspace limit); OpenRouter Hybrid 1,050,000 tokens                                                                                                                                      | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-096 | "On SWE-bench Pro, Claude Code leads by 28 percentage points over Copilot (69.2% vs 41.0%)"                                                                                                                                                                          | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   | See X-06.                                                                                                                                                          |
| C-097 | Full-time developers using Claude Code continuously across multiple repos "easily consume 10+ billion tokens over 8 months"                                                                                                                                          | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-098 | Raw pay-as-you-go API (Sonnet $3/M input, $15/M output) cost for that usage over 8 months: ~$15,000                                                                                                                                                                  | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-099 | Claude Code Max 20x subscription cost for the same 8 months: $1,600                                                                                                                                                                                                  | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   | See X-05 — conflicts with solo-consultant-workflow.md's $800 figure for an apparently identical scenario.                                                          |
| C-100 | Resulting savings: "~$13,400 (~89% reduction)"                                                                                                                                                                                                                       | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-101 | Single-vendor silo risk: Anthropic brownouts/throttling/regulatory pauses would stall the entire software delivery pipeline                                                                                                                                          | v1.md       | 2026-Q1  | CAUSAL         | LOW        | W5        | OPEN   |
| C-102 | Copilot/Codex "lacks accurate multi-file execution velocity"; its cloud-agent architecture "restricts multi-step bash execution and self-correcting terminal loops"                                                                                                  | v1.md       | 2026-Q1  | CAPABILITY     | MED        | W1        | OPEN   |
| C-103 | DeepSeek V4 Pro pricing: $0.435/M input, $0.870/M output, 1,050,000 context                                                                                                                                                                                          | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-104 | DeepSeek V4 Flash pricing: $0.090/M input, $0.180/M output, 1,050,000 context                                                                                                                                                                                        | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-105 | Break-even claim: fewer than 20 long-horizon multi-file autonomous debugging loops/day → under $15–30/month/seat while achieving 80.6% SWE-bench Verified                                                                                                            | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-106 | "Two-Tier Strategic Stack": Tier 1 Cursor Pro/Copilot Pro (~$20/mo, ~80% of routine coding tasks, zero-latency); Tier 2 Claude Code Max/custom CLI ($200/mo or variable, large features/migrations/refactors)                                                        | v1.md       | 2026-Q1  | RECOMMENDATION | MED        | W1        | OPEN   |
| C-107 | A root-level `AI.md` file (architectural maps, module boundaries, typing rules) cuts token consumption "by up to 40%" by eliminating exploratory codebase searches                                                                                                   | v1.md       | 2026-Q1  | QUANT          | HIGH       | W4        | OPEN   |
| C-108 | JSON blueprint target metrics: SWE-bench Verified ≥85.0%, SWE-bench Pro ≥60.0%, max monthly seat cost $200                                                                                                                                                           | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-109 | Blueprint Layer 1: Cursor IDE Fork, Pro subscription, $20/mo, primary engine claude-sonnet-4.6, fallback gpt-5.4-inline, 20,000-token context allocation                                                                                                             | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-110 | Blueprint Layer 2: Claude Code CLI, Max 20x, $200/mo, primary engine claude-opus-4.8, secondary claude-sonnet-4.6, capabilities include native bash execution, filesystem write, speculative test running, 1M prompt caching                                         | v1.md       | 2026-Q1  | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-111 | Blueprint Layer 3: OpenRouter API Gateway, pay-as-you-go, base token allowance $30; routing table names deepseek-v4-pro:xhigh ($0.435/$0.87 per M), deepseek-v4-flash:xhigh ($0.09/$0.18 per M), minimax-m3 ($0 cost)                                                | v1.md       | 2026-Q1  | QUANT          | HIGH       | W5        | OPEN   |
| C-112 | Execution-loop logic: route to Layer 2 if codebase >500,000 tokens and multi-file mutation is required; fall back to Layer 3 on Layer 2 rate limits or regional suspension                                                                                           | v1.md       | 2026-Q1  | CAPABILITY     | MED        | W1        | OPEN   |
| C-113 | Decision guide: full-time dev on interconnected multi-file systems → Claude Code Max 20x; avoid vendor lock-in → OpenRouter+OpenHands/Aider; small team/completion → Copilot Pro; unpredictable spikes → two-tier stack; max benchmark performance → Claude Code Max | v1.md       | 2026-Q1  | RECOMMENDATION | MED        | W1        | OPEN   |
| C-114 | Open-source terminal framework (OpenHands/Aider) + OpenRouter (V4 Pro design, V4 Flash test iteration) achieves "roughly 90% of Claude's autonomous capability" at variable cost tied to production velocity                                                         | v1.md       | 2026-Q1  | QUANT          | HIGH       | W1        | OPEN   |
| C-115 | Key takeaway: "$200/month vs ~$15,000 in raw API costs over 8 months is not a rounding error"                                                                                                                                                                        | v1.md       | 2026-Q1  | CAUSAL         | MED        | W5        | OPEN   | See X-02.                                                                                                                                                          |
| C-116 | Key takeaway: two-tier stacking is "the practical optimum for most teams," covering ~95% of development workflows with no gaps                                                                                                                                       | v1.md       | 2026-Q1  | RECOMMENDATION | MED        | W1        | OPEN   |
| C-117 | Key takeaway: OpenRouter is "the resilience hedge" — a configured Layer 3 fallback prevents single-vendor brownouts from halting delivery                                                                                                                            | v1.md       | 2026-Q1  | RECOMMENDATION | LOW        | W5        | OPEN   |

### Source: v2.md (asserted "2026 Q2" per workflow-plan-v2.md's own characterization; the file

carries no internal date and was last saved 2026-07-14)

| ID    | Claim (as stated)                                                                                                                                                                                                                                                                                                                                         | Source file | Asserted | Type           | Volatility | Verify in | Status |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | -------------- | ---------- | --------- | ------ |
| C-118 | Terminal-Bench 2.1: Claude Code Max 78.9% (Opus 4.8); Codex CLI+GPT-5.5 83.4%; Modular Stack 74–81% (routing-dependent)                                                                                                                                                                                                                                   | v2.md       | 2026-Q2  | QUANT          | HIGH       | W1        | OPEN   | See X-06.                                                                                                                  |
| C-119 | Context window: Claude Code Max "up to 1M tokens"; Codex CLI+GPT-5.5 "512k tokens"; Modular Stack "elastic… up to 2M"                                                                                                                                                                                                                                     | v2.md       | 2026-Q2  | QUANT          | HIGH       | W1        | OPEN   | The 512k Codex figure conflicts with v1.md's ~200,000-token figure for a nominally similar Copilot/Codex product — see §5. |
| C-120 | Monthly cost: Claude Code Max flat $200; Codex CLI custom enterprise tier; Modular Stack ~$40–70/mo pay-as-you-go                                                                                                                                                                                                                                         | v2.md       | 2026-Q2  | QUANT          | HIGH       | W5        | OPEN   |
| C-121 | Vendor lock-in: Claude Code Max High (Anthropic ecosystem); Codex High (OpenAI ecosystem); Modular Stack Zero (swap models dynamically)                                                                                                                                                                                                                   | v2.md       | 2026-Q2  | CAPABILITY     | MED        | W5        | OPEN   |
| C-122 | "Raw API usage for autonomous agents can hit $13–50 per developer day during intense sessions due to large context loops"                                                                                                                                                                                                                                 | v2.md       | 2026-Q2  | QUANT          | HIGH       | W5        | OPEN   |
| C-123 | The original standalone Codex API was deprecated and folded into OpenAI's frontier reasoning models; "today's 'Codex CLI' environments run on GPT-5.5"                                                                                                                                                                                                    | v2.md       | 2026-Q2  | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-124 | Codex CLI/GPT-5.5 has the highest Terminal-Bench 2.1 score (83.4%) but is "less autonomously agentic than Claude Code during prolonged local system debugging or multi-step environment configuration"                                                                                                                                                    | v2.md       | 2026-Q2  | CAUSAL         | MED        | W1        | OPEN   |
| C-125 | "Judge-Builder" loop: a Builder model generates code, a secondary adversarial Judge model critiques it and returns precise feedback, and the Builder refactors before a human ever looks at the file                                                                                                                                                      | v2.md       | 2026-Q2  | RECOMMENDATION | MED        | W3        | OPEN   | See X-01.                                                                                                                  |
| C-126 | OpenRouter provides "zero-completion insurance": if a provider hits rate limits or 5xx errors, OpenRouter dynamically shifts traffic to an alternative provider mid-session                                                                                                                                                                               | v2.md       | 2026-Q2  | CAPABILITY     | MED        | W5        | OPEN   |
| C-127 | The "80/15/5 Token Rule": Execution tier 80% (DeepSeek V4 Flash, Gemini 2.5 Flash, OpenRouter Pareto — completions/patches/test templates/boilerplate); Planning tier 15% (Claude 3.5 Sonnet, OpenRouter Auto — architecture/migrations/security audits); Deep Reasoning tier 5% (Claude Opus, GPT-5.5 xhigh — legacy bug logic/structural breaks/crypto) | v2.md       | 2026-Q2  | RECOMMENDATION | MED        | W5        | OPEN   | See X-02.                                                                                                                  |
| C-128 | "The average developer running this stack spends $40–70/month instead of $200+, with comparable or better throughput for most workflows"                                                                                                                                                                                                                  | v2.md       | 2026-Q2  | QUANT          | HIGH       | W5        | OPEN   |
| C-129 | Recommended core stack: Hermes Agent CLI (orchestrator), OpenRouter (gateway with multi-provider failover), Manifest (local router/fallback/caching layer), Cursor or Aider (visual interface)                                                                                                                                                            | v2.md       | 2026-Q2  | RECOMMENDATION | MED        | W1        | OPEN   | Directly reversed by workflow-plan-v2.md — see Recommendation Inventory item 9.                                            |
| C-130 | Hermes Agent is installed via a curl script from the NousResearch/hermes-agent GitHub repo                                                                                                                                                                                                                                                                | v2.md       | 2026-Q2  | CAPABILITY     | HIGH       | W1        | OPEN   |
| C-131 | Recommended CLAUDE.md/.cursorrules tier-enforcement rule: "NEVER use the REASONING_MODEL for tasks completable by the EXECUTION_MODEL"                                                                                                                                                                                                                    | v2.md       | 2026-Q2  | RECOMMENDATION | LOW        | W4        | OPEN   |
| C-132 | Manifest (github.com/mnfst/manifest) binds standard consumer accounts (Claude Pro/ChatGPT Plus) into API pipelines as "zero-cost fallbacks" when primary credits expire                                                                                                                                                                                   | v2.md       | 2026-Q2  | CAPABILITY     | HIGH       | W5        | OPEN   |
| C-133 | Key takeaway: "Multi-tier routing is the unlock" — the 80/15/5 rule "consistently delivers 60–70% cost reduction vs. single-model setups with minimal quality loss"                                                                                                                                                                                       | v2.md       | 2026-Q2  | QUANT          | HIGH       | W5        | OPEN   |
| C-134 | Key takeaway: "Flat subscriptions trade flexibility for predictability" — Claude Code Max is excellent if token anxiety hurts productivity                                                                                                                                                                                                                | v2.md       | 2026-Q2  | CAUSAL         | LOW        | W5        | OPEN   |
| C-135 | Key takeaway: the Judge-Builder loop "changes the review dynamic" — quality is enforced before human review rather than during it, "compounding velocity gains"                                                                                                                                                                                           | v2.md       | 2026-Q2  | CAUSAL         | MED        | W3        | OPEN   |
| C-136 | Key takeaway: vendor lock-in is a real risk; OpenRouter eliminates it, Anthropic and OpenAI ecosystems do not                                                                                                                                                                                                                                             | v2.md       | 2026-Q2  | CAUSAL         | LOW        | W5        | OPEN   |
| C-137 | Key takeaway: context standards (CLAUDE.md/.cursorrules) are infrastructure — without them, tier enforcement "degrades into random model selection"                                                                                                                                                                                                       | v2.md       | 2026-Q2  | CAUSAL         | LOW        | W4        | OPEN   |

### Source: workflow-plan.md (dated 2026-06-27 in the document; based on "session patterns Jun

2026")

| ID    | Claim (as stated)                                                                                                                                                                                                                                                                                               | Source file      | Asserted   | Type           | Volatility | Verify in | Status |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | -------------- | ---------- | --------- | ------ |
| C-138 | "Your current workflow (Claude Max all the time) is not wrong — for heavy multi-file agentic work, it's the single most cost-effective option at scale"                                                                                                                                                         | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W5        | OPEN   |
| C-139 | Restates v1.md's figure: "the subsidy arbitrage is real: ~$13,400 saved over 8 months vs. raw pay-as-you-go API"                                                                                                                                                                                                | workflow-plan.md | 2026-06-27 | QUANT          | HIGH       | W5        | OPEN   |
| C-140 | Recommendation: create a `<subject>/CONTEXT.md` per active research subject (established facts, open questions, key constraints, sources already consumed)                                                                                                                                                      | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W4        | OPEN   | See Recommendation Inventory item 11 — status ambiguous in later documents.                    |
| C-141 | Recommendation: maintain a `WORKFLOW.md` at the repo root (active tracks, sequencing rule, research conventions, models in use)                                                                                                                                                                                 | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W2        | OPEN   | Same ambiguous-status note as C-140.                                                           |
| C-142 | Verification target: creating CONTEXT.md files should produce a 30–40% token-count reduction on a comparable research run vs. baseline                                                                                                                                                                          | workflow-plan.md | 2026-06-27 | QUANT          | MED        | W4        | OPEN   |
| C-143 | Three-tier routing for the operator's actual workload: Tier A Judgment (Claude Max Opus/Sonnet — settlement/VA/CPA/architecture); Tier B Generation (Claude Max Sonnet/Haiku — drafts/collateral/formatting); Tier C Bulk (OpenRouter DeepSeek V4 Flash $0.09/M or Haiku — bulk formatting/queries/boilerplate) | workflow-plan.md | 2026-06-27 | RECOMMENDATION | MED        | W5        | OPEN   | A third distinct tier-ratio scheme, alongside the 70/30 split and the 80/15/5 rule — see X-02. |
| C-144 | Routing decision tree: high-stakes → Tier A; novel research synthesis → Tier A; generation from known spec → Tier B; bulk/repetitive (100+ items) → Tier C; else → Tier B                                                                                                                                       | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W5        | OPEN   |
| C-145 | Pre-run "question statement" protocol: "a 200-token question statement can save 2M tokens of exploratory wandering"                                                                                                                                                                                             | workflow-plan.md | 2026-06-27 | QUANT          | HIGH       | W6        | OPEN   |
| C-146 | Checkpoint discipline: before a 100+ agent run, ask "What does success look like, and how will I know the run failed early?" — if you can't answer both, the run is underspecified                                                                                                                              | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W6        | OPEN   |
| C-147 | Three-stage research model: Draft (single session, no subagents, <50K tokens) → Deep (deep-research skill, 2–6M tokens) → Verify (source-capture + spot-check, <200K tokens)                                                                                                                                    | workflow-plan.md | 2026-06-27 | RECOMMENDATION | MED        | W6        | OPEN   | Status ambiguous — not carried into workflow-plan-v2.md.                                       |
| C-148 | OpenRouter Layer 3 setup: fund with $30–50/mo; alias `bulk-fast`→deepseek-v4-flash, `arch-plan`→deepseek-v4-pro; Cursor IDE uses claude-sonnet-4.6 for inline completion                                                                                                                                        | workflow-plan.md | 2026-06-27 | RECOMMENDATION | MED        | W5        | OPEN   |
| C-149 | Estimated Claude Max hours freed by Tier C offload: 20–30% reduction in Max token consumption                                                                                                                                                                                                                   | workflow-plan.md | 2026-06-27 | QUANT          | HIGH       | W5        | OPEN   |
| C-150 | §7216 compliance rule: client tax data (PII, financial records) must NOT be sent to OpenRouter; client-data workflows stay on local Claude Code instances only                                                                                                                                                  | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W8        | OPEN   |
| C-151 | Dual-Mac mapping: M4 Pro (48GB) = Tier A+B interactive/judgment; M5 Air (24GB) = Tier B+C autonomous batch/overnight                                                                                                                                                                                            | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W2        | OPEN   |
| C-152 | Operational rules: never run unattended Tier A work on M5 Air; batch 5–10 Tier C items for an overnight run; write progress to a shared checkpoint file so a failed batch isn't fully re-run                                                                                                                    | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W2        | OPEN   |
| C-153 | CPA automation build workflow: write feature spec → hand to Claude Code Max → review as a senior engineer → reject/refine the spec (never edit agent output directly) → merge when tests pass and spec is satisfied                                                                                             | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-154 | Weekly 15-minute review cadence: check last week's research-run quality, update CONTEXT.md, check OpenRouter spend vs. Claude Max, review WORKFLOW.md priority, flag misrouted Tier C tasks, update M5 batch queue                                                                                              | workflow-plan.md | 2026-06-27 | RECOMMENDATION | LOW        | W9        | OPEN   |
| C-155 | Total cost estimate: current $200/mo → after $215–230/mo ($200 + $15–30 OpenRouter)                                                                                                                                                                                                                             | workflow-plan.md | 2026-06-27 | QUANT          | HIGH       | W5        | OPEN   |

### Source: workflow-plan-v2.md ("Version 2.0, supersedes workflow-plan.md"; dated 2026-06-27;

based on "live audit of recovery-platform, rag-system, cpa-consulting")

| ID    | Claim (as stated)                                                                                                                                                                                                                                                                                                                                                                                                               | Source file         | Asserted   | Type           | Volatility | Verify in | Status |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------- | -------------- | ---------- | --------- | ------ |
| C-162 | Reconciliation of v1/v2 benchmark disagreement: "Different benchmarks measure different things. SWE-bench Pro (multi-file architectural repair) maps to your work better than Terminal-Bench (code generation speed). Claude Max stays."                                                                                                                                                                                        | workflow-plan-v2.md | 2026-06-27 | CAUSAL         | LOW        | W1        | OPEN   | See X-06 — this reconciliation is itself unverified.                                            |
| C-163 | Cost-floor reconciliation: "Not mutually exclusive. Max is the backbone; OpenRouter handles the 80% cheap tier. Blended target: $80–120/mo."                                                                                                                                                                                                                                                                                    | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | MED        | W5        | OPEN   |
| C-164 | Quality-mechanism reconciliation: "Both apply. Context files are already in place across all repos. Judge-Builder loop is the missing unlock."                                                                                                                                                                                                                                                                                  | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-165 | Vendor-lock-in reconciliation: "Low risk given Max subscription model; add OpenRouter as fallback/cheap tier"                                                                                                                                                                                                                                                                                                                   | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W5        | OPEN   |
| C-166 | Config-required reconciliation: "Medium path: OpenRouter API key + tier policy in CLAUDE.md. Skip Hermes/Manifest overhead."                                                                                                                                                                                                                                                                                                    | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | MED        | W5        | OPEN   | Overrides v2.md's own Hermes+Manifest stack recommendation (C-129) — direct in-corpus reversal. |
| C-169 | "Reduction opportunity: Moving 40–50% of work to cheaper models (Tier C) saves the equivalent of 2–3 Claude Max subscription months per quarter"                                                                                                                                                                                                                                                                                | workflow-plan-v2.md | 2026-06-27 | QUANT          | MED        | W5        | OPEN   |
| C-170 | 80/15/5 Tier Policy block for every CLAUDE.md: Tier A (5%, reasoning) — cross-product architecture, security-critical code, complex multi-file bugs, final review; Tier B (15%, planning) — single-module features, migrations, non-trivial PR review, research synthesis; Tier C (80%, execution) — test stubs, boilerplate, linting, doc reformatting; anti-pattern guard: "NEVER use Tier A for tasks completable by Tier C" | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | MED        | W5        | OPEN   | See X-02.                                                                                       |
| C-171 | Per-repo tier calibration for recovery-platform (Tier A: cross-product integration, Firebase security rules, Stripe webhooks, Redux architecture) and rag-system (Tier A: retrieval pipeline architecture, auth provider changes, pg-boss orchestration, cross-package API contracts)                                                                                                                                           | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W5        | OPEN   |
| C-172 | "Do NOT use Hermes Agent CLI or Manifest proxy (too much config overhead for a solo developer). Route directly to OpenRouter API for Tier C tasks."                                                                                                                                                                                                                                                                             | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | MED        | W5        | OPEN   | Contradicts v2.md's C-129/C-130/C-132.                                                          |
| C-173 | Cursor Pro ($20/mo) provides zero-latency inline autocomplete from Sonnet, replacing the friction of switching Claude Max sessions for routine edits — "pays for itself"                                                                                                                                                                                                                                                        | workflow-plan-v2.md | 2026-06-27 | CAUSAL         | MED        | W1        | OPEN   |
| C-174 | Cost math: Cursor Pro $20 + OpenRouter ~$30–40 = $50–60/month added; Claude Max reduction (estimated) 30–40% fewer heavy sessions = ~$60–80 recaptured; net new cost $0–20/month                                                                                                                                                                                                                                                | workflow-plan-v2.md | 2026-06-27 | QUANT          | HIGH       | W5        | OPEN   |
| C-175 | Judge-Builder loop for this operator: Builder writes code → cheap Judge model critiques asynchronously → Builder revises → human sees only the final output                                                                                                                                                                                                                                                                     | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | MED        | W3        | OPEN   | See X-01.                                                                                       |
| C-176 | Judge review checklist for recovery-platform: logic errors, unsafe `any` casts, Firebase security rule violations, missing error handling, Stripe webhook signature bypass risk, Redux mutation violations, missing Zod validation, missing tests; returns a structured issues/verdict object                                                                                                                                   | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-177 | The Judge pass should run on the Tier C model (DeepSeek V4 Flash) "because the judge pass is pattern-matching, not deep reasoning"; escalate to Tier B only for auth/payments/cross-product changes                                                                                                                                                                                                                             | workflow-plan-v2.md | 2026-06-27 | CAUSAL         | MED        | W3        | OPEN   |
| C-178 | Judge pass should trigger automatically after any multi-file change and before PR creation; not needed for documentation, package.json, or config edits                                                                                                                                                                                                                                                                         | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-179 | rag-system Judge calibration checklist: missing Zod validation on new routes, auth middleware gaps, missing pg-boss error handlers, un-awaited Drizzle queries, MCP tools missing input schemas, embedding-dimension mismatch risk                                                                                                                                                                                              | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-180 | "Without automated CI gates, bugs reach main and require expensive multi-file repair sessions. A 15-minute CI run catching a TypeScript error early eliminates a 2-hour debugging session with Claude."                                                                                                                                                                                                                         | workflow-plan-v2.md | 2026-06-27 | CAUSAL         | MED        | W3        | OPEN   |
| C-181 | Maestro Cloud can run on GitHub Actions; the existing flows (login-and-join-group.yaml, login-and-view-dashboard.yaml) are "ready to run — just need the Maestro Cloud API key and a device target"                                                                                                                                                                                                                             | workflow-plan-v2.md | 2026-06-27 | CAPABILITY     | MED        | W3        | OPEN   |
| C-182 | LocalEmbeddingProvider should be used for all development/testing/CI e2e runs (zero API cost per embed); degrade to Gemini only in production                                                                                                                                                                                                                                                                                   | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-183 | Production model routing for the CPA KB: Gemini `text-embedding-004` (768-dim, $0.00002/1K tokens, "essentially free") for ingestion; hybrid RRF (HNSW+BM25) retrieval; OpenRouter DeepSeek V4 Flash for first-pass answers, escalate to Sonnet for complex multi-document synthesis                                                                                                                                            | workflow-plan-v2.md | 2026-06-27 | QUANT          | HIGH       | W5        | OPEN   |
| C-184 | CPA document-type tier assignment table: strategy-doc initial draft C→B; client-facing advisory output A; collateral variations C; CLAUDE.md updates C; financial figure validation A ("must not hallucinate numbers"); interview capture→structured notes C; RAG KB question testing B                                                                                                                                         | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W5        | OPEN   |
| C-185 | Tier annotations in the `prompts/` directory create "an executable record of which model should run which document"                                                                                                                                                                                                                                                                                                             | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W4        | OPEN   |
| C-186 | Weekly ops cadence (15 min): cost check, quality check (Judge-pass patterns, Maestro failures, CI status), context maintenance, routing-discipline check                                                                                                                                                                                                                                                                        | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W9        | OPEN   |
| C-187 | Summary before/after: monthly cost $200 (Max only) → gross ~$250 (Max+Cursor+OpenRouter) minus ~$60–80 recaptured = net $170–190 first month, trending to $130–150 as Tier C routing matures                                                                                                                                                                                                                                    | workflow-plan-v2.md | 2026-06-27 | QUANT          | HIGH       | W5        | OPEN   |
| C-188 | "The bottleneck is not the $200/mo subscription. It is routing 80% of your work through Opus/Sonnet when DeepSeek V4 Flash could handle it at a fraction of the cost."                                                                                                                                                                                                                                                          | workflow-plan-v2.md | 2026-06-27 | CAUSAL         | MED        | W5        | OPEN   | See X-04 — frames the bottleneck as cost/routing, never review capacity.                        |
| C-189 | Execution-order priority: tier policy first (no cost), OpenRouter account (parallel), CI pipeline, Judge-Builder skill, LocalEmbeddingProvider env var, CPA tier annotations before Aug-1 engagement, Maestro Cloud CI, then ongoing weekly review                                                                                                                                                                              | workflow-plan-v2.md | 2026-06-27 | RECOMMENDATION | LOW        | W9        | OPEN   |

### Source: implementation-plan.md (undated; derived from workflow-plan-v2.md, 2026-06-27; file

last saved 2026-07-14)

| ID    | Claim (as stated)                                                                                                                                                                                                | Source file            | Asserted  | Type           | Volatility | Verify in | Status |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | --------- | -------------- | ---------- | --------- | ------ |
| C-206 | Anti-pattern guard: do not edit sub-product CLAUDE.md files (root policy cascades down); do not add tier policy to `.claude/CLAUDE.md` files (tooling config, not agent context)                                 | implementation-plan.md | (undated) | RECOMMENDATION | LOW        | W4        | OPEN   |
| C-207 | "The recovery-platform CI must handle a monorepo with 4 distinct TypeScript sub-projects, each with different package managers and dependency trees. Do NOT write a single-package CI — it will fail."           | implementation-plan.md | (undated) | RECOMMENDATION | MED        | W3        | OPEN   |
| C-209 | Judge-review skill anti-pattern guards: must not call back to Claude Max for every review ("defeats the cost purpose"); must not block commits automatically — return findings for review, not gate the workflow | implementation-plan.md | (undated) | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-210 | CI anti-pattern guards: use `--passWithNoTests` (some packages have zero tests); do not run `npm run build` for mobile packages in CI (require Xcode/Android SDK)                                                | implementation-plan.md | (undated) | RECOMMENDATION | LOW        | W3        | OPEN   |
| C-211 | Maestro anti-pattern guards: run only on PRs, not every push to main (saves Maestro Cloud credits); do not gate the CI phase on a perfect Maestro run — ship unit CI first                                       | implementation-plan.md | (undated) | RECOMMENDATION | LOW        | W3        | OPEN   |

---

## 2. Repo Ground Truth

Audited facts about the operator's own repositories, as stated by the source document on the
date given. **Not web-verifiable — Phase B must not attempt to verify these.** They may have
changed since the audit date.

| ID    | Repo fact (as stated)                                                                                                                                                                                                                                                                                                                 | Source file            | Audited as of                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------------------------- |
| C-156 | Operator profile: "not primarily a software developer" — a high-volume research operator (4–10M tokens per deep-research run), multi-track entrepreneur managing 9 business ventures in sequence, legal/financial case manager (active settlement and VA tracks), occasional software builder (CPA automation, gated on §7216 review) | workflow-plan.md       | 2026-06-27 (session patterns Jun 2026) |
| C-157 | `unemployment-fraud-detection/` — 25/29 sources verified; REPORT.md is final                                                                                                                                                                                                                                                          | workflow-plan.md       | 2026-06-27                             |
| C-158 | `fmla-retaliation-settlement/` — counter window, timeline, and figures are settled                                                                                                                                                                                                                                                    | workflow-plan.md       | 2026-06-27                             |
| C-159 | `va-disability/` — claim plan phases logged                                                                                                                                                                                                                                                                                           | workflow-plan.md       | 2026-06-27                             |
| C-160 | A prior run burned 4.78M tokens on a failed VR&E research run — cited as the model failure case to prevent                                                                                                                                                                                                                            | workflow-plan.md       | 2026-06-27                             |
| C-161 | Dual-Mac fleet: M4 Pro (48GB, primary workstation, SSH master) + M5 Air (24GB, runner/secondary, SSH linked)                                                                                                                                                                                                                          | workflow-plan.md       | 2026-06-27                             |
| C-167 | Cost diagnosis: no routing discipline currently — "same model for a 5-line boilerplate stub as for a cross-product architectural decision"                                                                                                                                                                                            | workflow-plan-v2.md    | 2026-06-27                             |
| C-168 | Estimated token allocation: 40–50% routine generation, 25–30% complex multi-file dev (recovery-platform/rag-system), 15–20% research/strategy, 5–10% high-stakes judgment                                                                                                                                                             | workflow-plan-v2.md    | 2026-06-27                             |
| C-190 | recovery-platform: 5 products, 1,954 files, ~387K lines; TypeScript monorepo; Firebase/Firestore; React Native + Next.js + Angular 9                                                                                                                                                                                                  | workflow-plan-v2.md    | 2026-06-27                             |
| C-191 | recovery-platform has Maestro e2e flows (`e2e-maestro/`, `regroup/mobile/maestro/`) and Detox e2e on both mobile products                                                                                                                                                                                                             | workflow-plan-v2.md    | 2026-06-27                             |
| C-192 | recovery-platform CI is "zero automated test pipeline — only AI code review via `claude-code-review.yml`"                                                                                                                                                                                                                             | workflow-plan-v2.md    | 2026-06-27                             |
| C-193 | recovery-platform has CLAUDE.md at root and per-product; multi-agent swarm hooks already wired (`swarm-notify.sh`)                                                                                                                                                                                                                    | workflow-plan-v2.md    | 2026-06-27                             |
| C-194 | Angular 9 legacy in `regroup/web` is "the most expensive context to load" — the most complex part of the most complex codebase                                                                                                                                                                                                        | workflow-plan-v2.md    | 2026-06-27                             |
| C-195 | rag-system: 688 files, 290 TS; pnpm monorepo; Fastify + MCP + Next.js + pg-boss + pgvector                                                                                                                                                                                                                                            | workflow-plan-v2.md    | 2026-06-27                             |
| C-196 | rag-system has real CI (`ci.yml` unit+typecheck+lint, `e2e.yml` Docker-backed Vitest); comprehensive CLAUDE.md and test coverage structure                                                                                                                                                                                            | workflow-plan-v2.md    | 2026-06-27                             |
| C-197 | rag-system: active development (document classification, local embeddings); Railway deployment target; Sentry monitoring; "the technical foundation for the CPA consulting KB"                                                                                                                                                        | workflow-plan-v2.md    | 2026-06-27                             |
| C-198 | cpa-consulting: pure Markdown, no build, no tests; custom Claude Code skills/agents; well-structured CLAUDE.md with epistemic constraints and labeled financial figures; Aug-1 engagement start                                                                                                                                       | workflow-plan-v2.md    | 2026-06-27                             |
| C-199 | Current spend pattern: Claude Max $200/mo flat, primary tool; Opus 4.8 for planning/architecture; Sonnet 4.6 for implementation; no routing discipline                                                                                                                                                                                | workflow-plan-v2.md    | 2026-06-27                             |
| C-200 | recovery-platform: NO `ci.yml` exists — only `claude.yml` and `claude-code-review.yml`                                                                                                                                                                                                                                                | implementation-plan.md | (undated; ≤2026-07-14)                 |
| C-201 | rag-system: real CI exists (`ci.yml` + `e2e.yml`); no `EMBEDDING_PROVIDER` env var in `e2e.yml`                                                                                                                                                                                                                                       | implementation-plan.md | (undated; ≤2026-07-14)                 |
| C-202 | cpa-consulting: no code, no tests, pure Markdown workspace                                                                                                                                                                                                                                                                            | implementation-plan.md | (undated; ≤2026-07-14)                 |
| C-203 | All three repos have CLAUDE.md files; none have a Model Tier Policy block                                                                                                                                                                                                                                                             | implementation-plan.md | (undated; ≤2026-07-14)                 |
| C-204 | recovery-platform has Maestro flows at `e2e-maestro/` and `regroup/mobile/maestro/`                                                                                                                                                                                                                                                   | implementation-plan.md | (undated; ≤2026-07-14)                 |
| C-205 | OpenRouter is NOT yet configured anywhere                                                                                                                                                                                                                                                                                             | implementation-plan.md | (undated; ≤2026-07-14)                 |
| C-208 | "regroup/web uses Angular 9 with NODE_OPTIONS=--openssl-legacy-provider workarounds and a legacy build that is likely to fail on modern Node" — explicitly excluded from CI for this reason                                                                                                                                           | implementation-plan.md | (undated; ≤2026-07-14)                 |

---

## 3. Contradiction Register

**X-01 — Multi-agent fan-out for coding: banned pattern, or the corpus's own flagship feature?**

- **Position A:** Large multi-agent fan-out is the _worst_ pattern for coding — ranked #11 of 11
  ("How it works: an orchestrator decomposes a goal and spawns many worker agents in parallel
  worktrees... Why it ranks lowest: ~7–15x token cost, Anthropic says it's a poor fit for
  interdependent coding, and it overwhelms a solo reviewer.") — `solo-consultant-workflow.md`,
  ranking table and C-069. Backed by: "Anthropic reports multi-agent systems 'use about 15x more
  tokens than chat interactions'... explicitly noting they are 'less effective for tightly
  interdependent tasks such as coding.'" (C-026, C-027)
- **Position B:** A Builder/Judge two-model adversarial loop — "Rather than manually interacting
  with an AI, this setup runs a multi-round asynchronous loop... A Builder model generates code
  ... a secondary adversarial Judge model critiques it... The Builder refactors before you ever
  look at the file" — is v2.md's central recommendation (C-125), and `workflow-plan-v2.md`
  operationalizes it as a concrete `.claude/skills/judge-review/SKILL.md` for recovery-platform
  specifically because "complex multi-product patterns make unreviewed code riskiest" (C-175,
  C-176).
- **Researchable question:** Does a two-model Builder/Judge adversarial loop for coding tasks
  measurably differ — in token cost, defect-catch rate, or net review-time savings — from the
  "large multi-agent fan-out" pattern Anthropic's own guidance warns against, or is it the same
  failure mode at smaller scale?
- **Why it matters to the operator:** determines whether `workflow-plan-v2.md`'s flagship Phase 3
  recommendation (Judge-Builder skill for recovery-platform) is sound engineering practice or the
  exact anti-pattern `solo-consultant-workflow.md` ranks dead last.
- **Assigned to:** W1, W3

**X-02 — Cost architecture and model-routing ratio**

- **Position A:** Flat-rate subscription arbitrage — "$200/month vs ~$15,000 in raw API costs
  over 8 months is not a rounding error" (C-115); "Claude Code Max 20x — subscription arbitrage
  makes it dramatically cheaper than pay-as-you-go at scale" (v1.md, Decision Guide).
- **Position B:** Tiered/open-weight routing — "The most cost-effective architectures in 2026 use
  a decoupled, multi-tier execution strategy" (v2.md §1); the 80/15/5 rule "consistently delivers
  60–70% cost reduction vs. single-model setups" (C-133).
- **Further wrinkle (not previously flagged):** the corpus contains _three_ different, unreconciled
  routing ratios for the same operator: `solo-consultant-workflow.md`'s ~70% Sonnet / ~30% Opus,
  two-tier split with no cheap-model tier at all (C-010); v2.md's 80/15/5 Execution/Planning/
  Reasoning split (C-127); and `workflow-plan.md`'s separate three-tier A/B/C mapping keyed to the
  operator's actual (mostly non-coding) task mix (C-143). `workflow-plan-v2.md` adopts 80/15/5
  as "the" policy going forward (C-170) without ever addressing the 70/30 split or reconciling it
  with the earlier A/B/C mapping.
- **Researchable question:** For a solo operator's actual task mix, what tiered-routing split (if
  any) is cost-optimal against current pricing and quality data, and does the answer differ for a
  code-heavy repo vs. a research/knowledge-repo workload?
- **Why it matters to the operator:** `workflow-plan-v2.md`'s headline $80–120/mo blended target
  depends entirely on the 80/15/5 split holding up; if it doesn't, neither does the number.
- **Assigned to:** W5

**X-03 — Ceremony level: "dumbest thing that works" vs. mandatory context/spec infrastructure**

- **Position A:** "the dumbest possible thing that will work": long descriptive function names
  over clever abstractions, plain SQL over ORM gymnastics (C-022, quoting Armin Ronacher). The
  same document ranks Kiro (#10) a "sledgehammer to crack a nut" (C-054, C-070) and spec-kit
  (#8) as "the volume of generated markdown is tedious to review and it's heavy for routine work"
  (C-072).
- **Position B:** v1.md treats a maintained `AI.md` file as "load-bearing infrastructure" that
  must contain "explicit architectural system maps, module boundaries and ownership, typing
  rules and conventions" (C-107). v2.md mandates a CLAUDE.md/.cursorrules file that "must include"
  a tech-stack overview, an exact Definition of Done, and a tier-enforcement rule (C-131), wired to
  an automated Judge-Builder loop. `workflow-plan-v2.md` operationalizes this into multi-paragraph
  Tier Policy blocks, per-repo calibration tables, and a fixed JSON-schema judge-review skill
  (C-170, C-171, C-176) — substantial specification ceremony per repo.
- **Researchable question:** Where is the actual break-even between minimal-ceremony practice and
  structured spec/context infrastructure (AI.md, Definition-of-Done blocks, Judge-Builder schemas)
  for a solo operator — does the ceremony pay for itself in reduced token/review cost, or does it
  become the same "sledgehammer to crack a nut" the corpus itself warns against for Kiro/spec-kit?
- **Why it matters to the operator:** the stated quality bar (TDD-backed, well-documented code)
  pulls toward ceremony; the stated hard constraint (review capacity) pulls toward minimalism. The
  corpus argues both without reconciling them.
- **Assigned to:** W1, W4

**X-04 — Where the bottleneck actually is**

- **Position A:** "Your review capacity, not model throughput or subscription limits, is the
  binding constraint" (C-003). Reinforced in the Caveats section: "Solo-reviewer ceiling is real
  and central. Every parallelism gain is capped by your ability to review output. Multiple
  practitioners independently report becoming the bottleneck at 3+ concurrent sessions." (C-084)
  — `solo-consultant-workflow.md`.
- **Position B:** v1.md, v2.md, `workflow-plan.md`, `workflow-plan-v2.md`, and
  `implementation-plan.md` all frame the central problem as cost/token throughput and never once
  name review capacity as a constraint. Most explicit: "The bottleneck is not the $200/mo
  subscription. It is routing 80% of your work through Opus/Sonnet when DeepSeek V4 Flash could
  handle it at a fraction of the cost." (C-188, `workflow-plan-v2.md`). This is a disagreement of
  omission, not an explicit rebuttal — none of the four cost-focused documents engages with the
  review-capacity thesis at all.
- **Researchable question:** For this operator's actual output volume, is review capacity or
  model/subscription cost the binding constraint on throughput — and does optimizing the cost
  side (per `workflow-plan-v2.md`'s entire program) risk raising throughput past review capacity
  without the plan ever checking for that?
- **Why it matters to the operator:** the operator_profile's explicit hard constraint is
  "throughput that outruns review capacity is a defect, not a gain" — a cost-optimization program
  that increases velocity without checking this could violate the operator's own stated
  constraint.
- **Assigned to:** W9, W5

**X-05 — The Redelinghuys anecdote's dollar figures disagree with v1.md's own model of the same
scenario (discovered; not on the known-conflicts list)**

- **Position A:** `solo-consultant-workflow.md` reports the practitioner's ~10-billion-token,
  8-month usage "would have cost 'over $15,000' at API rates" but "ran him 'around $800 total…
  a 93% saving.'" (C-006, C-007)
- **Position B:** v1.md, describing what reads as the identical scenario ("full-time developers
  using Claude Code continuously across multiple repositories easily consume 10+ billion tokens
  over 8 months" against the same ~$15,000 API estimate), computes the subscription-side cost as
  a flat $1,600 (8 × $200/mo) for "~89% reduction" (C-098, C-099, C-100) — not $800/93%.
- **Researchable question:** which figure, if either, is correct — does the $800 come from
  Redelinghuys not paying the full $200/mo for the entire period, a different plan tier, a
  different accounting method, or does one of the two documents round/fabricate a number to fit
  its narrative?
- **Why it matters to the operator:** this ~$800 discrepancy sits under the corpus's single most
  load-bearing "proof" of subscription arbitrage; if two documents in the same corpus can't agree
  on the dollar total for what is presented as the same anecdote, the headline savings claim needs
  primary-source verification, not restatement.
- **Assigned to:** W5

**X-06 — The benchmark "winner" flips depending on which benchmark is cited (discovered)**

- **Position A:** "On SWE-bench Pro, Claude Code leads by 28 percentage points over Copilot
  (69.2% vs 41.0%)" — v1.md, C-096 — used to support "Maximum benchmark performance, cost is
  secondary → Claude Code Max 20x — 88.6% SWE-bench Verified, 69.2% SWE-bench Pro" in its
  Decision Guide.
- **Position B:** "Terminal-Bench 2.1 Score: Claude Code Max 78.9% (Opus 4.8)... Codex CLI +
  GPT-5.5 83.4%" — v2.md, C-118 — GPT-5.5/Codex CLI outscores Claude Code Max by 4.5 points on
  this benchmark.
- `workflow-plan-v2.md` acknowledges the tension directly ("Different benchmarks measure different
  things") but asserts, without independent verification, that "SWE-bench Pro... maps to your work
  better than Terminal-Bench" (C-162) — a claim the ledger records but does not adjudicate.
- **Researchable question:** which benchmark — SWE-bench Verified/Pro or Terminal-Bench 2.1, if
  either — is a validated proxy for multi-file, interdependent professional coding work, and do
  current (re-verified) scores still show Claude Code leading on the more relevant one?
- **Why it matters to the operator:** the corpus's tool choice (stay on Claude Code Max) rests
  partly on a benchmark comparison that a second document in the same corpus contradicts using a
  different benchmark, with no adjudication of which benchmark should be trusted.
- **Assigned to:** W1

---

## 4. Recommendation Inventory

Deduplicated across the corpus. "Load-bearing" = other recommendations in the corpus assume this
one is true/adopted.

1. **Adopt the "Spec-Locked Single Loop" (Explore→Plan→Code→Commit, tight context management) as
   the default workflow.** — `solo-consultant-workflow.md`. **Load-bearing**: the document's
   entire staged rollout (C-080) and its #1-ranked status (C-079) assume this as the base loop.
   In ceremony tension with recommendation 10 below (see X-01, X-03).
2. **Route ~70% of tasks to Sonnet, ~30% to Opus.** — `solo-consultant-workflow.md` (C-010).
   **Contradicted** by the 80/15/5 rule (recommendation 8) and by `workflow-plan.md`'s separate
   three-tier A/B/C mapping (recommendation 7-adjacent, C-143). Not load-bearing beyond its own
   document.
3. **Cap parallel worktrees at 2–3.** — `solo-consultant-workflow.md` (C-046, C-076).
   **Load-bearing** for that document's Workflow B and its #4/#6 ranking entries; not addressed
   or contradicted elsewhere in the corpus.
4. **Add a fresh-context reviewer subagent / Writer-Reviewer split.** — `solo-consultant-workflow.md`
   (C-048, C-075). Not directly contradicted, but competes with recommendation 10 (Judge-Builder
   loop) as a different mechanism for the same goal (a second opinion before the operator reviews
   output) — Phase C will need to choose or reconcile.
5. **Hooks + a lean CLAUDE.md as foundational infrastructure.** — `solo-consultant-workflow.md`
   (C-034–C-040, C-077). **Load-bearing**: ranked #3, underpins the verification-gate story
   (its own #2-ranked entry, C-078) that the #1-ranked loop depends on. Consistent with, but far lighter
   than, recommendation 8's CLAUDE.md-centric ceremony (see X-03).
6. **Two-Tier Strategic Stack (Cursor/Copilot autocomplete + Claude Code Max heavy lifting).** —
   v1.md (C-106). **Load-bearing** for v1.md's entire argument. Superseded/contradicted by v2.md's
   three-tier 80/15/5 model (recommendation 8) and never explicitly reconciled except by
   `workflow-plan-v2.md`'s blended dollar target.
7. **Maintain a root `AI.md`/CLAUDE.md context file, claimed to cut token use "by up to 40%."** —
   v1.md (C-107). **Load-bearing**: `workflow-plan.md` and `workflow-plan-v2.md` both assume this
   figure is true and build CONTEXT.md/WORKFLOW.md (recommendation 11) and "tier policy in
   CLAUDE.md" (recommendation 8) on top of it without re-verifying the 40% figure.
8. **Adopt 80/15/5 tier routing.** — v2.md, `workflow-plan-v2.md`, `implementation-plan.md`
   (C-127, C-170). **Load-bearing** for the entire v2/workflow-plan-v2/implementation-plan chain
   (Judge-Builder tiering, the $80–120/mo cost target, and the CI phase ordering all reference it).
   **Contradicts** recommendations 2 and 6.
9. **Install Hermes Agent + Manifest + OpenRouter as a full orchestration stack.** — v2.md (C-129,
   C-130, C-132). **Explicitly reversed downstream**: `workflow-plan-v2.md` states "Do NOT use
   Hermes Agent CLI or Manifest proxy (too much config overhead for a solo developer)" (C-172) —
   a direct in-corpus reversal within the same document lineage. Not load-bearing since
   immediately overridden.
10. **Judge-Builder adversarial loop.** — v2.md (concept, C-125) → `workflow-plan-v2.md`/
    `implementation-plan.md` (concrete skill spec, C-175, C-176, C-209). **Load-bearing** for
    `workflow-plan-v2.md` Phase 3 and `implementation-plan.md` Phase 3; contingent on X-01's
    unresolved question of whether this is sound practice or a smaller version of the
    multi-agent anti-pattern.
11. **Create `CONTEXT.md` per subject + `WORKFLOW.md` at the repo root.** — `workflow-plan.md`
    (C-140, C-141). **Status ambiguous**: `workflow-plan-v2.md` ("Version 2.0, supersedes
    workflow-plan.md") never mentions either file again — silently dropped, not explicitly
    countermanded.
12. **Pre-run "question statement" + Draft→Deep→Verify research-run staging.** — `workflow-plan.md`
    (C-145–C-147). **Status ambiguous**, same as above: absent from `workflow-plan-v2.md` and
    `implementation-plan.md`, both of which pivot entirely to code-repo tier/CI/Judge concerns and
    drop the research-run-cost material.
13. **Dual-Mac fleet mapping (M4 = interactive/judgment, M5 = batch/Tier C).** — `workflow-plan.md`
    (C-151, C-152) **and** `workflow-plan-v2.md` (Phase 5, not separately IDed as it restates
    C-151/C-152). Consistent across both versions — carried forward, not dropped.
14. **§7216 constraint: never send client tax data to OpenRouter; keep client-data workflows
    local.** — `workflow-plan.md` (C-150), `workflow-plan-v2.md`, `implementation-plan.md`.
    **Load-bearing** and consistent across all three — a hard compliance constraint every
    OpenRouter recommendation in the corpus must route around.
15. **Add a real CI pipeline (typecheck + unit tests) to recovery-platform.** —
    `workflow-plan-v2.md` (Phase 4), `implementation-plan.md` (Phase 4, C-207). **Load-bearing**:
    the Judge-Builder "quality without extra review time" framing (recommendation 10) assumes this
    CI exists; per the corpus's own dependency graph, Maestro CI (recommendation 16) depends on it.
16. **Wire Maestro e2e into CI.** — `workflow-plan-v2.md` (Phase 4.2), `implementation-plan.md`
    (Phase 7, C-181, C-211). Depends on recommendation 15 per the corpus's own stated ordering.
17. **Add tier annotations to the `cpa-consulting/prompts/` directory.** — `workflow-plan-v2.md`
    (Phase 7, C-185), `implementation-plan.md` (Phase 6). Consistent between the two.
18. **Use LocalEmbeddingProvider in rag-system CI to drop the Gemini dependency.** —
    `workflow-plan-v2.md` (Phase 6.1, C-182), `implementation-plan.md` (Phase 5). Consistent;
    `implementation-plan.md` adds the caveat that this is conditional on the LocalEmbeddingProvider
    feature itself being merged.
19. **Weekly review cadence (~15 minutes).** — `workflow-plan.md` (C-154) and
    `workflow-plan-v2.md` (C-186) — same cadence, different checklist substance (research-run
    quality in the v1 plan vs. CI/Judge-pass/routing-discipline quality in the v2 plan),
    reflecting the underlying pivot from a research-ops framing to a dev-ops framing between the
    two plan versions.
20. **Anti-over-engineering guardrails in CLAUDE.md** ("do the simplest thing that works," ask
    before adding dependencies). — `solo-consultant-workflow.md` (C-022, C-082). **In tension**
    with the ceremony built up by recommendations 7–10 and 15–18 (see X-03).

---

## 5. Extraction Notes

**Files read in full, with size:**

| File                            | Lines | Words | Role in corpus                                                      |
| ------------------------------- | ----- | ----- | ------------------------------------------------------------------- |
| `solo-consultant-workflow.md`   | 113   | 3,013 | Prior deep-research output; ranked-workflow prior art               |
| `v1.md`                         | 233   | 1,471 | Benchmark/cost comparison, subscription-arbitrage argument          |
| `v2.md`                         | 215   | 1,355 | Tiered multi-model / Judge-Builder / OpenRouter argument            |
| `workflow-plan.md`              | 309   | 2,104 | Personalized plan built on v1.md; research-ops framing              |
| `workflow-plan-v2.md`           | 540   | 3,453 | Personalized plan built on v1+v2; live repo audits; dev-ops framing |
| `implementation-plan.md`        | 569   | 2,944 | Executable phase plan derived from workflow-plan-v2.md              |
| `android-release-build-plan.md` | 480   | 1,959 | Style reference only — no research claims extracted, see below      |

Files excluded per instructions and confirmed absent/out of scope before extraction began: the
entire `prompts/` subdirectory (this project's own instructions); `solo-consultant-workflow-optimized.md`
(308 lines — the original combined prompt, not source material); `corpus-ledger.md`, `REPORT.md`,
and `findings/` (none existed prior to this file being written).

**Discrepancy between the phase prompt's summary and its own corpus table:** the phase-a-ledger.md
header describes "the six corpus documents," but its `<corpus>` table lists seven files
(`workflow-plan.md` and `workflow-plan-v2.md` are two separate files sharing one table row). All
seven were read and extracted from (except `android-release-build-plan.md`, per its explicit
"style reference only" instruction). This ledger treats the table, not the summary count, as
authoritative.

**Structural conventions noted, not extracted as research claims (per instruction for
`android-release-build-plan.md`, and observed identically in `workflow-plan-v2.md` and
`implementation-plan.md`):** all three documents share one planning-doc format — a "Phase 0:
Ground Truth" section up front separating "Confirmed facts (do not re-derive)" from "Known gaps
(what's still needed)"; each subsequent phase states an estimated time, a prerequisite/blocker,
whether human action is required, literal shell commands under "what to implement," a checkbox
"Verification checklist" phrased as runnable commands, an "Anti-pattern guards" list, and (where
applicable) a literal `git commit` step; each document ends with a phase dependency graph and a
final end-to-end verification script. This is the operator's standing planning-doc convention,
not something unique to code-focused work — `android-release-build-plan.md` (a hardware/mobile
build task with no AI-research content) uses the identical structure to `implementation-plan.md`
(an AI-workflow-tooling task).

**Claims/figures I suspect are wrong or unstable, flagged as suspicion only — not corrected in the
register above:**

- v1.md's own table (C-093) attributes the OpenRouter Hybrid Stack's SWE-bench Pro score (59.0%)
  to "MiniMax M3 / GLM-5.1 orchestration," while the same table's column header and every other
  row in that column describe the stack as "DeepSeek V4." Either the score belongs to a different
  stack configuration than the one being compared, or the table conflates two different hybrid
  configurations under one header.
- The dollar/percentage mismatch between `solo-consultant-workflow.md` (C-007: $800, 93%) and
  v1.md (C-099, C-100: $1,600, 89%) for what reads as the same Redelinghuys-style anecdote (see
  X-05) — one or both figures were likely restated loosely rather than sourced independently.
- Model-name drift across documents describing supposedly current models: v1.md and
  `workflow-plan-v2.md` reference `claude-opus-4.8` / `claude-sonnet-4.6`, while v2.md's own
  environment-variable example under its "Judge-Builder" setup instructions uses
  `anthropic/claude-3.5-sonnet` and `anthropic/claude-opus` — an older naming scheme, inconsistent
  with the rest of the same document's benchmark table (which uses "Opus 4.8"). This suggests the
  setup instructions in v2.md were not updated when the rest of the document's benchmark figures
  were.
- v1.md's Copilot/Codex context-window figure (~200,000 tokens, C-095) and v2.md's Codex CLI+GPT-5.5
  figure (512k tokens, C-119) describe what the documents treat as the same competitor product but
  differ by more than 2.5x — plausibly because v1.md is describing GPT-5.2-era Copilot and v2.md a
  later GPT-5.5-era Codex CLI, but the corpus never states this explicitly; the two figures should
  not be treated as interchangeable.
- The 88.6%/69.2%/78.9% SWE-bench/Terminal-Bench figures for "Claude Code Max" appear precise to
  a tenth of a percentage point across two independently-styled documents with no shared citation
  — a pattern more consistent with fabricated-plausible figures than sourced benchmark runs. Flag
  for W1 to check whether any of these benchmark numbers resolve to a real, citable leaderboard
  entry at all.

**Ambiguous or undated items:**

- `implementation-plan.md` carries no internal date; it is presented as derived directly from
  `workflow-plan-v2.md` (dated 2026-06-27) and was last saved 2026-07-14, so its assertions are
  dated as "undated, ≤2026-07-14" in the register above.
- v1.md and v2.md carry no internal dates at all; the only dating evidence in the corpus is
  `workflow-plan-v2.md`'s own characterization of them as "2026 Q1" and "2026 Q2" respectively.
  This ledger uses that characterization but flags it as itself a claim, not a directly-stated
  fact from the primary documents.

**Coverage gaps — subject areas the corpus never addresses:**

- **The entire consulting side is absent.** Nothing in the corpus discusses rapid domain ramp-up
  for a new client engagement (W6), methodologies for diagnosing internal process/organizational
  dysfunction before recommending automation (W7), or productized-consulting mechanics — pricing,
  scoping, phase-gated engagement structure, IP reuse across clients, client-data confidentiality
  as a general practice rather than the one narrow §7216/CPA-specific carve-out (W8). The corpus
  is entirely a software/AI-tooling optimization exercise; the operator_profile's stated "general
  business consultant who streamlines internal operations" role and "distinguish problems
  automation can solve from problems only process or org change can solve" recurring demand have
  no prior art here at all. Confirmed: this is a genuine gap, not a sampling artifact — all seven
  files were read in full and none touches this material.
- **Documentation/knowledge-repo coherence (W4) is addressed only glancingly** — as a token-cost
  optimization (AI.md/CLAUDE.md cutting exploration cost) and as tier-routing metadata (annotating
  `prompts/` files), never as a documentation-quality or fact-verification practice in its own
  right. Nothing in the corpus discusses doc-drift detection, citation/fact verification
  workflows, or keeping a no-code knowledge repository (like this research repo itself, or
  `cpa-consulting/`) internally consistent as it grows — despite the operator_profile explicitly
  naming "code-free knowledge/documentation repositories" as half of the operator's actual work.
- **W2 (multi-project orchestration and shared context) has only partial coverage.** The corpus
  addresses a single operator running one Claude Code session against one repo at a time (plus a
  two-machine batch/interactive split); it does not address the operator_profile's "desired
  session topology" of one orchestrator holding shared context _across projects within one
  session_, or session-resume/handoff mechanics beyond the one checkpoint-file mention for a
  failed overnight batch run (C-152).
- **No discussion of e2e/mobile testing beyond Maestro wiring already in place.** W3's broader
  scope (mutation testing, contract tests, golden files, screenshot diffs) is entirely unaddressed
  — the corpus's testing content is limited to unit/typecheck CI and one Judge-Builder pattern.
- **No discussion of solo-operator capacity math, WIP limits, or context-switching cost as a
  general subject (W9)** beyond the review-capacity thesis in `solo-consultant-workflow.md`
  (C-003, C-084, C-085), which the rest of the corpus does not engage with at all (see X-04).

**Claim-count sanity check:** 211 total (187 in §1, 24 REPO-FACT in §2). No claim from
`android-release-build-plan.md` was extracted into either register table, per its "style
reference only" treatment.
