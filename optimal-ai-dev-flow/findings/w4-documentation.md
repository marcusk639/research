# W4 — Documentation and Knowledge-Repo Coherence

_Phase B findings | Generated: 2026-08-01 | Sources consulted: 44 | Read in full: 5_

> **Do not cite these — encountered and rejected.** "75% of APIs drift from their specs" and
> "contract drift plagues ~70% of API failures" (unsourced content marketing). "20–40% of
> knowledge bases contain irrelevant articles," "product documentation holds for 90 days," "teams
> lose 25% of their time hunting for answers" (vendor blogs, no cited study). "GPT-3.5 55% /
> GPT-4 18% fabricated citations across 42 literature-review topics" and "19.9% of GPT-4o
> citations fabricated" (could not be traced to a primary source). "CodeLLaMA-7B achieves 94.0%
> precision on code-comment inconsistency" (unverifiable course-hosted PDF; and F-W4-12 shows
> synthetic-benchmark precision collapses on real data). "Copilot code review reads only the first
> 4,000 characters of instruction files" (contradicted by the June 2026 changelog announcing limit
> removal). Every figure in the body below either resolves to a primary source I fetched or is
> explicitly marked second-hand.

**Scope note.** Ten ledger claims were assigned here, all of them about instruction/context
files. Per §5 of the ledger, the corpus never addresses documentation quality, doc-drift
detection, fact verification, or code-free knowledge repositories at all. The majority of this
file is therefore open-field research, and a large fraction of it reports honest gaps.

---

## Ledger Verdicts

