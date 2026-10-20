# Tooling Matrix

**Date:** 2026-09-29

One row per tool evaluated, **including rejected ones**. Scores are the author's judgement against the two
bars measured in `ledger/run_manifest.json`:

- **Bar A (capability bar):** contributes to building a ~195k-LOC three-surface product (RN/Expo + Firebase
  Functions + Next.js) with 400–950-line Firestore rules.
- **Bar B (brownfield feature bar):** contributes to landing one feature into such a repo as a reviewable PR
  with tests.

1 = no contribution · 3 = useful component · 5 = load-bearing and evidenced.
"Pricing: not found" means I did not fetch a price page and will not recall one.
Verdicts: **adopt** · **trial** · **watch** · **reject**.

## Harnesses and agents

| Tool | What it does | Status / evidence date | Pricing | Bar A | Bar B | RN | Firebase | Next.js | Unattended-safe? | Evidence quality | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude Code | CLI agent harness; headless `-p`, hooks, subagents | active, docs reference v2.1.259–261 | subscription + API; cost in result metadata | 3 | **5** | yes (as editor) | yes | yes | yes, with devcontainer + hooks | vendor-primary mechanism; no independent brownfield proof | **adopt** (already in use) | S7, S8, S9, S18 |
| GitHub Copilot coding agent | issue→PR in ephemeral Actions sandbox | active; Agent HQ preview 2026-02 | Pro $10/mo 300 premium req; Pro+ $39/mo 1500; overage $0.04/req | 2 | 4 | untested here | untested here | yes | yes, by design | vendor-documented; no independent brownfield data | **trial** (as a second opinion on PRs) | S48, S49, S87 |
| GitHub Agent HQ | control plane for third-party agents inside GitHub/VS Code | public preview 2026-02 | not found | 1 | 2 | — | — | — | n/a (orchestration) | vendor blog only | **watch** | S48 |
| OpenAI Codex (CLI + cloud) | local and cloud-sandboxed coding agent | active; CLI released 2025-04-16 | not found | 2 | 3 | untested here | untested here | untested here | cloud tasks isolated | secondary; security critique on autonomous patches | **trial** | S50 |
| Devin (Cognition) | "AI software engineer" | active; Cognition valued $10B 2025-09 | **not found** (billing page 404) | 1 | 1 | no evidence | no evidence | no evidence | claimed | **independent negative**: 3 clean successes / 20 tasks, unpredictable | **reject** for this workload | S46, S52, S92 |
| Cursor background agents | background/composer agents | exists, widely used | not found | 2 | 3 | anecdotal negative on EAS logs | — | yes | **unconfirmed** | primary page returned JS shell only | **watch** until claims verifiable | S56, S74 |
| Factory (Droids) | repo-wide agentic platform | active | not found | 2 | 3 | no evidence | no evidence | no evidence | claimed | vendor-only | **watch** | S55 |
| OpenHands | open-source orchestration over other agents; "Large Codebase SDK" | active, OSS | free/self-host | 2 | 3 | no evidence | no evidence | no evidence | claimed | vendor blog only | **watch** | S54 |
| Google Jules | asynchronous coding agent | out of beta 2025-08-06 | Google AI Pro/Ultra tiers | 1 | 2 | no evidence | no evidence | no evidence | async by design | vendor; no brownfield data | **watch** | S53 |
| Google Antigravity | agent-first IDE | announced 2025-11-18 with Gemini 3 | not found | 1 | 2 | no evidence | no evidence | no evidence | claimed | secondary (encyclopedia) | **watch** | S51 |
| SWE-agent / mini-SWE-agent | research harness; the standardized benchmark scaffold | active, MIT | free | 1 | 1 | no | no | no | research only | primary (it is the benchmark harness) | **reject** as a product; **use** its leaderboard as the honest score source | S2 |
| NousResearch Hermes-Agent | general-purpose self-improving agent, 7 sandbox backends | active, MIT | free/self-host | 1 | 1 | no | no | no | sandboxes available | primary (own repo) | **reject** — not a coding harness | S47 |
| Meta Hermes (JS engine) | **not an agent**; RN bytecode engine already in this stack | active | n/a | n/a | n/a | yes (it *is* RN) | — | — | n/a | primary | **not applicable** — name collision only | — |

## Spec and process tooling

