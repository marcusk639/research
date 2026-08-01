# Process Diagnosis Playbook

_Phase C deliverable 6 | 2026-08-01 | Evidence base: `findings/w7-process-diagnosis.md`, with supporting material from `findings/w6-domain-rampup.md`_

**What this is.** The pre-automation playbook: an eight-phase, time-boxed procedure that answers
"must this process be fixed before it is automated?" with a number, plus the ranked shortlist of
methodologies worth carrying from engagement to engagement.

**Scope — both project kinds.** The six gates in §3 are process-agnostic. They apply to a client's
back-office workflow, and they apply unchanged to the operator's _own_ internal pipelines —
including a code-free knowledge repository's document pipeline (where "cases" are documents,
"activity" is a status change, and the event log is git history, which trivially satisfies Gate 5).
Where a gate behaves differently for the knowledge-repo case, it is marked **[KR]**.

---

## 0. The three things you must say out loud before starting

**1. No single published, validated test exists for "must this be fixed before automating."**
Nobody has run the study. What exists is a set of individually-evidenced gates that can be assembled
into a rule. The assembly in §3 is a construction; the components are not. Each gate is tagged
`STATED` (found in a source) or `CONSTRUCTED` (assembled here from cited evidence).

**2. Every widely-quoted automation failure statistic is unusable.** The table in §7 gives the
provenance of each. Do not put any of them in a client deliverable.

**3. "Standardise before you automate" is near-universally repeated and, as far as can be
established, has never been tested.** Every source advocating it sells either diagnosis or
implementation; the strongest offering is an unattributed anecdote with no n and no comparison group
(F-W7-19, Tier C — _and that is the best tier available_). The maxim is also **unfalsifiable as
usually stated**, because "standardised enough" is never operationalised. **No source anywhere
gives a threshold** — no "automate if ≥X% of cases follow the happy path." That number does not
exist. Do not invent one. Record the exception count, rank on it, and let the client decide with the
number in front of them.

---

## 1. The diagnosis at a glance

| Phase                            | Time-box (log present / log absent) | AI role                            | Non-delegable                                  |
| -------------------------------- | ----------------------------------- | ---------------------------------- | ---------------------------------------------- |
| **P0 — Frame**                   | 1–2 h                               | Draft                              | Choosing the process boundary                  |
| **P1 — Boundary (SIPOC)**        | 1–2 h                               | High — structured summary          | Validating the named customer is the real one  |
| **P2 — Instrumentation verdict** | 0.5–2 h                             | Medium — schema inspection         | Deciding whether a log can be manufactured     |
| **P3 — Touch-time**              | 0.5–1 day                           | Low                                | **The walk-through**                           |
| **P4 — Constraint**              | 1–3 days / weeks                    | Low                                | **Observing where work actually waits**        |
| **P5 — Six-gate test**           | 0.5 day                             | Medium — computation               | Every verdict                                  |
| **P6 — Residue & role design**   | 0.5–1 day                           | Medium — design against constructs | **Any conversation about who owns what after** |
| **P7 — Recommendation**          | 1 day                               | High — drafting                    | The kill decisions                             |

**Every duration is convention, not measured data.** No study measures how long any of these takes
at SMB scale (W7 Gap 5). The one exception is the five-day kaizen-event box, a stated Lean
Enterprise Institute convention (Tier B for the convention, not for its optimality). Recalibrate
against your own tracked hours.

**The fork that sets the price.** Gate 5's verdict determines which of two products you are
delivering:

| Event log present                                                                                      | Event log absent                                     |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Process mining is fast, AI-heavy, largely delegable                                                    | Engagement is interview-driven, human-time dominated |
| Cost set by tooling                                                                                    | Cost set by **the operator's calendar**              |
| 1–2 days to a discovered model                                                                         | Weeks to indefinite if the log must be manufactured  |
| **These are two different products with two different cost structures and should not be sold as one.** |                                                      |

---

## 2. Phases

### P0 — Frame

