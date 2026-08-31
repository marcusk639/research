# Ketamine Research — Claude Chat App Version (Research mode)

Companion to `ketamine-crisis-context-deep-research.md`, which targets the Claude Code
`deep-research` skill. This version is re-engineered for the chat app, not ported.

**How to use:**

1. Open a new conversation in the Claude app and turn on **Research**.
2. Paste **Prompt 1**. Expect a long run (10–20 min) and a single large report.
3. Then paste follow-ups **2A / 2B / 2C** as separate turns in the same conversation, in any
   order or not at all. Each is its own focused Research run that inherits the conversation's
   context.
4. Before pasting, fill the `[bracketed]` fields in Prompt 1's context block, or delete the
   lines you don't want to share.

**Why it's split.** Research mode allocates search effort roughly across the questions you ask.
The Code version asks 25 — in chat that yields 25 shallow answers and a truncated report.
Prompt 1 carries the questions that most directly answer the two original questions; the
follow-ups take the deeper cuts with a fresh budget each.

---

## Prompt 1 — Main research run

```
I want a rigorous literature review, not advice and not reassurance. Research mode on.

<context>
I'm a non-clinician preparing for a conversation with a prescriber about ketamine. I've
already read the general landscape material on psychedelic-assisted therapy, so skip the
introductory framing — assume I know what esketamine is, that it's the only FDA-approved
option in this category, and that the field has serious methodological problems with
functional unblinding and bundled psychotherapy.

Relevant history I'm willing to share: [e.g. diagnoses, current medications, prior ketamine
or psychedelic experience — or delete this line]
- Bipolar type 2
- Anxiety disorder
- OCD
- Complex PTSD

What I actually want to know is narrower than "does ketamine work."
</context>

<questions>
Three questions.

**A — Acute state.** Does ketamine deliver antidepressant and anxiolytic benefit when the
person is, at the moment of dosing, in acute psychological crisis or a highly activated
state — intense anxiety, panic, agitation, acute suicidality? Is that state a reason to
proceed, a reason to wait, or irrelevant to the pharmacology?

**B — Circumstantial context.** Does it deliver benefit when someone's external life
circumstances are unstable and in crisis — housing, finances, employment, legal exposure,
relationships, active loss? Does instability moderate response, durability, or harm?

**C — Dose and population.** How do effects on depression and on anxiety vary by dose range,
and does that dose-response differ across populations: people with no psychiatric diagnosis,
people with ordinary non-treatment-resistant depression or anxiety, people with
treatment-resistant depression, people with bipolar type 2 disorder, and people in acute crisis?
Is the curve the same for depression, for anxiety, and for suicidality?
</questions>

<how_to_keep_these_apart>
The way this goes wrong is collapsing distinct things into one word. Tag every finding you
report with all four axes. If you can't tag a finding on all four, you don't understand it
well enough to report it.

STATE: S1 acute suicidal crisis · S2 acute activation (agitation, panic, hyperarousal) ·
S3 peri-traumatic, days-to-weeks post-trauma · S4 chronic life instability ·
S0 stable outpatient baseline (what nearly every trial actually studied)

ROUTE: R1 IV racemic · R2 IM · R3 intranasal esketamine · R4 sublingual/oral at-home
telehealth · R5 subcutaneous

DOSE, anchored to IV racemic mg/kg: D1 <0.1 · D2 0.1–0.4 (sub-dissociative) ·
D3 ~0.5 over 40 min (the pivotal-trial reference dose) · D4 0.75–1.0 ·
D5 >1.0 IV or 4–5 IM (procedural sedation — see firewall below)

POPULATION: P1 healthy volunteers · P2 ordinary non-treatment-resistant depression or a
primary anxiety disorder · P3 treatment-resistant MDD · P4 bipolar type 2 depression ·
P5 mixed features or agitated depression of uncertain polarity · P6 acute crisis presentation

TIME WINDOW: T1 0–60 min (the drug experience itself) · T2 2–24 h · T3 2–7 days · T4 >7 days

Two hard rules from these:

FIREWALL. D5 sedation-dose ketamine for prehospital or ED agitation is a different drug at a
different dose for a different purpose. You may discuss it in one clearly marked paragraph
because it's technically "ketamine in an activated person," but never let it inform an
antidepressant or anxiolytic claim. News coverage conflates these constantly.

ROUTE ≠ DOSE. Sublingual and oral bioavailability is a fraction of IV. A milligram number is
meaningless across routes. If you compare doses between routes, state and cite the
bioavailability assumption; if the source doesn't support the conversion, say so instead of
estimating.
</how_to_keep_these_apart>

<sources>
Research mode will surface a lot of commercial material for these search terms. Source
discipline matters more here than usual.

Prioritize: PubMed/PMC primary trials · Cochrane and other systematic reviews ·
ClinicalTrials.gov records (use these directly to read eligibility criteria verbatim) ·
FDA prescribing information and REMS documents · professional guidelines (APA, CANMAT,
NICE, VA/DoD).

Ketamine clinic websites, telehealth provider pages, and practitioner blogs are NOT evidence.
Cite them only as documentation of what's being sold and at what price, labeled as such.

Report the trials that FAILED, by name — including short-term esketamine trials that missed
their primary endpoints and dose arms that didn't separate from control. A dose-response
section that names only the doses that worked is a false picture of the dose-response.

Flag industry sponsorship. Also flag when an observational dataset is authored by people who
own or operate ketamine clinics — common in this literature and rarely disclosed prominently.

Citations tell me where a claim came from; they don't tell me what it says. So for every
efficacy claim, give me in the text: n, comparator, dose and route, population, timepoint,
and effect size with CI where reported. An effect size without those is not usable — omit it
rather than reporting it bare.
</sources>

<what_to_cover>
Weight your effort roughly in this order. Depth on the first six beats coverage of all ten.

1. ACUTE SUICIDAL CRISIS (S1). Does ketamine reduce suicidal ideation faster and further than
   active comparator, and for how long? Cover: effect on ideation independent of depression
   change; durability past 72h and past a week; whether ANY trial is powered for attempts or
   deaths rather than ideation scales; head-to-head vs ECT and vs midazolam; and for the
   esketamine-plus-standard-of-care suicidality trials, what the control arm actually
   received and what that does to the observed increment.

2. ACTIVATION AS A MODERATOR (S2). Does high baseline anxiety, agitation, or arousal predict
   better, worse, or equal response? Cover the anxious-depression subtype literature.
   ⚠️ Do NOT answer this using #1's evidence. Trials in acutely suicidal patients tested
   crisis as an INDICATION; they did not test activation as a MODERATOR. If no true moderator
   analysis exists, the answer is Unstudied — say that.

3. THE SESSION ITSELF (T1), by dose band. Ketamine is commonly anxiogenic and dissociating
   during the infusion while being anxiolytic at 24h. Those are opposite signs and both are
   real. Report T1 effects on their own terms at each dose band — an aversive acute experience
   is a genuine cost even when the T2 outcome is good, and it's the most decision-relevant
   thing for someone who is already panicking. Include hemodynamic response and emergence
   phenomena, and whether peri-infusion dissociation actually predicts antidepressant response
   (report the original finding AND the replication record — don't present a contested
   correlation as mechanism).

4. DOSE-RESPONSE, three separate curves. Across D1–D4: for depression, for anxiety, and for
   suicidality. These may not share a shape. Prioritize actual dose-ranging RCTs that
   randomized multiple doses against a common comparator over cross-trial comparison, which
   confounds dose with everything else. Is it monotonic, flat above a threshold, or
   inverted-U? Include dose-escalation work in refractory anxiety disorders.

5. BIPOLAR TYPE 2 (P4, P5). The separate evidence base — which trials, which subtype, what doses,
   what effects. Then three things that are usually buried:
   • Were trial patients required to be on lithium or valproate? If so, the safety and
     efficacy findings do NOT transfer to unmedicated bipolar type 2 patients. Check and state this.
   • Manic/hypomanic switch rates — and whether the trials were powered or long enough to
     detect them.
   • P5: has ketamine been studied in mixed features or agitated depression of uncertain
     polarity at all? This is the population most likely to present as "highly activated,"
     and I expect it's been excluded from everything. If so, say so plainly and say what
     follows from it.

6. WHO WAS ACTUALLY STUDIED. Pull the exclusion criteria from the pivotal ketamine and
   esketamine trials — use the ClinicalTrials.gov records directly. Specifically: active
   substance use disorder, unstable housing, active suicidality, bipolar type 2 diagnosis, psychotic
   features, concurrent benzodiazepines, inability to attend a monitored series. Build a
   table. Then answer straight: has anyone in circumstances resembling S4, or in populations
   P2, P4, or P5, actually been studied? If the evidence base systematically excluded the
   people I'm asking about, that's the most important thing you can tell me.

7. HEALTHY VOLUNTEERS (P1). What do controlled studies show ketamine does to mood and anxiety
   in people with no psychiatric diagnosis, by dose? Expect this to be largely
   psychotomimetic-model research — i.e. pointing the OPPOSITE direction from the patient
   literature. Report that asymmetry honestly and say what it implies. Popular accounts omit
   this entirely.

8. DURABILITY UNDER ONGOING STRESS. Relapse timelines after single vs serial dosing. What
   maintains response — maintenance dosing, oral antidepressant continuation, structured
   therapy in the post-dose window. Then the mechanistic question directly: if ketamine opens
   a window of neuroplasticity, what does the evidence say happens when that window closes
   onto an unchanged adverse environment?

9. CONTRAINDICATIONS AND SCREENING for an activated presentation. Emerging mania read as
   agitation; psychosis history; uncontrolled hypertension; capacity and informed consent in
   an acutely suicidal person consenting to a dissociative drug; and whether concurrent
   benzodiazepines blunt the antidepressant effect — which matters because people in crisis
   are disproportionately on them.

10. COMPARED TO WHAT. Ketamine against the alternatives actually available in a crisis:
    crisis stabilization and safety planning, inpatient admission, ECT, benzodiazepines,
    antipsychotics for agitation, conventional antidepressant initiation. Speed of onset,
    evidence quality, what each costs the person. Without this the only supportable
    conclusion is "better than nothing," which isn't my question.
</what_to_cover>

<label_every_claim>
Use exactly these, consistently:

Established — replicated RCT evidence, consistent direction
Supported — RCT evidence, limited replication or notable limits
Suggestive — open-label, observational, post-hoc, or single study
Contested — credible evidence pointing both ways. You must also say WHICH SIDE HAS THE
  STRONGER DESIGN, or explain why they're genuinely comparable. "Contested" is not a way to
  avoid a judgment.
Unstudied — no direct evidence found. Anything you say is inference; mark it as inference and
  say what would test it.

Never upgrade a label to make a section feel finished. For several of these questions —
especially #2, #5's P5 sub-question, and #7 — the honest answer may be that nobody has asked.
Say so. "The evidence doesn't address this" is worth more to me than a confident-sounding
inference, and far more than a plausible sentence attached to a citation that doesn't support
it. A report with no gaps in it would be a warning sign, not a strength.
</label_every_claim>

<known_ways_this_goes_wrong>
Guard against each of these explicitly:

• Motivated synthesis. I obviously have a stake in the answer. Don't assemble findings into
  the most useful-sounding conclusion. Where the evidence supports an unwelcome answer, give
  me the unwelcome answer.
• Surrogate-outcome inflation. "Reduced scores on an ideation scale at 24 hours" is not
  "prevents suicide." Whenever you report an ideation outcome, say what was measured and over
  what window in the same sentence.
• The crisis-indication tautology. See the warning in #2.
• Population colonization. TRD findings drifting into claims about healthy volunteers,
  ordinary depression, bipolar type 2, or mixed states.
• Dose laundering. Milligram figures compared across routes without a bioavailability
  adjustment.
• Ecological fallacy. Response rates, NNT, and remission percentages are group statistics.
  Where they're most likely to read as personal prediction, say explicitly what they do and
  don't tell an individual.
• Green-lighting. Don't resolve this into a recommendation, and don't produce anything
  assemblable into a self-administration plan. Every path forward routes through a prescriber.
  Be especially unambiguous about R4 × S4 — unsupervised at-home sublingual dosing during a
  period of life instability is the highest-risk combination in this whole grid, regardless of
  what the efficacy evidence says.
</known_ways_this_goes_wrong>

<output>
~3,000–4,000 words. Lead with the answer — no preamble, no restating my question back to me.

1. BOTTOM LINE — numbered, direct answers to A, B, and C. If an answer is conditional, put the
   condition in the first sentence.
2. Findings for items 1–10, each led by its evidence label and its S/R/D/P tags.
3. DOSE × POPULATION MATRIX — dose bands D1–D5 as rows, populations P1–P6 as columns, each
   cell holding an evidence label and a one-line summary where evidence exists. Leave empty
   cells visibly empty. Don't fill them with inference and don't merge rows or columns to hide
   sparsity. A mostly-empty matrix is the correct output if that's the state of the field.
4. RED FLAGS — when the literature or guidelines say don't proceed, or stabilize something
   else first. Scannable. Must cover the polarity question and R4 × S4 specifically.
5. WHAT WOULD CHANGE THIS ANSWER — including what a prescriber would need to know about me
   that this report can't.
6. QUESTIONS FOR MY PRESCRIBER — 10–15 specific ones generated by your findings, each
   traceable to something above. At least two on dose selection, at least two on bipolar type 2 and
   polarity screening.
7. SELF-AUDIT — before you finish, re-open the primary sources behind your five most
   load-bearing numeric claims and confirm each one: does the source say that number, for that
   population, at that dose and route, at that timepoint? Report which ones you confirmed and
   which you couldn't. If a claim doesn't survive, delete it and mark the section Unstudied
   rather than backfilling with a weaker source. Also note which of my three questions you had
   to leave least well answered, and why.

Tables for anything comparative. Report harms at the same depth and with the same rigor as
benefits. Don't soften a finding to be reassuring or sharpen one to be cautionary — I'm served
by accuracy in both directions.

This is a literature review, not medical advice, and it doesn't replace a prescriber who knows
my full history.
</output>
```

