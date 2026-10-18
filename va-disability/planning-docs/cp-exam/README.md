# C&P Exam Prep — 21 Oct 2026 (VES telehealth, mental disorders / initial PTSD-MST)

| File | What it is |
| --- | --- |
| `MOCK-CP-EXAM-PTSD-MST-2026-10-21.pdf` | 32-page mock C&P exam: how the exam works (Part A), the ten things that decide it, ~200 rehearsal prompts in real exam order with assessing / your-file / guidance / trap annotations (Part B), questionnaires incl. validity tests (Part C), two illustrative examiner reports from the same facts (Part D), checklist, debrief, rubric and post-exam playbook (Part E). |
| `CP-EXAM-DAY-NOTES-2026-10-21.docx` | 5-page glance reference for the exam: opening moves, dated timeline, meds table, a fill-in frequency worksheet, the ten things, facts-to-include for tough questions, corrections, do/don't, closing checklist. |
| `src/` | HTML sections + `build-pdf.js` (Chromium/Playwright) and `build-docx.js` (docx-js). Rebuild with `node src/build-pdf.js` and `node src/build-docx.js`. |

**Basis:** the full `va-disability/` corpus plus the veteran's 2026-10-18 status confirmations (exam date/format, Austin address current, Cherie's updated letter signed and filed, belief content = fear of being fired/failing, current opioid use, Erica attending, no Goff statement, no sleep study).

**Verification:** 21 legal citations checked by `citation-verifier` (2026-10-18) — 19 confirmed, 2 corrected and applied (4.16(a) family-business marginal employment is facts-found, not automatic; 3.353 fiduciary appointment runs through Part 13). Fact check by `claim-consistency-checker` (2026-10-18): 9 of 10 findings applied — exam weekday corrected to **Wednesday** 21 Oct, the signed personal statement's 2022 Starlite-therapist disclosure added (prep no longer implies Cherie was the first disclosure), OCD coding sources, Poquette timing, perpetrator-source attribution, caregiving-detail attribution, Recover 5/15 PTSD reference, and Report B's unsourced social facts converted to brackets. Finding #9 (Recover evals deny delusions) was kept — it is sourced in the Phase-4 register I-17.

**Guardrail:** internal prep material — never submit to VA. Neither document scripts symptoms or witness wording; all guidance is "the whole, accurate truth at its real depth."
