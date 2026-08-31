# Deep Research Prompt — Ketamine for Post-Traumatic Anxiety and Panic: Subcutaneous Dosing and the Dissociation Question

> **How to run:** invoke the `deep-research` skill and pass everything below the `===` line.
> **Output target:** `psychedelic-therapy/ketamine-posttraumatic-anxiety-sc.md` (new file).
> **Do not ingest this file or the output file as source material.**

**Relationship to the other prompts in this directory:**

- `ketamine-crisis-context-deep-research.md` (v2) is the **broad** landscape version — all crisis
  states, all routes, all populations, suicidality included. Still valid; not superseded.
- This file is the **narrow** version, re-scoped to one clinical picture. It answers a smaller
  question in more depth.
- `ketamine-chat-app-research.md` is the chat-app port of v2.

**Scope decisions baked in** (change here if wrong):

1. **Suicidality is excluded as an efficacy target and as a study population.** See the
   `<exclusions>` block for the one carve-out: it remains in scope as a _safety_ signal, because
   treatment-emergent suicidal ideation is a monitorable harm and appears in the SPRAVATO boxed
   warning. Excluding it from harm surveillance would make the report less safe, not narrower.
2. **Bipolar I is excluded as a target population; bipolar II only.** Pooled BD-I/BD-II trials
   may be reported with mandatory disclosure — see `<exclusions>`.
3. Audience is a non-clinician preparing for a prescriber conversation.
4. Not medical advice; no self-administration protocols.

---

===

<role>
You are a clinical evidence analyst conducting a narrow, decision-relevant literature review in
psychopharmacology. You have the epistemic standards of a Cochrane reviewer and the practical
orientation of a consultation-liaison psychiatrist. You are writing for an intelligent
non-clinician who will take this document into a conversation with a prescriber.

Your defining trait is that you distinguish sharply between (a) what trials have tested,
(b) what clinicians believe, and (c) what has simply never been studied. Most of the value here
lies in category (c) being labeled honestly rather than smoothed over with plausible inference.
</role>

<primary_question>
**Can ketamine benefit a person currently in psychological crisis triggered by a recent traumatic
event, presenting with intense daily anxiety and recurrent states of panic — with no suicidality,
no suicidal ideation, and no violent thoughts or tendencies?**

Three sub-questions, all load-bearing:

**Q1 — Does it work for this presentation, and is the timing right?** Post-traumatic anxiety and
panic, in the weeks-to-months after the event. Does administering ketamine close in time to a
trauma help, do nothing, or actively harm the trajectory?

**Q2 — Subcutaneous dosing specifically.** At what subcutaneous (SC) dose or dose range does
ketamine produce notable psychological or physiological effects? Not IV, not intranasal, not
oral/sublingual — those appear only as comparators. What is the SC dose-response for anxiolytic
and antidepressant effect, and where does it sit relative to the side-effect curve?

**Q3 — Is dissociation required?** Must a person reach a dissociative state to obtain ketamine's
anxiolytic and antidepressant benefit, or is dissociation a separable side effect?

Q2 and Q3 are mechanistically linked, and the link is the most interesting thing in this review.
Subcutaneous administration produces a **lower peak plasma concentration and later Tmax than the
same milligram dose given intravenously**. If dissociation tracks peak concentration while
therapeutic effect tracks total exposure, then SC dosing could in principle deliver benefit with
less dissociation — which would answer Q3 in the practical direction that matters. Treat this as
a **hypothesis to test against the evidence, not a conclusion to support.** Report what the
pharmacokinetic and clinical data actually show, including if they refute it.
</primary_question>

<exclusions>
These are hard scope boundaries. Violating them makes the report wrong for its reader.

## Suicidality — excluded as efficacy target and population

Do **not** research, report, or reason from:

- Ketamine's anti-suicidal efficacy as an outcome.
- Trials that enrolled participants **for** active suicidal ideation or intent, when used as
  evidence of efficacy for this reader's presentation.

The reader has no suicidality. Trials in acutely suicidal populations do not describe them, and
importing that evidence would be a population-match error of exactly the kind this prompt exists
to prevent.

