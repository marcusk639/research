# Engagement Playbook

_Phase C deliverable 4 | 2026-08-01 | Evidence base: `findings/w6-domain-rampup.md`, `findings/w7-process-diagnosis.md`, `findings/w8-productized-consulting.md`, `findings/w9-composition.md`_

**What this is.** A phase-gated, time-boxed, repeatable client engagement for a one-person
AI/operations consultancy. Structure follows ISO 20700:2017 (Tier A — the only international
standard defining a management-consulting engagement) rather than a self-invented five-phase
model, because the ISO decomposition is defensible to a client and a self-invented one is not
(F-W8-01).

**What this is not.** A validated method. **No study exists measuring whether ISO 20700
conformance changes any engagement outcome** (W8 Gap 7), whether productization improves win rate,
margin, or delivery hours (F-W8-16, W8 Gap 2), or whether a paid diagnostic converts better than a
proposal (W8 Gap 3). Every efficacy claim in the consulting-methods genre traces to someone selling
a course. This playbook is built on standards, binding regulation, and the handful of peer-reviewed
results that exist; where it is convention, it says so.

**The reuse ratio is an assumption, not a fact.** The project brief's 80/20 carryover target has
**zero evidence base** — no study, survey, or dataset measures what fraction of an engagement's
artefacts carries over between clients (W8 Gap 1). §7 of this playbook instruments it so the
operator can measure their own ratio by engagement 4. Treat 80/20 as a hypothesis under test.

---

## 0. The engagement at a glance

| Phase                       | Gate type                        | Time-box (elapsed)        | Billing                 | Kill point            |
| --------------------------- | -------------------------------- | ------------------------- | ----------------------- | --------------------- |
| **E0 — Qualify**            | Pre-contract (ISO Annex C)       | ≤2 h, unbilled            | Free                    | Decline               |
| **E1 — Contract**           | **ISO gate 1: Contracting**      | ≤3 business days          | —                       | No agreement, no work |
| **E2 — Discovery**          | Inside execution                 | 5–10 business days        | Fixed fee (Diagnostic)  | Refund-and-stop       |
| **E3 — Process diagnosis**  | Inside execution                 | 5–10 business days        | Same fixed fee          | Stop at findings      |
| **E4 — Opportunity rank**   | Inside execution                 | 2–3 business days         | Same fixed fee          | Stop at findings      |
| **E5 — Roadmap + decision** | **Client decision gate**         | 1 day + client's calendar | Diagnostic ends here    | Client declines build |
| **E6 — Build**              | Re-enters contracting (ISO §6.3) | Per work package          | Fixed price per package | Package abandoned     |
| **E7 — Closure**            | **ISO gate 3: Closure**          | ≤2 business days          | Final invoice           | —                     |

**Two products, not one.** E2–E5 is the **Diagnostic**. E6 is the **Build**. They are separately
contracted, separately priced, and either can be sold without the other. This is not a style
preference — it follows FAR 16.104's structural rule that requirement uncertainty determines
contract type, and uncertainty is highest at diagnosis and lowest at a repeated build (F-W8-13,
Tier A).

**Elapsed-time warning.** Every duration above is **practitioner convention, not measured data**.
No study measures how long any diagnostic methodology takes at SMB scale (W7 Gap 5). The one
exception is the 5-day kaizen-event box, which is a stated Lean Enterprise Institute convention
(Tier B for the convention, not for its optimality). Treat these as starting budgets to be
recalibrated against your own tracked hours from §7.

---

## 1. Phase E0 — Qualify

| Field                | Content                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | An inbound or referred conversation exists. Nothing else.                                                                                                                                                                                                                                                                                                                                                              |
| **Activities**       | Run the 8-item qualification checklist below. Ask nothing that requires client preparation.                                                                                                                                                                                                                                                                                                                            |
| **Artifacts**        | `qualify-<client>.md` — one page: the 8 answers, a go/no-go, and the reason.                                                                                                                                                                                                                                                                                                                                           |
| **Time-box**         | **≤2 hours total, including the call. Unbilled.** ISO 20700 Annex C places pre-contract context-understanding outside the governed process, and notes the provider "will devote considerable resources to this activity" — i.e. it is sales cost, not delivery cost (F-W8-04). Cap it so it stays that way.                                                                                                            |
| **Human checkpoint** | The call itself. Not delegable.                                                                                                                                                                                                                                                                                                                                                                                        |
| **Exit test**        | **All four hard gates pass, or decline.** Hard gates: (1) a named decision-maker will be in the room for E5; (2) the client can name one process and one number they want changed; (3) no regulated-data class is in scope that you have not already solved contractually (§6); (4) the engagement fits your active-engagement cap (§8). Soft signals may be ignored. A failed hard gate is a decline, not a discount. |

### E0 qualification checklist — FIXED, reuse verbatim