| Field                | Content                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | Signed agreement (`engagement-playbook.md` E1). A named process and a named number exist. Domain ramp D0–D2 complete.                               |
| **Activities**       | State the process boundary. State the client's claimed problem _and_ the problem you suspect, separately. State what would falsify your suspicion.  |
| **Artifacts**        | `diagnosis/frame.md` — claimed problem, suspected problem, falsifier, boundary.                                                                     |
| **Time-box**         | 1–2 hours.                                                                                                                                          |
| **Human checkpoint** | Choosing the boundary. An AI-generated issue tree inherits the framing it was given — the framing must be human-checked before the tree is trusted. |
| **Exit test**        | The falsifier is written and is checkable against something the client already has. "We'd know if it didn't work" fails.                            |

### P1 — Boundary (SIPOC)

| Field                | Content                                                                                                                                                                                                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | `frame.md` exists.                                                                                                                                                                                                                                                                                                               |
| **Activities**       | Suppliers → Inputs → Process (5–7 steps, no more) → Outputs → Customers, on one page.                                                                                                                                                                                                                                            |
| **Artifacts**        | `diagnosis/sipoc.md`.                                                                                                                                                                                                                                                                                                            |
| **Time-box**         | 1–2 hours.                                                                                                                                                                                                                                                                                                                       |
| **Human checkpoint** | **Validating that the named customer is the real customer.** This is the single judgment SIPOC exists to force and the one an AI draft will get wrong by inheriting the client's own org chart.                                                                                                                                  |
| **Exit test**        | Someone who does the work confirms the 5–7 steps without correction, and names the customer the same way you wrote it. **Honest caveat: no reliable evidence found that producing a SIPOC changes any downstream outcome** (F-W7-21). Keep it because it is a cheap one-page coordination artefact, not because it is evidenced. |

### P2 — Instrumentation verdict (Gate 5, run early)

| Field                | Content                                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | `sipoc.md` names the systems.                                                                                                                                                                                            |
| **Activities**       | Check the four Fluxicon data-suitability criteria against the client's actual system of record. Then check the four disqualifying conditions.                                                                            |
| **Artifacts**        | `diagnosis/event-log-verdict.md` — PRESENT / MANUFACTURABLE / ABSENT, with the four criteria evidenced.                                                                                                                  |
| **Time-box**         | 0.5–2 hours. It is a schema inspection, not a project.                                                                                                                                                                   |
| **Human checkpoint** | Deciding whether a log can be manufactured (screen/UI recording, EDF-style interactive generation), and pricing that. **Manufacturing converts a hard gate into a cost, and the cost lands before any analysis begins.** |
| **Exit test**        | A single verdict word plus evidence for each of the four criteria. If ABSENT, the diagnosis proceeds on interviews — **a weaker but not invalid basis, which must be stated in the deliverable rather than hidden.**     |

**Fluxicon data-suitability criteria — FIXED (Tier A, definitional and matched by the academic literature):**

| Required                                                                                     | Disqualifying                                                                           |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 1. Structured tabular data (Excel/CSV/DB)                                                    | Case IDs where every identifier "appears just exactly once"                             |
| 2. A **case ID** column where the same ID appears in multiple rows                           | An activity field that "never changes over the course of a case"                        |
| 3. An **activity name** column whose value **changes over time** for a given case            | Timestamps that don't change over time for the same case                                |
| 4. A **timestamp** with differing values across a case (or rows already in occurrence order) | Over-aggregated data with one event per case, showing only end result or current status |

Also: ERP and database systems organised around **business objects rather than processes** require
custom correlation work first — that is extraction cost, not a log.

**[KR] Knowledge-repo variant.** For the operator's own documentation pipelines the log is git:
case ID = file path, activity = commit type, timestamp = commit date. Gate 5 passes trivially. The
gate that binds instead is Gate 3 (exception rate), because prose work has no dominant path.

**SMB reality.** The SME process-mining literature names a "constraining data access barrier"
negatively affecting event-log availability, incomplete de jure processes, data-privacy concerns,
and the need for management to "shift manpower or hire experts" (Tier B). The existence of a
purpose-built SME event-log _generation_ tool is itself evidence that SMEs generally lack usable
logs. **No base rate exists for what fraction of SMBs have a minable log** (W7 Gap 3), and the
barrier is a function of **stack fragmentation, not headcount** — an SMB on a single modern SaaS
system of record that stamps status transitions can have a perfectly usable log with no extraction
work. No study separates those two variables.