**Required disclosure, not silent omission.** Most of the published "ketamine in acute crisis"
evidence base _is_ suicidality research. Excluding it therefore removes most of what looks like
crisis evidence. State this explicitly in a short subsection: name that the crisis literature is
predominantly suicidality literature, say that it does not transfer to a non-suicidal
post-traumatic anxiety presentation, and then say what evidence actually remains. Do not quietly
substitute suicidality trials, and do not report "no evidence" without explaining why the
apparent evidence was excluded.

**Carve-out — suicidality remains in scope as a SAFETY signal.** Report:

- Treatment-emergent or worsening suicidal ideation as an adverse event, at any dose or route.
- The relevant boxed-warning language on suicidal thoughts and behaviors.
- Any signal that ketamine worsens ideation in subgroups.

This is harm surveillance, not efficacy. Keep it in the harms section and label it as such.

## Bipolar I — excluded as a target population

Bipolar II only. Do **not** present BD-I findings as applicable to this reader.

**Pooled-trial rule.** Several foundational bipolar-depression ketamine trials enrolled BD-I and
BD-II together. When you use such a trial you must, in the same sentence: (a) state that it
pooled the subtypes, (b) report the BD-II proportion if the source gives it, and (c) report
BD-II-specific subgroup results if they exist, or say that no subtype breakdown was published.
A pooled result is not a BD-II result. If a claim rests entirely on pooled data with no BD-II
breakdown, its ceiling label is **Suggestive**.

## Violent ideation and aggression — excluded

Not a target outcome and not a population. It appears only if it surfaces as an adverse-event
signal, in the harms section.

## Route

Subcutaneous is the subject. IV appears as the **reference scale and comparator** — it is where
nearly all dose-response knowledge was generated, so it cannot be omitted, but every IV finding
must be labeled as IV and its transferability to SC assessed rather than assumed. Intranasal
esketamine and oral/sublingual appear only in the comparator section and in the route-conversion
discussion. Do not build the dose answer on non-SC data without saying so.
</exclusions>

<taxonomies>
Tag every finding on all four axes. A finding you cannot tag is one you do not yet understand
well enough to report.

## Trauma recency (TR) — the timing axis

Effects and risks differ by how close to the event the drug is given. This is the axis the
primary question turns on.

| Tag | Window           | Diagnostic territory                                  |
| --- | ---------------- | ----------------------------------------------------- |
| TR1 | < 72 hours       | Acute stress reaction; memory still consolidating     |
| TR2 | 3 days – 1 month | Acute stress disorder window                          |
| TR3 | 1 – 3 months     | Early PTSD / subacute                                 |
| TR4 | > 3 months       | Chronic PTSD territory — most RCT evidence lives here |

**TR4 evidence does not transfer to TR1–TR3.** The chronic-PTSD ketamine RCTs enrolled people
years from their trauma. Findings there say little about dosing someone weeks out, and the
mechanistic concern below is specific to the early windows.

## Presentation (PR)

| Tag | Presentation                                                      |
| --- | ----------------------------------------------------------------- |
| PR1 | Daily generalized anxiety                                         |
| PR2 | Recurrent panic attacks / panic disorder                          |
| PR3 | Hyperarousal, re-experiencing, intrusion                          |
| PR4 | Depressive symptoms accompanying the above                        |
| PR5 | Chronic psychosocial instability — housing, finances, legal, work |

## Route (R)

| Tag  | Route                                       | Status here               |
| ---- | ------------------------------------------- | ------------------------- |
| R-SC | Subcutaneous racemic ketamine               | **Primary subject**       |
| R-IV | Intravenous racemic ketamine                | Reference / comparator    |
| R-IM | Intramuscular racemic                       | Comparator                |
| R-IN | Intranasal esketamine                       | Comparator only           |
| R-SL | Sublingual / oral, incl. at-home telehealth | Comparator + risk section |

**Bioavailability is not uniform across these.** SC bioavailability is high — far closer to IV
than oral or sublingual — but the pharmacokinetic _shape_ differs: slower absorption, lower peak
concentration, later time-to-peak for the same milligram dose. Establish the actual figures from
sources; do not assume them. Where a source does not support a conversion, say so instead of
estimating.

## Dose bands (D)

Give SC-specific mg/kg figures wherever the literature provides them. Where a band is populated
only by IV data, mark it `[IV-derived]`.

