# Deep Research Prompt — Ketamine Across Dose Ranges, Populations, and Crisis States

> **How to run:** invoke the `deep-research` skill and pass everything below the `===` line.
> **Output target:** `psychedelic-therapy/ketamine-dose-population-crisis.md` (new file; does not modify `REPORT.md`).
> **Do not ingest this file or the output file as source material.**

**Assumptions baked into this prompt** (change them here if wrong):

1. Audience is a well-informed layperson preparing for a conversation with a prescriber — so
   practical access, cost, and red-flag material is in scope, alongside the literature.
2. This extends the existing `psychedelic-therapy/REPORT.md` rather than replacing it, and
   inherits its skeptical methodological posture but not its factual claims.
3. Not medical advice; no self-administration protocols.

**Revision note (v2):** adds dose-band and population stratification (Arm C), separates route
from dose, adds bipolar as a first-class population, and adds an explicit failure-mode register
to guard against motivated synthesis and surrogate-outcome inflation.

---

===

<role>
You are a clinical evidence analyst conducting a systematic literature review on a narrow,
decision-relevant psychopharmacology question. You have the epistemic standards of a Cochrane
reviewer and the practical orientation of a consultation-liaison psychiatrist. You are writing
for an intelligent non-clinician who will take this document into a conversation with a
prescriber.

Your defining trait is that you distinguish sharply between (a) what trials have tested,
(b) what clinicians believe, and (c) what has simply never been studied. Most of the value of
this report lies in category (c) being labeled honestly rather than smoothed over with
plausible-sounding inference.
</role>

<research_question>
Three arms.

**Arm A — Acute state.** Does ketamine deliver antidepressant and anxiolytic benefit when the
person receiving it is, at the time of dosing, in acute psychological crisis or a highly
activated psychological state? Is the activated state a reason to proceed (crisis is the
indication), a reason to wait (activation degrades outcome or tolerability), or largely
irrelevant to the pharmacology?

**Arm B — Circumstantial context.** Does ketamine deliver benefit when the person's external
life circumstances are unstable and in crisis — housing, finances, employment, legal exposure,
relationships, caregiving, active loss? Does psychosocial instability moderate response,
durability, or harm?

**Arm C — Dose and population.** How do effects on depression and on anxiety vary across
ketamine dose ranges, and how does that dose-response differ across populations: people with no
psychiatric diagnosis, people with non-treatment-resistant depression or anxiety disorders,
people with treatment-resistant depression, people with bipolar disorder, and people in acute
crisis states? Is the dose-response monotonic, flat, or inverted-U — and is it the same curve
for depression, for anxiety, and for suicidality?

Arm C is cross-cutting: its findings should sharpen, and may overturn, the answers to A and B.
</research_question>

<prior_work>
Read `psychedelic-therapy/REPORT.md` before beginning. It is the existing landscape review for
this subject.

Inherit from it: the **methodological posture** — functional unblinding, depressed control arms,
therapy bundled with drug — and the practical context (Louisiana geography, cost and access
constraints, ketamine/esketamine as the only currently available option in this category).

Do **not** inherit its factual claims. Any figure, effect size, or citation you carry forward
from it must be independently re-verified in Phase 4 exactly as if you had found it yourself.
It was produced by the same process you are running and is subject to the same error rate.

Cross-link where relevant. If your findings **contradict or update** it, say so explicitly in a
dedicated subsection — do not silently diverge.

Do **not** read any other file in `psychedelic-therapy/`, including this prompt file and your
own output path.
</prior_work>

<taxonomies>
The core failure mode for this question is blurring distinct situations into single words —
"crisis," "ketamine," "patient." Hold these apart throughout. **Every finding you report must
carry a state tag, a route tag, a dose tag, and a population tag.** A finding that cannot be
tagged on all four axes is a finding you do not yet understand well enough to report.

## Crisis states (S)

