# Claude Code Plugin & Skill Inventory — Keep / Disable Recommendations

**Date:** 2026-06-06
**Owner:** marcus
**Scope:** Global `~/.claude` plugin set (agents, skills, commands).
**Your active projects (used to judge relevance):**

- **recovery-platform** — TS/React Native + Firebase (Functions, Firestore) + Stripe; web is Angular 9 (regroup) + CRA (homegroups). Possible Angular→React migration.
- **cpa-consulting** — accounting/financial advisory; document- and spreadsheet-heavy, compliance.
- **research** — literature/web research + writing/synthesis.
- **rag-system** — retrieval-augmented generation; vector DB + embeddings + LLM.

> Confidence note: recommendations below come from each plugin's installed manifest + general product knowledge, **not** a deep per-plugin web-research pass (skipped deliberately for cost). Items marked **(low-confidence)** depend on facts about your non-recovery projects I haven't verified. Everything is reversible.

---

## How plugin context works (why this matters)

- An **enabled** plugin injects all its agent + skill **descriptions** into every turn. With ~100 enabled, that metadata is the real context cost.
- **Skill bodies** and **MCP tool schemas** are already lazy — loaded only when triggered. So the lever is the _count of enabled plugins_, not the skills themselves.
- **Disable** = stays installed/cached, out of context, re-enable instantly (`settings.json` → `enabledPlugins[...] = false`).
- **Uninstall** = removed from registry + cache (reinstall from marketplace to restore).
- Source path pattern: `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>`.

---

## Current state (already actioned this session)

### Uninstalled (4) — removed entirely

| Plugin                     | Marketplace           | Why                                                                      |
| -------------------------- | --------------------- | ------------------------------------------------------------------------ |
| systems-programming        | claude-code-workflows | c/cpp/golang/rust pros — you're TS/RN/Python; no C/C++/Go/Rust projects. |
| seo-analysis-monitoring    | claude-code-workflows | SEO tooling not in current scope.                                        |
| seo-content-creation       | claude-code-workflows | "                                                                        |
| seo-technical-optimization | claude-code-workflows | "                                                                        |

> Reversible: reinstall from the `claude-code-workflows` marketplace. SEO may be worth re-adding later for recovery-platform's 62K group-page SEO work (HG-SPEC-07/08) — flag for then.

### Disabled (15) — cached, unrelated to any project

adobe-for-creativity, atlan, base44, conductor, dash0, hyperframes, nimble, playground, qodo-skills, qt-development-skills, resend, runway-api, ui5-typescript-conversion, vanta, zapier — rationale in §D below.

**Net: 100 plugins enabled.** Recommendations below would take that to a leaner core.

---

## A. KEEP — core engineering (high confidence, used across all projects)

| Plugin                       | What it does                                                   | Verdict                 |
| ---------------------------- | -------------------------------------------------------------- | ----------------------- |
| serena                       | Semantic/symbol-aware code nav + edit (your primary code tool) | **KEEP**                |
| context7                     | Live library/framework docs lookup                             | **KEEP**                |
| typescript-lsp / pyright-lsp | LSP for TS (recovery) and Python (rag-system/research)         | **KEEP both**           |
| github                       | GitHub PRs/issues/API                                          | **KEEP**                |
| git-pr-workflows             | Git/PR workflow skill                                          | **KEEP** (light)        |
| commit-commands              | commit / commit-push-pr helpers                                | **KEEP**                |
| code-review                  | Diff review (bugs + cleanups)                                  | **KEEP**                |
| pr-review-toolkit            | PR-focused review agents                                       | **KEEP**                |
| code-simplifier              | Quality-only simplification pass                               | **KEEP**                |
| feature-dev                  | Structured feature workflow                                    | **KEEP**                |
| superpowers                  | Brainstorming, TDD, debugging, parallel-agent disciplines      | **KEEP** (foundational) |
| hookify                      | Author/manage hooks                                            | **KEEP**                |
| plugin-dev                   | Build plugins/agents/skills/hooks                              | **KEEP**                |
| skill-creator                | Author skills                                                  | **KEEP**                |
| mcp-server-dev               | Build MCP servers (rag-system tooling)                         | **KEEP**                |
| claude-md-management         | Maintain CLAUDE.md files                                       | **KEEP**                |
| claude-code-setup            | Harness/automation config                                      | **KEEP**                |
| semgrep                      | Static security scanning                                       | **KEEP**                |
| security-guidance            | Secure-by-default guidance                                     | **KEEP** (very light)   |
| playwright                   | Browser automation / E2E                                       | **KEEP**                |
| firecrawl + exa              | Web scraping + neural search (research project)                | **KEEP both**           |
| warp                         | Terminal integration                                           | **KEEP**                |

