# AI Workflow Optimization Plan — Full Stack Audit

**Version:** 2.0 (supersedes workflow-plan.md)
**Date:** 2026-06-27
**Sources:** v1.md + v2.md research findings + live audit of recovery-platform, rag-system, cpa-consulting
**Goal:** Maintain current velocity, quality, and Maestro e2e coverage while reducing cost from $200/mo flat to a targeted $80–120/mo blended

---

## Phase 0: Situation Assessment (Completed)

### What the Research Says — v1 vs v2 Contrast

| Dimension             | v1.md (2026 Q1)                                                | v2.md (2026 Q2)                                     | Resolution for Marcus                                                                                                                                                                  |
| --------------------- | -------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Benchmark leader**  | Claude Code Max — SWE-bench Pro 69.2% (28-pt gap over Copilot) | GPT-5.5 — Terminal-Bench 2.1 83.4% (Claude 78.9%)   | Different benchmarks measure different things. SWE-bench Pro (multi-file architectural repair) maps to your work better than Terminal-Bench (code generation speed). Claude Max stays. |
| **Cost floor**        | Subscription arbitrage: $200/mo vs ~$15k raw API over 8 months | Modular stack: $40–70/mo via 80/15/5 tier routing   | Not mutually exclusive. Max is the backbone; OpenRouter handles the 80% cheap tier. Blended target: $80–120/mo.                                                                        |
| **Quality mechanism** | AI.md / CLAUDE.md context cuts 40% token waste                 | Judge-Builder loop catches bugs before human review | Both apply. Context files are already in place across all repos. Judge-Builder loop is the missing unlock.                                                                             |
| **Vendor lock-in**    | Accepts it; subscription arbitrage worth the risk              | OpenRouter zero-lock hedge                          | Low risk given Max subscription model; add OpenRouter as fallback/cheap tier                                                                                                           |
| **Config required**   | Minimal (already on Claude Max)                                | High (Hermes + OpenRouter + Manifest + tier rules)  | Medium path: OpenRouter API key + tier policy in CLAUDE.md. Skip Hermes/Manifest overhead.                                                                                             |

### What the Repo Audits Reveal

**recovery-platform** (highest priority — 5 products, 1,954 files, ~387K lines)

- TypeScript monorepo, Firebase/Firestore, React Native + Next.js + Angular 9
- Has Maestro e2e flows (`e2e-maestro/` + `regroup/mobile/maestro/`) — must preserve
- Has Detox e2e on both mobile products
- CI: **zero automated test pipeline** — only AI code review via `claude-code-review.yml`
- CLAUDE.md exists at root and per-product — solid context foundation
- Multi-agent swarm hooks already wired (`swarm-notify.sh`)
- Most complex codebase; Angular 9 legacy in regroup/web is the most expensive context to load

**rag-system** (second priority — 688 files, 290 TS)

- pnpm monorepo, Fastify + MCP + Next.js + pg-boss + pgvector
- Has real CI: `ci.yml` (unit + typecheck + lint) + `e2e.yml` (Docker-backed Vitest)
- Comprehensive CLAUDE.md and test coverage structure
- Active development (document classification feature, local embeddings)
- Railway deployment target; Sentry monitoring
- The rag-system is the technical foundation for the CPA consulting KB

**cpa-consulting** (strategy workspace — not a software project)

- Pure Markdown, no build, no tests
- Custom Claude Code skills/agents for CPA engagement
- Well-structured CLAUDE.md with epistemic constraints and labeled financial figures
- Aug-1 engagement start; strategy docs are the current output
- AI workflow here is about document quality, not code execution

### Cost Diagnosis

Marcus's current spend pattern:

- Claude Max ($200/mo flat) — primary tool
- Opus 4.8 for planning and architecture
- Sonnet 4.6 for implementation
- No routing discipline — same model for a 5-line boilerplate stub as for a cross-product architectural decision

**Where tokens actually go (estimated):**

