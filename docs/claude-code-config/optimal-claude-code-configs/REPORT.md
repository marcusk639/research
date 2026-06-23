# Optimal Claude Code Configs

> Status: draft · Started: 2026-06-23 · Scope: solo indie dev, **cpa-consulting venture prioritized**

## Research Question

What is the optimal Claude Code configuration — `CLAUDE.md`, skills, subagents, hooks,
MCP servers, `settings.json`, model/effort policy, and prebuilt bundles — for Marcus
(a solo indie dev), tuned specifically to the **cpa-consulting venture** and its
associated repos? Highest priority is the `rag-system` production monorepo (TS-primary
pnpm workspace + Python parser sidecar, Drizzle/pgvector, pg-boss, MCP server, Next.js
web, Railway), followed by the `cpa-consulting` strategy workspace; `cpa-backend`
(legacy) and `cpa-knowledge-base` (deprecated) are secondary.

### Repo landscape (grounding)

| Repo                 | Role                                            | Stack                                                                                                                              | Existing Claude config                                                                                      |
| -------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `rag-system`         | **Priority** — production product               | pnpm monorepo, Node 22, TS-primary, Python parser sidecar, Drizzle/pgvector, pg-boss, MCP, Next.js web, Railway, vitest + e2e/eval | Minimal: `settings.local.json` only; 107-line `CLAUDE.md`; no committed skills/agents/hooks/`settings.json` |
| `cpa-consulting`     | Strategy/planning workspace (Markdown, no code) | Markdown only                                                                                                                      | Rich: `settings.json` (constraint-guard hook), `constraint-reviewer` agent (Haiku), 8 domain skills         |
| `cpa-backend`        | Legacy backend                                  | Express/Mongo/Redis/SQS/Textract/OpenAI                                                                                            | None                                                                                                        |
| `cpa-knowledge-base` | Deprecated UI prototype                         | Next.js 15 + Tailwind + shadcn                                                                                                     | Minimal                                                                                                     |

---

## Key Findings

1. **The priority repo is the least configured.** `rag-system` is the production product
   and the venture's center of gravity, yet it has no committed `settings.json`, no
   project skills, no subagents, and no project hooks — only a personal
   `settings.local.json` and a solid 107-line `CLAUDE.md`. The single highest-leverage
   move in this whole subject is to bring `rag-system`'s committed config up to the
   standard `cpa-consulting` already demonstrates. ([rag-system/.claude](/Users/marcus/dev/rag-system/.claude); [cpa-consulting/.claude/settings.json](/Users/marcus/dev/cpa-consulting/.claude/settings.json))

2. **`rag-system` already has the #1 reliability lever built in: verifiable checks.**
   `pnpm typecheck`, `pnpm lint`, `pnpm test` (vitest), `pnpm e2e`, and a retrieval
   `pnpm eval` harness all exist ([rag-system/CLAUDE.md:17-38](/Users/marcus/dev/rag-system/CLAUDE.md)).
   The Solo Guide's official #1 reliability principle is "give Claude a check it can run …
   the difference between a session you watch and one you walk away from" [SoloGuide §5].
   The gap is not the checks — it's wiring them into **PostToolUse/Stop hooks** so they
   run deterministically instead of when Claude remembers to.

3. **Marcus's existing config patterns are already best-practice and should be
   replicated, not reinvented.** The `cpa-consulting` workspace shows: a domain-scoped
   constraint-guard PreToolUse hook, a cheap read-only `Haiku` reviewer subagent, and
   tightly-scoped skills with explicit refusal boundaries (e.g. `workpaper-generator`
   refuses regulated audit/tax workpapers). These mirror the artifacts' guidance on
   hooks-as-determinism, role-based tool/model presets, and pairing prohibitions with
   directions [SoloGuide §2, §1]. The job is to port these patterns into `rag-system`.

4. **Context management is the master skill, and the venture's repos are big.**
   `rag-system` is a 7-package + 4-app monorepo; the dominant failure mode is context
   bloat, not model choice [SoloGuide §0, §8]. The mitigations that matter most here:
   a lean `CLAUDE.md` (already good — keep it ≤150 lines), **child-directory `CLAUDE.md`
   files per app/package** (the official pattern for monorepos), disciplined MCP server
   count, and Serena (already installed) for symbol-level reads instead of whole-file dumps.

