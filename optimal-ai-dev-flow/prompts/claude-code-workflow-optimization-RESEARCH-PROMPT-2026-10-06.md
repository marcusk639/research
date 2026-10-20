# Research Prompt — Optimal Claude Code Workflow (generic → personalized)

**Designed:** 2026-10-06 · **Intended runner:** `deep-research` skill in dynamic/multi-phase mode
**Deliverables it requests:** Markdown + DOCX

> **How to use.** Paste everything inside the `<prompt>` block below as the research directive.
> The notes after it explain the design choices and what to adjust if circumstances change.

---

<prompt>

<role>
You are a senior research analyst specializing in agentic AI developer tooling and LLM-assisted
software workflows. You are rigorous about evidence, skeptical of vendor marketing, and you
prioritize subtraction over accumulation. You are writing for a single named reader — a staff-level
software engineer with a large, heavily-customized Claude Code installation — not for a general
audience.
</role>

<non_negotiable_preconditions>
Do these BEFORE any web search. Skipping them invalidates the work.

1. **Read the existing corpus first. There is ~600KB of prior research on this exact topic.**
   - `~/dev/research/optimal-ai-dev-flow/` — REPORT.md (~140KB), corpus-ledger.md (~116KB),
     WORKFLOW-DECISION.md, solo-consultant-workflow-optimized.md, solo-consultant-workflow.md,
     implementation-plan.md, workflow-plan.md, workflow-plan-v2.md, v1.md, v2.md,
     LEDGER-HIGHLIGHTS.md, plus `findings/` and `playbooks/`.
   - `~/dev/research/app-dev/` — REPORT.md (~37KB), TOOLING-MATRIX.md (~17KB),
     VERIFICATION-STRATEGY.md (~20KB), SOURCES.md (~26KB), ADOPTION-PLAN.md, GUIDE.md, RISKS.md,
     GAPS.md, SPEC-FORMAT.md, STAGE0-RESULTS.md, STAGE1-RESULTS.md, plus `ledger/`.

   You do not need to read every byte, but you must read both REPORT.md files, both tooling/
   decision documents, and the GAPS/RISKS files in full. Then state explicitly, in your output,
   **what is already settled and what you are adding.**

2. **Produce a DELTA, not a fresh report.** Any finding already established in the corpus should be
   cited to it in one line, not re-derived. Your value is: (a) what has changed since those
   documents were written, (b) what they got wrong, (c) what they never covered, and
   (d) personalization to this specific installation, which they largely lack.

3. **Resolve contradictions between the two corpora explicitly.** `app-dev/` and
   `optimal-ai-dev-flow/` were produced separately and may disagree. Where they do, name both
   positions, say which is better supported, and why. Do not silently pick one.

4. **Check for a staleness trap.** Determine each corpus document's date and flag any load-bearing
   claim that depends on model lineups, pricing, context windows, or product features that have
   changed since. Do not assume recency from file order; check git log.
   </non_negotiable_preconditions>

<measured_baseline>
These are real measurements from this installation taken 2026-10-06 via `/context`. **Re-measure
rather than trusting them** — run `/context` (and `/context all`) yourself and report current
figures — but use them to understand the shape of the problem.

| Component                    | Measured                      | Note                                            |
| ---------------------------- | ----------------------------- | ----------------------------------------------- |
| Model                        | Opus 5, 1M context            | `claude-opus-5[1m]`                             |
| Session usage at measurement | 523.2k / 1M (52%)             | mid-session, after heavy research               |
| **Skills**                   | **309 skills · 38.7k tokens** | always loaded                                   |
| **Custom agents**            | **148 agents · 15.5k tokens** | always loaded                                   |
| Memory files                 | 12 files · 9.8k tokens        | CLAUDE.md + rules/, duplicated across two homes |
| MCP tools                    | 355 tools · **31 tokens**     | deferred/on-demand — working as intended        |
| System prompt                | 4.1k tokens                   |                                                 |
| Deferred system tools        | 24.1k tokens                  |                                                 |
| Messages                     | 455k tokens (45.5%)           |                                                 |

**Derived facts worth testing:**

- Always-on overhead before any work ≈ **64k tokens** (skills + agents + memory + system prompt).
  On a 200k-context model that would be ~32% of the window consumed at startup.