| Tool | What it does | Status | Pricing | Bar A | Bar B | Unattended-safe? | Evidence quality | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|---|
| AGENTS.md convention | plain-Markdown steering file, cross-tool | active, Linux-Foundation-adjacent stewardship | free | 3 | **4** | yes | primary; adoption figure self-reported | **adopt** (conventions live here, not in specs) | S38 |
| GitHub Spec Kit | `/speckit-*` workflow producing spec/plan/tasks + converge loop | active | free | 2 | 2 | partly | primary + **independent negative benchmark** | **reject** wholesale; **borrow** the converge-loop idea | S32, S43 |
| AWS Kiro | spec + steering + file-event hooks | active (announced 2025-07-14) | not found | 2 | 2 | hooks yes | vendor | **watch** — steering/hooks concepts worth copying | S33 |
| OpenSpec | lightweight spec artifacts | active | free | 2 | 2 | partly | primary; scores 0/2 on Roles and Validation in a taxonomy | **watch** | S34, S42 |
| Tessl | spec-driven framework + registry | active | not found | 2 | 2 | unknown | vendor; annotation markers, no schema | **watch** | S35 |
| BMAD-METHOD | agent-role-based process framework | active | free | 2 | 2 | partly | primary; no independent evaluation | **watch** | S36, S42 |
| Agent-OS | spec/standards scaffolding | active | free | 2 | 2 | partly | primary | **watch** | S37 |
| **This report's `SPEC-FORMAT.md`** | minimal 4-required-field YAML + assumption ledger | untested | free | 3 | 4 | yes | **none — original design** | **trial**, with eyes open | — |

## Test and verification tooling

| Tool | What it does | Status | Pricing | Bar A | Bar B | Unattended-safe? | Evidence quality | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|---|
| **StrykerJS** | mutation testing; the anti-vacuous gate | active | free, OSS | **5** | **5** | yes | primary docs for exact config; practitioner reports on cost | **adopt** — and set `thresholds.break` | S6 |
| `@firebase/rules-unit-testing` | Firestore rules tests vs emulator | active | free | **5** | **5** | yes | vendor-primary, authoritative | **adopt** | S10 |
| Firebase Emulator Suite | local full-stack backend for CI | active | free | **5** | **5** | yes — `emulators:exec` is the CI form | vendor-primary | **adopt** | S14 |
| Maestro | RN/mobile E2E | active | free tier + cloud (not found) | 4 | 4 | yes via EAS Workflows | vendor comparison with own caveat | **adopt** (already in both repos) | S65, S76 |
| Detox | RN gray-box E2E | active; maintenance reportedly slowing | free | 3 | 3 | yes | blog claim on maintenance, unverified | **watch** | S65 |
| Playwright | web E2E | active, adoption leader | free | 4 | 4 | yes | search-only for adoption figures | **adopt** | S67 |
| Playwright MCP | exposes browser to agents via a11y tree | active, v0.0.78 Jul 2026 | free | 3 | 4 | yes | search-only | **trial** | S67 |
| `agent-browser` (Vercel Labs) | Rust CLI for agent browser control; embedded axe-core; screenshot/snapshot diff | active, Apache-2.0 | free | 3 | **4** | yes | primary repo; context-savings claim is vendor | **trial** | S59 |
| EAS Workflows + Maestro | `pull_request`-triggered mobile build→install→E2E | active | EAS build minutes (not found) | 4 | **4** | **yes — the only unattended mobile loop found** | vendor-primary describing a CI trigger | **adopt** | S76, S99 |
| Neon branching | per-run isolated Postgres | active | not found | 3 | 3 | yes | vendor; no latency figure published | **adopt** (for the Neon project only) | S64, S100 |
| Testcontainers | disposable real services in tests | active | free | 3 | 3 | yes | search-only | **trial** | S69 |
| fast-check | property-based testing for TS | active | free | 3 | 3 | yes | search-only | **trial** | S68 |
| axe-core / Lighthouse CI | a11y and perf gates | active | free | 3 | 3 | yes | independent benchmark: 40–63% of seeded defects caught, 17% undetectable | **adopt**, with no illusions | S75 |
| Chromatic / Percy | hosted visual regression | active | not found | 2 | 2 | yes | no fetched case of catching AI-generated regressions | **watch** — `agent-browser` diffing may suffice | — |
| Coverage (as a gate) | line/branch coverage thresholds | — | — | 1 | 1 | — | peer-reviewed as a weak proxy | **reject as a gate**; keep as a report | S58 |

