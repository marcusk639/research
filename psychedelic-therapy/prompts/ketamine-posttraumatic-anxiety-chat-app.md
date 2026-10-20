# Post-Traumatic Anxiety, SC Dosing, Dissociation — Claude Chat App Version (Research mode)

Chat-app port of `ketamine-posttraumatic-anxiety-deep-research.md` (the narrow, v3 scope).
Re-engineered for Research mode, not pasted across.

**How to use:**

1. **Start a NEW conversation.** Do not continue the earlier ketamine conversation — that one is
   saturated with suicidality trial material, and this scope excludes it. Continuing there will
   contaminate the answer.
2. Turn on **Research**. Paste **Prompt 1**. Expect 10–20 minutes and one long report.
3. Then paste **2A / 2B / 2C** as separate turns in the same conversation, in any order or not at
   all. Each is a fresh Research run inheriting the conversation context.
4. Fill the `[bracketed]` fields in Prompt 1 first, or delete the lines you don't want to share.
   The time-since-event field is the one that most changes which literature applies — fill it if
   you can.

**Why it's split.** Research mode spreads its search budget across the questions you ask. The Code
version asks 23; in chat that yields 23 shallow answers and a truncated report. Prompt 1 carries
your three actual questions. The follow-ups take depth with a fresh budget each.

---

## Prompt 1 — The three questions

