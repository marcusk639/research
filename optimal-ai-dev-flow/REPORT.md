# Optimal AI Development Flow — Synthesis Report

_Phase C | 2026-08-01 | Consumes `corpus-ledger.md` (211 claims) + `findings/w1..w9` (~5,300 lines) | Produces this report + four playbooks_

**Playbooks (the operational output):**

| File                                                                   | What it is                                                          |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`playbooks/engagement-playbook.md`](playbooks/engagement-playbook.md) | The repeatable client engagement, E0→E7. **The commercial core.**   |
| [`playbooks/domain-rampup.md`](playbooks/domain-rampup.md)             | Reaching working depth in an unfamiliar domain, with a calibration test |
| [`playbooks/process-diagnosis.md`](playbooks/process-diagnosis.md)     | The pre-automation playbook and the six gates                       |
| [`playbooks/harness-blueprint.md`](playbooks/harness-blueprint.md)     | What to configure once, and what to delete                          |

---

## 1. Executive summary

**Instrument review before optimising anything else.** The one longitudinal field study of an AI
throughput mandate (802 developers, 196,212 PRs, Tier A) found throughput rose 2.09x while
substantive review fell 39%→21% and silent approvals doubled — with merge rate and revert rate
staying green throughout. A cost-and-velocity dashboard would have shown that program succeeding.
**Substantive-review share is the instrument that catches it, and it appears in none of the corpus's
proposed cadences.** Log it from week one. Every other stage is gated on it.