- The MCP deferral mechanism is working extremely well (355 tools → 31 tokens). Skills and agents
  are NOT deferred and are the dominant fixed cost.
- The harness itself flagged: _"Read results using 213.4k tokens (21%) → save ~64k"_ — i.e. tool
  output handling, not instructions, dominated this session's consumption.
- Memory files appear duplicated between `~/.claude/` and `~/.claude-acct2/` (same filenames,
  same sizes). Verify whether both are actually loading.

**The reader has also built or installed at least five overlapping token/context tools:**
`token-optimizer`, `token-optimizer-mcp`, `claude-token-optimizer`, `token-savior`,
`claude-context`, plus the `context-mode` and `claude-mem` plugins. Assess overlap and
contention — multiple context-management layers competing can cost more than they save.
</measured_baseline>

<research_questions>

### Phase 1 — Generic: what is the optimal Claude Code workflow in late 2026?

Answer each with evidence, not assertion. Where the corpus already answers it, cite and move on.

1. **Context economics.** What actually consumes context in practice, in what proportion? What are
   the current best practices for: tool-output handling, subagent isolation, compaction timing,
   when to start a fresh session vs continue, and what belongs in CLAUDE.md vs a skill vs nothing.
   Quantify where possible.

2. **Model routing.** Current Claude model lineup, pricing, context windows, and the honest
   decision boundary between them. When is Haiku genuinely sufficient (and when does routing to it
   cost _more_ through retries and escalation)? Where does Sonnet beat Opus on cost-adjusted
   throughput? What does the evidence say about the common claim that cheap-model delegation
   degrades output — is there measurement, or only anecdote? Cover subagent model override,
   default-subagent-model configuration, and any routing automation.

3. **Subagents vs. a single agent.** What does the evidence actually support? Cover: context
   isolation as the primary benefit, the cost of cold-start context re-derivation, fan-out for
   independent tasks, when a fork (inheriting context) beats a fresh agent, and documented failure
   modes — agents returning status messages instead of work, conflicting parallel edits, and
   over-spawn. Be concrete about the break-even point.

4. **Multi-session strategy.** When to split work across sessions, how to hand off reliably
   (session files, memory tools, scratchpads), and what degrades as a single session grows.

5. **Skills, hooks, agents, plugins, MCP.** For each: what it is actually good for, its true
   context cost, and its failure modes. Critically: **what is the right number of each?** Address
   the specific hypothesis that 309 skills and 148 agents is far past the point of diminishing
   returns, and that discovery/selection accuracy degrades as the catalog grows.

6. **Verification and quality control.** Patterns that catch model error before it reaches the
   user: adversarial review passes, TDD enforcement, hooks as guardrails, independent verifier
   agents. What is the measured effectiveness of each?

### Phase 2 — Discovery: tools and techniques the reader does not know about

**This is an explicit mandate, not a bonus.** Surface **at least 10 tools, techniques, or
practices** that appear in neither corpus and are not already installed. For each: what it does,
why it might matter here, maturity, cost, and a clear adopt / trial / watch / reject call.

Required named target:

- **Hermes AI agent** (https://hermes-agent.nousresearch.com/, Nous Research). Determine what it
  actually is — do not assume. Assess fit against this workflow specifically, and say plainly if
  it does not fit.

Also sweep for: model-routing layers and proxies; context-compression and retrieval tooling;
agent orchestration frameworks; spec-driven and plan-driven development harnesses; evaluation and
regression harnesses for agent output; terminal/IDE agent alternatives worth comparing against
Claude Code; and anything emerging that credibly changes the cost curve.

### Phase 3 — Personalization: this reader's actual repositories

Generic advice is the easy half. This half must be concrete and per-repo.

**Verify the repo inventory yourself** (`ls -d ~/dev/*/`); the reader's list was partial. Known
active repos include at least: `recovery-platform`, `rag-system`, `cpa-consulting`, `cpa-backend`,
`llm-guides`, `research`, `smm-therapy`, `veteran-claims-app`, `doc-classifier`, `claude-config`,
`claude-crawler`, `content-creator`, `cowork-tools`, `software-dev-team`, `persona-twin`, plus
several token-optimizer variants. Read each repo's `CLAUDE.md` (and `~/dev/CLAUDE.md`, which
describes the workspace and flags legacy/superseded projects — respect those flags).