- 40–50%: Routine generation (boilerplate, test stubs, doc formatting, collateral drafts) — Tier C material running on Tier A models
- 25–30%: Complex multi-file development in recovery-platform and rag-system — legitimately needs Tier A
- 15–20%: Research and strategy (cpa-consulting, research repo) — 80% of this can be Tier B
- 5–10%: High-stakes judgment (CPA advisory output, legal/financial analysis) — must stay Tier A

**Reduction opportunity:** Moving 40–50% of work to cheaper models (Tier C) saves the equivalent of 2–3 Claude Max subscription months per quarter.

---

## Phase 1: Install the 80/15/5 Tier Policy in Every CLAUDE.md

**Goal:** Enforce model tier routing at the context level. Agents use cheaper models by default and escalate only when the task demands it.

**Timeline:** 1 session per repo. Start with rag-system (already has the best CI baseline), then recovery-platform, then cpa-consulting.

### 1.1 — Add the following block to every CLAUDE.md

Append to the root CLAUDE.md in each repo:

```markdown
## Model Tier Policy (80/15/5 Rule)

### Tier A — Reasoning (5% of tasks) — Claude Opus / Sonnet full context

Use ONLY for:

- Cross-product architectural decisions affecting multiple modules
- Security-critical code (auth, token handling, PII flows)
- Complex bugs requiring deep multi-file causal reasoning
- Final review of client-facing or legally sensitive output
- Anything requiring genuine architectural judgment

### Tier B — Planning (15% of tasks) — Claude Sonnet or OpenRouter Auto

Use for:

- Single-module feature implementation
- Database schema changes and migrations
- Code reviews of non-trivial PRs
- Research synthesis and strategy document drafting
- Debugging with a clear hypothesis

### Tier C — Execution (80% of tasks) — OpenRouter DeepSeek V4 Flash or Haiku

Use for:

- Test stub generation and boilerplate
- Repetitive file patches and linting fixes
- Type annotation passes
- Document reformatting and collateral variations
- Firebase function scaffolding from established patterns
- Content calendar generation, email drafts, standard templates

### Anti-pattern guard

NEVER use Tier A for tasks completable by Tier C.
When in doubt, start at Tier C and escalate if output quality is insufficient.
```

### 1.2 — Per-repo tier calibration

**recovery-platform additions:**

```markdown
## Recovery Platform Tier Calibration

Tier A tasks in this repo:

- Cross-product integration changes (recovery-api ↔ homegroups/regroup)
- Firebase security rules changes (affects all users)
- Stripe webhook and payment logic
- Redux state architecture changes in mobile apps

Tier B tasks:

- Single-product feature implementation
- Firestore query optimization
- React/RN component implementation from defined spec

Tier C tasks:

- Firebase function boilerplate (copy established pattern from existing function)
- Jest test stubs for new service functions
- Maestro flow generation for new screens (copy from e2e-maestro/ patterns)
- Angular/React component props updates
- Package.json script additions
```

**rag-system additions:**

```markdown
## RAG System Tier Calibration

Tier A tasks:

- Retrieval pipeline architecture changes (RRF weights, embedding strategy)
- Auth provider changes (OIDC, JWT, composite)
- pg-boss job handler orchestration
- Cross-package API contract changes (@rag/core types)

Tier B tasks:

- New connector implementation (follow connector/ pattern)
- New MCP tool (follow tools/ pattern)
- Drizzle migration authoring
- Vitest e2e spec authoring

Tier C tasks:

- Zod schema boilerplate for new entities
- Pino log statement additions
- New Fastify route (copy from routes/ pattern)
- Python parser endpoint expansion (copy from parse endpoint pattern)
```

**Verification:** After adding tier policies, run one session and check: did the agent self-select appropriate models, or did it default to Opus for a boilerplate task? If the latter, the tier policy language needs to be stronger.

---

## Phase 2: OpenRouter Integration — The Tier C Infrastructure

**Goal:** Configure OpenRouter as the execution-tier provider. Add to both M4 Pro and M5 Air.