---

## B. KEEP — recovery-platform stack (high confidence)

| Plugin                      | What it does                                                                   | Verdict                                                                                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| firebase (firebase mp)      | Firebase basics, Firestore, Auth, Crashlytics, security-rules auditor, hosting | **KEEP** (core to both apps)                                                                                                                                                                                               |
| firestore-native            | Direct Firestore data access                                                   | **KEEP**                                                                                                                                                                                                                   |
| stripe                      | Stripe best-practices, error explain, test cards                               | **KEEP** (both apps bill via Stripe)                                                                                                                                                                                       |
| payment-processing          | Stripe/PayPal integration, billing automation, PCI                             | **KEEP** (overlaps stripe but adds PCI/billing patterns)                                                                                                                                                                   |
| sentry + sentry-cli         | Error tracking (regroup uses Sentry — your D-6 choice)                         | **KEEP both**                                                                                                                                                                                                              |
| frontend-design             | UI/design-direction skill                                                      | **KEEP**                                                                                                                                                                                                                   |
| frontend-mobile-development | RN architecture, state mgmt, Next.js, Tailwind patterns                        | **KEEP** (RN core)                                                                                                                                                                                                         |
| frontend-mobile-security    | XSS/WebView/mobile input security                                              | **KEEP**                                                                                                                                                                                                                   |
| multi-platform-apps         | Cross-platform app skill                                                       | **KEEP** (RN iOS+Android)                                                                                                                                                                                                  |
| javascript-typescript       | TS advanced types, JS/Node testing patterns                                    | **KEEP**                                                                                                                                                                                                                   |
| vercel                      | Next.js/Vercel deploy (if regroup web → React/Next)                            | **KEEP**                                                                                                                                                                                                                   |
| code-modernization          | Legacy assess→map→transform (Angular 9 → React for regroup)                    | **KEEP** — per your directive; **best-fit installed tool** for the Angular migration. Only near-alternatives are `ecc:angular-developer` (maintain, not migrate) and `ecc:ui-to-vue` (wrong target). No reason to disable. |

---

## C. KEEP — memory, planning, meta (high confidence)

| Plugin                              | What it does                                                                               | Verdict                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| claude-mem                          | Session memory / observations / make-plan                                                  | **KEEP** (you actively use it)                                         |
| pensyve                             | Memory recall/remember + memory-informed workflows                                         | **KEEP** (active hooks)                                                |
| remember                            | Lightweight remember skill                                                                 | **KEEP** (low cost) — minor overlap with claude-mem/pensyve; harmless. |
| session-report                      | Session summaries                                                                          | **KEEP** (light)                                                       |
| taches-cc-resources                 | Large meta-kit: create agents/skills/commands/hooks/plans + "consider" + "research" skills | **KEEP** — directly useful for this very task; broad but high utility. |
| tdd-workflows                       | Red/green/refactor cycle                                                                   | **KEEP**                                                               |
| error-debugging / error-diagnostics | Debugging + error-trace skills                                                             | **KEEP** (consider merging use with superpowers:systematic-debugging)  |
| dependency-management               | Dep audit/conflict skill                                                                   | **KEEP** (light)                                                       |
| developer-essentials                | Auth/debug/e2e/monorepo/sql/git patterns                                                   | **KEEP** — broad but practical; overlaps ecc somewhat (see §E).        |
| codebase-cleanup                    | deps-audit, refactor-clean, tech-debt                                                      | **KEEP**                                                               |
| comprehensive-review                | Multi-dimension full review                                                                | **KEEP** (or fold into code-review)                                    |

---

## D. DISABLED (15) — rationale (cached, re-enable anytime)