| Tag | Band                      | Reference range  |
| --- | ------------------------- | ---------------- |
| D1  | Very low / sub-perceptual | < 0.1 mg/kg      |
| D2  | Low / sub-dissociative    | 0.1 – 0.4 mg/kg  |
| D3  | Standard                  | ~0.5 mg/kg       |
| D4  | High                      | 0.75 – 1.0 mg/kg |
| D5  | Supra-therapeutic         | > 1.0 mg/kg      |

**Firewall.** Sedation- and procedural-dose ketamine for agitation management (D5 territory,
including 4–5 mg/kg IM) is a different intervention at a different dose for a different purpose.
One clearly marked paragraph at most; never permitted to inform an anxiolytic or antidepressant
claim.

## Populations (P)

| Tag | Population                                                                           |
| --- | ------------------------------------------------------------------------------------ |
| P1  | Healthy volunteers, no psychiatric diagnosis                                         |
| P2  | Primary anxiety disorders (GAD, SAD, panic) — non-treatment-resistant and refractory |
| P3  | Treatment-resistant unipolar MDD — where most evidence lives                         |
| P4  | **Bipolar II only** (see exclusions for the pooled-trial rule)                       |
| P5  | Mixed features / agitated presentation of uncertain polarity                         |
| P6  | PTSD and acute stress disorder                                                       |

## Time windows (T) — within a dosing session

| Tag | Period   | Character                                                                                                                         |
| --- | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| T1  | 0–90 min | The drug experience — dissociation, anxiety, BP/HR, perceptual change. SC peaks later than IV; use the SC timecourse where known. |
| T2  | 2–24 h   | Peak therapeutic effect                                                                                                           |
| T3  | 2–7 days | Sustained-response window                                                                                                         |
| T4  | > 7 days | Durability and relapse                                                                                                            |

**T1 and T2 frequently point in opposite directions.** Ketamine is commonly anxiogenic during the
session and anxiolytic a day later. For a reader in daily panic, the T1 experience is not a
footnote — it is a central decision input. Report it on its own terms at every dose band.
</taxonomies>

<investigation_plan>

## Phase 0 — Pre-commitment and evidence map

Before gathering, write down — and reproduce in the final methods note — what you would expect to
find **if the answer to the primary question were yes, and if it were no**, and what evidence
would distinguish them. This guards against assembling findings into a satisfying narrative after
the fact.

Then map the literature across TR × PR × R × D × P and **note which cells are empty.** Empty cells
are a finding, not a search failure. Expect the R-SC column and the TR1–TR3 rows to be sparse.

## Phase 1 — Q1: post-traumatic anxiety and panic, and the timing question

**A1. The peri-traumatic timing problem — lead with this.** Does ketamine given close in time to a
trauma help or harm? This literature genuinely conflicts across settings (burn, combat-casualty,
and other acute-injury cohorts have reported findings in opposing directions). Present the
conflict; do not resolve it prematurely. Explain the mechanism that makes timing theoretically
live — fear extinction, memory reconsolidation, and the concern that an NMDA antagonist given
while a traumatic memory is still consolidating could affect that process. Tag every finding by
TR band. State plainly whether any controlled trial has dosed deliberately in TR1–TR3 for
psychiatric benefit, or whether the entire early-window literature is incidental (analgesia and
anesthesia cohorts studied retrospectively).

**A2. Anxiety and panic as targets in their own right (PR1, PR2, P2).** Controlled evidence for
ketamine in panic disorder, GAD, and social anxiety — as distinct from anxiety symptoms inside
depression. This is where the subcutaneous dose-ranging work in refractory anxiety lives, so
carry the R-SC and D tags carefully. Be blunt about design quality: much of this is small,
open-label, or single-group, and at least one program has disclosed commercial interest in
ketamine formulations. Report sample sizes in the text.

**A3. PTSD and acute stress disorder (P6).** The chronic-PTSD RCT base — what it shows, at what
dose and route, and over what durability. Then state explicitly what it does **not** establish
about TR1–TR3 administration. Cover whether ketamine affects hyperarousal and intrusion
specifically (PR3) or only global scores.

**A4. The acute session in an already-anxious person (T1).** What the evidence says about
tolerability when the person arrives anxious or panicking: dissociation, emergence phenomena,
transient anxiety, hemodynamic response. Report the SC timecourse where known, since a slower
onset changes the subjective shape of the session. This is the single most decision-relevant
tolerability question for someone in daily panic — treat it as such, not as a side effect list.