**One-time setup: ~2 hours**

### 2.1 — OpenRouter account and models

1. Create account at `openrouter.ai`, fund with $40 (first month Tier C budget)
2. Generate API key, store in `~/.zshrc` or `~/.config/openrouter`:

```bash
export OPENROUTER_API_KEY="sk-or-..."
# Tier C model (bulk execution)
export TIER_C_MODEL="deepseek/deepseek-v4-flash"
# Tier B model (planning, can also use Claude Sonnet via OpenRouter)
export TIER_B_MODEL="anthropic/claude-3.5-sonnet"
# Tier A stays as Claude Max native — no OpenRouter for this
```

3. Add to `.env.local` in each repo root (gitignored):

```bash
OPENROUTER_API_KEY="sk-or-..."
EXECUTION_MODEL="deepseek/deepseek-v4-flash"
PLANNING_MODEL="anthropic/claude-3.5-sonnet"
```

### 2.2 — When to invoke each channel

| Channel                           | How to invoke                                              | Use for                                                                           |
| --------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Claude Code Max (interactive)     | `claude` CLI — default                                     | Tier A: architectural decisions, complex debugging, code review of critical paths |
| Claude Code Max (autonomous loop) | `/run` skill, subagent swarms                              | Tier A/B: large feature implementation, multi-file refactors                      |
| OpenRouter direct (Tier C)        | `curl openrouter.ai/api/v1/chat/completions` or via Cursor | Test stub gen, boilerplate, doc formatting, collateral                            |
| Cursor Pro ($20/mo, Layer 1)      | IDE inline                                                 | Real-time inline completion during active editing                                 |

**Note:** Do NOT use Hermes Agent CLI or Manifest proxy (too much config overhead for a solo developer). Route directly to OpenRouter API for Tier C tasks.

### 2.3 — Cursor Pro setup (optional but recommended)

Cursor Pro at $20/mo provides zero-latency inline autocomplete from Sonnet — this replaces the friction of switching between Claude Max sessions for routine edits. It pays for itself by reducing the number of Claude Max sessions you open for small tasks.

Configure Cursor to use:

- Inline completion: `claude-sonnet-4.6` (fast, sufficient for autocomplete)
- Composer: `claude-opus-4.8` (for larger tasks opened in Cursor)

**Total monthly addition:** Cursor Pro $20 + OpenRouter ~$30–40 = $50–60/month added
**Claude Max reduction (estimated):** 30–40% fewer heavy sessions = effectively $60–80 recaptured from the $200 budget
**Net new cost:** $0–20/month vs current, with better task routing

---

## Phase 3: The Judge-Builder Loop — Quality Without Extra Human Review Time

**Goal:** Implement the v2 adversarial critique loop in recovery-platform where complex multi-product patterns make unreviewed code riskiest.

### 3.1 — How the Judge-Builder loop works for your workflow

Instead of: Claude writes code → you review it

Use: Claude (Builder) writes code → Cheap model (Judge) critiques → Builder revises → you see final output

The Judge model runs asynchronously and returns a structured critique before you ever open the file.

### 3.2 — Implementation in recovery-platform

Create `.claude/skills/judge-review/SKILL.md` (or add to existing agent config):

```markdown
---
name: judge-review
description: Adversarial code review — used after Builder produces output. Routes to cheap model. Critiques for: logic errors, type safety, Firebase security rule violations, cross-product coupling, missing error handling. Returns structured findings before human review.
---

# Judge Review

After a Builder agent produces code output, invoke this skill to run an adversarial pass.

## Judge prompt template

Review the following code change for the recovery-platform monorepo.

Products in scope: homegroups, regroup, detox-recovery, recovery-api, shared.

Check for:

1. Logic errors or off-by-one issues
2. Missing TypeScript types or unsafe `any` casts
3. Firebase security rule violations (especially cross-product data access)
4. Missing error handling in async functions
5. Stripe webhook signature verification bypass risks
6. Redux state mutations (immutability violations)
7. Missing Zod validation on external inputs
8. Tests that should exist but don't

Return a JSON object: { issues: [{ severity: "critical"|"high"|"medium", location: "file:line", description: string }], verdict: "approve"|"revise" }

## Model to use for Judge pass

Use Tier C model (DeepSeek V4 Flash via OpenRouter) — the judge pass is pattern-matching, not deep reasoning.
Escalate to Tier B only if the change touches auth, payments, or cross-product integrations.
```

