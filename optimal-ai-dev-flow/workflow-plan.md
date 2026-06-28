# Personalized AI Workflow Optimization Plan

**Subject:** Cost-effective, high-quality AI development workflow for Marcus  
**Based on:** `v1.md` research findings + observed session patterns (Jun 2026)  
**Date:** 2026-06-27

---

## Phase 0: Situation Assessment (Already Complete)

### What the v1.md Research Confirms

Your current workflow (Claude Max all the time) is **not wrong** — for heavy multi-file agentic work, it's the single most cost-effective option at scale. The subscription arbitrage is real: ~$13,400 saved over 8 months vs. raw pay-as-you-go API. You should keep Claude Max.

**The problem is not the plan — it's efficiency within the plan.**

### What the Session Patterns Reveal

You are not primarily a software developer. You are a:

- High-volume research operator (4–10M tokens per deep-research run)
- Multi-track entrepreneur managing 9 business ventures in sequence
- Legal/financial case manager running active settlement and VA tracks
- Occasional software builder (CPA automation, gated on §7216 review)

This means the cost levers in v1.md need to be reweighted for your actual workload:

| v1.md Recommendation                        | Relevance to Your Workload                                         |
| ------------------------------------------- | ------------------------------------------------------------------ |
| AI.md cuts token consumption 40%            | HIGH — applies to research repos, not just code repos              |
| Two-tier stack (IDE autocomplete + agentic) | MEDIUM — your coding volume is low currently                       |
| OpenRouter Layer 3 for bulk tasks           | HIGH — most of your bulk work is research + document gen, not code |
| Declarative spec → agent → review           | HIGH — correct model for CPA automation when you build it          |
| Checkpoint + fallback discipline            | CRITICAL — you burned 4.78M tokens on a failed VR&E run            |

---

## Phase 1: Context Scaffolding — Eliminate Blind Exploration

**Goal:** Reduce the "exploratory search" phase of every agent run by 40–60% using maintained context documents.

### 1.1 — Create a `CONTEXT.md` per active research subject

The v1.md `AI.md` principle applies to research repos: when agents start a new session without knowing what's already established, they re-explore. This burns tokens.

For each active subject directory, create `<subject>/CONTEXT.md` containing:

```markdown
# <Subject> Context

## What's established (do not re-research)

- [Verified fact 1 with source]
- [Verified fact 2 with source]

## Open questions (current research targets)

- [Question 1 — assign to this run]

## Key constraints

- [Constraint or scope limit]

## Sources already consumed

- [URL or doc — skip re-fetching]
```

**Apply immediately to these active subjects:**

- `unemployment-fraud-detection/` — 25/29 sources verified; REPORT.md is final
- `fmla-retaliation-settlement/` — counter window, timeline, and figures are settled
- `va-disability/` — claim plan phases logged; avoid re-deriving VA rating rules
- `optimal-ai-dev-flow/` — this document is the output; v1.md benchmarks are locked

**Anti-pattern:** Do not use CONTEXT.md as a live scratchpad. It should only contain verified, stable facts. Open questions move out as they get answered.

### 1.2 — Maintain a `WORKFLOW.md` at the repo root

A single file the agents can read in the first 2,000 tokens of any session:

```markdown
# Research Repo Workflow

## Active tracks (priority order)

1. CPA automation (Track 1) — funding everything else
2. [Next track]

## Sequencing rule

One track at a time. CPA consults → income → fund parallel tracks.

## Research conventions

- deep-research skill for substantive new topics
- source-capture skill for archiving discovered sources
- Every run must cite claims inline
- Primary output: <subject>/REPORT.md

## Models in use

- Claude Max: all interactive + high-stakes work
- [OpenRouter when configured — see Phase 4]
```

**Verification:** After creating CONTEXT.md files, run one deep-research task and compare token count vs. a baseline run on the same subject. Target: 30–40% reduction.

---

## Phase 2: Task-Tier Routing Rules

**Goal:** Match task complexity to model cost. Not every prompt needs Opus.

### The Three Tiers for Your Workload

| Tier                         | Model                                           | Your Tasks                                                                                                           |
| ---------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Tier A — Judgment**        | Claude Max (Opus/Sonnet)                        | Settlement negotiation, VA strategy, CPA advisory, architectural decisions, complex legal/financial analysis         |
| **Tier B — Generation**      | Claude Max (Sonnet/Haiku)                       | Writing venture drafts, collateral generation, document formatting, CPA back-office templates                        |
| **Tier C — Bulk/Repetitive** | OpenRouter DeepSeek V4 Flash ($0.09/M) or Haiku | Formatting reports, running grep-style research queries, generating boilerplate, CPA missing-item detection at scale |

