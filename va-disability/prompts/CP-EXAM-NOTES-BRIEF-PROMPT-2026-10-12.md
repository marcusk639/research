# Prompt: One-Page In-Exam Notes for the PTSD/MST C&P Exam

> Created 2026-10-12 · Run from `~/dev/research/va-disability/` · Output: `planning-docs/CP-EXAM-NOTES-BRIEF.md` (+ `.pdf`)
> Paste everything below the line into a fresh Claude Code session.

---

<goal>
Write a **one-page** sheet I can keep beside me during my VA mental-health C&P exam. I'll be on video with the examiner, so I need to find a fact with a single glance — a date, a dose, a correction I filed, an example I mean to mention — without visibly reading. One page means I never flip pages on camera, and it leaves only what I'd actually look at.

These are reminders, not a script. VA lets a veteran bring a short list but expects answers in the veteran's own words, and in an MST claim credibility decides service connection. Every line should pass this test: I'd be comfortable if the examiner read it aloud. So use facts and cue words only, with no rating strategy, no percentages, and no sentences to recite.
</goal>

<exam>
- **Date: not yet set.** VA rescheduled the original 2026-10-13 exam and the new date is expected within about 30 days. Leave a blank for the date and time. The format is VES TeleC&P.
- Initial PTSD exam (MST, 2012), with MDD, GAD, OCD, and SUD secondary to PTSD. Tinnitus is already service-connected.
- VSO: James York. Treating therapist: Cherie Mills (CPT).
</exam>

<inputs>
Your starting point is the existing 2-page sheet, `planning-docs/CP-EXAM-NOTES-2026-10-13.md`. Its companion, `planning-docs/CP-EXAM-NOTES-2026-10-13-SOURCES.md`, records the source of every line and how conflicts were resolved. A full-corpus pass and a consistency check went into both. Condense the sheet rather than rebuilding it, but read the corpus wherever you need to confirm a line, settle a conflict, or apply the facts below. When sources conflict, primary evidence (signed and filed forms, clinical records, Cherie's letter and notes) outranks any analysis of it. Newer outranks older. Anything marked `[SUPERSEDED]` or `[RETRACTED]` is history only.

You don't need new web research; the companion file already has it.

Don't read anything in `prompts/` or `personal-records/prompts/`, or `.remember/`, or the output files. A run that reads its own instructions or output contaminates itself.
</inputs>

<new_facts>
These were settled with me on 2026-10-12, after the 2-page sheet was written. They take priority over the corpus:

- **Exam rescheduled by VA**; date to be determined (see above).
- **Pre-service mental health:** anxiety and depression at about 18. I saw a **psychiatrist** (Lake Charles) as an outpatient for 2–3 months, stopped, and got better. My 10/7 21-4138 says about 19. If the age is the only difference, the cue is "18 or 19"; no new filing is needed.
- **Kratom from ~18** is corrected in my filed 21-4138 (10/9).
- **The Starlite entries** ("use from ~18," "anxiety/depression at 18," "opioids at 25") are history Starlite recorded at intakes in 2022–25, not treatment before service. "Opioids at 25" (~2014) places the escalation after service. Only a brief "if asked" cue is needed.
- **How to describe symptoms:**
  - The symptoms tied to the MST by their content are intrusive memories, nightmares, avoidance of reminders and of women, distress at cues, shame and self-blame, and intimacy problems.
  - Withdrawal and heavier drinking from summer 2012 (per Reyes) tie in by timing.
  - Sleep, concentration, irritability, depression, anxiety, panic, OCD, and substance use overlap with other causes.
  - The sheet's cue is: **what it is · how often · when it started · what it's about · "not sure" is fine.** Don't attribute everything to the MST.
- **Open items from the 10/12 run** — keep these as "if asked" cues, not conclusions:
  - The 8/4 hospital record ("antihistamine poisoning," gabapentin 1200 mg plus other medications; opiates negative, no kratom test).
  - Whether the ankle is service-connected (my personal statement says 10%; other documents say only tinnitus).
  - The early-June relapse versus Cherie's "currently sober" notes of 7/9 and 7/16.
    </new_facts>

<what_to_keep>
Fill one page in roughly this order of priority; the first items are what I'll most need at a glance:

1. **Top strip:** 988 (press 1) / text 838255 · VES 877-637-8387 if the video drops · "I can ask for a break" · the symptom cue above · "If today isn't typical, say so" · "Current SI: answer truthfully."
2. **Medications:** name · dose · prescriber · "Now?" Carry over the 2-page sheet's blanks for anything the corpus doesn't settle.
3. **Key dates:** service, the 2012 incident as a range, who I told and when, treatment stays, jobs (start, end, how each ended), the overdoses, my filings. Compress these to one line per item.
4. **Corrections I filed,** so I raise them myself: civilian perpetrator; pre-service therapy; kratom from ~18 plus the "after 2024" fix; the overdoses (7-OH, SI present, understated at the hospital).
5. **Make sure these get covered:** one cue per symptom area, each with a blank for a recent example where the corpus has none.
6. **If asked, say what's true:** keep only the highest-likelihood items. The 2-page sheet has about 30. Choose about 8, ranked by how likely the examiner is to raise each one, and move the rest to the companion's "cut for space" list. A long list here invites reading from the page.
7. **Before the call ends:** self-care, isolation, job losses, overdoses, corrections, typical day versus bad day.
   </what_to_keep>

<constraints>
- No recitable answers. No wording for any witness (Erica, Reyes, Poquette, Goff), and no clinical judgments for Cherie. Coached statements are the biggest credibility risk in this file (`CLAIM-ASSESSMENT.md` Part 0).
- Be accurate in both directions. Keep the corrections where my documents overstate ("delusions," "FMLA at every job," "total estrangement") and the reminders where I tend to minimize.
- Write plain, scannable language I can read under stress: short lines, bold anchors, no paragraphs.
- PHI stays in `planning-docs/`.
</constraints>

<output>
1. `planning-docs/CP-EXAM-NOTES-BRIEF.md`, rendered to `.pdf` with pandoc and headless Chrome, as done for the earlier notes. It must fit on **one page** of US Letter at a readable size (no smaller than about 9pt). Confirm the page count with `pdfinfo`.
2. A short appendix at the end of `planning-docs/CP-EXAM-NOTES-2026-10-13-SOURCES.md`. Append only and don't rewrite the existing content. List what was cut and why, which "if asked" items were kept and how they were ranked, and every change driven by `<new_facts>`.

Leave the existing 2-page sheet and its PDF unchanged; they stay as the backup.
</output>

<done_when>

- The PDF is one page, and every line traces to the corpus or `<new_facts>`.
- The `claim-consistency-checker` agent has run on the brief sheet against the corpus. Fix any finding that has a clear fix; turn anything else into an "if asked" cue.
- No line fails the read-aloud test, and no stale or retracted position appears.
- No other corpus file is changed except for the appendix above.
- End by telling me, in a few lines, what I still need to fill in by hand before the exam.
  </done_when>