| #   | Question to the client                                                                        | Why it is here                                                                                                                                         | Disqualifying answer                                 |
| --- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| 1   | Who signs, and will they be in the room when we decide what to build?                         | ISO §4.1.3 assigns accountability for decisions and outcomes to the **client** (Tier A). If the decider is absent, accountability has nowhere to land. | "I'll take it to them afterwards."                   |
| 2   | Name one process you want changed and one number that would tell us it worked.                | Forces a measurable objective before contracting; ISO §5.5.6 requires acceptance criteria in the agreement.                                            | No number can be named after two attempts.           |
| 3   | Roughly how long does a case take end to end, and how long is someone actually working on it? | This is the touch-time ratio in question form (F-W7-17). Their inability to answer is itself the finding.                                              | (Not disqualifying — a blank is a positive signal.)  |
| 4   | What systems does this process touch, and do any of them record when a step changed status?   | Pre-screens the event-log gate (F-W7-09). Determines which of the two Diagnostic variants you are selling.                                             | (Not disqualifying — it sets the variant.)           |
| 5   | Does any of this touch health records, tax return information, or EU personal data?           | Each triggers a distinct, mandatory contractual instrument before any tooling touches the material (F-W8-10, Tier A).                                  | Yes, and the client will not execute the instrument. |
| 6   | Has anyone tried to automate this before? What happened?                                      | Prior bots are the arrested-scaling signal (F-W7-03).                                                                                                  | (Not disqualifying.)                                 |
| 7   | Who would lose a decision or an approval if this changed?                                     | Names the political failure mode early. Decision-rights conversations fail in person and cannot be delegated to tooling (W7 methodology table).        | "Nobody" — treat as unanswered, ask again in E2.     |
| 8   | What is your budget range for a two-to-four-week diagnostic?                                  | ISO §4.0-equivalent: agree the fee basis before accepting the engagement (IMC USA Code §9.0, Tier A).                                                  | Refuses to state any range.                          |

---

## 2. Phase E1 — Contract

| Field                | Content                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | E0 exit test passed. Budget range stated. Decision-maker identified.                                                                                                                                                                                                                                                                                      |
| **Activities**       | Fill the six-section agreement (below) and the 17-item work plan. Execute any data instrument from §6. Create the client repository (see `harness-blueprint.md` §Knowledge-repo variant).                                                                                                                                                                 |
| **Artifacts**        | `agreement-<client>.md` (6 sections), `workplan-<client>.md` (17 items), executed data instrument(s), empty per-client repo.                                                                                                                                                                                                                              |
| **Time-box**         | ≤3 business days from E0 go. If it exceeds a week, the client is not ready — return to E0.                                                                                                                                                                                                                                                                |
| **Human checkpoint** | Signature. Also: the operator personally reads the agreement's Context section aloud to the client and gets verbal confirmation. Context is the one section that is client-specific (F-W8-02) and therefore the one most likely to be wrong.                                                                                                              |
| **Exit test**        | **"Execution should not start until there is an agreement" (ISO §6.3, verbatim, Tier A).** All six sections filled, all 17 work-plan items either filled or explicitly struck with a one-line reason, acceptance criteria stated as a checkable condition, and every applicable data instrument from §6 executed. Any unstruck blank item fails the test. |

### E1 agreement template — FIXED (six sections, ISO 20700 §5.5)

| §     | Section                    | Fixed / Variable                    | Content rule                                                                                                                                                                                             |
| ----- | -------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5.5.2 | **Context**                | **VARIABLE — the only one**         | Current situation, client objectives, why now, assumptions and their impact. Every other section carries over. (F-W8-02, Tier A)                                                                         |
| 5.5.3 | Services and deliverables  | Fixed skeleton, variable line items | Name each artefact from the phase tables in this playbook.                                                                                                                                               |
| 5.5.4 | Approach and work plan     | **Fixed 17-item checklist**         | See below.                                                                                                                                                                                               |
| 5.5.5 | Roles and responsibilities | Fixed                               | Operator = MCSP. Client names one sponsor and one operational point of contact.                                                                                                                          |
| 5.5.6 | **Acceptance criteria**    | Fixed form, variable value          | "Such as key performance indicators" (ISO). This is the mechanism that ends the engagement instead of letting it drift into unpaid support (F-W8-06). Write it as a condition a third party could check. |
| 5.5.7 | Terms and conditions       | Fixed                               | Includes 5.5.7.2: ownership of material and deliverables, user rights, licensing, IP, liability limits. See §5 of this playbook for the IP position.                                                     |

### E1 work-plan checklist — FIXED, all 17 items (ISO §5.5.4 a–q)

Tick or strike each with a reason. Items (n) and (o) are the two solo consultants most often omit
and ISO places them at **contracting**, not closure (F-W8-19, Tier A).