---

## Follow-up 2A — Dose-response deep dive

Paste in the same conversation after Prompt 1 lands.

```
Go deeper on dose, with a fresh search. Same tagging, labeling, and sourcing rules as before.

1. DOES DISSOCIATION MEDIATE THE BENEFIT, OR JUST ACCOMPANY IT? This is the crux of the whole
   dose question: if dissociation is mechanistically necessary, sub-dissociative regimens
   can't work; if it's a separable side effect, they can. Give me the mediation analyses, and
   any trials designed to separate the two — dissociation-blocking comparators, active
   controls that mimic dissociation, non-dissociating NMDA agents. Where does the field
   actually stand? Don't pick a side the evidence hasn't picked.

2. P2 — ORDINARY PATIENTS. Has ketamine been tested in first- or second-line depression, or in
   primary anxiety disorders, as opposed to treatment-resistant cohorts? What dose, what
   effect, what design quality? If this population is essentially unstudied, say so and spell
   out how much that undercuts extrapolating the TRD results to an ordinary patient.

3. RACEMIC VS ESKETAMINE POTENCY. Is there a settled conversion between IV racemic mg/kg and
   intranasal esketamine 56/84 mg? If the field hasn't settled it, say so rather than
   supplying a number. What do the head-to-head comparisons show?

4. DOSE × POPULATION INTERACTION. Any evidence that crisis-state or bipolar type 2 patients need,
   tolerate, or are harmed by different doses than stable TRD patients? Separate tested
   interactions from plausible-but-untested ones.

5. Update the D × P matrix from your first report with anything new, and tell me which cells
   moved.
```

