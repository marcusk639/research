# Reusable Agents & Skills — Design Specs for `veteran-claims-app`

> **Status:** design-only (per user decision) · **Created:** 2026-07-09 · **Type:** proposals, not implementations
> **What this is:** specs for generalizable tools — distilled from this claim's work — that could help _other_ veterans through [`veteran-claims-app`](file:///Users/marcusklein/dev/veteran-claims-app) (Next.js + Vercel AI SDK; agents: Knowledge Assistant, Evidence/Checklist, Drafting; retrieval via `rag-system` MCP; Clerk auth; Neon Postgres). **Nothing here is built.** Each spec lists purpose, inputs, outputs, where it fits the existing architecture, and its guardrails.
> **Scope note:** these encode _method_, never this veteran's facts — no PHI, no names, no case-specific data.

## Cross-cutting guardrails (apply to EVERY tool below — non-negotiable)

The app already hard-enforces refusal of any request to exaggerate/fabricate and respects the free-VSO baseline (`veteran-disability-ai-resources/knowledge-base/representation-and-fees.md`). Extend that with:

1. **General-educational only, not individualized legal advice.** Non-accredited advice on a specific VA claim implicates 38 CFR 14.629 accreditation rules and unauthorized-practice-of-law (UPL) exposure. Every tool presents information and _options_, never "you should file X" as legal counsel; every output carries a not-legal-advice disclaimer and **routes the user to an accredited representative** (VSO/attorney via ogc.va.gov).
2. **No witness coaching, ever.** Any drafting-adjacent tool must refuse to write, script, or suggest wording for a buddy/spouse/lay statement — it may only generate _open-ended, non-leading memory prompts_ the witness answers themselves. (This is the single biggest credibility risk documented in the source claim.)
3. **No win-rate / "best attorney" claims as fact.** Representation tools present accredited options as candidates to vet (accreditation verifiable at ogc.va.gov), never a ranked leaderboard from marketing.
4. **No PHI training/leakage.** Tools operate on the user's own tracked claim data within their private workspace; nothing cross-tenant; uploaded documents remain opaque metadata (per the app's v1 non-goal).
5. **Requires legal review before shipping.** Any tool that touches representation, fees, or claim strategy is flagged for review by a VA-accredited attorney before it goes live to third parties.

---

## 1. `representation-matcher` (Knowledge Assistant sub-skill)

- **Purpose:** given claim stage + condition + geography, explain _which representation type fits and when_ (VSO vs. accredited attorney vs. claims agent), grounded in the fee-timing rule.
- **Inputs:** claim stage (initial / post-decision / appeal), condition category, state, whether a prior decision exists.
- **Outputs:** an educational decision guide — e.g., "pre-initial-decision → an attorney can't charge yet (38 U.S.C. § 5904(c)(1)); a free accredited VSO is the fit; here's how to find one" — plus the ogc.va.gov accreditation-search link. **Never** a ranked firm list.
- **Fits:** Knowledge Assistant Agent, sourced from the KB's `representation-and-fees.md` via the `rag-system` `search` MCP tool.
- **Guardrails:** #1, #3, #5. The "whether a prior decision exists" input maps to the same insight this claim surfaced (it gates both fee-timing and effective date) — the tool flags it as a question for the user's VSO, not something it answers.

## 2. `free-consult-prep` (Knowledge Assistant + Evidence/Checklist)

- **Purpose:** help a veteran get maximum value from a free attorney/VSO consult.
- **Inputs:** claim stage + condition category (from the user's tracked claim).
- **Outputs:** a checklist of what to bring (PHI-minimized) and a list of _the veteran's own_ questions to ask (accreditation, MST/PTSD _schedular_ appeal experience, contingency %, EAJA) + red flags (upfront fees on an initial claim are illegal; verify accreditation).
- **Fits:** Evidence/Checklist Agent (produces a checklist artifact), knowledge from the Knowledge Assistant.
- **Guardrails:** #1, #4. Explicitly instructs the user _not_ to bring internal strategy documents to a rater/consult.

## 3. `schedular-vs-tdiu-explainer` (Knowledge Assistant sub-skill)

- **Purpose:** educationally model the schedular-vs-TDIU tradeoff, foregrounding the earning-capacity implication (TDIU generally requires not maintaining substantially gainful employment).
- **Inputs:** current combined rating + whether the user wants to retain the ability to work.
- **Outputs:** a plain-English comparison (what each path is, the income-restriction tradeoff, that schedular 100% has no earnings bar) — _education, not a recommendation_.
- **Fits:** Knowledge Assistant, sourced from `knowledge-base/tdiu.md` + `ratings-and-va-math.md`.
- **Guardrails:** #1. Never tells the user which to pursue; surfaces the tradeoff so they discuss it with their accredited rep.

## 4. `gap-and-issue-auditor` (Evidence/Checklist Agent feature)

- **Purpose:** generalize this effort's issue-register method — scan a user's tracked contentions/evidence against the rating criteria and surface _documentation gaps_ (not legal conclusions).
- **Inputs:** the user's tracked claim data (contentions, evidence checklist, deadlines).
- **Outputs:** a prioritized list of _evidence gaps_ with the general category of evidence that typically addresses each (e.g., "no current-diagnosis document on file for contention X") + a nudge to discuss with their rep. **Never** "your claim is worth Y%."
- **Fits:** Evidence/Checklist Agent (operates on tracked metadata; consistent with the app's "don't parse document contents" v1 non-goal — it works from user-entered checklist state, not by reading uploads).
- **Guardrails:** #1, #4, #5.

## 5. Ports of the two corpus review agents (quality infrastructure, internal)

- **`citation-verifier` (port):** verify every legal/CFR/case cite the Knowledge Assistant surfaces against primary sources before it's shown, labeling marketing vs. primary. Internal quality gate, not user-facing. Directly addresses the "40 of 109 misstated" failure mode.
- **`claim-consistency-checker` (port):** for the Drafting Agent's worksheet outputs, cross-check user-entered facts (dates, diagnoses, employment) for internal contradictions and flag them back to the user to reconcile — never auto-"fix," never invent.
- **Fits:** both as internal middleware around the existing agents.
- **Guardrails:** #2 (the consistency checker flags, never rewrites witness content), #4.

---

## What NOT to build (deliberate exclusions)

- **No "rate my claim / predict my %" estimator** — invites reliance on a number no tool can responsibly give, and reads as legal advice.
- **No ranked attorney directory** — marketing-as-fact (#3); point to ogc.va.gov instead.
- **No auto-drafted buddy/spouse statements** — the exact coaching risk (#2); the Drafting Agent already refuses this, and any "statement helper" must be memory-prompt-only.
- **No cross-user data reuse** for training or matching (#4).

## Next step (if the user opts in to build)

Start with **#5 (`citation-verifier` port)** — lowest UPL risk, highest quality payoff, purely internal — as a proof of the pattern, then **#4 (`gap-and-issue-auditor`)** on tracked metadata. Defer #1–#3 until a VA-accredited attorney has reviewed the UPL posture (#5 guardrail).