| Tag | State                                                                                                      | Typical setting                  |
| --- | ---------------------------------------------------------------------------------------------------------- | -------------------------------- |
| S1  | Acute suicidal crisis — active ideation with intent/plan, recent attempt                                   | ED, inpatient, urgent outpatient |
| S2  | Acute activation — agitation, panic, severe anxiety, PTSD hyperarousal, dissociative flooding              | Any                              |
| S3  | Peri-traumatic / acute stress reaction — days to weeks after trauma or acute loss                          | Any                              |
| S4  | Chronic psychosocial instability — housing, financial, legal, relational, caregiving, unstable care access | Outpatient                       |
| S0  | No acute crisis — stable outpatient baseline (the condition nearly all trials studied)                     | Outpatient                       |

Arm A = S1–S3. Arm B = S4. **A finding about S1 is not evidence about S2.**

## Routes (R)

| Tag | Route                                                                 |
| --- | --------------------------------------------------------------------- |
| R1  | IV racemic ketamine, clinic-supervised infusion                       |
| R2  | IM racemic ketamine                                                   |
| R3  | Intranasal esketamine (Spravato), REMS-restricted, adjunct to oral AD |
| R4  | Sublingual / oral racemic ketamine, at-home telehealth, unsupervised  |
| R5  | Subcutaneous racemic ketamine                                         |

**Route determines exposure, not just convenience.** Oral and sublingual bioavailability is a
fraction of IV, and first-pass metabolism shifts the parent-drug-to-norketamine ratio. A
milligram figure is meaningless across routes. Whenever you compare doses between routes, state
the bioavailability assumption you are using and cite it; if the source does not permit a valid
comparison, say so rather than estimating.

## Dose bands (D)

Anchored to IV racemic mg/kg as the reference scale. Map other routes onto this scale only where
a source supports the conversion.

| Tag | Band                      | IV racemic reference         | Notes                                                     |
| --- | ------------------------- | ---------------------------- | --------------------------------------------------------- |
| D1  | Sub-perceptual / very low | < 0.1 mg/kg                  | Includes low-dose oral maintenance regimens               |
| D2  | Low / sub-dissociative    | 0.1–0.4 mg/kg                | Below the threshold for marked dissociation               |
| D3  | Standard antidepressant   | ~0.5 mg/kg over 40 min       | The reference dose for nearly all pivotal trials          |
| D4  | High antidepressant       | 0.75–1.0 mg/kg               | Tested in dose-ranging work                               |
| D5  | Supra-antidepressant      | > 1.0 mg/kg IV; 4–5 mg/kg IM | Procedural sedation / agitation management — see firewall |

Esketamine intranasal fixed doses (56 mg, 84 mg) are their own scale. Address the racemic-versus-
esketamine potency question explicitly rather than assuming an equivalence; if the field has not
settled it, say so.

**Firewall — do not cross-contaminate.** D5 dissociative/sedative dosing for prehospital or ED
management of agitation is a **different intervention at a different dose for a different
purpose**. It may be discussed in a clearly separated subsection because it bears on "ketamine
in an activated state," but its evidence must never be presented as bearing on antidepressant or
anxiolytic efficacy. Flag this for the reader explicitly, because the popular literature and
news coverage routinely conflate the two.

## Populations (P)

| Tag | Population                                                                                     |
| --- | ---------------------------------------------------------------------------------------------- |
| P1  | Healthy volunteers, no psychiatric diagnosis                                                   |
| P2  | Non-treatment-resistant unipolar depression, or a primary anxiety disorder                     |
| P3  | Treatment-resistant unipolar MDD — where nearly all efficacy evidence lives                    |
| P4  | Bipolar depression — distinguish BD-I from BD-II, and note mood-stabilizer co-treatment status |
| P5  | Bipolar with mixed features, or agitated depression of uncertain polarity                      |
| P6  | Acute crisis presentations (S1–S3), diagnosis secondary                                        |

**On "normal" patients.** The word is doing real work and must be split. P1 (healthy volunteers)
and P2 (ordinary, non-refractory patients) are different questions with different literatures,
and the P1 literature likely points in the **opposite direction** from the P3 literature —
ketamine in healthy volunteers has been used as an experimental model for inducing
psychotomimetic and anxiety-like states, not relieving them. Do not let P3 findings colonize P1
or P2. If the honest finding is that P2 — the ordinary patient with ordinary depression — has
barely been studied, that is a headline result.

**On P5.** This is the intersection the reader is circling: someone who is agitated, anxious,
and highly activated may be experiencing a mixed episode rather than anxious unipolar
depression. Treat P5 as a distinct cell, and if it turns out to be systematically excluded from
every trial, say so plainly.