## Infrastructure, routing, observability

| Tool | What it does | Status | Pricing | Bar A | Bar B | Unattended-safe? | Evidence quality | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|---|
| Claude Code devcontainer + `init-firewall.sh` | containment for unattended runs | active reference example | free | 4 | **5** | **yes — this is what makes it safe** | vendor-primary; "working example rather than a maintained base image" | **adopt** | S18 |
| Claude Code hooks (`exit 2`) | deterministic tool-call blocking | active | free | 4 | **5** | yes | vendor-primary | **adopt** | S9 |
| Vercel previews | web verification substrate | active | existing plan | 4 | 4 | yes | — | **adopt** (already in use) | — |
| Vercel MCP | agent access to Vercel | active 2026-09-15 | not found | 2 | 3 | with confirmation | vendor; own guidance is "always enable human confirmation" | **trial** | S98 |
| **Railway** | container PaaS; remote MCP, `railway agent`, PR Environments | active; MCP needs CLI 5.44.0+ | Hobby $5/mo; RAM $10/GB/mo; CPU $20/vCPU/mo | 2 | 2 | yes, destructive tools flagged at protocol level | vendor-primary, unusually good guardrail design; own 2026-02-11 incident | **watch** — orthogonal to Firebase/Expo stack; adopt only if a container service appears | S13, S95, S96, S97 |
| Neon | serverless Postgres with branching | active | not found | 3 | 3 | yes | vendor-primary | **adopt** (Neon project only) | S100 |
| OpenRouter | model routing/fallback, BYOK | active | BYOK 5% of normal cost; free under $25k/mo PAYG | 2 | 2 | yes | vendor-primary for fees; single-source quality critique | **watch** — pin providers if used | S81, S89 |
| LiteLLM proxy | self-hosted gateway with budgets that fail closed | active | free/self-host | 3 | 3 | yes | vendor-primary | **trial** — the only practical hard spend stop for a solo account | S82 |
| Vercel AI Gateway | routing, 0% token markup | active (page 2026-09-08) | 0% markup; allowlist/ZDR $0.10/1k req | 2 | 2 | yes | vendor-primary | **watch** | S88 |
| Anthropic Spend Limits API | server-side spend caps | active | Enterprise only | 1 | 1 | yes | vendor-primary | **reject** — not available at this account tier | S84 |
| Anthropic prompt caching | native cost reduction | active | cache read 0.1x input; 5-min write 1.25x | 4 | 4 | yes | vendor-primary | **adopt** — does most of what a gateway is sold for | S83 |
| OpenTelemetry GenAI conventions | standard `invoke_agent` spans | active standard | free | 3 | 3 | yes | primary open standard | **adopt** for run tracing | S85 |
| Laminar | agent tracing + automated failure detection | active | not found | 2 | 3 | yes | vendor marketing; no independent accuracy data | **trial** | S86 |
| LangSmith / Braintrust / AgentOps / W&B Weave | agent eval and tracing | not researched this pass | not found | — | — | — | **no evidence gathered** | **unassessed** | — |
| Sentry Seer | production error → agent fix | page 404'd | not found | — | — | — | unconfirmed | **unassessed** | S93 |

## UX and design tooling

| Tool | What it does | Status | Pricing | Bar A | Bar B | RN? | Evidence quality | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|---|
| Figma MCP server | supplies agents tokens, component/Code Connect mappings, screenshots | beta | not found | 3 | 3 | indirectly | vendor-only; no independent eval fetched | **trial** | S71, S72 |
| React Native Reusables | "Bringing shadcn/ui to React Native", on NativeWind | active, MIT | free | 4 | 3 | **yes** | primary repo | **adopt** for new RN UI | S73 |
| v0 / Lovable / Bolt / Figma Make | AI UI/app generators | active | not found | 1 | 1 | mostly no | comparison source 403'd | **reject** for this stack — web-greenfield oriented, no RN path evidenced | S79 |
| shadcn/ui registries | constrained component vocabulary for agents | active | free | 3 | 3 | via RN Reusables | registry governance claims unverified | **adopt** (web) | — |

## Architecture enforcement