### P3 — Touch-time (Gate 2, the sharpest instrument)

| Field                | Content                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | `sipoc.md` complete. A cooperative person who does the work is available for one walk-through.                                                                                                                                 |
| **Activities**       | Walk one real case end to end with a stopwatch. Record hands-on work time per step. Separately obtain elapsed time from any timestamped record (email dates, invoice dates, ticket dates — anything). Divide.                  |
| **Artifacts**        | `diagnosis/touch-time.md` — the ratio, both inputs, the method, and the sample size (usually n=1 to 3 cases — say so).                                                                                                         |
| **Time-box**         | 0.5–1 day.                                                                                                                                                                                                                     |
| **Human checkpoint** | **The walk itself.** AI can compute the ratio and draft the map from a transcript. It cannot walk the floor.                                                                                                                   |
| **Exit test**        | A single number with both inputs sourced and dated, and a stated sample size. "About 10%" fails. **This gate requires no event log**, which is why it runs before P4 and why it is the one gate to run if only one can be run. |

**Why this is the sharpest test.** It requires no event log, no tooling, and no methodology
training — a stopwatch and one walk-through gives touch time; any timestamped record gives elapsed
time. It **discriminates directly between the two failure modes**: a high ratio means work is
genuinely slow and automation may help; a low ratio means the delay lives in queues, handoffs, and
approvals, and automating the work steps will change nothing the client can perceive. And it is
falsifiable in a way "is the process broken?" is not.

**The canonical instance, cited honestly.** Hammer 1990 reports an insurer whose applications spent
**22 days in process while being worked on for 17 minutes** — roughly 0.05%. Automating execution
speed cannot move a 0.05% denominator. **Provenance caveat, carried forward:** that is one insurer,
reported second-hand, in 1990, with **no distribution behind it**. No study establishes typical
touch-time ratios for administrative processes, so **there is no evidenced threshold for what counts
as an alarming ratio** (W7 Gap 10). Use the number as the client's own diagnostic, not as a
benchmark comparison.

**Commercial note.** This is the most commercially valuable instrument in the playbook. It costs one
walk-through, produces a single number, and reframes an engagement from "build me a bot" to "your
work is waiting, not running" — using the client's own data.

### P4 — Constraint

| Field                | Content                                                                                                                                                                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | `touch-time.md` exists. Event-log verdict known.                                                                                                                                                                                                                       |
| **Activities**       | Locate where work accumulates. If a log exists: compute queue lengths and waiting times per step. If not: observe, and ask "what were you waiting for?" at every handoff in the walk.                                                                                  |
| **Artifacts**        | `diagnosis/constraint.md` — the named constraint, how it was identified, and **what observation would falsify it**.                                                                                                                                                    |
| **Time-box**         | 1–3 days if flow data exists; weeks if not.                                                                                                                                                                                                                            |
| **Human checkpoint** | **Observing where work actually waits.** AI can compute where queues accumulate _given_ data. It cannot see the informal constraint — one person who approves everything, one licence, one relationship — and the constraint is usually social and undocumented.       |
| **Exit test**        | The constraint is named as a specific person, queue, system, or approval — not a department or a capability. "Finance is slow" fails. "Every credit memo over $5k waits for one controller who reviews them Thursday afternoons" passes. And the falsifier is written. |

**Why TOC's logic and not TOC's numbers.** Theory of Constraints has the largest reported effect
sizes of any methodology in this set — inventory −49%, lead/cycle time improved >60%, throughput
+44% — from a meta-analysis of 80+ applications that **simultaneously reports finding zero
failures despite extensive searches** (Tier B, 2003 review of 1990s cases). **The zero-failure
finding disqualifies the effect sizes as estimates; they are upper bounds.** What survives is the
core structural claim, which is not an empirical claim at all: _a non-constraint's improvement
cannot raise system throughput_ follows from the definition of a constraint and is reproducible in
any queueing model. Goldratt's formulation: "an hour saved at a non-bottleneck is a mirage."

**Honest reading: TOC's logic is the most defensible thing in this workstream; TOC's numbers are the
least defensible.**

### P5 — The six-gate automation test