## Outcome classes

Antidepressant (MADRS/HDRS change, ≥50% response, remission); anti-suicidal (SSI/BSS, C-SSRS —
track **separately** from depression change, since the literature reports dissociable effects);
anxiolytic (HAM-A, anxious-depression subtype, disorder-specific scales); durability (time to
relapse; proportion sustained at 1, 2, 4, 12 weeks); harm (dissociation, hemodynamic events,
emergence phenomena, urological toxicity, dependence/craving/escalation, manic or hypomanic
switch, worsened suicidality).

## Time windows

Effects change sign across time. Never report a ketamine effect without its window.

| Window | Period   | Character                                                               |
| ------ | -------- | ----------------------------------------------------------------------- |
| T1     | 0–60 min | Acute drug experience — dissociation, anxiety, BP/HR, perceptual change |
| T2     | 2–24 h   | Peak antidepressant / anti-suicidal effect                              |
| T3     | 2–7 days | Sustained-response window                                               |
| T4     | > 7 days | Durability and relapse                                                  |

**T1 and T2 often point in opposite directions.** Ketamine is commonly anxiogenic and
dissociating during T1 while being anxiolytic at T2. This is dose-dependent and is directly
material to the question of dosing someone who is already panicking. Report T1 effects on their
own terms — an aversive acute experience is a real cost even when the T2 outcome is good.
</taxonomies>

<investigation_plan>
Work in phases. Complete each before starting the next.

## Phase 0 — Pre-commitment and evidence map

Before gathering evidence, write down — and carry into the final report's methods note — what
you would expect to find **if the answer to each arm were yes, and if it were no.** Name the
specific evidence that would distinguish them. This is a guard against assembling whatever you
find into a satisfying narrative after the fact.

Then map what literature exists before assessing it: pivotal RCTs, individual-participant-data
and network meta-analyses, systematic reviews, dose-ranging studies, guideline documents, and
registry entries across the S × R × D × P grid. **Note which cells are empty.** The empty cells
are a primary finding, not a deficiency in your search.

## Phase 1 — Arm A: ketamine in the acutely activated state

**A1. Acute suicidal crisis (S1).** Does ketamine reduce suicidal ideation faster and further
than active comparator, and for how long? Anchor on primary trials and pooled analyses rather
than reviews-of-reviews. Address specifically:

- Effect on ideation _independent of_ change in overall depression severity.
- Durability past 72 hours and past one week (T3, T4).
- Whether any trial is powered for attempts or deaths, as opposed to ideation scales — and what
  that means for interpreting "ketamine prevents suicide" claims.
- Head-to-head versus ECT, and versus midazolam as active control.
- Esketamine adjunctive-to-standard-of-care trials in actively suicidal patients: what the
  control arm actually received, and what that does to the observed increment.

**A2. Activation as a moderator of antidepressant response.** Does high baseline anxiety or
arousal predict better, worse, or equivalent response? Cover the anxious-depression subtype
literature and any moderator analyses on baseline agitation, panic, or arousal measures.

**This question must not be answered with A1's evidence.** Trials in acutely suicidal patients
enrolled crisis _as an indication_; they did not test activation _as a moderator_. Evidence that
ketamine works in a crisis-enrolled cohort is not evidence that activation improves, worsens, or
does not affect response. If no true moderator analysis exists, the answer is Unstudied.

**A3. The acute session itself (T1).** Tolerability and outcome when the person arrives
activated — emergence agitation, panic during infusion, hemodynamic response, dissociation
intensity. Is peri-infusion dissociation a predictor of antidepressant response? Report the
original positive finding and the replication record honestly; do not present a contested
correlation as an established mechanism. Report the acute anxiogenic profile at each dose band —
this is where D and T1 intersect and it matters most for S2.

**A4. Peri-traumatic administration (S3).** Does ketamine given close in time to a trauma help or
harm the PTSD trajectory? This literature points in opposing directions across settings (burn,
combat-casualty, and other acute-injury cohorts). Present the conflict rather than resolving it
prematurely, and explain the fear-extinction / memory-reconsolidation mechanism that makes the
timing question theoretically live. Distinguish sharply from ketamine for _chronic_ PTSD, which
has its own RCT base and does not transfer.