### 3.3 — When to trigger Judge pass

- Automatically after any multi-file change in recovery-platform
- Before creating a PR (the existing `claude-code-review.yml` GitHub Action is the right place to add this)
- Not needed for: documentation changes, package.json updates, config file edits

### 3.4 — rag-system Judge calibration

rag-system has better test coverage, so the Judge focus is different:

```
Check for:
1. Missing Zod validation on new API routes
2. Auth middleware not applied to new endpoints
3. Missing pg-boss error handler on new job types
4. Drizzle query using .execute() without await
5. New MCP tools missing input schema validation
6. LocalEmbeddingProvider dimension mismatch risks
```

---

## Phase 4: CI/CD Gap — recovery-platform Needs a Real Test Pipeline

**Gap identified:** recovery-platform's CI is 100% AI code review with zero automated unit/type/build checks. This is the biggest quality risk in the entire workflow.

**Current state:**

- `claude.yml` — AI responds to @claude mentions
- `claude-code-review.yml` — AI reviews every PR

**Missing:**

- `ci.yml` — no typecheck, no lint, no unit tests in CI
- No Maestro run in CI (runs are manual)

### 4.1 — Add a real CI pipeline

Create `.github/workflows/ci.yml` in recovery-platform, modeled on rag-system's `ci.yml`:

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  typecheck-and-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        package: [recovery-api, homegroups/functions, regroup/functions]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: cd ${{ matrix.package }} && npm ci
      - run: cd ${{ matrix.package }} && npx tsc --noEmit
      - run: cd ${{ matrix.package }} && npm test -- --passWithNoTests

  detox-recovery-ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: cd detox-recovery && npm ci
      - run: cd detox-recovery && npx tsc --noEmit
      - run: cd detox-recovery && npm test
```

**Why this matters for cost:** Without automated CI gates, bugs reach main and require expensive multi-file repair sessions. A 15-minute CI run catching a TypeScript error early eliminates a 2-hour debugging session with Claude.

### 4.2 — Maestro smoke in CI (optional, high-ROI)

Maestro Cloud can run on GitHub Actions. Add after the unit CI passes:

```yaml
maestro-smoke:
  needs: typecheck-and-test
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Run Maestro smoke tests
      uses: mobile-dev-inc/action-maestro-cloud@v1
      with:
        api-key: ${{ secrets.MAESTRO_CLOUD_API_KEY }}
        app-file: # path to .apk or .ipa
        flow-file: e2e-maestro/