### Routing Decision Tree

```
Is this task high-stakes (legal, financial, medical, architectural)?
  YES → Tier A (Claude Max, Opus priority)
  NO →
    Is this a novel research question requiring synthesis across sources?
      YES → Tier A (deep-research with Claude Max)
      NO →
        Is this generation from a known spec or template?
          YES → Tier B (Claude Max Haiku, or Sonnet for longer docs)
          NO → Is this bulk/repetitive (100+ similar items)?
            YES → Tier C (OpenRouter Flash or local)
            NO → Tier B
```

### Practical Application

**Tier A examples:**

- Deep-research runs on new subjects
- Settlement counter-offer framing
- VA nexus letter strategy
- CPA client advisory output (any client-facing deliverable)

**Tier B examples:**

- Writing venture chapter drafts once outline is locked
- SDVOSB proposal boilerplate from existing templates
- RCM denial code lookup tables
- Reformatting/editing completed research reports

**Tier C examples (configure OpenRouter for these):**

- Bulk CPA audit: scan 200+ transactions for missing-item patterns
- Homegroups collateral variations (A/B versions of same asset)
- Recovery content calendar — repeating post generation
- Formatting REPORT.md artifacts into specific deliverable formats

---

## Phase 3: Research Run Optimization

**Goal:** Eliminate the 4.78M token waste pattern from failed runs.

### 3.1 — Pre-run question sharpening (mandatory)

Before launching any deep-research run, write a one-paragraph "question statement" that answers:

1. What is the specific question?
2. What would a complete, usable answer contain?
3. What do I already know that the agents should NOT re-derive?
4. What sources should be excluded (already captured, paywalled, etc.)?

This goes in the prompt, not as context. A 200-token question statement can save 2M tokens of exploratory wandering.

**Anti-pattern:** "Research VR&E self-employment funding" → agents explore the entire VR&E regulatory landscape  
**Pattern:** "Confirm the dollar threshold for VR&E counselor vs. supervisor approval of self-employment startup costs, per 38 CFR § 21.94 or nearest equivalent. Already know: $2,500 is the threshold per prior research. Confirm or correct with primary source citation."

### 3.2 — Checkpoint before deep runs

Before a 100+ agent run, ask: "What does success look like, and how will I know the run failed early?"

If you cannot answer both questions, the run is underspecified. Refine first.

### 3.3 — Subject staging: draft → deep → verify

Three-stage research model instead of one monolithic run:

| Stage      | Tool                                | Token target |
| ---------- | ----------------------------------- | ------------ |
| **Draft**  | Single Claude session, no subagents | <50K tokens  |
| **Deep**   | deep-research skill                 | 2–6M tokens  |
| **Verify** | source-capture + spot-check         | <200K tokens |

The Draft stage produces the question statement for the Deep stage. This prevents the Deep stage from re-discovering what you already know.

---

## Phase 4: OpenRouter Layer 3 — Setup and Use

**Goal:** Route Tier C tasks to DeepSeek V4 Flash at $0.09/M, freeing Claude Max for Tier A/B.

### 4.1 — What to set up

This is a one-time configuration task (1–2 hours):

1. Create an OpenRouter account and fund with $30–50 (monthly budget for Tier C)
2. Set up two model aliases:
   - `bulk-fast` → `deepseek/deepseek-v4-flash` (repetitive/formatting/generation)
   - `arch-plan` → `deepseek/deepseek-v4-pro` (architecture planning when Claude is rate-limited)
3. Configure Cursor IDE (Layer 1) to use `claude-sonnet-4.6` for inline completion

**Monthly cost addition:** ~$15–30/month for Tier C volume  
**Claude Max hours freed:** Estimate 20–30% reduction in Max token consumption

### 4.2 — Layer 3 use cases for your specific tracks

| Track           | Tier C task                                    | Model             |
| --------------- | ---------------------------------------------- | ----------------- |
| CPA Track 1     | Missing-item detection across 200 1040 returns | DeepSeek V4 Flash |
| Writing venture | 30-day content calendar drafts                 | DeepSeek V4 Flash |
| Homegroups      | A/B variations of GTM collateral               | DeepSeek V4 Flash |
| RCM Copilot     | Denial code lookup → template mapping          | DeepSeek V4 Flash |
| SDVOSB          | Proposal boilerplate generation                | DeepSeek V4 Flash |

