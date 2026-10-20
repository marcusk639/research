# Prompt: In-Exam Reference Notes for the PTSD/MST C&P Exam

> Created 2026-10-12 · Run from `~/dev/research/va-disability/` · Output: `planning-docs/CP-EXAM-NOTES-2026-10-13.md` (+ `.pdf`)
> Paste everything below the line into a fresh Claude Code session. Expect a long run; start it tonight, not the morning of the exam.

---

<goal>
I have a VA mental-health C&P exam tomorrow. Read the entire `va-disability/` corpus until you understand my PTSD/MST claim completely: the history, the evidence, the corrections I've filed, the open discrepancies, and what the examiner will be trying to determine. Then write a short set of notes I can keep beside me during the exam.

The notes are reminders, not a script. VA lets a veteran bring a short list (medications, key dates, recent examples to mention) but expects answers in their own words. Dr. Howard will see me on video. If I'm visibly reading, the exam looks rehearsed, and in an MST claim credibility decides service connection. So write notes I can find a fact in at a glance: a date, a dose, a correction I filed, an example I meant to mention. I should never be reading sentences aloud from them.

Write every line so I'd be comfortable if Dr. Howard read it aloud. That means facts and reminders only: no rating-strategy language, no "say this to reach 70%," and no percentages.
</goal>

<exam>
- Tuesday 2026-10-13, 12:00 PM Central, VES TeleC&P (doxy.me), VES# 227264947760
- Examiner: Kasi Howard, PsyD. I'll be in Texas.
- Initial PTSD exam (MST, 2012), with MDD, GAD, OCD, and SUD claimed as secondary. Tinnitus already service-connected.
- VSO: James York. Treating therapist: Cherie Mills (CPT).
</exam>

<corpus>
Read all of it, and keep reading until you could explain the claim to someone who has never seen it. That includes `supporting-docs/`, `personal-records/` (extract PDF text with `pdftotext -layout`), `document-analysis/`, `planning-docs/`, `rater-kb/`, `ratings/`, `vre/` (only for what it says about employment and the shared C-file), the root files, and the PDFs in the root and in `planning-docs/`. That includes the blank Initial PTSD DBQ, `planning-docs/VA-DBQ-for-PTSD-Initial-DSM-V.pdf`, so you know what the examiner has to fill in. The corpus is large; dispatching parallel `document-analyst` readers by folder and synthesizing their reports is fine, as long as every file is actually read.

The corpus has drifted and contradicts itself. A past drafting pass made three critical errors by trusting the wrong file. Resolve conflicts in this order:

1. The facts in `<recent_facts>` below.
2. Primary evidence (signed statements, filed 21-4138s, the 21-0781, clinical and hospital records, Cherie's letter and notes, employer documents) over any analysis of it.
3. Then newest first. `planning-docs/CP-EXAM-PREP-2026-10-13.md` (10/9, consistency-checked) is the most recent synthesis. Use it as your baseline and check it against the corpus; don't simply copy it. Read `REASSESSMENT-2026-10-08-CP-EXAM.md`, `CLAIM-RECONCILIATION-WORKLIST.md`, `RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md`, and `CLAIM-ASSESSMENT.md` Part 0 before treating any position as settled.
4. Treat as history only: `REPORT.md` "Start here", `MASTER-STRATEGY.md`, `PATH-TO-100-PERCENT-2026-07-07.md`, `100-PERCENT-SCHEDULAR-PATHWAY.md`, `knowledge-base.md`, `veteran-profile.md`, `claim-maximization-research-2026-06.md`, `strategy.md`, `CLAIM-EXECUTION-PLAN.md`, `DO-THIS-WEEK.md`, and anything marked `[SUPERSEDED]` or `[RETRACTED]`. (For example, 38 CFR 4.130 has no 90% level, and the ~6/25/26 SI denial does not exist.)

If the rules above don't settle a conflict, don't pick a side. Put it in the notes' "if asked, say what's true" list and cite both sources in the companion file.

Exclude this prompt, everything in `prompts/` and `personal-records/prompts/`, `.remember/`, and both output files, so the run doesn't ingest its own instructions or output.
</corpus>

<recent_facts>
Settled with me 10/8–10/9. These override older documents:

- **Overdoses, 8/4 and 8/5/2026:** caused by 7-OH (concentrated kratom) at toxic doses, with SI at the time. At the hospital I understated both, so the records ("gabapentin, accidental," "no SI") are inaccurate. My 21-4138 correcting this was uploaded 10/9.
- **Pre-service substance use:** kratom from about age 18; legal, bought in stores, and I didn't know it was an opioid. I don't recall any cocaine before service. A correction was filed 10/9. Its "after 2024" error (I separated 2013-11-22) was corrected separately on 10/9.
- **Perpetrator:** a coworker's civilian wife, not a service member. Corrected in the 10/7 21-4138.
- **Persecutory worry:** recurring, not fixed. The "grandiose" belief is ordinary self-belief.
- **Family:** strained relations with my brother and both parents; little contact.
- **Incident year:** 2012. I can't pin down the exact month, and whether I was 22 or 23 depends on it. An honest date range is the right answer; don't invent precision.
  </recent_facts>

<research>
The prep doc already covers general C&P logistics with citations. Research only what the corpus doesn't answer, focusing on PTSD and MST specifically. Prefer sources in this order: VA's own (M21-1 Part VIII on MST/personal assault, 38 CFR 3.304(f)(5), the DBQ, VA MST and National Center for PTSD examiner materials, VBA MST fact sheets); then peer-reviewed literature (examiner practice, delayed disclosure, symptom validity); then BVA decisions; then reputable veteran-law firms. Use blogs only as labeled secondary sources. Questions to answer:
- How examiners are trained to conduct MST exams: trauma-informed approach, how much stressor detail they need, how they assess and opine on "markers," and how they treat delayed disclosure and memory gaps.
- What a TeleC&P PTSD exam changes compared with in-person: instruments that can be given remotely, and what happens if the connection drops.
- Anything from 2025–2026 that changes how contract MST/PTSD exams are run.

Cite every external claim. Run the `citation-verifier` agent on every legal citation (CFR, USC, M21-1, case law). Label anything it can't confirm UNVERIFIED, or drop it. Research findings go in the companion file, and a finding reaches the notes only if it changes what I should do in the room.
</research>

<constraints>
Each of these protects the claim, which is why it's here:
- **No recitable answers.** Write cue words and facts ("ask for a break," "Reyes, late 2013"), never sentences to say. Scripted answers sound rehearsed, and if they drift from the truth they become false statements to a federal examiner.
- **No wording for any witness** (Erica, Reyes, Poquette, Goff), and no clinical judgments for Cherie. Coached statements are the biggest credibility risk in this file (`CLAIM-ASSESSMENT.md` Part 0).
- **Accuracy in both directions.** Where my documents overstate something ("feeds me," "delusions," "FMLA at every job," "total estrangement"), note what's actually supported. Where I tend to minimize, note that too: typical day versus bad day, and holding it together on camera.
- **Safety.** Include 988 (press 1) / text 838255, and remind me that current SI gets answered truthfully.
- **PHI.** These are my own notes, so dates and medications belong in them. Keep them in `planning-docs/`, and don't copy `personal-records/` content anywhere outside this repo.
- **Plain language,** second person, scannable under stress: short lines, bold anchors, no paragraphs.
</constraints>

<output>
**1. `planning-docs/CP-EXAM-NOTES-2026-10-13.md`, the sheet I keep beside me.** It must fit on two printed pages, because more than that means flipping pages on camera. Contents:
- **Top strip:** 988 / 838255; VES phone 877-637-8387 if the video drops; "I can ask for a break"; "be specific: how often, how bad, an example."
- **Key dates:** service dates, the 2012 incident (as a range), each disclosure (who and when), treatment admissions, jobs (start/end and how each ended), the overdoses, my filings.
- **Current medications:** name, dose, prescriber. Where the corpus doesn't settle one, leave a blank for me to fill in.
- **Corrections I've filed:** one line each, so I can raise them myself.
- **Things to make sure get covered:** one cue line per symptom area, each with a real recent example drawn from the corpus (for example, "panic — mornings, most days — [example]"). Where the corpus has no recent example, leave a blank for me.
- **If asked, say what's true:** the open discrepancies as cue words (for example, "Cherie, sober in July?", "Mountain end date 6/26 vs 6/30").
- **Before the call ends:** the items not to leave unsaid.

Render it to PDF with pandoc plus headless Chrome, as was done for the prep doc, and confirm it's two pages or fewer.

**2. `planning-docs/CP-EXAM-NOTES-2026-10-13-SOURCES.md`, the companion I don't bring into the exam.** For each line in the notes: the corpus file (or files) it rests on, how any conflicts were resolved, the research findings with citations and verification status, and anything that changed from the 10/9 prep doc.
</output>

<done_when>

- Every fact in the notes traces to a corpus file in the companion, and every external claim is verified or labeled UNVERIFIED.
- The `claim-consistency-checker` agent has run on the notes against the corpus. Fix whatever has a clear fix; anything else becomes an "if asked" cue in the notes and is explained in the companion.
- Neither file contains a recitable answer, witness wording, rating-strategy language, or a stale or retracted position.
- The PDF is two pages or fewer.
- Change no other file in the corpus.
- End with a few lines telling me what I still need to fill in by hand, and anything you found that contradicts the 10/9 prep doc.
  </done_when>