```
I want a rigorous literature review, not advice and not reassurance. Research mode on.

<context>
I'm a non-clinician preparing for a conversation with a prescriber. I already know the general
psychedelic-therapy landscape — skip introductory framing.

My situation: I'm in a current psychological crisis triggered by a recent traumatic event. The
presentation is intense daily anxiety and recurrent states of panic. I have NO suicidality, no
suicidal ideation, and no violent thoughts or tendencies. I have a bipolar II diagnosis.
I'm specifically interested in subcutaneous administration.

Time since the traumatic event: [e.g. "6 weeks" — or delete this line]
Current medications: [including any mood stabilizer and any benzodiazepine — or delete]
Location: [state/region — or delete]
</context>

<hard_exclusions>
Read these before searching. They are scope boundaries, not preferences, and the first one is the
most likely thing to go wrong.

1. NO SUICIDALITY AS AN EFFICACY TOPIC. Do not research, report, or reason from ketamine's
   anti-suicidal effect, or from trials that enrolled people FOR active suicidal ideation, as
   evidence about my presentation. I am not suicidal; those trials do not describe me.

   ⚠️ This is the trap: most of the published "ketamine in acute crisis" literature IS
   suicidality research, and it will dominate your search results for terms like "ketamine
   crisis" and "ketamine acute." Do not let it fill the gap. Instead, give me a short explicit
   subsection saying so — that the crisis literature is predominantly suicidality literature,
   that it doesn't transfer to non-suicidal post-traumatic anxiety, and what evidence actually
   remains once it's set aside. Don't silently substitute it, and don't report "no evidence"
   without telling me why the apparent evidence was excluded.

   CARVE-OUT: suicidality stays in scope as a SAFETY signal — treatment-emergent or worsening
   ideation as an adverse event, and the boxed-warning language. Put that in the harms section,
   labeled as harm surveillance, not efficacy.

2. BIPOLAR II ONLY. Don't present bipolar I findings as applying to me. Several foundational
   bipolar ketamine trials pooled BD-I and BD-II — when you use one, say in the same sentence
   that it pooled them, give the BD-II proportion if reported, and give BD-II subgroup results or
   state that no subtype breakdown was published. A pooled result is not a BD-II result; if a
   claim rests only on pooled data, its ceiling label is Suggestive.

3. NO VIOLENT IDEATION / AGGRESSION as a target outcome. Only if it appears as an adverse-event
   signal.

4. SUBCUTANEOUS IS THE SUBJECT. IV is where nearly all dose-response knowledge was generated, so
   it can't be omitted — but every IV finding must be labeled IV, and its transferability to SC
   assessed rather than assumed. Mark any SC claim that actually rests on IV data as
   [IV-derived]. Intranasal and oral/sublingual appear only as comparators.
</hard_exclusions>

<my_questions>
**Q1 — Does it work for this presentation, and is the timing right?** Ketamine for post-traumatic
anxiety and panic in the weeks-to-months after the event. Does dosing close in time to a trauma
help, do nothing, or actively harm the trajectory?

**Q2 — Subcutaneous dose ranges.** At what SC dose or dose range does ketamine produce notable
psychological or physiological effects? What's the SC dose-response for anxiolytic and
antidepressant effect, and where does it sit against the side-effect curve?

**Q3 — Is dissociation required?** Do I have to reach a dissociative state to get the anxiolytic
and antidepressant benefit, or is dissociation a separable side effect?

Q2 and Q3 are linked, and the link is the interesting part: SC administration produces a lower
peak plasma concentration and a later Tmax than the same mg dose IV. If dissociation tracks peak
concentration while therapeutic effect tracks total exposure, SC could deliver benefit with less
dissociation. Treat that as a HYPOTHESIS TO TEST, not a conclusion to support — report what the
PK and clinical data actually show, including if they refute it.
</my_questions>

<tags>
Tag every finding on all of these. If you can't tag it, you don't understand it well enough yet.

TRAUMA RECENCY (the axis my question turns on):
TR1 <72h (memory still consolidating) · TR2 3d–1mo (acute stress disorder window) ·
TR3 1–3mo (early PTSD) · TR4 >3mo (chronic PTSD — where nearly all RCT evidence lives)
⚠️ TR4 evidence does NOT transfer to TR1–TR3. The chronic-PTSD trials enrolled people years out.

PRESENTATION: PR1 daily generalized anxiety · PR2 panic attacks/panic disorder ·
PR3 hyperarousal/re-experiencing · PR4 accompanying depression · PR5 life instability

ROUTE: R-SC subcutaneous (the subject) · R-IV (reference/comparator) · R-IM · R-IN intranasal
esketamine · R-SL sublingual/oral incl. at-home telehealth

DOSE: D1 <0.1 mg/kg · D2 0.1–0.4 · D3 ~0.5 · D4 0.75–1.0 · D5 >1.0
Give SC-specific mg/kg wherever the literature provides it. Mark IV-only bands [IV-derived].

POPULATION: P1 healthy volunteers · P2 primary anxiety disorders (GAD/SAD/panic) ·
P3 treatment-resistant MDD · P4 bipolar II only · P5 mixed features / uncertain polarity ·
P6 PTSD and acute stress disorder

TIME WINDOW IN A SESSION: T1 0–90 min (the drug experience — SC peaks later than IV, use the SC
timecourse where known) · T2 2–24h · T3 2–7d · T4 >7d
⚠️ T1 and T2 often point OPPOSITE directions — ketamine is commonly anxiogenic during the session
and anxiolytic a day later. For someone in daily panic that's not a footnote, it's a central
decision input. Report T1 on its own terms at every dose band.

FIREWALL: sedation/procedural-dose ketamine for agitation management (D5 territory, 4–5 mg/kg IM)
is a different drug at a different dose for a different purpose. One marked paragraph at most,
and never allowed to inform an anxiolytic or antidepressant claim.
</tags>

<sources>
These search terms surface a lot of commercial material. Source discipline matters more than usual.

Prioritize: PubMed/PMC primary trials and pharmacokinetic studies · Cochrane and systematic
reviews · trial registries read directly for eligibility criteria — ClinicalTrials.gov AND the
Australian New Zealand registry (ANZCTR), since much of the subcutaneous ketamine trial work is
Australian/New Zealand · FDA prescribing information · professional guidelines.

Ketamine clinic websites, telehealth provider pages, and practitioner blogs are NOT evidence.
Cite them only as documentation of what's being sold and at what price, labeled as such.

Name the trials that FAILED and the dose arms that did NOT separate from control. A dose-response
section listing only the doses that worked is a false picture of the dose-response.

Flag industry sponsorship, and flag when an author holds a ketamine formulation contract, patent,
or clinic ownership — this is common in the anxiety and SC literature and is rarely prominent.

Citations tell me where a claim came from, not what it says. So in the prose, every efficacy claim
needs: n, comparator, dose AND route, population, trauma-recency band where relevant, timepoint,
and effect size with CI where reported. Omit a claim rather than report it bare.
</sources>

<what_to_cover>
Weight your effort in this order. Depth on the first six beats coverage of all nine.

1. PERI-TRAUMATIC TIMING (Q1's hard part). Does ketamine given close in time to a trauma help or
   harm the trajectory? This literature genuinely conflicts across settings — burn, combat-
   casualty, and other acute-injury cohorts have reported findings in opposing directions.
   Present the conflict; don't resolve it prematurely. Explain the mechanism that makes timing
   live: fear extinction, memory reconsolidation, and the concern about an NMDA antagonist given
   while a traumatic memory may still be consolidating. Tag everything by TR band. Then answer
   directly: has ANY controlled trial deliberately dosed in TR1–TR3 for psychiatric benefit, or
   is the entire early-window literature incidental — analgesia and anesthesia cohorts looked at
   retrospectively?

2. ANXIETY AND PANIC AS TARGETS (PR1, PR2, P2). Controlled evidence for ketamine in panic
   disorder, GAD, and social anxiety — distinct from anxiety symptoms inside depression. This is
   where the subcutaneous dose-ranging work in refractory anxiety lives, so carry R and D tags
   carefully. Be blunt about design quality and put sample sizes in the text; much of this is
   small, single-group, or open-label, and at least one program has disclosed a commercial
   interest in ketamine formulations.

3. SC PHARMACOKINETICS vs IV. Bioavailability, Tmax, Cmax, and the parent-drug-to-norketamine
   ratio for SC vs IV at the same mg dose. Cite actual PK studies. This is the foundation for
   both the dose answer and the Q3 hypothesis — get the numbers right or say they aren't
   established.

4. SC DOSE-RESPONSE (Q2). Which trials gave ketamine subcutaneously, at what mg/kg, in what
   population, against what comparator, and what separated from control? Prioritize trials that
   randomized MULTIPLE SC doses against a common comparator over cross-trial comparison, which
   confounds dose with everything else. Where does notable benefit begin, and where do side
   effects start outpacing it? Give the anxiolytic and antidepressant curves separately if the
   evidence allows — they may differ in shape. Say whether the curve is monotonic, threshold-like,
   or inverted-U, and how confident that shape is.

5. IS DISSOCIATION REQUIRED (Q3). Four parts: (a) does dissociation MEDIATE response or merely
   correlate — report the original positive findings and their replication record with equal
   weight; (b) trials designed to separate the two, including sub-dissociative/low-dose regimens
   that did or didn't work and any design using an agent that blocks dissociation; (c) the
   ANXIOLYTIC case specifically — nearly all mediation work is about antidepressant effect, so if
   nobody has asked this separately for anxiety, say so; (d) test the PK hypothesis from my
   questions against #3 — does the SC concentration profile plausibly decouple dissociation from
   benefit, and is there direct evidence either way? Separate "mechanistically plausible" from
   "tested." End with an EXPLICIT VERDICT and its evidence label, not a summary of both positions.

6. THE ACUTE SESSION IN SOMEONE ALREADY PANICKING (T1). Tolerability when the person arrives
   anxious: dissociation, emergence phenomena, transient anxiety, blood pressure and heart rate.
   Use the SC timecourse where known — slower onset changes the subjective shape of the session.
   This is the most decision-relevant tolerability question for daily panic; treat it as a
   finding, not a side-effect list.

7. BIPOLAR II. What exists specifically for BD-II, applying the pooled-trial rule at every use.
   Then the thing that's usually buried: if the positive bipolar evidence was generated in
   patients REQUIRED to be maintained on therapeutic lithium or valproate, it does not transfer
   to someone unmedicated or differently medicated. Check this per trial and state it prominently.

8. MIXED FEATURES / UNCERTAIN POLARITY (P5). Daily anxiety and panic in a BD-II patient raises
   whether this is anxious depression or a mixed state. Has ketamine been studied in mixed
   features or agitated depression of uncertain polarity? If it's essentially unstudied — the
   likely answer — say so plainly and state the consequence.

9. WHAT THE SUICIDALITY EXCLUSION REMOVED. The short disclosure subsection described above. Put
   it where I won't miss it.
</what_to_cover>

<labels>
Use exactly these:

Established — replicated RCT evidence, consistent direction
Supported — RCT evidence, limited replication or notable limits
Suggestive — open-label, observational, post-hoc, single study, or pooled-only bipolar data
Contested — credible evidence both ways. You must also say WHICH SIDE HAS THE STRONGER DESIGN, or
  explain why they're genuinely comparable. "Contested" is not a way to avoid a judgment.
Unstudied — no direct evidence found. Anything you say is inference; mark it and say what would
  test it.

Several of these will likely come back empty — most plausibly #1 for deliberate early-window
dosing, #5c for anxiolytic-specific dissociation mediation, and #8 for mixed features. Say so.
"The evidence doesn't address this" is worth more to me than a confident-sounding inference. Never
upgrade a label to make a section feel finished. A report with no gaps would be a warning sign.
</labels>

<known_ways_this_goes_wrong>
• Smuggled suicidality evidence — the most likely scope violation, because it dominates the search
  results and it's tempting to fill the gap with it.
• Route laundering — IV dose-response reported as if it establishes SC dose-response. Most likely
  in #4, because that's where the data is. Mark [IV-derived].
• Timing laundering — chronic-PTSD evidence used to answer a question about dosing weeks out.
• Pooled-bipolar laundering — BD-I/II pooled results presented as BD-II results.
• Dissociation overreach — "it's required" and "it's irrelevant" are BOTH stronger than the
  evidence if stated flatly.
• Motivated synthesis — I'm currently suffering and I have a stake in the answer. Don't assemble
  findings into the most useful-sounding conclusion. If the evidence supports an unwelcome answer,
  give me the unwelcome answer.
• Ecological fallacy — response rates and remission percentages are group statistics. Where
  they'd read as personal prediction, say what they do and don't tell an individual.
• Green-lighting — don't resolve this into a recommendation, and don't produce anything
  assemblable into a self-administration plan. Every path forward routes through a prescriber.
</known_ways_this_goes_wrong>

<output>
~3,000–4,000 words. Lead with the answer. No preamble, no restating my questions back to me.

1. BOTTOM LINE — direct answers to the main question and to Q1, Q2, Q3. Conditions go in the
   first sentence, not the last.
2. WHAT THE EXCLUSIONS REMOVED — short, so I know the boundaries of what follows.
3. FINDINGS for items 1–9, each led by its evidence label and its TR/PR/R/D/P tags.
4. SC DOSE TABLE — columns: dose band | population | trial (n) | comparator | effect | side-effect
   profile | SC-native or [IV-derived]. This is the deliverable for Q2; don't bury it in prose.
5. DISSOCIATION VERDICT — one clearly marked subsection with an explicit answer and its label.
6. RED FLAGS — scannable. Must cover the peri-traumatic timing concern, the polarity/mixed
   question, the acutely anxiogenic session, and unsupervised at-home dosing.
7. WHAT WOULD CHANGE THIS ANSWER — including what a prescriber needs to know about me that this
   report can't.
8. QUESTIONS FOR MY PRESCRIBER — 10–15, each traceable to a finding above. At least three on SC
   dose selection, two on timing relative to the trauma, two on BD-II and polarity screening.
9. SELF-AUDIT — before finishing, re-open the primary sources behind your five most load-bearing
   numeric claims and confirm each: does the source say that number, for that population, at that
   dose AND ROUTE, at that timepoint? Report which you confirmed and which you couldn't. If a
   claim doesn't survive, delete it and mark the section Unstudied rather than backfilling with a
   weaker source. Also confirm explicitly that no suicidality-efficacy evidence and no
   BD-I-as-target evidence survived into the report, and say which of Q1/Q2/Q3 you answered least
   well and why.

Tables for anything comparative. Report harms at the same depth and rigor as benefits. Don't
soften a finding to be reassuring or sharpen one to be cautionary — I'm served by accuracy in both
directions. Write plainly and without alarm: don't add distress the evidence doesn't warrant, and
don't withhold a finding because it's unwelcome.

This is a literature review, not medical advice, and it doesn't replace a prescriber who knows my
full history.
</output>
```