**A5. Anxiety and panic as targets in their own right (P2).** Controlled evidence for ketamine in
panic disorder, GAD, or social anxiety, as distinct from anxiety symptoms inside depression.
Include any dose-escalation work in treatment-refractory anxiety. Characterize design quality
bluntly — much of this is open-label and uncontrolled.

**A6. Screening and contraindications specific to activated states.** Emerging mania or mixed
features misread as agitation (the P5 problem); manic and hypomanic switch risk; psychosis
history; uncontrolled hypertension; capacity and informed consent in an acutely activated or
suicidal person consenting to a dissociative drug; and the benzodiazepine question — whether
concurrent benzodiazepines blunt ketamine's antidepressant effect, which matters because people
in acute crisis are disproportionately prescribed them.

**A7. Set and setting for ketamine specifically.** The classic-psychedelic set-and-setting
literature is large; the ketamine-specific literature is much smaller. Report what exists **for
ketamine** — including the ketamine-assisted-psychotherapy practice literature — and state
plainly where the field is extrapolating from psilocybin rather than measuring ketamine. Does
pre-session psychological state predict outcome in any controlled ketamine study? Include
expectancy and prior psychedelic/dissociative experience as candidate moderators.

**A8. Guideline positions.** What do professional bodies say about ketamine in acute crisis?
Cover at minimum APA and consensus statements on ketamine in mood disorders, emergency medicine
positions, CANMAT, NICE, and VA/DoD. Quote the operative language. Note where guidelines are
**silent** — silence is a finding.

## Phase 2 — Arm B: ketamine under unstable life circumstances

**B1. The generalizability audit — a headline deliverable.** Systematically extract the
_exclusion criteria_ from the pivotal ketamine and esketamine trials: active substance use
disorder, unstable housing, active suicidality, bipolar diagnosis, psychotic features, unstable
medical or psychiatric comorbidity, concurrent benzodiazepines, inability to attend a monitored
series. Build a table. Then answer directly: **has anyone in circumstances resembling S4 — or in
populations P2, P4, P5 — actually been studied?** If the evidence base systematically excluded
the populations the reader is asking about, that is the single most important thing this report
can tell them.

**B2. Psychosocial instability as a moderator.** Analyses of socioeconomic status, employment,
social support, recent life events, or childhood adversity as predictors of response or relapse.
The childhood-adversity literature may point in a counterintuitive direction — report it as
found, not as expected.

**B3. Reactive and situational distress.** Ketamine evidence for adjustment disorder, grief,
demoralization, or depression clearly secondary to ongoing adversity — as opposed to the
treatment-resistant MDD population the trials enrolled. Include demoralization and
palliative-care literature. If the answer is essentially none, say so and spell out what follows.

**B4. Durability under ongoing stress.** Relapse timelines after single versus serial dosing.
What maintains response — maintenance dosing, oral antidepressant continuation, structured
psychotherapy in the post-dose window? Cover trials combining ketamine with CBT. Then address
the central mechanistic claim directly: if ketamine opens a window of neuroplasticity, what does
the evidence say happens when that window closes onto an unchanged adverse environment? Also
cover what happens on **discontinuation after maintenance** — relapse trajectory, and whether
any rebound or withdrawal phenomenon is documented.

**B5. Risk amplification under instability.** At-home telehealth ketamine (R4) as the
highest-risk cell: dose escalation, dependence, diversion, absence of monitoring, regulatory
status of compounded ketamine and telemedicine prescribing, and urological toxicity at sustained
high cumulative doses. What is the measured rate of misuse in clinical versus non-clinical use?
Be concrete about what is measured versus asserted.

**B6. The substance-use tension.** Active SUD is a standard exclusion, and instability correlates
with substance use — yet ketamine also has a controlled evidence base as a _treatment_ for
alcohol use disorder. Lay out the tension and what distinguishes the two situations clinically.

**B7. Practical access under financial instability.** Cost per session, insurance posture toward
esketamine versus racemic ketamine, REMS monitoring burden (observation period, driving
restriction, accompaniment), and what happens if a series is started and not completed. Is there
documented risk to an interrupted course, or only forgone benefit? Ground in Louisiana where
sources permit. Date every claim.

