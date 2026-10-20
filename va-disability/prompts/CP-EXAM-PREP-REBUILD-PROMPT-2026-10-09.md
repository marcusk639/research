# Prompt: Rebuild the C&P Exam Prep Doc from the Full Corpus

> Created 2026-10-09 · Run from `~/dev/research/va-disability/` · Output: `planning-docs/CP-EXAM-PREP-2026-10-13.md`
> Paste everything below the line into a fresh Claude Code session.

---

<goal>
Write one self-contained prep document for my VA mental-health C&P exam. It should cover what the exam will actually be like and how I should prepare for it, grounded in everything in `va-disability/` that is current, plus outside research on how these exams are run. When the exam starts I should be able to put every other prep file away and use only this one.

The goal is an **accurate, complete, consistent** account of how I actually function. The doc helps me give one. It does not help me perform. An MST claim's service connection rests on credibility. Dr. Howard has the claims file, so answers that match the record (or openly correct it) count for more than any single symptom.
</goal>

<exam>
- Tuesday 2026-10-13, 12:00 PM Central, VES TeleC&P (doxy.me), VES# 227264947760
- Examiner: Kasi Howard, PsyD (psychologist, Texas-licensed). I'll be in Texas.
- Conditions: PTSD (MST, 2012, perpetrator a coworker's civilian wife), MDD, GAD, OCD, SUD secondary to PTSD. Tinnitus already service-connected at 10%.
- VSO: James York. Treating therapist: Cherie Mills (CPT).
- This is a supplemental claim. Failure to report without good cause means the claim "shall be denied" (38 CFR 3.655(b)).
</exam>

<source_precedence>
This corpus has drifted and contradicts itself, and a past drafting pass produced three CRITICAL errors by trusting the wrong file. Resolve conflicts like this:

1. **Facts I gave on 2026-10-08 and 2026-10-09 come first** (recorded in the files below and in this prompt's `<recent_facts>`).
2. Then files by **last-modified date / internal dates, newest first**. Start with:
   - `planning-docs/CP-EXAM-PREP-MENTAL-HEALTH.md` (updated 10/9): current exam guidance; this new doc supersedes it
   - `planning-docs/REASSESSMENT-2026-10-08-CP-EXAM.md`: read the evening and late updates. They supersede its §2 odds.
   - `planning-docs/PATH-TO-100-WITHOUT-TDIU-2026-10-08.md`, `planning-docs/RECORDS-TO-GET-AND-PATHS-TO-100-2026-10-08.md`
   - `planning-docs/CLAIM-RECONCILIATION-WORKLIST.md`: open discrepancies, including retractions marked inline
   - `planning-docs/RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md`: newer than MASTER-STRATEGY and reverses it (TDIU)
   - the most recent `COMPREHENSIVE-FINDINGS-*.md`, for facts already reconciled
   - `CLAIM-ASSESSMENT.md` §0 (the coached-statement risk and SI retraction)
3. Primary evidence beats any analysis of it: `supporting-docs/` (signed statements, Cherie's letter and CPT progress notes, buddy statements, employer documents) and `personal-records/` (clinical records, the 21-0781, the 21-4138s, overdose records).
4. Treat these as stale history and don't use them as authority: `REPORT.md`'s "Start here" (it still recommends a 90% mental-health route, but **38 CFR 4.130 has no 90% level**), `MASTER-STRATEGY.md`, `PATH-TO-100-PERCENT-2026-07-07.md`, `100-PERCENT-SCHEDULAR-PATHWAY.md`, `knowledge-base.md`, `veteran-profile.md`, `strategy.md`, `CLAIM-EXECUTION-PLAN.md`, `DO-THIS-WEEK.md`, and anything marked `[SUPERSEDED]` or `[RETRACTED]`.

When two sources disagree and the rules above don't settle it, don't pick one. List it under "Unresolved — ask me or James" with both sources cited.
</source_precedence>

<recent_facts>
Settled with me on 10/8–10/9. These override older documents:
- **Overdoses 8/4 and 8/5/2026:** caused by 7-OH (concentrated kratom) at toxic doses. At the hospital I understated my usage and my SI, so the hospital records (gabapentin "accidental," "no SI") are inaccurate. **I uploaded my own 21-4138 about this to the VA portal on 10/9.**
- **Pre-service substance use:** kratom from about age 18. It was legal and sold in stores, and I didn't know it was an opioid. I don't recall any cocaine before service. A correction 21-4138 is drafted but not yet filed (status checklist in CP-EXAM-PREP-MENTAL-HEALTH.md).
- **Persecutory belief:** a recurring worry that started after service, not a fixed delusion. The "grandiose" belief is ordinary self-belief, not a symptom.
- **Family:** relations with my brother and both parents are strained, with little contact.
- **The ~6/25/26 SI denial does not exist** (retracted).
- **2012 is the correct year of the incident.** Whether I was 22 or 23 depends on the month; flag it, don't decide it.
</recent_facts>

<exclusions>
Don't read this prompt file, anything in `prompts/` or `personal-records/prompts/`, `.remember/`, or the output file itself. They would feed the run its own instructions or output.
</exclusions>

<research>
Use the `deep-research` skill (standard mode; the exam is days away) for the parts of the exam the corpus can't answer. Cite every claim:
- How a VES TeleC&P initial PTSD exam runs: length, structure, what the examiner reviews beforehand, the order of questions, and whether the examiner can stop or reschedule (for example over location, intoxication, or technical failure).
- What the current Initial PTSD DBQ and Mental Disorders DBQ ask: the Criterion A–H walkthrough, the MST-specific markers under 38 CFR 3.304(f)(5), the occupational/social impairment checkbox levels, and the suicide-risk fields.
- Which psychometric instruments tele-exams commonly use (PCL-5, CAPS-5, PHQ-9, validity measures such as the M-FAST, SIMS or MMPI-2-RF/3 if given remotely) and how symptom-validity results affect how much weight the exam gets. Explain this so I understand why careful, honest answers matter. Don't give tips for "passing" validity scales.
- How examiners and raters handle delayed MST disclosure, inconsistent SI reporting, co-occurring SUD (*Allen*, *Mittleider*), and the gap between how someone presents on camera and how they function. Prefer VA's own sources (M21-1, the DBQ forms, 38 CFR, VES/VA exam pages) and BVA decisions over blogs.
- Anything that changed in 2025–2026 for contract exams, including the cross-state licensure item already flagged as UNVERIFIABLE in the reassessment.

Before any citation goes in the doc, run the `citation-verifier` agent on every legal citation (CFR, USC, case law, M21-1). Label anything it can't confirm as UNVERIFIED, or drop it.
</research>

<constraints>
These protect the claim, so each one comes with its reason:
- **No scripted answers.** Give *what to cover* and *the true facts from my file* for each likely question, never sentences to recite. Scripted answers sound rehearsed, and if they drift from the truth they become false statements to a federal examiner.
- **Never write or suggest wording for a witness** (Erica, Reyes, Poquette, Goff) or a clinical judgment for Cherie. Flag the issue and name who owns it. Coached statements are the single biggest credibility risk in this file (`CLAIM-ASSESSMENT.md` Part 0; 38 U.S.C. § 6103 forfeiture exposure).
- **Accuracy over impact.** Where my documents overstate something ("feeds me," "cuts my hair," "delusions," "every day for years," "FMLA at every job"), say what's actually supported. Where I tend to minimize, say that too. Don't add or inflate symptoms.
- **Safety first.** The doc includes 988 (press 1) / text 838255, keeps the "be sober for the exam, and get medical help to taper 7-OH rather than stopping cold" guidance, and treats current SI as something to answer truthfully on the day.
- **PHI:** quote only what the prep needs, and don't copy `personal-records/` content anywhere outside this repo.
- Plain language, written to me in the second person. I'll be reading it stressed.
</constraints>

<output_format>
`planning-docs/CP-EXAM-PREP-2026-10-13.md`, with a status header (date, sources read, what it supersedes), then:

1. **One-page summary:** the 5–7 things that matter most, plus the before-Tuesday checklist with owners (me / James / Cherie / VES), including what to confirm VA has received (both 10/7 21-4138s, the overdose 21-4138, the kratom correction, which nexus letters, employer documents, Erica's statement, CPT notes).
2. **What the exam will be like:** logistics, sequence, the DBQ sections, the testing, how long it takes, and what happens afterward (requesting the DBQ). Cited.
3. **Your record at a glance:** a facts-only timeline (service, the 2012 incident, every disclosure with its date, treatment admissions, jobs with start/end dates and how each ended, the overdoses, every filing). Each line cites its source file. This is for my reference, not a script.
4. **Discrepancies the examiner may raise:** a table with the item, what each record says (with citations), whether a correction is filed or pending, and the honest way to handle it. At minimum: the disclosure timeline (C3), single incident vs. a year of harassment (H1), the SI denials, pre-service use (Victory vs. Starlite), the overdose records, the perpetrator's status, the marriage/ADL characterization, layoffs vs. terminations, the Mountain end date, the age at the incident, gaming, and the two Recover PsychEvals.
5. **Likely questions by DBQ domain:** for each, what the examiner is assessing, the true facts from my file, and what to make sure gets said (worst and typical days, frequency, concrete examples).
6. **Testing and validity:** why careful, honest answers protect the exam.
7. **Exam-day setup:** alone, a private room, ID, medication list, joining early, what to do if the video fails, Erica's role only if the examiner asks for her.
8. **After the exam:** request the DBQ, the scenario lanes (from REASSESSMENT §3), the sleep apnea ITF, and raising TDIU with James.
9. **Unresolved — ask me or James.**
10. **Sources:** corpus files read and external sources with verification status.
</output_format>

<done_when>
- Every factual claim about me cites a corpus file, and every external claim cites a source the citation-verifier confirmed or that is labeled UNVERIFIED.
- Run the `claim-consistency-checker` agent on the finished doc against the corpus. Fix any contradictions it finds where the fix is clear; move the rest to section 9.
- None of the stale or retracted positions in `<source_precedence>` item 4 or `<recent_facts>` appear as current, including any 90% mental-health level or the 6/25 denial.
- The doc contains no wording for any witness and no recitable answer scripts.
- Add a dated line at the top of `CP-EXAM-PREP-MENTAL-HEALTH.md` pointing to the new doc as its replacement. Change nothing else in the corpus.
- End by telling me, in a few lines, what's still open before Tuesday.
</done_when>