- [ ] a. Objectives, scope, expected outcomes
- [ ] b. Approach and methodology
- [ ] c. Project governance including escalation
- [ ] d. Contents
- [ ] e. Documentation
- [ ] f. Data, information and technological resources ← **name every AI tool that will touch client material here**
- [ ] g. Project organization
- [ ] h. MCSP human resources
- [ ] i. Client/recipient human resources and roles
- [ ] j. Timetable and milestones
- [ ] k. Project budget
- [ ] l. Project management methods
- [ ] m. Communications
- [ ] n. **Client and/or recipient capacity building**
- [ ] o. **Knowledge transfer**
- [ ] p. Quality and risk methodology
- [ ] q. Deliverables

---

## 3. Phase E2 — Discovery

| Field                | Content                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | Signed agreement. Data instrument executed. `domain-rampup.md` phases D0–D2 complete (the written mechanism draft exists **before** the first practitioner conversation).                                                                                                                                                                                                                                                                         |
| **Activities**       | Interviews per the sampling rule below. Systems walk. Artefact collection (forms, spreadsheets, email threads, exports). One physical or screen-share walk-through of the process end to end.                                                                                                                                                                                                                                                     |
| **Artifacts**        | `interviews/<role>-<n>.md` (one per interview, transcript + coded themes), `systems-inventory.md`, `walkthrough-notes.md`, `contradictions.md` (cross-interview disagreements, auto-drafted, human-confirmed).                                                                                                                                                                                                                                    |
| **Time-box**         | **5–10 business days.** Interviews at 45–90 min each. Convention, not measured (W7 Gap 5).                                                                                                                                                                                                                                                                                                                                                        |
| **Human checkpoint** | **Every interview and the walk. Not delegable, at all.** AI can generate the protocol, code the transcript, and flag cross-interview contradictions — that last one is genuinely valuable. It cannot conduct the interview or walk the floor (W7 methodology table). Diagnosis engagements do not parallelise the way code worktrees do; the human-presence constraint binds harder here than review capacity does.                               |
| **Exit test**        | **Two conditions, both required.** (1) **Saturation per stratum**: no new code appears in the last 2 interviews within each role stratum. (2) **Contradiction closure**: every entry in `contradictions.md` is either resolved or explicitly logged as an open disagreement with both positions named. If either fails, extend by up to 3 days; if it still fails, the process is more heterogeneous than scoped — trigger the E1 change control. |

### Interview sampling rule — FIXED

| Population shape                                      | Target count                        | Basis                                                                                                                                                                                                                       |
| ----------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One homogeneous role, one narrow process              | **9–12**                            | Code saturation ~9; Guest et al. saturation within 12, metathemes by 6 (Tier A, F-W6-02 / F-W7-16)                                                                                                                          |
| Need mechanism, not just process steps                | **16–24**                           | Meaning saturation 16–24 (Tier A)                                                                                                                                                                                           |
| Cross-functional (owner + ops + finance + front line) | **9–12 _per stratum_, or a census** | Saturation is per-stratum; a multi-role business is a multi-site study, where the replicated figure is 20–40 (Hagaman & Wutich). **Do not transfer "12" to a cross-functional diagnosis** — the source does not support it. |
| Business has ≤17 people total                         | **Census the role, not a sample**   | The sampling question collapses. Interview everyone who touches the process.                                                                                                                                                |

**Commercial consequence, carried from W6:** a single-function engagement and a cross-functional
engagement are **different products at different prices**, not the same product at two sizes. Price
E2 by stratum count, not by headcount.

### Discovery deliverable template — FIXED

```markdown
# Discovery Record — <client> — <process>

## 1. Scope boundary

Suppliers / Inputs / Process (5–7 steps) / Outputs / Customers ← SIPOC, 1–2 h
Named real customer (validated in interview, not assumed):

## 2. Roles interviewed

| Stratum | Interviews | Saturation reached at | New codes in last 2 |

## 3. The process as described (per stratum)

| Step | Who | System | Stated rule | Observed exceptions |

## 4. Contradictions between accounts

| Topic | Account A (role) | Account B (role) | Resolved? | If not, why it matters |

## 5. Artefacts collected

| Artefact | Source | Retention/return obligation (ISO §7.5.3) |

## 6. What I could not learn, and why
```

---

## 4. Phase E3 — Process diagnosis

Full method in `process-diagnosis.md`. Engagement-level wrapper only here.