5. **MCP discipline is a live issue.** `rag-system` already leans on Serena, Context7,
   Railway, and claude-mem MCP servers ([rag-system/.claude/settings.local.json](/Users/marcus/dev/rag-system/.claude/settings.local.json)).
   Each connected server burns ~2–5K tokens of schema before any prompt, and a benchmarked
   GitHub query cost ~32× more through MCP than the `gh` CLI [SoloGuide §3]. The advice:
   keep the active set to ~3–4 high-value servers (Serena and Context7 clearly earn their
   place here; prefer the `gh`/`railway` CLIs over MCP equivalents where they exist).
   `rag-system` is _also itself_ an MCP server (`apps/mcp`) — distinct concern, don't conflate.

6. **For prebuilt bundles, the artifacts' verdict maps cleanly onto this venture:**
   **Superpowers** (methodology/TDD discipline) for `rag-system` code work, optionally
   **OpenSpec** as a lightweight brownfield spec layer for multi-session features, and
   **cherry-picked** TS/Node subagents from `wshobson/agents`. Avoid the heavy
   enterprise systems (BMAD, Claude Flow/Ruflo, full ECC as a daily driver) [Bundles
   §Recommendations]. Note: Marcus's global config already shows ECC/GSD lineage (GSD
   PreToolUse guards in `~/.claude/hooks/`, `ECC_GATEGUARD=off`) — a reason to consolidate
   on one methodology rather than stack three.

7. **The product has a compliance-and-secrets profile that should drive deny-hooks.**
   `rag-system` ingests client documents (SharePoint/Gmail/Outlook) and `cpa-consulting`
   holds gitignored firm transcripts under `docs/firm/`. Both touch IRC §7216 / Circular
   230 territory ([cpa-consulting/CLAUDE.md:54-64](/Users/marcus/dev/cpa-consulting/CLAUDE.md)).
   This argues for PreToolUse **deny** hooks (which hold even under YOLO mode) on `.env`,
   secrets, and `firm/` paths, plus `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` in any CI
   [SoloGuide §5, §8]. The `.env` and lockfile blocks already exist globally — extend the
   pattern to client-data paths.

---

## Details

### 0. Layered config model (where each setting belongs)

The artifacts describe a four-layer harness; mapped onto this venture:

- **`~/.claude/` (global/user)** — personal defaults that apply everywhere: default model,
  the always-on safety hooks (`.env`/lockfile blocks — already present), `defaultMode`,
  and stable MCP servers (Serena, Context7). Keep the global `CLAUDE.md` <15 lines
  [SoloGuide §1]. Marcus's global already sets `defaultMode: acceptEdits`,
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, and experimental agent teams on
  ([~/.claude/settings.json](/Users/marcus/.claude/settings.json)).
- **`<repo>/.claude/settings.json` (project, committed)** — shared, repo-specific
  permissions and hooks. **This is the file `rag-system` is missing.**
- **`<repo>/.claude/settings.local.json` (project, gitignored)** — personal per-repo
  permission grants and `additionalDirectories`. `rag-system` already uses this well.
- **Precedence (high→low):** managed → CLI args → `settings.local.json` → `settings.json`
  → `~/.claude/settings.json`; array keys like `permissions.allow` _concatenate_ across
  scopes, scalars override [SoloGuide §8].

### 1. `rag-system` — the priority configuration

**1a. `CLAUDE.md` (already strong; keep lean).** The existing 107-line file is high-signal:
mental model, exact commands, architectural ground rules, a "where to find things" table,
and a "things that will trip you up" section ([rag-system/CLAUDE.md](/Users/marcus/dev/rag-system/CLAUDE.md)).
This already satisfies the official include/exclude test [SoloGuide §1]. Recommendation:
**hold the line on length** (Claude starts ignoring rules past ~200 lines), and push
package-specific detail _down_ into child `CLAUDE.md` files rather than growing the root.

**1b. Child-directory `CLAUDE.md` (the monorepo win).** The official pattern: child
`CLAUDE.md` files load on demand when Claude reads a file in that directory [SoloGuide §1].
Highest-value placements here:

- `packages/db/CLAUDE.md` — Drizzle migration discipline, the "rag-worker is the single
  migration owner / deploy worker first" rule, pgvector dimension lock (768/Gemini).