**Delete the ceremony layer, keep exactly one instruction file per repo.** Instruction files pay
enormously for *existing* (0% → 55–68% compliance, Cohen's h = 1.93) and pay nothing for
*elaboration* (size, position, architecture, and inter-file conflict all null; BF10 = 0.096). The
corpus's load-bearing "AI.md cuts tokens 40%" figure is not merely unsupported — **its direction is
inverted**: repository context files raise inference cost 20–23% (p < 0.001) with no success-rate
gain. Apply a content test, not a length budget: keep a line only if nothing else in the repository
states it. Move anything that must *hold* into a hook, because compliance decays 5.6% per generated
function.

**Route the reviewer to frontier capability, not to the cheap tier.** Cheap-Judge routing is the
single most directly contradicted claim in the cost program. It is also mostly moot: under a flat
subscription, token cost below the cap is not a marginal cost. Route cheap only where work is
mechanical, spec-complete, and metered.

**Abandon the cross-project session topology.** It is not a supported configuration and Anthropic
closed the request as not planned. Build a written startup recipe and a checkpoint file instead.
Give up durable cross-project context; keep reach within a live session.

**Drop the $80–120/mo target.** It is arithmetically impossible — three corpus claims assume a flat
subscription fee shrinks with reduced usage. Stay on Max as the backbone; consider metered routing
only above roughly $150–200/mo of API-equivalent spend *outside* the subscription.

**Separate client repositories absolutely.** Two independent layers require it: every cross-project
context mechanism is a leak path (and user-scope imports load without an approval dialog), and
residuals clauses cover only unaided memory — a per-client knowledge repo has **no contractual
protection**. One-way flow: generic → client, never the reverse without an explicit
de-identification-and-permission gate.

**Sell diagnosis on the touch-time ratio, not on failure statistics.** Every circulated automation
failure figure is a marketing artefact. The evidenced reframe is **arrested scaling**: ≥85% met
non-financial expectations, 11.5-month payback, only 3% reach 50+ bots.

**Treat 80/20 reuse as a hypothesis under measurement.** It has zero evidence base anywhere.

_(394 words)_

---

## 2. Corpus reconciliation ledger

**Aggregate:** 211 claims. CONFIRMED 81 · UNVERIFIED 51 (29%) · REFUTED 15 · STALE 10 ·
PARTIALLY CONFIRMED 10 · SKIPPED 2 · CONTESTED 1 · REPO-FACT (not verifiable by design) 25.

**The 29% UNVERIFIED rate is the headline number for corpus reliability.** Where a recommendation
below rests on an UNVERIFIED claim, it says so inline.

**Verdict vocabulary is not uniform and was deliberately not normalised.** W3 used
`PARTIALLY CONFIRMED` and `CONTESTED / PARTIALLY REFUTED`; those labels encode real distinctions
(mechanism confirmed, magnitude unchecked) that flattening would destroy. Read the correction column,
not just the label.

### 2.1 W1 — Dev loop (77 claims)

| ID    | Verdict                | Current value / correction                                                                                                                  | Tier |
| ----- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| C-001 | CONFIRMED              | Single-agent loop + tight context + worktrees remains Anthropic's own recommended scaling pattern                                            | B    |
| C-002 | **UNVERIFIED**         | No "2026 Agentic Coding Trends Report" and no "95%" statistic exists. Likely a misattribution of the June 2025 multi-agent research blog post | —    |
| C-009 | CONFIRMED              | Weekly + 5-hour per-seat allowances are real, shared with Claude chat and Cowork, and throttle parallel work                                 | A    |
| C-011 | CONFIRMED              | research→plan→execute→verify→review matches Anthropic's documented loop                                                                      | A    |
| C-012 | CONFIRMED (verbatim)   | "Claude's context window fills up fast, and performance degrades as it fills"                                                                | A    |
| C-013 | CONFIRMED              | `/clear` between tasks, subagents for investigation, fresh sessions — Anthropic's own guidance                                               | A    |
| C-014 | CONFIRMED (exact)      | Karunaratne: <1,000 hand-written lines of 20,000                                                                                            | B    |
| C-015 | **UNVERIFIED**         | Source real; exact quote not re-verified verbatim                                                                                            | C    |
| C-016 | **UNVERIFIED**         | Same caveat as C-015                                                                                                                        | C    |
| C-017 | CONFIRMED (exact)      | Explore → Plan → Implement → Commit is the current documented workflow                                                                       | A    |
| C-018 | CONFIRMED (exact)      | AskUserQuestion interview → SPEC.md → fresh session                                                                                          | A    |
| C-022 | CONFIRMED              | Ronacher's "dumbest possible thing that will work"                                                                                          | B    |
| C-024 | CONFIRMED (exact)      | 90.2% multi-agent research-eval improvement — Anthropic self-report about its own system, not third-party replicated                         | A    |
| C-025 | CONFIRMED              | Measured on breadth-first decomposable tasks, not coding                                                                                     | A    |
| C-026 | CONFIRMED (exact)      | "About 15x more tokens than chat interactions"                                                                                              | A    |
| C-027 | CONFIRMED (exact)      | "Less effective for tightly interdependent tasks such as coding"                                                                            | A    |
| C-028 | CONFIRMED, evolving    | Osmani's "70% problem" is real and current, but he has since published "The 80% Problem" — treat the percentage as illustrative, not a constant | B  |
| C-030 | CONFIRMED              | Agent Teams and worktree sessions draw from one shared per-seat allowance                                                                    | A    |
| C-031 | CONFIRMED (exact)      | "Approximately 7x more tokens… when teammates run in plan mode." Note: Agent Teams remain gated behind `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | A |
| C-032 | CONFIRMED              | A separate model-specific Opus limit message exists                                                                                          | A    |
| C-033 | CONFIRMED (components) | Codex async fan-out and Cursor inline autocomplete are genuine differentiators; "best but not only" is a judgment call                       | B    |
| C-037 | CONFIRMED              | PostToolUse formatter hook is a current documented pattern                                                                                   | A    |
| C-040 | CONFIRMED (exact)      | Hooks fire inside subagents, carrying `agent_id`/`agent_type`                                                                                | A    |
| C-041 | CONFIRMED              | Subagents isolated, tool allow-lists, cheap models supported. **But see the composed routing rule in §3.4 — "route them cheap" is wrong for the reviewer role** | A |
| C-042 | CONFIRMED (exact)      | Built-in Explore/general-purpose subagents; `isolation: worktree` is a real current field                                                    | A    |
| C-043 | CONFIRMED (exact)      | `.claude/skills/SKILL.md`; `disable-model-invocation: true`                                                                                 | A    |
| C-044 | **UNVERIFIED**         | "Workflow A" and "~80% of work" are the corpus's own naming and allocation                                                                   | —    |
| C-045 | CONFIRMED (exact)      | `--worktree`/`-w`; `.worktreeinclude` copies gitignored secrets into new worktrees                                                            | A    |
| C-047 | CONFIRMED, nuanced     | Clean **unnamed** worktrees auto-remove; named ones and those with changes persist or prompt                                                  | A    |
| C-050 | CONFIRMED              | Ralph = bash loop, fresh context per iteration, filesystem/TODO/git as memory                                                                 | B    |
| C-051 | PARTIALLY CONFIRMED    | Mechanism confirmed; **the "100–150k token" threshold appears in no source** — treat as an unsupported operator estimate                     | A / — |
| C-052 | **UNVERIFIED**         | Not independently re-confirmed                                                                                                              | —    |
| C-053 | **STALE**              | Spec-kit is at **111k+ stars** (2026-06-11), not 93k; 30+ agents confirmed                                                                    | B    |
| C-054 | CONFIRMED / opinion    | Kiro's EARS notation and three-document spec system are real; "sledgehammer" is editorial                                                     | A / C |
| C-055 | CONFIRMED / opinion    | PRP/Context Engineering is a real methodology; "adopt the idea" is the corpus's recommendation                                                | B    |
| C-056 | **UNVERIFIED**         | Head-to-head verdicts are the corpus's own synthesis; components individually confirmed                                                       | —    |
| C-057 | CONFIRMED              | Codex is cloud-first/async, parallel tasks, returns PRs. "More token-efficient for batch" is unquantified                                     | B    |
| C-058 | CONFIRMED              | Cursor credit billing produced real overages; a documented 2025 apology-and-refund incident exists                                            | B    |
| C-059 | **UNVERIFIED**         | Amp's "free, ad-supported" model could not be confirmed — fetch failed, budget exhausted                                                      | —    |
| C-061 | CONFIRMED / UNVERIFIED | Claude Squad confirmed (tmux + worktrees, 8.2k stars); Crystal→Nimbalyst and Vibe Kanban not checked                                          | B    |
| C-062 | CONFIRMED              | Aider is git-native, model-agnostic, maintains its own leaderboards                                                                          | A    |
| C-066 | CONFIRMED              | All session types draw from one shared per-seat bucket                                                                                       | A    |
| C-067 | **STALE**              | True for ~one week. Weekly caps received a temporary +50% boost from May 13, repeatedly extended (last known: Aug 19, 2026)                   | B    |
| C-069 | UNVERIFIED-AS-RANKING  | Underlying facts (7–15x cost, poor fit for interdependent coding) confirmed; "#11 of 11" is the corpus's own synthesis                        | B    |
| C-070 | UNVERIFIED-AS-RANKING  | Kiro facts confirmed; ranking is opinion                                                                                                     | C    |
| C-071 | UNVERIFIED-AS-RANKING  | Ralph's cost/slop risk plausible; no source ranks it                                                                                         | B/C  |
| C-072 | UNVERIFIED-AS-RANKING  | Spec-kit's growth does not validate a ranking                                                                                                | C    |
| C-073 | UNVERIFIED-AS-RANKING  | Cursor/Codex differentiators confirmed; ranking is opinion                                                                                   | C    |
| C-077 | UNVERIFIED-AS-RANKING  | Hooks/CLAUDE.md confirmed as real infrastructure; ranking is opinion                                                                          | B    |
| C-079 | UNVERIFIED-AS-RANKING  | Underlying loop is Anthropic's default; "#1" is judgment                                                                                     | B    |
| C-080 | **UNVERIFIED**         | Staged rollout is the corpus's own plan. **Superseded by §4 of this report**                                                                 | —    |
| C-087 | CONFIRMED (exact)      | `--dangerously-skip-permissions` refuses under root/sudo; containers/VMs without internet only                                               | A    |
| C-088 | CONFIRMED → **STALE**  | 88.6% was Opus 4.8's real SWE-bench Verified score; current SOTA (Claude Fable 5) 95.0%                                                       | A    |
| C-089 | CONFIRMED (raw number) | 80.0% is GPT-5.2's real score; attributing it to the product "GitHub Copilot" conflates wrapper and model — SWE-bench benchmarks models       | A    |
| C-090 | **UNVERIFIED**         | **"DeepSeek V4" resolves to no model at any benchmark score anywhere**                                                                       | —    |
| C-091 | CONFIRMED → **STALE**  | 69.2% was real for Opus 4.8; Claude Fable 5 (80.3%) has surpassed it                                                                          | A    |
| C-092 | **UNVERIFIED, likely wrong** | No source cites 41.0%; real GPT-5.2/Codex figures found are **55.6–56%** — a 14.6-point gap                                            | —    |
| C-093 | **UNVERIFIED**         | No DeepSeek/MiniMax/GLM combination at 59.0%; a separate GLM-5.1 figure of 58.4% is close, corroborating the ledger's own mislabelling flag  | C    |
| C-095 | PARTIALLY CONFIRMED    | Claude's ~1M context confirmed; Copilot ~200k and OpenRouter 1.05M not re-checked                                                            | A / — |
| C-096 | **UNVERIFIED**         | The "28-point lead" cannot be validated because one input (C-092) does not resolve                                                           | —    |
| C-102 | PARTIALLY CONFIRMED    | Codex's cloud-async architecture confirmed as structurally different; the performance judgment is unquantified                               | B / C |
| C-106 | **UNVERIFIED**         | Corpus's own strategic recommendation                                                                                                       | —    |
| C-108 | **UNVERIFIED**         | Corpus's own self-set target metrics                                                                                                        | —    |
| C-109 | PARTIALLY CONFIRMED    | Model names plausible; 20,000-token allocation and `gpt-5.4-inline` not checked                                                              | C    |
| C-110 | PARTIALLY CONFIRMED    | `claude-opus-4.8` is a real designation; capability list consistent with confirmed docs                                                       | B    |
| C-112 | **UNVERIFIED**         | Corpus's own routing logic                                                                                                                  | —    |
| C-113 | **UNVERIFIED**         | Decision matrix is the corpus's own synthesis; components plausible                                                                          | —    |
| C-114 | **UNVERIFIED**         | No source for "~90% of Claude's autonomous capability" — an unsupported estimate                                                             | —    |
| C-116 | **UNVERIFIED**         | No source for "~95% of development workflows"                                                                                               | —    |
| C-118 | CONFIRMED → **STALE**  | 78.9% (2026-07-09) and 83.1% ±1.1 (2026-05-01) are real dated entries. Superseded: GPT-5.6 Sol 85.77%, Claude Opus 5 84.64% (2026-07-31)     | A    |
| C-119 | PARTIALLY CONFIRMED    | Claude ~1M confirmed; GPT-5.5's figure and "Modular Stack ~2M" not checked. "Modular Stack" resolves to no product                            | A / — |
| C-123 | CONFIRMED              | Codex CLI + GPT-5.5 is a real benchmarked pairing                                                                                           | B    |
| C-124 | CONFIRMED / **REFUTED**| Raw figures real; the implied "Codex leads" framing is refuted — **"Claude Code + Fable 5" at 83.8% already outscored Codex on the same board at the same date** | A |
| C-129 | **UNVERIFIED**         | Not checked (budget). Already reversed in-corpus by C-172; and see C-132's ToS finding                                                        | —    |
| C-130 | **UNVERIFIED**         | Not checked                                                                                                                                 | —    |
| C-162 | See §2.8 X-06          | The "SWE-bench Pro maps to your work better" reconciliation has **no independent citation** — it is a defensible but unsupported argument     | C    |
| C-173 | CONFIRMED / UNVERIFIED | Cursor inline autocomplete is real; "pays for itself" is the corpus's own inference                                                          | B / — |

### 2.2 W2 — Orchestration (7 claims)

| ID    | Verdict        | Current value / correction                                                                                                                                                                                                                       | Tier |
| ----- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| C-046 | **REFUTED**    | **No source documents a 2–3 ceiling.** Vendor guidance is *higher*: "Start with 3–5 teammates"; `/batch` splits across **5 to 30** worktree-isolated subagents. The embedded phrase "the documented practical ceiling" is false | A    |
| C-060 | **STALE**      | Conductor: Mac-only yes, closed-source yes, but now drives Claude Code, Codex **and Cursor**, and has paid tiers (Free $0 BYO / Pro $50 / Teams $60 per user / Enterprise), as of 2026-08-01. "One-click PRs" and "Linear/GitHub integration" **could not be verified** — a competitor is credited with first-class Linear/Jira integration | A / — |
| C-074 | **STALE**      | An external orchestrator is no longer required for worktree lifecycle. Native: `--worktree`, `/batch`, `isolation: worktree`, `WorktreeCreate`/`WorktreeRemove` hooks, agent view, desktop auto-worktree                        | A    |
| C-076 | **UNVERIFIED** | No controlled study, no practitioner report with numbers, no vendor data on optimal lane count for a solo reviewer. Every figure found (2–4, 3–5, 5–30, "N", 10) is assertion                                                     | —    |
| C-141 | CONFIRMED      | Pattern confirmed by three independent implementations. **Filename correction: `WORKFLOW.md` has no special status** — it enters context only if imported or explicitly read                                                     | A / B |
| C-151 | **REFUTED**    | RAM is not the binding variable for cloud-model tiers. Splitting machines has a documented cost: auto memory is machine-local and `/usage` is computed from local history "on this machine"                                       | A    |
| C-152 | CONFIRMED      | Checkpoint-file rule confirmed and reinforced: `-p` sessions don't appear in the picker and their worktrees are never auto-cleaned; teams cannot resume in-process teammates; `/add-dir` dirs aren't restored. **Batch size "5–10" is UNVERIFIED** | A |

### 2.3 W3 — Verification (27 claims)

| ID    | Verdict                        | Current value / correction                                                                                                                                                        | Tier |
| ----- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| C-019 | CONFIRMED                      | "Give Claude a way to verify its work" leads the current best-practices doc: "the difference between a session you watch and one you walk away from"                              | A    |
| C-020 | CONFIRMED                      | Beck: TDD is a "superpower"; agents "delete tests in order to make them 'pass'." Single-practitioner account; his "immutable test" fix is an intention, not a shipped mechanism    | B    |
| C-021 | CONFIRMED (verbatim)           | "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens"                                                                       | A    |
| C-023 | CONFIRMED (near-verbatim)      | Reviewer over-flagging is Anthropic's own stated expectation, presented as an operational heuristic, not a measured result                                                         | A    |
| C-038 | CONFIRMED                      | Exit 2 blocks `PreToolUse`/`Stop`; override after **8 consecutive blocks**. A documented escape valve, not absolute enforcement                                                    | A    |
| C-039 | PARTIALLY CONFIRMED            | Synchronous blocking confirmed; the `--findRelatedTests`/Stop-hook split is **not in current official docs** — it is the corpus's own recommendation                               | A / — |
| C-048 | CONFIRMED (verbatim)           | "A fresh context improves code review since Claude won't be biased toward code it just wrote" — the documented Writer/Reviewer pattern                                             | A    |
| C-049 | CONFIRMED (verbatim)           | "Flag only gaps that affect correctness or the stated requirements"                                                                                                               | A    |
| C-075 | PARTIALLY CONFIRMED            | Pattern is real and documented. **No quantified "measurable accuracy gain" figure exists** — "measurable" is doing unsupported work                                                | A / — |
| C-078 | PARTIALLY CONFIRMED            | Direction strongly supported; the superlative "single biggest lever, ranked against all others" is not something any source measures                                               | B    |
| C-082 | CONFIRMED                      | "Tidy First" correctly attributed to Beck                                                                                                                                        | B    |
| C-125 | See §2.8 X-01                  | Mechanism real; effectiveness addressed in the contradiction resolution                                                                                                          | —    |
| C-135 | **UNVERIFIED**                 | "Quality enforced before human review / compounding velocity gains" is the corpus's own framing. The underlying mechanism has partial support (CriticGPT: human+critic beats human-alone ~60%) but that study **assists a human reviewer** — it does not show quality can be fully enforced before a human looks | C / B |
| C-153 | CONFIRMED (as sound practice)  | Spec-as-source-of-truth review matches documented practice. Not externally benchmarked against alternatives                                                                       | B    |
| C-164 | **UNVERIFIED**                 | An internal editorial judgment; no external evidence can confirm or refute it                                                                                                     | —    |
| C-175 | CONFIRMED (mechanism)          | Builder→Judge→revise matches the studied actor-critic pattern                                                                                                                     | B    |
| C-176 | Repo-specific / CONFIRMED as general practice | Structured domain-specific checklist beats open-ended "find bugs." Repo specifics not web-verifiable                                                              | B    |
| C-177 | **CONTESTED / PARTIALLY REFUTED** | **"The judge pass is pattern-matching, not deep reasoning" is directly contradicted.** LLM-judge research documents negation blindness and explicit model variance; OpenAI's critic was built on GPT-4-class capability *because* subtle bugs need reasoning capacity. **The single most load-bearing revision in the whole cost program** | B |
| C-178 | CONFIRMED (general practice)   | Gating review on multi-file changes while skipping docs/config edits is standard cost/noise reduction                                                                              | C    |
| C-179 | Repo-specific / CONFIRMED as general practice | Same treatment as C-176                                                                                                                                            | B    |
| C-180 | PARTIALLY CONFIRMED            | Direction well established; the "100x" multiplier is contested and dated (modern estimates 10–30x). **The "15 minutes saves 2 hours" figure has no independent source** — illustrative, not measured | B / — |
| C-181 | CONFIRMED                      | Maestro Cloud integrates with GitHub Actions, CircleCI, EAS Workflows                                                                                                             | A/B  |
| C-182 | CONFIRMED (general practice)   | Substituting a local/stub provider for a paid API in CI is uncontested convention                                                                                                 | B    |
| C-207 | CONFIRMED (general practice)   | Current monorepo guidance explicitly warns against a single undifferentiated pipeline across multiple package managers                                                             | B    |
| C-209 | CONFIRMED                      | Consistent with Anthropic's own hard-gate-vs-advisory distinction. No source states it in these words for a "Judge-review skill" — a sound inference, not an independent claim     | A    |
| C-210 | CONFIRMED                      | `--passWithNoTests` is a real Jest flag; mobile native builds require Xcode/Android SDK or a managed service                                                                       | A/B  |
| C-211 | CONFIRMED (general practice)   | PR-only e2e and not gating on a perfect run matches converged flaky-test guidance                                                                                                 | B    |

### 2.4 W4 — Documentation (10 claims) — **6 of 10 refuted**

| ID    | Verdict        | Current value / correction                                                                                                                                                                                                                                     | Tier |
| ----- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| C-034 | CONFIRMED      | Verbatim in current docs. Accurate quotation; whether the underlying causal premise holds is C-035's question                                                                                                                                                   | A    |
| C-035 | **REFUTED**    | **Refuted across 25–500 lines**, the band covering essentially all real files. ICR 60.0/65.2/67.7/64.0% at 25/100/250/500 lines; GLMM chi2=5.16, df=3, p=0.16; **affirmative-null BF10 = 0.096**. Untested above 500 lines. The vendor asserts the opposite and supplies no data | A |
| C-036 | **STALE**      | **Five scopes, not three** (managed policy, user, project — including `./.claude/CLAUDE.md` — local, nested). Imports have a **max depth of four hops**; external imports trigger a one-time approval dialog                                                     | A    |
| C-107 | **REFUTED — DIRECTION INVERTED** | Repository context files **increase** cost **20% (SWE-bench) / 23% (CTXBench), p < 0.001%**, driven by +2.45 and +3.92 agent steps, with no significant success-rate change. **No source anywhere supports a 40% reduction.** The same paper found no correlation between file length and either success rate or per-instance cost, and that the "repository overview" section — exactly what C-107 prescribes — is inert | A |
| C-131 | **STALE**      | `.cursorrules` superseded by `.cursor/rules/*.mdc`. Separately, **a prose line in CLAUDE.md cannot select the model for the session it is loaded into**                                                                                                          | A    |
| C-137 | **REFUTED**    | Anthropic states the opposite of the "infrastructure" framing: instruction files are "context, not enforced configuration." The "degrades into random model selection" consequence is separately **UNVERIFIED**. Two independent errors in one claim              | A    |
| C-140 | **UNVERIFIED** | No study of per-subject context files in code-free repos. Nearest evidence cuts both ways: context files helped **only** where all other documentation was stripped; otherwise "redundant documentation" — and a research subject dir is all documentation      | —    |
| C-142 | **REFUTED**    | Stated as a verification target, never measured. The closest real measurement runs the other way (+19–23% cost), and file length showed no relationship to cost at all                                                                                          | A    |
| C-185 | **REFUTED**    | "Executable" is false. **Nothing reads a tier annotation in a markdown file and routes on it.** The annotation is a legitimate record of intent; calling it executable describes a mechanism that does not exist — itself an instance of the drift class in question | A |
| C-206 | **REFUTED**    | `./.claude/CLAUDE.md` **is** a first-class project-instructions location. And nested subdirectory CLAUDE.md files load **on demand and are not re-injected after `/compact`**, so they are not redundant with a root file                                        | A    |

### 2.5 W5 — Cost and routing (53 claims)

| ID    | Verdict        | Current value / correction                                                                                                                                        | Tier |
| ----- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| C-004 | CONFIRMED      | Max 20x is cost-favourable above ~$400–2,000/mo API-equivalent. Conditional on volume, not universal                                                              | B    |
| C-005 | CONFIRMED      | ~10 billion tokens over 8 months, self-reported (Redelinghuys)                                                                                                    | B    |
| C-006 | CONFIRMED      | "$15,000+" API-equivalent, self-reported, not independently audited                                                                                               | B    |
| C-007 | CONFIRMED      | **"~$800 total… 93% saving" is the correct primary-source figure.** Resolves X-05                                                                                  | B    |
| C-008 | **STALE**      | "~95% Opus" confirmed; "over 90% cache reads" imprecise — primary source shows 63% cache-read + 34% cache-write = 97% cache-*related*                              | B    |
| C-010 | **UNVERIFIED** | No source ties 70/30 to any measured outcome. The one detailed practitioner data point ran **the opposite ratio (~95% Opus)** and reported it as his best result   | B    |
| C-063 | CONFIRMED      | Sonnet 4.6 $3/$15, Opus 4.8 $5/$25, Haiku 4.5 $1/$5 per MTok, as of 2026-08-01                                                                                     | A    |
| C-064 | CONFIRMED      | Opus ~67% more per token than Sonnet; fewer Opus-hours than Sonnet-hours per tier                                                                                  | A/B  |
| C-065 | CONFIRMED      | Cache reads cost 0.1x base input; included in the flat fee — the actual mechanism behind subscription arbitrage                                                    | A    |
| C-068 | CONFIRMED      | **Agent SDK, `claude -p`, GitHub Actions moved to a separate credit pool billed at API rates, effective 2026-06-15**                                               | B    |
| C-081 | **UNVERIFIED** | Compound claim. "Stay on Max 20x" supported; the 70/30 component unsupported; "watch the weekly cap" sound                                                         | B    |
| C-083 | CONFIRMED      | _Kahn v. Anthropic, PBC_, No. 3:26-cv-05763, N.D. Cal., filed 2026-06-14. Unresolved, no certified class                                                           | A    |
| C-094 | **UNVERIFIED** | Claude Max $200 flat confirmed; Copilot/Codex $10–39 and OpenRouter terms not re-verified                                                                          | A / — |
| C-097 | **UNVERIFIED** | A generalisation from one case to "full-time developers" broadly; no second practitioner data point found                                                          | B    |
| C-098 | CONFIRMED      | ~$15,000 API-equivalent, self-reported                                                                                                                            | B    |
| C-099 | **REFUTED**    | **Real 8-month subscription cost was ~$800, not $1,600.** $1,600 = 8 x $200 is an assumption v1.md imported, not what the source reports — he was on $100/mo Max 5x for at least part of the window | B |
| C-100 | **REFUTED**    | Real savings ~= $14,200 (~93–95%), not "$13,400 (~89%)". Derivative error propagating from C-099                                                                    | B    |
| C-101 | **UNVERIFIED** | Logically sound vendor-dependency risk; no documented incident of an Anthropic outage stalling a solo pipeline was found                                            | C    |
| C-103 | CONFIRMED      | DeepSeek V4 Pro $0.435/$0.870 per MTok on OpenRouter. **Note the tension with C-090:** the *pricing pages* exist while no *benchmark entry* does                    | A    |
| C-104 | CONFIRMED      | DeepSeek V4 Flash $0.0896/$0.1792 per MTok; released 2026-04-24                                                                                                    | A    |
| C-105 | **UNVERIFIED** | Reconstructing the math does not reproduce "<20 loops/day → $15–30/mo" without much smaller per-loop token counts than agentic loops use                            | B    |
| C-111 | **UNVERIFIED** | DeepSeek pricing confirmed; "minimax-m3 ($0 cost)" could not be verified — no evidence of a genuinely free tier                                                     | A / — |
| C-115 | CONFIRMED      | True on its face regardless of which subscription total is used                                                                                                    | C    |
| C-117 | CONFIRMED      | OpenRouter's automatic provider failover is real and on by default                                                                                                | A    |
| C-120 | **UNVERIFIED** | Claude Max $200 confirmed; Codex enterprise tier and "Modular Stack $40–70" not verified                                                                            | A / — |
| C-121 | **STALE**      | "Zero lock-in" overstates it — OpenRouter is itself a single-vendor dependency, and 2026-01/02 ToS enforcement added a new constraint the claim doesn't account for | A    |
| C-122 | **UNVERIFIED** | "$13–50/developer-day" plausible as an order of magnitude, but the one real data point implies ~$70+/day at peak intensity — above the stated ceiling               | B    |
| C-126 | **REFUTED**    | **Feature-name conflation.** "Zero Completion Insurance" means *you are not billed for empty/failed completions* — it is **not** mid-session provider failover. That failover is a separate, correctly-real feature | A |
| C-127 | **UNVERIFIED** | No source ties 80/15/5 (as opposed to 70/30, 90/10, or A/B/C) to any measured cost or quality outcome. Central to X-02                                              | B/C  |
| C-128 | **UNVERIFIED** | "$40–70/month" plausible at moderate volume; "comparable or better throughput" has no supporting benchmark                                                          | B    |
| C-132 | **STALE**      | Manifest's capability description is accurate as written — **but since 2026-01/02 Anthropic has explicitly banned and technically blocked using Claude Max/Pro OAuth tokens outside Claude Code/Claude.ai.** Real ban risk not disclosed in the claim | A |
| C-133 | **UNVERIFIED** | General routing research shows 40–85% reductions achievable, but **no study tests the 80/15/5 ratio**, and "consistently" overstates the reported variance          | B    |
| C-134 | CONFIRMED      | Low-bar qualitative claim; flat pricing removes per-token anxiety at the cost of overpaying at low usage                                                            | C    |
| C-136 | **STALE**      | Same critique as C-121                                                                                                                                            | A    |
| C-138 | CONFIRMED      | At 1B+ tokens/month, Max remains cheaper by a wide margin                                                                                                          | B    |
| C-139 | **REFUTED**    | Restates the erroneous $13,400/89% figure                                                                                                                         | B    |
| C-143 | **UNVERIFIED** | No external benchmark validates the A/B/C ratio either — but it is **explicitly keyed to the operator's real, mostly non-coding task mix**, unlike 80/15/5          | —    |
| C-144 | **UNVERIFIED** | Reasonable heuristic decision tree; no external validation                                                                                                        | —    |
| C-148 | **UNVERIFIED** | **OpenRouter has no native "alias" feature** — achievable only via a wrapper or application code                                                                    | A / — |
| C-149 | **UNVERIFIED** | No evidence for a 20–30% Max-token-reduction figure; internal planning estimate                                                                                    | —    |
| C-155 | **UNVERIFIED** | $215–230/mo plausible as an order of magnitude; not measured against actual spend                                                                                  | B    |
| C-163 | **REFUTED**    | **"$80–120/mo blended" is arithmetically impossible while "Max is the backbone."** Cheapest Max tier is $100/mo; Max 20x is $200/mo. Max + nonzero OpenRouter cannot land below $100, let alone $80 | A |
| C-165 | CONFIRMED      | With a clarification: OpenRouter access to Anthropic models **via API key** is unaffected by the ToS ban; only binding the *consumer subscription's own OAuth credential* into third-party tools is barred | A |
| C-166 | CONFIRMED      | Reinforced by post-hoc evidence — Manifest's subscription-binding feature carries ToS/ban risk                                                                      | A    |
| C-169 | **UNVERIFIED** | No evidence for "saves 2–3 Max subscription months per quarter"                                                                                                    | —    |
| C-170 | **UNVERIFIED** | Same as C-127 — no external source validates this tier-ratio policy. **Also see C-185: the Tier Policy block's delivery mechanism does not exist**                  | B/C  |
| C-171 | **SKIPPED**    | Repo-specific tier calibration; depends on §2 ground truth, excluded from verification by design                                                                    | —    |
| C-172 | CONFIRMED      | "Route directly to OpenRouter, skip Hermes/Manifest" is reinforced by the ToS finding                                                                              | A    |
| C-174 | **REFUTED**    | Assumes Max's cost drops ~$60–80/mo from "fewer heavy sessions." **Max is a flat monthly fee.** Reduced usage does not recapture dollars absent an explicit tier downgrade, which the claim never states | A |
| C-183 | **UNVERIFIED** | Gemini embedding pricing not re-verified; DeepSeek/Sonnet escalation routing directionally reasonable                                                              | —    |
| C-184 | **SKIPPED**    | Engagement-specific document-tier assignment; not web-verifiable                                                                                                   | —    |
| C-187 | **REFUTED**    | Same flat-rate arithmetic error as C-163/C-174                                                                                                                    | A    |
| C-188 | CONFIRMED (cost component only) | Routing waste is real and evidenced (~40–60% of production LLM budgets go to unnecessary flagship use). **Whether it is *the* bottleneck vs. review capacity is a separate question — resolved against this claim in X-04** | B |

### 2.6 W6, W8, W9 (12 claims)

| ID    | WS  | Verdict        | Current value / correction                                                                                                                                                                                        | Tier |
| ----- | --- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| C-145 | W6  | **UNVERIFIED** | **No published measurement of "200-token question statement saves 2M tokens" exists in either direction.** The 10,000:1 ratio is presented as measured and is not                                                  | —    |
| C-146 | W6  | **UNVERIFIED** | The checkpoint rule has no evidence base. Two adjacent lineages support the *general* principle (prospective hindsight; "select the right questions" from the GJP training study); **neither has been tested on agent runs** | — |
| C-147 | W6  | **UNVERIFIED** | The three-stage *shape* independently matches validated rapid-assessment designs (weak corroboration). **The token bands (<50K / 2–6M / <200K) are unsourced** — budget policy, not findings                       | B (structure only) |
| C-086 | W8  | **UNVERIFIED** | Conductor's marketing page makes no statement about source availability, GitHub OAuth scopes, or what data leaves the machine; no security or privacy documentation located. **The normative half — that a third-party binary with client-repo access is a confidentiality event requiring contractual treatment — is independently established at Tier A** | — |
| C-150 | W8  | **REFUTED**    | Wrong on premise and remedy. §7216 does **not** flatly prohibit disclosure to a service provider — 26 CFR §301.7216-2(d)(2) permits it under written notice. And "local Claude Code" is not a compliance state; it transmits to a hosted API. **The operative restrictions are geographic:** (d)(1) US-located recipient; (d)(3) no SSNs outside US territory; (c)(2) restricts intra-firm disclosure abroad. **The operational conclusion about OpenRouter survives, for a different reason** | A |
| C-003 | W9  | **CONFIRMED** (qualified) | Holds, and now has Tier A field evidence that did not exist when asserted: 802 devs / 196,212 PRs; PR volume grew 3.1x while the reviewer pool grew 1.5x. Qualified: conditional on the operator being reviewer of record; cost binds first only below a throughput floor already passed | A |
| C-029 | W9  | CONFIRMED      | Near-verbatim: "Code review became the new bottleneck" (2026-01-28). Osmani himself is Tier C; his underlying data is second-hand from vendor telemetry, and **he gives no reviewer-capacity number**              | C    |
| C-084 | W9  | **UNVERIFIED** | No measured study establishes a concurrent-session ceiling. **"Multiple practitioners independently" is the part that fails** — several sources trace to the same Anthropic guidance, and Anthropic frames 3–5 as a productivity *floor*, not a supervision *ceiling*. The corpus inverted its source | C |
| C-085 | W9  | CONFIRMED (attribution) | Quote real, marginally misquoted (Dzombak, 2025-08-08). An accountability position, not evidence about capacity                                                                                              | C    |
| C-154 | W9  | **UNVERIFIED** | No evidence a 15-minute weekly cadence detects review-capacity drift — and none refutes it. **The weekly-review construct itself has no empirical validation.** What the evidence does say: the metrics the cadence should watch are not the ones it lists | — |
| C-186 | W9  | **UNVERIFIED** | Same as C-154. The v2 cadence adds a routing check but **still contains no review-load or review-latency indicator**                                                                                             | —    |
| C-189 | W9  | **UNVERIFIED** | An internal plan sequence. The one W9-relevant property — that "ongoing weekly review" is sequenced **last** — is **the sequencing the evidence argues against**: in the one field study, review-side damage accrued *during* the ramp | — |

### 2.7 REPO-FACT rows (25) — ground truth, not web-verifiable

Audited 2026-06-27 (C-156–C-168, C-190–C-199) or ≤2026-07-14 (C-200–C-205, C-208). **Phase B was
instructed not to verify these and did not.** They may have changed.

| ID    | Fact (abbreviated)                                                                                | Verdict                              | Freshness risk                                                       |
| ----- | ------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------------------------------- |
| C-156 | Operator profile: research-heavy, 9 ventures, legal/financial case manager, occasional builder    | ACCEPTED AS GROUND TRUTH             | Low — the profile drives every recommendation here                    |
| C-157 | `unemployment-fraud-detection/` — 25/29 sources verified, REPORT.md final                          | ACCEPTED                             | Medium                                                               |
| C-158 | `fmla-retaliation-settlement/` — counter window, timeline, figures settled                         | ACCEPTED                             | Medium                                                               |
| C-159 | `va-disability/` — claim plan phases logged                                                       | ACCEPTED                             | **High — this repo is actively changing**                            |
| C-160 | A prior run burned 4.78M tokens on a failed VR&E research run                                     | ACCEPTED                             | Low (historical)                                                     |
| C-161 | Dual-Mac fleet: M4 Pro 48GB + M5 Air 24GB                                                         | ACCEPTED, **but see C-151 REFUTED**  | Low                                                                  |
| C-167 | No routing discipline currently                                                                   | ACCEPTED                             | **High — likely changed since audit**                                |
| C-168 | Token allocation 40–50% routine / 25–30% multi-file dev / 15–20% research / 5–10% judgment        | ACCEPTED as estimate                 | **High — and §4 Stage 7 depends on it. Re-measure before acting**    |
| C-190 | recovery-platform: 5 products, 1,954 files, ~387K lines                                           | ACCEPTED                             | High                                                                 |
| C-191 | recovery-platform has Maestro + Detox e2e flows                                                   | ACCEPTED                             | Medium                                                               |
| C-192 | recovery-platform CI: zero automated test pipeline, only AI code review                           | ACCEPTED                             | **High — §4 Stage 2 depends on this. Verify before acting**          |
| C-193 | CLAUDE.md at root and per-product; swarm hooks wired (`swarm-notify.sh`)                          | ACCEPTED                             | Medium — the swarm hook is on the delete list                        |
| C-194 | Angular 9 in `regroup/web` is "the most expensive context to load"                                | ACCEPTED                             | Medium                                                               |
| C-195 | rag-system: 688 files, 290 TS, pnpm monorepo                                                      | ACCEPTED                             | High                                                                 |
| C-196 | rag-system has real CI (`ci.yml`, `e2e.yml`)                                                      | ACCEPTED                             | Medium                                                               |
| C-197 | rag-system: active dev, Railway, Sentry, foundation for the CPA KB                                | ACCEPTED                             | High                                                                 |
| C-198 | cpa-consulting: pure Markdown, no build, no tests; Aug-1 engagement start                         | ACCEPTED                             | **Expired — the Aug-1 date is today**                                |
| C-199 | Spend: Max $200/mo flat, Opus for planning, Sonnet for implementation, no routing discipline      | ACCEPTED                             | High                                                                 |
| C-200 | recovery-platform: NO `ci.yml`, only `claude.yml` and `claude-code-review.yml`                     | ACCEPTED                             | **High**                                                             |
| C-201 | rag-system: real CI exists; no `EMBEDDING_PROVIDER` in `e2e.yml`                                   | ACCEPTED                             | High                                                                 |
| C-202 | cpa-consulting: no code, no tests, pure Markdown                                                   | ACCEPTED                             | Medium                                                               |
| C-203 | All three repos have CLAUDE.md; none has a Model Tier Policy block                                 | ACCEPTED — **and per C-185 none should get one** | Medium                                                   |
| C-204 | recovery-platform Maestro flows at `e2e-maestro/` and `regroup/mobile/maestro/`                    | ACCEPTED                             | Medium                                                               |
| C-205 | OpenRouter is NOT yet configured anywhere                                                          | ACCEPTED — **and §4 Stage 7 says leave it that way until the signal fires** | High                                          |
| C-208 | `regroup/web` uses Angular 9 with `--openssl-legacy-provider`; excluded from CI                     | ACCEPTED                             | Medium                                                               |

**Recommendations that depend on a repo fact that may have changed:** §4 Stage 2 (depends on C-192 /
C-200 — verify no CI exists before building one), §4 Stage 7 (depends on C-168's task-mix estimate
and C-205's "OpenRouter not configured"), and `harness-blueprint.md` §2's delete list for the swarm
hook (depends on C-193). **Re-audit before acting on any of the three.**

### 2.8 Contradiction resolutions — decision + flip condition

**X-01 — Multi-agent fan-out: banned pattern or flagship feature?**
**RESOLVED: they are different patterns.** W1 and W3 reached this independently on different
evidence. Anthropic's warning targets *parallel decomposition across many workers* on breadth-first
decomposable work (3–5 subagents each running 3+ tools in parallel, ~15x tokens). A Builder/Judge
loop is two roles, sequential, bounded, on one artifact — matching a **Writer/Reviewer pattern
Anthropic's own current docs recommend**. Supporting measurement: reviewer-guided revision raised
SWE-bench resolve rate 27.5%→52.6% (weak generator) and reached a 38.4% resolve rate at **2.44
average samples versus 8.9 for independent parallel resampling** — the sequential loop was *more*
token-efficient than fan-out-style resampling.
**Decision: build the Writer/Reviewer pattern. Do not build fan-out.**
**Flips if:** a controlled comparison of fan-out vs. bounded Judge loop on identical tasks, measuring
both token cost and defect-catch rate, finds fan-out superior at matched compute. **No such study
exists on either side.** Also flips *against the Judge* if the reviewer is routed to a
same-family/cheap model — see X-03b and §3.4.

**X-02 — Cost architecture and the three unreconciled ratios.**
**TESTED, decision rule delivered rather than a verdict.** The 80/15/5 split ties to no measured
result anywhere; neither do 70/30 or A/B/C. The decisive fact is structural: **tiered per-token
routing optimises API/pay-as-you-go spend and has no bearing on Max-subscription spend, which is flat
regardless of model mix below the cap.**
**Decision:** Max 20x as the interactive backbone. Metered routing applies only to (a) the
post-2026-06-15 programmatic/Agent-SDK credit pool and (b) genuine pay-as-you-go usage. Where a
taxonomy is needed for the operator's *actual* mostly-non-coding mix, **A/B/C (Judgment / Generation
/ Bulk) is the better-fitted starting point than 80/15/5** — a coding-shop taxonomy whose "execution
tier" examples (test stubs, boilerplate, linting) do not decompose research work — while remaining
equally unvalidated externally.
**Flips if:** monthly API-equivalent spend *outside* the subscription exceeds ~$150–200/mo (the
order-of-magnitude threshold at which routing setup and debugging hours are plausibly repaid — **this
threshold is derived, not measured**), or if Anthropic introduces metered Max billing.

**X-03 — Ceremony level.** ⚠ **This is a collision between workstreams and it is adjudicated, not
averaged.**
W1: unresolved, no controlled comparison exists, and the load-bearing "40% token reduction" could not
be corroborated. W4: **it resolves on an axis neither corpus position considered — existence vs.
elaboration.**
**Decision: adopt W4's axis.** W4 carries materially stronger sources: a purpose-built benchmark from
ETH Zurich + LogicStar (CTXBench, 138 instances, 12 repos with developer-committed context files,
four models, two benchmarks, extensive ablations) and a 1,650-session pre-registered factorial with
**affirmative-null Bayes factors** (BF10 = 0.096 for size, 0.053 for conflict) rather than mere
failures to reject. W1's null is not overturned — **it is consistent with W4's axis**: W1 found no
break-even for *ceremony*, and W4 explains why (elaboration has no measured effect to break even
against).

- **Existence pays enormously:** 0 of 1,669 functions complied without a CLAUDE.md (Wilson 95% upper
  bound 0.73%); 54.9–67.7% with one; chi2 = 534.27, p = 3.3e-118, **Cohen's |h| = 1.93**.
- **Elaboration pays nothing:** size (25–500 lines), position, file architecture, and inter-file
  conflict all null. A contradicting instruction in an adjacent AGENTS.md did not measurably override
  the primary file (+0.33 pp, p = 0.912).
- **And files ratchet:** median 57 words added per commit vs. under 15 deleted (~4:1), 67.4% of files
  modified in multiple commits, median Flesch Reading Ease 16.6.

**The rule: a content test, not a length budget.** Keep a line only if nothing else in the repository
states it.
**Flips if:** the file exceeds 500 lines (McMillan's null is explicitly bounded there), or carries
more than ~150 instructions (where IFScale's primacy bias peaks), or the repository genuinely has no
other documentation (the one ablation where context files helped, +2.7%).
**Also flips if** someone finally measures the outcome that would justify instruction files — code
quality, security, style conformance, documentation accuracy. **Nobody has.** "Context files don't
help" currently means "context files don't help you close more tickets."

**X-03b — W4 contradicts Anthropic's own documentation, and that framing is preserved.**
Anthropic asserts verbatim that "Bloated CLAUDE.md files cause Claude to ignore your actual
instructions!" and recommends "target under 200 lines per CLAUDE.md file." **The only controlled
factorial test of that proposition finds affirmative-null Bayesian evidence against it across
25–500 lines, and the vendor supplies no data.** W4 flagged the tension rather than deferring, and
this report does the same: **the vendor is authoritative on its own product's mechanisms and
unsourced on this effect.** The counterweight is stated honestly in §7 CA-2 — the refuting study is a
single-author, single-affiliation, unreviewed preprint with a trivial dependent variable.

**X-04 — Where the bottleneck is.**
**RESOLVED in favour of review capacity.** W9 carries Tier A field evidence; W5 explicitly deferred
the capacity question as outside cost data. Position B (cost/routing) is **unfalsifiable as written**
— it never defines a success metric that could reveal the review failure it would cause. In the
field study, throughput rose 2.09x, substantive review fell 39%→21%, silent approvals roughly
doubled, and **the median reviewer's commented reviews stayed flat at ~3/month** — everything above
the constant became rubber stamp — while **merge rate stayed flat and revert rate went slightly
down**. A cost-and-velocity dashboard would have shown the program succeeding.
**Decision: substantive-review share is the governing throttle.** Cost optimisation is permitted only
downstream of it.
**Flips if:** monthly output falls below a volume floor where everything is substantively reviewed
within available hours — then whatever else is scarce binds, and that may be spend. **No evidence
establishes where that floor sits for one person; it is the one gap self-instrumentation can close
in four weeks** (§6).
**Note what does *not* survive:** C-084's "3+ concurrent sessions." There is no measurement anywhere
of a per-person concurrent-session ceiling, and the widely-repeated 3–5 is a vendor *floor* inverted
into a ceiling.

**X-05 — $800 vs $1,600.**
**RESOLVED: $800/93% is correct.** The primary source reports a peak month at "$5,623 API equivalent
on a **$100 monthly subscription**" — i.e. Max 5x for at least part of the window, consistent with
~$800 across 8 months and inconsistent with a constant $200/mo. **v1.md substituted its own assumed
$1,600 (8 x $200) for the practitioner's actual reported total**, and two downstream documents then
treated the derived $13,400/89% as settled fact. C-099, C-100, C-139 refuted.
**Flips if:** the primary author publishes a month-by-month plan history contradicting the
plan-switching inference (confidence on the *mechanism* is medium; on the *figure*, high).

**X-06 — The benchmark winner flips by benchmark.**
**PARTIALLY RESOLVED: different constructs, and neither cited configuration is current.** SWE-bench
Pro evaluates multi-file repository-level issue resolution across 41 professional repos;
Terminal-Bench 2.1 evaluates broader agentic terminal competence including sysadmin, security, and
data-science tasks. SWE-bench Pro is the closer proxy for the operator's work — **but the corpus's
own assertion of that has no independent citation.** More decisively: on the same leaderboard the
corpus cites, **"Claude Code + Fable 5" at 83.8% already outscored "Codex CLI + GPT-5.5" at 83.1%**
at the same snapshot, so the comparison was incomplete the day it was written. Both are now
superseded (GPT-5.6 Sol 85.77%, Claude Opus 5 84.64%, 2026-07-31).
**Decision: treat any benchmark table without an explicit as-of date as expired on arrival.** A tool
choice built on a benchmark comparison is a wasting asset from the day it is written.
**Flips if:** a same-vendor configuration falls materially behind on a benchmark that matches your
own task shape *and* the gap persists across two independent trackers for a full quarter.

**X-W7-A (new, surfaced in Phase B) — "fix the process first" vs. "automate the happy path."**
**CHARACTERISED, NOT RESOLVED — and deliberately so.** Neither side has a controlled study; they are
not measuring the same dependent variable (end-to-end process outcomes vs. time to first delivered
bot). The construction this report adopts is narrower than either camp and does not require the
untested maxim:

> Automation of a step that is not the constraint, or whose elapsed time is dominated by queueing,
> cannot produce a benefit the client will perceive — regardless of how well the automation works.

**Flips if:** a matched-pair or stepped-wedge comparison of standardise-then-automate against
automate-as-is is published, measuring **24-month total cost of ownership and rework rate rather
than go-live date.** Full treatment in `playbooks/process-diagnosis.md` §4.

### 2.9 Cross-workstream convergences

Stronger than any single finding, because the agents could not see each other's work.

1. **X-01 settled twice, independently** (W1 architectural, W3 empirical).
2. **Client separation required by two independent layers** — harness mechanics (W2: every
   cross-project context mechanism is simultaneously a leak path, and user-scope imports load without
   an approval dialog) and contract law (W8: residuals clauses cover only *unaided memory* and
   explicitly exclude recorded material, so a per-client knowledge repo has **no contractual
   protection at all**).
3. **Unsourced numbers propagate everywhere — five workstreams caught it.** W1 ("DeepSeek V4"
   resolves to no model), W2 (a vendor re-serving its own blog as third-party validation), W5 ($1,600
   was an assumption presented as data), W7 (a 2016 marketing brochure behind 10 citations, with a
   population explicitly selected on failure), W9 (two cited "studies" that exist nowhere outside the
   pages citing them). **This is a property of the wider literature, not just this corpus.**

---

## 3. The operating system

### 3.0 The default workflow

One loop. Everything else is a variant of it.

| Phase           | Entry criteria                          | Activities                                                    | Artifacts                        | Automated gates                                 | Human checkpoint                              | Exit test                                                                  |
| --------------- | --------------------------------------- | ------------------------------------------------------------- | -------------------------------- | ----------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------- |
| **0. Frame**    | A task exists that is not one sentence  | Write the goal and the check that will prove it                | `GOAL` line or `SPEC.md`         | none                                             | You write it                                   | A machine-checkable success signal is named. If none exists, say so explicitly and accept manual verification as the gate |
| **1. Explore**  | Goal written                            | Read-only investigation, delegated to a subagent if broad      | Findings summary in-session      | none                                             | none                                           | You can state what will change and where, without opening a file            |
| **2. Plan**     | Explore complete                        | Plan mode. For a change describable in one sentence, **skip 0–2 entirely** | Plan in-session                  | none                                             | Approve the plan                               | The plan names files and the verification step                              |
| **3. Execute**  | Plan approved                           | Implement                                                     | The diff                          | Formatter on write; secret-scan block            | none                                           | Work complete per plan                                                     |
| **4. Verify**   | Execution complete                      | Run the check                                                 | Test/build output                 | **Stop-hook gate** (code) or write-boundary check (knowledge) | none                            | The check passes **without the agent having modified the check**            |
| **5. Review**   | Verify passed                           | Fresh-context reviewer subagent, then **you open the diff**    | Review notes                      | Reviewer subagent (frontier tier, narrow mandate) | **Substantive review — mandatory, logged**    | **You opened the diff and wrote a note.** No note, no merge                 |
| **6. Commit**   | Review complete                         | Commit; append to `substantive-review-log.md`                  | Commit + log line                 | none                                             | none                                           | The log line exists                                                        |
| **7. Handoff**  | Session ending or switching project     | Update `CHECKPOINT.md`; `SessionEnd` archives transcript       | `CHECKPOINT.md`                   | `SessionEnd` hook                                | none                                           | A cold `start.sh` run reconstructs the working state                        |

**The one non-negotiable:** phase 5's human checkpoint. Throughput that outruns it is a defect, not
a gain, and the field evidence shows the failure is *silent* — outcome metrics stay green while
review hollows out.

**Why phase 0–2 is skippable.** Anthropic's own docs recommend skipping planning for a change you
"could describe in one sentence." That is the middle path, and it is itself evidence against a single
universal ceremony level.

### 3.1 Variant A — Code project

| Phase | Differences from the default                                                                                                                                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | The check is a test. Write it first where the change is a bug fix or a new behaviour — agents introduce regressions and **have been measured deleting, weakening, and hardcoding tests to make suites pass**                     |
| 3     | Worktree per lane. Native `claude --worktree <name>`; `.worktreeinclude` carries `.env` in. **Lane count is governed by phase 5's log, not by a number** — no source documents a ceiling, and the vendor's guidance is a floor  |
| 4     | Stop-hook gate on tests/build. **Cap the unattended run**: the visible-vs-held-out test gap grows ~28 points per tenfold increase in code size, so reward-hacking risk is concentrated in exactly the long tasks you want to leave running |
| 4     | Unattended work runs **sandboxed at the OS level** — mount only the project directory, no home dir, no SSH keys — with per-task commits so the morning review is a git review, not an archaeology dig                            |
| 5     | Reviewer subagent at frontier tier with the correctness/requirements-only mandate                                                                                                                                               |
| 6     | CI per `playbooks/harness-blueprint.md` §7. **Price any AI step against the separate post-2026-06-15 credit pool**                                                                                                              |

**Exit test:** tests green, reviewer flags triaged, **diff opened and noted**, CI green, log appended.

### 3.2 Variant B — Knowledge / documentation project

**There is no oracle here.** Every controlled study in the documentation literature borrows its
oracle from a compiler or a test suite. This variant substitutes checks that have measured precision
characteristics, and states where they do not.

| Phase | Differences from the default                                                                                                                                                                                                                                        |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | The check is **not** a test. It is: every new assertion carries source + retrieval date + confidence + change-vs-previous (the ICD 203 clause — the only one of four mature provenance standards that addresses assertion-level dating)                              |
| 1     | Grep and a partitioned index (~250 units per domain + index file), **not** a semantic pipeline. BM25 is a hard baseline; graph/semantic advantages are a *scaling* property. **No study evaluates retrieval at a few-hundred-document scale, and none compares semantic search against plain grep at any scale** |
| 3     | Type-first directory taxonomy, topics in frontmatter. Format does not affect accuracy (chi2 = 2.45, p = 0.484) but does affect cost — Markdown costs +7% to +105% more tokens than YAML per grep hit                                                                  |
| 4     | Write-boundary check (PostToolUse hook or pre-commit) on the provenance schema. **Conventions cannot be held by an instruction file across a long run** — same 5.6%-per-function decay mechanism                                                                     |
| 5     | Citation verifier + consistency checker, **human-in-the-loop, never unattended, tuned for precision.** Naive prompting flags 98% of items at F1 0.22 against an ~11% real base rate; a checker with a 30% noise rate is one you will stop reading                     |
| 6     | Docs CI: links, anchors, redirects. **Know that none of it can detect a well-formed sentence that is false**, and check the defaults — Sphinx nitpicky has not failed the build under `-W` since 1.6; Docusaurus `onBrokenAnchors` only warns; lychee fragment checking is off by default |

**Exit test:** provenance schema satisfied on every new assertion, citation verifier run with flags
triaged, consistency checker run, **document opened and noted**, docs CI green.

**Honest scoping:** contradiction detection over prose is measurable, common, and **beyond reliable
automation** — the best fully automated detector reaches 75.1% AUROC, while human-in-the-loop let
editors find **64.7% more inconsistencies in the same time**. Design for the loop, not the automation.

### 3.3 Variant C — New-client discovery engagement

Full specification in `playbooks/engagement-playbook.md` (E0–E7). The operating-system-level
differences:

| Element             | Difference                                                                                                                                                                                                                     |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Binding constraint** | **Human presence, not review capacity.** The interview, the walk, and the decision-rights conversation are serial and non-delegable. Diagnosis engagements cannot be run three-at-a-time the way worktrees can              |
| **Gates**           | ISO 20700's three: contracting → execution → closure. **Not** a self-invented five-phase model                                                                                                                                 |
| **Automated gates** | Secret-scan block; the applicable data instrument executed before any tool touches client material                                                                                                                             |
| **Human checkpoint**| Every interview, the walk, the constraint identification, the kill decisions, the E5 presentation with the decision-maker present, and the E7 de-identification review                                                          |
| **Exit test**       | `playbooks/engagement-playbook.md` §12                                                                                                                                                                                         |
| **Repo**            | Per-client, isolated from every leak path in `playbooks/harness-blueprint.md` §9. One-way flow only                                                                                                                             |

### 3.4 The composed cheap-tier rule (adjudication 3)

W3 and W5 are **not** contradictory; they compose:

> **Route the reviewer to frontier-class capability. Under a flat subscription this costs nothing —
> token cost below the cap is not a marginal cost, so routing the Judge cheap saves nothing you are
> actually paying. Where work *is* metered (the post-2026-06-15 Agent SDK / `claude -p` / GitHub
> Actions credit pool, or genuine pay-as-you-go), route cheap only where the work is mechanical and
> spec-complete — never the reviewer role.**

Supporting: self-review shows measurably reduced recall vs. cross-model review; "not all reasoning
models perform equally at code review"; LLM judges exhibit negation blindness; OpenAI's critic was
built on GPT-4-class capability *because* subtle bugs need reasoning capacity. And the most detailed
practitioner data point ran **~95% Opus** and was cost-effective anyway, precisely because flat-rate
billing made the mix irrelevant.

---

## 4. Adoption sequence

**No stage may be justified by "best practice" alone.** Each has a bottleneck signal that triggers
it, a success benchmark for advancing, and a kill criterion for backing out. **Stage 0 is first
because the evidence says so:** in the one field study, review-side damage accrued *during* the ramp,
which makes the corpus's own ordering — weekly review sequenced last (C-189) — the sequencing the
evidence argues against.

| Stage | What                                                        | Bottleneck signal that triggers it                                                                                              | Success benchmark to advance                                                                    | Kill criterion                                                                                                                                                          |
| ----- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0** | **Substantive-review log.** One line per merged unit: did you open it, did you write a note | **Unconditional.** The signal is that you cannot currently state what fraction of merged work you actually read              | 4 consecutive weeks of entries, and a stated baseline share                                     | Logging costs >10 min/week, **or** you catch yourself back-filling entries. Then fall back to a purely instrumented proxy (was the diff opened, for how long) and stop self-rating |
| **1** | **Subtraction pass.** `harness-blueprint.md` H0–H2 + the delete list | `/context` shows instruction files consuming a material share of the window at session start, **or** you find a rules file asserting something false | Token delta at session start recorded, and **no convention regression over 2 weeks**            | A convention regresses that a deleted line was holding. **Restore it as a hook, not as prose** — if it cannot be a hook, restore the line and record why                    |
| **2** | **Minimal hook set + verification gate.** `harness-blueprint.md` H3 | You merged something whose tests you did not see pass                                                                       | Zero unverified merges over 4 weeks; every hook fires in <2s                                     | Hook latency exceeds 2s, **or** 8-consecutive-block overrides start occurring (the gate is stuck, not converging). Remove the hook rather than working around the override  |
| **3** | **Fresh-context reviewer subagent**, frontier tier, narrow mandate | A defect class reached main that a second read would have caught                                                            | Substantive-review share **holds ≥90% while throughput rises**                                  | >30% of reviewer flags are noise you ignore. Tighten the mandate **once**; if it recurs, remove the subagent — an over-flagging reviewer you stop reading is worse than none |
| **4** | **Cross-project startup recipe + `CHECKPOINT.md`.** `harness-blueprint.md` H6 | You spent >15 minutes reconstructing a multi-project session after a resume                                                | The cold-start test passes for every active project                                              | The recipe drifts and fails the cold-start test twice. Collapse to single-project sessions — **the desired topology is not supported and no amount of tooling fixes that** |
| **5** | **Client-repo separation + data instruments.** `engagement-playbook.md` §10, `harness-blueprint.md` §9 | First client engagement                                                                                    | Leak-path table all clear; the applicable instrument executed before any tool touches material  | **The kill criterion is the engagement, not the stage.** If the instrument cannot be executed, decline the work                                                              |
| **6** | **Citation-verification harness** on the labelled VA corpus. `harness-blueprint.md` §11 | A citation defect reached a client-facing document, **or** you want a productised offer with a measured claim behind it     | Measured **precision ≥0.80** on the labelled set (40 known misstatements of 109)                | Precision <0.70 after two tuning passes. Stop and do manual spot-check sampling instead — an unusable checker is worse than a known-manual process                            |
| **7** | **Metered-tier routing** (conditional, and probably never)  | Monthly API-equivalent spend **outside** the Max subscription exceeds ~$150–200/mo — i.e. the Agent-SDK credit pool or real pay-as-you-go | Measured spend reduction **with no increase in escaped defects** over 4 weeks                | Any quality regression, **or** setup + debug hours exceed dollars saved. **This stage is off by default.** Its threshold is derived from order-of-magnitude reasoning, not measured |

**What is deliberately absent from this sequence:** OpenRouter configuration, Tier Policy blocks,
Hermes/Manifest, a two-machine tier split, multi-agent swarm hooks, mutation testing, contract
testing, visual diffing, and an MCP memory server. Each is either refuted, unsupported, commoditised,
or has no named present bottleneck. See `playbooks/harness-blueprint.md` §2.

---

## 5. Risk and volatility register

### Likely to change within 6 months

| Item                                                                                | Risk                                                                                                                            | Mitigation                                                                            |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Benchmark leaderboards**                                                          | Every figure in §2.1 was superseded within weeks to months. Two fetches of the same tracker during Phase B returned different numbers | Treat any benchmark without an as-of date as expired. Never build a tool choice on one |
| **Rate limits**                                                                     | The +50% weekly boost has been extended repeatedly (May 13 → Jul 13 → Jul 19 → Aug 19). **W5 found no source dated after 2026-07-13 confirming current status** | Re-check before any quota-dependent decision                        |
| **Model pricing**                                                                   | Sonnet 5's introductory $2/$10 reverts to $3/$15 on **2026-08-31** — guaranteed drift within a month of this report               | Re-derive any dollar figure at use time                                                |
| **Claude Code version-gated behaviour**                                             | W2 recorded behaviour changes at ~14 distinct versions within one research pass                                                    | `/doctor` + changelog before treating any flag as load-bearing                          |
| **Agent Teams**                                                                     | Experimental, disabled by default, with tools already removed in the changelog                                                     | Do not build on it                                                                     |
| **Third-party orchestrator pricing/platform**                                       | Conductor's tiers were read 2026-08-01; assume stale within a quarter. Its Pro tier adds a **cloud workspace**, changing data residency | Re-verify before any client engagement                                          |
| **Vendor terms**                                                                    | Anthropic Commercial Terms are stamped 2025-06-17. Industry data-handling terms change materially and repeatedly                    | Re-verify before every regulated-data engagement, and check which product tier applies |
| **_Kahn v. Anthropic_** (No. 3:26-cv-05763, filed 2026-06-14)                        | Active, unresolved, no certified class. Alleges Max delivers less than advertised                                                  | Watch. Do not treat allegations as findings                                            |
| **SPI benchmark figures**                                                           | Calendar-2024 data published 2025-02; **the 2026 edition already supersedes them**                                                 | Re-check before quoting any delivery baseline                                          |

### What the recommendations depend on that could break

| Dependency                                                    | If it breaks                                                                                                             |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Flat-rate subscription billing**                            | The entire X-02 decision inverts. Metered Max billing would make tiered routing suddenly relevant to interactive work     |
| **Hooks remain deterministic**                                | The whole "move enforcement out of prose" strategy rests on it. The 8-block override is already a documented soft spot    |
| **`--add-dir` reach within a live session**                   | If removed, even the degraded cross-project story collapses to one repo per session                                       |
| **McMillan's factorial result**                               | Single author, single affiliation, unreviewed, trivial dependent variable, single-turn `--print` mode. **Independent replication does not exist.** If it fails to replicate, the content test loses its strongest support (but not the cost finding, which is a different group) |
| **Repo facts C-168, C-192, C-200, C-205**                     | Stages 2 and 7 are built on them. Re-audit before acting                                                                  |

### Anecdote-grade claims that appear in this report

Stated so they are not mistaken for measurements:

- The **22 days / 17 minutes** touch-time datum: one insurer, second-hand, 1990, **no distribution
  behind it**. The *logic* is arithmetic; the *number* is an anecdote.
- The **Redelinghuys** cost anecdote: one practitioner, self-reported, not third-party audited. **The
  entire subscription-arbitrage argument in the corpus rests on this single data point** — no second
  full-detail case study exists.
- **Ford 20% vs 75%** headcount reduction: n=1, consultant-reported, and the 20% is a projection never
  executed.
- The **mabl 40%→<5%** context-drift figure: self-reported, no operational definition, five bundled
  interventions, and being laundered through a vendor blog.
- **Meta-repo pattern**: three convergent implementations, **zero metrics** among them.
- **Every documented personal operating system** (GTD, Personal Kanban, BASB, Slow Productivity): all
  Tier C, none empirically validated; GTD's own reviewers state "no academic papers have investigated
  this method."
- **Percy's "3x review time reduction / ~40% fewer false positives"**: vendor figures with no
  independent audit.

---

## 6. Open questions

Each with the cheapest experiment that would resolve it. Items marked with an arrow are within the
operator's own reach.

| #  | Question                                                                              | Cheapest resolving experiment                                                                                                                                                  |
| -- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 →| **Where does the cost-vs-review crossover sit for one person?**                       | Log units merged, units substantively reviewed, and review minutes, for four weeks. This is Stage 0 and it is the single gap self-instrumentation closes fastest                |
| 2 →| **Does a `CONTEXT.md` per subject help or hurt?** (C-140 UNVERIFIED, C-142 REFUTED)   | One day. Run the same research task on two subject directories, one with and one without, and compare `/context` token counts and output quality. **Nobody has published this because nobody outside this use case cares** |
| 3 →| **Does a written question statement reduce token spend?** (C-145 UNVERIFIED)          | One afternoon. Same research question twice against the same corpus, with and without `QUESTION.md`, with harness token accounting                                              |
| 4 →| **What is the operator's actual 80/20 reuse ratio?**                                  | `engagement-playbook.md` §7's per-artefact log, read at engagement 4. **The ratio has zero evidence base anywhere** — no study measures it                                      |
| 5 →| **Can a narrow, single-domain citation checker beat the ~80% general ceiling?**        | The VA corpus already has 40 known misstatements out of 109 — a labelled set with a base rate. Measure precision and recall. **The only place in this whole programme where the operator can generate evidence that does not exist anywhere** |
| 6 →| **Do frontier models actually fail at process modelling?**                             | The 105-pair BPMN benchmark protocol is published and cheap to re-run. **No frontier proprietary model has ever been benchmarked on it** — only open-source models to 405B      |
| 7  | **Optimal concurrent-lane count for a solo reviewer**                                  | A within-operator A/B over ≥4 weeks logging time-to-first-review, review minutes per merged change, and post-merge defects at 1/2/3/5 lanes. **Every published number is assertion** |
| 8  | **Does cultural consensus theory give a usable domain-calibration instrument?**        | A literature check, not a study. W6 exhausted its budget before verifying the method's sample-size properties. **The highest-value unclosed item in the consulting half**       |
| 9  | **Does standardise-then-automate beat automate-as-is?**                                | Matched-pair or stepped-wedge, measuring 24-month TCO and rework rate, not go-live date. **Neither side of the debate can currently appeal to outcome data**                     |
| 10 | **Is there a threshold for "standardised enough"?**                                    | A dose-response study of exception rate against automation maintenance cost. **Until it exists, any percentage quoted for this is invented**                                     |
| 11 | **Do instruction files improve code quality, security, or documentation accuracy?**    | Nobody has measured the outcome that would justify them. Named as explicit future work by the researchers who measured the null on task success                                  |
| 12 | **Does the meta-repo registry itself drift?**                                          | Not addressed by any of its three independent authors — and a 4:1 add/delete ratio says it will                                                                                 |

### What Phase B left underdone

Five workstreams exhausted their web-search budget (W1, W2, W5, W6, W8) and marked the remainder
UNVERIFIED rather than guessing. Highest-value unclosed items, carried forward:

- **Jørgensen's software-estimation literature** (W8) — the obvious adjacent body of work for
  time-boxing, never retrieved. Every time-box in the playbooks is convention as a result.
- **Cultural consensus theory's sample-size properties** (W6) — item 8 above.
- **arXiv 2606.09090, "Context Rot in AI-Assisted Software Development: Repurposing Documentation
  Consistency for AI Configuration Artifacts"** — surfaced twice (W2 and W4), read by neither, and it
  sounds directly on-topic for the drift problem.
- **Copilot Pro/Codex current pricing, Cursor's credit structure, Gemini embedding pricing** (W5).
- **SPI's fixed-price vs. T&M margin comparison** (W8) — paywalled; the single most
  decision-relevant number for contract-type choice.
- **Current status of the +50% weekly rate-limit boost** past its 2026-07-13 stated end date (W5).

---

## 7. Surviving counterarguments

Six recommendations were attacked adversarially. All six survived in weakened form. **These are the
counterarguments that were not defeated.**

**CA-1 — Against Stage 0 (substantive-review share): the metric may not mean anything for a solo
operator.**
In the field study, "silent approval" had social meaning — a reviewer visibly rubber-stamping a
colleague's PR. **In a solo setting there is no second party to whom a review is visible, so the
metric must be self-reported — and self-report about AI-assisted work is unreliable in the optimistic
direction.** METR's developers forecast 24% faster, estimated 20% faster afterwards, and measured 19%
slower. The study also has a reviewer *pool* to dilute; a solo operator has no dilution mechanism,
which cuts both ways.
**Weakening adopted:** the metric is instrumented, not self-rated (was the diff opened, for how long,
was a note written), and the log's kill criterion explicitly fires on back-filled entries. **No
published work validates such a proxy for solo operators.** **This counterargument is not defeated.
It is the reason Stage 0's kill criterion exists.**

**CA-2 — Against the content test: the refuting study is thin, and it measures the wrong outcome.**
The size null rests on a **single-author, single-affiliation, unreviewed preprint** whose dependent
variable is one trivial annotation (`// @tracked`), run in single-turn `--print` mode, not multi-turn
interactive use; the author himself writes that transfer "to more demanding instructions… is an open
question," and calls for replication that does not exist. Two of the three strongest sources in that
workstream share one author — a real concentration risk. Meanwhile Anthropic's own docs assert the
opposite and are the more authoritative source on their own product.
And the cost study measures **task resolution only** — not code quality, security, or style
conformance, which is exactly where instruction files plausibly earn their keep and where nobody has
measured them.
**Weakening adopted:** the recommendation is a content test, **not** "instruction files are useless."
The strongest and least contested leg is the cost finding (different group, purpose-built benchmark,
four models, disconfirming their own field's advice). **Surviving:** if the quality/security/accuracy
outcome is ever measured and instruction files help, the content test is under-restrictive.

**CA-3 — Against pitching on touch-time and arrested scaling: both anchors are weak in different
ways.**
The touch-time datum is n=1, second-hand, 1990, with **no distribution behind it** — so there is no
evidenced threshold for what counts as an alarming ratio. The Deloitte data is 2017 fieldwork,
self-selected large enterprises, and a firm that sells RPA implementation; **it may not describe SMBs
at all**, and pitching "arrested scaling" to a client with zero bots is pitching a problem they do
not have yet.
**Weakening adopted:** touch-time is deployed as a **diagnostic on the client's own data**, not as a
benchmark comparison — its validity does not depend on the 1990 anecdote generalising. Arrested
scaling is offered only as a *correction* when a client cites failure statistics, not as the opening
frame. **Surviving:** the fix-first position the whole diagnosis playbook orbits has **zero outcome
evidence**, X-W7-A is genuinely unresolved, and the "standardised enough" threshold does not exist.
The playbook's construction (Gates 1 and 2 only) is deliberately narrower than the maxim for exactly
this reason, and it is still a construction.

**CA-4 — Against building the Judge/Builder loop: the operator is in the regime where it helps
least.**
The strongest supporting study measured **+25 percentage points for a weak generator (27.5%→52.6%)**,
+16 for a mid-tier one, and **only +3.0 points for a strong generator (72.2%→75.2%)**. **The operator
runs a frontier model — the strong-generator regime, where the measured gain was smallest.** Gains
plateau within 4–5 rounds. And no head-to-head study of fan-out vs. bounded Judge loop exists on
identical tasks measuring both cost and defect-catch; the X-01 resolution is architectural, not
empirical, on that narrower point.
**Weakening adopted:** start with the *built-in* Writer/Reviewer pattern (a fresh-context reviewer
subagent with a narrow mandate), and build the fixed-schema auto-triggering Judge skill **only if the
reviewer demonstrably misses a defect class you can name** (Stage 3's benchmark and kill criterion).
**Surviving, and this is the sharpest one:** the marginal value of the whole Judge apparatus for this
specific operator, on a frontier model, may be ~3 points — well inside the noise of a
single-reviewer setup.

**CA-5 — Against the meta-repo: it is meaningful setup with no measurement, and its own authors
hedge.**
It is a design pattern with **three convergent implementations and zero metrics among them**. The
solo author's own caveats: "None of this is a silver bullet"; the "immune system" of agents told to
verify "still requires discipline"; the pattern "may become obsolete as models improve." The only
before/after number in the space (40%→<5%) is self-reported, undefined, bundled across five
interventions, at 25-engineer scale, and is being laundered through a vendor blog.
**Weakening adopted:** the recommendation is reduced to the two cheapest components — a repo-map
table and `repos.yaml` — plus the startup recipe, which is the part that actually addresses the
enumerated resume losses. **Surviving:** **whether the registry itself drifts is unaddressed by every
author**, and a measured 4:1 add-to-delete ratio across 2,303 context files says it will. The
mechanism that would catch registry drift is the same unbuilt environment-assertion linter named in
`playbooks/harness-blueprint.md` §10.

**CA-6 — Against the whole operating system: the review-capacity thesis is enterprise evidence
applied to n=1.**
The Tier A field study is a **single firm, non-randomised rollout, self-described as a "near-best-case
setting — a young, AI-forward firm with uncapped tool budgets,"** and is a preprint, not peer
reviewed. Its mechanism is *pool dilution*, which structurally cannot occur for one person. The
closest transferable number is from a different domain entirely — single-reviewer screening misses a
median 5% of relevant material (13% for a less-experienced reviewer) versus dual review — and that is
a relevance-classification task, not an "is this correct and internally consistent" task. **No study
measures how much analytical prose one person can verify per day before accuracy degrades**, and a
substantial share of the operator's work mix is exactly that.
**Weakening adopted:** the throttle is a *measured local baseline*, not an imported threshold, and
every count-based number (2–3 worktrees, 3+ sessions, optimal-N projects) has been explicitly
dropped. **Surviving:** the direction is well evidenced and the magnitude is unknown for this
operator. Everything downstream of Stage 0 is calibrated against a baseline that does not yet exist.

---

## 8. Sources

Tiered, with why each was trusted. Full per-workstream source lists with URLs and access notes are in
`findings/w1..w9`.

### Tier A — primary, methodologically transparent, or binding

| Source                                                                                     | Why trusted                                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Anthropic Claude Code docs — best-practices, costs, hooks, sub-agents, worktrees, sessions, memory, agent-teams, agents, permission-modes | Primary vendor documentation for the exact mechanics under test; ~10 pages read in full across W1/W2/W3/W4. Trusted for behaviour, **not** for comparative or effect claims |
| He, Agarwal, Denisov-Blanch et al., "AI Writes Faster Than Humans Can Review," arXiv:2607.01904 (2026-07-03) | 802 devs / 196,212 PRs, fixed-effects panel; authors report results that cut against their own framing. Preprint, single firm |
| Gloaguen, Mündler, Müller, Raychev, Vechev, "Evaluating AGENTS.md," arXiv:2602.11988 (ETH Zurich + LogicStar) | Purpose-built benchmark for the exact question; four models, two benchmarks, extensive ablations, disconfirming its own field's advice. Python only |
| McMillan, "Instruction Adherence in Coding Agent Configuration Files," arXiv:2605.10039     | Pre-registered analysis plan, published condition matrix, frozen dataset, affirmative-null Bayes factors, self-undermining limitations section. **Single author, unreviewed** |
| Chatlatanagulchai, Li, Kashiwa, Reid et al., "Agent READMEs," arXiv:2511.12884              | 2,303 files across 1,925 repos; Mann-Whitney U with Cliff's delta throughout                                    |
| Rozenblit & Keil, "The misunderstood limits of folk science," _Cognitive Science_ 26(5) 2002 | 12 studies, non-elite replication, alternative explanations tested and excluded, 898 citations. Read in full     |
| Melumad & Yun, "LLMs versus web search on depth of learning," _PNAS Nexus_ 4(10) 2025       | Preregistered, n=10,462, seven experiments including a content-matched control, explicit null-generalisation caveat by the authors |
| Magesh, Surani, Dahl, Suzgun, Manning, Ho, "Hallucination-Free?", _JELS_ 2025               | Preregistered, published methodology, inter-rater kappa=0.77, unusually explicit limitations, authors have no product to sell. **Data March–May 2024** |
| Chang, Chen, Mellers & Tetlock, GJP training study, _Judgment and Decision Making_          | Randomised assignment, four annual replications, and it reports principles that made accuracy *worse*           |
| Waffenschmidt et al., single vs. double screening, _BMC Med Res Methodol_ 19:132 (2019)     | Peer-reviewed methodological review; conclusion permissive rather than alarmist                                 |
| METR, "Early-2025 AI and Experienced Open-Source Developer Productivity," arXiv:2507.09089  | Pre-registered RCT reporting a result contrary to its own field's expectations; **METR itself flags it as historical.** N=16 |
| Humphrey, Nahrgang & Morgeson (2007), _JAP_ 92(5)                                            | 259 studies, 219,625 participants. The strongest evidence base in the consulting half                            |
| Wewerka & Reichert, RPA systematic literature review, arXiv:2012.11951                      | Kitchenham protocol, 1,510→63 publications, and it reports findings against the field's interest (zero failure cases, hype bias). **Explicitly declined quality assessment** |
| Guest, Bunce & Johnson (2006), _Field Methods_ 18(1); Hennink & Kaiser; Hennink, Kaiser & Marconi | The saturation literature; robust within qualitative methodology, scoped to homogeneous populations       |
| Bainbridge, "Ironies of Automation," _Automatica_ 19(6) 1983                                 | 4,700+ citations, conceptually reproduced across four decades. No effect sizes                                   |
| ISO 20700:2017, _Guidelines for management consultancy services_                             | The only international standard defining a consulting engagement; ISO/PC 280, 48 countries. **Non-certifiable, never evaluated** |
| IMC USA Enforceable Code of Ethics                                                          | Enforceable, a condition of membership and CMC certification, signed in writing. Binds members, not consultants generally |
| 26 CFR §301.7216-2; 45 CFR §164.504; GDPR Art. 28; FAR 16.104 / 16.601                       | Binding regulation, read directly. FAR is written for a monopsony public buyer — transferability is limited      |
| Semnani et al., "Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia," EMNLP 2025  | Peer-reviewed at a top venue, **authentic** rather than synthetic contradictions, negative headline about automation |
| Xu, Wahab, Holmes, Lemieux, "DocPrism," arXiv:2511.00215; Kiecker et al., "Cascade," arXiv:2604.19400 | Two independent groups, real-world (not synthetic) evaluation, and DocPrism reports its own naive-baseline failure honestly |
| Tan, Wagner, Treude, outdated code-element references, EMSE / arXiv:2212.01479               | Best base-rate and persistence data, trusted partly *because* it reports its own developer-validated false positives |
| Li et al., "AttributionBench," Findings of ACL 2024; Gao et al., ALCE / RARR                  | The ~80% ceiling on automated citation-support checking, plus the operational metric definitions                  |
| Fluxicon, _Process Mining Book_ 3.1 data-suitability                                        | Vendor-authored, but the content is disqualifying conditions that **reduce** the vendor's addressable market       |
| Anthropic, multi-agent research system post (June 2025)                                     | Vendor self-report about its own system. Real, widely cited, **not third-party replicated**                       |
| Sharma et al. (Anthropic), sycophancy, arXiv:2310.13548                                      | Vendor-authored but reports a defect in its own products — passes the "stake in being correct" test               |
| Goddard, Roudsari & Wyatt, automation bias, _JAMIA_ 19(1) 2012                                | Systematic review, 74 studies with meta-analysis. Predates LLMs                                                   |
| Hammer, "Reengineering Work: Don't Automate, Obliterate," HBR 1990                           | Primary source for what Hammer actually wrote, and it discloses its own consulting interest. **Its case numbers are Tier C** |
| llm-stats.com, snorkel.ai, vals.ai, morphllm.com leaderboards                               | Dated, per-entry rows with margins of error; three trackers converged on the same figures — and disagreed with each other at other moments, which is itself the finding |

### Tier B — measured but vendor-published, single-site, or preprint

Deloitte 2018 RPA survey (n=424, disclosed method, figures cutting against the publisher's interest —
**the only defensible numbers in the automation-failure field**, 2017 fieldwork) · SWE-Review
arXiv:2607.06065 · SpecBench arXiv:2605.21384 · "Do Coding Agents Deceive Us?" arXiv:2606.07379 ·
LLM-as-a-Judge review arXiv:2510.24367 · Faros AI telemetry (22,000 devs; **vendor selling the
remedy**) · SmartBear 200–400 LOC (**vendor-run ~2006 Cisco study, never independently replicated**)
· ksred.com cost tracker + pricing guide (**the single practitioner data point the entire arbitrage
argument rests on**) · SPI Research 2025 Benchmark (n=403; self-selected, self-reported financials,
PSA-vendor sponsored, **headline figures are ratios of ratios**) · mabl engineering blog · seylox
meta-repo pattern · Mabin & Balderstone TOC meta-analysis (**zero failures found — effect sizes are
upper bounds**) · VSM systematic review (**every included study uncontrolled before/after**) ·
Venable / Wyrick Robbins residuals analyses (**all written from the disclosing party's perspective**)
· Chroma "Context Rot" · McMillan structured-context arXiv:2602.05447 · The Register on Anthropic ToS
enforcement · Kipping et al. SME process mining · rustman.org orchestrator survey · Camarate on
cross-lane drift · Heylighen & Vidal on GTD (**trusted specifically for stating GTD is empirically
uninvestigated**)

### Tier C — used only where nothing better exists, and labelled at every use

EY 2016 "Get ready for robots" (**read in full solely to establish the 30–50% figure's provenance —
no methodology, population selected on failure**) · Gartner agentic-AI forecast (**a prediction,
routinely mis-reported as measurement**) · MIT NANDA "95%" (**contested; undisclosed conflict**) ·
Consulting Success fee survey (**undated, self-selected from the publisher's own coaching audience**)
· Osmani essays · Dzombak · Anthropic power-user tips 3–5 (**self-described collected anecdote; a
floor, not a ceiling**) · every parallel-session practitioner blog · Percy/Applitools visual-diff
figures · Personal Kanban / Slow Productivity / BASB / GTD prescriptions · Kevin Davison's
knowledge-base case study · karun.me multi-repo layout

### Rejected — do not cite

- **firmem.com/Practiq** and **pharallax.ai** solo-consultant capacity benchmarks, attributed to a
  "Kennedy Research 2024 Independent Consultant Survey" and an "SCIP 2024 Solo Consultant Study."
  **Neither study is traceable anywhere outside those pages.** Fabricated citations.
- **riftmap.dev** on cross-repo context — vendor marketing recycling mabl's, Meta's, and a solo
  operator's numbers to sell the author's own API. Cited in `findings/w2` only to document the
  laundering path.
- Unsourced knowledge-base statistics: "75% of APIs drift from their specs," "20–40% of knowledge
  bases contain irrelevant articles," "product documentation holds for 90 days," "teams lose 25% of
  their time hunting for answers," "GPT-3.5 55% / GPT-4 18% fabricated citations." None resolves to a
  primary source.
- "Copilot code review reads only the first 4,000 characters of instruction files" — contradicted by
  a June 2026 changelog announcing removal of the limit.

---

## 9. Consulting/dev balance check

Required by the phase spec before shipping: confirm the engagement methodology (W6–W8) has as much
substance behind it as the tooling (W1–W5).

| Half            | Findings-file lines | Sources read **in full** | Tier A primary sources                                                                                                                                    |
| --------------- | ------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tooling (W1–W5) | 2,674               | 33                       | Anthropic docs x10, three benchmark trackers, ETH Zurich purpose-built benchmark, McMillan factorial, platform pricing                                       |
| Consulting (W6–W9) | 2,604            | 26                       | ISO 20700 full text, IMC Code, three binding regulations, FAR x2, Rozenblit & Keil, PNAS Nexus n=10,462, GJP training study, Humphrey meta-analysis (n=219,625), RPA SLR, Bainbridge |

**PASS.** The consulting half reads *more* primary regulation and standards material and carries the
single largest-N study in the whole programme. It is thinner on *measured outcomes* — but that is a
property of the field, established here as a finding (productization has no outcome evidence; ISO
20700 has never been evaluated; SIPOC/RACI/MECE have none of any kind; the fix-first maxim has never
been tested), not a shortfall of this pass. It is reported as such rather than papered over.

---

## 10. Acceptance criteria check

| Criterion                                                                             | Status                                                                                                                                                                              |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Every claim in the Phase A ledger appears in the reconciliation ledger with a verdict  | **PASS** — 186 claim rows in §2.1–2.6, 25 REPO-FACT rows in §2.7, total 211                                                                                                         |
| All contradictions from ledger §3 have a stated decision plus flip conditions          | **PASS** — X-01 to X-06 plus X-03b and the newly surfaced X-W7-A, all in §2.8, each with a flip condition                                                                            |
| Both project kinds addressed everywhere a workflow is recommended                      | **PASS** — §3.1/§3.2 variants; `harness-blueprint.md` §10 knowledge-repo variant; hook and CI tables carry a "both project kinds" column; `process-diagnosis.md` marks **[KR]** deviations |
| The consulting half is developed to the same depth as the dev half                     | **PASS** — §9, with the field's outcome-evidence thinness reported as a finding rather than concealed                                                                                |
| Every playbook phase has entry criteria, artifacts, a time-box, and an exit test       | **PASS** — all four playbooks use a six-field phase table (entry criteria / activities / artifacts / time-box / human checkpoint / exit test)                                        |
| Every quantitative claim carries a date, a source link, and an evidence tier           | **PARTIAL** — evidence tiers and dates are carried throughout; **inline URLs were not duplicated into this report**, which routes to `findings/w1..w9` for per-figure links. Flagged, not claimed as met |
| The adoption sequence has a kill criterion for every stage                             | **PASS** — §4, all 8 stages                                                                                                                                                         |
| At least three surviving counterarguments are reported                                 | **PASS** — six (§7)                                                                                                                                                                 |
| Nothing recommended exceeds what one person can review, or it is flagged where it does | **PASS** — Stage 0 gates everything downstream; every count-based lane/session/project number is explicitly dropped; CA-1 and CA-6 flag the residual risk                            |
| Every playbook is usable without editing the parts marked fixed                        | **PASS** — `engagement-playbook.md` §9 enumerates FIXED vs. VARIABLE line by line; the other three mark FIXED sections inline                                                        |