For each **active** repo, produce a concrete profile:

- What kind of work happens there (feature code, research/markdown, infrastructure, client docs)
- The right model tier for the bulk of that work, and why
- Which skills/agents/hooks genuinely serve it — and which installed ones are dead weight for it
- Session strategy: long-running vs. short, when to fork, when to start fresh
- Repo-specific context hazards (e.g. `recovery-platform` is a large RN/Firebase monorepo with
  nested CLAUDE.md files; `cpa-consulting` is a markdown knowledge repo whose canonical workstream
  is `docs/issue-synthesis/`; `research` holds very large reports that blow context if read whole)

Then produce a **consolidated configuration recommendation**: what to keep, demote, or remove
globally, with the token saving estimated for each change.

</research_questions>

<critical_constraints>

1. **Lead with subtraction.** With 309 skills and 148 agents installed, the highest-value finding
   is probably what to remove. Any recommendation to ADD something must state what it replaces or
   justify the marginal context cost explicitly.

2. **Every recommendation needs a cost and a benefit.** "Use X" is not a finding. "Use X instead of
   Y, saving ~Nk tokens per session, at the cost of Z" is.

3. **Make it measurable.** Propose a before/after measurement method so the reader can tell whether
   any change actually helped. A workflow plan that cannot be evaluated is worthless. Define the
   metrics (startup overhead, tokens per task, retries, wall-clock, cost per completed task).

4. **Separate evidence from inference.** Label every claim: `[measured]` (from this installation),
   `[primary]` (vendor docs, model cards, pricing pages, official changelogs), `[community]`
   (Reddit, HN, Discord, forums), `[vendor]` (a company selling the thing), `[inference]` (yours).
   Treat `[vendor]` and `[community]` as unverified unless corroborated.

5. **Respect the measurement-vs-model distinction.** Benchmarks on agentic coding are noisy and
   often vendor-run. Where you cite a benchmark, name who ran it and on what.

6. **Do not recommend anything that conflicts with the installed hook policy** without flagging the
   conflict: writes to `.env`/`pnpm-lock.yaml` are blocked; linter/formatter configs are
   write-protected; Prettier reformats after every edit; a Stop hook requires a semantic-harvest
   write. These are enforced, not advisory.
   </critical_constraints>

<source_requirements>
Search breadth is explicitly requested. Cover at minimum:

- **Primary/authoritative:** Anthropic docs, engineering blog, model cards, pricing and changelog
  pages; Claude Code release notes; OpenAI, Google DeepMind, Meta equivalents where relevant.
- **Practitioner community:** Reddit (r/ClaudeAI, r/ClaudeCode, r/LocalLLaMA, r/ChatGPTCoding),
  Hacker News, GitHub discussions and awesome-lists, Discord/forum summaries where citable.
- **Independent analysis:** Substack and newsletters covering agentic AI and LLM tooling; technical
  blogs by practitioners with real deployments; arXiv for anything with measurement.
- **Vendor material** is acceptable as a source about _its own product's capabilities_ and nothing
  more.

Minimum 25 distinct sources, with a bias toward the last 6 months — this space moves fast and
anything older than ~12 months on model routing or pricing should be treated as suspect.
Prefer sources containing numbers over sources containing opinions.
</source_requirements>

<scope_boundaries>
**In scope:** Claude Code workflow, context management, model selection and routing, subagent and
session strategy, skills/hooks/agents/plugins/MCP configuration, adjacent tooling, and per-repo
personalization.

**Out of scope — do not spend effort here:** prompt-engineering technique tutorials (well covered
elsewhere); general LLM theory; building a custom agent framework from scratch; anything requiring
the reader to leave Claude Code as the primary harness unless the evidence is strong enough to say
so explicitly; and any business, clinical, or personal-benefits content from other research
subjects in this repo.
</scope_boundaries>

<adversarial_review>
Before finalizing, run an adversarial pass over your own draft — ideally via a separate verifier
agent with fresh context. It must specifically attempt to refute:

- The central workflow recommendation
- Every quantitative claim about token cost or savings
- Any claim that a tool is "better" without a measured comparison
- The subtraction recommendations (would removing these actually break something the reader uses?)
- Whether the per-repo advice is genuinely repo-specific or generic advice with a repo name attached

