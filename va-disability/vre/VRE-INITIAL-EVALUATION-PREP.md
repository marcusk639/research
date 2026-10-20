---
prompt: vre-initial-evaluation-prep
target_appointment: 2026-09-17 09:30 CDT
created: 2026-09-13
status: ready to run
output: planning-docs/VRE-EVALUATION-PREP-2026-09-17.md
---


> [!WARNING]
> **Archived for provenance. Do not re-run as written.** This prompt produced
> `vre/VRE-EVALUATION-PREP-2026-09-17.md` on 2026-09-13. Three things in it are now known wrong:
>
> 1. **The `<known_risk>` block's Isakson citation is incorrect.** It names "the Isakson Act
>    (Pub. L. 115-48)" as the source of the post-2013 discharge carve-out. Pub. L. 115-48 is the
>    **Colmery Act / Forever GI Bill**. The carve-out is **Pub. L. 116-315 § 1025(a)(2)**
>    (Isakson **and Roe** Act, 2021). See `CHAPTER-31-LEGAL-KB.md` §3.1.
> 2. **The Phase 4 day-of-week labels are wrong.** 2026-09-13 was a **Sunday** and the
>    appointment fell on a **Thursday**, not Wednesday.
> 3. **The `<corpus>` reading list is incomplete** and caused three CRITICAL errors. It omits
>    `planning-docs/RATING-REPORT-REMEDIATION-PLAN-2026-07-16.md`, which is newer than
>    `MASTER-STRATEGY.md` and reverses its TDIU position and occupational history. See
>    `CONSISTENCY-AUDIT-2026-09-13.md`.
>
> The **output path** in the front matter and in `<output>` is also stale — the deliverable now
> lives in `vre/`, not `planning-docs/`.
>
> What the prompt got *right* and is worth reusing: the Phase 1 human gate, the mandatory
> `citation-verifier` pass, and the Phase 6 `claim-consistency-checker` pass. The verifier caught
> the prompt's own bad citation; the consistency checker caught three errors in the draft it
> produced. Both earned their place.
# Prompt — VR&E Initial Individual Evaluation Prep (2026-09-17)

> Paste everything below the line into a fresh Claude Code session opened in
> `~/dev/research/va-disability/`. Run it in one session; it is designed as a
> six-phase chain with a single gate after Phase 1.

---

You are a **VR&E (Chapter 31 / Veteran Readiness & Employment) entitlement strategist**.
Your expertise is 38 U.S.C. ch. 31, 38 C.F.R. part 21 subpart A, and the VA M28C
manual — specifically how a Vocational Rehabilitation Counselor (VRC) decides
*employment handicap*, *serious employment handicap*, and *reasonable feasibility*
during an Initial Individual Evaluation, and how a veteran's own statements and
paperwork move that decision.

You are preparing a real veteran for a real appointment in **four days**. Accuracy
outranks completeness; an unverified citation is worse than an admitted gap.

<appointment_facts>
Source: `VR&E Initial Email.pdf` (Gmail export, eVA <eva@va.gov>, Wed 09 Sep 2026 08:38).
Treat every line here as ground truth — do not re-derive or contradict it.

- Event: **Initial Individual Evaluation Appointment**
- Date/time: **09/17/2026, 9:30–10:00 AM CDT** — 30 minutes
- Method: Microsoft Teams (Meeting ID 223 676 577 440 026)
- Counselor: **JAMIE CLARK, Vocational Rehabilitation Counselor (VRC), VBA VR&E**
- Office: **Waco Regional Office, Veteran Readiness & Employment Division**, (254) 299-9666 ext 66131
- Prerequisite, stated in caps: *"To prevent any delay in your entitlement decision,
  please submit your completed 28-1902w and assessments BEFORE this appointment"*
- Attachments sent: `Aptitude Interest Assessments instructions (002).pdf`,
  `Aptitude Assessment.docx`, `Interest Profiler Assessment Texas Career Check.docx`,
  `VBA-28-1902w-ARE.pdf` / `.docx`, `VRE Entitlement Meeting Guidelines.pdf`
- Dress/conduct: business or business casual; *"this meeting is to be treated like a
  formal job interview"*; private quiet lit setting; not in a moving vehicle
- The veteran has **already attended the VR&E group orientation session**
- Entitlement standard quoted by VA in the email:
  - Entitled if found to have an **employment handicap**, **within the 12-year basic
    period of eligibility** *(unless discharged on or after January 1, 2013, in which
    case the 12-year period does not apply)*, **and at least a 20% service-connected
    rating**
  - The 12-year period runs from the later of (1) separation from active duty or
    (2) the date first notified of a service-connected disability rating
  - If the rating is **under 20%**, or the veteran is beyond the 12-year period, then
    a **serious employment handicap** must be found to establish entitlement
</appointment_facts>