- `packages/rag/CLAUDE.md` — embedding immutability, chunking/RRF retrieval conventions.
- `apps/mcp/CLAUDE.md` — MCP tool contract (must reuse `@rag/services`, never duplicate ask/search).
- `services/parser-py/CLAUDE.md` — the one place Python is allowed; parser-secret auth, separate process.
  These keep the root lean while giving Claude exactly-in-time context (progressive disclosure).

**1c. `settings.json` (commit one).** Today permissions live only in `settings.local.json`.
A committed project `settings.json` should encode the _team_ contract (even for a solo dev,
"team" = future-you + CI):

- `permissions.allow` for the safe inner-loop commands: `pnpm typecheck`, `pnpm lint`,
  `pnpm test`, `pnpm build`, `pnpm db:generate`, `docker compose … logs`.
- `permissions.ask` for `git push`, `pnpm db:migrate` (schema-changing), `docker compose … down`.
- `permissions.deny` for `Read(./.env)`, `Read(./.env.*)`, `Read(**/secrets/**)`, and any
  client-data path. Deny wins first-match and holds under bypass mode [SoloGuide §5, §8].
- Permission syntax is space-delimited, not colon (`Bash(pnpm test *)`), and glob spacing
  matters [SoloGuide §8].

**1d. Hooks (the biggest untapped lever).** `rag-system` inherits the global Prettier-on-edit
and `.env`/lockfile blocks ([rag-system/CLAUDE.md:103-107](/Users/marcus/dev/rag-system/CLAUDE.md)),
but has no _project_ hooks. Add:

- **PostToolUse (Write|Edit on `*.ts`)** → `pnpm -w typecheck` (or a package-scoped, faster
  `tsc --noEmit`) and `eslint --fix` on the touched file, feeding errors back to Claude.
  Keep each hook <200ms or mark `async` [SoloGuide §2].
