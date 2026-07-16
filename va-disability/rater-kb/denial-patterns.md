# Documented Denial & Underrating Patterns (MH/MST claims)

Scope: documented, sourced reasons VA denies or underrates mental-health and MST
claims. This file powers the harness's adversarial-reviewer role — it is the
checklist the harness uses to red-team a draft claim file before submission, so
every pattern below should be treated as "things a hostile reviewer will look
for," not general background reading.

---

## 1. VA OIG-documented MST claim mishandling (FY2017 cohort)

The VA Office of Inspector General's targeted audit of MST-related PTSD claims
denials found a large, specifically-attributed rate of improper processing.
Figures reported (with some variance across the primary landing page and
secondary summaries — flagged below, not silently reconciled):

- The OIG's review sample covered **~2,700** MST-related claims reviewed
  April–September 2017, out of an estimated **~5,500** total MST-related denials
  processed October 2016–September 2017.
- Approximately **1,300 of the ~2,700 reviewed (≈48%)** were found to be
  improperly processed.
- Secondary sources (see below) independently report a consistent overall
  picture — "nearly half" of FY2017 MST claims were mishandled, and cite the
  same ~5,500 denied-claims figure — but frame the denominator slightly
  differently (one states "12,000 MST claims filed" as the base rather than the
  OIG's ~2,700-claim review sample). **Do not treat the exact percentage as
  precision-verified** — the underlying rate (roughly half of denied MST claims
  in this period were mishandled) is corroborated by multiple sources; the exact
  arithmetic should be re-derived from the primary OIG report PDF by the
  citation-verifier pass, since that PDF could not be extracted by automated
  fetch in this pass (see Verification Ledger).

Source (primary, fetched directly): https://www.vaoig.gov/reports/audit/denied-posttraumatic-stress-disorder-claims-related-military-sexual-trauma

### 1.1 Four documented causes of improper denial

The OIG attributed improper denials to four specific procedural failures, each
with a reported incidence rate within the reviewed cases:

| Cause                                                       | Reported rate | What it looks like in a claim file                                                                                                                                                                                      |
| ----------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Medical exam not requested**                              | 28% of cases  | Evidence in the file was sufficient to trigger a C&P exam under the duty to assist, but staff did not order one.                                                                                                        |
| **Inadequate evidence gathering**                           | 13% of cases  | Staff did not request relevant records — most commonly, private/civilian treatment records the veteran had identified.                                                                                                  |
| **MST Coordinator outreach failures**                       | 11% of cases  | The MST Coordinator did not make required phone contact with the veteran, or letters sent did not include the required language asking whether the incident was reported in service or requesting a copy of any report. |
| **Reliance on contradictory/insufficient medical opinions** | 10% of cases  | The claim was denied based on a medical opinion that was internally contradictory or plainly insufficient, without the reviewer seeking clarification.                                                                  |

Source: same OIG report, as independently corroborated (consistent figures) by
two secondary practitioner summaries:
https://www.hillandponton.com/mst-cases-incorrect-denials/ and
https://cck-law.com/blog/va-mishandled-military-sexual-trauma-mst-claims-va-oig-reports/

### 1.2 Root causes identified by OIG (systemic, not case-by-case)

- Lack of reviewer specialization for MST claims
- No additional/higher level of review built into the MST claims process
- Discontinuation of special-focus quality-improvement reviews that had
  previously existed
- Inadequate or outdated training — MST-specific training materials had not been
  updated since 2014 as of the audit

Source: same OIG report and secondary summaries as § 1.1. The OIG's
recommendations included re-reviewing all ~5,500 denied claims from the period,
assigning MST claims to a specialized processor group, and adding a mandatory
additional review level for MST denials; as of a later status check cited in one
secondary source, some recommendations remained not fully implemented years
after the original audit — treat this as directional evidence that the
underlying failure modes are not fully remediated, not as a current-year
statistic.

**A second, more recent OIG report** (https://www.vaoig.gov/sites/default/files/reports/2024-11/vaoig-24-00118-01.pdf,
dated November 2024 per its filename) was located in the source bibliography
but could not be extracted by automated fetch (returned as an undecoded PDF
binary stream). This is a real gap — the citation-verifier pass or a manual
review should re-pull this report, since it likely reflects the most current
OIG assessment of whether the FY2017 failure modes persist.

## 2. General MH/MST denial and underrating patterns (derived from the

adjudication-procedure and DBQ files in this KB)

These are not separately OIG-sourced statistics — they are the failure modes
implied by the procedural rules documented in `rating-procedure.md`,
`dbq-mental-disorders.md`, and `mst-adjudication.md`, restated here as concrete
adversarial-review checkpoints. Each cross-references the rule it violates.