Fold corrections in and **state in the final document what the review changed.** If a headline
conclusion did not survive, say so prominently rather than quietly editing it.
</adversarial_review>

<deliverables>
Write to `~/dev/research/optimal-ai-dev-flow/`:

1. **`CLAUDE-CODE-WORKFLOW-PLAN-<YYYY-MM-DD>.md`** — the main deliverable:
   - Executive summary: the 5 highest-impact changes, each with estimated token/cost impact
   - What the existing corpus already settled (brief, cited)
   - What changed, what was wrong, what was missing
   - Phase 1: generic optimal workflow
   - Phase 2: discovery — new tools, with adopt/trial/watch/reject calls
   - Phase 3: per-repo profiles and the consolidated configuration recommendation
   - A prioritized action list: change, effort, expected saving, how to measure it
   - Risk register: what could break, and the rollback for each
   - Sources, with provenance tags
   - "Verify before relying": every figure that is inferred, vendor-sourced, or unconfirmed

2. **`CLAUDE-CODE-WORKFLOW-PLAN-<YYYY-MM-DD>.docx`** — same content, professionally formatted
   (cover page, contents, heading hierarchy, formatted tables).

   _Rendering recipe that works in this environment (learned the hard way):_ `npm install docx`
   locally first — it is NOT preinstalled despite the skill's claim; use a **static contents list**
   rather than docx-js `TableOfContents` (the field renders blank in PDF export); pass
   `soffice.py --outdir` an **absolute** path (relative exits 1 silently); and **always verify by
   rendering to JPEG via `pdftoppm` and viewing the pages** — every rendering bug produces a
   successful build with a nonzero-byte file.

Keep the markdown under ~6,000 words. Density over length. If a section cannot be made concrete,
say "insufficient evidence found" rather than padding it.
</deliverables>

<anti_patterns>
Do not produce: an undifferentiated list of tools; advice that would apply to any Claude Code user
(the personalization is the point); recommendations to install more things without removing any;
unsourced token-cost numbers; a report that re-derives what the existing corpus already settled; or
confident claims about model capabilities you did not verify against a primary source this week.
</anti_patterns>

</prompt>

---

## Design notes — why this prompt is built the way it is

**The single most important element is the precondition block.** Earlier work in this repo was
damaged by synthesizing from a newer document while skipping an older one that held the
adversarially-verified facts. With ~600KB of existing research on this exact topic, a prompt that
does not mandate reading it first would produce an expensive, contradictory duplicate. The delta
framing is what converts that corpus from a liability into an asset.

**Grounding in measured numbers rather than asking for generic advice.** The `/context` figures
(309 skills = 38.7k, 148 agents = 15.5k, 355 MCP tools = 31 tokens) turn a vague "optimize my
setup" into a specific, falsifiable problem. The instruction to _re-measure_ rather than trust the
snapshot guards against staleness.

**Subtraction is forced, not suggested.** Left to its own devices a research agent will produce a
list of things to add. The constraint that every addition must name what it replaces is the main
defense against a recommendation set that makes the context problem worse.

**The discovery mandate has a floor (≥10 tools).** "Tools I may not have heard of" is otherwise
easy to satisfy with two obscure mentions. Hermes is named explicitly with an instruction to verify
rather than assume, and with permission to reject it.

**Adversarial review is built in.** Two research passes in the prior session each came back with
multiple critical errors that survived a confident first draft. Requiring the final document to
_state what the review changed_ prevents quiet editing.

**Provenance tagging** (`[measured]`/`[primary]`/`[community]`/`[vendor]`/`[inference]`) matters
here because much of the agentic-tooling literature is produced by companies selling the tooling.

### Things to adjust before running

- **Scale.** This is a three-phase brief; if run with the `deep-research` skill's deeper modes it
  will fan out widely. Consider running Phase 1+2 first and Phase 3 as a follow-up, since Phase 3
  requires reading many repo `CLAUDE.md` files and will consume context.
- **The duplicate memory-file question** (`~/.claude/` vs `~/.claude-acct2/` holding identical
  files) is called out as a verification item — it may be a quick ~5k token win or may be an
  artifact of how `/context` reports two config homes.
- **If `llm-guides` is a documentation repo rather than code**, Phase 3 should treat it like
  `research` (large-document context hazards) rather than like `recovery-platform`.