**§7216 compliance note:** Client tax data (PII, financial records) must NOT be sent to OpenRouter. Keep Track 1 client-data workflows on local Claude Code instances only. OpenRouter is safe for non-client data (structure templates, anonymized examples, collateral drafts).

---

## Phase 5: Dual-Mac Fleet Alignment

**Goal:** Map the two machines to the tier system to prevent context thrashing.

### Current setup

- **M4 Pro (48GB)** — primary workstation, SSH master
- **M5 Air (24GB)** — runner/secondary, SSH linked

### Recommended mapping

| Machine | Tier  | Task type                                                                     |
| ------- | ----- | ----------------------------------------------------------------------------- |
| M4 Pro  | A + B | Interactive work, judgment calls, high-stakes sessions, CPA advisory output   |
| M5 Air  | B + C | Autonomous batch runs, overnight research, bulk generation, collateral drafts |

### Operational rules

1. **Never run unattended Tier A work on M5 Air.** High-stakes output needs human review before use.
2. **Batch C-tier tasks** — accumulate 5–10 Tier C items, then run them as one unattended session on M5 Air overnight.
3. **M4 Pro stays context-rich.** Keep the WORKFLOW.md and active subject CONTEXT.md files loaded here for fast session startup.
4. **Checkpoint file on shared drive.** If M5 Air is running a batch, write progress to a shared checkpoint file M4 Pro can read. This prevents re-running completed sub-tasks if the session fails.

---

## Phase 6: CPA Automation — When You Build It

**Goal:** Apply the declarative spec → agent → review model from v1.md when CPA Track 1 software development begins.

### Pre-build checklist (do these before writing any code)

- [ ] §7216 architecture review complete — data path documented and approved
- [ ] `AI.md` written for the CPA automation repo (module boundaries, typing rules, conventions)
- [ ] Feature spec written as a declarative document (not "build X" but "X must do A, B, C given inputs P, Q")
- [ ] Test cases written from spec (TDD: test before implementation)
- [ ] Model routing decided: which features need Sonnet, which can use Haiku

### Build workflow (when you start)

1. Write feature spec → hand to Claude Code Max (Layer 2 from v1.md)
2. Review output as a senior engineer, not a developer
3. Reject → refine spec → re-run (never edit agent output directly — fix the spec)
4. Merge when tests pass and spec is satisfied

**Anti-pattern:** Using Claude to write code while you supervise keystroke-by-keystroke. Your time value is in judgment and spec quality, not in watching agents type.

---

## Phase 7: Weekly Review Cadence

**Goal:** Catch drift early. 15 minutes per week.

### Weekly checklist

- [ ] Review last week's deep-research runs: did any produce low-quality output? Why?
- [ ] Update CONTEXT.md files for active subjects with new verified facts
- [ ] Check OpenRouter spend vs. Claude Max usage — is routing discipline holding?
- [ ] Review WORKFLOW.md — is the track priority still correct?
- [ ] Flag any Tier C tasks that ran in Tier A by mistake (cost waste)
- [ ] Update M5 Air batch queue for the coming week

---

## Summary: What Changes, What Stays the Same

|                      | Before                                      | After                                                   |
| -------------------- | ------------------------------------------- | ------------------------------------------------------- |
| **Claude Max**       | All tasks, all the time                     | Tier A + B tasks only (still most of the work)          |
| **Context files**    | CLAUDE.md per project (good start)          | Add CONTEXT.md per active subject + WORKFLOW.md at root |
| **Research runs**    | Launch directly, large exploratory prompts  | Draft question statement first, staged approach         |
| **Bulk tasks**       | Claude Max                                  | OpenRouter DeepSeek V4 Flash (~$0.09/M)                 |
| **Dual-Mac**         | Informal                                    | M4 = interactive/judgment, M5 = batch/autonomous        |
| **CPA coding**       | Not started (§7216 gated)                   | Spec-first when gate clears, agent executes             |
| **Total cost**       | $200/mo (Claude Max)                        | $200 + $15–30 (OpenRouter) = $215–230/mo                |
| **Value per dollar** | High (you're already in the arbitrage zone) | Higher — more coverage, less wasted token exploration   |

**The key insight:** You're already on the right subscription. The gains come from working smarter within it — better upfront context, staged research, and routing routine generation to cheaper models so Claude Max capacity stays available for the judgment work only you can define.