| Field                | Content                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | E2 exit test passed. `contradictions.md` closed or logged.                                                                                                                                                                                                                                                                                 |
| **Activities**       | Run the six gates in `process-diagnosis.md` §3 in order. Compute the touch-time ratio. Determine the event-log verdict. Identify the constraint. Enumerate the residue.                                                                                                                                                                    |
| **Artifacts**        | `diagnosis.md` containing the six-gate table with a pass/fail and evidence per gate; `touch-time.md` (the number, the method, the two timestamps); `constraint.md` (named constraint + how it was identified + what would falsify it).                                                                                                     |
| **Time-box**         | **5–10 business days.** Log present → the shorter end and AI-heavy. Log absent → the longer end and human-time dominated. These are two different cost structures (W7 Implications) and E1's budget should already reflect which one you sold.                                                                                             |
| **Human checkpoint** | Constraint identification. The constraint is usually social and undocumented — one person who approves everything, one licence, one relationship — and AI cannot see it (W7 methodology table).                                                                                                                                            |
| **Exit test**        | **Gate 2 (touch-time) has a number with both inputs sourced, and every one of the six gates has an explicit verdict with evidence.** A gate answered "probably" fails. If Gate 5 (event log) fails, the diagnosis proceeds on interviews — a **weaker but not invalid** basis, which must be stated in the deliverable rather than hidden. |

---

## 5. Phase E4 — Opportunity ranking

| Field                | Content                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | `diagnosis.md` complete with six gate verdicts.                                                                                                                                                                                                                                                                                |
| **Activities**       | Score every candidate change on the fixed rubric below. Separate **process/org changes** from **automation candidates** into two lists, explicitly. Kill anything that fails Gate 1 or Gate 2.                                                                                                                                 |
| **Artifacts**        | `opportunities.md` — the ranked table; `killed.md` — everything rejected with the gate it failed. Keep `killed.md`: it is the artefact that prevents the client re-proposing the same idea in month 4.                                                                                                                         |
| **Time-box**         | 2–3 business days.                                                                                                                                                                                                                                                                                                             |
| **Human checkpoint** | The kill decisions. An AI-generated ranking inherits the framing it was given (W7 methodology table) — the framing must be human-checked before the ranking is trusted.                                                                                                                                                        |
| **Exit test**        | Every candidate has a score on all six columns, a rank, and either a build estimate or a kill reason. **At least one item appears on the process/org list.** If the entire ranked list is automation, either the diagnosis was shallow or you are about to automate over dysfunction — re-run Gates 1 and 2 before proceeding. |

### Opportunity ranking rubric — FIXED

| Column                       | Scale                                        | Source                                                                                                |
| ---------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Is it the constraint?**    | Yes / No / Unknown                           | TOC — improvement at a non-constraint cannot raise throughput (definitional, F-W7-11)                 |
| **Touch-time ratio**         | Number (worked ÷ elapsed)                    | Low ratio ⇒ queueing/authority-bound ⇒ automation of the work step changes nothing perceivable        |
| **Variant count**            | Count of distinct paths + % on dominant path | Wewerka & Reichert Fig. 2 — high-variant work is human/BPM territory (Tier A, F-W7-06)                |
| **Exception rate**           | Count, per 100 cases                         | P57's operationalisation of stability. **No source gives a threshold — do not invent one** (W7 Gap 2) |
| **Digital + structured I/O** | Yes / Partial / No                           | Converged RPA selection criterion (Tier A, F-W7-06)                                                   |
| **Residue named?**           | Yes + trained / Yes + untrained / No         | Bainbridge — the residue is by construction the hardest part (Tier A, F-W7-14)                        |

**Ranking rule (fixed):** sort by `constraint = Yes` first, then by touch-time ratio descending,
then by exception rate ascending. Anything with `constraint = No` goes to `killed.md` regardless of
how attractive it looks.

**The threshold that does not exist.** No source anywhere gives a numeric answer to "standardised
enough to automate" (W7 Gap 2, W7 Q1). Any percentage a consultant quotes for this is invented.
Record the exception count, rank on it, and let the client decide with the number in front of them.

---

## 6. Phase E5 — Roadmap and decision gate

| Field                | Content                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | `opportunities.md` ranked and `killed.md` written.                                                                                                                                                                                                                   |
| **Activities**       | Package the top items into work packages with a fixed price each. Present. Obtain a decision. ISO §6.5.3's execution sequence is Prepare → Analyse options → Recommend → **Obtain decision** → Implement; the decision is a named step, not an assumption.           |
| **Artifacts**        | `roadmap.md` (work packages, sequence, dependency, fixed price each); `decision-record.md` (what was decided, by whom, on what date, and what was declined).                                                                                                         |
| **Time-box**         | 1 day to produce. Client's calendar to decide. **Set a decision expiry — 15 business days — after which prices are re-quoted.** Without it the Diagnostic drifts into unpaid support.                                                                                |
| **Human checkpoint** | The presentation, with the decision-maker from E0 gate 1 physically present. This is the checkpoint E0 gate 1 exists to guarantee.                                                                                                                                   |
| **Exit test**        | **A written decision exists naming the accepted packages and the declined ones.** "They're thinking about it" fails. The Diagnostic is complete and invoiceable at this point whether or not any build is bought — that is the point of separating the two products. |