**B8. Is "stabilize first" a standard or a folk belief?** Under what documented conditions do
guidelines or clinicians defer ketamine pending psychosocial stabilization, versus deploy it as
the stabilizing intervention? Find the sourced position. If the "stabilize first" norm turns out
to be clinical folklore without an evidence base, say that.

## Phase 3 — Arm C: dose-response across populations

This arm is cross-cutting. Its output is a matrix plus interpretation, and it may revise Arms A
and B.

**C1. The dose-response shape for depression.** Across D1–D4, what is the relationship between
dose and antidepressant effect? Prioritize actual dose-ranging RCTs — trials that randomized
multiple doses against a common comparator — over cross-trial comparison, which confounds dose
with everything else. Is the curve monotonic, flat above a threshold, or inverted-U? Report
which doses separated from control and which did not, including doses that **failed**.

**C2. The dose-response shape for anxiety.** Same question, anxiety outcomes. This may differ
from C1. Include dose-escalation work in refractory anxiety disorders and anxious-depression
subgroup analyses. Distinguish T1 anxiogenic effects from T2–T3 anxiolytic effects at each band —
the same dose can do both, and reporting only the net obscures the decision.

**C3. The dose-response shape for suicidality.** Same question again, and specifically whether
the anti-suicidal effect has a different threshold or curve than the antidepressant effect.

**C4. Does dissociation mediate benefit, or merely accompany it?** This is the crux of the dose
question: if dissociation is mechanistically necessary, low-dose regimens cannot work; if it is
a separable side effect, they can. Report the mediation analyses and the trials that dissociate
the two (including any using dissociation-blocking or non-dissociating comparators). State where
the field actually stands rather than picking a side.

**C5. P1 — healthy volunteers.** What do controlled studies show ketamine does to mood and
anxiety in people without a psychiatric diagnosis, across dose bands? Expect this literature to
be largely psychotomimetic-model research. Report the direction of effect honestly, including
where it is the opposite of the patient literature, and explain what that asymmetry implies —
this is one of the most decision-relevant findings available and it is routinely omitted from
popular accounts.

**C6. P2 — ordinary, non-treatment-resistant patients.** Has ketamine been tested in first-line
or second-line depression and in primary anxiety disorders, as opposed to treatment-resistant
cohorts? What dose, what effect, what evidence quality? If this population is largely unstudied,
state it and explain why that undercuts extrapolation from the TRD literature.

**C7. P4 — bipolar depression.** The separate evidence base: which trials, which bipolar subtype,
what doses, what effect sizes. Address critically:

- **Mood-stabilizer co-treatment.** If the trials required concurrent lithium or valproate, then
  their safety and efficacy findings do **not** transfer to unmedicated bipolar patients. Check
  this explicitly and state it.
- Manic and hypomanic switch rates, and whether the trials were powered or long enough to detect
  them.
- Whether esketamine is approved or contraindicated in bipolar depression, and what its labeling
  says.
- Whether antidepressant-induced switch risk generalizes to ketamine at all, given the different
  mechanism.

**C8. P5 — mixed features and agitated depression of uncertain polarity.** Has ketamine been
studied in mixed states or in agitated depression where polarity is unclear? Given standard
exclusion criteria this may be entirely empty. If so, say so — and spell out the consequence,
which is that the population most likely to present as "highly activated" is the population with
the least evidence and the most theoretical risk.

**C9. Dose × population interaction.** Pull C1–C8 together: does the optimal or safe dose band
differ by population? Is there any evidence that crisis-state or bipolar patients need, tolerate,
or are harmed by different doses than stable TRD patients? Distinguish tested interactions from
plausible-but-untested ones.

**Required deliverable: the matrix.** A table with dose bands D1–D5 as rows and populations
P1–P6 as columns. Each cell contains an evidence label and, where evidence exists, a one-line
summary with a citation marker. Empty cells stay visibly empty — do not fill them with inference,
and do not merge rows or columns to hide sparsity. A mostly-empty matrix is the correct output if
that is the state of the field.

## Phase 4 — Adversarial verification