- **Stop hook** → gate turn-end on `pnpm test` (or the relevant package's tests) passing —
  the progressive escalation from in-prompt → `/goal` → Stop hook → verification subagent
  is the official reliability ladder [SoloGuide §5].
- **PreToolUse deny** → block writes to `packages/db/drizzle/` migrations without
  confirmation (migrations auto-run on Railway deploy — a wrong one is hard to reverse).

**1e. Subagents (port the `cpa-consulting` pattern).** Recommended trio for `rag-system`,
following the role→tools→model presets [SoloGuide §2]:

- **reviewer** — `Read, Grep, Glob`, model Sonnet (or Haiku for cheap passes); fresh-context
  review of diffs, constrained to "correctness/requirements gaps only" to avoid nitpick floods.
- **retrieval-eval-runner** — runs `pnpm eval` and interprets the retrieval-quality delta
  (this repo's domain-specific verification surface).
- **planner** — read-only + plan, Opus or `opusplan`, for multi-file work across packages.
  Invoke explicitly to guarantee use. Serena gives all of them symbol-level reads instead
  of whole-file dumps (context savings).

**1f. MCP servers.** Keep the current high-value set: **Serena** (symbolic code nav — strongly
justified in a monorepo), **Context7** (live SDK docs — critical for fast-moving AI/Drizzle/MCP
APIs [SoloGuide §3, Bundles §How-they-interact]), **Railway** (deploy/logs — but prefer the
`railway` CLI for token efficiency where possible). `claude-mem` is in use for cross-session
memory; keep it if it earns its context cost, otherwise lean on `.remember/` + CLAUDE.md.
Don't add GitHub MCP — install/use the `gh` CLI instead (~32× cheaper) [SoloGuide §3].

**1g. Models & effort.** Daily driver **Sonnet 4.6**; `opusplan` for planning-heavy multi-package
refactors; **Haiku 4.5** for grep-heavy subagents and mechanical edits; reserve **Opus 4.8**
for genuinely hard, unfamiliar-code work. Start **effort at `xhigh`** for coding per official
guidance, step down to save cost [SoloGuide §8]. (The existing `constraint-reviewer` already
models cost-routing with `claude-haiku-4-5`.) **Verify model IDs/effort levels against current
docs before encoding** — this is the most drift-prone area [SoloGuide Caveats].

**1h. Bundles.** Adopt **Superpowers** as the methodology backbone (brainstorm → plan → TDD →
subagent review) — its hard TDD gate fits a repo that already has vitest + e2e + eval
[Bundles §Superpowers]. Optionally **OpenSpec** for brownfield specs that survive across
sessions on multi-package features [Bundles §OpenSpec]. Cherry-pick `typescript-pro`,
`backend-architect`, `test-automator` from `wshobson/agents` only if the built-ins fall short
[Bundles §Catalogs]. **Do not** stack Superpowers + GSD + ECC simultaneously — consolidate
(Marcus's global still carries GSD guard hooks; decide whether GSD stays or goes).

**1i. Worktrees & context hygiene.** `.worktrees/` already exists. Use it for 2–3 parallel
sessions scoped _by package/module_ (e.g. connectors vs. retrieval), not by task; add
`.worktrees/` to `.gitignore`; `/clear` between unrelated tasks [SoloGuide §5, §8].

### 2. `cpa-consulting` — already exemplary; refine, don't rebuild

This workspace is the model the other repos should imitate:

- **Constraint-guard PreToolUse hook** fires on edits to `strategy-eval/` docs and reminds
  about labeled figures, the 38% capture ceiling, and §7216 ([cpa-consulting/.claude/settings.json](/Users/marcus/dev/cpa-consulting/.claude/settings.json)).
- **`constraint-reviewer` subagent** (read-only, Haiku) enforces the six epistemic constraints
  ([constraint-reviewer.md](/Users/marcus/dev/cpa-consulting/.claude/agents/constraint-reviewer.md)) —
  a textbook fresh-context, narrowly-scoped reviewer.
- **8 scoped skills** with explicit refusal boundaries (`workpaper-generator` refuses regulated
  workpapers; `convert-firm-docs` is local-only, no cloud uploads; `qbo-workflow` is read-only
  by default). This is exactly the "pair every prohibition with a direction" and least-privilege
  discipline the artifacts call for [SoloGuide §1, §2].

Refinements (low priority): the root `CLAUDE.md` references a now-missing
`~/dev/claude-code-setup-report.md` roadmap (items I.1–S.16) — this REPORT.md supersedes that
pointer; update or drop the stale reference. Confirm the `SessionEnd` review-gate hook for
`deliverables/` (mentioned in `.claude/CLAUDE.md`) is actually installed, since it's described
as load-bearing for not leaking client artifacts.

### 3. `cpa-backend` (legacy) and `cpa-knowledge-base` (deprecated)

- **`cpa-knowledge-base`** is explicitly deprecated, superseded by `rag-system/apps/web`
  ([cpa-knowledge-base/README.md](/Users/marcus/dev/cpa-knowledge-base/README.md)). Don't invest
  in config. If kept for reference, a one-line root `CLAUDE.md` saying "DEPRECATED — do not
  develop; see rag-system/apps/web" prevents Claude from wasting effort here.
- **`cpa-backend`** (Express/Mongo/SQS/Textract/OpenAI) appears legacy relative to `rag-system`.
  Decide explicitly: retire it, or if still live, it needs at minimum the global safety hooks
  (it has its own `.env` at the repo root — ensure the global `.env` deny-hook covers it) and a
  short `CLAUDE.md`. No skills/subagents warranted until its status is settled.

### 4. Cross-cutting: security, compliance, and (if productized) monetization

- **Security/compliance hooks.** The venture handles client PII and tax data. Extend the
  existing global `.env`/lockfile PreToolUse blocks with deny rules on client-data paths
  (`docs/firm/**` in cpa-consulting; ingested-document and credential paths in rag-system), and
  set `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` in any headless/CI runs [SoloGuide §5, §8]. Treat
  AI-generated code as a junior dev's first PR — Veracode found 45% of LLM test cases produced
  OWASP-aligned vulnerabilities [SoloGuide §5]; review auth/access-control, input validation, and
  secrets before any deploy (rag-system's pluggable `AuthProvider` + scope-threaded retrieval is
  the right place to focus review attention).
- **Monetization (only if rag-system becomes a sold product).** If the RAG KB is ever offered
  beyond the firm, apply the artifacts' AI-specific rules: never offer unlimited high-tier LLM
  access; price with caps/credits or **BYOK**; per-action (per-document/per-query) beats
  per-token for non-developer buyers like a CPA firm; consider a Merchant-of-Record only for
  external B2C [SoloGuide §9]. For an internal-firm tool, this is informational, not urgent.

---

## Recommendations (staged, prioritized for the venture)

**Stage 1 — `rag-system` foundation (highest priority):**

1. Commit a project `settings.json` with the `allow`/`ask`/`deny` lists in §1c.
2. Add the PostToolUse typecheck+lint hook and a Stop hook gating `pnpm test` (§1d).
3. Add PreToolUse deny on `packages/db/drizzle/` migration writes and client-data/secret paths (§1d, §4).
4. Add 3–4 child `CLAUDE.md` files (db, rag, mcp, parser-py) to keep the root lean (§1b).

**Stage 2 — `rag-system` workflow:** 5. Add the reviewer / retrieval-eval-runner / planner subagents (§1e). 6. Install Superpowers; run one real multi-package feature through it to learn the cadence (§1h). 7. Lock the model/effort policy (Sonnet daily, opusplan for planning, Haiku subagents, xhigh
coding) — after verifying current model IDs (§1g).

**Stage 3 — hygiene & the other repos:** 8. Audit MCP server set to ~3–4 (Serena, Context7, Railway-or-CLI, optional claude-mem); drop idle ones (§1f). 9. Update `cpa-consulting`'s stale setup-report reference; confirm the deliverables SessionEnd gate (§2). 10. Decide `cpa-backend` retire-vs-maintain; add a one-line DEPRECATED `CLAUDE.md` to `cpa-knowledge-base` (§3).

**Thresholds that change the plan** [SoloGuide §Recommendations]:

- Claude starts ignoring `CLAUDE.md` rules → it's too long; prune / push to child files.
- Context climbs past ~10% from MCP overhead → remove idle servers.
- Reviewer subagent floods nitpicks → constrain to correctness/requirements gaps only.

---

## Caveats

- **This space drifts fast.** Both grounding artifacts carry explicit "verify before locking in"
  warnings. Re-check model IDs, effort levels, pricing/plan limits, the commands→skills merger,
  and bundle star-counts/repos against current official docs before encoding policy
  [SoloGuide Caveats; Bundles Caveats].
- **Bundle trust.** Verify live repos before installing — GSD had a meme-coin-scam incident
  (use open-gsd forks), Claude Flow renamed to Ruflo, and impostor "ECC" repos exist [Bundles Caveats].
  Anthropic does not vet plugin contents.
- **Research-only deliverable.** This report recommends config; it does **not** modify any repo.
  Applying any of it (committing `settings.json`, adding hooks/skills/agents) is a separate,
  explicitly-confirmed step.
- **Vulnerability/productivity statistics** (Veracode 45%, GitClear churn, the one controlled
  Superpowers benchmark) are named third-party research, directionally useful, point-in-time.

## Sources

_Cited inline above; full list maintained here._

### Local grounding artifacts (Compass research)

- **`compass_artifact_wf-7bcd3161-...md`** [cited as **SoloGuide**] — "The Solo Indie Developer's
  Guide to Claude Code (Mid-2026 Edition)." Harness setup, CLAUDE.md discipline,
  slash commands/skills/subagents/hooks, MCP starter pack, planning loop, models/effort/settings.json,
  context hygiene, indie monetization. Section numbers refer to its "Details" subsections (§1–§10)
  plus TL;DR/Key Findings (§0), Recommendations, and Caveats.
- **`compass_artifact_wf-9c887135-...md`** [cited as **Bundles**] — "Complete Reference Guide to
  Prebuilt Claude Code Bundles (2025–2026)." Survey + adoption plan of the bundle ecosystem
  (Superpowers, ECC, GSD, OpenSpec, Spec Kit, BMAD, Claude Flow/Ruflo, wshobson/agents,
  wondelai/skills, Compound Engineering, gstack) with comparison table and trust caveats.

### Repo evidence (this machine)

- `rag-system/CLAUDE.md`, `rag-system/.claude/settings.local.json`, `rag-system/package.json` — priority codebase stack, commands, conventions.
- `cpa-consulting/CLAUDE.md`, `cpa-consulting/.claude/{settings.json,CLAUDE.md,agents/constraint-reviewer.md,skills/*}` — exemplar config patterns.
- `cpa-knowledge-base/README.md`, `cpa-knowledge-base/package.json` — deprecation status.
- `cpa-backend/package.json`, `cpa-backend/cpa-api/package.json`, `cpa-backend/cpa-worker/package.json` — legacy stack.
- `~/.claude/settings.json` — global hooks (env/lockfile blocks, GSD guards), permissions, env flags.