### The pitch — FIXED framing, VARIABLE numbers

Use the operator's own client data, not industry statistics. Three defensible moves, in order:

1. **Lead with their touch-time ratio.** "Your cases take N days. Someone works on them for M
   minutes." It is the client's own number, it reframes the engagement from "build me a bot" to
   "your work is waiting, not running," and it requires no event log. This is the sharpest
   instrument in the whole diagnosis (W7 Implications).
2. **If they cite automation failure rates, correct them — carefully.** Every widely quoted figure
   is unusable in client-facing material: "30–50% of RPA projects fail" is one unsourced sentence
   in a 2016 EY marketing brochure whose observed population was explicitly selected on failure
   (Tier C, F-W7-01); "70% of change efforts fail" was self-labelled "our unscientific estimate"
   and **disowned by Hammer in 1995** (F-W7-02); "40% of agentic AI projects cancelled by 2027" is
   a Gartner **forecast** (F-W7-20); "95% of GenAI pilots fail" is 52 interviews with an undisclosed
   conflict of interest (F-W7-20). Citing any of these to a client who later traces the provenance
   is a credibility loss, not a persuasion win.
3. **Sell the evidenced version: arrested scaling, not project failure.** Deloitte's n=424 survey
   (2017 fieldwork, disclosed method — the only defensible numbers in the field, Tier B) found
   **≥85% of RPA projects met or exceeded expectations on accuracy, timeliness, flexibility and
   compliance**, with **11.5-month achieved payback** — and **only 3% of organisations reached 50+
   bots**, with **63% missing their time-to-implement expectations**. The costly failure is not a
   bot that does not work. It is a portfolio of bots that each work, each encode a different local
   variant of a process nobody standardised, and collectively cannot be extended. Date-stamp it as
   2017 fieldwork every time you use it.

---

## 7. Phase E6 — Build

| Field                | Content                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | Signed decision record naming this package. Package re-entered contracting (ISO §6.3 — execution does not start until there is an agreement). Acceptance criteria written as a runnable check.                                                                                                                                                                                                                               |
| **Activities**       | Per `harness-blueprint.md`, using the code variant or knowledge-repo variant of the operating system as appropriate. One package at a time.                                                                                                                                                                                                                                                                                  |
| **Artifacts**        | The built thing; its tests or verification harness; `handoff/<package>.md`; an updated `substantive-review-log.md` (see below).                                                                                                                                                                                                                                                                                              |
| **Time-box**         | Per package, fixed at contracting. **Softwareestimation is systematically optimistic and the operator has no bench to absorb an overrun** — a solo practice cannot reassign staff. Industry baseline for firms that do have a bench: project overrun **11.3%** in calendar 2024, up from 9.6%; on-time delivery **73.4%** (SPI n=403, Tier B, calendar-2024 data, superseded by the 2026 edition — re-check before quoting). |
| **Human checkpoint** | **Substantive review of every merged unit.** Defined as: the operator opened the diff, and a written note exists. This is the single governing throttle of the whole operating system — see `REPORT.md` §Adoption Sequence Stage 0.                                                                                                                                                                                          |
| **Exit test**        | The acceptance criterion from E1 §5.5.6 evaluates true, **and** substantive-review share for the package is ≥90% of merged units. A package that ships with a substantive-review share below 90% has not passed, regardless of whether the tests are green. Throughput that outran review is a defect, not a delivery.                                                                                                       |

### Change control — FIXED (ISO §6.5.4.6)

Five named trigger categories. Any one of them opens a change record; a change that falls outside
the change-control process **re-enters contracting** and may require renegotiating the agreement.

- [ ] Deviation from the work plan
- [ ] Changed context
- [ ] Change in the client's or recipient's operating environment
- [ ] Change in client expectations
- [ ] Change in the MCSP (you)

### Reuse instrumentation — do this from engagement 1

The 80/20 carryover ratio has no evidence base anywhere (W8 Gap 1). Measure your own. Log per
artefact, one line each:

| Artefact | Type (proposal / work plan / diagnostic instrument / report template / build artefact / handoff) | Reused unchanged | Reused adapted | Net new | Minutes spent |
| -------- | ------------------------------------------------------------------------------------------------ | ---------------- | -------------- | ------- | ------------- |

**Read it at engagement 4.** If reuse-unchanged is under 50% by minutes, the productization thesis
is failing and the fixed/variable split in §9 is wrong for your actual market — revise §9, do not
revise the measurement.

---

## 8. Phase E7 — Closure