---

## Follow-up 2B — Instability, access, and the at-home question

```
Go deeper on Arm B, fresh search, same rules.

1. PSYCHOSOCIAL INSTABILITY AS A MODERATOR. Socioeconomic status, employment, social support,
   recent life events, childhood adversity as predictors of ketamine response or relapse. The
   childhood-adversity literature may point somewhere counterintuitive — report it as found,
   not as expected.

2. REACTIVE AND SITUATIONAL DISTRESS. Any ketamine evidence for adjustment disorder, grief,
   demoralization, or depression clearly secondary to ongoing adversity — as opposed to the
   treatment-resistant MDD the trials enrolled? Include the demoralization and palliative-care
   work. If the answer is essentially none, say so and say what follows.

3. AT-HOME TELEHEALTH KETAMINE (R4) — the highest-risk cell, so be concrete. Dose escalation,
   dependence, diversion, absence of monitoring, urological toxicity at sustained cumulative
   doses, and the current regulatory status of compounded ketamine and telemedicine
   prescribing (date this — it changes). What is the MEASURED rate of misuse in clinical vs
   non-clinical use, as opposed to the asserted rate?

4. THE SUBSTANCE-USE TENSION. Active SUD is a standard trial exclusion and instability
   correlates with substance use — yet ketamine also has controlled evidence as a TREATMENT
   for alcohol use disorder. Lay out the tension and what distinguishes the two situations
   clinically.

5. ACCESS UNDER FINANCIAL STRAIN. Cost per session, insurance posture toward esketamine vs
   racemic, REMS burden (observation period, driving restriction, accompaniment), and what
   happens if a series is started and not finished — documented risk, or only forgone benefit?
   What about discontinuation after maintenance: relapse trajectory, and is any rebound or
   withdrawal phenomenon documented? Date every cost and regulatory claim.

6. IS "STABILIZE FIRST" A REAL STANDARD OR CLINICAL FOLKLORE? Under what documented conditions
   do guidelines or clinicians defer ketamine pending psychosocial stabilization, versus
   deploy it AS the stabilizer? Find the sourced position. If it turns out to be folklore with
   no evidence base, say that.
```

