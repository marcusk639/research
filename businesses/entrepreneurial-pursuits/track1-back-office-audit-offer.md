# Track 1 — "AI Back-Office Audit + Automation Sprint" Offer & Co-Sell Pitch

**Created:** 2026-06-13 · **Owner:** Marcus · **Track:** 1 (CPA advisory/automation engine, RANK 1)
**Derived from:** `PLAN.md` Phase 1 Track 1 (A3 advisory line) + `REPORT.md` v2 §5–6.
**Status:** draft offer, ready to use once D1 (revenue-share) and D6 (brother co-sells) are resolved.

> **What this is:** the productized service ladder that converts the warm CPA channel
> (TWK + brother Chris's client book) into paid advisory revenue, plus the one-sentence
> pitch Chris uses to open the door. This is the unblocked companion to signing D1.

---

## 0. Constraints this offer must respect (load-bearing)

These are baked into scope and copy below. Do not let a sales conversation drift past them.

1. **Marcus is non-CPA, influence-only.** The offer sells _workflow automation + advisory
   analysis_, never accounting/tax/attest work. A licensed CPA signs anything that is
   accounting work product.
2. **Capacity capture is 20–38%, not 100%.** Every ROI claim is framed as _recovered
   capacity / reduced cycle time_, never "we'll 10x your throughput." Under-promise.
3. **Tax-prep AI carries IRC §7216 + Circular 230 §10.22 obligations.** The diagnostic
   explicitly scopes _back-office / bookkeeping / workflow_ first; any tax-touching
   automation gets a compliance gate before it ships.
4. **Karbon (and QBO) are serious incumbents — do not rebuild their native features.**
   The audit _composes and fills gaps around_ the existing stack; it never proposes a
   parallel system that duplicates Karbon WIP reports, billing, or PM.
5. **Client data stays governed.** No PHI/PII or client financials move into an
   ungoverned LLM. Read-only by default; BAA/DPA where any data is touched.

---

## 1. The offer ladder

Three rungs, each a complete sale on its own. The diagnostic is the wedge; the sprint and
retainer are where the money is. Pricing matches `PLAN.md` Track 1 A3.

| Rung  | Name                                  | Price               | Duration  | What they get                                                                                                                                     | Purpose                                                           |
| ----- | ------------------------------------- | ------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **1** | **AI Back-Office Audit** (diagnostic) | **$2,500–5,000**    | 1–2 weeks | A prioritized findings report: where staff hours leak, which workflows are automatable, ranked by ROI and effort, with a recommended sprint scope | Low-risk entry; produces the shareable artifact that sells rung 2 |
| **2** | **Automation Sprint**                 | **$6,000–15,000**   | 3–6 weeks | One or two automations built and shipped on their existing stack (Karbon/QBO/SharePoint/Teams), with a before/after metric and staff handoff      | The proof-of-value; converts to retainer                          |
| **3** | **Fractional AI Ops Retainer**        | **$3,000–5,000/mo** | ongoing   | Continuous workflow improvement, new automations, exception monitoring, monthly partner-facing ROI report                                         | Durable recurring revenue; the real engine                        |

**Conversion math (from the plan's evidence):** ~62% of SMBs convert a project into a
retainer within 6 months. Price the diagnostic to be a near-impulse "yes" for a partner;
make the sprint the obvious next step; let the retainer be the natural landing place.

**Highest-revenue hook within the offer:** **Bookkeeping Exception Review + Advisory Report
Drafting** — it's recurring, it's back-office (no §7216 tax-prep exposure), and it visibly
returns partner/manager hours.

---

## 2. Diagnostic deliverable — the audit (rung 1 detail)

The diagnostic is the product that does the selling. It should land as a tight, partner-
readable report (≤10 pages) with this spine:

1. **Capacity leak map** — where staff hours are spent vs. where they create billable value.
2. **Top 5 automatable workflows**, each scored: _effort (S/M/L) × annual hours recovered ×
   risk/compliance flag_. Honest 20–38% capture applied.
3. **One "quick win"** Marcus can ship in the sprint with a measurable before/after.
4. **Stack-fit note** — what the existing Karbon/QBO/SharePoint stack already does (don't
   rebuild) vs. the real gaps.
5. **Recommended sprint scope + price** (the rung-2 close, written into the report).

### Concrete anchor candidates (validated TWK pain points)

These come straight from the TWK meeting record (`docs/super-badass-skills-probably.md`
P1–P5) and double as a menu for any firm with the same shape:

- **Time-entry hygiene** — inconsistent coding, missing descriptions; preparers log to
  whatever project is open. _Automatable: validation + missing-description detection +
  nightly flag report._ (Needs Karbon export/API + published coding rules first.)
- **SharePoint knowledge-base cleanup** — duplicates, empty folders, no naming convention,
  staff don't trust it. _Automatable: dedup/triage pass + naming convention + intake rule._
- **Execution/ownership gap** — initiatives stall because only the partner drives them.
  _This is Marcus's primary value-add: be the named weekly owner, not another plan._
- **Service-tier / budget-average framework** — exists but stalled on variance complexity.
  _Advisory analysis, not automation; apply the 20–38% capacity reality._
- **Unbilled WIP** — hourly-after-the-fact billing, no threshold trigger, no owner.
  _Automatable: WIP-threshold alerting — but Karbon already has the WIP report, so wrap/
  alert, don't rebuild; watch for Opzer dashboard overlap._

> Note: the first three are the strongest sprint candidates for a _first_ engagement —
> high visible pain, back-office (no tax-compliance gate), low rebuild-Karbon risk.

---

## 3. The brother's co-sell pitch (Decision D6)

The whole ceiling difference ($120k vs $200k) turns on whether Chris **actively co-sells**
vs. just hands over names. Give him copy so frictionless he'll actually use it.

### One-sentence intro (the ask)

> "My brother Marcus — ex-Meta engineer, now does AI workflow automation for accounting
> firms — runs a fixed-fee back-office audit that finds where your staff hours are leaking
> and what's worth automating. Want me to introduce you? It's a couple grand and you keep
> the report either way."

### Why it works

- **Borrowed trust** — it's the partner vouching, the warmest possible channel.
- **Credential up front** — "ex-Meta engineer" does the de-risking in four words.
- **Fixed fee + keep the report** — removes the "open-ended consulting" fear.
- **Specific outcome** — "where your staff hours are leaking," not "AI transformation."

### Email variant (Chris forwards / BCCs Marcus)

> Subject: quick intro — Marcus (AI workflow automation)
>
> [Name] — wanted to connect you with my brother Marcus. Background's software engineering
> (Meta), and he's been building AI automation into our own back office at TWK — time-entry
> cleanup, document intake, WIP follow-ups, that kind of thing.
>
> He does a fixed-fee audit ($2.5–5k) that maps where your team's hours go and what's
> actually worth automating on the tools you already run (Karbon/QBO). You get the report
> regardless of whether you do anything after.
>
> Worth a 20-minute call? I'll let you two take it from here.

### What Chris needs to do (and not do)

- **Do:** send the intro, name 3–5 client firms, vouch once.
- **Don't:** quote scope, negotiate price, or promise tax/accounting work. He opens the
  door; Marcus runs the diagnostic call.

---

## 4. Ideal client & qualification

**Best-fit profile:** 5–30-person accounting/CPA firm, already on Karbon or QBO, partner-
bottlenecked, in the brother's referral network (warm intro available). SWLA economy is
_contracting_ — this is warm-channel arbitrage, not a cold land-grab, so qualify hard on
"is there a warm intro?"

**Quick qualification on the intro call:**

- Who feels the pain — a partner, or staff? (Need a partner with budget authority.)
- What's the stack? (Karbon/QBO = fast; bespoke/legacy = scope carefully.)
- Is there one workflow they'd pay to fix today? (If no concrete pain, it's a no.)
- Can they give read access for the audit? (No access = no diagnostic.)

**Disqualify / defer:** firms wanting tax-prep AI as the _first_ project (compliance gate),
firms with no warm intro (CAC math breaks), or anyone expecting a Karbon replacement.

---

## 5. Objection handling

| Objection                                                | Response                                                                                                                                                                                 |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "We already have Karbon / Opzer is building dashboards." | "Good — I build _around_ what you have, I don't replace it. The audit specifically flags where Karbon already covers you so you don't pay twice."                                        |
| "You're not a CPA."                                      | "Correct — I do the workflow and automation engineering. Anything that's accounting work product, your CPAs own and sign. I make their hours go further."                                |
| "Will AI touch our client/tax data?"                     | "Back-office workflows first, read-only by default, governed access only. Anything tax-touching gets a compliance review (§7216 / Circular 230) before it ships."                        |
| "How do I know it'll pay off?"                           | "The audit is fixed-fee and you keep the report. If the sprint doesn't show a before/after metric, you don't go to retainer. I quote recovered capacity at 20–38%, not fantasy numbers." |
| "We don't have time to implement another initiative."    | "That's the actual product — I'm the named owner who drives it weekly, not another plan that sits there."                                                                                |

---

## 6. Activation checklist

- [ ] **D1 resolved** — revenue-share papered (gates whether TWK work counts toward Marcus's share).
- [ ] **D6 resolved** — Chris commits to active co-sell; he gets the §3 copy.
- [ ] Ship the **TWK reference automation** first (`PLAN.md` Track 1) → it _is_ the
      "before/after" proof the audit report points to. Sell from a live result, not a deck.
- [ ] Stand up a one-page audit offer sheet + a simple intake form for read access.
- [ ] Chris names the first **3–5 firms**; Marcus runs the first diagnostic.

---

## 7. Open items to confirm before first external sale

- **[VERIFY]** TWK reference automation has a shareable before/after metric (Day-60 goal).
- **[VERIFY]** Revenue-share terms cover externally-referred firms, not just internal TWK work.
- **[VERIFY]** Read-access path for diagnostics (Karbon export/API availability) at target firms.