- **Insufficient exam findings.** A C&P exam that fails to elicit and document
  frequency/severity/duration for each symptom leaves the rater unable to apply
  the Vazquez-Claudio standard (`criteria-4130-caselaw.md` § 3.2) — symptoms
  without functional-impairment detail cannot be mapped to a rating level even
  if a diagnosis is clear.
- **Credibility inconsistencies, including income/work-history conflicts with
  claimed impairment.** Under the credibility factors in `rating-procedure.md`
  § 2 (facial plausibility, consistency with other evidence, internal
  consistency), a claim asserting severe occupational impairment while the
  record shows sustained, unremarkable full-time employment invites a
  credibility challenge on the "consistency with other evidence" factor
  specifically — this is a documented adversarial-review vector independent of
  whether the underlying impairment is genuine.
- **Treatment gaps.** A long gap between an alleged in-service stressor and the
  first clinical mention of it is addressed specifically for MST claims in
  `mst-adjudication.md` § 4 (minimization/delayed-disclosure pattern) — but for
  non-MST mental-health claims generally, an unexplained treatment gap is not
  independently privileged the same way, and a hostile reviewer will treat it as
  a plain credibility/continuity-of-symptomatology gap unless a comparable
  explanation is put in the record.
- **Inadequate nexus language.** An opinion that hedges with "cannot state
  without resorting to mere speculation" does not, by itself, satisfy the
  claimant's evidentiary burden or trigger benefit-of-the-doubt
  (`rating-procedure.md` § 3, Fagan v. Shinseki boundary) — a nexus opinion
  needs to affirmatively reach "at least as likely as not" or better, with
  stated rationale, or it does not move the needle.
- **Stressor-marker insufficiency.** For MST claims, a stressor account with no
  marker evidence developed under § 3.304(f)(5) (`mst-adjudication.md` § 1) is
  vulnerable — not because the absence of a service report counts against the
  veteran (it doesn't, per AZ & AY), but because the alternative marker
  categories the regulation offers (records, statements, documented behavior
  changes) still have to be affirmatively identified and submitted; VA's duty is
  to advise the claimant of these categories, not to independently discover
  them.
- **Comorbid-condition dilution.** Where multiple mental-health diagnoses are
  present and the DBQ differentiation question (`dbq-mental-disorders.md` § 1.2)
  is answered "not possible to differentiate," a rater is supposed to treat
  impairment as an undifferentiated combined whole — a claim file that instead
  lets the exam findings get parceled thinly across several diagnoses (none of
  which individually reads as severe) risks an underrating that the cumulative-
  impact rule was designed to prevent.

---

## Verification Ledger

- VA OIG audit — denied MST-related PTSD claims (FY2017 cohort; ~48% improper
  processing rate; four-cause breakdown; root causes) —
  https://www.vaoig.gov/reports/audit/denied-posttraumatic-stress-disorder-claims-related-military-sexual-trauma
  — UNVERIFIED
- Secondary corroboration of the same OIG findings —
  https://www.hillandponton.com/mst-cases-incorrect-denials/ and
  https://cck-law.com/blog/va-mishandled-military-sexual-trauma-mst-claims-va-oig-reports/
  — UNVERIFIED
- Second (2024) OIG report — https://www.vaoig.gov/sites/default/files/reports/2024-11/vaoig-24-00118-01.pdf
  — NOT EXTRACTED (binary/PDF fetch failure); flagged as an open gap, not cited
  for any specific claim in this file
- General denial/underrating patterns in § 2 are derived from, and cite back to,
  claims already ledgered as UNVERIFIED in `rating-procedure.md`,
  `dbq-mental-disorders.md`, and `criteria-4130-caselaw.md` — no new independent
  citations introduced in § 2 beyond those cross-references

## Conflicts with prior research

`../claim-maximization-research-2026-06.md` does not present OIG denial-rate
statistics or a general denial-patterns taxonomy — it is organized around one
individual claimant's fact pattern (case-specific risk table, credibility risk
around SUD-disclosure timing, TDIU/income analysis) rather than documented
population-level denial causes. There is no directly overlapping statistical
claim to reconcile.

One adjacent point worth flagging: that document's risk table (its line ~364,
"PTSD rated at 50% instead of 70% — current employment cited as counter-
evidence") identifies the same income/work-history-vs-claimed-impairment
credibility tension flagged in this file's § 2 — the two documents are
directionally consistent on that specific risk, though the prior document
frames it as an individual mitigation strategy rather than a documented
denial-pattern statistic (it cites no denial-rate source for that specific
claim). Not a contradiction.

None found beyond the above.