---

## Follow-up 2A — SC delivery, safety, and dose-limiting effects

```
Go deeper on the practical and physiological side of subcutaneous administration. Fresh search,
same tags, labels, exclusions, and sourcing rules as before.

1. PHYSIOLOGICAL EFFECTS BY SC DOSE. Blood pressure and heart rate response, sedation depth,
   nausea, dizziness — dose-tagged, and using SC data rather than IV where it exists. What is
   dose-limiting in practice, and at what dose does it become so?

2. REPEATED AND SERIAL SC DOSING. Bladder and urinary symptoms, hepatic considerations, tolerance
   and dose escalation over a course. What's documented at what cumulative exposure, and over
   what duration of follow-up? Distinguish measured rates from asserted ones.

3. HOW SC IS ACTUALLY DELIVERED in the settings where it's been studied — supervised or not,
   observation period, titration schedule, single vs serial dosing, who administers it. Note
   where SC was chosen specifically to avoid IV access, and what monitoring intensity those
   protocols nonetheless assumed.

4. TREATMENT-EMERGENT ADVERSE PSYCHIATRIC EFFECTS. This is the safety carve-out: worsening
   anxiety, emergent or worsening suicidal ideation, activation, dissociative symptoms persisting
   past the session, derealization. Boxed-warning language. Report as harm surveillance.

5. UNSUPERVISED AT-HOME ROUTES (R-SL) — brief and unambiguous. Dose escalation, absence of
   monitoring, dependence, current regulatory status of compounded ketamine and telemedicine
   prescribing (date this — it moves), and documented harms.

6. Update the SC dose table from your first report with anything new, and tell me which rows
   changed or moved from [IV-derived] to SC-native.
```