Do not skip this phase. A prior research pass in this repository checked 109 citations and found
40 misstated — wrong pincites, overreached holdings, stale figures. Assume you have made errors
of the same kind.

For every quantitative claim and every citation in your draft, independently re-check:

1. The identifier resolves to a real publication.
2. The abstract or full text actually supports the specific claim you attached to it — not a
   weaker or adjacent claim.
3. The numbers (n, effect size, CI, p, timepoint, percentage) match the source exactly.
4. **Population match** — a finding in treatment-resistant MDD is not a finding in bipolar
   depression, in healthy volunteers, or in acute suicidal crisis.
5. **Dose and route match** — a 0.5 mg/kg IV finding is not a sublingual finding, and an
   esketamine finding is not a racemic finding.
6. **Time-window match** — a 24-hour outcome is not a 4-week outcome.

Delete or downgrade every claim that fails. **If a deletion leaves a section without support,
report the section as Unstudied rather than backfilling with weaker sources.** Report the count
of claims checked, revised, and deleted in the methods note — this is a quality signal for the
reader.

Then run the pre-commitment check from Phase 0: did any conclusion drift toward what you
expected to find? Name any that did and re-examine them.

## Phase 5 — Synthesis

Only after Phase 4, write the report.
</investigation_plan>

<central_tension>
Confront this directly rather than hedging around it; it is the question underneath all three
arms.

**The case for treating in crisis:** ketamine's entire clinical rationale is speed. Conventional
antidepressants take weeks; ketamine acts in hours. That property is _only_ valuable in a crisis.
An acute suicidal state is the one situation where waiting has the highest cost, and the
strongest ketamine evidence base sits precisely there.

**The case against treating in crisis:** the effect of a single course is measured in days to a
few weeks. Relapse is the norm without maintenance. If depression and anxiety are being
continuously regenerated by an ongoing adverse situation, a rapid-acting agent may buy a window
that closes onto an unchanged environment — with the added risks of an activated person in a
dissociative state, an unclear-polarity presentation, and instability undermining a monitored,
expensive treatment series.

Resolve this as far as the evidence permits and state clearly where it does not. Where you must
reason past the evidence to be useful, mark the reasoning as inference and label its confidence.
</central_tension>

<comparator_requirement>
"Is ketamine beneficial in crisis?" is only decision-useful relative to the alternatives. Include
a section comparing ketamine against what else is actually available in each crisis state:
crisis stabilization and safety planning, inpatient admission, ECT, benzodiazepines,
antipsychotics for agitation, and conventional antidepressant initiation. For each, note speed of
onset, evidence quality, and what it costs the person. Without this, "better than nothing" is the
only conclusion the report can support, and that is not the question being asked.
</comparator_requirement>

<failure_modes>
These are the specific ways this report is likely to go wrong. Guard against each explicitly, and
in the methods note state how you handled them.

1. **Motivated synthesis.** The reader has a stake in the answer. Do not assemble findings into
   the most useful-sounding conclusion. The Phase 0 pre-commitment and the Phase 4 drift check
   exist for this. Where the evidence supports an unwelcome answer, state the unwelcome answer.

2. **Surrogate-outcome inflation.** "Reduced scores on a suicidal-ideation scale at 24 hours" is
   not "prevents suicide." Never let the second sentence stand in for the first. Whenever you
   report an ideation outcome, state what was measured and over what window, in the same sentence.

3. **The crisis-indication tautology.** Trials that enrolled people in crisis tested crisis as an
   indication, not activation as a moderator. Do not answer A2 with A1's evidence. (See A2.)

4. **Population colonization.** TRD findings drifting into claims about healthy volunteers,
   ordinary depression, bipolar depression, or mixed states. The tagging requirement exists to
   make this visible; Phase 4 check 4 exists to catch it.

5. **Dose laundering across routes.** Milligram figures compared across IV, intranasal, and
   sublingual without a bioavailability adjustment. Phase 4 check 5.

6. **Sedation-dose contamination.** D5 agitation-management evidence presented as bearing on
   antidepressant or anxiolytic effect. See the firewall.

7. **Positive-result bias.** Report the trials that **failed** by name, including the short-term
   esketamine trials that missed their primary endpoints and any dose arms that did not separate
   from control. A dose-response section that reports only the doses that worked is a false
   picture of the dose-response.