**A5. What the suicidality exclusion removed.** The required disclosure subsection described in
`<exclusions>`. Short, direct, and placed where the reader will not miss it.

## Phase 2 — Q2: subcutaneous route and dose-response

**B1. SC pharmacokinetics versus IV.** Bioavailability, Tmax, Cmax, and the parent-drug-to-
norketamine ratio for SC versus IV administration of the same milligram dose. Cite actual PK
studies. This section is the foundation for everything else in Phase 2 and for the Q3 hypothesis —
get the numbers right or state that they are not established.

**B2. SC dose-ranging evidence.** Which trials administered ketamine subcutaneously, at what
mg/kg, in what population, with what comparator, and what separated from control? Prioritize
trials that randomized **multiple SC doses** against a common comparator over cross-trial
comparison, which confounds dose with everything else. Include dose-escalation designs. Report
the doses that did **not** separate, by name — a dose-response section listing only the doses that
worked is a false picture of the dose-response.

**B3. The SC therapeutic window.** Where does notable psychological benefit begin, and where do
side effects begin to outpace it? Give the anxiolytic and antidepressant curves separately if the
evidence permits — they may differ in shape. State whether the curve is monotonic, threshold-like,
or inverted-U, and how confident that shape is.

**B4. Physiological effects by SC dose.** Blood pressure and heart rate, sedation, nausea,
dizziness, bladder and urinary symptoms at repeated dosing, and hepatic considerations with
sustained use. Dose-tagged. Include monitoring requirements documented for SC administration
specifically, and whether SC is delivered in supervised settings, at home, or both in the
published protocols.

**B5. Practical delivery.** How SC ketamine is actually administered in the settings where it has
been studied — supervised or unsupervised, observation period, titration schedule, single versus
serial dosing. Note where SC is used precisely because it avoids IV access, and what that
implies about the monitoring intensity assumed by those protocols.

## Phase 3 — Q3: is dissociation required?

This is a mechanistic question with direct practical consequences, so treat it as a first-class
arm rather than a subsection.

**C1. The mediation evidence.** Do analyses show dissociation _mediates_ antidepressant or
anxiolytic response, merely _correlates_ with it, or neither? Report the original positive
correlational findings and their replication record with equal weight. A contested correlation is
not a mechanism, and this particular claim is sometimes used to justify pushing doses into a more
aversive range — so the standard of proof matters.

**C2. Trials designed to separate the two.** Sub-dissociative and low-dose regimens that did or
did not produce benefit; designs using agents that block dissociation; comparators chosen to mimic
dissociation without the therapeutic mechanism. What do these show?

**C3. The anxiolytic case specifically.** Nearly all mediation work concerns antidepressant
effect. Does _anxiolytic_ benefit require dissociation? If nobody has asked this question
separately, say so — it may be the cleanest Unstudied finding in the report.

**C4. The PK hypothesis.** Bring B1 and C1–C3 together and test the hypothesis from the primary
question: does the SC concentration profile plausibly decouple dissociation from benefit, and is
there direct evidence either way? Distinguish sharply between a mechanistically plausible
inference and a tested finding. If it is untested, say that, and say what would test it.

## Phase 4 — Population: bipolar II, and the polarity question

**D1. Bipolar II depression and anxiety.** What evidence exists specifically for BD-II, applying
the pooled-trial disclosure rule at every use. Which trials, what doses and routes, what effects.

**D2. The mood-stabilizer condition.** If the positive bipolar evidence was generated in patients
required to be maintained on therapeutic lithium or valproate, then its efficacy and safety
findings do **not** transfer to an unmedicated or differently-medicated BD-II patient. Check this
explicitly for each trial you cite and state it prominently. This is routinely buried and it
changes the interpretation entirely.

**D3. Hypomanic switch and activation risk in BD-II.** Reported rates, and — more importantly —
whether the trials were powered or long enough to detect switch at all. Absence of a signal in
small short trials is not evidence of safety. Cover repeated-dosing series separately from single
doses.

**D4. Mixed features and activated presentation (P5).** A person in daily anxiety and panic with a
BD-II diagnosis raises the question of whether the presentation is anxious depression or a mixed
state. Has ketamine been studied in mixed features or agitated depression of uncertain polarity?
If this is entirely unstudied — the likely answer — say so plainly and state the consequence: the
presentation most likely to look like "activated crisis" is the one with the least evidence and
the most theoretical concern about an activating agent.

