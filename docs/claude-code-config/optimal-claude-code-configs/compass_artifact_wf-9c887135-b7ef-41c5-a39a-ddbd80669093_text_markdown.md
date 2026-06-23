# The Complete Reference Guide to Prebuilt Claude Code Bundles (2025–2026): Survey + Adoption Plan for a Solo TS/React/Node + AI Indie Developer

## TL;DR
- **Start with Superpowers** (Jesse Vincent / `obra`; 224,691 GitHub stars as of June 2026 per Ry Walker Research, up from 57.5K in February — latest release v5.1.0 shipped May 4, 2026) installed from Anthropic's official marketplace. It is the single highest-leverage, lowest-friction bundle for a solo dev: it enforces brainstorm → plan → TDD → subagent review with no team coordination, and per its own repo has more installs on the official marketplace than Playwright. Layer in a lightweight spec tool (**OpenSpec**, ~56K stars) and cherry-pick subagents from **wshobson/agents** for your TS/React/Node stack.
- **Avoid the heavy, enterprise-oriented systems** (BMAD-METHOD's 12–21-agent team simulation, Claude Flow/Ruflo swarms, the full ECC) as a daily driver — they are powerful but over-engineered for a solo indie builder and carry real token and learning-curve costs.
- **For the business side** (marketing, monetization, positioning), the strongest match is **wondelai/skills** (Blue Ocean, STEPPS virality, CRO, $100M Offers as low-token markdown skills), optionally plus **Compound Engineering** (Every/Kieran Klaassen, ~21.7K stars) or **gstack** (Garry Tan) for founder-style "CEO review" planning loops.

## Key Findings

1. **The ecosystem crystallized around Anthropic's plugin system, launched October 9, 2025** (announced via @claudeai's X post; public beta via `/plugin`, shipping around Claude Code 2.0.13). Plugins bundle slash commands, subagents, skills (SKILL.md files), hooks, and MCP server configs as one-command installs via marketplaces — turning a sprawl of git-clone-and-symlink repos into installable, toggleable units.

2. **Three philosophical camps dominate:** (a) *methodology/discipline enforcers* (Superpowers, GSD, Compound Engineering, gstack) that change HOW the agent works; (b) *spec-driven development (SDD) tools* (Spec Kit, OpenSpec, BMAD, cc-sdd, claude-code-spec-workflow) that define WHAT gets built before coding; (c) *catalogs/collections* (wshobson/agents, awesome-claude-code, the official + community marketplaces) of reusable parts. A fourth, smaller camp is *multi-agent orchestration* (Claude Flow/Ruflo, ECC).

3. **For a solo dev, "lightweight + auto-triggering + official-marketplace" beats "comprehensive + enterprise."** Superpowers and OpenSpec win on this axis; BMAD, Claude Flow, and full ECC lose on it.

4. **Bundles can be layered but compound token cost and can conflict.** A sane stack is one methodology layer (Superpowers) + one spec layer (OpenSpec or Spec Kit) + targeted subagents. Stacking multiple opinionated frameworks (Superpowers + gstack + GSD all on) wastes tokens — a single execution-layer skill can consume 10K+ tokens before code is written — and creates confusing overlapping workflows.