| Plugin                    | What it is                              | Why disabled                                                                    |
| ------------------------- | --------------------------------------- | ------------------------------------------------------------------------------- |
| adobe-for-creativity      | Adobe photo/video batch edit            | No media-production work.                                                       |
| atlan                     | Atlan data-governance SaaS              | Enterprise data catalog; not used. **(re-enable if rag/research adopts Atlan)** |
| base44                    | Base44 app-builder platform             | Not your stack.                                                                 |
| conductor                 | Track/workflow orchestration            | Overlaps your own planning (claude-mem make-plan, gsd, superpowers).            |
| dash0                     | Dash0 observability SaaS                | Not used (you use Sentry/Crashlytics).                                          |
| hyperframes               | Web animation (GSAP/anime/three/lottie) | No animation-heavy web work now.                                                |
| nimble                    | Nimble CRM / sales intel                | Sales-intel SaaS; not core. **(reconsider for biz dev)**                        |
| playground                | Experimentation sandbox                 | Not needed.                                                                     |
| qodo-skills               | Qodo code-quality SaaS                  | Redundant with code-review/semgrep/pr-review-toolkit.                           |
| qt-development-skills     | Qt/QML C++ desktop                      | Not your stack.                                                                 |
| resend                    | Resend email API                        | Niche; re-enable if you build product email flows.                              |
| runway-api                | Runway AI video generation              | Not used.                                                                       |
| ui5-typescript-conversion | SAP UI5 → TS                            | Not your stack.                                                                 |
| vanta                     | Vanta SOC2/compliance automation        | Vanta-product-specific. **(re-enable only if cpa-consulting uses Vanta)**       |
| zapier                    | Zapier automation                       | Niche; re-enable on demand.                                                     |

---

## E. CONTESTED — honest redundancy analysis

You asked me to justify rather than assert. Here's the real picture. **Net recommendation: trim, don't keep all — but you decide.**

### E1. voltagent-\* (10 packs) — **biggest single context cost**

Packs: biz, core-dev, data-ai, dev-exp, domains, infra, lang, meta, qa-sec, research. Each pack registers ~10 subagents → **~100 agent descriptions** in the Task tool on every turn.

- **Genuine overlap:** `voltagent-lang` (python-pro, typescript-pro, react-specialist, etc.) duplicates the **built-in** language agents (python-pro, typescript-pro, react-specialist are already in your base agent list) _and_ `ecc` language reviewers. `voltagent-infra`/`voltagent-domains`/`voltagent-meta` cover cloud/k8s/blockchain/IoT/orchestration you don't use.
- **Genuinely useful for you:** `voltagent-core-dev` (backend/frontend/fullstack architects), `voltagent-data-ai` (ai-engineer, ml-engineer, llm-architect, **vector-database-engineer, nlp-engineer** → rag-system), `voltagent-qa-sec` (security-auditor, qa, perf), `voltagent-research` (research-analyst, market/competitive — biz validation).
- **Recommendation:** **KEEP** `voltagent-data-ai`, `voltagent-research`, `voltagent-qa-sec`; **consider keeping** `voltagent-core-dev`, `voltagent-biz`. **DISABLE** `voltagent-lang` (duplicates built-ins), `voltagent-domains`, `voltagent-infra`, `voltagent-meta`, `voltagent-dev-exp` (overlaps ecc/developer-essentials). That alone removes ~50 redundant agent descriptions while keeping the high-utility ones.
- If you want zero effort: keeping all is _fine functionally_ — the cost is context bloat, not breakage.

### E2. claude-code-workflows skill packs

Packs: agent-orchestration, agent-teams, context-management, backend-development, cloud-infrastructure, database-cloud-optimization, database-design, deployment-strategies, deployment-validation, cicd-automation, code-documentation, code-refactoring, c4-architecture, full-stack-orchestration, llm-application-dev.

- These are mostly **skills (patterns)**, so per-pack cost is lower than voltagent's agents.
- **Overlap:** `agent-orchestration`/`agent-teams`/`context-management` overlap `superpowers` (dispatching-parallel-agents, subagent-driven-development) and the built-in Task/Agent tooling. `backend-development`/`database-design`/`code-refactoring` overlap `ecc` (backend-patterns, postgres-patterns, refactor) and `developer-essentials`.
- **Genuinely useful:** `llm-application-dev` (rag-implementation, embedding-strategies, hybrid-search, vector-index-tuning, llm-evaluation) → **directly rag-system**. `database-design:postgresql` → if cpa/rag use Postgres (you also have `neon`). `cicd-automation` → recovery CI.
- **Recommendation:** **KEEP** `llm-application-dev` (rag-system), `cicd-automation`. **DISABLE** `agent-orchestration`, `agent-teams`, `context-management` (superpowers covers it), `cloud-infrastructure` (k8s/istio/terraform — not used), `c4-architecture` (you have draw.io/excalidraw + ecc), `full-stack-orchestration`, `deployment-validation`. **Toss-up:** backend-development, database-cloud-optimization, database-design, code-documentation, code-refactoring, deployment-strategies — keep if you lean on their skills, else disable as ecc/developer-essentials duplicates.