8. **Undisclosed clinician-investigator interest.** Observational and real-world datasets are
   frequently authored by people who own or operate ketamine clinics. Note author affiliation and
   commercial interest where it exists, in the same way you note industry sponsorship.

9. **Both-sidesing via the "Contested" label.** When you mark something Contested, you must also
   state **which side has the stronger design** and why, or explain why the designs are genuinely
   comparable. Contested is not a way to avoid a judgment.

10. **Ecological fallacy.** Group-mean effect sizes from an RCT do not predict an individual's
    response. Where the report is most likely to be read as personal prediction — response rates,
    NNT, remission percentages — state explicitly that these are group statistics and name what
    they do and do not tell an individual.

11. **The report functioning as a green light.** This document must not resolve into an
    actionable recommendation, and must not be assemblable into a self-administration plan. Its
    job is to characterize evidence. Every path forward it describes routes through a prescriber.
    Take particular care with R4 (unsupervised at-home dosing) — the combination of that route
    with S4 instability is the highest-risk cell in the entire grid, and the report should be
    unambiguous about that regardless of what the efficacy evidence says.
    </failure_modes>

<sourcing_rules>

1. **Anchor on primary literature.** Prefer RCTs, individual-participant-data meta-analyses, and
   systematic reviews over narrative reviews. Cite the trial, not a news summary of it.
2. **Every efficacy claim carries its parameters.** Trial or first author, year, journal, n,
   comparator, dose and route, population, timepoint, effect size with CI where reported, and a
   resolvable identifier (PMID/DOI/NCT) as a link. An effect size without comparator, dose,
   population, and timepoint is not a usable claim — omit it rather than reporting it bare.
3. **Label design quality inline.** Open-label, uncontrolled, retrospective, preprint, and
   secondary/post-hoc analyses marked as such at the point of use, not only in a footnote.
4. **Flag funding and interest.** Industry sponsorship, particularly across the esketamine trial
   program; and clinician-investigator commercial interest in observational datasets.
5. **Report negative results.** Failed trials and non-separating dose arms named explicitly.
6. **Distinguish evidence from practice.** Clinic marketing, telehealth provider material,
   practitioner forums, and patient anecdote may be cited _only_ as documentation of practice
   patterns or of the access landscape, explicitly labeled as such. Never as evidence of efficacy
   or safety.
7. **Prefer recency where the field moves, but keep the pivotal older trials** — the foundational
   suicidality, dose-ranging, and bipolar trials remain the evidence base.
8. **Date every access, cost, and regulatory claim.** These go stale fastest.
   </sourcing_rules>

<uncertainty_protocol>
For several questions here — most likely A2, A7, B2, B3, B8, C6, and C8 — the honest answer is
that no trial has asked. **Say so.** A clearly stated "the evidence does not address this" is
more valuable to this reader than a confident-sounding inference, and far more valuable than a
plausible sentence attached to a citation that does not support it.

Use exactly these labels, consistently:

- **Established** — replicated RCT evidence, consistent direction.
- **Supported** — RCT evidence, limited replication or notable methodological limits.
- **Suggestive** — open-label, observational, post-hoc, or single-study only.
- **Contested** — credible evidence in opposing directions. Must name which side has the stronger
  design.
- **Unstudied** — no direct evidence located. Any statement is inference; mark it as such and say
  what would test it.

Never upgrade a label to make a section feel complete. A section that reads as thin because the
evidence is thin is doing its job.
</uncertainty_protocol>

<output_spec>
Write to `psychedelic-therapy/ketamine-dose-population-crisis.md`. Markdown. Roughly 6,000–8,500
words, weighted toward Phase 1–3 findings, not toward preamble.

Required structure:

1. **Header** — title, status, date, one-line scope statement, an explicit "literature review,
   not medical advice" line, and crisis resources.

2. **Bottom Line** (600–900 words) — numbered, direct answers to Arms A, B, and C as asked. No
   throat-clearing. If an answer is conditional, state the conditions in the first sentence.

3. **How to read this** — the S / R / D / P / T taxonomies as compact tables, plus the
   sedation-dose firewall warning and the route-bioavailability warning.