---

## Follow-up 2B — Bipolar II, polarity, and who was actually enrolled

```
Go deeper on population. Fresh search, same rules — and hold the bipolar II exclusion strictly.

1. HYPOMANIC SWITCH AND ACTIVATION IN BD-II. Reported rates, and more importantly: were the
   trials powered or long enough to detect switch at all? Absence of a signal in small short
   trials is not evidence of safety. Cover repeated/serial dosing separately from single doses,
   and note whether any switch data exists for SC specifically.

2. THE MOOD-STABILIZER CONDITION, per trial. For each bipolar ketamine trial you cite: were
   patients required to be on therapeutic lithium or valproate? If yes, say what that does to
   transferability for someone not on one. This may be the single most consequential detail for
   me and it's routinely buried in methods sections.

3. WHO WAS ACTUALLY ENROLLED — the exclusion audit, re-scoped to my situation. Pull eligibility
   criteria directly from the registry records for the pivotal SC trials and the anxiety trials.
   Ask directly: were people with a RECENT TRAUMA, ACTIVE PANIC ATTACKS, ACUTE STRESS DISORDER,
   BIPOLAR II, or UNSTABLE LIFE CIRCUMSTANCES ever enrolled? Build a table. If the trials
   systematically excluded this presentation, that's the most important sentence you can write.

4. ANXIETY DISORDERS IN BIPOLAR II specifically. Comorbid anxiety is common in BD-II — has anyone
   studied ketamine for the anxiety component in a bipolar population, as opposed to the
   depressive component? If not, say so.

5. Given all of the above, revise your Bottom Line answer on population if it changed, and say
   what changed.
```