```

The existing `e2e-maestro/homegroups/login-and-join-group.yaml` and `e2e-maestro/regroup/login-and-view-dashboard.yaml` are ready to run — just need the Maestro Cloud API key and a device target.

---

## Phase 5: Dual-Mac Fleet Optimization

**Current state:** M4 Pro (48GB, primary) + M5 Air (24GB, runner), SSH-linked.

**Optimal mapping:**

| Machine | Role                    | Tasks                                                                     | Model tier          |
| ------- | ----------------------- | ------------------------------------------------------------------------- | ------------------- |
| M4 Pro  | Interactive development | Architecture decisions, code review, CPA advisory, complex debugging      | Tier A (Claude Max) |
| M5 Air  | Autonomous batch runner | Overnight research runs, Maestro test runs, bulk generation, Judge passes | Tier C (OpenRouter) |

**Operational rules:**

1. All Tier C batch work queues to M5 Air. Never run 100+ subagent research runs on M4 Pro while doing interactive work.
2. M5 Air should never hold client data (CPA/§7216 constraint). Route all cpa-consulting work to M4 Pro only.
3. Write checkpoint files to a shared directory (`~/dev/.batch-queue/`) that M4 Pro can read. If M5 Air run fails mid-batch, M4 Pro can inspect progress without re-running from scratch.
4. For overnight research runs, add a `--checkpoint` flag to deep-research invocations where available. The VR&E run that burned 4.78M tokens before failing is the model failure case to prevent.

---

## Phase 6: rag-system — AI Feature Model Routing

**rag-system already has good CI.** The optimization opportunity here is inside the product itself: the embedding and retrieval pipeline uses Google Gemini by default, with OpenAI and HuggingFace as alternatives.

### 6.1 — LocalEmbeddingProvider for development

The in-progress `LocalEmbeddingProvider` (Phase A-1 commit from today) is exactly right. Use it for:

- All development and testing (zero API cost per embed)
- CI e2e runs (already in Docker, should use local embeddings by default)
- Degrade to Gemini only in production

Add to `ci.yml` env:

```yaml
env:
  EMBEDDING_PROVIDER: local
  EMBEDDING_MODEL: Xenova/all-MiniLM-L6-v2 # or whichever the LocalEmbeddingProvider uses
```

### 6.2 — Production model routing in rag-system

For the CPA consulting KB (documented in `docs/CPA-KB-IMPLEMENTATION-SPEC.md`):

- Ingestion embeds: Gemini `text-embedding-004` (768-dim, $0.00002/1K tokens — essentially free)
- Retrieval: keep hybrid RRF (HNSW + BM25) — this is already cost-optimal
- LLM for answer generation: route through OpenRouter; use DeepSeek V4 Flash for first-pass answers, escalate to Sonnet only for complex multi-document synthesis

---

## Phase 7: cpa-consulting — Strategy Document Quality Workflow

**No code changes needed.** The workflow optimization here is entirely about tier routing for document generation.

### 7.1 — Tier assignments for CPA engagement work

| Document type                            | Current (Tier A) | Optimal tier    | Rationale                                                              |
| ---------------------------------------- | ---------------- | --------------- | ---------------------------------------------------------------------- |
| Initial draft of strategy doc            | Opus             | Tier C → Tier B | First draft doesn't need Opus; generate with Flash, refine with Sonnet |
| Client-facing advisory output            | Opus             | Tier A          | Stays. This is the product.                                            |
| Collateral variations (multiple formats) | Opus             | Tier C          | Flash handles format permutations fine                                 |
| CLAUDE.md context updates                | Sonnet           | Tier C          | Mechanical context maintenance                                         |
| Financial figure validation              | Opus             | Tier A          | Must not hallucinate numbers                                           |
| Interview capture → structured notes     | Sonnet           | Tier C          | Transcription/structuring is mechanical                                |
| RAG KB question testing                  | Sonnet           | Tier B          | Quality matters but not Opus-level                                     |

### 7.2 — Prompts directory as Tier routing documentation

The existing `prompts/` directory in cpa-consulting contains regeneration prompts for each document. Add a tier annotation to each:

```markdown
<!-- Tier: B -->
<!-- Model: anthropic/claude-3.5-sonnet via OpenRouter -->
<!-- Escalate to Tier A if: output contains invented financial figures -->
```

This creates an executable record of which model should run which document — critical when the Aug-1 engagement starts and document generation velocity increases.

---

## Phase 8: Weekly Operations Cadence

**15 minutes per week. Non-negotiable.**

### Weekly checklist

```markdown
## AI Workflow Weekly Review — [DATE]

### Cost Check

- [ ] OpenRouter spend this week: $\_\_\_
- [ ] Estimated Claude Max sessions: \_\_\_
- [ ] Any Tier C tasks that ran on Tier A? (List them)
- [ ] Any failed agent runs that burned tokens? (Root cause?)

### Quality Check