| Claim ID | Verdict    | Current value / correction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Evidence tier | Source                                                                                    | Notes                                                                                                                                                                                                                                                                    |
| -------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C-034    | CONFIRMED  | Verbatim in current Anthropic docs: _"Keep it concise. For each line, ask: 'Would removing this cause Claude to make mistakes?' If not, cut it."_ (retrieved 2026-08-01)                                                                                                                                                                                                                                                                                                                                                                                             | A (vendor)    | [Claude Code best practices](https://code.claude.com/docs/en/best-practices)              | Accurate quotation. The corpus attributes it correctly. Whether the underlying causal premise holds is a separate question — see C-035.                                                                                                                                  |
| C-035    | REFUTED    | Refuted across 25–500 lines, the band that covers essentially all real files. ICR by size: 60.0% / 65.2% / 67.7% / 64.0% at 25/100/250/500 lines; GLMM χ²=5.16, df=3, p=0.16; **affirmative-null BF₁₀=0.096**. Untested above 500 lines.                                                                                                                                                                                                                                                                                                                             | A             | [McMillan 2026, arXiv:2605.10039](https://arxiv.org/abs/2605.10039) (read in full)        | Vendor asserts it verbatim ("Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"); the only controlled factorial test (1,650 sessions, 16,050 function-level observations) finds affirmative-null Bayesian evidence against it. See X-03.          |
| C-036    | STALE      | Now **five** scopes, not three: managed policy (`/Library/Application Support/ClaudeCode/CLAUDE.md`, `/etc/claude-code/`, `C:\Program Files\ClaudeCode\`), user `~/.claude/CLAUDE.md`, project `./CLAUDE.md` **or `./.claude/CLAUDE.md`**, local `./CLAUDE.local.md`. Imports have a **max depth of four hops** and external imports trigger a one-time approval dialog. `.claude/rules/*.md` (path-scoped via `paths:` frontmatter) and auto-memory (`~/.claude/projects/<project>/memory/`, first 200 lines or 25KB) are additional mechanisms the claim predates. | A (vendor)    | [Claude Code memory docs](https://code.claude.com/docs/en/memory) (read in full)          | The three locations named are still correct; the claim is incomplete rather than wrong. `./.claude/CLAUDE.md` as a project-instruction location matters directly for C-206.                                                                                              |
| C-107    | REFUTED    | Direction is wrong. Measured effect of repository context files is a **cost _increase_ of 20% (SWE-bench) and 23% (CTXBench)** for LLM-generated files and up to 19% for developer-written ones (p < 0.001%), driven by +2.45 and +3.92 agent steps.                                                                                                                                                                                                                                                                                                                 | A             | [Gloaguen et al. 2026, arXiv:2602.11988](https://arxiv.org/abs/2602.11988) (read in full) | No source anywhere supports a 40% token reduction. The same paper found **no correlation between context-file length and either success rate or per-instance cost**, and that the "repository overview" section — exactly what C-107 prescribes — is inert.              |
| C-131    | STALE      | `.cursorrules` is superseded by `.cursor/rules/*.mdc`; current Cursor rules docs do not mention `.cursorrules` at all. Separately, a prose line in CLAUDE.md cannot select the model for the session it is loaded into — model selection is settings/`--model`/subagent frontmatter.                                                                                                                                                                                                                                                                                 | A (vendor)    | [Cursor rules docs](https://cursor.com/docs/context/rules); Claude Code memory docs       | Stale on file format; the enforcement premise is also unsupported — Anthropic states instruction files are "context, not enforced configuration." Efficacy of the specific rule text: **no reliable evidence found**.                                                    |
| C-137    | REFUTED    | Anthropic's own docs state the opposite of the "infrastructure" framing: _"Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead."_                                                                                                                                                                                                                                                                                                                                         | A (vendor)    | [Claude Code memory docs](https://code.claude.com/docs/en/memory)                         | The "degrades into random model selection" consequence is separately **UNVERIFIED** — no study measures model-routing discipline with vs. without an instruction file. Two independent errors in one claim.                                                              |
| C-140    | UNVERIFIED | No study of per-subject context files in code-free repositories exists. Nearest evidence cuts both ways (see F-W4-03).                                                                                                                                                                                                                                                                                                                                                                                                                                               | —             | [Gloaguen et al. 2026](https://arxiv.org/abs/2602.11988)                                  | The only relevant measurement: context files helped (+2.7% avg) **only** in the ablation where all other documentation was stripped from the repo; where documentation already existed they were "redundant documentation." A research subject dir is all documentation. |
| C-142    | REFUTED    | Stated as a verification target, never measured. The closest real measurement runs the other way: context files raised per-instance cost 19–23%, and file length showed no relationship to cost at all.                                                                                                                                                                                                                                                                                                                                                              | A             | [Gloaguen et al. 2026](https://arxiv.org/abs/2602.11988), Fig. 13 and Table 2             | Same failure mode as C-107: a token-savings number asserted with no measurement behind it. If the operator wants this number, it is cheaply measurable locally — see Gaps.                                                                                               |
| C-185    | REFUTED    | "Executable" is false. Nothing in Claude Code, Cursor, or Codex reads a tier annotation in a markdown file and routes on it. Model selection comes from settings.json, `--model`, `/model`, or subagent frontmatter.                                                                                                                                                                                                                                                                                                                                                 | A (vendor)    | [Claude Code memory docs](https://code.claude.com/docs/en/memory); best-practices doc     | The annotation is a _record of intent_, which is legitimate documentation; calling it "executable" describes a mechanism that does not exist. This is itself an instance of the drift class the operator is worried about.                                               |
| C-206    | REFUTED    | `./.claude/CLAUDE.md` **is** a first-class project-instructions location, loaded at launch with the same precedence as `./CLAUDE.md` — not "tooling config." Separately, nested subdirectory CLAUDE.md files load **on demand** and are **not re-injected after `/compact`**, so they are not redundant with a root file.                                                                                                                                                                                                                                            | A (vendor)    | [Claude Code memory docs](https://code.claude.com/docs/en/memory)                         | The "root policy cascades down" half is directionally right for _ancestor_ directories (files are concatenated root→cwd) and wrong for _descendant_ directories. `claudeMdExcludes` exists precisely because ancestor cascade is sometimes unwanted.                     |

**Verdict counts:** CONFIRMED 1 · STALE 2 · REFUTED 6 · UNVERIFIED 1 · SKIPPED 0. All ten
assigned claims appear.

---

## Contradiction Findings

### X-03 — Minimal ceremony vs. mandatory context/spec infrastructure

**Assigned jointly to W1 and W4. My angle, as instructed: do maintained context/instruction
files pay for themselves?**

The evidence does not split along the axis the corpus argues about. It splits cleanly between
the **existence** of a context file and its **elaboration**, and the answer is opposite on each.

**Existence pays, and the effect is enormous.** McMillan's factorial study includes four
no-configuration baseline cells across three models and two codebases. Across **1,669
function-level observations, zero functions** complied with the target convention without a
CLAUDE.md (Wilson 95% upper bound 0.73%). With one, compliance ran 54.9–67.7% depending on
model and codebase. The matched contrast is χ² = 534.27, p = 3.3 × 10⁻¹¹⁸, Cohen's |h| = 1.93.
For a convention the agent cannot derive from the code, the instruction file is the difference
between never and usually. Tier A.

**Elaboration does not pay, and this is now measured four independent ways.**

1. **Size, position, architecture, and inter-file conflict are all null.** None of the four
   manipulated structural variables, and none of the three two-way interactions, produced a
   detectable contrast after correction. Size and conflict carry affirmative-null Bayes factors
   (BF₁₀ = 0.096 and 0.053), robust across a prior sweep of σ ∈ {0.5, 1.0, 2.5, 5.0}. A 25-line
   file and a 500-line file are indistinguishable. A contradicting instruction in an adjacent
   AGENTS.md did not measurably override the primary file (pooled contrast +0.33 pp, p = 0.912).
   ([McMillan, arXiv:2605.10039](https://arxiv.org/abs/2605.10039), read in full.)

2. **Context files do not improve task success and cost 19–23% more.** Across four models and
   two benchmarks (SWE-bench and the purpose-built CTXBENCH of 138 instances from 12 repositories
   with developer-committed context files), LLM-generated context files reduced resolution rate
   by 0.5% and 2% on average (p = 0.87, p = 0.37 — not significant) while significantly raising
   step count and cost. Developer-written files improved success by 2.4% on average — also not
   significant (p = 0.21) — while still raising cost up to 19%.
   ([Gloaguen et al., arXiv:2602.11988](https://arxiv.org/abs/2602.11988), read in full.)

3. **The specific ceremony the corpus prescribes is the specific ceremony measured to be inert.**
   C-107 and X-03 Position B both centre on "architectural system maps, module boundaries,
   directory enumeration." Gloaguen et al. tested exactly this: 8 of 12 developer files and
   ~100% of Sonnet-generated files contained a codebase overview. Overviews did **not** reduce
   the number of steps before the agent first touched a file it needed to modify — on any agent,
   on either benchmark. Ablating the overview category changed accuracy by −5.8 pp on CTXBENCH
   (p = 0.15) and −0.2 pp on SWE-bench (p = 0.73): no significant effect either way. The paper's
   own summary: context files "are not effective at providing a repository overview" and are
   "redundant documentation."

4. **The ceremony ratchets and nobody prunes it.** Across 2,303 context files in 1,925
   repositories: median **57 words added** per Claude Code commit versus **under 15 words
   deleted**; 67.4% of files modified in multiple commits, median 24 hours apart. Median Flesch
   Reading Ease 16.6 — "very difficult," the band of dense legal contracts. The authors name the
   resulting state **"context debt."**
   ([Chatlatanagulchai et al., arXiv:2511.12884](https://arxiv.org/abs/2511.12884), read in full.)

**Both positions get the mechanism wrong.** The corpus argues about _what to write in the file_.
The largest measured effect in the only controlled study is not in the file at all: compliance
falls **5.6% in odds per function generated within a session** (OR = 0.944, 95% CI [0.937,
0.951], p = 1.1 × 10⁻⁴⁹), with the median first omission at generated function **4**. A rule
that must hold over a long run cannot be held by prose, regardless of how the prose is
structured. Anthropic's documentation says the same thing in plain language: instruction files
are "context, not enforced configuration"; hooks are the enforcement layer.

**Where the answer changes.** Three conditions flip it toward more infrastructure:

- **When the repository has no other documentation.** In Gloaguen et al.'s ablation — all `.md`
  files, example code, and `docs/` removed — LLM-generated context files improved performance by
  **2.7% on average** and beat developer-written ones. The authors offer this as the explanation
  for practitioner enthusiasm: "many less popular repositories contain little to no
  documentation." Context files substitute for missing documentation; they do not add to
  adequate documentation.
- **Above 500 lines.** McMillan's null is bounded; he explicitly flags that "a 5,000-line
  CLAUDE.md exists in some large repositories and is well outside our design."
- **Above roughly 150 instructions.** IFScale (500 keyword-inclusion instructions, 20 models,
  seven providers) found the best frontier model reaches only **68% accuracy at 500
  instructions**, with primacy bias — later instructions violated more — peaking at 150–200
  instructions. Claude Sonnet 4 showed linear decay.
  ([Jaroslawicz et al., arXiv:2507.11538](https://arxiv.org/abs/2507.11538).)

**Verdict on X-03, my lane:** Position A ("dumbest thing that works") is supported on
elaboration; Position B is supported only on existence, and only for conventions genuinely
underivable from the artifacts themselves. The break-even is not a line count — it is a content
test: _does this instruction encode something nothing in the repository already states?_ Every
measured benefit sits on that side; every measured cost sits on the other. The corpus's own
"sledgehammer to crack a nut" objection to Kiro/spec-kit turns out to apply to the corpus's own
AI.md/Tier-Policy prescription, with better evidence behind it than behind the prescription.

---

## Findings

### F-W4-01 — The presence of an instruction file is the whole measured effect; its structure is not

- **Claim** — For a convention not derivable from the artifacts, adding an instruction file moves
  compliance from ~0% to ~55–68%; varying that file's size (25–500 lines), the instruction's
  position within it, the number of files it is split across, or the presence of a contradicting
  instruction in an adjacent file produces no detectable change.
- **Evidence tier** — A.
- **Support** — [McMillan, "Instruction Adherence in Coding Agent Configuration Files,"
  arXiv:2605.10039, 11 May 2026](https://arxiv.org/abs/2605.10039). **Read in full.** 1,650
  Claude Code CLI sessions, 16,050 function-level observations, two TypeScript codebases, three
  models, five tasks, pre-registered GLMM with a Bayesian companion. Baseline 0/1,669 compliant;
  with-config 54.9–67.7%. Structural nulls: size χ²=5.16 p=0.16 (BF₁₀=0.096), position χ²=1.47
  p=0.83, architecture χ²=3.29 p=0.19, conflict χ²=0.10 p=0.76 (BF₁₀=0.053).
- **Date sensitivity** — Models tested were Sonnet 4.6 / Opus 4.6 / Opus 4.7 on Claude Code CLI
  2.1.92–2.1.123. Re-check on a materially newer model generation; the qualitative finding
  (presence ≫ structure) is more durable than the absolute rates.
- **Confidence** — High for the effect of presence (huge effect, replicated across two codebases
  and two models, exact zero baseline in four independent cells). Medium for the structural
  nulls: they are affirmative only for size and conflict; position and architecture are failures
  to reject, and the design rules out effects above ~6 pp but not smaller ones.
- **Counter-evidence** — Single author, single affiliation (HxAI Australia), preprint, not peer
  reviewed. The dependent variable is one trivial annotation (`// @tracked`); the author himself
  writes that transfer "to more demanding instructions... is an open question." Single-turn
  `--print` mode, not multi-turn interactive use. Anthropic's own documentation asserts the
  opposite of the size null and is the more authoritative source on its own product — but
  provides no data.

### F-W4-02 — Repository-level context files raise inference cost 19–23% without significantly improving task success

- **Claim** — Adding an AGENTS.md/CLAUDE.md-style context file to a repository significantly
  increases agent steps and inference cost while producing no statistically significant change in
  task resolution rate, for both LLM-generated and developer-committed files.
- **Evidence tier** — A.
- **Support** — [Gloaguen, Mündler, Müller, Raychev, Vechev, "Evaluating AGENTS.md: Are
  Repository-Level Context Files Helpful for Coding Agents?", arXiv:2602.11988v2, 23 Jun
  2026](https://arxiv.org/abs/2602.11988) (ETH Zurich + LogicStar.ai). **Read in full.** Cost
  increase 20% (SWE-bench) and 23% (CTXBENCH), p < 0.001% by stratified permutation test.
  Resolution rate: −0.5% and −2% for LLM-generated (p = 0.87, 0.37); +2.4% for developer-written
  (p = 0.21). Four agents/models: Sonnet-4.5, GPT-5.2, GPT-5.1 Mini, Qwen3-30B-Coder. New
  benchmark CTXBENCH: 138 instances, 12 repositories with developer-committed context files.
- **Date sensitivity** — Model-generation sensitive; the cost multiplier is likely stable but the
  success deltas could move. Re-check within 12 months.
- **Confidence** — High. Multi-model, multi-benchmark, purpose-built benchmark for the exact
  question, ablations for length, category, contamination, and generating model, and a
  disconfirming result published against the authors' own field's prevailing advice.
- **Counter-evidence** — Python only; the authors note Python is heavily represented in training
  data, which may nullify the effect that context files would have in niche languages/toolchains.
  Developer-written files did beat LLM-generated ones significantly (p = 0.038), so _some_ human
  content carries signal. Measures task resolution only, not code quality, security, or style
  conformance — which is where instruction files plausibly earn their keep and where nobody has
  measured them.

### F-W4-03 — Context files help measurably in exactly one tested condition: when no other documentation exists

- **Claim** — When all documentation (`.md` files, example code, `docs/`) is stripped from a
  repository, LLM-generated context files improve success by 2.7% on average and outperform
  developer-written files; where documentation already exists, they are measurably redundant.
- **Evidence tier** — A.
- **Support** — [Gloaguen et al., §B "Context files are redundant
  documentation"](https://arxiv.org/abs/2602.11988). Read in full.
- **Date sensitivity** — Low. This is a structural finding about redundancy, not a figure.
- **Confidence** — Medium. A single ablation, run on three of the four models (Claude Code
  excluded for cost), with a small effect size.
- **Counter-evidence** — 2.7% is small and the ablation is artificial: nobody deletes their docs.
  Its practical reading is inferential — that context files pay when they carry non-redundant
  content — and that inference is the authors' own, not an independently tested claim.

### F-W4-04 — Instruction compliance decays _within_ a session as output accumulates, independent of file structure

- **Claim** — Each additional function an agent generates within a session is associated with
  ~5.6% lower odds of complying with a standing instruction; among runs that broke the rule at
  all, the median first violation was at generated function 4.
- **Evidence tier** — A.
- **Support** — [McMillan, arXiv:2605.10039](https://arxiv.org/abs/2605.10039), §4.6. Read in
  full. OR = 0.944, 95% Wald CI [0.937, 0.951], p = 1.08 × 10⁻⁴⁹; Bayesian posterior centred at
  −0.0578 log-odds, Savage-Dickey BF at numerical floor. Reproduces in direction on a second
  codebase (Umami, OR = 0.934) and a second model (Opus 4.6, OR = 0.971). Median first-omission
  generation position 4; post-omission compliance 55.0%.
- **Date sensitivity** — Medium. Harness-dependent; may change with context-management changes in
  the CLI.
- **Confidence** — Medium. The largest effect in the dataset by orders of magnitude and Bayes-
  supported, but the author is explicit that it was **identified during analysis, not
  pre-specified**, and calls for independent replication. The relationship is non-monotonic, so
  the 5.6% is an average, not a per-step constant (per-task slopes: T3 +0.005 ns, T4 −0.046,
  T5 −0.185).
- **Counter-evidence** — Part of the late-session "recovery" in the curve is compositional (file
  types with stable high compliance dominating the tail), not genuine re-engagement — the author
  says so. Single-turn harness; multi-turn sessions with compaction may behave differently in
  either direction.

### F-W4-05 — Adherence degrades systematically with instruction count, and later instructions are dropped first

- **Claim** — At 500 simultaneous instructions the best frontier model reaches 68% accuracy;
  degradation follows one of three model-dependent curves; models preferentially violate
  instructions appearing later in the list, with that bias peaking at 150–200 instructions.
- **Evidence tier** — A.
- **Support** — [Jaroslawicz, Whiting, Shah, Maamari, "How Many Instructions Can LLMs Follow at
  Once?", arXiv:2507.11538](https://arxiv.org/abs/2507.11538) (Distyl AI). IFScale: 500
  keyword-inclusion instructions on a business-report task, 20 models across seven providers,
  density swept 10→500 in steps of 10, five runs each. Threshold decay (gemini-2.5-pro, o3),
  linear decay (gpt-4.1, claude-sonnet-4), exponential decay (gpt-4o, llama-4-scout, floors at
  7–15%). At 500 instructions: o3 62.8%, grok-3 61.9%, claude-3.7-sonnet 52.7%, claude-opus-4
  44.6%, claude-sonnet-4 42.9%. Omission:modification error ratio rises sharply with density
  (llama-4-scout 34.88 at max).
- **Date sensitivity** — **High.** Model lineup is July 2025 vintage. The absolute numbers are
  stale by roughly a year as of 2026-08-01; the _shape_ of the finding is the durable part.
- **Confidence** — High on shape, low on the specific 2025 numbers.
- **Counter-evidence** — The task is keyword inclusion in a single generated report, not a
  multi-turn agent loop reading a config file; instruction density there is far above what any
  reasonable CLAUDE.md contains. Notably, `claude-3.7-sonnet` outperformed the newer
  `claude-opus-4` and `claude-sonnet-4` at max density, which cuts against "newer is better" and
  against extrapolating any of it to current models. This finding constrains the _upper_ bound of
  ceremony, not the 25–500-line range McMillan actually tested.

### F-W4-06 — Instruction files accumulate monotonically: additions outpace deletions ~4:1, and readability is already at legal-contract difficulty

- **Claim** — Agent context files are actively maintained but almost never pruned; the median
  Claude Code commit adds 57 words and deletes under 15, and the median file scores Flesch
  Reading Ease 16.6 ("very difficult"). The authors formalize the result as **context debt**.
- **Evidence tier** — A.
- **Support** — [Chatlatanagulchai, Li, Kashiwa, Reid et al., "Agent READMEs: An Empirical Study
  of Context Files for Agentic Coding", arXiv:2511.12884, Nov 2025](https://arxiv.org/abs/2511.12884).
  **Read in full.** 922 CLAUDE.md + 694 AGENTS.md + 687 copilot-instructions.md across 1,925
  repositories (≥5 stars); 5,655 CLAUDE.md-touching commits analysed. 67.4% of Claude Code files
  modified in multiple commits; median inter-commit interval 24.1 hours. Median length 485 words
  (Claude Code), 535 (Copilot), 335.5 (Codex).
- **Date sensitivity** — Medium. Snapshot of Nov 2025 open-source practice; the ratchet dynamic is
  likely durable, the absolute lengths will grow.
- **Confidence** — High for the descriptive statistics; the "context debt" framing is the
  authors' interpretation, not a measured harm.
- **Counter-evidence** — This measures open-source repositories with ≥5 stars, which skews toward
  projects with multiple contributors — a solo operator's ratchet dynamics may differ. Critically,
  the paper measures _accumulation_, and F-W4-01 says accumulation up to 500 lines has no
  measured compliance cost. The two findings only conflict if you assume length is the harm; the
  demonstrated harm is to **human** maintainability (FRE 16.6) and to inference cost (F-W4-02),
  not to adherence.

### F-W4-07 — The vendor's own documentation classifies instruction files as advisory and names hooks as the enforcement layer

- **Claim** — Anthropic explicitly states that CLAUDE.md and auto-memory are context rather than
  configuration, that compliance is not guaranteed, and that deterministic enforcement requires
  hooks or settings — directly contradicting the corpus's framing of context files as
  "infrastructure" (C-137).
- **Evidence tier** — A (vendor documentation, i.e. primary for the product, and against its own
  marketing interest here).
- **Support** — [Claude Code memory docs](https://code.claude.com/docs/en/memory), read in full:
  _"Claude treats them as context, not enforced configuration. To block an action regardless of
  what Claude decides, use a PreToolUse hook instead."_ And: _"Settings rules are enforced by the
  client regardless of what Claude decides to do. CLAUDE.md instructions shape Claude's behavior
  but are not a hard enforcement layer."_ Corroborated in
  [best practices](https://code.claude.com/docs/en/best-practices): _"Unlike CLAUDE.md
  instructions which are advisory, hooks are deterministic and guarantee the action happens."_
- **Date sensitivity** — Retrieved 2026-08-01. Feature-availability claims (`.claude/rules/`,
  `claudeMdExcludes`, auto memory, `/doctor` trim check, `InstructionsLoaded` hook) are versioned
  and will drift; the advisory-vs-enforced distinction is architectural and stable.
- **Confidence** — High.
- **Counter-evidence** — None found. This is a vendor stating a limitation of its own product,
  which is the strongest kind of vendor claim. Note the internal tension: the same vendor asserts
  the size→adherence relationship (C-035) that the independent study refutes, so the docs are
  authoritative on mechanism and unsourced on effect.

### F-W4-08 — Long-context degradation is measured, non-uniform, and — counterintuitively — worse on logically structured corpora than shuffled ones

- **Claim** — Model performance degrades with input length even at constant task difficulty; a
  single distractor measurably hurts; and in the one experiment that tested it, models performed
  **better** on shuffled, incoherent haystacks than on logically structured ones.
- **Evidence tier** — B (industry research lab with a commercial stake in retrieval, but
  methodologically transparent, reproducible, and publishing a result that complicates rather
  than flatters its own product).
- **Support** — [Chroma, "Context Rot: How Increasing Input Tokens Impacts LLM Performance,"
  14 July 2025](https://www.trychroma.com/research/context-rot). 18 models (GPT-4.1, Claude 4,
  Gemini 2.5, Qwen3 variants). LongMemEval: consistent gap between ~300-token focused prompts and
  ~113k-token full prompts, most pronounced on Claude models. Degradation is steeper for
  low-similarity needle-question pairs.
- **Date sensitivity** — **High.** July 2025 model lineup, roughly 13 months stale as of
  2026-08-01. Treat the mechanism as durable and every number as historical.
- **Confidence** — Medium. Well-instrumented and widely replicated in spirit by the academic
  long-context literature (Liu et al. "Lost in the Middle," RULER), but a vendor blog rather than
  peer review, and the shuffled-haystack result is explicitly unexplained by the authors.
- **Counter-evidence** — Directly relevant counter-evidence: McMillan tested the "Lost in the
  Middle" U-shape _inside a config file_ at five positions and found no detectable shape
  (quadratic component p = 0.94), noting that the U-shape is canonically observed at far longer
  contexts than a 250-line file. So context-rot findings do **not** transfer down to
  instruction-file scale. They bear on the knowledge-repo case (large corpora read into context),
  not the CLAUDE.md case.

### F-W4-09 — Domain-partitioned file indexes keep grep/read navigation accurate at 10,000 units where single-file context degrades

- **Claim** — For agents navigating a file-native knowledge layer with grep and read, single-file
  context maintains near-perfect navigation accuracy to ~1,000 units but requires domain
  partitioning (~250 units per domain plus an index file) to hold accuracy at 10,000 units, which
  keeps per-query context bounded regardless of total corpus size.
- **Evidence tier** — B.
- **Support** — [McMillan, "Structured Context Engineering for File-Native Agentic Systems,"
  arXiv:2602.05447, Feb 2026](https://arxiv.org/abs/2602.05447). 9,649 experiments, 11 models,
  4 formats (YAML/Markdown/JSON/TOON), 10→10,000 units. Also finds format has **no** significant
  aggregate accuracy effect (χ² = 2.45, p = 0.484) and that model capability dominates (21 pp
  frontier-vs-open-source gap). Identifies a "grep tax": file size does not predict token cost —
  Markdown cost +7% to +105% more tokens than YAML at equal information content because each grep
  hit returns denser output; the index-file approach at ~250 units/domain showed **no** measurable
  grep tax increase up to 10,000 units.
- **Date sensitivity** — Medium. Model lineup Feb 2026.
- **Confidence** — Low-to-medium. This is the closest thing that exists to a controlled study of
  index/ontology conventions for an agent-navigated document corpus — but the units are **database
  tables described in schema files**, not research documents, and the task is SQL generation. The
  transfer to a prose knowledge repository is an analogy, not a measurement.
- **Counter-evidence** — Same single author and affiliation as F-W4-01/F-W4-04; not peer reviewed;
  self-cited by his own later paper. Uses synthetic TPC-DS-derived schemas, so the "10,000 units"
  corpus is far more homogeneous than a real research repository. The finding that format doesn't
  matter cuts against elaborate ontology conventions as much as the partitioning finding supports
  simple ones.

### F-W4-10 — Retrieval-grounded systems over curated closed corpora still misground citations at high rates: grounding is not verification

- **Claim** — Purpose-built, commercially deployed RAG systems over closed, professionally curated
  legal corpora produced hallucinated answers 17–33% of the time; the best was accurate on 65% of
  queries and one was accurate on 42%.
- **Evidence tier** — A.
- **Support** — [Magesh, Surani, Dahl, Suzgun, Manning, Ho, "Hallucination-Free? Assessing the
  Reliability of Leading AI Legal Research Tools," arXiv:2405.20362, Stanford RegLab/HAI,
  May 2024](https://arxiv.org/abs/2405.20362). Preregistered, 200+ manually constructed queries
  across four categories. Lexis+ AI 65% accurate; Westlaw AI-Assisted Research 42% accurate and
  hallucinating nearly twice as often as the other legal tools; Ask Practical Law AI incomplete
  on >60% of queries. Crucially, their coding scheme separates **incorrect** from **misgrounded** —
  a response is hallucinated if it is _either_ factually wrong _or_ correct-but-cited-to-a-source-
  that-does-not-support-it. Misgrounding is the failure mode a fluent summary hides.
- **Date sensitivity** — **High.** May 2024. Two-plus years stale as of 2026-08-01; these products
  have shipped many versions since. The _rate_ is historical; the _failure taxonomy_ (correct vs.
  grounded as orthogonal axes) is the durable contribution.
- **Confidence** — High for the study as conducted; low that the numbers still describe today's
  products.
- **Counter-evidence** — Vendors disputed the methodology on publication, particularly the query
  construction and the treatment of refusals. The study is adversarial by design — queries were
  built to probe failure — so the rates are not a random sample of ordinary use. It measures
  vendor products, not a self-built corpus, so it bounds what a commercial RAG stack achieves,
  not what careful manual verification achieves.

### F-W4-11 — Automated claim-level fact verification against search reaches ~72% agreement with human annotators at >20× lower cost

- **Claim** — An LLM pipeline that decomposes long-form output into individual atomic claims and
  verifies each against search agrees with crowdsourced human annotators 72% of the time over
  ~16,000 facts, wins 76% of adjudicated disagreements, and costs more than 20× less than human
  annotation.
- **Evidence tier** — A.
- **Support** — [Wei et al., "Long-form factuality in large language models," arXiv:2403.18802,
  Google DeepMind, Mar 2024 (rev. Nov 2024)](https://arxiv.org/abs/2403.18802). SAFE
  (Search-Augmented Factuality Evaluator) + LongFact benchmark (thousands of questions, 38 topics).
- **Date sensitivity** — Medium-high. March 2024; the underlying models are two generations old,
  so 72% is likely a floor rather than a current figure.
- **Confidence** — Medium. Rigorous and widely cited, but 72% agreement means roughly one claim in
  four is scored differently than a human would score it — that is a triage tool, not an
  assurance mechanism. The "SAFE wins 76% of disagreements" figure is from a 100-case sample
  adjudicated by the paper's own authors, which is not independent.
- **Counter-evidence** — Crowdsourced annotators are a weak gold standard; agreement with them
  bounds the measurement, not the truth. The decompose-and-verify architecture is also the
  architecture that fails in F-W4-10 — SAFE checks whether a claim is supported by _something
  findable_, not whether the _specific citation attached to it_ supports it. Those are different
  checks, and the second is the one that failed 40/109 times in the operator's own prior corpus.

### F-W4-12 — Naive LLM doc-auditing has an unusable false-positive rate; the fix is filtering or grounding, and both cost recall

- **Claim** — Prompting an LLM directly to judge whether documentation matches code flags over 90%
  of functions as inconsistent against a real base rate of roughly 11%; structured filtering brings
  the flag rate to 14–17% at precision ~0.63, and grounding the judgment in generated tests reaches
  precision 0.88 at the cost of recall 0.21.
- **Evidence tier** — A.
- **Support** — [Xu, Wahab, Holmes, Lemieux (UBC), "DocPrism: Local Categorization and External
  Filtering to Identify Relevant Code-Documentation Inconsistencies," arXiv:2511.00215, rev.
  2026-07-29](https://arxiv.org/abs/2511.00215): naive prompting ablation **98% flag rate at
  F1 0.22**; LCEF method **14% flag rate at F1 0.77**; broad four-language eval (Python,
  TypeScript, C++, Java) **17% flag rate, precision 0.63**; conservative base rate **11% of
  code-documentation pairs** genuinely inconsistent; prior SOTA precision **collapses from
  synthetic-benchmark parity to 0.05–0.14 on real-world Java**. Complementary:
  [Kiecker et al. (HU Berlin/XBOW), "Cascade: Detecting Inconsistencies between Code and
  Documentation with Automatic Test Generation," arXiv:2604.19400,
  2026-04-21](https://arxiv.org/html/2604.19400) — 885 method-doc pairs from 16 Java projects;
  **precision 0.88, recall 0.21, specificity 0.97, F1 0.35**, versus best LLM-voting baseline
  precision 0.61 / recall 0.37 / F1 0.46; found 13 previously unknown real inconsistencies, 10
  fixed.
- **Date sensitivity** — Medium. Model-generation sensitive; the >90% naive flag rate will fall as
  models improve, but the structural cause (LLMs read _abstraction gaps_ between high-level prose
  and code as inconsistencies) is architectural, not a capability gap.
- **Confidence** — Medium-high. Two independent groups, real-world (not synthetic) evaluation
  sets, and the DocPrism synthetic-to-real precision collapse is itself a strong methodological
  warning that raises confidence in the pessimistic reading.
- **Counter-evidence** — Both are 2025–2026 preprints. DocPrism's 0.63 precision still means
  roughly a third of flags are noise, so neither result licenses unattended operation. Cascade's
  approach only works where documentation describes behavior expressible as a test — which
  excludes most prose documentation and all of a knowledge repository.

### F-W4-13 — Documentation drift is common, long-lived, and does not self-heal

- **Claim** — 28.9% of the 1,000 most-popular GitHub projects currently contain an outdated
  code-element reference in their documentation, 82.3% have had one at some point, and the mean
  persistence is 4.7 years with roughly a 55% survival probability after one month.
- **Evidence tier** — A.
- **Support** — [Tan, Wagner, Treude, "Detecting outdated code element references in software
  repository documentation," Empirical Software Engineering,
  arXiv:2212.01479](https://arxiv.org/abs/2212.01479) (tool: DOCER). Two corpora: 1,000
  most-popular GitHub projects (9,784 docs) and 2,279 Google-hosted projects (2,947 docs, 5.4%
  current / 29.7% historical — a much lower rate, plausibly reflecting review discipline).
- **Date sensitivity** — Low-medium. A base rate over project history, published 2023.
- **Confidence** — Medium-high for the base rate; the corpus is large and the detection target
  (a named code element that no longer exists) is unambiguous.
- **Counter-evidence** — The authors' own developer validation is sobering: of 15 Google projects
  contacted, **4 confirmed and 4 reported false positives** (7 no response), and only 5 of 19
  reported instances were fixed. So the measured rate is an upper bound and the demonstrated
  appetite to act on such reports is low. Detects only _code-element_ references — the narrowest
  and most machine-checkable class of drift.

### F-W4-14 — AI-authored change descriptions misstate what was actually changed, and "phantom changes" are the largest failure category

- **Claim** — In pull requests authored by AI coding agents, 1.7% show high message-code
  inconsistency overall but the rate varies 20× by agent (8.7% GitHub Copilot to 0.4% Devin);
  45.4% of those cases are "Phantom Changes" — the description claims modifications that were
  never implemented.
- **Evidence tier** — A.
- **Support** — [Gong, Pinna, Bian, Zhang, "Analyzing Message-Code Inconsistency in AI Coding
  Agent-Authored Pull Requests," MSR 2026, arXiv:2601.04886](https://arxiv.org/html/2601.04886v2).
  23,247 PRs from five AI agents across 2,807 repositories; 974 manually annotated at κ = 0.892.
  High-MCI PRs were accepted 28.3% of the time vs 80.0% for others and took 3.5× longer to merge
  (55.8h vs 16.0h).
- **Date sensitivity** — High. Agent lineup and per-agent rates will change fast; the failure
  taxonomy is durable.
- **Confidence** — Medium. Large sample, good annotator agreement, but MCI is judged by human
  raters and the definition of "high inconsistency" is theirs.
- **Counter-evidence** — The authors state explicitly they have **no comparison to human-authored
  PR rates**, so this may not be an AI-specific pathology at all. 1.7% overall is a low base rate.

### F-W4-15 — Every deterministic docs-CI check in production use is semantically blind

- **Claim** — The mature docs-CI toolchain (Vale, markdownlint, lychee, `mkdocs --strict`, Sphinx
  nitpicky, Docusaurus `onBrokenLinks`) verifies links, anchors, structure, prose style, and
  regeneration-process compliance. None of it parses code or environment semantics, so none of it
  can detect a well-formed sentence that is false.
- **Evidence tier** — A (vendor/project documentation, primary for tool behavior).
- **Support** — [GitLab documentation testing](https://docs.gitlab.com/development/documentation/testing/)
  is the most complete published inventory of a production docs pipeline: Vale + markdownlint +
  relative-link-and-anchor checks + `docs-lint redirects` (deleted/renamed files without
  redirects) + `graphql-verify` (fails when reference docs were not regenerated properly) +
  **`rubocop-docs` / `eslint-docs`, which check documentation links referenced _from_ `.rb` and
  `.js`/`.vue` source** — the only code→docs check I found in any production CI.
  Boundaries worth knowing: [MkDocs](https://www.mkdocs.org/user-guide/configuration/) `--strict`
  does **not** check anchors by default (`validation.links.anchors` defaults to info);
  [Docusaurus](https://docusaurus.io/docs/api/docusaurus-config) `onBrokenLinks` defaults to
  `throw` but `onBrokenAnchors` only to `warn`, and detection runs only on production builds;
  [Sphinx](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) nitpicky warnings have
  **not failed the build under `-W` since Sphinx 1.6**, so "we run nitpicky in CI" frequently
  gates nothing; [lychee](https://github.com/lycheeverse/lychee) has fragment checking off by
  default.
- **Date sensitivity** — Medium. Tool defaults change; verify the specific flags before relying
  on them.
- **Confidence** — High. These are documented behaviors, several of them documented gotchas.
- **Counter-evidence** — [Datadog's published Vale experience](https://www.datadoghq.com/blog/engineering/how-we-use-vale-to-improve-our-documentation-editing-process/)
  reports real production use at 20,000+ PRs/year but publishes **no quantified outcome** — no
  error counts, no review-time reduction. So the value of even the prose-linting layer is
  asserted rather than measured.

### F-W4-16 — The best-documented organizational finding on doc decay is Google's, and it is about ownership, not tooling

- **Claim** — At Google, documentation quality became the number-one developer complaint on annual
  developer surveys; on the deprecated internal wiki, ~90% of documents had no views or updates in
  the previous few months, attributed to the absence of true owners. The remedy adopted was
  ownership, freshness dates with automated staleness reminders, and treating docs as code.
- **Evidence tier** — A/B — an org publishing measured internal survey and usage data about its
  own failure, in a book with named authors and a public edition.
- **Support** — [_Software Engineering at Google_, Ch. 10
  "Documentation"](https://abseil.io/resources/swe-book/html/ch10.html) (O'Reilly 2020, free
  HTML). Also notable and contrarian: _"Because Google's Code Search browser is so robust, we've
  found little benefit to providing separate generated reference documentation"_ — a direct
  dissent from the standard generate-your-reference advice.
- **Date sensitivity** — Medium-high. 2020 publication describing an internal migration that
  predates it. Directionally durable, numerically historical.
- **Confidence** — Medium. Real numbers, but self-reported, unauditable, and at a scale
  (thousands of engineers) with no obvious transfer to one operator.
- **Counter-evidence** — The prescriptions (ownership, review, freshness reminders) are presented
  without any before/after measurement of whether they worked. Google's Code Search dissent is
  also a scale-specific argument: it holds because they built an exceptional search tool.

### F-W4-17 — No published measurement exists for the outcome of generating docs instead of hand-writing them

- **Claim** — The generated-vs-hand-written boundary is well specified in practice — Stripe treats
  OpenAPI as single source of truth and generates SDKs across seven languages, the CLI surface,
  API reference structure, and changelog entries, while hand-writing the API design and doc
  strings — but no organization has published a drift-rate, defect-rate, or time-to-propagate
  comparison.
- **Evidence tier** — B for the mechanism (vendor engineering blog), **none for the outcome**.
- **Support** — [Stripe, "How API changes flow into Stripe's developer products," 2026-06-15](https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products);
  [stripe/openapi](https://github.com/stripe/openapi). [Diátaxis](https://diataxis.fr/) supplies
  the conceptual boundary — reference is the quadrant that should be generated, tutorials and
  explanation are inherently hand-written — and is explicit that it offers testimonials, not
  measurement. [Write the Docs "Docs as Code"](https://www.writethedocs.org/guide/docs-as-code/)
  cites adoption by Google, Microsoft, AWS, UK GDS and others entirely via conference talks.
- **Date sensitivity** — Low; this is an absence, not a figure.
- **Confidence** — High that the gap exists; two independent searches found nothing.
- **Counter-evidence** — GitLab's `graphql-verify` job is indirect evidence that at least one org
  considers hand-editing generated docs a defect worth failing CI over. That is an enforcement
  signal, not an outcome measurement.

### F-W4-18 — Cross-repo consistency tooling is well-specified and completely unmeasured

- **Claim** — Mechanisms to keep several repositories mutually coherent exist and are
  CI-integrable — `cruft check` exits 1 when a project has fallen behind its template and is
  explicitly documented for CI use; file-sync actions open PRs in target repos when a synced file
  diverges; GitHub `.github` default community-health files cascade org-wide — but no published
  study measures drift rates or the effect of any of these.
- **Evidence tier** — A (tool documentation) for the mechanisms; **no evidence** for efficacy.
- **Support** — [cruft](https://cruft.github.io/cruft/): `.cruft.json` pins the template commit
  hash plus variables and skip patterns; `cruft diff --exit-code`; documented weekly
  GitHub Actions workflow. Stated blind spot: **files in the skip section are never monitored**.
  [GitHub default community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file):
  the `.github` repo must be **public**, and defaults are **all-or-nothing** — one file in a
  repo's own `.github/ISSUE_TEMPLATE` suppresses the entire default folder.
  [repo-file-sync-action](https://github.com/Redocly/repo-file-sync-action) opens a PR when a
  target file is out of sync. Claude Code adds a first-party analogue: `.claude/rules/` supports
  symlinks so one shared rules directory can be linked into many projects
  ([memory docs](https://code.claude.com/docs/en/memory)).
- **Date sensitivity** — Medium (tool behavior).
- **Confidence** — High on mechanisms, high that the efficacy evidence is absent.
- **Counter-evidence** — [Backstage TechDocs](https://backstage.io/docs/features/techdocs/)
  reports 5,000+ documentation sites and ~20% of Backstage traffic at Spotify — real adoption at
  scale for the docs-hub-over-many-repos pattern, but those are _usage_ numbers and say nothing
  about accuracy. On monorepo-vs-polyrepo, the only quantified source found is vendor-produced
  ([Faros.ai](https://www.faros.ai/blog/monorepo-vs-polyrepo-benchmark-data), 320 teams, median
  PR cycle 19h monorepo vs 2h polyrepo) and is about PR flow, not documentation.

### F-W4-19 — Corpus-level contradiction in prose is measurable, common, and beyond reliable automation

- **Claim** — At least 3.3% of facts in English Wikipedia contradict another fact elsewhere in the
  same corpus; the best fully automated detector reaches only 75.1% AUROC, while a human-in-the-loop
  agentic system let editors find 64.7% more inconsistencies in the same time.
- **Evidence tier** — A.
- **Support** — [Semnani, Burapacheep, Khatua, Atchariyachanvanit, Wang, Lam, "Detecting
  Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models," EMNLP 2025
  Main, arXiv:2509.23233](https://arxiv.org/abs/2509.23233). Introduces the CLID task, the
  WIKICOLLIDE benchmark of _authentic_ (not synthetic) cross-document contradictions, and the
  CLAIRE human-in-the-loop system. Inconsistencies propagate downstream into 7.3% of FEVEROUS and
  4.0% of AmbigQA examples. User study: 87.5% of editors reported higher confidence.
- **Date sensitivity** — Low-medium. Sept 2025; the 3.3% base rate is a property of Wikipedia, the
  75.1% AUROC will improve.
- **Confidence** — Medium-high. Peer-reviewed at a top venue, authentic rather than synthetic
  contradictions, and the headline is a negative result about automation.
- **Counter-evidence** — Wikipedia is a multi-author corpus edited by strangers; a single-author
  research repository has a different contradiction-generating process (drift over time rather
  than disagreement between authors), and 3.3% may not transfer in either direction. Corroborating
  the pessimism: [contradiction detection in RAG systems,
  arXiv:2504.00180](https://arxiv.org/html/2504.00180v1) finds LLM validators show **high
  precision but low recall** — they are conservative and miss real contradictions, which is the
  worse failure mode for a corpus you believe is clean. The 2008 foundational result
  ([de Marneffe, Rafferty, Manning, ACL](https://nlp.stanford.edu/pubs/contradiction-acl08.pdf))
  is that contradiction detection is substantially harder than entailment because it needs
  near-complete event coreference.

### F-W4-20 — Automated citation-support checking tops out around 80% and has no maintenance-pass tooling at all

- **Claim** — The task of deciding whether a cited source actually supports the claim attached to
  it is measurable (ALCE defines citation precision/recall via NLI entailment) but hard: a
  fine-tuned model reaches only ~80% macro-F1 on binary supported/not-supported classification,
  and no tool exists that runs this as a maintenance pass over an existing prose corpus.
- **Evidence tier** — A.
- **Support** — [Li et al., "AttributionBench: How Hard is Automatic Attribution Evaluation?",
  Findings of ACL 2024, arXiv:2402.15089](https://arxiv.org/abs/2402.15089) — aggregates seven
  attribution datasets; **fine-tuned GPT-3.5 ≈80% macro-F1**; analysis of 300+ error cases
  attributes most failures to nuanced information and to the model having less context than the
  human annotator. [Gao et al., ALCE, EMNLP 2023,
  arXiv:2305.14627](https://arxiv.org/abs/2305.14627) supplies the operational metric definitions.
  [Gao et al., RARR, arXiv:2210.08726](https://arxiv.org/abs/2210.08726) is the closest
  architectural fit for auditing existing text — retrofit attribution, find evidence for already-
  generated text and minimally edit unsupported claims — but was built for generation time.
- **Date sensitivity** — Medium-high. 2023–2024 model generation; the 80% ceiling is likely higher
  now but nobody has re-measured it on frontier models.
- **Confidence** — Medium-high on the ceiling, high on the tooling absence.
- **Counter-evidence** — 80% macro-F1 is on a hard aggregated benchmark spanning seven
  heterogeneous datasets; a narrow, domain-specific checker over a corpus with consistent citation
  formats could plausibly do much better, and nobody has tried. This is a gap that cuts in the
  operator's favour: the ceiling is a research-benchmark ceiling, not a demonstrated limit on a
  purpose-built checker.

### F-W4-21 — A maintained source-reliability convention measurably improved a prose corpus; this is the only such evidence I found

- **Claim** — After English Wikipedia introduced its perennial-sources reliability list in 2018,
  the median lifespan of a risky reference fell by more than 3×; over a decade, the share of
  sentences lacking a citation dropped roughly 20 percentage points while the proportion of
  unreliable sources stayed below 1%.
- **Evidence tier** — A.
- **Support** — [Wikimedia Research: Reference Quality in English
  Wikipedia](https://meta.wikimedia.org/wiki/Research:Reference_Quality_in_English_Wikipedia)
  (data through Jan 2022), operationalized as **Reference Need** (% of sentences lacking a
  citation) and **Reference Risk** (proportion of unreliable sources). Analysed 3.2M revisions
  from random articles, 23.8M from top-viewed pages, 4.2M+ reference occurrences. Published as
  [Baigutanova et al., WWW 2023](https://arxiv.org/pdf/2303.05227). The complementary rubric —
  which assertions _require_ a citation and why — is
  [Redi, Fetahu, Morgan, Taraborelli, "Citation Needed," WWW 2019,
  arXiv:1902.11116](https://arxiv.org/abs/1902.11116).
- **Date sensitivity** — Medium. Data through Jan 2022.
- **Confidence** — Medium. Observational and longitudinal, not a controlled intervention — the
  2018 list coincided with other changes in editorial practice and the causal attribution is the
  researchers' inference.
- **Counter-evidence** — Massively multi-author corpus with formal policy, dispute resolution, and
  bots. Two orders of magnitude away from a solo operator. Also, source _reliability_ is not
  source _support_: the perennial-sources list bounds where a citation may come from, not whether
  it says what it is cited for — which is the failure mode in F-W4-10 and F-W4-20.

### F-W4-22 — Nothing measures whether any note-organization convention improves anything, and the measured PIM literature contradicts the assumption they rest on

- **Claim** — Zettelkasten, Maps of Content, PARA, and Johnny.Decimal have zero controlled
  evaluations of retrieval success, time-to-find, or error rate. Meanwhile the measured personal-
  information-management literature finds that folder navigation, not search, dominates re-finding
  of one's own material — the opposite of what link-graph-first PKM tooling assumes.
- **Evidence tier** — A for the PIM literature; **C / none** for the PKM methods.
- **Support** — [Whittaker, "Personal information management: From information consumption to
  curation," ARIST 45(1):1–42,
  2011](https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/aris.2011.1440450108) — the
  canonical review; reports that people keep too much and that loosely-organized piles often
  outperform carefully-built filing structures. [Bergman et al., "Search is the future? The young
  search less for files," Proc. ASIS&T
  2019](https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/pra2.29) — 289 participants
  retrieving 1,557 of their own files. Bergman & Whittaker's Elicited Personal Information
  Retrieval line of work
  ([IJHCS 2014](https://www.sciencedirect.com/science/article/abs/pii/S107158191400127X)) is where
  the navigation-dominates finding comes from. The only academic empirical study of a modern PKM
  tool I found is [Ferreira et al., "How People Manage Knowledge in their 'Second Brains': A Case
  Study with Industry Researchers Using Obsidian," arXiv:2509.20187,
  Sept 2025](https://arxiv.org/abs/2509.20187) — qualitative, no retrieval-success rates; its one
  transferable finding is that **intended retrieval strategy determines how people structure the
  base**.
- **Date sensitivity** — Low for the PIM findings (stable over 15 years of replication); the
  Bergman 2024 follow-up ([HCI journal](https://www.tandfonline.com/doi/full/10.1080/07370024.2024.2379838))
  argues the navigate-vs-search split is a stable individual trait, not a tooling artifact.
- **Confidence** — High that the PKM-method evidence is absent (two independent searches, nothing
  found). Medium on the PIM findings: they predate LLM-assisted retrieval entirely, and an agent
  grepping a corpus is not a human browsing folders.
- **Counter-evidence** — Specific percentages circulating for the navigation/search split (e.g.
  "navigation in ~86% of retrievals," "search 4–15%") could not be verified at the primary papers
  in this pass and should not be cited as figures. The strongest claim available for
  Zettelkasten is Luhmann's personal output — an n=1 anecdote. The PIM literature also predates
  the case where the retriever is an agent, which is exactly the operator's case, so its
  applicability is an inference.

### F-W4-23 — Retrieval advantages over a knowledge base are a scaling property; at small corpus size keyword search is a hard baseline

- **Claim** — Graph-based retrieval's advantage over standard RAG emerges with corpus growth
  rather than existing at small scale, and lexical BM25 remains a robust baseline that dense
  retrievers frequently fail to beat out of domain — so the sophistication of a personal
  knowledge base's retrieval layer should track its size, not its ambition.
- **Evidence tier** — A.
- **Support** — [Thakur, Reimers, Rücklé, Srivastava, Gurevych, "BEIR: A Heterogeneous Benchmark
  for Zero-shot Evaluation of Information Retrieval Models," NeurIPS 2021 D&B,
  arXiv:2104.08663](https://arxiv.org/abs/2104.08663) — 18 datasets, 10 systems; BM25 is a robust
  out-of-domain baseline and dense retrievers generalize poorly.
  ["When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented
  Generation," arXiv:2506.05690, Jun 2025](https://arxiv.org/pdf/2506.05690) is the
  corpus-size-controlled study: Small ~56k / Medium ~603k / Large ~1,132k tokens; standard RAG
  complex-reasoning accuracy falls **58.64% → 43.20%** across that range while GraphRAG stays flat
  — i.e. the gap is smallest at the small end. _(These two figures are reported second-hand from
  the abstract and were not verified against the paper's tables; treat as indicative.)_
  [Li, Jin, Xiong et al., "Long Context vs. RAG for LLMs," arXiv:2501.01880,
  Jan 2025](https://arxiv.org/abs/2501.01880) finds the divergence in published results is
  explained by the evaluating model's long-context capacity — strong long-context models often do
  better with the full corpus in context than with retrieval.
- **Date sensitivity** — High. Retrieval results move fast; BEIR is 2021 and its dense-retriever
  lineup is obsolete, though the BM25-is-hard-to-beat finding has replicated repeatedly.
- **Confidence** — Medium. The direction is well supported; the specific small-corpus claim is an
  inference from the low end of a study designed to demonstrate the high end.
- **Counter-evidence** — [GraphRAG (Edge et al., Microsoft Research,
  arXiv:2404.16130)](https://arxiv.org/abs/2404.16130) does show large wins, but explicitly for
  _global sensemaking_ questions ("what are the themes across this corpus") over ~1M-token
  datasets — a question type a research repository genuinely has. On the other side,
  ["Comparing Lexical and Semantic Vector Search Methods When Classifying Medical Documents,"
  arXiv:2505.11582](https://arxiv.org/abs/2505.11582) found off-the-shelf semantic search
  _slightly worse_ and significantly slower than a bespoke lexical model on a specialist corpus.
  **No study I found evaluates retrieval over a few-hundred-document single-author corpus, and no
  study compares semantic search against plain grep at any scale.**

### F-W4-24 — Mature provenance and confidence standards exist in four adjacent fields, all of them mandates rather than evidence

- **Claim** — Intelligence analysis (ICD 203/206), scientific data management (FAIR),
  evidence synthesis (PRISMA 2020, PRISMA-P), and evidence grading (GRADE) each specify what a
  research document must state about source quality and uncertainty — but none of them is
  supported by evidence that following it improves accuracy, and none addresses assertion-level
  dating.
- **Evidence tier** — A for what the standards require; **none** for whether they work.
- **Support** — [ICD 203, Analytic
  Standards](https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf)
  (issued 2007, amended 21 Jan 2022): nine Analytic Tradecraft Standards, two of which map
  directly onto the operator's problem — _"Properly describes quality and credibility of
  underlying sources, data, and methodology"_ and _"Properly expresses and explains uncertainties
  associated with major analytic judgments"_ — plus a standard requiring analysts to **explain
  change to or consistency with previous judgments**, which is the closest thing in any standard
  to a drift-management requirement.
  [ICD 206](https://www.dni.gov/files/documents/ICD/ICD%20206.pdf) specifies the source summary
  statement. [Kent's Words of Estimative
  Probability](https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-8-no-4/words-of-estimative-probability/)
  is the canonical statement of why estimative language must map to fixed probability bands.
  [FAIR (Wilkinson et al., Scientific Data 3:160018, 2016)](https://www.nature.com/articles/sdata201618) principle **R1.2** requires detailed
  provenance metadata — in one sentence, with no specification of what it must contain.
  [PRISMA 2020](https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-021-01626-4)
  newly added items **15 and 22**, requiring reporting of both the method for and the result of a
  certainty assessment per outcome; [PRISMA-P](https://www.equator-network.org/reporting-guidelines/prisma-protocols/)
  is a 17-item pre-registration checklist. [GRADE](https://www.gradeworkinggroup.org/) defines
  four certainty levels (high/moderate/low/very low) rated down for risk of bias, inconsistency,
  indirectness, imprecision, and publication bias.
- **Date sensitivity** — Low. These are stable institutional standards.
- **Confidence** — High on content, high that efficacy evidence is thin.
- **Counter-evidence** — Two real measurements exist and both are cautionary. ["Better Together:
  Reliable Application of the Post-9/11 and Post-Iraq US Intelligence Tradecraft Standards
  Requires Collective Analysis"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6330287/) finds
  **individual analysts apply ICD 203 unreliably** and that collective judgment is needed — a
  direct problem for a one-person operation. A [2025 meta-epidemiological
  study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11795886/) measures how poorly PRISMA 2020
  is actually complied with in practice. And [a 2025
  study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12662624/) measuring whether GRADE use and
  protocol registration correlate with methodological quality is the nearest thing to positive
  evidence that any of this pays off. All four standards assume institutional review gates the
  operator does not have.

---

## Gaps

These are the things I could not establish. Several are central to the workstream.

1. **No controlled study of documentation-quality maintenance in a code-free knowledge
   repository exists.** Not one. Every controlled study I found — McMillan ×2, Gloaguen et al.,
   Chatlatanagulchai et al. — uses a code repository, a code-derived dependent variable (AST
   annotation presence, test-suite pass, SQL correctness), and a task that terminates in
   executable output. The entire measured literature on agent context files depends on having a
   compiler or a test suite as the oracle. A research repository has no oracle. **What would
   settle it:** a factorial study with a prose-level dependent variable — e.g. an
   independently-scored contradiction count or citation-accuracy rate across a corpus, measured
   with and without an index/CONTEXT.md convention. Nobody has built one.

2. **Doc-drift detection exists only where code is the oracle. For prose asserting facts about an
   environment, nothing measures it.** Code-comment inconsistency detection has a real research
   literature with real numbers (F-W4-12, F-W4-13) precisely because the code is ground truth.
   The operator's live problem — a rules file naming a model that isn't running, a reference to an
   uninstalled subsystem — has no oracle in that literature: the referent is a runtime
   environment, not a symbol in the same repository. **What would settle it:** measured
   precision/recall for an auditor checking prose assertions against a machine-readable
   environment description. I found no such measurement, no benchmark, and no tool. The only
   adjacent artifact is Chatlatanagulchai et al.'s _suggestion_ (§5.1) that researchers "design a
   linter for agent context files which could verify that the commands listed in the Build and Run
   section match the actual scripts in package.json or Makefile" — explicitly future work. Note
   that this specific class is the _easy_ case: model names, installed plugins, and file paths are
   all machine-checkable. It is unbuilt, not unbuildable.

2b. **No measured evidence that executable documentation actually catches drift.** Doctests
(Python `doctest`, `cargo test --doc`, Go testable examples), `mdbook test`, `mdsh --frozen`,
embedme, and Doc Detective all _assert_ the mechanism in their own documentation — Python's
stdlib docs name "checking that a module's docstrings are up-to-date" as the first use case, and
the Go blog states executable examples "guarantee that the information will not go out of date."
**Not one of them, and no third party, publishes a catch rate, a controlled comparison of
projects with versus without doctests, or defect-escape data.** Two known coverage holes are
documented: Go examples without an `// Output:` comment are compiled but never executed, and
`mdbook test` only supports Rust. **What would settle it:** a study of projects adopting doctests
measuring doc-defect rate before and after. This is the largest evidentiary hole in the
code-side half of this workstream.

3. **No measurement of whether a "CONTEXT.md per subject" convention (C-140) helps or hurts.**
   The nearest evidence (F-W4-03) is a repo-level ablation on Python code. **What would settle
   it:** the operator can measure C-142's own 30–40% claim locally in a day — run the same
   research task on two subject directories, one with and one without a CONTEXT.md, and compare
   `/context` token counts and output quality. It is a one-person A/B, not a research programme.
   Nobody has published it because nobody outside this use case cares.

4. **No cross-repository consistency evidence.** The mechanisms are well specified (F-W4-18) and
   the empirical picture is completely absent. Nobody has published "N% of repositories
   instantiated from template T are more than K commits behind," no drift rate for synced files,
   and no evaluation of `.github` defaults, `cruft check`, or symlinked shared rules. The related
   claim that monorepos keep documentation more consistent than polyrepos is **unsupported by any
   measurement I could find** — the only quantified monorepo/polyrepo source is vendor-produced
   and measures PR cycle time, not documentation.

4b. **No measured outcome for moving docs from hand-written to generated.** F-W4-17. Stripe
describes the machinery in detail with zero numbers; Google publishes survey and usage numbers
but no generated-versus-hand-written comparison; Diátaxis offers testimonials. If Phase C wants
to claim that generating reference documentation reduces drift, that claim is currently
unevidenced — and Google's own book argues the opposite for their context.

5. **Instruction files have never been evaluated on the outcome that would justify them.** Every
   study measures task success or trivial-convention compliance. Nobody has measured whether a
   context file improves **code quality, security, style conformance, or documentation
   accuracy** — the reasons practitioners actually write them. Gloaguen et al. name this as
   explicit future work. Until someone does, "context files don't help" means "context files
   don't help you close more tickets," which is not the same claim.

6. **The >500-line and >150-instruction regimes are unmeasured for config files.** McMillan's
   affirmative nulls stop at 500 lines; IFScale's degradation curve starts mattering above ~150
   instructions but measures a different task shape entirely. The band where the corpus's fear
   (C-035) and the corpus's prescription (C-107, C-170's multi-paragraph tier blocks) actually
   live — a few hundred lines carrying dozens of instructions across a hierarchy of files — is
   the band nobody has cleanly tested.

7. **Citation-verification-as-a-maintenance-pass does not exist as tooling and is unmeasured as a
   workflow.** All the machinery — ALCE's citation precision/recall, SAFE, RARR — was built for
   generation time or benchmark time. **I found no tool that audits an existing prose corpus for
   whether its citations support the claims attached to them.** The operator's exact failure mode
   (a citation that resolves but does not say what it is cited for) is coded as a distinct
   category in exactly one study I found (F-W4-10, "misgrounded"), and that study evaluates vendor
   products rather than a procedure. AttributionBench (F-W4-20) says a _general_ supported/
   not-supported classifier tops out near 80% macro-F1, but nobody has measured a narrow,
   single-domain, consistent-citation-format checker — which is a materially easier problem.
   **What would settle it:** a measured false-negative rate for an adversarial citation-checking
   agent run against a corpus with known planted errors. The operator's own VA corpus has the raw
   material (the 40-of-109 misstatement finding gives a base rate and a labelled set) and it would
   be the most transferable artifact in this entire workstream.

8. **Organizational knowledge-base staleness has no research literature — it is a marketing
   genre.** Every circulating figure I traced ("20–40% of knowledge bases contain irrelevant
   articles," "product documentation holds for 90 days," "teams lose 25% of their time hunting for
   answers") resolves to vendor content with no cited study. Phase C should not use any of them.
   The one defensible datum is a first-party vendor survey (Atlassian State of Teams 2025: 56% of
   employees still have to ping someone or schedule a meeting to get information) and it must be
   labelled as such. **Wikimedia is the only place where prose-corpus decay is properly measured**
   (F-W4-21), and it is measured because Wikipedia has full revision history, a formal reliability
   policy, and a research team. None of those transfer.

9. **No note-organization convention has ever been evaluated** (F-W4-22). Zero controlled studies
   of Zettelkasten, MOC, PARA, or Johnny.Decimal; zero measurements of orphan-note or link-rot
   detection improving anything, despite the tooling existing in Obsidian and Logseq. **What would
   settle it:** an EPIR-style protocol (the PIM literature's own method — ask someone to retrieve
   specific items from their own corpus and time it) applied to a corpus before and after adopting
   an index convention. It is a small, cheap study that nobody has run.

10. **Nobody has evaluated retrieval at the scale a personal research repository actually
    operates at.** Every RAG evaluation I found uses ≥50k tokens, most ≥1M. There is **no measured
    comparison of semantic search against plain grep at any corpus size**, which is the single
    most decision-relevant comparison for a few-hundred-document repo. The "for corpora under
    10,000 documents, in-memory BM25 is fast and effective" guidance circulating in blog posts is
    practitioner advice with no cited study.

11. **Two of my strongest sources share one author.** F-W4-01, F-W4-04, and F-W4-09 all rest on
    preprints by Damon McMillan (HxAI Australia), unreviewed and self-citing. The methodology is
    unusually transparent — pre-registered analysis plan, frozen dataset, published condition
    matrix, affirmative-null Bayes factors, and a limitations section that argues against his own
    headline — which is why I weight them Tier A/B rather than C. But a single-author preprint
    line is a real concentration risk, and the McMillan size-null directly contradicts the vendor.
    Independent replication is the thing that would settle it and it does not exist.

12. **Leads surfaced but not verified in this pass.** Recorded so Phase C does not mistake them
    for evidence, and so a later pass knows where to look: arXiv 2606.09090 ("Context Rot in
    AI-Assisted Software Development: Repurposing Documentation Consistency for AI Configuration
    Artifacts" — sounds directly on-topic for this workstream), 2604.03173 (reference
    hallucinations in deep-research agents), 2605.06635 (source attribution in deep-research
    agents), 2606.00898 (citation grounding via legal citation graphs), 2604.03159 (BibTeX
    citation hallucinations). **None were fetched or read. Treat as unverified.** Separately, a
    widely-repeated claim that GitHub Copilot code review reads only the first 4,000 characters of
    a custom instruction file **could not be confirmed** against the July 2026 changelog and sits
    next to a June 2026 changelog announcing removal of a character limit — do not cite it.

---

## Implications for the Operator

_My inferences. Not findings. Phase C does the reasoning._

- The evidence supports a **content test, not a length budget**, for every instruction file:
  keep a line only if nothing else in the repository states it. That reframes the operator's
  global `~/.claude/CLAUDE.md`, which currently restates the directory layout, the agent roster,
  and the rules hierarchy — all derivable by reading the directory. It is the exact content class
  Gloaguen et al. measured as inert and Anthropic's own table lists under "❌ Exclude."

- The drift instance named in my brief (a rules file asserting a model that isn't running; a
  reference to an uninstalled subsystem) is not a discipline failure — it is the predicted
  outcome of a 4:1 add/delete ratio on a file nothing verifies. Nothing in the measured
  literature detects it. If the operator wants it caught, the mechanism has to be built, and it
  has to be a check that _executes_ — the same argument F-W4-07 makes about hooks, applied to
  prose.

- For the code-free repositories, the single most transferable move suggested by the evidence is
  the one nobody has published: turn the citation-verification finding from the operator's own
  VA corpus into a measured harness. It is the only place where the operator has ground truth, a
  known base rate, and a repeatable, sellable procedure. Every published source in this
  workstream had to borrow an oracle from a compiler; the operator would be building one.

- If such a checker gets built, F-W4-12 is the design constraint. A naive "read these docs and
  tell me what's wrong" prompt produced a 90%+ flag rate against an 11% real base rate. Both
  measured fixes cost something: filtering buys a usable flag rate at ~0.63 precision, grounding
  in an executable check buys 0.88 precision at 0.21 recall. For a single reviewer, precision is
  the axis that matters — a checker with a 30% noise rate is one the operator will stop reading,
  which is worse than not having it.

- The measured drift picture (F-W4-13: 28.9% of popular repos carry an outdated code reference
  right now, mean persistence 4.7 years, ~55% survival after one month) says drift is not an
  event to be caught but a steady state to be budgeted for. That reframes the question from "how
  do I stop drift" to "what is the small set of assertions where drift is actually expensive," and
  the operator's own instances (a wrong model name, a missing subsystem) are all in the
  machine-checkable class.

- F-W4-22 and F-W4-23 both cut against elaboration on the knowledge-repo side. The measured PIM
  literature favours navigation over search; the measured retrieval literature says lexical
  baselines are hard to beat at small scale and that graph/semantic advantages are scaling
  properties. Combined with F-W4-09's partitioned-index result, the evidence points toward a
  cheap directory-and-index convention rather than an ontology or an embedding pipeline — but I
  want to be explicit that no study has evaluated any of this at a few-hundred-document scale, so
  this is an inference from adjacent evidence, not a supported recommendation.

- Of the four mature provenance standards (F-W4-24), the one item that maps directly onto the
  operator's live problem is ICD 203's requirement to **explain change to or consistency with
  previous judgments**. Nothing in FAIR, PRISMA, or GRADE addresses assertion-level dating at all.
  If Phase C wants a provenance convention, that is the one clause worth stealing — and the
  caution attached to it is that individual analysts have been measured applying ICD 203
  unreliably, in an institution built around review gates the operator does not have.

- F-W4-04 argues that document conventions cannot be held by instruction files across long runs
  any more than code conventions can. If the operator wants a research repo's dating, provenance,
  and citation conventions to hold, the enforcement has to sit at the file-write boundary
  (PostToolUse hook, pre-commit check), not in a CONTEXT.md.

- F-W4-09 weakly favours a partitioned index over a growing monolith for a corpus that keeps
  growing — but the evidence is an analogy from database schemas, and the same paper found format
  choice irrelevant. That argues for the cheapest possible index convention, not an ontology.

---

## Sources

**Read in full** (5):

1. **McMillan, D. (2026).** "Instruction Adherence in Coding Agent Configuration Files: A
   Factorial Study of Four File-Structure Variables." arXiv:2605.10039, 11 May 2026.
   <https://arxiv.org/abs/2605.10039> — **Tier A.** Trusted for methodological transparency:
   pre-registered analysis plan, published full condition matrix, frozen dataset, Bayesian
   companion with a prior-sensitivity sweep, and a limitations section that undercuts its own
   headline. Distrusted for: single author, single affiliation, no peer review, trivial dependent
   variable, single-turn harness.
2. **Gloaguen, T., Mündler, N., Müller, M., Raychev, V., Vechev, M. (2026).** "Evaluating
   AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" arXiv:2602.11988v2,
   23 Jun 2026. ETH Zurich + LogicStar.ai. <https://arxiv.org/abs/2602.11988> — **Tier A.** The
   single most decisive source in this workstream. Trusted for: purpose-built benchmark,
   four models, two benchmarks, extensive ablations (length, category, generating model, prompt,
   contamination), and a result that contradicts the authors' own field's standard advice.
   Distrusted for: Python only.
3. **Chatlatanagulchai, W., Li, H., Kashiwa, Y., Reid, B., et al. (2025).** "Agent READMEs: An
   Empirical Study of Context Files for Agentic Coding." arXiv:2511.12884, Nov 2025.
   <https://arxiv.org/abs/2511.12884> — **Tier A** for descriptive statistics. Trusted for scale
   (2,303 files, 1,925 repos, 10,659 commits) and statistical care (Mann-Whitney U with Cliff's
   delta throughout). "Context debt" is the authors' framing, not a measured harm.
4. **Anthropic. "How Claude Code remembers your project"** (memory / CLAUDE.md docs), retrieved
   2026-08-01. <https://code.claude.com/docs/en/memory> — **Tier A (vendor, primary).** Trusted
   as the authoritative source on its own product's mechanisms; distrusted where it makes
   unsourced effect claims (the size→adherence assertion).
5. **Anthropic. "Best practices for Claude Code,"** retrieved 2026-08-01.
   <https://code.claude.com/docs/en/best-practices> — **Tier A (vendor, primary).** Source of the
   verbatim text behind C-034 and C-035. Same caveat as (4).

**Sampled** (30):

_Doc-drift detection and docs CI_

A1. **Xu, Wahab, Holmes, Lemieux (UBC). "DocPrism," arXiv:2511.00215**, rev. 2026-07-29.
<https://arxiv.org/abs/2511.00215> — Tier A. The key false-positive source. Trusted for
multi-language real-world (not synthetic) evaluation and for reporting its own naive-baseline
failure honestly. Preprint.
A2. **Kiecker, Spark, Reuter, Ziegler, Grunske. "Cascade," arXiv:2604.19400**, 2026-04-21.
<https://arxiv.org/html/2604.19400> — Tier A. Test-generation grounding; new 885-pair benchmark
with developer-confirmed labels. Preprint.
A3. **Tan, Wagner, Treude. "Detecting outdated code element references," EMSE / arXiv:2212.01479.**
<https://arxiv.org/abs/2212.01479> — Tier A. Best base-rate and persistence data. Trusted partly
_because_ it reports its own developer-validated false positives.
A4. **Panthaplackel, Li, Gligoric, Mooney. AAAI 2021, arXiv:2010.01625.**
<https://arxiv.org/abs/2010.01625> — Tier A. The canonical JIT comment-inconsistency dataset
(40,688 examples, 1,518 Java projects); F1 79.6 full test / 87.1 on the manually cleaned subset —
note which number is quoted.
A5. **Dau, Guo, Bui. "DocChecker," EACL 2024 Demos, arXiv:2306.06347.**
<https://arxiv.org/abs/2306.06347> — Tier A. Useful for the LLM-baseline contrast (GPT-3.5 3-shot
61.4% vs fine-tuned 72.3%).
A6. **Gong, Pinna, Bian, Zhang. MSR 2026, arXiv:2601.04886.**
<https://arxiv.org/html/2601.04886v2> — Tier A. AI-agent PR message-code inconsistency; "Phantom
Changes." No human-authored control group.
A7. **GitLab documentation testing.** <https://docs.gitlab.com/development/documentation/testing/> —
Tier A (primary). The most complete published production docs-CI inventory found.
A8. **MkDocs configuration** <https://www.mkdocs.org/user-guide/configuration/>; **Docusaurus
config** <https://docusaurus.io/docs/api/docusaurus-config>; **Sphinx sphinx-build**
<https://www.sphinx-doc.org/en/master/man/sphinx-build.html>; **lychee**
<https://github.com/lycheeverse/lychee> — Tier A (primary tool docs). Source of the specific
default-behavior gotchas in F-W4-15.
A9. **Datadog, "How we use Vale to improve our documentation editing process," 2024-02-14.**
<https://www.datadoghq.com/blog/engineering/how-we-use-vale-to-improve-our-documentation-editing-process/>
— Tier C. Real production experience, zero quantified outcomes. Cited only as a negative.
A10. **Python `doctest`** <https://docs.python.org/3/library/doctest.html>; **Cargo test**
<https://doc.rust-lang.org/cargo/commands/cargo-test.html>; **"Testable Examples in Go"**
<https://go.dev/blog/examples>; **mdBook test** <https://rust-lang.github.io/mdBook/cli/test.html>;
**mdsh** <https://github.com/zimbatm/mdsh> — Tier A (primary) for mechanism, **no evidence** for
efficacy. Source of the coverage-hole details (Go examples without `// Output:`; mdbook test is
Rust-only; mdsh is regex-based and says so).

_Generated vs. hand-written, and cross-repo_

A11. **_Software Engineering at Google_, Ch. 10 "Documentation."**
<https://abseil.io/resources/swe-book/html/ch10.html> — Tier A/B. Real internal survey and usage
numbers; self-reported and unauditable.
A12. **Stripe, "How API changes flow into Stripe's developer products," 2026-06-15.**
<https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products> — Tier B (vendor
engineering blog). Detailed mechanism, explicitly zero metrics.
A13. **Diátaxis.** <https://diataxis.fr/> — Tier C. Useful taxonomy; the site offers testimonials,
not measurement, and says so.
A14. **cruft** <https://cruft.github.io/cruft/>; **GitHub default community health files**
<https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file>;
**repo-file-sync-action** <https://github.com/Redocly/repo-file-sync-action> — Tier A (primary).
Mechanisms only; no efficacy data exists for any of them.
A15. **Backstage TechDocs.** <https://backstage.io/docs/features/techdocs/> — Tier B. Adoption
numbers (5,000+ sites at Spotify), not accuracy numbers.

_Knowledge-repo coherence (no-code case)_

A16. **Semnani, Burapacheep, Khatua, Atchariyachanvanit, Wang, Lam. "Detecting Corpus-Level
Knowledge Inconsistencies in Wikipedia with LLMs," EMNLP 2025 Main, arXiv:2509.23233.**
<https://arxiv.org/abs/2509.23233> — Tier A. **The most transferable open-field source in this
file.** Peer-reviewed, authentic contradictions, negative headline about automation.
A17. **"Contradiction Detection in RAG Systems: Evaluating LLMs as Context Validators,"
arXiv:2504.00180.** <https://arxiv.org/html/2504.00180v1> — Tier B. High precision, low recall —
the failure mode that matters.
A18. **de Marneffe, Rafferty, Manning. "Finding Contradictions in Text," ACL 2008.**
<https://nlp.stanford.edu/pubs/contradiction-acl08.pdf> — Tier A. The foundational typology; cited
for the structural claim, not for its (now dated) numbers.
A19. **Wikimedia Research: Reference Quality in English Wikipedia** (data through Jan 2022)
<https://meta.wikimedia.org/wiki/Research:Reference_Quality_in_English_Wikipedia>; published as
**Baigutanova et al., WWW 2023** <https://arxiv.org/pdf/2303.05227> — Tier A. The only rigorous
longitudinal measurement of prose-corpus reference quality that exists.
A20. **Redi, Fetahu, Morgan, Taraborelli. "Citation Needed," WWW 2019, arXiv:1902.11116.**
<https://arxiv.org/abs/1902.11116> — Tier A. Empirical taxonomy of _why_ a statement needs a
citation. The model-performance figures were not extracted in this pass.
A21. **Pew Research Center, "When Online Content Disappears," 2024-05-17.**
<https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/> — Tier A. Link
rot: 38% of 2013 pages gone by Oct 2023; 23% of news pages contain a broken link.
A22. **Nyayachavadi, Zhu, Madhyastha. "Characterizing 'Permanently Dead' Links on Wikipedia," ACM
IMC 2022.** <https://dl.acm.org/doi/10.1145/3517745.3561451> — Tier A. ~3% of "permanently dead"
links still work; many URLs are first archived only after they break.
A23. **Li et al. "AttributionBench," Findings of ACL 2024, arXiv:2402.15089.**
<https://arxiv.org/abs/2402.15089> — Tier A. The ~80% macro-F1 ceiling on automated
citation-support checking.
A24. **Gao, Yen, Yu, Chen. ALCE, EMNLP 2023, arXiv:2305.14627**
<https://arxiv.org/abs/2305.14627>; **Gao et al. RARR, arXiv:2210.08726**
<https://arxiv.org/abs/2210.08726> — Tier A. Citation precision/recall definitions and the closest
architecture to a corpus-audit pass.
A25. **Dahl, Magesh, Suzgun, Ho. "Large Legal Fictions," Journal of Legal Analysis,
arXiv:2401.01301.** <https://arxiv.org/abs/2401.01301> — Tier A. >800,000 verifiable legal
questions; hallucination 58% (GPT-4) to 88% (Llama 2). Jan 2024 — the models are historical.
A26. **Whittaker, ARIST 45(1):1–42, 2011**
<https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/aris.2011.1440450108>; **Bergman et al.,
Proc. ASIS&T 2019** <https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/pra2.29>; **Bergman &
Whittaker, IJHCS 2014**
<https://www.sciencedirect.com/science/article/abs/pii/S107158191400127X> — Tier A. The measured
PIM literature. Predates agent-mediated retrieval entirely.
A27. **Ferreira, Segura, Souza, Brasil. "How People Manage Knowledge in their 'Second Brains',"
arXiv:2509.20187, Sept 2025.** <https://arxiv.org/abs/2509.20187> — Tier B. The only academic
empirical study of a modern PKM tool found; qualitative, no retrieval rates.
A28. **Thakur, Reimers, Rücklé, Srivastava, Gurevych. BEIR, NeurIPS 2021 D&B, arXiv:2104.08663.**
<https://arxiv.org/abs/2104.08663> — Tier A. BM25 as a hard out-of-domain baseline. 2021; the
dense-retriever lineup is obsolete.
A29. **"When to use Graphs in RAG," arXiv:2506.05690** <https://arxiv.org/pdf/2506.05690>;
**Edge et al. GraphRAG, arXiv:2404.16130** <https://arxiv.org/abs/2404.16130>; **"Long Context vs.
RAG for LLMs," arXiv:2501.01880** <https://arxiv.org/abs/2501.01880> — Tier A/B. The
corpus-size-controlled comparison and its bounds. **The 58.64%→43.20% figures are second-hand from
the abstract and were not verified against the paper's tables.**
A30. **ICD 203** <https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf>;
**ICD 206** <https://www.dni.gov/files/documents/ICD/ICD%20206.pdf>; **Kent, Words of Estimative
Probability**
<https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-8-no-4/words-of-estimative-probability/>;
**FAIR (Wilkinson et al., Sci Data 3:160018, 2016)** <https://www.nature.com/articles/sdata201618>;
**PRISMA 2020**
<https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-021-01626-4>;
**GRADE** <https://www.gradeworkinggroup.org/> — Tier A as standards, **no efficacy evidence**.
Counterweight: **"Better Together," PMC6330287**
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6330287/> (individual analysts apply ICD 203
unreliably).

_Original sampled set_

6. **Jaroslawicz, D., Whiting, B., Shah, P., Maamari, K. (2025).** "How Many Instructions Can LLMs
   Follow at Once?" arXiv:2507.11538, Distyl AI. <https://arxiv.org/abs/2507.11538> — Tier A;
   extracted full text and read the results/degradation/primacy sections. Model lineup is July
   2025 and now historical.
7. **Chroma Research. "Context Rot: How Increasing Input Tokens Impacts LLM Performance,"**
   14 Jul 2025. <https://www.trychroma.com/research/context-rot> — Tier B. Vendor with a
   commercial stake in retrieval, but transparent and publishing a result that complicates its
   own product story. 18 models, July 2025 vintage.
8. **McMillan, D. (2026).** "Structured Context Engineering for File-Native Agentic Systems."
   arXiv:2602.05447. <https://arxiv.org/abs/2602.05447> — Tier B. 9,649 experiments but a
   SQL-schema proxy, same single-author concentration risk as (1).
9. **Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., Ho, D. E. (2024).**
   "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools."
   arXiv:2405.20362, Stanford RegLab/HAI. <https://arxiv.org/abs/2405.20362> — Tier A;
   preregistered. Numbers are May 2024 and stale; the correct/grounded failure taxonomy is the
   durable part.
10. **Wei, J., et al. (2024).** "Long-form factuality in large language models" (SAFE / LongFact).
    arXiv:2403.18802, Google DeepMind. <https://arxiv.org/abs/2403.18802> — Tier A. Two model
    generations old.
11. **Cursor. Rules documentation,** retrieved 2026-08-01. <https://cursor.com/docs/context/rules>
    — Tier A (vendor, primary). Establishes `.cursor/rules/*.mdc` as the current mechanism and
    that `.cursorrules` no longer appears in the docs at all.
12. **Liu, N. F., et al. (2024).** "Lost in the Middle: How Language Models Use Long Contexts."
    TACL 12:157–173. — Tier A; cited via (1), which tested its U-shape prediction at config-file
    scale and did not reproduce it.
13. **Wallace, E., et al. (2024),** "The Instruction Hierarchy," arXiv:2404.13208, and **Geng, Y.,
    et al. (2026),** "Control Illusion: The Failure of Instruction Hierarchies in Large Language
    Models," AAAI 2026, arXiv:2502.15851 — Tier A; cited via (1). Establish that formal
    instruction-priority schemes behave unreliably, which is the theoretical grounding for the
    inter-file conflict null.
14. **damiencharlotin.com/hallucinations** (AI Hallucination Cases database) — **not retrievable**;
    returned HTTP 403 on 2026-08-01. Excluded rather than cited second-hand.