---

## Follow-up 2C — Trauma timing, anxiety disorders, and guidelines

```
Three remaining areas, fresh search, same rules.

1. PERI-TRAUMATIC ADMINISTRATION (S3). Does ketamine given close in time to a trauma help or
   harm the PTSD trajectory? This literature points in opposite directions across settings —
   burn, combat-casualty, other acute-injury cohorts. Present the conflict rather than
   resolving it prematurely, and explain the fear-extinction / memory-reconsolidation
   mechanism that makes timing theoretically live. Keep this sharply separate from ketamine
   for CHRONIC PTSD, which has its own RCT base and doesn't transfer.

2. ANXIETY DISORDERS AS TARGETS IN THEIR OWN RIGHT. Controlled evidence for ketamine in panic
   disorder, GAD, or social anxiety — as distinct from anxiety symptoms inside depression. Be
   blunt about design quality; much of this is open-label.

3. SET AND SETTING, FOR KETAMINE SPECIFICALLY. The classic-psychedelic set-and-setting
   literature is large; the ketamine-specific one is much smaller. Tell me what exists FOR
   KETAMINE, including the ketamine-assisted-psychotherapy practice literature, and say
   plainly where the field is extrapolating from psilocybin rather than measuring ketamine.
   Does pre-session psychological state predict outcome in any controlled ketamine study?
   Include expectancy and prior psychedelic/dissociative experience as candidate moderators.

4. GUIDELINES. What do APA, CANMAT, NICE, VA/DoD, and emergency-medicine bodies actually say
   about ketamine in acute crisis? Quote the operative language. Where they're SILENT, say so
   — silence is a finding, and I'd rather know a guideline declines to address this than see
   it paraphrased into a position it doesn't hold.

Close by revising your original Bottom Line if anything across 2A/2B/2C changed it, and tell
me specifically what changed and why.
```