| Field                | Content                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | P2, P3, P4 complete.                                                                                                                                                                                |
| **Activities**       | Run §3's six gates **in order**. Any gate that fails means the answer to "automate now?" is no.                                                                                                     |
| **Artifacts**        | `diagnosis/gates.md` — the six-gate table with verdict + evidence + tag per gate.                                                                                                                   |
| **Time-box**         | 0.5 day (the inputs already exist).                                                                                                                                                                 |
| **Human checkpoint** | Every verdict.                                                                                                                                                                                      |
| **Exit test**        | Six explicit verdicts with evidence. A gate answered "probably" fails. If Gate 3 or 4 fails, the recommendation is a **process/org change**, not an automation — and P7 must say so in those words. |

### P6 — Residue and role design

| Field                | Content                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry criteria**   | Gates 1–5 have verdicts.                                                                                                                                                                                                                               |
| **Activities**       | For each proposed automation, enumerate what is left for the human afterwards. Check whether anyone is trained for it and whether they will still practise it. Design the role against the work-design constructs, not against the leftover task list. |
| **Artifacts**        | `diagnosis/residue.md` — per automation: what remains, who does it, how often they will practise it, what training changes.                                                                                                                            |
| **Time-box**         | 0.5–1 day to design; months to embed (not your time-box).                                                                                                                                                                                              |
| **Human checkpoint** | **Any conversation about who owns what after automation removes the routine work.** AI can design against known constructs; it has no purchase on the political reality.                                                                               |
| **Exit test**        | Every proposed automation has a named residue owner and a stated answer to "how will they stay good at this?" An automation whose residue has no owner does not proceed to P7's recommendation list.                                                   |

**Why this phase exists, and why it is the most-skipped.** Bainbridge's _Ironies of Automation_
(1983, 4,700+ citations, Tier A conceptually): "By taking away the easy parts of the task,
automation can make the difficult parts of the human operator's task more difficult." The designer
who tries to eliminate the operator still leaves the operator **the tasks the designer could not
automate — by definition the hardest ones.** Consequence: operators no longer practise those skills
as routine work, so they need **more** training for rarer, more critical interventions, not less.

**Transfer caveat.** The original context is safety-critical continuous-process control with rare,
high-stakes interventions. Transfer to a five-person back office processing invoices is an
inference. **The mechanism (residue is the hard part) transfers cleanly; the severity may not.**
Bainbridge gives no effect sizes, and no study quantifies skill decay in a business-process setting.

**Why role design specifically.** Job and role design is **the only methodology in this set with a
large-sample meta-analytic evidence base, and it is strong**: 259 studies, 219,625 participants; 14
work characteristics explained on average **43% of variance** across 19 worker attitudes and
behaviours (Tier A). Standard caveat: the corpus is dominated by cross-sectional self-report
designs, which inflate common-method variance — the association is solid, causal direction is
medium-confidence. **It is also the methodology least likely to be in a technical consultant's
default kit.** "What is this person's job after the bot ships" is simultaneously the best-evidenced
and most commonly skipped part of an automation engagement.

### P7 — Recommendation

| Field                | Content                                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry criteria**   | P5 and P6 complete.                                                                                                                                                                                                                                                                                                                                              |
| **Activities**       | Produce two explicitly separated lists: process/org changes, and automation candidates. Feed both into `engagement-playbook.md` §5 ranking.                                                                                                                                                                                                                      |
| **Artifacts**        | `diagnosis.md` (the consolidated deliverable), `opportunities.md`, `killed.md`.                                                                                                                                                                                                                                                                                  |
| **Time-box**         | 1 day.                                                                                                                                                                                                                                                                                                                                                           |
| **Human checkpoint** | The kill decisions.                                                                                                                                                                                                                                                                                                                                              |
| **Exit test**        | **At least one item on the process/org list.** A recommendation set that is entirely automation means either the diagnosis was shallow or you are about to automate over dysfunction. Re-run Gates 1 and 2 before proceeding. Also: every claim in `diagnosis.md` cites a gate, a client artefact, or a dated source — none cites an industry failure statistic. |

---

## 3. The six gates — FIXED

Run in order. **Any gate that fails means the answer to "automate now?" is no.**