5. **Star counts are volatile and disagree across sources; treat all figures as approximate and drifting.** Rapid renames (Claude Flow → Ruflo) and trust incidents (GSD's original repo was reportedly turned into a meme-coin scam and forked to open-gsd) mean you must verify the live repo before installing.

## Details

### The platform layer: Anthropic's plugin system & marketplaces

Anthropic launched Claude Code plugins in public beta on **October 9, 2025** (around Claude Code 2.0.13). A plugin can bundle **slash commands, subagents, skills, hooks, and MCP server configs**, each toggleable to manage context.

Three official-ish marketplaces matter:
- **`claude-plugins-official`** (anthropics/claude-plugins-official) — curated by Anthropic, **auto-registered in every Claude Code install**, auto-update on by default. Install: `/plugin install <name>@claude-plugins-official`. Seeded with ~36 plugins at launch across LSP integrations (typescript-lsp, pyright), internal workflow tools (feature-dev; a pr-review that runs six specialized passes; a security-guidance hook), and external connectors (GitHub, Vercel, Supabase, Figma, Context7, Playwright).
- **`claude-plugins-community`** (anthropics/claude-plugins-community) — third-party plugins that passed automated validation/safety screening, each pinned to a commit SHA. Added manually: `/plugin marketplace add anthropics/claude-plugins-community`.
- The demo marketplace **`anthropics/claude-code`** with example plugins.

⚠️ Anthropic explicitly warns it does not control/verify plugin contents — trust before installing. A reported April 2026 policy change may restrict Pro/Max subscribers' use of some third-party agent frameworks; verify current terms. Note also that there is a *separate, unrelated* enterprise product also called "Anthropic Marketplace" for software procurement (Snowflake, Harvey, Replit as launch partners) — not the Claude Code plugin marketplace.

---

### THE THREE NAMED BUNDLES

#### 1. Superpowers (Jesse Vincent / `obra`)
- **What/who:** "An agentic skills framework & software development methodology that works," by **Jesse Vincent (obra)** — creator of Request Tracker (RT), former Perl 5 pumpking, co-founder of Keyboardio, and builder of K-9 Mail (now Thunderbird for Android) — through his company **Prime Radiant**, founded in early 2026 as the project's organizational home. Repo: `github.com/obra/superpowers`. **The most popular plugin in the ecosystem: 224,691 stars and ~20,000 forks as of June 2026, up from 57.5K in February (Ry Walker Research); latest release v5.1.0 shipped May 4, 2026.** MIT licensed. Per its own repo, it has more installs on Claude Code's official marketplace than Playwright.
- **Philosophy:** Discipline, not intelligence, is the bottleneck in AI coding. It enforces **brainstorming → plan sketch → design doc → implementation plan → subagent-driven implementation → code review**, with hard enforcement of **red/green/refactor TDD**, YAGNI, DRY, and a **4-phase systematic debugging** method (root cause before fixes). Skills auto-trigger via a session-start hook. As Jesse Vincent put it (quoted by Simon Willison): "The core of it is VERY token light. It pulls in one doc of fewer than 2k tokens... The long end to end chat for the planning and implementation process for that todo list app was 100k tokens."
- **Contents:** A composable skills library (14+ skills): brainstorming, writing-plans, test-driven-development, systematic-debugging, subagent-driven-development, code review against plan, skill authoring/testing, a visual companion that mocks up UI, plus audit and level-up skills.
- **Install (Claude Code):**
  ```
  /plugin install superpowers@claude-plugins-official
  ```
  or the original marketplace:
  ```
  /plugin marketplace add obra/superpowers-marketplace
  /plugin install superpowers@superpowers-marketplace
  ```
  Quit/restart Claude. Also supports Codex, Cursor, Gemini CLI, Copilot CLI, OpenCode, Factory Droid, Kimi, Antigravity (install per harness).
- **Strengths:** Auto-triggers (no commands to memorize); presents options/tradeoffs in digestible chunks (much better than vanilla Plan mode's wall-of-text); excellent for greenfield features and complex multi-file work; one-command official install; battle-tested and very actively maintained.
- **Weaknesses/tradeoffs:** **Overkill for trivial tasks.** In a controlled 12-session test by Engr Mejba Ahmed (6 with / 6 without Superpowers, $2 cap, zero human intervention), Superpowers delivered roughly **9% cost reduction and 14% token reduction on average, with savings concentrated on medium and complex tasks — while simple tasks actually used *more* tokens due to planning overhead.** It makes Claude more *disciplined*, not more *knowledgeable* — you still need domain context in CLAUDE.md. Learning curve from 14+ skills and a meta-vocabulary; auto-triggering can surprise; if a collaborator is on vanilla Claude Code, the artifacts (worktrees, plan files) confuse rather than help.
- **Reception:** Rave reviews. Simon Willison (creator of Datasette), Oct 10, 2025: "Jesse is one of the most creative users of coding agents (Claude Code in particular) that I know... Jesse is way ahead of the curve, so it's absolutely worth spending some time exploring what he's shared so far." **Officially accepted into Anthropic's marketplace on January 15, 2026.** Widely considered the default starting point for solo/small-team greenfield work.

#### 2. ECC — "Everything Claude Code" (Affaan Mustafa / `affaan-m`)
- **What/who:** **"Everything Claude Code"** (the acronym the user meant), by **Affaan Mustafa**, born from winning an Anthropic × Forum Ventures hackathon in NYC (Sept 2025, building zenith.chat in 8 hours for $15K in API credits). Repo: `github.com/affaan-m/ECC` (also `everything-claude-code`). Self-described "agent harness performance optimization system." ~82K–100K stars (early–mid 2026), 10K+ forks. MIT. v2.0.0 reframes it as a cross-harness "operating system."
- **Philosophy:** Battle-tested, production-grade configs across many harnesses (Claude Code, Codex, Cursor, OpenCode, Gemini, Zed, Copilot) with security-first and research-first development, memory persistence, and continuous learning.
- **Contents (large):** ~261 skills, 64 agents, 84 commands in the OSS layer (counts grew over versions; earlier ~28 agents / 119 skills / 60 commands); 102 security rules scanning every session; rules, hooks, MCP configs (GitHub, Context7, Exa, Memory, Playwright, Sequential Thinking, optionally Supabase); selective install profiles (core/developer/security/full) and per-language rule packs (TS/JS, Python, Go). NanoClaw orchestration layer. **ECC Pro** is a paid hosted GitHub App ($19/seat/mo) for private repos.
- **Install:** `/plugin install ecc@ecc` or the interactive "configure ecc" skill; the selective-install builder generates a copy-paste command.
- **Strengths:** Huge breadth; strong security tooling; cross-harness parity; selective install so a TS shop doesn't inherit Python overhead; a well-regarded code-reviewer agent (filters for confidence >80%).
- **Weaknesses:** **Over-engineering is the loudest community criticism** — "most people just need a good CLAUDE.md, not an entire ecosystem." The plugin system doesn't deliver rules (only agents/skills/hooks/commands), causing setup friction; documented duplicate-hook detection errors (Issues #29/#52/#103) with Claude Code v2.1+. Divisive on r/ClaudeCode.
- ⚠️ Beware impostor/scam repos like "ECC-Everything-Claude-Code-2026" with .rar downloads and "activation keys" — malware-pattern fakes, not the real project. Also distinct: `zhongkai/ECC` ("Everything Claude Code Extension," a config generator).

#### 3. GSD — "Get Shit Done" (TÂCHES / Lex Christopherson / "glittercowboy")
- **What/who:** A lightweight **meta-prompting & context-engineering** system by **TÂCHES (Lex Christopherson, aka glittercowboy)**. Launched Dec 2025; ~23K–59K stars across 2026 sources, 138 contributors, 2,100+ commits, 57 releases.
- **Philosophy:** Solves **"context rot"** — quality degradation as a single session fills its window. GSD breaks work into **atomic plans run in fresh subagent contexts** (each ~50% of a clean 200K window), grouped into dependency-based **"waves"** (parallel where independent). The main orchestrator stays at 30–40% utilization. Spec-driven: state externalized to Markdown. Phased loop: **Initialize → Discuss → Plan → Execute → Verify → Complete**, plus `/gsd:quick` for small tasks and goal-backward verification.
- **Contents:** ~29 skills (slash commands), 12 custom agents (research/planning/execution/verification), 2 hooks (status bar, update checker), a Node.js CLI helper (`gsd-tools.cjs`), ~50 Markdown files. No proprietary runtime. Per-agent model selection for cost control.
- **Install:** `npx get-shit-done-cc@latest` (interactive installer; supports 14 runtimes), then `/gsd:help`. Recommends skip-permissions or granular `.claude/settings.json`.
- **Strengths:** Sits between vibe-coding chaos and heavy enterprise frameworks — explicitly pitched at solo devs/founders; "the complexity is in the system, not your workflow"; strong for medium-to-large multi-feature projects prone to context rot.
- **Weaknesses:** Overkill for tiny tasks (use `/gsd:quick`); does little standalone "shipping" without an execution layer — it's a context stabilizer; asks many questions.
- ⚠️ **CRITICAL trust caveat:** The **original GSD repo was reportedly turned into a crypto/meme-coin scam** and the original author is no longer trusted. Development moved to **open-gsd governance** — actively maintained forks at `github.com/open-gsd/get-shit-done-redux` and `opengsd.net`; one source cited a move to `github.com/gsd-build/get-shit-done` (Feb 2026). **Verify the live, community-trusted repo before installing.**

---

### SPEC-DRIVEN DEVELOPMENT (SDD) TOOLS

#### Spec Kit (GitHub / Microsoft)
Official GitHub open-source toolkit. Repo: `github.com/github/spec-kit` (~111K stars per one mid-2026 source). Methodology: **Spec → Plan → Tasks → Implement**, with a `constitution.md` of non-negotiable principles and a `/speckit.analyze` cross-artifact consistency check. Installs the **Specify CLI** via `uv`/`uvx`: `uvx --from git+https://github.com/github/spec-kit.git specify init --integration claude`. Works with 30+ agents. Strength: rigorous, durable, human-readable artifacts; great greenfield and legacy-modernization. Weakness: heavyweight, Python/uv setup, "rigid phase gates," can feel like Waterfall for small tasks. Best combined with Superpowers (Spec Kit = WHAT, Superpowers = HOW).

#### OpenSpec (Fission-AI)
Repo: `github.com/Fission-AI/OpenSpec` (**~56K stars, ~3.9K forks**, mid-2026). **Lightweight, brownfield-first** SDD that "adds a lightweight spec layer so you agree on what to build before any code is written" — "fluid not rigid — no phase gates," with versioned "living specs" and change markers (ADDED/MODIFIED/REMOVED). Workflow: **Proposal → Implementation → Archive**. Install: `npm install -g @fission-ai/openspec@latest` then `openspec init` (supports 25+ tools, no API keys, no MCP). ~250 lines of spec vs ~800 for Spec Kit. Positions itself vs Spec Kit ("thorough but heavyweight") and Kiro ("IDE lock-in"). **Best lightweight spec layer for a solo dev on existing projects.**

#### BMAD-METHOD (BMad Code, LLC)
"Breakthrough Method of Agile AI-Driven Development." Repo: `github.com/bmad-code-org/BMAD-METHOD` (~43K–49K stars). Simulates a full **agile team of 12–21 specialized agents** (Analyst, PM, Architect, Scrum Master, PO, Dev, QA/Test Architect, UX). V6 adds scale-adaptive intelligence (3 tracks: Quick Flow / BMad Method / Enterprise), web bundles for ChatGPT/Gemini planning, party mode, BMad Builder. Install: `npx bmad-method install` (v4 stable) or `npx bmad-method@alpha install` (v6). Strength: comprehensive lifecycle, domain expansion packs (game dev, creative). **Weakness for solo: heavyweight "enterprise theater" / "sledgehammer to crack a nut" for small projects.** Free/MIT.

#### Others (briefly)
- **cc-sdd** (`gotalab/cc-sdd`): minimal "Kiro-style" SDD harness, 17 Agent Skills, `npx cc-sdd@latest --claude-skills`; flow kiro-discovery → spec-init → requirements → design → tasks → impl. 8 agents, 13 languages.
- **claude-code-spec-workflow** (`Pimzino/claude-code-spec-workflow`, ~3.6K stars): Requirements → Design → Tasks → Implementation + bug-fix workflow; `npx @pimzino/claude-code-spec-workflow`; real-time dashboard; companion `spec-workflow-mcp`. Author advocates Opus for the spec, Sonnet for implementation, in separate sessions.
- **SuperClaude Framework** (`SuperClaude-Org/SuperClaude_Framework`): a behavioral-config framework (not yet a native plugin — a TypeScript plugin is planned for v5.0). Python/pipx/npm install (`pipx install SuperClaude && SuperClaude install`); 30 `/sc:` commands (brainstorm, analyze, implement, design, workflow, test, research), ~20 agents, cognitive personas, MCP integration (Context7, Serena, Tavily). Wave→Checkpoint→Wave pattern; confidence gating. Good for those who want a coherent command vocabulary without the official plugin system.

---

### MULTI-AGENT ORCHESTRATION

#### Claude Flow → Ruflo (Reuven Cohen / `ruvnet`)
Repo renamed `ruvnet/claude-flow` → `ruvnet/ruflo` with v3.5 (Feb 27, 2026), reportedly for trademark reasons; **the npm package & CLI are still `claude-flow`**. ~31K–60K stars across sources. An "agent meta-harness": orchestrates 100+ specialized agents in swarms (mesh/hierarchical/ring/star topologies; Raft/BFT/Gossip/CRDT consensus), hive-mind queens/workers, self-learning memory (AgentDB/ReasoningBank), 300+ MCP tools, SPARC TDD methodology. v3.5 moved core to Rust/WASM. Install: `npx ruflo@latest init` or `claude mcp add ruflo -- npx ruflo@latest mcp start`. **Strength:** the most mature parallel multi-agent option (claims 84.8% SWE-bench, self-reported). **Weakness:** enterprise-grade complexity, massive overkill for a solo dev fixing a bug; most performance claims are self-reported. MIT.

---

### CATALOGS & COLLECTIONS

- **wshobson/agents** (~36.6K stars): multi-harness marketplace, **192 agents, 156 skills, 102 commands, 84 plugins** from one Markdown source. Includes TS/React/Node-relevant agents: backend-architect, frontend-developer, mobile-developer (React Native/Flutter), graphql-architect, typescript-pro, python-pro, react specialists, security-auditor, test-automator, ui-visual-validator. Install marketplace: `/plugin marketplace add wshobson/agents` then `/plugin install <collection>` (e.g., claude-code-essentials, full-stack-development). Companion **wshobson/commands** (52+ slash commands/workflows). **Excellent pick-and-choose source for a TS stack.**
- **awesome-claude-code** (`hesreallyhim/awesome-claude-code`, ~47K stars): the canonical human-curated directory of skills/hooks/commands/orchestrators/plugins (~203 resources, updated frequently). Best discovery list — treat as a discovery list, not an install list.
- Other subagent collections: `lst97/claude-code-sub-agents` (full-stack, MCP-configured), `davepoon/claude-code-subagents-collection` (36), `VoltAgent/awesome-claude-code-subagents`, `0xfurai`, `iannuttall/claude-agents`, `vijaythecoder/awesome-claude-agents`. Quality varies; prefer recently maintained ones.

---

### BUSINESS / MARKETING / MONETIZATION BUNDLES (weighted to "sells products themselves")

- **wondelai/skills** (`github.com/wondelai/skills`, ~1.4K stars, MIT): **the strongest single match for the business side.** ~50 markdown skills from canonical business books, installable as themed bundles: **marketing-cro** (CRO Methodology, StoryBrand, Contagious/STEPPS), **strategy-growth** (Crossing the Chasm, Blue Ocean / Four Actions ERRC, Traction/EOS, Obviously Awesome positioning), **sales-influence** (Cialdini, $100M Offers, Made to Stick), **product-strategy** (JTBD, The Mom Test), plus standalone monetizing-innovation, lean-analytics, cold-start-problem. Install: `/plugin marketplace add wondelai/skills` then `/plugin install marketing-cro@wondelai-skills` (etc.), or `npx skills add wondelai/skills/blue-ocean-strategy`. Plain markdown, low token cost, includes ~80 copy-paste prompts.
- **Compound Engineering** (`EveryInc/compound-engineering-plugin`, ~21.7K stars / ~1.6K forks): by **Kieran Klaassen & Dan Shipper (Every)**, born from building Cora (an AI chief-of-staff for email). Philosophy: *each unit of work makes the next easier* — loop **Plan → Work → Assess → Compound**, ~80% planning/review + 20% execution, learnings captured into CLAUDE.md (pruned via `/ce-compound-refresh`). 40+ agents (tiered persona code reviewers), 30+ commands (`/lfg`, `/ce-setup`), 35+ skills. Install: `/plugin marketplace add EveryInc/compound-engineering-plugin` → `/plugin install compound-engineering` → `/ce-setup`. Very actively developed (v3.12.0, June 2026). Good for a founder who wants a planning-heavy, learning-accumulating loop.
- **gstack** (`github.com/garrytan/gstack`, ~40K–71K stars reported — volatile): by **Garry Tan (YC CEO)**. "Thin harness, fat skills" — 23 opinionated role skills (CEO, Designer, Eng Manager, Release Manager, QA…) and commands like `/office-hours` (pressure-test like a YC partner), `/plan-ceo-review`, `/plan-eng-review`, `/autoplan`, `/qa` (Playwright), `/ship`, `/retro`. Install: `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`. **Most founder-oriented coding framework** (forces "what problem does this solve?" before code). Caveat: token-heavy persona layer (10K+ tokens before code), can feel bloated; it's single-instance role-switching, not true multi-agent. (Note: gstack is *not* the same as Superpowers/"ai-superpowers" — different author entirely.)
- **build-saas** (`saasroo/build-saas`, very new/small; Saasify theme by chaoming): scaffolds a full SaaS (Hugo + Saasify marketing site; React 19 + Firebase + Stripe via Fireact app). More "ship the SaaS plumbing" than growth strategy.
- ⚠️ No confirmed first-party Anthropic marketing/monetization bundle exists as of mid-2026; the richest business content is community-sourced (wondelai). Also note: Claude Code plugins themselves have **no built-in monetization mechanism** (all MIT/free) — revenue is external.

---

### Comparison table (broad survey)

| Bundle | Maintainer | Type | Approx. stars (drift!) | Install | Solo-dev fit | Token/learning cost |
|---|---|---|---|---|---|---|
| **Superpowers** | Jesse Vincent (obra) / Prime Radiant | Methodology (TDD/plan/debug) | 224K (Jun '26) | `/plugin install superpowers@claude-plugins-official` | ★★★★★ | Low core; medium discipline curve |
| **OpenSpec** | Fission-AI | Lightweight SDD | ~56K | `npm i -g @fission-ai/openspec@latest` | ★★★★★ | Low |
| **Spec Kit** | GitHub/Microsoft | SDD (heavier) | ~111K | `uvx ... specify init` | ★★★☆☆ | Medium; Python/uv |
| **wshobson/agents** | Will Hobson | Catalog (agents/cmds) | ~36.6K | `/plugin marketplace add wshobson/agents` | ★★★★☆ (cherry-pick) | Low if selective |
| **wondelai/skills** | wondelai | Business/marketing skills | ~1.4K | `/plugin marketplace add wondelai/skills` | ★★★★★ (biz) | Low |
| **Compound Engineering** | Every (Klaassen/Shipper) | Methodology (compounding) | ~21.7K | `/plugin marketplace add EveryInc/compound-engineering-plugin` | ★★★★☆ | Medium |
| **gstack** | Garry Tan (YC) | Methodology (founder roles) | ~40–71K | git clone + `./setup` | ★★★★☆ | High (token-heavy) |
| **GSD** | TÂCHES (glittercowboy) | Context-rot/SDD | ~23–59K | `npx get-shit-done-cc@latest` | ★★★☆☆ (use verified fork) | Medium |
| **BMAD-METHOD** | BMad Code | SDD agent team | ~43–49K | `npx bmad-method install` | ★★☆☆☆ | High |
| **ECC** | Affaan Mustafa | Mega config/harness | ~82–100K | `/plugin install ecc@ecc` | ★★☆☆☆ | High |
| **Claude Flow/Ruflo** | Reuven Cohen (ruvnet) | Multi-agent swarm | ~31–60K | `npx ruflo@latest init` | ★☆☆☆☆ | Very high |
| **SuperClaude** | SuperClaude-Org | Behavioral config | — | `pipx install SuperClaude` | ★★★☆☆ | Medium |

---

## Recommendations (the deeper evaluation)

### Your context recap
Solo indie dev; TS + React + Node primary; some Python; React Native mobile; building LLM/AI apps; sells your own indie SaaS; already on Claude Code; wants productivity, code quality, planning, research, PM, docs, and monetization.

### Recommended starter stack (adopt in this order)

**Stage 1 — Foundation (week 1). Trigger to begin: vanilla Claude Code "jumps to code" too fast for you.**
1. **Superpowers** — `/plugin install superpowers@claude-plugins-official`. Your methodology backbone for code quality, planning, TDD, and debugging. Run it on a *real* feature (not a toy) for 24 hours to learn the cadence.
2. **A solid CLAUDE.md** — Superpowers makes Claude disciplined, not knowledgeable. Put your stack conventions here (TS strictness, React patterns, Node/test runner, RN specifics, your AI-app architecture, package manager). Highest-ROI move and it's free.
3. **Official LSP + service plugins** from `claude-plugins-official`: `typescript-lsp` (biggest code-quality win for your stack), `pyright` for Python, plus **GitHub**, **Context7** (live version-specific docs — critical for fast-moving AI SDKs), **Playwright**, and **Supabase/Vercel** connectors as relevant.

**Stage 2 — Planning & specs (week 2–3). Trigger: you're losing context across sessions or shipping the wrong thing.**
4. **OpenSpec** (`npm i -g @fission-ai/openspec@latest`, `openspec init`) — a lightweight, brownfield-friendly spec layer that persists intent across sessions. Prefer this over Spec Kit for a solo dev (less ceremony, no Python/uv). Use Spec Kit instead only if you want GitHub's heavier, constitution-driven artifacts.
5. Optionally adopt the **spec-then-implement, two-session pattern**: a high-reasoning model for the spec/plan, a fast model for execution in a fresh session.

**Stage 3 — Targeted parts (ongoing). Trigger: a recurring task type is underserved.**
6. **Cherry-pick from wshobson/agents** — install only the agents you use (frontend-developer, backend-architect, mobile-developer for RN, test-automator, security-auditor, typescript-pro). Don't install the whole catalog.

**Stage 4 — Business/monetization (when you're shipping). Trigger: product works, now you need users/revenue.**
7. **wondelai/skills** business bundles (marketing-cro, strategy-growth, sales-influence) for positioning, pricing, launch copy, and growth — markdown-only, low token cost. Optionally **Compound Engineering** or **gstack** if you want a founder-style "CEO/eng review" planning loop on top.

### What NOT to adopt (for your context)
- **BMAD-METHOD, Claude Flow/Ruflo, full ECC** — powerful but enterprise-scale; the agent-team simulation and swarm orchestration are overkill for one person and burn tokens/learning time. Borrow patterns, don't run them daily.
- **Don't stack multiple methodology frameworks** (Superpowers + gstack + GSD simultaneously). Pick one execution methodology. Stacking causes overlapping workflows and 10K+ token preambles before code.
- **GSD** — good concept (context rot is real) but the trust/ownership saga means only adopt a verified open-gsd fork, and even then OpenSpec + Superpowers already cover most of its value for you.

### How these interact with your existing setup
- **CLAUDE.md** stays the source of project truth; methodology plugins read it at session start. Keep it lean (Compound Engineering's `/ce-compound-refresh` shows how to prune stale entries).
- **Subagents/hooks:** Superpowers and others install their own; watch for **duplicate-hook detection errors** (a documented ECC issue with CC v2.1+) if you also hand-roll hooks.
- **MCP servers:** GitHub, Context7, Playwright pair well with all these bundles. Context7 is especially valuable for your AI-app work (live SDK docs). Don't over-install MCP servers — each adds context overhead.
- **Token/context concerns:** the dominant tradeoff. Simple tasks can cost *more* under heavy methodology; use lightweight/quick modes for small work and reserve the full pipeline for complex features.

## Caveats
- **Star counts and contents drift fast and disagree across sources.** All figures here are approximate and dated where possible; verify on the live repo before relying on them.
- **Verify the live repo before installing**, especially for **GSD** (original repo reportedly became a meme-coin scam → use open-gsd forks) and **Claude Flow/Ruflo** (renamed). Watch for impostor "ECC" repos with .rar / "activation key" downloads — those are malware patterns.
- **Anthropic does not vet plugin contents**; treat third-party plugins like any dependency (review source, mind permissions). A reported April 2026 policy change may restrict Pro/Max use of some third-party frameworks — confirm current terms.
- **Performance/productivity claims are often self-reported or vendor marketing** (e.g., Ruflo's SWE-bench numbers, generic "30% productivity" figures). The one controlled benchmark cited (12 sessions, Superpowers) showed nuanced, task-dependent results — ~9% cost / ~14% token savings concentrated on medium/complex tasks, with simple tasks costing more — not blanket gains.
- This is a fast-moving space (late 2025–mid 2026); projects rename, get abandoned, or change install methods quickly. Re-check before committing a workflow.