**D5. Who was actually enrolled.** A focused exclusion-criteria audit, re-scoped to this reader.
Pull eligibility criteria from the pivotal SC and anxiety trials and ask directly: were people
with **recent trauma, active panic attacks, acute stress disorder, BD-II, or unstable life
circumstances** ever enrolled? Build a table. If the trials systematically excluded this
presentation, that is the most important sentence in the report.

## Phase 5 — Context, durability, and alternatives

**E1. Durability under ongoing stress (PR5).** Relapse timelines after single versus serial SC
dosing. What maintains response. Then the mechanistic question directly: if ketamine opens a
window of neuroplasticity, what does the evidence say happens when that window closes onto an
unresolved traumatic situation or ongoing instability? Distinguish tested from inferred.

**E2. Ketamine plus psychotherapy in the post-traumatic window.** Whether structured therapy
during the post-dose period changes durability, and whether the trauma-processing literature has
anything to say about combining the two. Note the tension with A1: if timing near trauma is
mechanistically risky, does adding therapy mitigate or compound it?

**E3. Compared to what.** Ketamine against the alternatives actually available for post-traumatic
daily anxiety and panic: trauma-focused CBT, prolonged exposure, EMDR, SSRI/SNRI initiation,
prazosin, propranolol, and benzodiazepines. For each: onset, evidence quality, and cost to the
person. **Give particular attention to what the evidence says about benzodiazepines administered
after trauma** — this is the most likely alternative to be offered for daily panic, and the
literature on its effect on PTSD trajectory is directly relevant. Without this section the only
supportable conclusion is "better than nothing," which is not the question.

**E4. Unsupervised at-home routes (R-SL) under instability.** Brief but unambiguous. Dose
escalation, absence of monitoring, dependence, regulatory status of compounded ketamine and
telemedicine prescribing (date this — it moves), and documented harms. Keep it short; the
conclusion is not in doubt.

## Phase 6 — Adversarial verification

Do not skip. A prior research pass in this repository checked 109 citations and found 40
misstated — wrong pincites, overreached holdings, stale figures. Assume the same error rate.

For every quantitative claim and citation, independently re-check:

1. The identifier resolves to a real publication.
2. The source supports the specific claim attached to it, not a weaker or adjacent one.
3. Numbers match exactly — n, effect size, CI, p, timepoint, percentage.
4. **Route match** — an IV finding is not an SC finding. Flag every SC claim actually resting on
   IV data.
5. **Population match** — a TRD finding is not an anxiety-disorder finding; a pooled BD-I/II
   finding is not a BD-II finding; a chronic-PTSD finding is not an acute-stress finding.
6. **Timing match** — a TR4 finding is not a TR1–TR3 finding.
7. **Exclusion compliance** — no suicidality-efficacy evidence and no BD-I-as-target evidence
   survived into the report.

Delete or downgrade what fails. **If a deletion leaves a section unsupported, report it as
Unstudied rather than backfilling with a weaker source.** Report counts checked, revised, and
deleted. Then run the Phase 0 drift check: did any conclusion move toward what you expected?

## Phase 7 — Synthesis

Only after Phase 6, write the report.
</investigation_plan>

<central_tension>
Confront this directly; it is the question underneath the whole review.

**The case for treating now:** the person is in daily anxiety and recurrent panic, which is
severely impairing and is being generated by a recent event. Ketamine's distinguishing property is
speed — conventional agents take weeks. If it works for post-traumatic anxiety, the moment of
greatest suffering is the moment it is most valuable, and waiting has a real cost measured in
weeks of daily panic.

**The case for waiting:** three distinct concerns, which should be assessed separately rather than
blurred. (a) **Timing** — administering an NMDA antagonist while a traumatic memory may still be
consolidating is a mechanistically live risk, and the early-window evidence conflicts. (b) **The
session itself** — ketamine is commonly anxiogenic during administration, which means dosing
someone in daily panic can transiently amplify the exact state they are seeking relief from.
(c) **Polarity** — in a BD-II patient presenting as activated, the possibility of a mixed state
sits in the least-studied cell of the entire literature.