| #   | Gate                                 | Test                                                                                                              | Tag                                    | Evidence                                                                                                                                                                                                                     |
| --- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Constraint**                       | Is the step you propose to automate the system constraint?                                                        | **CONSTRUCTED**                        | Throughput cannot rise by improving a non-constraint — definitional, reproducible in any queueing model. Effect sizes are upper bounds from a zero-failure literature (Tier B)                                               |
| 2   | **Touch-time ratio**                 | Hands-on work time ÷ elapsed time. If tiny, the process is queueing- and authority-bound, not execution-bound.    | **CONSTRUCTED**; the _datum_ is stated | Hammer 1990: 22 days elapsed, 17 minutes worked (≈0.05%). n=1, second-hand, 1990, **no distribution behind it** (W7 Gap 10)                                                                                                  |
| 3   | **Exception rate / standardisation** | What fraction of volume follows the dominant path, and can you state the rule that covers it?                     | **STATED**                             | RPA literature converges (8 primary papers): process must be "standardised, run in a stable environment, and only require limited exception handling." P57 operationalises stability as **exception count** (Tier A via SLR) |
| 4   | **Variant count**                    | Plot process variants against case frequency. High-variant work is human/BPM territory, not automation territory. | **STATED**                             | Wewerka & Reichert Fig. 2 — high-variant work "can only be performed by humans" (Tier A)                                                                                                                                     |
| 5   | **Measurability**                    | Does an event log exist — recurring case ID, activity that changes, timestamp that varies?                        | **STATED**                             | Fluxicon data-suitability criteria (Tier A, definitional). Failure ⇒ gates 1–4 answered from interviews: weaker but not invalid                                                                                              |
| 6   | **Residue**                          | After automation, what is left for the human, and is anyone trained for it?                                       | **CONSTRUCTED**                        | Bainbridge — the residue is by construction the hardest part, and routine practice at it disappears (Tier A conceptually)                                                                                                    |

**If only one gate can be run: Gate 2.**

**Not an evidence-based test, despite being universally recommended:** "is the process
standardised?" asked _qualitatively_. It is unfalsifiable until you replace it with a number, and
the only numeric version in the literature is P57's exception count. **No source gives a threshold.**
EY's 70/30 heuristic is the closest thing and it is a target for _how much_ of a process to
automate, not a gate for _whether_ to.