| Field                | Content                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | Acceptance process, as defined in the agreement, is complete (ISO §7.1 defines completion by reference to acceptance, Tier A).                                                                                                                                                                                                              |
| **Activities**       | Run the six-topic closure checklist. Debrief the client (§7.5.4 requires it). Return client property. Execute the repo separation step in §10.                                                                                                                                                                                              |
| **Artifacts**        | `closure-<client>.md` — the six topics with a line each; `surviving-obligations.md` — explicitly enumerated; a sanitised methodology delta proposed for the generic repo (see §10, requires an explicit permission step).                                                                                                                   |
| **Time-box**         | ≤2 business days.                                                                                                                                                                                                                                                                                                                           |
| **Human checkpoint** | The debrief, and the de-identification review of anything proposed for promotion to the generic repo. That review is not delegable — see §10.                                                                                                                                                                                               |
| **Exit test**        | All six ISO §7.1 topics addressed **and** `surviving-obligations.md` enumerates every continuing obligation by name. **Caveat carried forward honestly:** no evidence exists that performing closure formally reduces post-engagement support drag (F-W8-03). This checklist is standards-backed, not outcome-validated. It is still cheap. |

### Closure checklist — FIXED (ISO §7.1, §7.5)

- [ ] Legal and contractual matters — invoicing, expense reconciliation, formal sign-off and acceptance, release of subcontractors, warranties
- [ ] Final evaluation and improvement
- [ ] Administrative matters including payment
- [ ] Communication — **client is debriefed at the end of the assignment** (§7.5.4)
- [ ] **Intellectual property rights** — ownership confirmed against §5.5.7.2 as agreed at contracting
- [ ] Outstanding minor issues
- [ ] **Return of client property** (§7.5.3) — "files, records, data, security passes"; add: revoke tool access, delete or return per §6 instruments
- [ ] **Surviving obligations enumerated** (§7.4) — guarantees, confidentiality, data protection, IP, non-competition, outstanding issues

---

## 9. What changes per client vs. what is fixed

This is the productization contract. **Anything in the FIXED column is used verbatim; editing it is
a defect in the playbook, not a customisation.**

### FIXED — carries over unchanged

| Asset                                                         | Where                      | Authority                                                                           |
| ------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------------------------- |
| The 8-item qualification checklist                            | §1                         | Constructed from ISO + W7 gates                                                     |
| The 6-section agreement skeleton (5 of 6 sections)            | §2                         | ISO 20700 §5.5 (Tier A)                                                             |
| The 17-item work-plan checklist                               | §2                         | ISO 20700 §5.5.4 a–q (Tier A) — **the single most reusable asset identified in W8** |
| The interview sampling rule                                   | §3                         | Saturation literature (Tier A)                                                      |
| The discovery deliverable template                            | §3                         | Constructed                                                                         |
| The six diagnostic gates                                      | `process-diagnosis.md`     | Constructed from TOC / Hammer / RPA SLR / Fluxicon / Bainbridge                     |
| The opportunity ranking rubric (6 columns + sort rule)        | §5                         | Constructed from Tier A criteria                                                    |
| The pitch framing (touch-time first, arrested-scaling second) | §6                         | Deloitte n=424 (Tier B), Hammer 1990 (Tier A for text)                              |
| The 5-trigger change-control list                             | §7                         | ISO §6.5.4.6 (Tier A)                                                               |
| The 8-item closure checklist                                  | §8                         | ISO §7.1, §7.5 (Tier A)                                                             |
| The data-instrument decision table                            | §10                        | GDPR Art. 28 / 45 CFR §164.504 / 26 CFR §301.7216-2 (Tier A)                        |
| The IP position and one-way flow rule                         | §10                        | ISO §4.4.8, IMC USA §5.0, residuals doctrine (Tier A/B)                             |
| The domain ramp-up procedure                                  | `domain-rampup.md`         | Rozenblit & Keil, GJP training study (Tier A)                                       |
| The harness configuration                                     | `harness-blueprint.md`     | Anthropic primary docs (Tier A)                                                     |
| The substantive-review-share throttle                         | §7, `harness-blueprint.md` | arXiv:2607.01904 (Tier A)                                                           |

### VARIABLE — rewritten every engagement

| Asset                             | Why it cannot be fixed                                                                                           |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Agreement §5.5.2 **Context**      | "An accurate description of the organization's current situation" — definitionally client-specific (F-W8-02)     |
| Acceptance criteria **values**    | The form is fixed; the number is theirs                                                                          |
| Interview **strata and counts**   | Set by the client's role structure; a cross-functional engagement is a different product (F-W6-02)               |
| The **touch-time numbers**        | Measured, not transferred. There is no published distribution of typical touch-time ratios (W7 Gap 10)           |
| The **constraint**                | Usually social and undocumented; different every time                                                            |
| The **build packages and prices** | Set by the ranked list                                                                                           |
| The **domain knowledge base**     | Per-client, per §10 never merged into the generic repo without an explicit de-identification and permission step |
| Which **data instrument** applies | Per §10 decision table                                                                                           |

### Pricing rule — FIXED structure, variable numbers