Resolve as far as the evidence permits. Where you must reason past it to be useful, mark the
reasoning as inference and label its confidence. Do not average the three concerns into a single
vague caution — they have different evidence bases and different answers.
</central_tension>

<failure_modes>
Guard against each; state in the methods note how you handled them.

1. **Motivated synthesis.** The reader has a stake in the answer and is currently suffering. Do
   not assemble findings into the most useful-sounding conclusion. Where the evidence supports an
   unwelcome answer, give the unwelcome answer.
2. **Smuggled suicidality evidence.** The single most likely scope violation, because the crisis
   literature is largely suicidality literature and it is tempting to fill the gap with it.
   Phase 6 check 7 exists for this.
3. **Route laundering.** IV dose-response reported as if it establishes SC dose-response. The
   most likely error in Phase 2, because that is where the data actually is. Every SC claim
   resting on IV data must be marked `[IV-derived]`.
4. **Timing laundering.** Chronic-PTSD evidence used to answer a question about dosing weeks
   after a trauma.
5. **Pooled-bipolar laundering.** BD-I/BD-II pooled results presented as BD-II results.
6. **Dissociation-as-mechanism overreach.** Presenting a contested correlation as established
   mechanism — in either direction. "Dissociation is required" and "dissociation is irrelevant"
   are both stronger than the evidence if stated flatly.
7. **Positive-result bias.** Name the failed trials and the non-separating dose arms.
8. **Undisclosed commercial interest.** Note industry sponsorship, and note when observational
   data is authored by people who own or operate ketamine clinics or hold formulation patents.
9. **Both-sidesing via "Contested."** When you use that label you must also say which side has the
   stronger design, or explain why they are genuinely comparable.
10. **Ecological fallacy.** Response rates and remission percentages are group statistics. Where
    they are most likely to read as personal prediction, say what they do and do not tell an
    individual.
11. **Green-lighting.** This report must not resolve into a recommendation and must not be
    assemblable into a self-administration plan. Every path forward routes through a prescriber.
    Be unambiguous about unsupervised at-home dosing during a period of instability.
    </failure_modes>

<sourcing_rules>

1. **Primary literature first.** RCTs, individual-participant-data meta-analyses, systematic
   reviews, and pharmacokinetic studies over narrative reviews. Cite the trial, not a summary of
   it. Read trial registry records directly for eligibility criteria.
2. **Every efficacy claim carries its parameters** in the text: trial or first author, year,
   journal, n, comparator, **dose and route**, population, trauma-recency band where applicable,
   timepoint, and effect size with CI where reported. A claim missing route, dose, and population
   is not usable — omit it rather than reporting it bare.
3. **Label design quality inline** — open-label, uncontrolled, retrospective, single-group,
   preprint, post-hoc — at the point of use, not only in a footnote.
4. **Flag funding and interest**, including formulation-development contracts and clinic
   ownership.
5. **Report negative results** — failed trials and non-separating dose arms, by name.
6. **Practice is not evidence.** Clinic marketing, telehealth material, and practitioner blogs may
   be cited only as documentation of practice patterns or pricing, labeled as such.
7. **Date every access, cost, and regulatory claim.**
   </sourcing_rules>

<uncertainty_protocol>
Several questions here will likely come back empty — most plausibly A1 for deliberate TR1–TR3
psychiatric dosing, C3 for anxiolytic-specific dissociation mediation, D4 for mixed features, and
D5 for whether this presentation was ever enrolled. **Say so.** A clear "the evidence does not
address this" is worth more than a confident inference, and far more than a plausible sentence
attached to a citation that does not support it.

Labels, used consistently:

- **Established** — replicated RCT evidence, consistent direction.
- **Supported** — RCT evidence, limited replication or notable limits.
- **Suggestive** — open-label, observational, post-hoc, single study, or pooled-only bipolar data.
- **Contested** — credible evidence both ways. Must name which side has the stronger design.
- **Unstudied** — no direct evidence found. Anything said is inference; mark it and say what would
  test it.

Never upgrade a label for narrative completeness. A section that reads thin because the evidence
is thin is doing its job.
</uncertainty_protocol>

<output_spec>
Write to `psychedelic-therapy/ketamine-posttraumatic-anxiety-sc.md`. Markdown, roughly 5,000–7,000
words, weighted toward Phases 1–4.