**Also converged, from the same SLR, as supporting criteria (not gates):** repetitiveness / high
transaction volume (the most-mentioned criterion, 11 primary publications); low complexity ("all
publications agree that the lower the complexity, the better"); high manual effort; digital and
structured inputs and outputs; limited human intervention. **Confidence caveat:** the SLR
**explicitly declined to apply quality-assessment criteria** ("applying rigid quality assessment
questions would probably exclude relevant publications"), so this consensus may be a citation
cascade rather than independent findings. The SLR also records internal disagreement — one paper
says unpredictable volume peaks _suit_ RPA, another says volumes should be predictable, and one
states the maximalist opposite of any selectivity gate: "any activity that a person performs with
mouse and keyboard can be carried out by a software robot."

---

## 4. The unresolved dispute you must not pretend to resolve

**X-W7-A — "fix the process first" vs. "automate the happy path and optimise later."** Both
positions are held by credentialed sources with real delivery experience. **Neither side has a
controlled study.** What separates them is not evidence quality but _dependent variable_:

| Position                    | Argues about                | Best support                                                                                                                                                                                                                                                                                                                    | Fatal weakness                                                                                                                                                                                                                        |
| --------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fix first**               | End-to-end process outcomes | Two published methods make maturity/standardisation a hard Step 1 gate before automation potential is even assessed; a third argues explicitly against automating the as-is process (Tier B, proposed not validated). Deloitte's survey names process standardisation as the **top challenge at PoC and pilot stages** (Tier B) | The maxim has never been tested (F-W7-19). The Deloitte item is a _reported-difficulty_ question, not an outcome measurement — reported difficulty and causal contribution are different quantities. Fix-first sources sell diagnosis |
| **Automate the happy path** | Time to first delivered bot | EY 2016: "Automating 70% of a process that is the lowest-value, and leaving the high-value 30% to humans is a good initial target. It's always possible to back and optimize the process later." Non-invasiveness is a _defining_ RPA property in the literature (Tier B)                                                       | Advocated by a firm selling RPA delivery, and it is **precisely the behaviour that produces the arrested-scaling pattern**. The same literature records RPA characterised as a **workaround** and a **temporary solution**            |

**The resolution this playbook adopts — narrower and more useful than either.** State it this way
to clients, because it is arguable from first principles, survives the publication-bias problem, and
is falsifiable on the client's own numbers:

> **Automation of a step that is not the constraint, or whose elapsed time is dominated by queueing,
> cannot produce a benefit the client will perceive — regardless of how well the automation works.**

This is Gates 1 and 2, and it is the position that does not require the untested maxim. It is
_compatible with_ automate-first: where Gates 1 and 2 pass and Gates 3–4 are marginal, a bounded
happy-path automation with a named residue owner is a defensible call. **The two findings are
consistent with each other: automate-first works, and then stops working.** What is not defensible
is automating a non-constraint or a queueing-bound step, in either camp's framing.

**Flip condition.** If a controlled or quasi-experimental comparison of standardise-then-automate
against automate-as-is is ever published — matched-pair or stepped-wedge, measuring **24-month total
cost of ownership and rework rate rather than go-live date** — adopt its finding and retire this
construction.

---

## 5. Ranked methodology shortlist — carry these engagement to engagement

Ranked by **evidence strength × transferability to a solo operator at SMB scale**, not by how well
known they are.

| Rank | Method                                 | Evidence on the method itself                                                                                                                                                                                                                                | Carry it?                                                              | AI unaided                                                                                | Human must be present for                                                                                                   |
| ---- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Touch-time ratio**                   | Datum is n=1/1990; the _logic_ is arithmetic and falsifiable on client data                                                                                                                                                                                  | **Always**                                                             | Low — computes the ratio, cannot walk                                                     | The walk-through                                                                                                            |
| 2    | **Job / role design**                  | **259 studies, 219,625 participants; 14 characteristics explain ~43% of variance across 19 outcomes (Tier A)** — the strongest evidence base in the whole workstream                                                                                         | **Always**                                                             | Medium — design against known constructs; **none** for the political reality              | Any conversation about who owns what after the bot ships                                                                    |
| 3    | **Theory of Constraints (logic only)** | Logic definitional (Tier A); reported effect sizes are upper bounds from a zero-failure literature (Tier B) — **carry the logic, never the numbers**                                                                                                         | **Always**                                                             | Low — computes queues given data; blind to the informal constraint                        | Observing where work actually waits                                                                                         |
| 4    | **Discovery interviews**               | Saturation quantified (Tier A); structured interviews rated among the most effective elicitation techniques (Tier A). **Saturation assumes homogeneity; SMB roles are stratified**                                                                           | **Always**                                                             | Low for the interview; **genuinely valuable for cross-interview contradiction detection** | The interview                                                                                                               |
| 5    | **Value stream mapping**               | PRISMA-conformant systematic review positive on time dimensions, but **every included study was uncontrolled before/after** (Tier B on C primaries). Effect sizes range 5.3% to 43% lead-time reduction with no moderator analysis                           | **When Gate 5 fails** and you need a shared picture of where time goes | Medium-low — drafts the map from a transcript, computes ratios, cannot walk               | The walk. **The map's value is that people who do the work agree on it in one room** — a consensus artefact, not a document |
| 6    | **Process mining**                     | Requirement definitional (Tier A); SME data-access barrier documented (Tier B). **The log is a hard gate most SMBs fail**                                                                                                                                    | **When Gate 5 passes**                                                 | High, conditional on a log. Zero without one                                              | Interpreting whether a discovered variant is a defect or a legitimate case type                                             |
| 7    | **BPMN modelling**                     | Benchmarked: 17 open-source LLMs, 105 text→BPMN pairs, 8,925 generations; strong syntactically and pragmatically (~0.8), **notably weaker on semantic quality, where humans still outperform**; only 11 of 17 models produced enough valid output to analyse | **Only when a formal model is a contracted deliverable**               | High for _transcription_. **Not for elicitation**                                         | Nowhere, once the description exists — the prerequisite description is the human part                                       |
| 8    | **SIPOC**                              | **No reliable evidence found** (F-W7-21)                                                                                                                                                                                                                     | Yes — 1–2 h, cheap coordination artefact                               | High as a draft                                                                           | Validating the named customer is the real customer                                                                          |
| 9    | **RACI / decision-rights mapping**     | **No reliable evidence found** for RACI specifically; Bain's decision-rights survey data is paywalled and could not be verified, so it is excluded rather than reported                                                                                      | Yes, when Gate 1's constraint is an approval                           | Medium — builds the matrix, flags conflicts; **cannot get people to concede authority**   | **The conversation where someone loses a decision right. This is the part that fails, and it fails in person**              |
| 10   | **Issue trees / MECE**                 | **No reliable evidence found**                                                                                                                                                                                                                               | Optional                                                               | High — near-pure structured generation                                                    | Nowhere; but the framing must be human-checked, since the tree inherits it                                                  |
| 11   | **DMAIC / Lean Six Sigma**             | Many systematic reviews, mostly healthcare, mostly uncontrolled; reviews repeatedly note "a lack of empirical evidence" (Tier B/C)                                                                                                                           | **No** — disproportionate ceremony below ~20 staff                     | Medium on Measure/Analyse if data exists; low on Define and Control                       | Define (framing what counts as a defect) and Control (whether the standard survives contact)                                |
| 12   | **Full reengineering (Hammer)**        | Hammer's own article concedes the enabling condition that kills portability: "executive leadership with real vision," and "Reengineering cannot be planned meticulously and accomplished in small and cautious steps. It's an all-or-nothing proposition."   | **No** — not a method a solo consultant can time-box                   | —                                                                                         | —                                                                                                                           |

**Absence of evidence is genuinely uninformative for ranks 8–10.** These are cheap communication
artefacts whose value is coordination, and coordination artefacts are rarely studied. Low evidence
is not low value here; it is low measurement. Do not, however, claim they are evidence-based.

**Cross-cutting capability finding, six years stale and worth re-measuring.** As of the last
measurement found (2020, 14 commercial RPA tools × 48 functionalities), automation tooling covered
the **operation phase at >80% and the analysis phase at <15%** — the diagnosis step is the _least_
tool-supported part of the pipeline. That figure predates the push of process-mining vendors and LLM
tooling into the analysis phase, so it should be re-measured rather than relied upon (F-W7-08).

---

## 6. Where AI earns its place in diagnosis, and where it does not

| AI genuinely helps                                                                                      | AI does not help                                                       |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Transcript coding                                                                                       | The walk                                                               |
| **Cross-interview contradiction detection** — the single most valuable AI contribution in this playbook | The interview                                                          |
| BPMN transcription from an _agreed_ description                                                         | **Process elicitation** — no benchmark exists for it at all (W7 Gap 7) |
| Issue-tree generation (framing must be human-checked)                                                   | Any conversation in which someone gives up a decision right            |
| Computing ratios and queue statistics from a log                                                        | Seeing the informal constraint                                         |

**The binding constraint here is different from the code half.** Review capacity bites less in
diagnosis because the volume of artefacts is small. **The human-presence constraint bites much
harder, and it does not parallelise at all.** Diagnosis engagements cannot be run three-at-a-time
the way worktrees can — which is why `engagement-playbook.md` §11 forbids overlapping E2/E3 across
two clients.

**Benchmark caveat that matters.** The one rigorous process-modelling benchmark tested
**open-source models only**, topping out at 405B open weights, through April 2025. **No frontier
proprietary model has been benchmarked on process modelling** (W7 Gap 6) — and the operator will be
running a frontier model, on which that benchmark is silent. The protocol is published and cheap to
re-run; that is the cheapest experiment in this workstream.

---

## 7. Failure statistics — provenance table, for your protection

**Do not put any Tier C row in a client deliverable.** Citing "30–50% of RPA projects fail" to a
client who later traces it to a 2016 EY brochure is a credibility loss, not a persuasion win.

| Circulated figure                                                                                                                                                              | Actual provenance                                                                                                                                                                                                                                                                       | Tier  | Verdict                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------- |
| "30–50% of initial RPA projects fail"                                                                                                                                          | One sentence, 2016 EY marketing brochure. No n, no method, no definition of failure. **Population explicitly selected on failure** — "often called upon to help companies when their first attempt failed." Author sells RPA remediation. Ten downstream citations all trace back to it | **C** | Not a rate. An anchored guess                                                          |
| "70% of change/reengineering fails"                                                                                                                                            | Hammer & Champy 1993, self-labelled **"our unscientific estimate"** of 50–70%. **Hammer disowned it in 1995**: "There is no inherent success or failure rate for reengineering." Hughes (2011, peer-reviewed) found no empirical basis in any of the five most-cited sources            | **C** | **Disowned by its own author. Do not use**                                             |
| "40% of agentic AI projects cancelled by end 2027"                                                                                                                             | Gartner press release 2025-06-25. A **forecast**, routinely re-reported as measurement                                                                                                                                                                                                  | **C** | Not a measurement. Re-check after end-2027                                             |
| "95% of GenAI pilots fail"                                                                                                                                                     | MIT NANDA 2025: 52 executive interviews, 153 survey responses, 300 public deployments. Methodology contested; **undisclosed conflict — the recommended remedy is the project's own offering**                                                                                           | **C** | Contested. Do not cite as fact                                                         |
| **3% scaled to 50+ bots; 63% missed time expectations; 37% missed cost expectations; payback 11.5 mo actual vs 9.3 expected; ≥85% met or exceeded non-financial expectations** | Deloitte, online survey Sept 2017, **n=424**, disclosed method, disclosed question wording, per-chart sample sizes, and several figures cutting against the publisher's own commercial interest                                                                                         | **B** | **The only defensible numbers in this table.** Date-stamp as 2017 fieldwork every time |
| "20% (automate as-is) vs 75% (redesign) headcount reduction"                                                                                                                   | Hammer 1990, Ford accounts payable. n=1, consultant-reported, and **the 20% is a projection never executed**, not a measured control arm                                                                                                                                                | **C** | The only quantified head-to-head that exists, and it is one case from 36 years ago     |

**Three things that can be said with confidence:**

1. **The academic denominator does not exist.** Two independent systematic reviews, in two different
   methodological traditions, report the same absence: the RPA literature "covers only successful
   RPA projects," and across 80+ TOC applications "no reports of failures were found." **You cannot
   compute a failure rate from a literature that systematically excluded failures — and this is true
   of both the automation literature and the process-improvement literature, so neither side of the
   fix-first debate can appeal to outcome data.**
2. **The observed failure mode is arrested scaling, not project failure.** Deloitte's n=424 shows
   projects succeeding individually while almost never propagating. The costly failure is not a bot
   that doesn't work; it is a portfolio of bots that each work, each encode a different local variant
   of a process nobody standardised, and collectively cannot be extended or maintained. **That is
   compatible with every project in the portfolio having passed its own business case.**
3. **No quantification exists anywhere of the cost of automating a broken process specifically.** The
   only quantified cost figure found (EY's "four-or five-fold" duration increase, 2–4 weeks → 10–15
   weeks) is about _delivery-method error_ — wrong methodology, under-skilled staff, over-automating
   — and none of its three issues is "the underlying process was broken."

---

## 8. ⚠ Client-safe flag

**Process mining is a data-export event.** It requires exporting operational event data — which for
healthcare, legal, or financial clients means PHI, privileged material, or regulated financial
records leaving their system of record and passing through your tooling and possibly a third-party
model API. The SME process-mining literature already records data-privacy concerns and distrust of
cross-departmental event data as adoption barriers. **Any productised process-mining offer needs a
data-handling answer before it is sold, not after** — see `engagement-playbook.md` §10 for the
instrument decision table.

---

## 9. Diagnosis exit test

- [ ] All eight phases' exit tests passed in order
- [ ] Gate 2 has a number with both inputs sourced, dated, and a stated sample size
- [ ] All six gates have explicit verdicts with evidence; none says "probably"
- [ ] If Gate 5 failed, the interview-based basis is stated in the deliverable, not hidden
- [ ] The constraint is named as a specific person/queue/system/approval, with a falsifier
- [ ] Every proposed automation has a named residue owner and a practice answer
- [ ] At least one item is on the process/org list
- [ ] No Tier C failure statistic appears anywhere in the client-facing deliverable
- [ ] No invented "standardised enough" threshold appears anywhere
