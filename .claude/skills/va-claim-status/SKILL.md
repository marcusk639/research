---
name: va-claim-status
description: Report current status of the VA disability claim in va-disability/ — overdue deadlines, next actions, open blockers, and outstanding evidence. Use when the user asks "what's the status of my VA claim", "what's next", "what's overdue", or "what am I still waiting on".
disable-model-invocation: true
---

# va-claim-status

Give a fast, accurate snapshot of where the `va-disability/` claim currently
stands, without re-reading the entire corpus. This skill is a status check, not a
research task — it reads the synthesis documents that already exist and reports
what they say, flagging anything that looks stale.

## Steps

1. **Read the current-state documents**, in this priority order:
   - `va-disability/COMPREHENSIVE-FINDINGS-2026-07.md` (or the most recent
     `COMPREHENSIVE-FINDINGS-*.md` file if a newer one exists — always prefer the
     latest dated version)
   - `va-disability/planning-docs/CLAIM-EXECUTION-PLAN.md`
   - `va-disability/planning-docs/DO-THIS-WEEK.md`
   - `va-disability/planning-docs/strategy.md`

2. **Compute today's date** relative to every deadline mentioned in those files
   (intent-to-file windows, development-letter response deadlines, appeal windows,
   C&P exam dates). Do not assume a deadline is still open — flag anything whose
   date has already passed as **OVERDUE** and call it out first.

3. **Report in this structure:**
   - **Overdue / needs immediate attention** — anything with a passed deadline, or
     an open critical risk flagged in the comprehensive findings (credibility
     risks, unresolved diagnostic inconsistencies, corrupted/missing evidence
     files) that hasn't been marked resolved.
   - **Next actions** — the highest-priority open items from the execution plan,
     in order.
   - **Waiting on** — evidence or documents that are outstanding (e.g. a nexus
     letter, a buddy statement, a records request) and who/what they're waiting on.
   - **Recently resolved** — anything the findings docs mark as newly confirmed or
     fixed since the last status check, if it's possible to tell.

4. **Do not re-derive new findings.** If the user's question requires reading
   source PDFs or reconciling new documents that aren't reflected in the existing
   synthesis files, say so explicitly and suggest re-running the corpus digest
   (parallel subagents reading every document) or invoking `/va-rating-strategy`
   rather than guessing.

5. Keep the report tight — this is a status check, not a new report. Link to the
   underlying file for anything the user wants more detail on.