### E3. agent-alchemy-\* (7 packs)

claude-tools, core-tools, dev-tools, git-tools, opencode-tools, sdd-tools, tdd-tools.

- **Useful:** `core-tools` (codebase-analysis, deep-analysis, interview-me, technical-diagrams), `dev-tools` (bug-killer, code-quality, docs-manager, feature-dev), `tdd-tools` (full TDD cycle), `sdd-tools` (spec-driven dev — pairs with your make-plan/spec work).
- **Disable candidates:** `opencode-tools` (only relevant if you author for the OpenCode editor — you don't), `git-tools` (single git-commit skill — `commit-commands` covers it), `claude-tools` (claude-code-tasks/teams — overlaps built-in Task + agent-teams).
- **Recommendation:** **KEEP** core-tools, dev-tools, tdd-tools, sdd-tools; **DISABLE** opencode-tools, git-tools, claude-tools.

### E4. ecc — the elephant

`ecc` is a kitchen-sink: **hundreds** of skills/commands/agents (languages, frameworks, ops, homelab, trading, healthcare, scientific, motion/video, etc.). It is very likely your **single largest context contributor** and overlaps nearly everything else.

- **Reality:** you use a sliver (react/ts/python/firebase/security/planning). The other ~90% (cisco-ios, defi, energy-procurement, logistics, manim, kotlin/swift/rust/perl, homelab) is dead weight in context.
- **Problem:** ecc is one plugin — you can't disable sub-skills, only the whole thing.
- **Recommendation (your call):** Either (a) **KEEP** and accept the cost (it's genuinely capable), or (b) **DISABLE ecc** and rely on the more targeted plugins above (superpowers, taches, developer-essentials, language packs) — this would be the **single biggest context reduction available**. I lean (b) _if_ you find its specific skills aren't pulling weight; otherwise (a). Flagging it because no other plugin comes close in footprint.

---

## F. HELD — data/AI (decide per your projects)

Still **enabled**; I didn't disable these because your rag-system/research/cpa work plausibly needs them.

| Plugin              | What it does                                                                        | Recommendation                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| qdrant-skills       | Qdrant vector DB: clients/SDK, deploy, scaling, search-quality, embedding migration | **KEEP** if rag-system uses Qdrant (very likely). **(low-confidence on which vector DB you use)** |
| llm-application-dev | RAG impl, embeddings, hybrid search, vector tuning, eval                            | **KEEP** (rag-system) — see §E2                                                                   |
| data-engineering    | Airflow/dbt/pipelines/lineage                                                       | **KEEP** only if rag/research has real data pipelines; else disable. **(low-confidence)**         |
| datahub-skills      | DataHub metadata catalog                                                            | **DISABLE** unless you run DataHub specifically (niche).                                          |
| bigdata-com         | Financial research: earnings, valuation, sector, investment memos                   | **KEEP** if cpa-consulting does market/financial analysis; else disable. **(low-confidence)**     |

---

## G. Judgment calls

| Plugin              | Note                                                                  | Recommendation                                                                                                            |
| ------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| neon                | Neon Postgres MCP                                                     | **KEEP** if any project uses Neon/Postgres; recovery is Firebase-only, but rag/cpa may use Postgres. **(low-confidence)** |
| redis-development   | Redis patterns                                                        | **DISABLE** unless rag-system caches in Redis. **(low-confidence)**                                                       |
| document-skills     | docx/pdf/pptx/xlsx, brand-guidelines, canvas-design                   | **KEEP** — strong fit for **cpa-consulting** (client spreadsheets/reports) and research write-ups.                        |
| claude-api          | Anthropic API/SDK reference (models, pricing, tool use, RAG, caching) | **KEEP** — directly relevant to **rag-system** LLM integration.                                                           |
| sourcegraph         | Code search across repos                                              | **KEEP** if you use Sourcegraph; else disable.                                                                            |
| greptile            | AI codebase Q&A SaaS                                                  | **DISABLE** — overlaps serena + code-review; SaaS dependency.                                                             |
| harness-engineering | Agent-harness readiness/setup                                         | **KEEP** (per your directive).                                                                                            |
| knowledge-catalog   | Knowledge-catalog discovery                                           | **KEEP** (per your directive; plausibly useful to research/rag).                                                          |

---

## H. Keep biz/marketing (per your directive)

You want these for regroup/homegroups/business planning + validation — **agreed, KEEP all**:

- `content-marketing` (content strategy/SEO copy), `customer-sales-automation` (cold email, sales, support), `business-analytics` (KPI dashboards, data storytelling), `social-publishing` (multi-platform posting).
- Also relevant and already kept: `voltagent-research` / `voltagent-biz` (market/competitive analysts), `recovery-app-go-to-market` (project skill), `business-strategy` (project skill).

---

## I. Suggested "lean core" target (optional, aggressive)

If you later want maximum context savings, disabling the following (all argued above) would cut the most bloat with least loss:

```
voltagent-lang, voltagent-domains, voltagent-infra, voltagent-meta, voltagent-dev-exp,
agent-orchestration, agent-teams, context-management, cloud-infrastructure,
c4-architecture, full-stack-orchestration, deployment-validation,
agent-alchemy-opencode-tools, agent-alchemy-git-tools, agent-alchemy-claude-tools,
datahub-skills, greptile, redis-development
```

Plus the **ecc decision** (§E4) — the single biggest lever if you choose to disable it.

This would take you from 100 → ~80 enabled (or ~79 without ecc), keeping every plugin that maps to recovery-platform / rag-system / cpa-consulting / research.

---

## J. How to apply changes

Disable (cached, reversible) — set `false` in `~/.claude/settings.json` `enabledPlugins`:

```bash
# example: disable one
python3 - <<'PY'
import json
p="/Users/marcus/.claude/settings.json"
s=json.load(open(p)); s["enabledPlugins"]["<plugin>@<marketplace>"]=False
json.dump(s,open(p,"w"),indent=2,ensure_ascii=False); open(p,"a").write("\n")
PY
```

Re-enable: set the same key to `True`. Changes take effect on next Claude Code restart. Backups from this session: `~/.claude/settings.json.bak-*`, `~/.claude/plugins/installed_plugins.json.bak-uninstall-*`.

---

## Appendix — verdict summary table

| Verdict                                     | Plugins                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Uninstalled**                             | systems-programming, seo-analysis-monitoring, seo-content-creation, seo-technical-optimization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Disabled (done)**                         | adobe-for-creativity, atlan, base44, conductor, dash0, hyperframes, nimble, playground, qodo-skills, qt-development-skills, resend, runway-api, ui5-typescript-conversion, vanta, zapier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Keep (core/stack/meta)**                  | serena, context7, typescript-lsp, pyright-lsp, github, git-pr-workflows, commit-commands, code-review, pr-review-toolkit, code-simplifier, feature-dev, superpowers, hookify, plugin-dev, skill-creator, mcp-server-dev, claude-md-management, claude-code-setup, semgrep, security-guidance, playwright, firecrawl, exa, warp, firebase, firestore-native, stripe, payment-processing, sentry, sentry-cli, frontend-design, frontend-mobile-development, frontend-mobile-security, multi-platform-apps, javascript-typescript, vercel, code-modernization, claude-mem, pensyve, remember, session-report, taches-cc-resources, tdd-workflows, error-debugging, error-diagnostics, dependency-management, developer-essentials, codebase-cleanup, comprehensive-review |
| **Keep (biz/marketing)**                    | content-marketing, customer-sales-automation, business-analytics, social-publishing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Keep (data/AI/docs)**                     | qdrant-skills, llm-application-dev, document-skills, claude-api, knowledge-catalog, harness-engineering                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Recommend disable (contested/redundant)** | voltagent-lang, voltagent-domains, voltagent-infra, voltagent-meta, voltagent-dev-exp, agent-orchestration, agent-teams, context-management, cloud-infrastructure, c4-architecture, full-stack-orchestration, deployment-validation, agent-alchemy-opencode-tools, agent-alchemy-git-tools, agent-alchemy-claude-tools, datahub-skills, greptile, redis-development                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Keep (recommended subset of contested)**  | voltagent-data-ai, voltagent-research, voltagent-qa-sec, voltagent-core-dev, voltagent-biz, agent-alchemy-core-tools, agent-alchemy-dev-tools, agent-alchemy-tdd-tools, agent-alchemy-sdd-tools, cicd-automation, agent-sdk-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Decide per project (low-confidence)**     | data-engineering, bigdata-com, neon, sourcegraph, backend-development, database-cloud-optimization, database-design, code-documentation, code-refactoring, deployment-strategies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Biggest single lever**                    | ecc (keep & accept cost, or disable for max context savings)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