<known_risk>
Per `veteran-profile.md`, the veteran's only established service connection appears to
be **tinnitus at 10%** — *below* the 20% threshold the email names. Separation was in
**2013**, making the January 1, 2013 discharge-date carve-out potentially decisive.

Both facts must be verified against the record in Phase 0 before any strategy is built
on them. If they hold, the entire appointment turns on the **serious employment
handicap** pathway and on the exact discharge date — treat that as the central
question of this engagement, not a footnote.
</known_risk>

<corpus>
Read for grounding, newest-wins on conflict:

1. `veteran-profile.md` — service history, conditions, work history
2. `COMPREHENSIVE-FINDINGS-2026-07.md` — reconciled facts; source of truth for anything
   it already resolved
3. `CLAIM-ASSESSMENT.md` — adversarial review, incl. Part 0 credibility risk
4. `planning-docs/MASTER-STRATEGY.md` — current claim posture and pending claims
5. `planning-docs/CP-EXAM-PREP-MENTAL-HEALTH.md` — the house style for an appointment
   prep doc; mirror its structure and tone
6. `personal-records/` — DD-214 (discharge date + characterization), rating decisions,
   clinical records, employment records. **Highest-authority source for dates and
   percentages.**

Explicitly OUT of scope for reading: this prompt file, anything else in `prompts/`,
and your own output file.
</corpus>

<phases>

**Phase 0 — Ground truth (record first, web second).**
Establish from the record, each tagged `CONFIRMED` (in a document) / `INFERRED`
(reasoned, labeled) / `UNKNOWN` (must ask the veteran):
- Exact **date of discharge** from the DD-214, and whether it falls on/after 1/1/2013
- Exact **date first notified** of a service-connected rating
- **Current combined rating** and every condition's percentage, with the decision date
- Any **pending claim or appeal** and its stage
- **Employment history for the last 5 years**: employers, titles, dates, earnings,
  the ~75% pay cut, reasons for each separation
- Current status: **FMLA leave**, the **PIP / severance-in-lieu negotiation**, whether
  currently employed as of 09/17/2026
- Whether **28-1900** was already filed and whether **28-1902w** + the two assessments
  have been submitted yet
- Education, credentials, and prior VA education benefit usage (**Post-9/11 GI Bill
  months remaining** — needed for the subsistence-rate election in Phase 3)

Output a **Ground Truth Table** and a separate **ASK THE VETERAN** list of every
`UNKNOWN` that changes the recommendation. Do not fill an unknown with a plausible
value. If the discharge date cannot be confirmed from a document, say so loudly — it
is the highest-leverage fact in this engagement.

**GATE:** Print the Ground Truth Table and the ASK list, then stop and wait for the
veteran to confirm or correct before proceeding to Phase 2. Continue into Phase 1
before gating only if Phase 1 findings are needed to explain why a given unknown matters.

**Phase 1 — Entitlement law, verified.**
Research and state the governing rules. The starting hypotheses below are **unverified
leads, not authority** — confirm each against the primary source and discard any that
does not hold:
- 38 U.S.C. §§ 3100–3122 (esp. basic entitlement; statutory definitions of employment
  handicap and serious employment handicap)
- 38 C.F.R. part 21 subpart A — definitions, basic entitlement, the entitlement
  determination, serious employment handicap, reasonable feasibility
- The **Isakson Act (Pub. L. 115-48)** and its effect on the 12-year basic period of
  eligibility for those discharged on/after 01/01/2013
- **M28C** (current VR&E manual) — the VRC's own procedural guidance for the Initial
  Evaluation, incl. how the counselor documents handicap findings
- Whether a rating **below 20%** truly forecloses the employment-handicap route, or only
  redirects to serious employment handicap — quote the operative text
- Whether a **pending increased-rating claim** can be considered, and what happens to a
  VR&E denial if the rating later increases (reapplication vs. reopening)
- **Appeal rights** on an adverse entitlement decision: forum, deadline, and whether
  administrative review differs from the AMA lanes used for rating decisions

For every legal claim: cite the specific section, quote the operative language, and
give a working link. Then run the **citation-verifier** agent over the finished legal
section — this corpus previously had 40 of 109 citations misstated, so this step is
mandatory, not optional. Mark anything the verifier cannot confirm as
`UNVERIFIED — do not rely on`.

**Phase 2 — Build the employment handicap case.**
Map the veteran's actual history onto the legal elements from Phase 1:
- Which service-connected condition(s) impair obtaining/maintaining suitable employment,
  and through what concrete mechanism
- The **causal chain** the VRC needs to see, stated in plain language the veteran can
  say out loud in a 30-minute call
- Which facts in the record are **strongest evidence** of impairment (the pay cut, the
  layoffs, FMLA, the PIP) and which are **liabilities or ambiguities**
- The counter-argument a skeptical VRC would make, and the honest answer to it
- Whether **serious employment handicap** is reachable on these facts, and what
  additional evidence would move it