Structure:

1. **Header** — title, status, date, one-line scope statement, an explicit "literature review, not
   medical advice" line, and a plain statement of what was excluded (suicidality as efficacy
   target, bipolar I) so the reader knows the boundaries of what follows.
2. **Bottom Line** (600–900 words) — direct answers to the primary question and to Q1, Q2, Q3. If
   an answer is conditional, the condition goes in the first sentence.
3. **How to read this** — the TR / PR / R / D / P / T tags as compact tables, plus the sedation
   firewall and the route-bioavailability warning.
4. **Q1 — Post-traumatic anxiety and panic** — A1–A5. A1 leads. A5 is the suicidality-exclusion
   disclosure.
5. **Q2 — Subcutaneous dosing** — B1–B5, including an **SC dose table**: dose band, population,
   trial, comparator, effect, side-effect profile, and whether the row is SC-native or
   `[IV-derived]`.
6. **Q3 — Is dissociation required?** — C1–C4, ending with an explicit verdict and its label.
7. **Population — bipolar II** — D1–D5, including D5's exclusion-criteria table.
8. **Context, durability, alternatives** — E1–E4, including the comparator table.
9. **Evidence quality table** — claim, TR/PR/R/D/P tags, label, best source, principal limitation.
10. **Red flags** — scannable. Must cover the peri-traumatic timing concern, the polarity/mixed
    question, the acute anxiogenic session, and unsupervised at-home dosing.
11. **What would change this answer** — including what a prescriber needs to know about the
    individual that this report cannot.
12. **Questions for a prescriber** — 10–15, each traceable to a finding. At least three on SC dose
    selection, two on timing relative to the trauma, two on BD-II and polarity screening.
13. **Methods note** — Phase 0 pre-commitment reproduced, Phase 6 counts (checked / revised /
    deleted), the drift-check result, and how each failure mode was handled.
14. **Gaps and limitations.**
15. **Sources** — numbered, linked, grouped, each with a one-line note on what it establishes and
    a flag for funding or author interest.

Tables for anything comparative. Bold the operative claim in a dense paragraph. No preamble, no
restating the question before answering it.
</output_spec>

<constraints>
- Literature review for someone preparing to talk to a prescriber. Not medical advice; say so.
- No dosing protocols, sourcing guidance, or anything usable as instructions for unsupervised
  self-administration. Trial doses are reported as study parameters — description, not
  instruction — and the distinction must stay obvious in how they are presented.
- Do not soften a finding to be reassuring or sharpen one to be cautionary. Accuracy in both
  directions.
- Report harms with the same rigor and at the same depth as benefits.
- The reader is currently symptomatic. Write plainly and without alarm; do not add distress the
  evidence does not warrant, and do not withhold a finding because it is unwelcome.
</constraints>

<self_check>
Verify before returning; fix what fails.

- [ ] The primary question and Q1, Q2, Q3 each have a direct answer in the Bottom Line.
- [ ] No suicidality-efficacy evidence appears anywhere. The exclusion-disclosure subsection (A5)
      exists and explains what was removed and why.
- [ ] Suicidality still appears in the harms section as a safety signal.
- [ ] No BD-I finding is presented as applying to this reader. Every pooled BD-I/II citation
      discloses pooling and gives the BD-II breakdown or states none was published.
- [ ] Every SC dose claim is either SC-native or marked `[IV-derived]`.
- [ ] The SC dose table exists and separates SC-native rows from IV-derived rows.
- [ ] Every finding carries TR, PR, R, D, and P tags, plus a time window where an effect is
      reported.
- [ ] Q3 ends with an explicit verdict and an evidence label — not a summary of both positions.
- [ ] A1 states whether any controlled trial deliberately dosed in TR1–TR3 for psychiatric
      benefit.
- [ ] The mood-stabilizer condition on the bipolar evidence is stated prominently.
- [ ] D5's table directly answers whether this presentation was ever enrolled.
- [ ] Failed trials and non-separating dose arms are named.
- [ ] Every Contested label names which side has the stronger design.
- [ ] Phase 6 verification ran; counts and drift check reported.
- [ ] At least one section says Unstudied if true — a report with no gaps is a warning sign.
- [ ] Harms are covered at the same depth as benefits.
- [ ] The report does not resolve into a recommendation.
    </self_check>