**No source found supports a specific price, rate, or margin target for a solo AI/operations
consultant** (W8 Implications). Every pricing figure in the consulting genre is C-tier — the one
survey with published numbers is undated, self-selected from the publisher's own coaching audience,
and has no methodology section (F-W8-15). Do not import one. What is defensible is the _structure_:

| Phase                     | Contract type                       | Why (FAR 16.104, Tier A)                                                                                                                                                                                                           |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E2–E5 Diagnostic          | **Bounded fixed fee**               | High requirement uncertainty, but a defined deliverable and a hard time-box. Not T&M: FAR 16.601 says T&M "provides no positive profit incentive for cost control" and requires a ceiling the contractor exceeds at its own risk.  |
| E6 Build, engagements 1–3 | **Fixed price + ceiling, generous** | Requirement is still novel; you are buying your own estimation data                                                                                                                                                                |
| E6 Build, engagement 4+   | **Fixed price, tightened**          | FAR's structural insight: **"as requirements recur, cost risk should shift to the contractor"** and risk decreases with repetitive acquisitions. This is the mechanism by which productization and pricing are the _same_ problem. |

---

## 10. Client-safe: data, IP, and the one-way flow rule

⚠ **Every item in this section has confidentiality, data-residency, regulated-data, or
third-party-access implications.**

### Data instrument decision table — FIXED (Tier A, binding regulation)

| If client material includes… | Instrument required **before** any tool touches it | Key clause                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EU/UK personal data          | **GDPR Art. 28 DPA**                               | Sub-processor requires prior written authorisation (28(2)); 8 mandated terms (28(3)(a)–(h)); **identical obligations flow down** to sub-processors and you remain fully liable (28(4)); deletion or return at end of service                                                                                                                                                                              |
| Protected health information | **HIPAA Business Associate Agreement**             | 45 CFR §164.504(e)(2): permitted uses; subcontractors bound to same restrictions ((e)(2)(ii)(D)); **return or destroy all PHI and retain no copies** at termination ((e)(2)(ii)(J)). Note the overlooked permission: (e)(2)(i)(A) expressly allows use "for the proper management and administration of the business associate" — a negotiable route to limited internal reuse most parties never ask for |
| US tax return information    | **§7216 written notice**                           | 26 CFR §301.7216-2(d)(2): disclosure to a contractor for auxiliary/technical services is permitted **only if** written notice explaining §§7216 and 6713 is given; the contractor thereby becomes a return preparer                                                                                                                                                                                       |

**The §7216 rule the corpus got wrong.** The corpus's claim that client tax data "must stay on
local Claude Code instances only" is **refuted on both premise and remedy** (C-150). §7216 does not
flatly prohibit disclosure to a service provider, and "local Claude Code" is not a compliance
state — Claude Code transmits content to a hosted API, which is itself a disclosure to a third
party. **The operative restrictions are geographic, not tool-branded:** (d)(1) requires the
recipient be located within the United States absent consent; (d)(3) bars disclosure of SSNs to a
preparer outside US territory without consent; (c)(2) restricts even intra-firm disclosure to
members located outside the US.

**Correct rule:** a US-located single provider under written §7216 notice is a permitted
configuration. A multi-provider router that may route to non-US inference endpoints is not, without
taxpayer consent. The corpus's operational conclusion about OpenRouter survives — for a different
reason than it gave.

**Vendor terms are necessary and nowhere near sufficient.** Anthropic's Commercial Terms (eff.
2025-06-17, checked 2026-08-01) state the customer retains rights to inputs, owns outputs, and that
Anthropic may not train on customer content from Services. That is a favourable clause. It does not
by itself satisfy any of the three regimes above — a BAA, a §7216 notice, and an Art. 28 DPA are
separate instruments with their own required contents. Re-verify the terms version, and which
product tier they apply to (commercial/API terms are not consumer-subscription terms), before every
regulated-data engagement.

**Process mining is a data-export event.** Any productised process-mining offer needs a
data-handling answer before it is sold, not after: event data for healthcare, legal, or financial
clients means PHI, privileged material, or regulated records leaving the client's system of record
and passing through your tooling and possibly a third-party model API. The SME process-mining
literature already records data-privacy concern and distrust of cross-departmental event data as
adoption barriers (F-W7-10).

### The one-way flow rule — FIXED

Two independent layers require hard structural separation between a **generic methodology repo**
and **per-client repos**, and they were established by two workstreams that could not see each
other's work:

- **Harness mechanics (W2).** Every mechanism that shares context across projects also shares it
  across clients: a shared `autoMemoryDirectory`, user-scope `~/.claude/CLAUDE.md`,
  `~/.claude/rules/*.md` (which "apply to every project on this machine"), symlinked rule
  directories, `@~/` imports, and `--add-dir` across client repos. Critically, **the harness's own
  safety gate does not cover the user-scope path**: an import in a project-level memory file
  resolving outside the working directory triggers a one-time approval dialog, but "imports in
  user-scope memory files… load without the dialog." And auto memory is **written by Claude, not by
  the operator**, so its contents are never reviewed before they are shared — which means auto
  memory cannot be the layer where the client-boundary decision is enforced (F-W2-14, Tier A).
