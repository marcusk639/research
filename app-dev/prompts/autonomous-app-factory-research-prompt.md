# Research prompt — Autonomous App Factory (spec → shipped, tested app)

Paste everything inside the fence below as the argument to the deep-research skill.
Recommended invocation: `/deep-research:deep-research-ultradeep` (or `/deep-research` with `mode: ultradeep`).
Optional: prefix your message with `ultracode` to allow multi-agent workflow fan-out.

---

```text
<role>
You are a principal engineer and tooling analyst evaluating whether a solo developer can
delegate end-to-end construction of non-trivial, multi-surface software applications to a
combination of AI agents, driven almost entirely by a written specification. You are
skeptical by default: vendor demos are marketing, benchmark numbers are context-dependent,
and "it generated code" is not "it shipped working software". Your job is to produce a
decision-grade, fully cited report plus a usable operating guide — not an enthusiastic
listicle.
</role>

<research_question>
What is the best achievable 2026 toolchain and operating procedure for building non-trivial
software applications — and smaller features inside existing applications — autonomously
from a written specification (natural language, YAML, or a hybrid), such that the AI system
produces intelligent architecture, modern and robust UX, well-written code, and unit +
integration + E2E tests that verify substantive behavior; validates that the app actually
works; and asks the human clarifying questions only when a genuine blocking ambiguity
exists?
</research_question>

<context>
Operator profile (the person this report is for):
- Solo developer / consultant on macOS. Primary harness today: Claude Code (Opus-tier main
  session, tiered subagent delegation, Serena MCP for symbol-aware edits, token-optimizer,
  ~90 project skills, ~33 subagents). Comfortable with CLI-first, git-worktree, and
  hook-based automation. Budget-sensitive but willing to pay for leverage.
- Existing stacks in scope: React Native (Expo) mobile, Firebase (Cloud Functions,
  Firestore with rules + indexes, Auth, Storage), Next.js web, TypeScript throughout,
  pnpm/Turborepo monorepos, Neon Postgres + Drizzle on one project, Inngest, Clerk.

Capability bar — the report must be judged against apps of this class, not to-do demos:
- `~/dev/recovery-platform/regroup` and `~/dev/recovery-platform/homegroups`: each is a
  three-surface product (React Native mobile app + Firebase Cloud Functions backend +
  Next.js web app) with real auth, real-time data, meeting/group domain models,
  notifications, and deployment pipelines.
- BEFORE searching, inspect those two directories locally (file counts, LOC by surface,
  package manifests, function counts, collection/rule counts, test presence) and write a
  short "capability bar" section quantifying what "non-trivial" means here. Every tool
  assessment later in the report must be scored against THIS bar, not a generic one.
- Secondary bar: a single feature added to one of those existing repos (brownfield), driven
  by a YAML or natural-language feature spec, landing as a reviewable PR with tests.

Tools the operator has named as candidates worth checking (treat as leads to verify, NOT
as a recommended set, and explicitly disambiguate any ambiguous name):
Hermes AI agent, OpenRouter, Railway.
</context>

<scope_and_materiality>
In scope:
- Greenfield multi-surface app generation AND brownfield feature delivery into existing repos.
- Specification formats and spec-authoring ergonomics (natural language, YAML, hybrid,
  schema-validated specs).
- Agent harnesses, orchestration, verification loops, model routing, sandboxing, infra
  automation, test generation, UX/design generation, and human-in-the-loop gating.
- Evidence about real-world reliability and failure modes, including cost and wall-clock time.

Explicitly out of scope (state this and do not drift):
- Model pretraining/fine-tuning research.
- No-code app builders that cannot emit owned source code into a git repo.
- Enterprise procurement, SOC2 vendor questionnaires, team-of-20 process design.
- Pure prompt-engineering tips with no toolchain implication.

Materiality rule: a tool only matters if it plausibly contributes to shipping the
capability-bar app or a brownfield feature with tests, owned in the operator's own repos.
Reject anything that only works on greenfield toy scaffolds, or that locks source into a
proprietary hosted editor with no export.
</scope_and_materiality>

<search_angles>
Decompose the work into these orthogonal angles. Treat each as its own retrieval program
with multiple distinct queries; do not rephrase one query twelve times. Add angles if the
evidence demands it, but do not silently drop any.

A1. SPEC AS SOURCE OF TRUTH — spec-driven development formats and tools: GitHub Spec Kit,
    AWS Kiro (spec/steering/hooks), OpenSpec, Tessl, BMAD-METHOD, Agent-OS, Conductor-style
    track/spec/plan artifacts, SDD/PRD→plan pipelines, `AGENTS.md`/`CLAUDE.md` conventions.
    What does a spec need to contain for an agent to not need to ask? Is there any published
    spec SCHEMA (YAML/JSON) with evidence of working end to end? How is spec→code drift
    detected and re-synced?

A2. AUTONOMOUS CODING HARNESSES — Claude Code (+ Claude Agent SDK, headless/`-p`, hooks,
    subagents, skills, plugins), OpenAI Codex CLI/cloud, Google Jules/Antigravity, Cursor
    background agents, GitHub Copilot coding agent / Agent HQ, Devin, Factory Droids,
    OpenHands, SWE-agent, Aider, Cline/Roo/Kilo, opencode, Amp, Goose, Trae, Charlie,
    Hermes (verify identity — there are multiple unrelated "Hermes" products: disambiguate
    the agent harness from NousResearch's Hermes model family and from any namesake).
    For each: unattended-run support, repo-scale handling, multi-surface/monorepo handling,
    cost model, permission/sandbox model, evidence of brownfield success.

A3. ORCHESTRATION & VERIFICATION LOOPS — how multiple agents are composed so output is
    checked rather than trusted: generator/evaluator (GAN-style) harnesses, planner→
    implementer→reviewer chains, adversarial critic agents, LLM-as-judge with calibration,
    durable orchestration (Temporal, Inngest, LangGraph, Claude's Workflow/fan-out
    patterns), parallelism via git worktrees or containers (container-use, devcontainers),
    and self-healing loops driven by failing tests/CI/logs. What loop topology has the best
    published evidence of raising correctness? Where do loops reward-hack instead?

A4. TESTS THAT ACTUALLY VERIFY — the hardest part of the ask. Agent-generated unit,
    integration, and E2E tests for: React Native (Maestro, Detox), web (Playwright,
    Playwright MCP, Vercel Agent Browser, Cypress), Firebase (Emulator Suite, rules unit
    tests, Functions integration tests), Postgres (Neon branching, testcontainers, seeded
    fixtures). Critically: what techniques detect VACUOUS tests — mutation testing (Stryker
    et al.), coverage-plus-mutation gates, property-based testing, golden/approval tests,
    assertion-density and flakiness analysis, independent test-writer vs implementer agents,
    "tests written from the spec before the code" (TDD-for-agents)? Cite measured results
    where they exist.

A5. UX AND DESIGN AUTONOMY — producing modern, robust UX without a designer: v0, Lovable,
    Bolt, Figma Make + Figma MCP, design tokens and design systems as agent input,
    shadcn/ui registries, Tamagui/NativeWind for RN, Storybook + Chromatic/Percy/visual
    regression as an automated UX gate, accessibility automation (axe, Lighthouse CI),
    screenshot-feedback loops where an agent sees its own rendered UI. What actually
    produces UX quality that survives review, on mobile as well as web?

A6. ARCHITECTURE QUALITY — can agents make good architectural decisions from a spec?
    Evidence on agent architecture/design review, ADR generation, dependency and
    boundary enforcement (dependency-cruiser, ESLint boundaries, Nx/Turbo graph rules),
    codebase-context tooling (Serena/LSP-aware editing, repo maps, semantic indexes),
    and known pathologies (over-abstraction, duplicated concerns, God modules, ignoring
    existing patterns in brownfield repos).

A7. MODEL ROUTING, COST AND RELIABILITY — OpenRouter, LiteLLM, Requesty, Portkey,
    Helicone, Vercel AI Gateway, Bedrock/Vertex: per-task routing (cheap model for
    mechanical edits, frontier for judgment), fallbacks, rate-limit and outage handling,
    prompt caching economics, spend caps. Include a grounded cost picture: what does one
    capability-bar app build plausibly cost in tokens/dollars/wall-clock, and one brownfield
    feature? Cite real published run costs where available; label estimates as estimates.

A8. INFRASTRUCTURE AND ENVIRONMENT AUTONOMY — Railway (agent tooling/MCP, ephemeral
    environments), Vercel, Firebase App Hosting + emulators + `firebase deploy`, Expo EAS
    Build/Submit/Update, Neon branch-per-agent-run, preview environments, seeded demo data,
    secret handling, and CI (GitHub Actions) as the agent's verification substrate. What
    does the agent need in order to RUN the app it just wrote, on all three surfaces,
    including a mobile build?

A9. UNATTENDED-RUN SAFETY AND CONTROL — sandboxing (Docker/devcontainers, macOS
    sandbox-exec, VM isolation), permission models and the real risks of
    bypass-permissions/YOLO modes, prompt-injection exposure when agents read issues/web,
    budget and time kill switches, checkpointing/rollback, audit trails, and what MUST stay
    human-gated (prod deploys, migrations, payments, secrets, force-push).

A10. MINIMIZING CLARIFYING QUESTIONS — the operator's specific requirement. Techniques:
    spec completeness linting/scoring, ambiguity detection passes, explicit assumption
    ledgers ("I assumed X because Y — flagged for review"), defaults/convention libraries
    ("steering" files, house style, stack defaults), question-budget policies, and
    escalation criteria (ask only when the wrong guess is expensive/irreversible).
    What is empirically better: asking up front, asking never and flagging assumptions, or
    a one-shot batched clarification round? Cite evidence, not vibes.

A11. OBSERVABILITY AND FEEDBACK — agent-run tracing and evals (LangSmith, Braintrust,
    Laminar, AgentOps, Weave), plus production signal loops (Sentry/Crashlytics →
    agent-authored fix PRs). How do you know a long autonomous run is going wrong before
    it has burned $80 and 4 hours?

A12. END-TO-END "APP FACTORY" PRODUCTS — Replit Agent, Lovable, Bolt, Emergent, Blitzy,
    Cosine, CodeGen, Factory, Devin, and any newer entrant. Assess each strictly against
    the capability bar and the brownfield bar. Be blunt about the gap between demo and
    three-surface production app, and about source-code ownership/export.

A13. GROUND TRUTH ON AUTONOMY LIMITS — independent measurement rather than vendor claims:
    SWE-bench Verified and its criticisms, SWE-Lancer, Terminal-Bench, Aider polyglot,
    METR time-horizon and RCT-style developer-productivity studies, published post-mortems
    of long autonomous runs, and any data on greenfield vs brownfield success rates,
    context-length degradation, and multi-hour task reliability. This angle is the reality
    check on every other angle; the final recommendation MUST be consistent with it.

A14. FIT TO THIS OPERATOR'S STACK — which parts of the toolchain actually handle React
    Native + Expo, Firestore security rules and indexes, Cloud Functions, monorepo
    pnpm/Turborepo, and mobile E2E. Name the gaps where NO tool is good yet and the human
    must stay in the loop.
</search_angles>

<method>
Follow the deep-research pipeline in ultradeep mode: scope → plan → retrieve → triangulate
→ synthesize → red-team critique → refine → package. Non-negotiable specifics:

1. Local grounding first: read the two reference repos to establish the capability bar
   before any web retrieval. Ground the bar in numbers you actually measured.
2. Recency: this field changes monthly. Prefer sources from the last 6 months; anything
   older than 12 months must be marked `[STALE?]` with a note on what may have changed.
   Record the publication date of every source. Do not present a deprecated product,
   pricing tier, or model name as current.
3. Fetch before quoting: never cite a page you only saw as a search snippet. Never cite a
   URL you could not retrieve — record it as a gap instead.
4. Independence: for every load-bearing claim (a capability, a price, a benchmark number,
   a reliability rate) require corroboration from ≥2 independent sources, or label it
   `single-source`. Vendor documentation is acceptable for "what the product claims to do"
   and NEVER acceptable as evidence that it works.
5. Disconfirmation duty: for every tool you recommend, actively search for its failure
   reports, negative reviews, abandonment, and cost blowups. A recommendation with no
   disconfirming search performed is not finished work.
6. Verify existence and identity: any tool named in this prompt, and any tool you surface,
   must be confirmed to exist with a real URL, current status (active/abandoned), and
   pricing as of the report date. Explicitly resolve the "Hermes" ambiguity. If a named
   lead turns out to be irrelevant or dead, say so plainly — do not pad the report with it.
7. No invention: do not invent tool names, CLI flags, config keys, prices, model IDs, or
   benchmark scores. If you do not know, write "unknown / not found" and list it as a gap.
   Any command, YAML key, or config snippet in the deliverables must either be traceable to
   a cited doc or be explicitly labeled `[UNVERIFIED — author's design, needs testing]`.
8. Confidence labels: every recommendation carries `high` / `medium` / `low` confidence and
   a one-line statement of what evidence would change it.
9. Distinguish three tiers throughout: (a) works today, evidenced; (b) plausible but
   unproven at this scale; (c) aspirational / not there yet.
10. Clarifying questions to the operator: ask at most 3, only if a genuinely blocking
    ambiguity exists (e.g. hard budget ceiling, willingness to run unattended overnight,
    cloud-vs-local execution preference). Otherwise state your assumptions in the manifest
    and proceed.
</method>

<deliverables>
Write all output into `~/dev/research/app-dev/` (this is the research subject directory;
keep everything self-contained there). Exclude this prompt file, anything under
`prompts/`, and your own output files from any "read every file" pass.

1. `REPORT.md` — the primary synthesis. Required structure:
   - Executive summary: the honest verdict in ≤10 bullets, including what is NOT possible
     yet at the capability bar.
   - Capability bar (measured from the two reference repos).
   - The recommended reference architecture for an autonomous build pipeline, presented as
     stages: spec authoring → spec validation → architecture/plan → scaffold → implement →
     test authoring → verification loop → run/deploy → acceptance validation → human review
     gates. For each stage: what runs it, what it costs, what it produces, what gates it.
   - A Mermaid diagram of the pipeline.
   - Angle-by-angle findings (A1–A14) with inline citations.
   - Three concrete pipeline variants with tradeoffs: Minimal (extends the operator's
     current Claude Code setup, lowest new surface area), Recommended (best
     evidence/effort ratio), Maximal (highest autonomy, highest cost/risk). Give each a
     cost estimate and a "what breaks first" note.
   - What still requires the human, and why — be specific and unapologetic.
   - Confidence table and open questions.
2. `TOOLING-MATRIX.md` — one row per tool evaluated (include rejected tools). Columns:
   tool, category, what it does, status/last release, pricing, fit to capability bar
   (1–5), fit to brownfield feature bar (1–5), handles RN / Firebase / Next.js?,
   unattended-safe?, evidence quality, verdict (adopt / trial / watch / reject), primary
   citations.
3. `SPEC-FORMAT.md` — a proposed, concrete specification format for this operator:
   a documented YAML schema (+ natural-language escape hatches) covering product intent,
   users/roles, surfaces, domain model, data model and access rules, flows, non-functional
   requirements, design/UX direction, acceptance criteria, test strategy, out-of-scope, and
   assumption-resolution policy. Include: (a) a filled-in APP-level example that would
   plausibly produce a Homegroups-class app; (b) a filled-in FEATURE-level example for a
   single feature added to an existing repo; (c) a spec-completeness checklist the agent
   runs before it starts, listing exactly which missing fields justify asking the human.
   Derive the format from cited prior art (A1) and mark every original element as
   `[UNVERIFIED — author's design]`.
4. `GUIDE.md` — the operating runbook. Prerequisites and install/config steps for each
   required tool (with citations to official docs), accounts/keys needed, cost controls to
   set on day one, the exact sequence of commands/invocations for (a) a greenfield app run
   and (b) a brownfield feature run, the human review checkpoints, how to abort and roll
   back, and a troubleshooting section for the most likely failure modes. Mark any command
   you have not verified.
5. `VERIFICATION-STRATEGY.md` — how the pipeline proves the app works: the test pyramid per
   surface, concrete gate thresholds (coverage, mutation score, E2E flow list, a11y,
   visual regression), how vacuous/reward-hacked tests are detected and rejected, and the
   acceptance-validation step that checks the running app against the spec's acceptance
   criteria rather than against its own tests.
6. `ADOPTION-PLAN.md` — a staged 30-day plan with a falsifiable experiment per stage
   (start with a brownfield feature in an existing repo, not a greenfield app), each with
   a success metric, a cost ceiling, and a kill criterion.
7. `RISKS.md` — risk register: security (prompt injection, secret exposure, destructive
   ops), correctness (silent breakage, vacuous tests, architectural rot), cost blowups,
   vendor/lock-in and abandonment risk, and maintainability of AI-authored code. Each with
   likelihood, impact, and a specific mitigation tied to a pipeline gate.
8. `SOURCES.md` — the full source registry: ID, title, publisher, URL, date, type
   (primary/vendor/independent/community), quality rating. Plus a `GAPS.md` section or file
   listing every question you could not answer and what would answer it.

Formatting: GitHub-flavored Markdown, every file opens with title + date + one-paragraph
summary, tables over prose for comparisons, inline citations as `[S12]` keyed to
`SOURCES.md`, no emojis, no marketing tone. Prefer "this is unproven" over a confident
guess. A shorter report with defensible claims beats a long one with padding.
</deliverables>

<self_check_before_finishing>
Before declaring done, verify and state explicitly in the report:
- Every recommended tool: exists, is active, has a cited URL and dated evidence.
- Every load-bearing number: cited, dated, and either corroborated or labeled single-source.
- Disconfirming evidence was searched for each "adopt" verdict, and what it showed.
- The final recommendation is consistent with the ground-truth autonomy limits in A13 — if
  the evidence says fully unattended multi-surface app generation is not reliable today,
  the report says so in the executive summary instead of burying it.
- The three pipeline variants are actually runnable by one person on macOS with the stacks
  listed in `<context>`, and the RN/Firebase/mobile-E2E gaps are named.
- `GUIDE.md` is specific enough that the operator could start the 30-day plan tomorrow
  without further research, and every unverified command is labeled as such.
</self_check_before_finishing>
```

---

## Techniques used (and why)

| Technique                             | Where                           | Purpose                                                                  |
| ------------------------------------- | ------------------------------- | ------------------------------------------------------------------------ |
| System/role framing with a skeptic bias | `<role>`                      | Counteracts the tool-hype failure mode that dominates this topic         |
| Explicit XML sectioning               | throughout                      | Keeps the long prompt parseable; each section is separately addressable   |
| Concrete capability bar from local repos | `<context>`                   | Forces "non-trivial" to be measured, not asserted; anchors every verdict  |
| Orthogonal angle decomposition (A1–A14) | `<search_angles>`             | Matches the pipeline's Phase 1 requirement; prevents rephrased queries    |
| Grounding + fetch-before-quote rules  | `<method>` 3–4                  | Primary hallucination control for a topic full of stale/invented tooling  |
| Disconfirmation duty                  | `<method>` 5                    | Forces negative evidence, the thing tool research usually omits           |
| Identity/existence verification       | `<method>` 6                    | "Hermes" is ambiguous; dead products are the main padding risk            |
| Explicit `[UNVERIFIED]` labeling      | `<method>` 7, deliverables 3–4  | Lets the prompt demand original design work without licensing invention   |
| Confidence labels + falsifiers        | `<method>` 8                    | Makes the report actionable and re-checkable later                        |
| Question budget (max 3, blocking only) | `<method>` 10                  | Mirrors the autonomy behavior being researched                            |
| Rigid output contract (8 files)        | `<deliverables>`                | Consistency across runs; separates matrix/guide/risks from synthesis      |
| Three-variant recommendation           | `REPORT.md` spec                | Avoids a single fragile "stack of the week" answer                        |
| Self-check gate                        | `<self_check_before_finishing>` | Pre-commits the report to its own quality gates before it ships           |

## Usage notes

- `ultradeep` mode is the right setting: ≥15 sources, full red-team loop. `standard` will
  produce a plausible-sounding but under-verified tool list on this topic.
- The local-repo grounding step in `<context>` requires the run to have filesystem access to
  `~/dev/recovery-platform/`. If you run this in a sandbox without it, delete that bullet
  and supply the num el fan-out across the 14 angles, prefix your message with `ultracode`;
  otherwise the pipeline will work through them sequentially.
- Expect to answer 0–3 clarifying questions. The likely ones: hard monthly budget ceiling,
  whether unattended overnight runs are acceptable, and local vs cloud execution.
- Re-run cadence: this landscape turns over fast. Treat the report as valid for ~90 days;
  `SOURCES.md` dates make the staleness check cheap.