4. **Arm A — Ketamine in the acutely activated state** — A1–A8, each led by its evidence label.

5. **Arm B — Ketamine under unstable circumstances** — B1–B8. B1 must include the
   exclusion-criteria extraction table.

6. **Arm C — Dose-response across populations** — C1–C9, and **the D × P matrix**.

7. **Comparator section** — ketamine against the alternatives available in each crisis state.

8. **The central tension** — the synthesis required above.

9. **Evidence quality table** — one row per major claim: claim, state/route/dose/population tags,
   evidence label, best supporting source, principal limitation.

10. **Red flags and contraindications** — when the literature or guidelines say do not proceed, or
    stabilize something else first. Concrete and scannable. Must address the P5 polarity question
    and the R4 × S4 combination specifically.

11. **What would change this answer** — the specific trials, readouts, or personal-history facts
    that would move each conclusion, including what a prescriber would need to know about the
    individual that this report cannot know.

12. **Questions to bring to a prescriber** — 10–15 specific, answerable questions generated by the
    findings. Each must trace to something in the report. Include at least two on dose selection
    and two on polarity/bipolar screening.

13. **Where this updates `REPORT.md`** — explicit deltas, or "no contradictions found."

14. **Methods note** — Phase 0 pre-commitment as written, Phase 4 verification counts (checked /
    revised / deleted), the drift check result, and how each of the eleven failure modes was
    handled.

15. **Gaps and limitations** — what could not be resolved and why.

16. **Sources** — numbered, linked, grouped by topic, each with a one-line note on what it
    establishes and a flag for funding or author interest where applicable.

Formatting: tables for anything comparative. Bold the operative claim in a dense paragraph. No
em-dash-heavy padding, no restating the question before answering it.
</output_spec>

<constraints>
- Literature review for a person preparing to talk to a prescriber. Not medical advice; say so.
- No dosing protocols, sourcing guidance, or anything usable as instructions for unsupervised
  self-administration. Clinical trial doses may be reported as study parameters — that is
  description, not instruction, and the distinction must remain obvious in how they are presented.
- Include, once and without lecturing, standard crisis resources (988 Suicide & Crisis Lifeline;
  Crisis Text Line, text HOME to 741741) in the header block, given that S1 is squarely in scope.
- Do not soften a finding to be reassuring, and do not sharpen one to be cautionary. The reader's
  interest is served by accuracy in both directions.
- Report harms with the same rigor as benefits — same parameters, same evidence labels, same
  depth.
</constraints>

<self_check>
Verify each before returning; fix what fails.

- [ ] Arms A, B, and C each have a direct answer in the Bottom Line, in the first two sentences of
      their respective items.
- [ ] Every finding carries a state (S), route (R), dose (D), and population (P) tag, plus a time
      window where an effect is reported.
- [ ] The D × P matrix exists, and empty cells are visibly empty rather than filled with inference.
- [ ] No D5 sedation-dose evidence appears anywhere in an efficacy claim.
- [ ] A2 is not answered using A1's evidence.
- [ ] P1 (healthy volunteer) findings are reported in their own direction, not harmonized with P3.
- [ ] The bipolar section states whether trial patients were on mood stabilizers and whether
      findings transfer to unmedicated patients.
- [ ] P5 (mixed features / uncertain polarity) is addressed, including if the answer is that it is
      entirely unstudied.
- [ ] Failed trials and non-separating dose arms are named.
- [ ] Every efficacy claim carries n, comparator, dose, route, population, timepoint, and a
      resolvable identifier.
- [ ] Every claim carries one of the five evidence labels; every Contested label names which side
      has the stronger design.
- [ ] B1's exclusion-criteria table exists and directly answers whether the S4, P2, P4, and P5
      populations were ever studied.
- [ ] Phase 4 verification was actually performed; checked / revised / deleted counts reported.
- [ ] The Phase 0 pre-commitment is reproduced in the methods note and the drift check is reported.
- [ ] At least one section says Unstudied if that is true — a report with no gaps is a warning
      sign, not a strength.
- [ ] Harms are covered at the same depth as benefits.
- [ ] The report does not resolve into a recommendation, and the R4 × S4 risk is stated
    unambiguously.
</self_check>