- [ ] Did any Judge passes catch issues the Builder missed? (Record patterns)
- [ ] Did any Maestro smoke flows fail? (Ticket created?)
- [ ] rag-system CI: all green? If not, why?
- [ ] recovery-platform (when CI added): all green?

### Context Maintenance

- [ ] CLAUDE.md files up to date in active repos?
- [ ] New product decisions to record in cpa-consulting CLAUDE.md?
- [ ] Any new cross-product patterns in recovery-platform to document?

### Routing Discipline

- [ ] Did the tier policy hold this week?
- [ ] Any new task types that need tier assignment?
```

---

## Summary: Before vs. After

| Dimension                | Current State                            | Target State                                                                                                                                                                                       |
| ------------------------ | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Monthly cost**         | $200 (Claude Max only)                   | $200 (Max) + $20 (Cursor) + $30–40 (OpenRouter) = ~$250 gross; minus ~$60–80 recaptured from routing discipline = **$170–190 net** first month, trending to **$130–150** as Tier C routing matures |
| **Model routing**        | Opus/Sonnet for everything               | 80% Tier C (Flash), 15% Tier B (Sonnet), 5% Tier A (Opus)                                                                                                                                          |
| **Judge-Builder**        | None — human reviews raw output          | Tier C judge pass before human review on recovery-platform                                                                                                                                         |
| **recovery-platform CI** | AI code review only — no automated tests | Unit + typecheck CI on every PR                                                                                                                                                                    |
| **Maestro e2e**          | Manual smoke runs                        | CI-integrated on Maestro Cloud (post unit CI)                                                                                                                                                      |
| **rag-system CI**        | Already solid — no change                | Add LocalEmbeddingProvider in CI env                                                                                                                                                               |
| **cpa-consulting**       | Opus for all docs                        | Tiered: Flash for drafts, Sonnet for planning, Opus for final deliverables                                                                                                                         |
| **Dual-Mac usage**       | Informal                                 | M4 Pro = interactive/judgment; M5 Air = Tier C batch only                                                                                                                                          |
| **Context files**        | CLAUDE.md per repo (good)                | Add tier policy block + task-type tier table to each                                                                                                                                               |
| **Failed runs**          | Unguarded (4.78M burned on failed run)   | Question statement protocol before every deep-research run                                                                                                                                         |

### What does NOT change

- Claude Max stays as the backbone — subscription arbitrage is still real at this usage level
- Maestro e2e flows stay — they're already wired and working
- Existing CLAUDE.md structure — extend, don't replace
- rag-system CI discipline — it's already a reference implementation
- Multi-agent swarm capability in recovery-platform — keep wired, just route swarm agents to appropriate tiers

### The one-line version

> The bottleneck is not the $200/mo subscription. It is routing 80% of your work through Opus/Sonnet when DeepSeek V4 Flash could handle it at a fraction of the cost. Fix the routing, add a Judge pass, harden recovery-platform CI, and wire Maestro to CI. Nothing else changes.

---

## Execution Order (Priority)

1. **This week:** Add tier policy block to all CLAUDE.md files (Phase 1) — no cost, immediate routing discipline
2. **This week:** Create OpenRouter account, fund $40, set env vars (Phase 2) — 1 hour
3. **Next session:** Add `.github/workflows/ci.yml` to recovery-platform (Phase 4.1) — 1 session
4. **Next session:** Add Judge-Builder skill to recovery-platform `.claude/skills/` (Phase 3) — 1 session
5. **When rag-system CI next runs:** Add `EMBEDDING_PROVIDER=local` to e2e CI env (Phase 6.1) — 5 minutes
6. **Before Aug-1 engagement:** Add tier annotations to cpa-consulting `prompts/` directory (Phase 7.2) — 1 session
7. **After above are stable:** Set up Maestro Cloud CI integration (Phase 4.2) — requires Maestro Cloud API key
8. **Ongoing:** Weekly 15-minute review (Phase 8)