- **Contract law (W8).** A residuals clause — the recognised contractual device for permitting
  knowledge reuse — is limited in every formulation found to information "retained in the **unaided
  memory**" of the recipient's people, and protective drafting explicitly excludes knowledge
  retained by reference to notes, documents, or recorded material. **A per-client knowledge
  repository is recorded material and falls entirely outside residuals protection** (F-W8-09,
  Tier B). Separately, IMC USA's enforceable Code §5.0 prohibits _use_ — not merely disclosure — of
  client proprietary information "for use by myself, the client's firm, or another client, without
  the client's permission" (Tier A), and ISO §4.4.7 bars using a client's data even as a credential
  when selling to the next one.

**The rule:**

| Direction                              | Permitted?                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| generic methodology repo → client repo | **Yes, freely.** ISO §4.4.8: "The MCSP normally retains the ownership for intellectual property rights that they bring to a project" (Tier A)                                                                                                                                                                                                                 |
| client repo → generic methodology repo | **Only via an explicit two-step gate:** (1) de-identification — no client name, no figures, no artefact excerpts, no combination that re-identifies; (2) permission, or a determination in writing that the item is generic professional method and contains nothing client-proprietary. The operator personally performs this review at E7 and nowhere else. |
| client repo A → client repo B          | **Never.** No exceptions, no de-identified route.                                                                                                                                                                                                                                                                                                             |

**Negotiating baseline, not protection.** ISO §4.4.8's "normally retains" is a description of
practice, routinely overridden by client-drafted MSAs demanding assignment of all work product.
Law-firm guidance describes the market resolution as _assignment of deliverables with a license-back
for general-purpose tools_ — weaker than ISO's default. Agree it at contracting (§5.5.7.2), not at
closure. **No case was found of a solo consultant sued for cross-client methodology reuse**, so the
risk is unquantified rather than proven low.

---

## 11. Portfolio control

**Two separate throttles, and the evidence only speaks to one.** Every documented personal
operating system that appears to cap at 2–3 is capping _today's execution WIP_, not the _engagement
portfolio_ (F-W9-12, Tier C for all of them — none is empirically validated). Do not conflate them.

| Throttle                  | Setting                                                          | Basis                                                                                                                                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Execution WIP**         | Governed by substantive-review share, not by a count             | The only Tier A evidence (arXiv:2607.01904) measures review degradation, not session count. **No measurement of a solo operator's concurrent-session ceiling exists at all** (W9 Gap 1, W2 F-W2-11)                                                                        |
| **Engagement portfolio**  | Start at **2 active + 1 in E0/E1**, and adjust from your own log | Convention. The multi-project literature gives an inverted-U shape with a sample mean of 2.71 projects but **no vertex** (F-W9-07, Tier A) — anyone quoting an "optimal N" from it is over-reading. Older PM literature converges on 2–3 and calls itself sparse (F-W9-08) |
| **Human-presence phases** | **Do not overlap E2 or E3 across two clients**                   | Diagnosis does not parallelise: the interview, the walk, and the decision-rights conversation are all serial and all non-delegable (W7 Implications). This binds harder than review capacity for the consulting half                                                       |

**Discount your own sense of capacity.** Every time self-report and instrumentation have been
compared in this literature, self-report was the optimistic one — METR's developers forecast 24%
faster, estimated 20% faster afterwards, and measured **19% slower** (Tier A, N=16, tooling
Feb–Jun 2025, explicitly historical). "I can handle four engagements" is exactly the judgment that
record says to distrust.

**Contaminated search space — do not cite.** Precise-looking solo-consultant capacity benchmarks
attributed to a "Kennedy Research 2024 Independent Consultant Survey" and an "SCIP 2024 Solo
Consultant Study" appear on multiple sites and **neither study is traceable anywhere outside those
pages** (F-W9-13). They are fabricated citations.

---

## 12. Engagement-level exit test

The engagement is complete when **all** of the following are true:

- [ ] Every phase's exit test above passed, in order, with no phase skipped
- [ ] The ISO §7.1 closure checklist is complete
- [ ] `surviving-obligations.md` enumerates every continuing obligation by name
- [ ] Client property returned; tool access revoked; §6-instrument deletion/return performed
- [ ] Reuse instrumentation logged for every artefact (§7)
- [ ] Substantive-review share recorded for every build package, and ≥90% for each
- [ ] The one-way flow gate (§10) has been run on anything proposed for the generic repo, by the operator personally
- [ ] Nothing from this client's repo has entered any other client's repo
