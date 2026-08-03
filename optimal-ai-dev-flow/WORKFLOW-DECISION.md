# Workflow Decision — Which Operating Model a Solo Consultant Should Rely On

_2026-08-02 | Decision note derived from [`REPORT.md`](REPORT.md), [`findings/w1..w9`](findings/), and the four [`playbooks/`](playbooks/). No new research was conducted for this note — it is a determination made against the existing corpus._

**Question answered:** of the workflows available to a one-person AI-leveraged consultancy, which one should be relied on for maximum effectiveness, efficiency, and financial gain?

**Answer in one line:** run the single-agent loop with a fresh-context reviewer, throttled by a substantive-review log, sold as a two-product fixed-fee engagement under ISO 20700's three gates.

---

## 1. The framing correction that changes the answer

"Workflow" is two independent axes, and they do not optimise together:

| Axis           | What it governs                        | Which criteria it moves   |
| -------------- | -------------------------------------- | ------------------------- |
| **Delivery**   | How the work actually gets done        | Effectiveness, efficiency |
| **Commercial** | How the work gets scoped, sold, priced | Financial gain            |

**Financial gain is almost entirely a commercial-axis variable.** Under a flat Max subscription, token cost below the cap is not a marginal cost. Every cost-optimisation scheme in the corpus was refuted or unsupported: tiered per-token routing (X-02), cheap-tier reviewer routing (C-177, the most load-bearing revision in the whole cost programme), OpenRouter as a savings mechanism (C-121, C-136), the two-machine tier split (C-151), and the "$80–120/mo blended" target — which is **arithmetically impossible**, because three separate claims assumed a flat subscription fee shrinks with reduced usage (C-163, C-174, C-187).

**There is no meaningful money on the cost side.** Optimising delivery buys throughput and quality. It does not buy dollars until the commercial structure converts throughput into revenue. That conversion is the whole game.

---

## 2. Delivery workflows — the candidate set