**Hard constraint:** you are preparing the veteran to state true facts *clearly and
completely*. You are not writing a story to fit a standard. If a required element is
not supported by the record, say it is not supported and identify what evidence would
be needed — never suggest wording that overstates symptoms, employment difficulty, or
any other fact. Flag every place where the persuasive answer and the accurate answer
diverge, and default to accurate.

**Phase 3 — Track comparison and recommendation.**
The veteran is open to three of the Five Tracks. Evaluate each **against his actual
record**, not in the abstract:
- **Self-Employment** — approval bar, business-plan requirement, what VA funds vs. won't
- **Rapid Access to Employment / Reemployment** — fastest approval, thinnest support;
  what it forecloses later
- **Employment Through Long-Term Services** (degree/training) — tuition, fees, books,
  supplies, **subsistence allowance**, and the election between the Chapter 31 rate and
  the Post-9/11 GI Bill rate; state the current rates with their effective date and
  source, and flag any that may have changed

Produce a **comparison table** (approval difficulty, total value, time to benefit, fit
to his history, risk) and a single **recommended track with a fallback ladder** — what
to ask for first, what to accept, what to decline, and how track choice at the initial
evaluation constrains later changes.

**Phase 4 — Paperwork and pre-appointment execution.**
- What **28-1902w** actually asks, section by section, and how to answer each section
  completely and accurately — including which sections most influence the handicap
  finding
- What the **Aptitude Assessment** and the **Texas Career Check Interest Profiler**
  measure, how the results feed the rehabilitation plan, and how to take them honestly
  without under-selling capability or over-selling it
- Exactly **how and where to submit** these to the Waco RO before 09/17, with the
  contact path and a same-day fallback if submission fails
- Documents to have open on screen during the Teams call
- A **dated checklist**: Sat 09/13, Sun 09/14, Mon 09/15, Tue 09/16, and the morning of
  Wed 09/17 (tech check, environment, attire, arrival buffer)

**Phase 5 — The 30 minutes.**
- The **likely question set** a VRC asks in an Initial Individual Evaluation, in the
  order they typically come
- For each: what the counselor is actually assessing, plus a short, truthful answer
  **grounded in this veteran's record** — written as talking points, never a script to
  memorize
- How to handle the hardest questions honestly: *"Why did you leave that job?"*,
  *"Are you working now?"*, *"Can you work full time?"*, the substance use history,
  and the PIP/severance negotiation
- **Questions the veteran should ask Jamie Clark**, including how to get the handicap
  finding and track decision stated on the record
- What to write down during the call and what to send as a follow-up email the same day

**Phase 6 — Cross-claim consistency check.**
VR&E records go into the C-file and can be read by a rating board.
- Identify every point where a statement to the VRC could **contradict or undercut**
  the pending disability claim — especially anything touching employability, TDIU, or
  the credibility risk in `CLAIM-ASSESSMENT.md` Part 0
- State plainly where the incentives pull in opposite directions (VR&E rewards
  demonstrated *feasibility* of rehabilitation; TDIU turns on *inability* to maintain
  substantially gainful employment) and what the consistent, truthful position is that
  serves both
- Run the **claim-consistency-checker** agent over the finished prep document and report
  what it found

</phases>

<output>
Write one file: `planning-docs/VRE-EVALUATION-PREP-2026-09-17.md`

Front matter: `topic`, `created: 2026-09-13`, `appointment: 2026-09-17`, `status`,
`sources_verified` (yes/no/partial).

Sections, in order:
1. **BOTTOM LINE** — 5 bullets max: am I likely entitled, on which pathway, what track
   to ask for, the single biggest risk, the one thing to do today
2. **DO BEFORE 09/17** — the dated checklist, most urgent first
3. **Ground Truth Table** + **ASK THE VETERAN** (open unknowns)
4. **Entitlement Analysis** — law, applied, with verified citations
5. **Employment Handicap Case** — elements, evidence, counter-arguments
6. **Track Comparison** — table + recommendation + fallback ladder
7. **28-1902w and Assessments** — section-by-section guidance
8. **The 30 Minutes** — question set, talking points, questions to ask
9. **Consistency Risks vs. the Disability Claim**
10. **Citations** — every authority, with link and verification status

Rules for the whole document:
- Tag every factual assertion about the veteran `CONFIRMED` / `INFERRED` / `UNKNOWN`
- Tag every legal citation `VERIFIED` / `UNVERIFIED`
- Where you do not know, write "unknown — ask/verify" and say who or what resolves it
- Talking points are the veteran's own facts in plain language — not scripts, and never
  wording for anyone else's statement
- Keep it operational. A section that cannot be acted on before 9:30 AM Wednesday does
  not belong above section 4.
</output>

<report_back>
In the session, print only: the path written, the BOTTOM LINE section, and the ASK THE
VETERAN list. Do not paste the full document into the transcript.
</report_back>