| Tool | What it does | Status | Pricing | Bar A | Bar B | Unattended-safe? | Evidence quality | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|---|
| Nx `@nx/enforce-module-boundaries` | tag-based import boundaries, CI-gateable | active | OSS rule free; language-agnostic Conformance path "Requires Nx Enterprise plan" | 4 | 4 | yes | vendor-primary | **adopt** the ESLint rule; skip Enterprise Conformance | S103 |
| Turborepo `boundaries` | tag-based boundaries in `turbo.json` | **experimental** per its own docs | included | 3 | 3 | yes | vendor-primary | **trial** — explicitly experimental, RFC open | S104 |
| dependency-cruiser | dependency-graph rules in CI | active | free | 3 | 3 | yes | practitioner blog only, not its own docs | **trial** | S112 |
| LLM ADR-violation checking | agent checks code against written ADRs | research | — | 3 | 3 | yes | primary: >90% accuracy, Fleiss κ=0.724 on **explicit** decisions; falls short on implicit/deployment ones | **trial**, for written rules only | S111 |

## App-factory products

Scored strictly against Bar A and Bar B. The category-level finding is an **absence**: no surveyed product has
evidence of landing a reviewable PR with tests into an existing three-surface repo at this scale.

| Product | What it is | Owned source? | Existing repo? | Mobile/RN? | Pricing (as published) | Independent evidence | Verdict | Cites |
|---|---|---|---|---|---|---|---|---|
| Replit Agent | in-browser agent, effort/checkpoint billed | yes, exports to GitHub | attaches to repos; three-surface parity unverified | web-first, mobile not core | Core $25/mo, Pro $100/mo (2025 vintage, `STALE?`) | **negative** — deleted a production DB during a code freeze and "hid and lied about it" | **reject** as an app factory | S116, S129 |
| Lovable | prompt-to-app builder | GitHub sync exists | **export-oriented, not general import** | no RN pipeline found | not found | **negative** — BOLA exposed source, DB credentials and chat histories across "thousands of projects" | **reject** | S117, S122 |
| Bolt (bolt.new) | WebContainer in-browser builder | not confirmed | not confirmed | **architecturally impossible** — no Xcode/Android Studio/EAS in a browser VM | not found | none found | **reject** | S127 |
| Emergent | credit-based prompt-to-app | not confirmed | not confirmed | claims "Build web & mobile apps" — **vendor-only** | Free $0/10 credits; Standard $20/100; Pro $200/750 | none found | **reject** for this bar | S121 |
| Blitzy | reverse-engineers legacy code, then generates | n/a (enterprise) | **yes, by design** — the only one | none found | $0.10/line onboarded; $0.20/line generated; Enterprise from $500k/yr | one named enterprise deployment (secondary) | **reject** for a solo operator; closest architectural fit, at enterprise cost | S128, S130 |
| Cosine (Lumen) | enterprise agent for legacy codebases | not confirmed | positioned for it | none found | no figures found | none found | **gap** — insufficient evidence to score | S120 |
| Codegen | PR-generating agent against existing repos | via PRs | **yes, by design** | not confirmed | not found | none found | **gap** — closest fit to "reviewable PR with tests", unverified | S123 |
| Factory (Droids) | agentic dev platform | not confirmed | positioned for enterprise repos | not confirmed | $20 / $100 / $200 / $60+$40 per seat | none found | **gap** on mobile and independent evidence | S119 |
| Devin | autonomous "AI software engineer" | via PRs | by design | not found | not found (billing 404) | **negative** — 3/20 tasks; one study reported by three outlets, `STALE?` | **reject** for this workload | S46, S125, S126 |

## Rejected categories, with the reason

| Category | Why rejected |
|---|---|
| Parallel multi-agent code-writing | Anthropic and Cognition independently agree coding is a poor fit; Claude Code itself avoids it for code-writing; ~15× token cost [S101][S102] |
| LLM-judge-as-final-gate | Position and calibration bias persist in 2026-era judges [S109][S110]; executable tests against a running build must be the last word |
| Coverage-threshold gating | Peer-reviewed as a weak proxy; trivially inflatable by assertion-free tests [S58] |
| `--bare` for gated runs | Skips hooks, skills, MCP and CLAUDE.md [S7] — it disables the entire gate architecture |
| Devin for this workload | Independent negative evidence, unpredictable failures [S46] |