| Workflow                                                                                      | Effectiveness                                                                                                                                                                                                                                              | Efficiency                                                                                                                                                                                                                                                             | Verdict                                                 |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Single-agent loop** — Frame → Explore → Plan → Execute → Verify → Review → Commit → Handoff | High. Anthropic's own documented loop (C-011, C-017, Tier A). Phases 0–2 are explicitly skippable for a change describable in one sentence                                                                                                                 | High. Tight context, `/clear` between tasks, subagents for investigation                                                                                                                                                                                               | **Adopt as the default**                                |
| **Writer/Reviewer** — fresh-context reviewer subagent, narrow mandate                         | Documented pattern (C-048, verbatim: a fresh context "won't be biased toward code it just wrote"). But the supporting study measured **+25 pts for a weak generator and only +3.0 for a strong one** — and a frontier model is the strong-generator regime | Cheaper than fan-out resampling: 2.44 average samples vs 8.9 for independent parallel resampling                                                                                                                                                                       | **Adopt, expecting a small marginal gain** (CA-4)       |
| **Multi-agent fan-out / Agent Teams**                                                         | Measured on breadth-first decomposable tasks. Anthropic states it is "less effective for tightly interdependent tasks such as coding" (C-027, exact)                                                                                                       | ~15x tokens vs chat (C-026); ~7x more when teammates run in plan mode (C-031); still gated behind an experimental flag                                                                                                                                                 | **Reject**                                              |
| **Parallel worktree lanes**                                                                   | Real and natively supported — `--worktree`, `/batch`, `isolation: worktree` (C-045, C-074)                                                                                                                                                                 | **No published lane ceiling exists.** Every figure found (2–4, 3–5, 5–30, 10) is assertion (C-076, C-084)                                                                                                                                                              | **Use — but let the review log set the count**          |
| **Autonomous loop (Ralph-style)**                                                             | Fresh context per iteration, filesystem/TODO/git as memory (C-050)                                                                                                                                                                                         | Reward-hacking concentrates in exactly the long unattended runs you want: the visible-vs-held-out test gap grows ~28 pts per tenfold increase in code size                                                                                                             | **Reject as a primary mode; OS-sandbox if used at all** |
| **Heavy spec ceremony** (spec-kit / Kiro / PRP)                                               | No controlled comparison exists anywhere (X-03)                                                                                                                                                                                                            | Instruction-file **existence** pays enormously (0% → 55–68% compliance, Cohen's h = 1.93). **Elaboration** pays nothing (size/position/architecture all null, BF10 = 0.096) — and context files **raise** inference cost 20–23%, p < 0.001 (C-107, direction inverted) | **Reject the ceremony; one instruction file per repo**  |

### The governing constraint

**Review capacity, not tokens and not lane count.** The strongest study in the corpus — 802 developers, 196,212 PRs, fixed-effects panel (arXiv:2607.01904, Tier A) — found throughput rose **2.09x** while substantive review fell **39% → 21%** and silent approvals roughly doubled, with **merge rate flat and revert rate slightly down** throughout. A cost-and-velocity dashboard would have shown that programme succeeding.

Any workflow that outruns your ability to actually read the diff produces defects invisibly. That is why lane count is an output of the review log rather than an input to the design.

---

## 3. Commercial workflows — where the money actually is

| Model                                                                            | Financial verdict                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hourly / T&M**                                                                 | **The worst possible fit for an AI-leveraged solo practice** — the one model where getting 3x faster reduces revenue 3x. FAR 16.601 (Tier A, binding) states it flatly: T&M "provides no positive profit incentive to the contractor for cost control or labor efficiency," and requires a ceiling the contractor exceeds at its own risk |
| **Monthly retainer**                                                             | Reasonable for ongoing operations. Does not capture productisation gains. No outcome evidence in either direction                                                                                                                                                                                                                         |
| **Value-based**                                                                  | The only supporting data is a single undated, self-selected vendor survey whose income correlation is confounded in the obvious direction — consultants who can already command large engagements are the ones who can switch to value pricing (F-W8-15, Tier C)                                                                          |
| **Two-product split: bounded fixed-fee Diagnostic + fixed-price Build packages** | **The structurally defensible one.** Follows FAR 16.104's rule that requirement uncertainty determines contract type: uncertainty is highest at diagnosis (bounded fee, hard time-box, defined deliverable) and lowest at a repeated build (F-W8-13, Tier A)                                                                              |

### The compounding mechanism

FAR 16.104's structural insight: **"as requirements recur, cost risk should shift to the contractor,"** and risk decreases with repetitive acquisitions.

| Stage                     | Contract type                                                            |
| ------------------------- | ------------------------------------------------------------------------ |
| E2–E5 Diagnostic          | Bounded fixed fee                                                        |
| E6 Build, engagements 1–3 | Fixed price + generous ceiling — you are buying your own estimation data |
| E6 Build, engagement 4+   | Fixed price, tightened                                                   |

Every hour AI saves inside a fixed price is margin retained. **This is the only place in the entire analysis where delivery-side effectiveness converts directly into money** — which is why productisation and pricing are one problem, not two.

---

## 4. The determination

1. **Delivery.** One loop: Frame → Explore → Plan → Execute → Verify → Review → Commit → Handoff. Skip phases 0–2 for anything describable in one sentence. Reviewer subagent at **frontier tier** — routing the reviewer cheap saves nothing you are actually paying and measurably degrades recall (§3.4, the composed cheap-tier rule).
2. **The non-negotiable gate.** You opened the diff and wrote a note. **No note, no merge.** Lane count is whatever keeps substantive-review share ≥90%, discovered from your own log rather than imported from a blog.
3. **Harness.** One instruction file per repo under a **content test** — keep a line only if nothing else in the repository states it. Move anything that must _hold_ into a hook: prose compliance decays ~5.6% per generated function, and hooks are deterministic where instruction files are advisory (C-021, verbatim). Delete the rest per `playbooks/harness-blueprint.md` §2.
4. **Commercial.** Diagnostic (E2–E5) and Build (E6) separately contracted, separately priced, either sellable without the other. Fixed fee both. **Never hourly.** Full specification in `playbooks/engagement-playbook.md`.
5. **Client separation, absolute.** One-way flow: generic → client, never the reverse without an explicit de-identification-and-permission gate. Two independent layers require this — harness mechanics (every cross-project context mechanism is a leak path, and **user-scope imports load without an approval dialog**) and contract law (residuals clauses cover only _unaided memory_, so a per-client knowledge repo has **no contractual protection at all**, F-W8-09).

### First move, before anything else

**The substantive-review log.** Four weeks, one line per merged unit: did you open it, did you write a note.

This is first because the evidence says so. In the one field study, review-side damage accrued _during_ the ramp — which makes the corpus's own ordering, with weekly review sequenced last (C-189), the sequencing the evidence argues against. Everything downstream is calibrated against a baseline that does not yet exist.

**Kill criterion:** logging costs >10 min/week, or you catch yourself back-filling entries. Then fall back to an instrumented proxy (was the diff opened, for how long) and stop self-rating.

---

## 5. What this determination is exposed to

Stated so it is not mistaken for settled.

- **The review-capacity thesis is enterprise evidence applied to n=1.** Its mechanism is reviewer-_pool dilution_, which structurally cannot occur for one person. The study is a single firm, non-randomised, self-described as a "near-best-case setting," and a preprint. The direction is well evidenced; **the magnitude for one operator is unknown** (CA-6). The solo variant of the metric must also be self-reported, and self-report about AI-assisted work is unreliable in the optimistic direction — METR's developers forecast 24% faster, estimated 20% faster afterwards, and measured **19% slower** (CA-1).
- **The 80/20 reuse ratio — the entire productisation thesis — has zero evidence base anywhere.** Not weak evidence: none. No study, survey, or dataset measures what fraction of an engagement's artefacts carries between clients (W8 Gap 1). Instrument it per artefact from engagement 1 and read it at engagement 4 (`engagement-playbook.md` §7). If reuse-unchanged is under 50% by minutes, the fixed/variable split is wrong for your market.
- **Nothing in this corpus addresses pipeline.** For most solo consultants the binding constraint on income is deal flow, not delivery capacity or margin structure. If that is true here, the highest-value work lies in a direction this research never looked — and no finding in `REPORT.md` speaks to it.
- **The Judge apparatus may be worth ~3 points for this operator.** The strongest supporting study measured +25 pts for a weak generator and **+3.0 for a strong one**. On a frontier model that is well inside the noise of a single-reviewer setup (CA-4). Start with the built-in reviewer; build a fixed-schema Judge skill only if the reviewer demonstrably misses a defect class you can name.
- **Repo facts are stale-risk.** Stages 2 and 7 of the adoption sequence depend on C-168, C-192, C-200, C-205 — audited 2026-06-27 to 2026-07-14 and flagged high-freshness-risk. Re-audit before acting on either.

---

## 6. What was explicitly rejected

Not deferred — rejected, each for a stated reason:

| Rejected                                          | Why                                                                                                |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Multi-agent fan-out / Agent Teams                 | Wrong task shape for coding; ~15x tokens; experimental                                             |
| Cheap-tier reviewer routing                       | Directly contradicted (C-177); and moot under a flat subscription                                  |
| OpenRouter / metered routing (Stage 7)            | Off by default. Only fires above ~$150–200/mo of API-equivalent spend **outside** the subscription |
| Tier Policy blocks in CLAUDE.md                   | **Nothing reads a tier annotation in a markdown file and routes on it** (C-185, REFUTED)           |
| The $80–120/mo blended cost target                | Arithmetically impossible while Max is the backbone                                                |
| Cross-project session topology                    | Not a supported configuration; Anthropic closed the request as not planned                         |
| Heavy spec ceremony / elaborate instruction files | Elaboration measured null; context files raise cost 20–23%                                         |
| Hourly / T&M billing                              | Converts every efficiency gain into a revenue loss                                                 |

---

_Traceability: claim IDs (C-nnn), contradiction resolutions (X-nn), and counterarguments (CA-n) refer to [`REPORT.md`](REPORT.md) §2–§7. Findings (F-Wn-nn) refer to the corresponding file in [`findings/`](findings/). Every quantitative figure carries its evidence tier and date at its source; figures dated before 2026-08-01 in a volatile category (pricing, benchmarks, rate limits) should be re-derived at use time per `REPORT.md` §5._
