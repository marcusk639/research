# W9 — Composition (Solo-Operator Capacity, WIP, and Review Economics)

_Phase B findings | Generated: 2026-08-01 | Sources consulted: 41 | Read in full: 7_

**Scope note.** Per the W9 sequencing instruction, this file does **not** compose W1–W8 findings —
those workstreams ran in parallel and their outputs were not read. What follows is the standalone
evidence base Phase C will compose with: published evidence on solo-operator review capacity,
context-switching cost, WIP limits, whether AI changes review economics, and documented personal
operating-system designs. The central question is contradiction **X-04**.

---

## Ledger Verdicts

| Claim ID | Verdict                              | Current value / correction                                                                                                                                                                                                                                                        | Evidence tier                                   | Source                                                                                                                                                                                                                                                                                                                               | Notes                                                                                                                                                                                                                                                                                                                          |
| -------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C-003    | **CONFIRMED** (qualified)            | Holds as stated, and now has Tier A field evidence behind it that did not exist when asserted. Qualification: it is conditional on the operator actually being the reviewer of record. Cost binds first only below a throughput floor the operator has already passed.            | A                                               | [He et al., arXiv:2607.01904 (2026-07-03)](https://arxiv.org/html/2607.01904v1)                                                                                                                                                                                                                                                      | 802 devs / 196,212 PRs. When generation doubled, PR volume grew 3.1× while the reviewer pool grew 1.5×; per-reviewer load ~2.0×. The org did not add review capacity — it degraded review. See X-04.                                                                                                                           |
| C-029    | **CONFIRMED**                        | Near-verbatim. Osmani's published sentence is "Code review became the new bottleneck" (2026-01-28); a companion piece (2026-01-05) states "When output increases faster than verification capacity, review becomes the rate limiter."                                             | C (opinion) — the underlying data he cites is B | [Osmani, "The 80% Problem in Agentic Coding" (2026-01-28)](https://addyo.substack.com/p/the-80-problem-in-agentic-coding); [Osmani, "Code Review in the Age of AI" (2026-01-05)](https://addyo.substack.com/p/code-review-in-the-age-of-ai)                                                                                          | Osmani himself is Tier C (practitioner essay). He sources the claim to Faros AI / DORA-adjacent telemetry and Cortex's State of AI Benchmark 2026 (~18% larger PRs, incidents/PR +24%, change-failure +30%). He gives **no** reviewer-capacity number.                                                                         |
| C-084    | **UNVERIFIED**                       | No measured study, no telemetry, and no structured survey with an N establishes a concurrent-session ceiling. The "3+" figure is folk consensus with a probable vendor origin. Published numbers found: Anthropic 3–5 (vendor tip), practitioner blogs 2–4, 3–5, 3–6, ≤2, 5–7.    | C                                               | [Anthropic, Claude Code power-user tips (2026-06-25)](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips); [engineered.at (2026-04)](https://engineered.at/articles/your-parallel-agent-limit); [codewithseb (2026-04)](https://www.codewithseb.com/blog/parallel-claude-code-sessions-git-worktrees-guide) | **"Multiple practitioners independently"** is the part that fails. The sources are not independent — several trace to Anthropic's own 3–5 guidance (attributed to Boris Cherny), and Anthropic frames 3–5 as a productivity _floor_ ("the biggest productivity unlock"), not a supervision _ceiling_. Date-stamped 2026-08-01. |
| C-085    | **CONFIRMED** (attribution)          | Quote is real, marginally misquoted. Original: "I believe I'm ultimately responsible for the code **that goes into** a PR with my name on it, regardless of how it was produced." — Chris Dzombak, 2025-08-08.                                                                    | C                                               | [Dzombak, "Getting Good Results from Claude Code" (2025-08-08)](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/)                                                                                                                                                                                         | Single individual's stated norm. It is an accountability position, not evidence about capacity. Flagged per evidence standards: **single-person source**.                                                                                                                                                                      |
| C-154    | **UNVERIFIED**                       | No published evidence establishes that a 15-minute weekly cadence is adequate to detect review-capacity or quality drift. No evidence refutes it either. The one thing the evidence does say: the metrics such a cadence should watch are not the ones C-154 lists (see F-W9-16). | —                                               | [Heylighen & Vidal, _Long Range Planning_ 41(6), 2008](http://pespmc1.vub.ac.be/Papers/GTD-cognition.pdf); [arXiv:2607.01904](https://arxiv.org/html/2607.01904v1)                                                                                                                                                                   | The weekly-review construct itself (GTD's core throttle) has **no empirical validation** — Heylighen & Vidal state plainly that "no academic papers have investigated this method." C-154's checklist is entirely cost/quality-of-output; it contains no review-capacity indicator.                                            |
| C-186    | **UNVERIFIED**                       | Same as C-154. The v2 cadence adds a routing-discipline check but still contains no review-load or review-latency indicator.                                                                                                                                                      | —                                               | as above                                                                                                                                                                                                                                                                                                                             | Duplicate of C-154 in substance; the two documents disagree only in checklist items, not in cadence or duration.                                                                                                                                                                                                               |
| C-189    | **UNVERIFIED** / partly out of scope | The execution ordering is an internal plan sequence, not a web-verifiable proposition. Its cost/routing items belong to **W5**, its CI/Judge-Builder items to **W3**. The only W9-relevant property — that "ongoing weekly review" is sequenced **last** — is unsupported.        | —                                               | [arXiv:2607.01904](https://arxiv.org/html/2607.01904v1)                                                                                                                                                                                                                                                                              | The one Tier A field study of a throughput-raising program found the review-side damage accrued _during_ the ramp, not after it. Ordering the review mechanism last is the sequencing the evidence argues against. Substantive verification of the cost items should be read from W5.                                          |

**Counts:** CONFIRMED 3 · STALE 0 · REFUTED 0 · UNVERIFIED 4 (one of which is partly out of scope) · SKIPPED 0. All 7 W9-assigned claims verdicted.

---

## Contradiction Findings

### X-04 — Where the bottleneck actually is

**Position A** (`solo-consultant-workflow.md`): review capacity is the binding constraint.
**Position B** (v1, v2, `workflow-plan.md`, `workflow-plan-v2.md`, `implementation-plan.md`): the
bottleneck is cost/routing; review capacity is never named.

**Verdict: the evidence supports Position A on the mechanism and is silent on Position A's number.
Position B is not wrong about cost — it is wrong about cost being _the_ constraint, and it is
unfalsifiable as written because it never defines a success metric that could reveal the review
failure it would cause.**

Four independent lines of evidence:

**1. The one longitudinal field test of exactly this program found review capacity binding.**
He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo & Vasilescu (Stanford/CMU, arXiv:2607.01904,
2026-07-03) studied a mid-sized B2B software firm that mandated doubling merged PRs per engineer.
802 developers, 196,212 PRs, Jan 2024–Apr 2026. The mandate worked: mean PRs per active developer
rose from 21.2 to 44.3 (2.09×); within-developer gain 1.46–1.72× under fixed effects. **The
throughput gain was real and the review system absorbed it by failing.** PR volume grew 3.1× while
the reviewer pool grew 1.5×; per-reviewer load roughly doubled. The share of PRs receiving at least
one human review fell 21 points (89% → 68%). Automated AI review coverage rose ~19% → ~84%.
Critically: **substantive review — reviews containing a human-written comment — fell from ~39% to
~21% of PRs, while silent approvals held roughly flat at ~50%.** At the median, a reviewer's
commented reviews stayed flat (~3/month) while their silent approvals roughly doubled.

That last sentence is the finding. Under a successful throughput program, **the reviewer's
substantive output did not increase at all.** It was constant. Everything above the constant became
rubber stamp. This is a direct empirical instantiation of the operator's stated hard constraint —
throughput outran review capacity, and the system's response was not to slow down but to
silently lower the review bar.

**2. Position B's own success metric would not have caught it.** In the same study, short-term
quality proxies stayed clean: merge rate flat, revert rate slightly _down_ (−0.067 post-mandate,
p<0.001). The authors are explicit that their throughput metric "miss[es] the downstream costs of
AI-generated code at scale — technical debt, diluted ownership and understanding." A cost-and-
velocity dashboard of the kind `workflow-plan-v2.md` specifies would have shown this program
succeeding on every axis it measured while the review function hollowed out.

**3. Independent telemetry shows the review side degrading faster than the generation side
improves.** Faros AI (22,000 developers, 4,000+ teams, two-year window through 2026) reports for
high-AI-adoption cohorts: median time in PR review **+441.5%**, median time to first review
**+156.6%**, average PR size **+51.3%**, bugs per PR **+54%**, and **PRs merged without review
+31.3%**. Faros is a vendor selling engineering-intelligence tooling and these findings support its
product thesis — Tier B, discount accordingly — but it is measured git telemetry, not self-report.

**4. Cost cannot be the binding constraint for this operator at current prices, but review can.**
This is arithmetic, not a citation, and it is where W5 owns the numbers: a fixed monthly
subscription is a _cap_, not a marginal cost, so once paid it imposes no per-unit throttle on
output volume at all. Review time is strictly per-unit. Any program that raises units/month against
a fixed cost cap moves the constraint to the per-unit resource by construction. Position B's
framing — "the bottleneck is not the $200/mo subscription, it is routing 80% of work through
Opus/Sonnet" (C-188) — is a claim about _unit cost_, and lowering unit cost is exactly the
intervention that raises volume against a fixed review budget.

**Under what conditions the answer changes.** Three:

- **Below a volume floor**, cost binds and review does not. If total monthly output is small enough
  that the operator reviews everything substantively within available hours, the constraint is
  whatever else is scarce, and that may well be spend. No evidence found establishes where that
  floor sits for one person; see Gaps.
- **If review is genuinely delegated to an automated gate that the operator has validated**, the
  ceiling moves from "what the operator reads" to "what the gate catches." The arXiv study shows
  the organization did exactly this (automated review 19% → 84%) — and the authors do _not_ claim
  it worked, only that it absorbed volume. Whether automated gates substitute for or merely
  displace human review is W3's question, not mine.
- **For output types where the operator is not the accountable reviewer** — internal scratch work,
  throwaway exploration — no review ceiling applies and cost dominates.

**What the evidence does not support.** It does not support C-084's specific number. There is no
measurement anywhere of a per-person concurrent-session ceiling (F-W9-06). The mechanism is
well-evidenced; the threshold is not.

---

## Findings

### F-W9-01 — Under a successful AI throughput mandate, review capacity became binding and the organization absorbed it by degrading review quality, not by adding review capacity

- **Claim.** In the only longitudinal field study of an enterprise AI throughput mandate, doubling
  per-developer PR output produced a 3.1× rise in PR volume against a 1.5× rise in reviewers;
  substantive human review fell from ~39% to ~21% of PRs while silent approvals roughly doubled and
  the median reviewer's commented reviews stayed flat.
- **Evidence tier.** A.
- **Support.** He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo & Vasilescu, "AI Writes Faster Than
  Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate," [arXiv:2607.01904](https://arxiv.org/html/2607.01904v1)
  (2026-07-03). Panel: 802 developers, 196,212 PRs, Jan 2024–Apr 2026; estimation sample 564
  developers with ≥3 active months; employee and calendar-month fixed effects. **Read in full.**
- **Date sensitivity.** Preprint, 2026-07-03; not yet peer-reviewed as of 2026-08-01. Figures are
  firm-specific and will not drift, but replication status will.
- **Confidence.** High on the review-degradation finding (it is a direct count, robust to the
  specification choices reported). Medium on generalization: single firm, non-randomized rollout,
  self-described "near-best-case setting — a young, AI-forward firm with uncapped tool budgets."
- **Counter-evidence.** The same paper's short-run quality proxies came out _clean_: merge rate
  flat, revert rate slightly down (−0.067, p<0.001), AI-authored PRs no less likely to get a human
  review than comparable human ones, review rounds and change-request counts flat. If one takes
  merge/revert as the quality measure, nothing broke. The authors themselves say this metric misses
  technical debt and diluted understanding. Also: it is an enterprise with a reviewer _pool_; a
  solo operator has no pool to dilute, which cuts both ways — no dilution mechanism available, but
  also no slack.

### F-W9-02 — Independent telemetry across 22,000 developers shows review-side metrics degrading several times faster than throughput improves

- **Claim.** In high-AI-adoption cohorts, median time in PR review rose 441.5%, median time to
  first review 156.6%, average PR size 51.3%, bugs per PR 54%, and PRs merged with no review at all
  31.3%.
- **Evidence tier.** B (measured telemetry, vendor-published, vendor's product thesis benefits).
- **Support.** [Faros AI, "AI Code Quality: The Hidden Cost Senior Engineers Pay"](https://www.faros.ai/blog/ai-code-quality-senior-engineer-review-burden)
  — 22,000 developers, 4,000+ teams, two-year window through 2026. **Read in full.** Corroborating
  vendor figure: CodeRabbit analysis of 470 OSS PRs finds AI-generated code produces 1.7× more
  issues, logic/correctness errors +75%.
- **Date sensitivity.** Figures are cohort comparisons published 2026; will drift as models and
  tooling change. Time-stamp any use as "Faros telemetry, 2026."
- **Confidence.** Medium. Real instrumentation and a large N, but a vendor selling the remedy, no
  published methodology for cohort assignment, and "high AI adoption" is not defined precisely.
- **Counter-evidence.** **Citation hazard:** several secondary articles attribute these figures to
  the DORA 2025 report. They are not DORA's. DORA 2025 (~5,000 respondents, survey) reports 90% AI
  use, >80% self-reported productivity gain, 59% reporting positive influence on code quality, and
  found no correlation between AI adoption and increased burnout — a materially more favourable
  picture than Faros's telemetry. Where self-report and instrumentation have been compared they
  disagree, and self-report has been the optimistic one (see F-W9-11).

### F-W9-03 — Human code review has a measured per-session throughput ceiling of roughly 200–400 LOC, under 500 LOC/hour, and about 60 minutes

- **Claim.** Defect-detection effectiveness falls off sharply above ~400 LOC per review, above
  ~500 LOC/hour inspection rate, and after ~60 minutes of continuous review; a 200–400 LOC review
  over 60–90 minutes is reported to yield 70–90% defect discovery.
- **Evidence tier.** B. This is the single most-cited number in code review and it is **not**
  Tier A: it is a vendor-run internal study (SmartBear, on a Cisco team, ~2006), never
  independently replicated at that scale, and the primary write-up is distributed as marketing
  collateral. Treat as the best available anchor, not as settled science.
- **Support.** [SmartBear, "Best Practices for Peer Code Review"](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
  — **read in full**; verbatim: "developers should review no more than 200 to 400 lines of code
  (LOC) at a time"; "a review of 200-400 LOC over 60 to 90 minutes should yield 70-90% defect
  discovery"; "a significant drop in defect density at rates faster than 500 LOC per hour";
  "performance starts dropping off after about 60 minutes." The underlying case study (2,500
  reviews, 3.2M LOC, 10 months, Cisco) is distributed as a
  [PDF](https://static1.smartbear.co/support/media/resources/cc/book/code-review-cisco-case-study.pdf)
  that could not be text-extracted — **sampled via the vendor summary page, not read in the
  original.**
- **Date sensitivity.** ~2006 study on human-written C/C++. Twenty years old. Whether the LOC
  thresholds transfer to AI-generated code is untested; F-W9-14 gives reason to think review of
  AI-written code is _harder_ per line, which would lower the ceiling, not raise it.
- **Confidence.** Medium. The direction (effectiveness declines with volume and session length) is
  corroborated by the broader modern-code-review literature; the specific numbers rest on one
  vendor study.
- **Counter-evidence.** The same vendor reports that "spot checking" only 20–33% of code achieved
  lower defect density with minimal time — which, if true, undercuts the premise that full review
  is required and would materially raise an operator's effective ceiling. No independent
  replication of that claim found.

### F-W9-04 — For non-code analytical work, the solo-reviewer penalty is directly measured: single screening misses a median 5% of relevant material vs. double screening, and 13% when the single reviewer is inexperienced

- **Claim.** In systematic-review screening — a code-free analytical review task structurally
  similar to the operator's knowledge-repo work — a single reviewer misses a median 5% of relevant
  studies (range 0–58%); median 3% for experienced reviewers (range 0–21%) and 13% for
  less-experienced reviewers (range 0–58%). A separate randomized crowd trial puts single-reviewer
  abstract screening at 86.6% sensitivity (95% CI 80.6–91.2) vs 97.5% (95% CI 95.1–98.8) for dual.
- **Evidence tier.** A.
- **Support.** Waffenschmidt, Knelangen, Sieben, Bühn & Pieper, "Single screening versus
  conventional double screening for study selection in systematic reviews: a methodological
  systematic review," _BMC Med Res Methodol_ 19:132 (2019),
  [PMC6599339](https://pmc.ncbi.nlm.nih.gov/articles/PMC6599339/) — **read in full**; 23 screenings
  across 9 reviewers. Crowd RCT: [Gartlehner et al., _J Clin Epidemiol_ (2020)](https://www.sciencedirect.com/science/article/pii/S0895435619309825)
  — sampled. Impact figure: across 7 single screenings covering 18,148 references, 3 (all by the
  same less-experienced reviewer) would have **substantially changed** the meta-analysis
  conclusions; the 4 by experienced reviewers had negligible impact.
- **Date sensitivity.** None material. Human review reliability is not a fast-moving figure.
- **Confidence.** High for the domain studied. Medium for transfer to consulting knowledge repos —
  the task shape (binary relevance judgment over many items by one person) is close, but the
  materials and stakes differ.
- **Counter-evidence.** The authors' own conclusion is deliberately permissive: single screening
  "could still represent an appropriate methodological shortcut in rapid reviews, **as long as it
  is conducted by an experienced reviewer**." The experienced/inexperienced gap (3% vs 13%) is
  larger than the single/dual gap for experienced reviewers — reviewer expertise dominates reviewer
  count. Limitations: reviewer-experience classification was rough and inconsistently reported.

### F-W9-05 — Exhaustive human review of documents achieves far lower recall and precision than practitioners assume

- **Claim.** In the TREC 2009 Legal Track, exhaustive manual review by official assessors achieved
  59.3% recall and 31.7% precision (F1 36.0), versus 76.7% recall / 84.7% precision (F1 80.0) for
  technology-assisted review that touched only ~1.9% of documents.
- **Evidence tier.** A.
- **Support.** Maura R. Grossman & Gordon V. Cormack, "Technology-Assisted Review in E-Discovery
  Can Be More Effective and More Efficient Than Exhaustive Manual Review," 17 _Richmond J.L. &
  Tech._ 11 (2011), [landing page + abstract read in full](https://scholarship.richmond.edu/jolt/vol17/iss3/5/).
  The recall/precision figures are **sampled from secondary summaries** — both the Richmond and
  IADC full-text PDFs returned 403 / unextractable. Flagged accordingly.
- **Date sensitivity.** 2009 data, 2011 publication. The _human_ baseline is the durable part; the
  TAR comparison figure is obsolete relative to 2026 tooling.
- **Confidence.** Medium-high on the human baseline (it is a competition with ground truth, which
  is rare), low-medium on my transcription of the exact digits given I could not open the primary
  PDF.
- **Counter-evidence.** The manual reviewers were TREC assessors working at volume under time
  pressure — arguably a worse case than a motivated principal reviewing their own deliverable. The
  study is also frequently criticized in the e-discovery literature for treating the assessors'
  own later adjudications as ground truth. Do not read this as "humans catch 59% of everything";
  read it as "exhaustive human review of a large corpus by one pass is much leakier than it feels."

### F-W9-06 — There is no measured evidence for any concurrent-agent-session ceiling; the widely-repeated 3–5 figure is vendor-origin folk consensus

- **Claim.** No study, telemetry report, or structured survey with a stated N establishes how many
  concurrent AI coding sessions one person can supervise. Every published number is a vendor tip or
  a single practitioner's introspection, and several of the "independent" sources trace to the same
  Anthropic guidance.
- **Evidence tier.** C for every number located. There is no Tier A or B source on this question.
- **Support.** Vendor origin: [Anthropic, "Claude Code power user tips" (2026-06-25)](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
  — "The biggest productivity unlock is running 3–5 Claude sessions in parallel, each in its own
  git worktree," self-described as "patterns collected from individual engineers on the Claude Code
  team." Anthropic's own product docs ([worktrees](https://code.claude.com/docs/en/worktrees),
  [best practices](https://code.claude.com/docs/en/best-practices.md)) state **no** human
  supervision limit. Practitioner blogs: [engineered.at](https://engineered.at/articles/your-parallel-agent-limit)
  "three to four threads"; [codewithseb](https://www.codewithseb.com/blog/parallel-claude-code-sessions-git-worktrees-guide)
  "2–4"; [dev.to/jcamarate](https://dev.to/jcamarate/why-20-claude-code-instances-break-down-and-what-to-do-2i5j)
  "3–5"; [codefather.dev](https://codefather.dev/blog/post/vibecoding-parallelizes-features-but-doesnt-parallelize-me)
  "N ≤ 2"; [MindStudio](https://www.mindstudio.ai/blog/claude-code-git-worktree-parallel-branches)
  (vendor) "two to three"; [Backgrind](https://backgrind.com/blog/git-worktrees-parallel-agents/)
  (vendor, sells the fix) "three to five." Some cited ceilings are RAM/CPU limits, not attention
  limits, and are conflated with the human question.
- **Date sensitivity.** High. Anthropic's guidance is dated 2026-06-25 and is a moving target;
  re-check any number quoted here against current vendor docs.
- **Confidence.** High that no measurement exists (searched vendor docs, the major developer
  surveys, and the practitioner corpus). Low on any specific number.
- **Counter-evidence.** The convergence itself is mildly informative — a dozen independent-seeming
  writers landing in 2–5 is weak evidence of a real working-memory-shaped constraint. But
  convergence of anecdote is not measurement, and Anthropic frames 3–5 as a floor to aim for, not a
  ceiling to respect, so the corpus's use of it as a _ceiling_ inverts the source's meaning. The
  one falsifiable proxy anyone proposed is queue-based, not count-based: track how long each diff
  waits before a human first opens it; if that wait grows week over week, added agents are adding
  queue, not capacity ([Context Studios, 2026-07](https://www.contextstudios.ai/blog/run-10-claude-code-agents-review-is-your-real-bottleneck), Tier C).

### F-W9-07 — The relationship between concurrent projects and individual performance is an inverted U, not monotonic decline; the empirical mean in the only large panel study is 2.71 projects

- **Claim.** Multi-project work has an inverted-U relationship with project performance — some
  concurrency beats one project, too much is worse than one — and the effect is moderated by
  specialized experience, project similarity, and familiarity with counterparts.
- **Evidence tier.** A.
- **Support.** Colicev, Hakkarainen & Pedersen, "Multi-project work and project performance:
  Friends or foes?", _Strategic Management Journal_ 43(11), 2022,
  [doi:10.1002/smj.3443](https://doi.org/10.1002/smj.3443)
  ([accepted manuscript](https://livrepository.liverpool.ac.uk/3159074/1/Accepted%20article.pdf)).
  9,649 project-month-employee observations; 42 NPD projects, 580 employees, 20 months. 58% of
  employees engaged in multi-project work, averaging **2.71 projects** (max 12). Specialized
  experience interaction .14, p=.026. Sampled via subagent extraction, not read personally.
- **Date sensitivity.** None material.
- **Confidence.** Medium-high on the shape of the relationship. **Low on any "optimal N"** — the
  turning point of the inverted U is not stated in the accessible manuscript text, and 2.71 is the
  sample mean, not the vertex. Do not quote a peak.
- **Counter-evidence.** Manufacturing NPD context, not knowledge-service delivery. Patanakul (_IEEE
  TEM_ 2012, N=169 multi-project managers averaging 5–6 simultaneous projects) found project _count_
  was **not** the significant predictor of effectiveness — teamwork culture and PM competency were
  (Adj. R²=0.577). That is a direct counterweight to count-based throttling.

### F-W9-08 — The older project-management literature converges on 2–3 concurrent major projects per individual, but explicitly describes itself as sparse

- **Claim.** Reviews of the multi-project literature conclude that in high-technology environments
  an individual should not work on more than two to three relatively large projects, while noting
  the literature on the question is thin.
- **Evidence tier.** B.
- **Support.** Steyn & Schnetler, "Concurrent Projects: How Many Can You Handle?", _South African
  Journal of Industrial Engineering_ 26(3), 2015
  ([full text](https://www.scielo.org.za/scielo.php?pid=S2224-78902015000300009&script=sci_arttext)).
  Synthesizes McCollum & Sherman (64 high-tech firms; "two projects seemed to be optimal," "one to
  three assignments may not be problematic") and Fricke & Shenhar ("two to three 'major' projects…
  an effective maximization of an engineer's productivity"; "apparent de facto standard of two to
  three projects per person"). Verbatim caveat from the authors: "The literature on the topic of
  the number of projects that a person can handle is sparse." Sampled via subagent extraction.
- **Date sensitivity.** Low; the primary sources predate 2015.
- **Confidence.** Medium on the claim as stated; low on transfer to solo consulting. The "2–3"
  traces back to Wheelwright & Clark's R&D-engineer productivity curve — a manufacturing NPD
  context.
- **Counter-evidence.** Steyn & Schnetler's own survey found actual practice wildly exceeds the
  prescription: responses ranged 0 to 200 concurrent projects, 77% cumulative in the 0–6 band, and
  services-industry respondents ran 3–8× more concurrent projects than other industries. Either the
  prescription is wrong or the services industry is chronically over-committed; the study does not
  resolve which.

### F-W9-09 — The three most-quoted context-switching statistics are not published findings

- **Claim.** Weinberg's "20% loss per additional project," the "23 minutes 15 seconds to refocus,"
  and "task switching costs 40% of productive time" are, respectively, a self-declared heuristic, an
  interview remark never printed in a paper, and a press-page quote — none is a measured result.
- **Evidence tier.** A for the debunking (the primary papers are checkable); the claims themselves
  are Tier C.
- **Support.**
  - **Weinberg 20%:** _Quality Software Management Vol. 1: Systems Thinking_ (Dorset House, 1991),
    pp. 284–285. Per [contextcost.com](https://contextcost.com/) (**read in full**): "These
    estimates were heuristic, not laboratory measurements, and Weinberg said so."
  - **23m15s:** not in Mark, González & Harris (CHI 2005) or Mark, Gudith & Klocke (CHI 2008).
    Traced to a June 2006 _Gallup Management Journal_ interview describing a different (n=36)
    sample. Two independent tracebacks:
    [oberien](https://blog.oberien.de/2023/11/05/23-minutes-15-seconds.html),
    [Mazeroff](https://geoffmazeroff.com/2026/03/23/the-context-switching-statistic-that-got-lost-in-translation/).
  - **40% of productive time:** [APA, "Multitasking: Switching costs"](https://www.apa.org/topics/research/multitasking)
    — "Meyer **has said** that even brief mental blocks… can cost as much as 40 percent of someone's
    productive time." An attributed remark on a topic page, not a result in Rubinstein, Meyer &
    Evans (_JEP:HPP_ 27(4), 2001), whose own switching costs are reported in **milliseconds per
    switch** (comparable Allport et al. costs discussed in-paper: ~135–180 ms, one paradigm
    ~1,100 ms).
- **What the published record actually says.** Mark, González & Harris, "No Task Left Behind?"
  (CHI 2005; 24 informants, >700 hours of stopwatch-timed shadowing): informants worked in an
  average of **11.7 working spheres**; average **11 min 4 s** in a working sphere before switching
  or being interrupted; **57.1%** of segments interrupted; **77.2%** of interrupted work resumed
  same-day, taking an average **25 min 26 s** to resume, with **2.26 intervening working spheres**
  first. Leroy (_OBHDP_ 109(2), 2009; N=84 and N=78) demonstrates attention residue with η² ≈ 0.09
  and one clean contrast at d = 0.86 — millisecond-scale priming and ~10-point rating differences,
  not workday percentages.
- **Date sensitivity.** None; these are historical-record questions.
- **Confidence.** High.
- **Counter-evidence.** The direction of the folklore is not wrong — residue and resumption cost
  are real and replicated. What is wrong is the magnitude and the provenance. Anyone building a
  capacity model on "20% per project" is building on an acknowledged guess.

### F-W9-10 — In the one controlled experiment on interruption cost, interrupted work was completed _faster_ with no quality difference; the cost was stress, not time

- **Claim.** Mark, Gudith & Klocke (CHI 2008, N=48) found interrupted participants finished the
  task in **less** time (20.31 and 20.60 min for same- and different-context interruption vs 22.77
  min baseline, F(2,77.98)=3.36, p<.05) with no difference in errors (F(2,92)=1.70, p<.19), while
  reporting significantly higher stress (F(2,92)=12.15, p<.001), frustration, time pressure and
  effort. The mechanism the authors propose: people compensate by working faster and writing less.
- **Evidence tier.** A.
- **Support.** [Mark, Gudith & Klocke, "The Cost of Interrupted Work: More Speed and Stress," CHI
  2008](https://www.ics.uci.edu/~gmark/chi08-mark.pdf). Sampled via subagent extraction with
  verbatim statistics.
- **Date sensitivity.** None.
- **Confidence.** High for the experiment as run; low for transfer — a 20-minute email task is not
  a multi-hour agentic session, and "wrote less" is precisely the failure mode that matters when
  the output is a client deliverable.
- **Counter-evidence.** This is itself the counter-evidence to the switching-cost narrative. It
  should not be read as "interruption is free": the compensation mechanism (faster, shorter output)
  is a quality reduction that the experiment's error metric was too coarse to detect. It does mean
  that **time-based** models of context-switching cost are poorly supported, and that the real cost
  is more plausibly quality and depletion.

### F-W9-11 — Self-assessment of AI-assisted productivity is systematically biased optimistic, which makes felt capacity an unreliable throttle

- **Claim.** In a randomized controlled trial, experienced developers took **19% longer** on real
  tasks when allowed AI tools, having forecast 24% faster beforehand and estimated 20% faster
  afterwards. The direction of error was optimistic in every comparison.
- **Evidence tier.** A.
- **Support.** METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer
  Productivity," [blog](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
  and [arXiv:2507.09089](https://arxiv.org/abs/2507.09089) (2025-07-10) — **read in full** (blog +
  abstract). 16 developers, 246 tasks, repos averaging 22k+ stars and 1M+ LOC where developers had
  ~5 years' prior experience; each task randomly assigned AI-allowed or not. Screen-recording
  analysis of 143 labeled hours attributes the slowdown to time reviewing AI outputs, prompting,
  and waiting for generations. Economics experts predicted 39% faster; ML experts 38% faster.
- **Date sensitivity.** **High and explicitly acknowledged by METR** — the tooling studied was
  Cursor Pro with Claude 3.5/3.7 Sonnet, Feb–Jun 2025. METR itself now labels the result historical.
  Do **not** cite the 19% as a current fact about 2026 tooling; cite it as evidence about the
  perception gap.
- **Confidence.** High on the perception gap (three independent estimate sources all wrong in the
  same direction). Low on the 19% as a current effect size — N=16, 56% had never used Cursor, and
  the setting (mature repos the developers knew intimately) is close to a worst case for AI.
- **Counter-evidence.** Directly contradicted on effect direction by every large self-report survey
  (DORA 2025: >80% report productivity gains) and by the arXiv:2607.01904 field study, which
  measured a genuine 1.46–2.09× throughput increase. The reconciliation is that these measure
  different things — METR measured time-to-complete-a-task for an expert on familiar code; the
  field study measured PRs merged per developer. Both can be true. What survives across all of them
  is that **self-report and instrumentation disagree, and self-report is the optimistic one.**

### F-W9-12 — Documented personal operating systems put the throttle in different places, and only one gives a number; none has empirical validation

- **Claim.** GTD's throttle is the weekly review with no WIP cap; Personal Kanban's is an explicit
  but self-declaredly arbitrary WIP cap of ~2–3 on today's tasks; Building a Second Brain has no
  project cap and a daily task cap of ~10; Cal Newport's Slow Productivity is the only one with a
  hard concurrency number — **3 active projects** with a visible queue behind them. None has been
  empirically validated.
- **Evidence tier.** C for every system's efficacy claim; A for the statement that GTD is
  unvalidated.
- **Support.**
  - GTD: Heylighen & Vidal, "Getting Things Done: The Science behind Stress-Free Productivity,"
    _Long Range Planning_ 41(6), 2008 ([PDF](http://pespmc1.vub.ac.be/Papers/GTD-cognition.pdf)) —
    verbatim: "as yet no academic papers have investigated this method," and testing it is
    "intrinsically difficult… because GTD does not embrace explicit priorities or optimization
    criteria, there is no obvious standard by which to measure expected productivity enhancements."
  - Personal Kanban: [Benson, "How To: Setting Your Personal WIP Limit"](https://personalkanban.com/pk/uncategorized-how-to-setting-your-personal-wip-limit/)
    — "Start With 3… Three stickies are easy to see, easy to grasp… **But three is not the only
    number. It's just a handy, arbitrary one.**"
  - Newport: [GQ interview](https://www.gq.com/story/cal-newport-slow-productivity-interview) —
    "At the top of the list are the three things I'm actively working on right now… Below that is
    an ordered list of the queue… **This scheme is not about directly saying yes or no to things.
    It's about having two statuses: Actively working on, and waiting to work on.**"
  - Forte: [weekly review as OS](https://fortelabs.com/blog/the-weekly-review-is-an-operating-system/) —
    caps the daily list at 10 tasks, focuses on "2 or 3 projects" per week, but explicitly argues
    _against_ WIP limiting at the portfolio level ("keep multiple balls in the air").
  - All sampled via subagent extraction with verbatim quotes.
- **Date sensitivity.** None.
- **Confidence.** High that none is validated. High on the quoted throttle mechanisms.
- **Counter-evidence.** The apparent agreement on 2–3 across four systems is not four
  corroborating data points — they are four independent prescriptions that happen to coincide, and
  at least one author (Benson) openly runs a dozen-plus concurrent engagements behind a two-item
  daily WIP via a two-tier board. **The distinction that resolves the apparent agreement: every
  system that caps at 2–3 is capping today's execution WIP, not the engagement portfolio.** They
  are silent on how many clients you may sign.

### F-W9-13 — Solo-consultant concurrent-client capacity has only Tier B survey data, and the field is contaminated by fabricated benchmark citations

- **Claim.** The best available figures: MBO Partners (2020, N=503 independent professionals, MoE
  ±4.1%) reports the average independent professional "works with 4 to 6 clients at a time";
  Antenna's 2019 survey of 80 $100K+ independent consultants found 41% serving only one client at a
  time, 30% serving 2–3, 21% serving 3–5, 8% more than six; Antenna's 2020 edition (N>150) reports
  "91% of respondents are usually working with more than one client at a time; 22% often work with
  more than six." SPI Research's 2025 benchmark (403 firms) puts billable utilization at 68.9% for
  2024, down from ~73.2% in 2021.
- **Evidence tier.** B for all of the above. No Tier A study of solo-consultant concurrent-client
  capacity exists.
- **Support.** [MBO Partners Client of Choice 2020](https://event.hbrturkiye.com/storage/uploads/client-of-choice-2020-6152c243355d2.pdf);
  [Antenna 2019](https://www.lemonly.com/general-uploads/Work/191010_Antenna_ConsultantSurvey_eBook_Final.pdf);
  [Antenna 2020](https://www.lemonly.com/general-uploads/Work/201125_Antenna_ConsultantSurvey_eBook_WF.pdf);
  [SPI Research 2025 summary](https://www.saibongroup.com/blogs/consultant-utilization-rate-benchmark).
  All sampled via subagent extraction.
- **Date sensitivity.** Utilization figures are annual and drift; time-stamp as 2024/2025 data.
  Client-count figures are 2019/2020 and predate agentic tooling entirely.
- **Confidence.** Low-medium. Every source is run by a firm selling to the population it surveys
  (staffing marketplaces, compliance vendors, coaching programs). The Antenna 2019→2020 shift
  (41% → 9% single-client) is too large to be a real one-year change and most likely reflects a
  sample or question change the reports do not explain.
- **Counter-evidence / contamination warning.** Two sources that surface prominently for this query
  — [firmem.com/Practiq](https://firmem.com/benchmarks/how-many-engagements-can-a-boutique-consulting-firm-handle)
  ("solo consultants past 5 concurrent engagements miss deliverable dates on at least one
  engagement per month") and [pharallax.ai](https://pharallax.ai/insights/consulting-benchmarks/)
  ("Active Clients 3–5 for solo consultants") — present precise-looking benchmarks attributed to a
  "Kennedy Research 2024 Independent Consultant Survey" and an "SCIP 2024 Solo Consultant Study."
  **Neither study is traceable anywhere outside those pages.** Treat as AI-generated SEO content
  with invented citations; do not cite.

### F-W9-14 — Developers report that reviewing AI-generated code takes more effort than reviewing human code, while trust in AI output is falling as adoption rises

- **Claim.** 38% of developers say reviewing AI-generated code requires **more** effort than
  reviewing a human colleague's, vs 27% who say less; 95% spend at least some effort reviewing,
  testing and correcting AI output and 59% rate that effort "moderate" or "substantial." In the
  largest developer survey, active distrust of AI accuracy (46%) now exceeds trust (33%), up from
  31% distrust the prior year, while adoption rose 76% → 84%.
- **Evidence tier.** A for the Stack Overflow survey (N=49,000+, 177 countries, public microdata);
  B for Sonar (vendor sells code-quality tooling and benefits directly from this finding; full N
  not clearly stated, one sub-table n=1,149).
- **Support.** [Stack Overflow Developer Survey 2025 — AI section](https://survey.stackoverflow.co/2025/ai)
  (trust breakdown: highly trust 3.1% / somewhat trust 29.6% / somewhat distrust 26.1% / highly
  distrust 19.6%; top frustration cited by 66% is "AI solutions that are almost right, but not
  quite"; 45% cite debugging AI code as more time-consuming; experienced developers are the most
  cautious). [Sonar, State of Code Developer Survey (Jan 2026)](https://www.sonarsource.com/state-of-code-developer-survey-report.pdf).
  [JetBrains State of Developer Ecosystem 2025](https://devecosystem-2025.jetbrains.com/) (N=24,534;
  top AI concern is quality of AI-generated code, 23%). All sampled via subagent extraction.
- **Date sensitivity.** High — annual surveys; re-check against the 2026 editions. Stamp all
  figures as 2025 fieldwork.
- **Confidence.** Medium-high. Large N and transparent methodology, but all self-report.
- **Counter-evidence.** Stack Overflow publishes **two inconsistent trust numbers for its own 2025
  survey** — the AI results page says 33% trust / 46% distrust, while its December 2025 blog post
  and leaders' summary say trust "fell from 40% in previous years to just 29% this year," and the
  same two materials reverse the 66%/45% frustration figures. SO never reconciles them. Cite the
  primary results page and footnote the discrepancy. Also: DORA 2025 (~5,000 respondents) found
  > 80% reporting productivity gains and 59% reporting positive influence on code quality — the
  > same population is simultaneously less trusting and more positive, which should temper any strong
  > reading of either.

### F-W9-15 — "Comprehension debt" is a named but barely-measured phenomenon; no study quantifies the cost of maintaining code no human authored

- **Claim.** The term traces to Jason Gorman (2025-08-16), popularized by Addy Osmani (2026). One
  academic study exists — qualitative, undergraduate population, no cost quantification. The nearest
  hard baseline is that professional developers spend ~58% of their time on program comprehension.
- **Evidence tier.** A for the comprehension-time baseline and for the EASE 2026 study's method;
  the phenomenon's cost is unquantified.
- **Support.**
  - Origin: [Gorman, LinkedIn (2025-08-16)](https://www.linkedin.com/posts/jasongorman_comprehension-debt-the-time-it-will-take-activity-7362368955966996480-onU6)
    — "Comprehension Debt: the time it will take developers to understand code they didn't write
    when they have to change it or fix it"; [Codemanship blog (2025-09-30)](https://codemanship.wordpress.com/2025/09/30/comprehension-debt-the-ticking-time-bomb-of-llm-generated-code/).
    Multiple secondary sources misattribute the coinage to Osmani or Arvid Kahl; the academic
    literature credits Gorman.
  - Only study: Ahmad, "Comprehension Debt in GenAI-Assisted Software Engineering Projects,"
    EASE 2026 ([arXiv:2604.13277](https://arxiv.org/html/2604.13277v1)) — 621 reflective diary
    entries, 207 undergraduates, 8 weeks, thematic analysis. Four accumulation patterns; one
    mitigating pattern ("rewrite before commit"). No cost quantification.
  - Baseline: Xia, Bao, Lo, Xing, Hassan & Li, "Measuring Program Comprehension: A Large-Scale
    Field Study with Professionals," _IEEE TSE_ — 78 professionals, 7 projects, 3,148 instrumented
    working hours: "on average developers spend ~58% of their time on program comprehension
    activities," and developers on projects in the **maintenance** phase spend significantly more
    of their time on comprehension than those in the development phase.
  - Intellectual ancestor: Peter Naur, "Programming as Theory Building" (1985). All sampled via
    subagent extraction.
- **Date sensitivity.** The origin/attribution question is settled. The measurement gap is live and
  could close within a year.
- **Confidence.** High on the attribution and on the absence of cost measurement. Medium on the
  58% figure's transfer (pre-LLM, two Chinese IT firms, does not isolate authorship).
- **Counter-evidence.** The EASE 2026 study's population is undergraduates on a course project —
  the weakest possible proxy for a professional maintaining client code. Its most useful output is
  not a measurement but a mitigating practice with a mechanism: students who rewrote AI code before
  committing "never incurred" comprehension debt because they "retained authorial and cognitive
  ownership." That is a hypothesis, not a finding.

### F-W9-16 — Review capacity has usable leading indicators, and none of them appear in the corpus's proposed weekly cadence

- **Claim.** Two review-capacity indicators with empirical grounding exist: (a) the **share of
  merged units receiving substantive review** — i.e. review containing a written comment, as
  opposed to silent approval — which is the metric that revealed the failure in arXiv:2607.01904;
  and (b) **queue latency before first human open**, which detects added parallelism turning into
  queue rather than capacity. Neither appears in C-154's or C-186's weekly checklists, which are
  composed entirely of cost, output-quality and routing checks.
- **Evidence tier.** A for indicator (a) — it is the metric that carried the finding in the field
  study. C for indicator (b) — proposed in a vendor blog, never validated.
- **Support.** [arXiv:2607.01904](https://arxiv.org/html/2607.01904v1) (**read in full**):
  substantive review fell ~39% → ~21% of PRs while merge rate and revert rate stayed flat — i.e.
  the outcome metrics stayed clean while the process metric collapsed.
  [Context Studios (2026-07)](https://www.contextstudios.ai/blog/run-10-claude-code-agents-review-is-your-real-bottleneck)
  for the queue-latency proxy. Ledger claims C-154/C-186 for the checklist contents.
- **Date sensitivity.** None material.
- **Confidence.** High that the substantive-review-share metric detected the failure in the one
  study where both were observed. Medium that it transfers to a single-operator setting, where
  "silent approval" has no social meaning and must be operationalized differently (e.g. diffs
  merged without the operator having opened them, or without a written note).
- **Counter-evidence.** In a solo setting there is no second party to whom a review is visible, so
  the metric must be self-reported — and F-W9-11 establishes that self-report about AI-assisted
  work is unreliable in the optimistic direction. An instrumented proxy (did the diff get opened?
  for how long? was a comment written?) is more defensible than a self-rating, but no published
  work validates such a proxy for solo operators.

---

## Gaps

1. **No measurement of a solo operator's concurrent-session ceiling exists — at all.** Not from
   Anthropic, not from Cursor or Cognition, not from Stack Overflow / JetBrains / DORA / Octoverse
   (none of the four major developer surveys asks how many agents a developer runs at once), and
   not from any academic group. What would settle it: an instrumented within-subject study varying
   concurrent session count for a fixed operator and measuring escaped-defect rate or
   substantive-review share per unit merged. Nothing of the kind was found.
2. **No quantitative anchor for a solo reviewer's daily ceiling in units the operator works in.**
   The SmartBear 200–400 LOC / 60-minute figure is per-_session_, from ~2006, vendor-run, on
   human-written code. Nothing establishes a per-_day_ sustainable figure, and nothing tests whether
   the LOC threshold changes for AI-generated code. Given F-W9-14 (38% say AI code is harder to
   review), the honest position is that the 200–400 LOC figure is an **upper** bound for AI output,
   not a transferable one.
3. **The review ceiling for code-free knowledge/documentation output is inferred, not measured.**
   The best analogues — systematic-review screening (F-W9-04) and e-discovery (F-W9-05) — are
   relevance-classification tasks, not "is this analysis correct and internally consistent" tasks.
   No study measures how much analytical prose one person can verify per day before accuracy
   degrades. This is a real gap and it matters because a substantial share of the operator's work
   mix is exactly this.
4. **No study quantifies the maintenance cost of code no human authored.** Comprehension debt has a
   name, an origin, one qualitative student study, and no price tag (F-W9-15).
5. **The turning point of the multi-project inverted U is not established.** Colicev et al. give
   the shape and a sample mean (2.71), not a vertex. Anyone quoting an "optimal N" from that paper
   is over-reading it.
6. **Where the cost-vs-review crossover sits for one person is not established** and probably
   cannot be established externally — it depends on the operator's own hourly review throughput,
   which has never been measured for them. This is the one gap that self-instrumentation could close
   in weeks: log units merged, units substantively reviewed, and review minutes, for four weeks.
7. **Solo-consultant capacity data is vendor-survey-only and pre-agentic** (2019–2020 fieldwork),
   and the search space is actively contaminated by fabricated benchmark citations (F-W9-13).

---

## Implications for the Operator

_My inferences. Not findings. Phase C owns the synthesis._

1. **X-04 resolves in favour of review capacity as the binding constraint, but the corpus's
   evidence for it was weak and its number was wrong.** Position A was right for reasons the corpus
   did not have. C-084's "3+ concurrent sessions" should be dropped as a threshold — it is a vendor
   productivity tip inverted into a limit — and replaced with a measured indicator.
2. **The cost program in `workflow-plan-v2.md` is not wrong; it is incomplete in a specific,
   nameable way.** It optimizes unit cost against a fixed subscription cap, which mechanically
   raises volume against a fixed review budget. The Tier A field study shows precisely this
   configuration degrading review while every outcome metric stayed green. If the cost program ships
   without a review-load indicator, it will look like a success on its own dashboard whether or not
   it is one.
3. **The single highest-value missing instrument is substantive-review share** — the fraction of
   merged work the operator actually opened and commented on. It is the metric that carried the
   finding in the only study that observed both, and it is absent from both proposed weekly
   cadences.
4. **Throttle placement, not throttle count, is the real design question.** Every documented
   personal operating system that appears to cap at 2–3 is capping _today's execution WIP_, not the
   _engagement portfolio_ — Benson runs a dozen engagements behind a two-item daily board. Phase C
   should treat intake gating and execution WIP as two separate controls; the evidence only speaks
   to the second.
5. **Discount your own sense of capacity.** Every time self-report and instrumentation have been
   compared in this literature, self-report was optimistic — METR's developers believed +20% while
   measuring −19%; DORA's respondents reported no added friction while telemetry showed stalled work
   up 26%. "I can handle four sessions" is exactly the kind of judgment that record says to
   distrust.
6. **The solo-reviewer penalty is real and quantified in the knowledge-work analogue, not the code
   one.** Single vs dual screening: 5% median miss rate, 13% for a less-experienced reviewer,
   enough to change conclusions in 3 of 7 cases. The operator has no second reviewer by definition,
   so the relevant lever is not adding a reviewer but raising reviewer expertise in-domain and
   narrowing what must be reviewed — which is where W6's domain-ramp work and W3's automated gates
   land.
7. **Client-safety flag.** Nothing in W9's evidence base is confidentiality-sensitive on its own,
   but one composition consequence is: automated review gates (the mechanism the enterprise study's
   firm used to absorb review load, 19% → 84% coverage) mean client code and client documents pass
   through third-party review tooling. That is a data-residency and third-party-access decision, not
   just a quality one, and it should be made per engagement rather than once globally.

---

## Sources

**Read in full (7):**

1. He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo & Vasilescu, "AI Writes Faster Than Humans Can
   Review: A Longitudinal Study of an Enterprise 2x Mandate," [arXiv:2607.01904](https://arxiv.org/html/2607.01904v1),
   2026-07-03. **Tier A.** Trusted: 802 devs / 196,212 PRs, fixed-effects panel, authors state
   limitations candidly and report results that cut against their own framing (quality proxies
   clean). Distrust factor: preprint, single firm, non-randomized rollout.
2. Waffenschmidt, Knelangen, Sieben, Bühn & Pieper, _BMC Med Res Methodol_ 19:132 (2019),
   [PMC6599339](https://pmc.ncbi.nlm.nih.gov/articles/PMC6599339/). **Tier A.** Trusted:
   peer-reviewed methodological review, explicit limitations, conclusion permissive rather than
   alarmist.
3. METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity,"
   [blog](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) +
   [arXiv:2507.09089](https://arxiv.org/abs/2507.09089), 2025-07-10. **Tier A.** Trusted:
   pre-registered RCT design, reports a result contrary to its own field's expectations, METR
   itself flags the result as historical. Distrust factor: N=16.
4. [Faros AI, "AI Code Quality: The Hidden Cost Senior Engineers Pay"](https://www.faros.ai/blog/ai-code-quality-senior-engineer-review-burden).
   **Tier B.** Trusted: measured telemetry, 22,000 devs. Distrusted: vendor selling the remedy, no
   published methodology, cohort definitions vague.
5. [contextcost.com](https://contextcost.com/). **Tier B** (secondary but source-critical).
   Trusted specifically because it debunks the numbers it presents — states Weinberg's estimates
   were "heuristic, not laboratory measurements," and that the 23-minute figure is not in the
   papers. Used only for provenance, never as a source of effect sizes.
6. [SmartBear, "Best Practices for Peer Code Review"](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/).
   **Tier B/C.** Distrusted as a vendor summarizing its own unreplicated study; used because it is
   the primary distribution point for the only widely-cited review-throughput numbers that exist.
7. [Addy Osmani, "The 80% Problem in Agentic Coding" (2026-01-28)](https://addyo.substack.com/p/the-80-problem-in-agentic-coding)
   and [ "Code Review in the Age of AI" (2026-01-05)](https://addyo.substack.com/p/code-review-in-the-age-of-ai).
   **Tier C.** Read for verbatim quote verification (C-029) only; his underlying figures are
   second-hand from Faros/Cortex.

**Sampled (not read in full):**

8. Grossman & Cormack, 17 _Richmond J.L. & Tech._ 11 (2011),
   [landing page](https://scholarship.richmond.edu/jolt/vol17/iss3/5/). **Tier A.** Abstract read;
   full-text PDFs returned 403 / unextractable, so the recall/precision digits are second-hand.
9. Colicev, Hakkarainen & Pedersen, _Strategic Management Journal_ 43(11), 2022,
   [doi:10.1002/smj.3443](https://doi.org/10.1002/smj.3443). **Tier A.** The only large-panel study
   on individual multi-project performance.
10. Steyn & Schnetler, _SAJIE_ 26(3), 2015,
    [full text](https://www.scielo.org.za/scielo.php?pid=S2224-78902015000300009&script=sci_arttext).
    **Tier B.** Trusted for its candour that the literature is sparse.
11. Patanakul, _IEEE TEM_ 2012, [doi:10.1109/tem.2012.2199993](https://doi.org/10.1109/tem.2012.2199993).
    **Tier A/B.** Counterweight: project count was not the significant predictor.
12. Mark, González & Harris, "No Task Left Behind?", CHI 2005,
    [PDF](https://www.ics.uci.edu/~gmark/CHI2005.pdf). **Tier A.** Source of the real numbers
    (11m04s per working sphere, 57.1% interrupted, 25m26s to resume).
13. Mark, Gudith & Klocke, "The Cost of Interrupted Work," CHI 2008,
    [PDF](https://www.ics.uci.edu/~gmark/chi08-mark.pdf). **Tier A.** Trusted because it reports a
    counterintuitive null on time.
14. Leroy, _OBHDP_ 109(2), 2009, [doi:10.1016/j.obhdp.2009.04.002](https://doi.org/10.1016/j.obhdp.2009.04.002).
    **Tier A.** Attention residue; effect sizes are small and lab-scale.
15. Rubinstein, Meyer & Evans, _JEP:HPP_ 27(4), 2001,
    [PDF](https://www.apa.org/pubs/journals/releases/xhp274763.pdf). **Tier A** for the paper;
    the widely-quoted "40%" comes from [APA's topic page](https://www.apa.org/topics/research/multitasking),
    **Tier C**.
16. Heylighen & Vidal, _Long Range Planning_ 41(6), 2008,
    [PDF](http://pespmc1.vub.ac.be/Papers/GTD-cognition.pdf). **Tier B.** Trusted for its explicit
    statement that GTD is empirically uninvestigated.
17. Xia, Bao, Lo, Xing, Hassan & Li, "Measuring Program Comprehension," _IEEE TSE_,
    [PDF](https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=4781&context=sis_research).
    **Tier A.** 78 professionals, 3,148 instrumented hours; ~58% of time on comprehension.
18. Ahmad, "Comprehension Debt in GenAI-Assisted Software Engineering Projects," EASE 2026,
    [arXiv:2604.13277](https://arxiv.org/html/2604.13277v1). **Tier A** method, weak population
    (207 undergraduates).
19. [Gorman, Codemanship (2025-09-30)](https://codemanship.wordpress.com/2025/09/30/comprehension-debt-the-ticking-time-bomb-of-llm-generated-code/)
    and [LinkedIn (2025-08-16)](https://www.linkedin.com/posts/jasongorman_comprehension-debt-the-time-it-will-take-activity-7362368955966996480-onU6).
    **Tier C.** Origin of "comprehension debt."
20. [Stack Overflow Developer Survey 2025 — AI](https://survey.stackoverflow.co/2025/ai).
    **Tier A** (N=49,000+, public microdata). Caveat: SO publishes inconsistent trust figures
    across its own 2025 materials (see F-W9-14).
21. [JetBrains State of Developer Ecosystem 2025](https://devecosystem-2025.jetbrains.com/).
    **Tier A.** N=24,534; raw dataset published.
22. [DORA / Google Cloud, State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/).
    **Tier A/B.** ~5,000 respondents; vendor-run; self-report only.
23. [Sonar, State of Code Developer Survey (Jan 2026)](https://www.sonarsource.com/state-of-code-developer-survey-report.pdf).
    **Tier B.** Vendor sells code-quality tooling; N not clearly stated.
24. [Anthropic, Claude Code power-user tips (2026-06-25)](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips);
    [worktrees docs](https://code.claude.com/docs/en/worktrees). **Tier C** for the 3–5 figure —
    vendor, own product, self-described as collected anecdote.
25. [Dzombak, "Getting Good Results from Claude Code" (2025-08-08)](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/).
    **Tier C.** Source of the C-085 quote; single individual.
26. [Benson, Personal Kanban WIP limit](https://personalkanban.com/pk/uncategorized-how-to-setting-your-personal-wip-limit/);
    [Benson on running many projects](https://personalkanban.com/pk/general-what-you-say-you-have-too-many-projects-and-cant-limit-wip/).
    **Tier C.** Self-declared arbitrary; author sells courses.
27. [Newport, GQ interview](https://www.gq.com/story/cal-newport-slow-productivity-interview);
    [Forte, weekly review as OS](https://fortelabs.com/blog/the-weekly-review-is-an-operating-system/).
    **Tier C.** Prescription, no data; both authors sell books/courses.
28. [MBO Partners Client of Choice 2020](https://event.hbrturkiye.com/storage/uploads/client-of-choice-2020-6152c243355d2.pdf);
    [Antenna 2019](https://www.lemonly.com/general-uploads/Work/191010_Antenna_ConsultantSurvey_eBook_Final.pdf);
    [Antenna 2020](https://www.lemonly.com/general-uploads/Work/201125_Antenna_ConsultantSurvey_eBook_WF.pdf);
    [SPI Research 2025 summary](https://www.saibongroup.com/blogs/consultant-utilization-rate-benchmark).
    **Tier B.** All run by firms selling to the surveyed population.
29. Practitioner blogs on parallel-session limits, all **Tier C**:
    [engineered.at](https://engineered.at/articles/your-parallel-agent-limit),
    [codewithseb](https://www.codewithseb.com/blog/parallel-claude-code-sessions-git-worktrees-guide),
    [dev.to/jcamarate](https://dev.to/jcamarate/why-20-claude-code-instances-break-down-and-what-to-do-2i5j),
    [codefather.dev](https://codefather.dev/blog/post/vibecoding-parallelizes-features-but-doesnt-parallelize-me),
    [Context Studios](https://www.contextstudios.ai/blog/run-10-claude-code-agents-review-is-your-real-bottleneck),
    [MindStudio](https://www.mindstudio.ai/blog/claude-code-git-worktree-parallel-branches) (vendor),
    [Backgrind](https://backgrind.com/blog/git-worktrees-parallel-agents/) (vendor selling the fix).
30. "23 minutes" tracebacks: [oberien](https://blog.oberien.de/2023/11/05/23-minutes-15-seconds.html),
    [Mazeroff](https://geoffmazeroff.com/2026/03/23/the-context-switching-statistic-that-got-lost-in-translation/).
    **Tier B.** Trusted because both show their work and check the primary papers.

**Rejected — do not cite:**

31. [firmem.com/Practiq consulting benchmarks](https://firmem.com/benchmarks/how-many-engagements-can-a-boutique-consulting-firm-handle)
    and [pharallax.ai](https://pharallax.ai/insights/consulting-benchmarks/). Precise-seeming
    solo-consultant capacity benchmarks attributed to a "Kennedy Research 2024 Independent
    Consultant Survey" and an "SCIP 2024 Solo Consultant Study." Neither study is traceable
    anywhere outside those pages. Treated as fabricated citations.