---

## Follow-up 2C — Alternatives, durability, and integration

```
Three remaining areas. Fresh search, same rules.

1. COMPARED TO WHAT. Ketamine against the alternatives actually available for post-traumatic daily
   anxiety and panic: trauma-focused CBT, prolonged exposure, EMDR, SSRI/SNRI initiation,
   prazosin, propranolol, and benzodiazepines. For each: onset, evidence quality, cost to the
   person. Table it.

   ⚠️ Give particular attention to BENZODIAZEPINES ADMINISTERED AFTER TRAUMA. That's the most
   likely thing to be offered for daily panic, and the literature on what it does to the PTSD
   trajectory is directly relevant to my decision. Report it carefully and with its evidence
   quality — including whether the finding is causal or confounded by indication.

2. DURABILITY UNDER AN UNRESOLVED SITUATION. Relapse timelines after single vs serial SC dosing.
   What maintains response. Then the mechanistic question directly: if ketamine opens a window of
   neuroplasticity, what does the evidence say happens when that window closes onto an unresolved
   traumatic situation or ongoing life instability? Separate what's been tested from what's
   inferred — I'd rather have "nobody has tested this" than a confident mechanism story.

3. KETAMINE PLUS PSYCHOTHERAPY IN THE POST-TRAUMATIC WINDOW. Does structured therapy during the
   post-dose period change durability? Does the trauma-processing literature have anything to say
   about combining them? Note the tension with the timing question: if dosing near a trauma is
   mechanistically risky for memory consolidation, does adding trauma-focused therapy in that
   window mitigate the risk or compound it? Say clearly if this is untested.

4. Close by revising your original Bottom Line if anything across 2A/2B/2C changed it, and tell me
   specifically what changed and why.
```
