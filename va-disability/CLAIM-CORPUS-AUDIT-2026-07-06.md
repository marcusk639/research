# VA Claim Corpus Audit — 2026-07-06

**Scope:** All 16 `va-claim-document-analyst` reports found in
`va-disability/document-analysis/`, covering: `CPT-Impact-Statement`,
`Erica-Personal-Statement`, `Spouse-Statement-Draft-Erica`,
`CP-EXAM-PREP-MENTAL-HEALTH`, `MASTER-STRATEGY`, `NEXUS-LETTER-GUIDE-CHERIE`,
`DD214`, `Poquette-Buddy-Statement`, `CREDIBILITY-INCONSISTENCY-RESEARCH`,
`VBA-21-0781-Signed-Personal-Statement`, `Reyes-Buddy-Statement`,
`COMPREHENSIVE-FINDINGS-2026-07`, `100-PERCENT-SCHEDULAR-PATHWAY`,
`SLEEP-APNEA-SECONDARY-CLAIM`, `PRE-POST-SERVICE-SEVERITY-CONTRAST`, and
`CLAIM-ASSESSMENT`.

**Output location reasoning:** Path was given explicitly by the caller
(`va-disability/CLAIM-CORPUS-AUDIT-2026-07-06.md`); no inference needed.

**Note on source-report granularity:** `CLAIM-ASSESSMENT-ANALYSIS.md` is a
condensed summary rather than the full section-by-section template the other
15 reports use (its own header says so explicitly — a full pass "was not
completed in this run"). Its score (7/10), CRITICAL flag (yes), and citation
list are treated as valid here, but it carries less granular Strengths/
Weaknesses/Gaps detail than the other 15 documents, and that document should
get a full re-run if deeper detail on `CLAIM-ASSESSMENT.md` itself is ever
needed.

**Note on cross-report connections surfaced during synthesis:** Two
specific connections recur across multiple individual reports and are
surfaced explicitly in Cross-Document Findings below, not left for the reader
to reconstruct: (1) the Erica-statement provenance question is raised
independently by both the `Erica-Personal-Statement` report and the
`COMPREHENSIVE-FINDINGS-2026-07` report, one day apart, with opposite
conclusions; (2) the `Poquette-Buddy-Statement` report discovered that
`COMPREHENSIVE-FINDINGS-2026-07` appears to have quoted Poquette's disclosure
language from a superseded draft rather than the actual signed/executed VA
Form 21-10210, which materially changes how strong that evidence is.

---

## Credibility Risks & Citation Verification (read this section first)

This corpus's own history establishes that credibility, not insufficient
documented severity, is the actual ceiling on this claim (`CLAIM-ASSESSMENT.md`
§0.1–0.2; `COMPREHENSIVE-FINDINGS-2026-07.md` §0.2). Every item below is a
credibility risk or an unverified citation — nothing here is about the
claim's underlying severity, which multiple reports independently found
sufficient and non-overreaching.

### Credibility risks

**Tier 1 — active, unresolved, highest consequence:**

- **A signed federal form and a signed personal statement already assert, under
  penalty of perjury, an opioid-origin theory ("no recollection of using
  opioids before active duty") that is directly contradicted by the veteran's
  own repeated self-reports to two different facilities across two different
  years (2018 Victory Addiction Recovery Center; January 2023 Starlite) of
  first opioid/heroin use at age 18, pre-enlistment.** No document in the
  corpus confirms this has been resolved with a VSO/attorney or that a
  corrective supplemental statement has been filed. — source:
  `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md` (CRITICAL flag: yes),
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` (§0.8, Open Task #13),
  `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`,
  `MASTER-STRATEGY-ANALYSIS.md` (flags `MASTER-STRATEGY.md` itself omits this
  item entirely), `PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md` (CRITICAL
  flag: yes — new suggested personal-statement language would restate the
  same unresolved claim without acknowledging it).

- **The Erica spousal-statement provenance question is not genuinely closed,
  despite being logged as "Confirmed."** `Erica Personal Statement.md` is
  logged in `DOCUMENT-PROVENANCE.md` as "self-authored... per veteran's
  confirmation... fully original," confirmed 2026-07-06 — but the file as saved is byte-identical
  to the AI-extracted draft (`BLOG-POST-DRAFT-OUR-STORY.md`) and still
  contains an unedited "Notes" section, in a drafter's voice, describing itself
  as "a first draft built for tone and structure" that "Erica should read...
  and rewrite... in her own words." No textual divergence from the
  acknowledged AI draft is visible anywhere in the reviewed file. — source:
  `Erica-Personal-Statement-ANALYSIS.md` (score 3/10).
  **This exact tension is independently flagged one day earlier** by
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`, which asks whether Open Task #2
  (resolve the Erica coaching issue) is actually closed given the provenance
  log's 2026-07-06 entry doesn't reconcile with its own §0.2 finding that this
  is "the largest concrete threat to the compensation outcome identified
  anywhere in this corpus." Two reports, working from different documents,
  converged on the same unresolved question without either having read the
  other — see Cross-Document Findings below for the full analysis.

- **A second, separately-drafted "scripted" spousal statement
  (`Spouse_Statement_Draft_Erica.converted.txt`) carries an attached
  "Why this version helps the claim" rating-optimization annotation directly
  beneath text intended to become Erica's sworn account**, and independently
  reproduces the same "work as avoidance, not ambition" reframing pattern
  `COMPREHENSIVE-FINDINGS-2026-07.md` attributes to the coached email chain.
  This means at least two structurally similar "coached-adjacent" artifacts
  exist for the same declarant. — source:
  `Spouse-Statement-Draft-Erica-ANALYSIS.md` (score 3/10).

**Tier 2 — active, lower severity, or already-mitigated-but-worth-noting:**

- **The CPT Impact Statement's own header admits its two most legally
  load-bearing sections (etiology of the assault, self-worth impact) are "not
  yet his own words."** This is the same underlying pattern (AI-organized
  narrative later adopted wholesale) as the corpus's top-ranked risk, at lower
  stakes (a private therapeutic worksheet, not a sworn VA form) — but the
  document itself says the rewrite hasn't happened yet. — source:
  `CPT-Impact-Statement-ANALYSIS.md` (score 6/10).

- **`COMPREHENSIVE-FINDINGS-2026-07.md` contains two internally competing
  claims about which single item is the corpus's #1 priority risk** (§0.2:
  the coached-Erica-statement issue; §9a item 1: the signed-document
  opioid-origin contradiction), never reconciled against a common yardstick.
  A reader who reads only one section walks away with a different "#1 risk"
  answer. — source: `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.

- **`COMPREHENSIVE-FINDINGS-2026-07.md`'s own diagnostic ledger and task list
  have gone stale in a way that could cause duplicated or dropped work**: it
  presents an overstated F15.20 "zero supporting narrative" claim in its
  high-visibility §0 that its own later §9a softens without updating the
  original passage or task list; and two of its own self-flagged
  inconsistencies (Harmony Junction stay-length mismatch, CPT worksheet
  age-arithmetic error) never get promoted into its own "what needs to happen"
  task list, breaking its own internal pattern of doing so. — source:
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.

- **Poquette's signed/executed VA Form 21-10210 does not match the draft
  version quoted as ground truth elsewhere in the corpus** — see
  Cross-Document Findings below for full detail. Net effect: the corpus's
  own synthesis document may be citing stronger in-service-disclosure language
  than what was actually filed under penalty of perjury. — source:
  `Poquette-Buddy-Statement-ANALYSIS.md` (score 6/10).

- **Reyes and Poquette's statements conflict on the disclosure year** (2012 vs.
  "late 2013"), a fact directly load-bearing under 38 CFR 3.304(f)(5)'s
  in-service-vs-post-service timing test. Per this corpus's own hard rule,
  this is not something to draft or reconcile on the witnesses' behalf — it
  is for Reyes and Poquette to resolve independently, in their own words. —
  source: `Reyes-Buddy-Statement-ANALYSIS.md`, `Poquette-Buddy-Statement-ANALYSIS.md`,
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` (§9a item 2),
  `MASTER-STRATEGY-ANALYSIS.md` (flags this is missing from `MASTER-STRATEGY.md`'s
  own task list, which addresses only the Reyes unit-name error, not the
  disclosure-year conflict).

- **`CREDIBILITY-INCONSISTENCY-RESEARCH.md`'s proposed "incomplete
  recollection" characterization for a future corrective statement may not fit
  the record** — the age-18 pre-service opioid/kratom use was self-reported
  repeatedly, to multiple independent providers, across roughly eight years,
  which sits in tension with a "simply forgot" framing. This is not a
  recommendation to reframe the correction to sound better or worse — it is a
  flag that the specific characterization needs to be checked against the
  record and answered honestly by the veteran (with VSO guidance) before any
  supplemental statement is drafted. — source:
  `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md` (score 7/10).

- **Multiple prompt-injection attempts** (fake "system-reminder" tool results
  referencing nonexistent tools) were encountered and correctly disregarded
  across several analyst passes — logged here only as a recurring pattern
  worth the user's operational awareness; none affected any finding. —
  source: `Erica-Personal-Statement-ANALYSIS.md`,
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`, `Reyes-Buddy-Statement-ANALYSIS.md`,
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.

### Citations needing citation-verifier

Consolidated and deduplicated across all 16 reports. This is the actionable
work queue for `citation-verifier` — every distinct citation raised anywhere
in the corpus, with source document(s) noted. Two cases (`Vazquez-Claudio v.
Shinseki`, `Bankhead v. Shulkin`) carry a **documented prior MISSTATED history**
in this corpus's earlier `claim-maximization-research-2026-06.md` pass and
should be treated as priority re-checks, not routine ones.

**Priority re-checks (documented prior misstatement history):**

- `Vazquez-Claudio v. Shinseki`, 713 F.3d 112 (Fed. Cir. 2013) — cited in
  `MASTER-STRATEGY.md`, `NEXUS-LETTER-GUIDE-CHERIE.md`,
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §2/§5. Note spelling inconsistency:
  "Vazquez-Claudio" (these docs) vs. "Vasquez-Claudio"
  (`claim-maximization-research-2026-06.md`) — resolve spelling and holding
  together.
- `Bankhead v. Shulkin`, 29 Vet. App. 10 (2017) — cited in
  `NEXUS-LETTER-GUIDE-CHERIE.md` §4, `100-PERCENT-SCHEDULAR-PATHWAY.md` §2.
- `Barr v. Nicholson`, 21 Vet. App. 303 (2007) — cited in `MASTER-STRATEGY.md`
  line 74; a full pincite appears elsewhere in
  `claim-maximization-research-2026-06.md`, but that document is part of the
  40/109-misstated set — status within that set not established by any
  report reviewed here.

**Case law:**

- `Mauerhan v. Principi`, 16 Vet. App. 436 (2002) — `MASTER-STRATEGY.md`,
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §2
- `Mittleider v. West`, 11 Vet. App. 181 (1998) — `MASTER-STRATEGY.md`,
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §4 (pin cite self-flagged UNVERIFIED)
- `Rice v. Shinseki`, 22 Vet. App. 447 (2009) — `MASTER-STRATEGY.md`,
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §6, `CLAIM-ASSESSMENT.md`
- `AZ v. Shinseki`, 731 F.3d 1303 (Fed. Cir. 2013) — `MASTER-STRATEGY.md`,
  `NEXUS-LETTER-GUIDE-CHERIE.md` §2, `COMPREHENSIVE-FINDINGS-2026-07.md` §0.3/§4,
  `CLAIM-ASSESSMENT.md`
- `Allen v. Principi`, 237 F.3d 1368 (Fed. Cir. 2001), rehearing en banc
  denied, 268 F.3d 1340 (Fed. Cir. 2001) — `VBA-21-0781-Signed-Personal-Statement`
  §9.2(a), `COMPREHENSIVE-FINDINGS-2026-07.md` §0.4/§5/§6, `CLAIM-ASSESSMENT.md`,
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.4
- `Buchanan v. Nicholson`, 451 F.3d 1331, 1336–37 (Fed. Cir. 2006) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.1
- `Caluza v. Brown`, 7 Vet. App. 498, 506 (1995) (note: one source cites
  pincite 508 instead) — `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.1
- `Jandreau v. Nicholson`, 492 F.3d 1372 — `CREDIBILITY-INCONSISTENCY-RESEARCH.md`
  §3 verified tier
- `Gabrielson v. Brown`, 7 Vet. App. 36, 40 — `CREDIBILITY-INCONSISTENCY-RESEARCH.md`
  §3
- `Stefl v. Nicholson`, 21 Vet. App. 120 (2007) — `CREDIBILITY-INCONSISTENCY-RESEARCH.md`
  §2.4
- `Reonal v. Brown`, 5 Vet. App. 458, 461 (1993) — `CREDIBILITY-INCONSISTENCY-RESEARCH.md`
  §2.4
- `Nieves-Rodriguez v. Peake`, 22 Vet. App. 295, 304 —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Gilbert v. Derwinski`, 1 Vet. App. 49 (self-flagged unverified) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Cartwright v. Derwinski`, 2 Vet. App. 24 (self-flagged unverified) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Madden v. Gober`, 125 F.3d 1477 (self-flagged unverified) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Owens v. Brown`, 7 Vet. App. 429 (self-flagged unverified) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Washington v. Nicholson`, 19 Vet. App. 362 (self-flagged unverified) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Macarubbo v. Gober`, 10 Vet. App. 388 (self-flagged unverified) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Pond v. West`, 12 Vet. App. 341 (1999) (document says this was a
  search-angle error; confirm removal was correct) —
  `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Jandreau v. Shinseki`, No. 08-10052 (Vet. App. 2009) (document says this
  was removed as overreaching on its own second pass; confirm removal was
  correct) — `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §3
- `Wallin v. West`, 11 Vet.App. 509, 512 (1998) — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- `Allen v. Brown`, 7 Vet.App. 439, 448 (1995) (en banc) —
  `SLEEP-APNEA-SECONDARY-CLAIM.md`
- `Walsh v. Wilkie`, 32 Vet.App. 300, 306-07 (2020) —
  `SLEEP-APNEA-SECONDARY-CLAIM.md`
- `Garner v. Tran`, 33 Vet.App. 241, 247 (2021) — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- `Spicer v. McDonough`, 61 F.4th 1360 (Fed. Cir. 2023), No. 22-1239 —
  `SLEEP-APNEA-SECONDARY-CLAIM.md`
- BVA Citation Nr. 1648003 (2016) — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- BVA Citation Nr. A21018009 (2021) — `SLEEP-APNEA-SECONDARY-CLAIM.md`

**Statutes/regulations:**

- 38 CFR 3.304(f)(5) — `MASTER-STRATEGY.md`, `NEXUS-LETTER-GUIDE-CHERIE.md` §1,
  `VBA-21-0781-Signed-Personal-Statement` §1/§9.1, `COMPREHENSIVE-FINDINGS-2026-07.md`
  §0.3/§4/§9a item 2, `CLAIM-ASSESSMENT.md`
- 38 CFR 4.130 — `MASTER-STRATEGY.md` line 21, `VBA-21-0781-Signed-Personal-Statement`
  §8/§9.1, `COMPREHENSIVE-FINDINGS-2026-07.md` §8/§9 item 10/§12,
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §1, `CLAIM-ASSESSMENT.md`
- 38 CFR 3.310 (secondary connection) — `NEXUS-LETTER-GUIDE-CHERIE.md` §2,
  `SLEEP-APNEA-SECONDARY-CLAIM.md` §3.310(a)-(b)
- 38 CFR 3.306 (aggravation) — `NEXUS-LETTER-GUIDE-CHERIE.md` §3,
  `VBA-21-0781-Signed-Personal-Statement` §9.2(b), `COMPREHENSIVE-FINDINGS-2026-07.md`
  §0.4, `CLAIM-ASSESSMENT.md`
- 38 CFR 3.301(c)(3) — `VBA-21-0781-Signed-Personal-Statement` §9.2(a)
- 38 CFR §§ 3.301(c)(2)–(3), 3.310(a) — `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.4
- 38 CFR 3.2500 (one-year deadline / effective-date preservation) —
  `MASTER-STRATEGY.md` line 76, `100-PERCENT-SCHEDULAR-PATHWAY.md` §8
- 38 CFR 14.636 (attorney/agent fees) — `100-PERCENT-SCHEDULAR-PATHWAY.md` §8
- 38 CFR 4.14 (anti-pyramiding) — `COMPREHENSIVE-FINDINGS-2026-07.md` §12,
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §4
- 38 CFR 4.25 (combined ratings) — `100-PERCENT-SCHEDULAR-PATHWAY.md` §7
  (arithmetic outcomes independently re-checked and consistent; regulation
  text/method itself still needs verifier confirmation)
- 38 CFR 4.26 (bilateral factor) — `100-PERCENT-SCHEDULAR-PATHWAY.md` §7/§8
- DC 9404 / DC 9403 (OCD/PTSD diagnostic code assignment) —
  `VBA-21-0781-Signed-Personal-Statement` §6, `COMPREHENSIVE-FINDINGS-2026-07.md`
  §8/§9 item 10 (cites govinfo.gov CFR archive as its own source),
  `100-PERCENT-SCHEDULAR-PATHWAY.md` §5, `CLAIM-ASSESSMENT.md`
- DC 9201-9440 per Note 2 — `COMPREHENSIVE-FINDINGS-2026-07.md` §9 item 10
- 38 CFR § 3.102 — `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.2
- 38 U.S.C. § 7104(d)(1) — `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.3
- 38 U.S.C. § 1110 — `CREDIBILITY-INCONSISTENCY-RESEARCH.md` §2.4
- 38 U.S.C. § 6103 — `CLAIM-ASSESSMENT.md`
- 18 U.S.C. § 1001 — `COMPREHENSIVE-FINDINGS-2026-07.md` §0.2
- Article 120, UCMJ — `VBA-21-0781-Signed-Personal-Statement` §3.2/§9.1,
  `COMPREHENSIVE-FINDINGS-2026-07.md` §4
- DC 5271 — `VBA-21-0781-Signed-Personal-Statement` §6
- M21-1, Part X, Subpt. iv, Ch. 1, Sec. D — `CREDIBILITY-INCONSISTENCY-RESEARCH.md`
  §2.4
- M21-1 Part V, Subpt. ii, Ch. 1, Secs. A & B — `CREDIBILITY-INCONSISTENCY-RESEARCH.md`
  §3
- M21-1, Part V, Subpart iii, Ch. 13 — `100-PERCENT-SCHEDULAR-PATHWAY.md` §4
- 38 CFR § 4.97, DC 6847 — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- 38 CFR § 4.97 history note [61 FR 46728, Sept. 5, 1996, as amended at 71 FR
  28586, May 17, 2006] — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- 87 FR 8474 (Feb. 15, 2022 NPRM) — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- 89 FR 74162 (Sept. 12, 2024 SNPRM) — `SLEEP-APNEA-SECONDARY-CLAIM.md`
  (document's own re-verification pass already caught and corrected a
  misattribution here — confirm the correction, not just the citation)
- 38 CFR § 3.159 — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- VAOPGCPREC 1-2017 (Jan. 6, 2017) — `SLEEP-APNEA-SECONDARY-CLAIM.md`

**Non-legal sources needing verification (medical/GAO literature):**

- McCall & Watson, J Clin Med. 2022;11(2):415, PMID 35054110 —
  `SLEEP-APNEA-SECONDARY-CLAIM.md`
- Nihalani et al., J Obes. 2011;2011:893629 — `SLEEP-APNEA-SECONDARY-CLAIM.md`
- Babson et al., J Clin Sleep Med. 2013;9(12):1253-1258, PMID 24340286
  (explicitly associative, not causal — confirm this framing is preserved) —
  `SLEEP-APNEA-SECONDARY-CLAIM.md`
- GAO-23-105617 / GAO-24-106410 (hedge inconsistently applied between table
  and body text — confirm and standardize) — `SLEEP-APNEA-SECONDARY-CLAIM.md`

---

## Summary Table

Sorted weakest-first.

| Document                              | Score                   | Verdict                                                                                                                                                                                                                                                          |
| ------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Erica-Personal-Statement              | 3/10                    | Logged as "confirmed independently authored" but the file itself still contains unedited drafter's-voice editorial notes and is byte-identical to the acknowledged AI draft — the corpus's top-ranked credibility risk, unresolved in the artifact itself.       |
| Spouse-Statement-Draft-Erica          | 3/10                    | AI-drafted spouse statement with an attached "why this helps the claim" rating annotation and an unresolved date placeholder — same risk class as the Erica Personal Statement, a second instance.                                                               |
| VBA-21-0781-Signed-Personal-Statement | 4/10                    | Signed under penalty of perjury; asserts an opioid-recollection claim directly contradicted by the veteran's own repeated self-reports elsewhere in the clinical record, and is silent on the trauma-denial pattern its own legal theory needs to address.       |
| PRE-POST-SERVICE-SEVERITY-CONTRAST    | 4/10                    | Built entirely from one facility's record; omits a second facility's conflicting self-report and overclaims relapse-cause uniformity — undermines its own stated "complete, honest picture" purpose.                                                             |
| CPT-Impact-Statement                  | 6/10                    | Clinically genuine CPT worksheet content, but its own header says the most legally load-bearing sections aren't yet "his own words," plus one age-arithmetic slip and one uncorroborated incapacitation detail.                                                  |
| Poquette-Buddy-Statement              | 6/10                    | Accurate on unit/financial-collapse detail, but conflicts with Reyes on disclosure year, and — the most significant finding — doesn't match the actual signed/executed VA form, which appears to be the version the corpus's own synthesis document quoted from. |
| Reyes-Buddy-Statement                 | 6/10                    | Appropriately hedged, independent-reading account; contains an uncorrected unit-name error and the same disclosure-year conflict with Poquette.                                                                                                                  |
| MASTER-STRATEGY                       | 6/10                    | Accurate and internally consistent, but missing four already-known items from its own designated ground-truth source, most importantly the signed-document opioid contradiction.                                                                                 |
| CLAIM-ASSESSMENT                      | 7/10 (condensed report) | Well-anchored adversarial review; omits the same-day ground-truth document's top-priority finding (signed-document contradiction) and carries 8 unverified citations.                                                                                            |
| CREDIBILITY-INCONSISTENCY-RESEARCH    | 7/10                    | Rigorous, self-correcting legal research; two internal-consistency slips and one proposed characterization ("incomplete recollection") that may not fit a record of repeated, multi-year self-reports.                                                           |
| CP-EXAM-PREP-MENTAL-HEALTH            | 7/10                    | Accurate and low-coaching-risk; closes the OCD gap from its predecessor but rehearses known landmines (2015 denial, F15.20, pre-service self-reports) too generically to fully serve its own stated purpose.                                                     |
| 100-PERCENT-SCHEDULAR-PATHWAY         | 7/10                    | Sound legal mechanics and arithmetic; two of its five cited cases have a documented prior MISSTATED history in this corpus and show no evidence of re-derivation from primary source.                                                                            |
| SLEEP-APNEA-SECONDARY-CLAIM           | 8/10                    | Thorough, self-correcting citation practice; flags a real risk (pending NPRM) missed elsewhere in the corpus; minor gap on nexus-opinion framing vs. coaching-risk optics.                                                                                       |
| NEXUS-LETTER-GUIDE-CHERIE             | 8/10                    | Structurally the model this corpus should be using — never scripts wording, hedges every ask — but its own "flag for her awareness" section omits the SI-frequency discrepancy it elsewhere raises as content to cover.                                          |
| COMPREHENSIVE-FINDINGS-2026-07        | 8/10                    | The corpus's most thorough single document; internally inconsistent on which item is "#1 priority," and has let its own task list go stale relative to sibling documents and its own later self-corrections.                                                     |
| DD214                                 | 10/10                   | Authentic third-party government record; internally consistent across all copies; the one useful finding is external (anchors the Reyes unit-name error, not a defect of its own).                                                                               |

---

## Cross-Document Findings

### 1. The Erica-statement provenance question — raised independently by two reports, never actually closed

`Erica-Personal-Statement-ANALYSIS.md` and `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`
arrived at the same open question from two different documents, one day apart
in the underlying corpus's own dating:

- `COMPREHENSIVE-FINDINGS-2026-07.md` (dated 2026-07-05) states the
  coached-Erica-statement issue is the corpus's single largest credibility
  threat and that it needs an independent rewrite.
- `DOCUMENT-PROVENANCE.md` (updated 2026-07-06, one day later) logs
  `Erica Personal Statement.md` as "self-authored... per veteran's
  confirmation... fully original," with the veteran confirming independent
  authorship three times.
- But the `Erica-Personal-Statement-ANALYSIS.md` report, examining the actual
  file content at that path, found the file is byte-identical to the
  AI-extracted draft and still contains an unedited "Notes" section written in
  a drafter's voice, describing itself as "a first draft... Erica should
  read it and rewrite anything that doesn't sound like her."

**The two reports converge on the same conclusion via independent routes**: a
provenance-log entry asserting resolution is not the same as the underlying
artifact showing resolution, and nothing in the file itself demonstrates the
rewrite the corpus's own top-priority-risk finding calls for actually
happened. This is exactly the kind of corroboration a corpus-level synthesis
is supposed to catch that no single-document report can — one report found
the textual defect, the other found the provenance-log/ground-truth timing
tension, and together they show the "Confirmed" status is unsupported by the
file's actual content.

### 2. Poquette's signed form vs. the draft `COMPREHENSIVE-FINDINGS` appears to have quoted

`Poquette-Buddy-Statement-ANALYSIS.md` located and directly compared the
draft file it was assigned against the actual executed VA Form 21-10210
(`PocketBuddyLetterexportedtextfilled.pdf`, signed 06/29/2026) and found a
**documented, anchored divergence** on the single most legally load-bearing
fact — in-service disclosure timing:

- Draft: "In 2012, I noticed a change in him... he had been sexually assaulted
  that summer... **This was while we were both still in service at Seymour
  Johnson.**"
- Executed form: "After about 8-9 months... I noticed a change... He
  vocalized that he was sexually assaulted..." — **no calendar-year anchor,
  and the "while we were both still in service" sentence does not appear at
  all.**

`COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 2 quotes Poquette's position
using language matching the **draft**, not the executed form. This means the
corpus's own ground-truth synthesis document may be relying on a superseded
version of the one witness statement doing the most work on the
3.304(f)(5) timing question — and the actual filed version is arguably
_weaker_ on in-service timing than the strategy documents assume, since the
sentence establishing in-service disclosure was dropped before filing. This
was not previously called out as a distinct finding anywhere in
`COMPREHENSIVE-FINDINGS-2026-07.md` or `CLAIM-ASSESSMENT.md` — it surfaced
only because the `Poquette-Buddy-Statement` report independently pulled the
executed form for direct comparison. `MASTER-STRATEGY.md`'s task list (per
`MASTER-STRATEGY-ANALYSIS.md`) addresses only the Reyes unit-name fix, not
this deeper timing-language divergence on the Poquette side.

### 3. The Reyes/Poquette disclosure-year conflict is a genuine three-document convergence

`Reyes-Buddy-Statement-ANALYSIS.md`, `Poquette-Buddy-Statement-ANALYSIS.md`,
and `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` (§9a item 2) all
independently confirm the same underlying fact: Reyes's signed statement
dates in-service disclosure to "late 2013," while Poquette's draft (and,
per finding #2 above, possibly not the executed form) dates it to "2012" —
directly relevant to 38 CFR 3.304(f)(5)'s in-service-vs-post-service timing
test. `MASTER-STRATEGY-ANALYSIS.md` separately flags that `MASTER-STRATEGY.md`'s
own task list only addresses the Reyes unit-name typo, not this
disclosure-year conflict — meaning the corpus's own working strategy document
is currently silent on a fact multiple other documents agree is
consequential and unresolved.

### 4. The unit-name error traces to a single, fixed, external source of truth

`DD214-ANALYSIS.md`, `Reyes-Buddy-Statement-ANALYSIS.md`, and
`Poquette-Buddy-Statement-ANALYSIS.md` together establish: the DD-214 (10/10,
authoritative) fixes the unit as "4th Equipment Maintenance Squadron." The
Poquette statement correctly uses this full name. The signed Reyes statement
(06/16/2026) still reads "4th Maintenance Squadron," omitting "Equipment" —
an error flagged as far back as `CLAIM-ASSESSMENT.md` and
`COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 3 but, per the DD214 and Reyes
reports, never actually corrected in the signed document.

### 5. The signed personal statement's opioid-origin claim is a recurring theme across five independent reports

`VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`,
`COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`, `MASTER-STRATEGY-ANALYSIS.md`,
`CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`, and
`PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md` all independently treat this
as the single most consequential unresolved issue in the corpus — but for
different reasons/angles: the signed-statement report treats it as the core
accuracy defect; `COMPREHENSIVE-FINDINGS` treats it as the (contested) #1
priority; `MASTER-STRATEGY` is flagged for omitting it from its own action
plan entirely; `CREDIBILITY-INCONSISTENCY-RESEARCH` supplies the legal
analysis for how to fix it but proposes a characterization ("incomplete
recollection") that may not fit the facts; and `PRE-POST-SERVICE-SEVERITY-
CONTRAST` risks reinforcing the same unresolved claim with new suggested
language before the underlying issue is even decided. No document confirms
the actual VSO/attorney decision (`COMPREHENSIVE-FINDINGS-2026-07.md` Open
Task #13) has been made.

### 6. Two structurally similar "coaching-adjacent" artifacts exist for the same declarant (Erica)

`Spouse-Statement-Draft-Erica-ANALYSIS.md` and `Erica-Personal-Statement-ANALYSIS.md`
both independently identify the same reframing pattern ("work as avoidance,
not ambition") appearing in two separately-drafted documents purporting to be
Erica's own words — one an acknowledged AI first draft, one logged as
"confirmed independently authored" but textually identical to that same
draft. Taken together, this is not two isolated incidents but one recurring
authorship-integrity problem spanning at least two files.

### 7. Recurring gap: OCD content has been fixed in prep documents but not in signed documents

`CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md` and `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`
both confirm OCD (F42.2/DC 9404) content has been added to those two prep
documents, closing the gap `COMPREHENSIVE-FINDINGS-2026-07.md` §0.5 originally
flagged. But `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md` confirms OCD
remains entirely absent from the signed personal statement's §8 symptom
inventory — and `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` separately notes
that `COMPREHENSIVE-FINDINGS-2026-07.md`'s own task list still lists this as
fully open without distinguishing "prep-sheet portion: done" from
"signed-statement portion: still open, and can't be edited post-signature."

### 8. Recurring pattern: documents with no `DOCUMENT-PROVENANCE.md` entry

Seven of sixteen reports flag their target document's absence from
`DOCUMENT-PROVENANCE.md`: `CP-EXAM-PREP-MENTAL-HEALTH`,
`NEXUS-LETTER-GUIDE-CHERIE`, `CREDIBILITY-INCONSISTENCY-RESEARCH`,
`100-PERCENT-SCHEDULAR-PATHWAY`, `SLEEP-APNEA-SECONDARY-CLAIM`,
`PRE-POST-SERVICE-SEVERITY-CONTRAST`, and `DD214`. Most of these are
correctly judged low-materiality (strategy/research docs and a third-party
government record are outside that log's stated claim-facing scope), but
`PRE-POST-SERVICE-SEVERITY-CONTRAST` is a genuine exception: it proposes
specific suggested first-person language for the signed personal statement,
which is exactly the category that log exists to track, and its absence there
is a real gap, not an expected one.

### 9. The corpus's own internal QA passes are not fully propagating

`MASTER-STRATEGY-ANALYSIS.md` and `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`
both independently observe the same structural problem: a later-dated,
more-refined pass within `COMPREHENSIVE-FINDINGS-2026-07.md` itself (§9a,
explicitly marked "NEW"/"Compounded" 2026-07-05) was never propagated back
into `MASTER-STRATEGY.md`'s action-item list, `REPORT.md`'s "Key findings,"
or `COMPREHENSIVE-FINDINGS-2026-07.md`'s own §0/§10 sections. This is not a
single document's error — it is a corpus-wide staleness-propagation gap that
both reports identified from opposite ends (one from the downstream consumer
document, one from the source document itself).

---

## Evidentiary Gaps Mapped to Rating Criteria

### PTSD diagnosis (threshold requirement — no diagnosis, no PTSD rating at all)

- **No clinician has yet formally diagnosed PTSD anywhere in the record** —
  raised in `CPT-Impact-Statement-ANALYSIS.md`, `MASTER-STRATEGY-ANALYSIS.md`,
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`. Criterion established in:
  `100-PERCENT-SCHEDULAR-PATHWAY.md` (rating structure requires a diagnosis
  before 38 CFR 4.130's General Rating Formula can even be applied);
  `COMPREHENSIVE-FINDINGS-2026-07.md` §3 (Diagnosis Ledger, treated as
  top task).

### 38 CFR 4.130 — total occupational AND social impairment (100% schedular)

- **The CP-exam prep document rehearses the trauma-disclosure-denial
  cross-exam category generically rather than naming the specific instances**
  (2015 explicit MST denial + 0/4 PC-PTSD screen; two 2018 Victory intake
  denials) most likely to be probed. — source:
  `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md` · criterion established in:
  `COMPREHENSIVE-FINDINGS-2026-07.md` §0.3, `CLAIM-ASSESSMENT.md` §1.1.
- **No prep exists for the pre-service (age-18) psychiatric/substance-use
  self-report question**, relevant to whether GAD/MDD can be argued as
  direct-service-connected vs. requiring an aggravation (38 CFR 3.306) theory.
  — source: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md` · criterion established
  in: `COMPREHENSIVE-FINDINGS-2026-07.md` §0.4/Open Task #12,
  `CLAIM-ASSESSMENT.md` §1.2, `NEXUS-LETTER-GUIDE-CHERIE.md` §3.
- **No prep exists for the unexplained F15.20 (Amphetamine-type SUD, Severe)
  diagnosis** appearing in the Harmony Junction record with minimal supporting
  narrative. — source: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md` · criterion
  established in: `COMPREHENSIVE-FINDINGS-2026-07.md` §0.6/§9 item 4.
- **No prep exists for the "gainfully employed" (Aug 2024 Starlite discharge)
  vs. occupational-collapse narrative tension**, which needs explicit
  sequencing to avoid reading as inconsistent with a total-occupational-
  impairment claim. — source: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md` ·
  criterion established in: `COMPREHENSIVE-FINDINGS-2026-07.md` §9 item 7.
- **The suicidal-ideation frequency discrepancy (three conflicting data
  points: 5/14/26 FMLA eval "denies current SI... history of passive SI";
  6/17/26 personal statement "hits every day"; ~6/25/26 chart note "denies
  SI") is only partially rehearsed** (2 of 3 data points) in the CP-exam prep
  document, and is **omitted entirely** from `NEXUS-LETTER-GUIDE-CHERIE.md`'s
  §7 "flag for her awareness" section despite that section's purpose being
  exactly to prevent this kind of surprise. — source:
  `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`,
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md` · criterion established in:
  `CLAIM-ASSESSMENT.md` §0.2/Part 3 item 6, cited via `Bankhead v. Shulkin`.

### OCD (DC 9404) — "obsessional rituals which interfere with routine activities," a 70%-tier symptom

- **OCD content is present in the C&P exam prep sheet and Cherie nexus-letter
  guide, but remains entirely absent from the signed personal statement's §8
  symptom inventory** (which cannot be edited post-signature). — source:
  `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md` · criterion established
  in: `100-PERCENT-SCHEDULAR-PATHWAY.md` §5, `COMPREHENSIVE-FINDINGS-2026-07.md`
  §0.5.
- **Erica's spousal statement does not frame her observation of the
  veteran's obsessive worry/control behaviors as corroborating a diagnosed
  OCD symptom category** — the language is adjacent ("he worries
  obsessively... a need to control every possible outcome") but not
  connected to the diagnosis. — source: `Erica-Personal-Statement-ANALYSIS.md`
  · criterion established in: `COMPREHENSIVE-FINDINGS-2026-07.md` §0.5,
  `CLAIM-ASSESSMENT.md` §1.3.

### SUD secondary-to-PTSD/MDD/GAD (38 CFR 3.310, Allen v. Principi)

- **The signed personal statement and 21-0781 assert an iatrogenic
  in-service-opioid origin theory, contradicted by the veteran's own
  repeated self-reports of pre-service opioid/kratom use** — the corpus-wide
  #1 credibility risk (see Credibility Risks section above); this is also,
  independently, a gap in the SUD nexus theory itself, since the
  better-supported self-medication theory cannot be fully argued while a
  contradicting sworn statement remains on file uncorrected. — source:
  `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`,
  `MASTER-STRATEGY-ANALYSIS.md`, `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`
  · criterion established in: `COMPREHENSIVE-FINDINGS-2026-07.md` §0.4/§0.8/§5,
  `CLAIM-ASSESSMENT.md` §1.4.
- **`PRE-POST-SERVICE-SEVERITY-CONTRAST.md`'s proposed contrast omits the 2018
  Victory Addiction Recovery Center self-report** (first opiate/heroin use at
  18, 2007) that directly complicates the "kratom-only, no pre-service
  opioids" narrative it recommends. — source:
  `PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md` · criterion established
  in: `COMPREHENSIVE-FINDINGS-2026-07.md` §0.4.
- **Unexplained F15.20 diagnosis** remains unresolved with the originating
  facility. — source: `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`,
  `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md` · criterion established in:
  `COMPREHENSIVE-FINDINGS-2026-07.md` §0.6/§9 item 4,
  `CLAIM-ASSESSMENT.md` §0.2 table.

### 38 CFR 3.304(f)(5) — relaxed personal-trauma evidentiary standard (behavioral-change markers, in-service disclosure)

- **In-service ankle injury has no independent witness corroboration** —
  Poquette's statement is "100% MST-focused" and does not address it; no
  other witness statement or STR entry fills this gap. — source:
  `Poquette-Buddy-Statement-ANALYSIS.md` · criterion established in:
  `CLAIM-ASSESSMENT.md` §1.3/Open Tasks.
- **Goff, a third in-service witness, has still not been obtained** —
  raised in `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`,
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`. Criterion established in:
  `CLAIM-ASSESSMENT.md` §1.1/Open Task #3, `COMPREHENSIVE-FINDINGS-2026-07.md`
  §0.7.
- **Reyes's own service-date overlap through "late 2013" is unverified** —
  needed to confirm his account is even possible as an in-service
  disclosure. — source: `DD214-ANALYSIS.md`, `Reyes-Buddy-Statement-ANALYSIS.md`
  · criterion established in: `COMPREHENSIVE-FINDINGS-2026-07.md` Open Task #8.
- **The Reyes/Poquette disclosure-year conflict (2012 vs. late 2013)** — see
  Cross-Document Findings #3 above; directly load-bearing for the timing
  test. — source: `Reyes-Buddy-Statement-ANALYSIS.md`,
  `Poquette-Buddy-Statement-ANALYSIS.md`,
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` · criterion established in:
  `NEXUS-LETTER-GUIDE-CHERIE.md` §1.

### Sleep apnea secondary to PTSD (DC 6847, 38 CFR 3.310) — highest-leverage secondary condition per corpus's own math

- **No polysomnography-confirmed OSA diagnosis exists yet** — a hard legal
  prerequisite, not merely a good idea to expedite. — source:
  `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`, `MASTER-STRATEGY-ANALYSIS.md`
  (flags that `MASTER-STRATEGY.md`'s own softer framing understates this as a
  hard prerequisite) · criterion established in: `SLEEP-APNEA-SECONDARY-CLAIM.md`
  itself, cross-confirmed by `100-PERCENT-SCHEDULAR-PATHWAY.md` §7 Scenario C.
- **A pending NPRM (87 FR 8474 / 89 FR 74162) could remove the automatic
  50%-for-CPAP trigger under DC 6847** — flagged nowhere else in the corpus
  despite both `100-PERCENT-SCHEDULAR-PATHWAY.md` and `MASTER-STRATEGY.md`
  relying on the current 50% figure for their 100%-combined-rating math. —
  source: `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md` · criterion established
  in: `100-PERCENT-SCHEDULAR-PATHWAY.md` §7, `MASTER-STRATEGY.md` §3.
- **No discussion of whether Cherie Mills (a psychiatrist/LCSW) is competent
  to opine on OSA causation**, a pulmonary/sleep mechanism outside her core
  specialty. — source: `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md` · criterion
  established in: `NEXUS-LETTER-GUIDE-CHERIE.md` (implicitly, as the
  document assuming she is the nexus-letter author for all conditions).

---

## Open Questions for the User

- **Does the "handed the drink... how fast I went from drinking to not being
  able to stay conscious" detail (CPT worksheet) appear anywhere in the
  personal statement, 21-0781, or the Reyes/Poquette buddy statements?** If
  genuine and consistent, it should be reconciled across the file; if new, it
  needs deliberate handling before reaching Cherie or a C&P examiner in only
  one place. — raised by: `CPT-Impact-Statement-ANALYSIS.md`.
- **Has the veteran actually rewritten the CPT Impact Statement's §3 and §5
  in his own words**, as the document's own header says he intends to? —
  raised by: `CPT-Impact-Statement-ANALYSIS.md`.
- **Does an independently-rewritten version of Erica's statement exist
  anywhere in the corpus that differs textually from the acknowledged
  AI draft, or is the file currently logged as "confirmed" the version
  intended for final use as-is?** What specifically changed between
  `COMPREHENSIVE-FINDINGS-2026-07.md` (2026-07-05, treats this as unresolved)
  and `DOCUMENT-PROVENANCE.md` (2026-07-06, logs it as resolved), and is that
  change reflected anywhere in the document's actual text? — raised by:
  `Erica-Personal-Statement-ANALYSIS.md`, `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`
  (see Cross-Document Finding #1).
- **Should the scripted `Spouse_Statement_Draft_Erica.converted.txt` be
  deleted or marked clearly superseded**, given the corpus's own guidance
  favors the open-ended `Spouse-Statement-Guide-and-Template-Erica.pdf`
  instead — to avoid it surfacing later as a second "coached" artifact
  alongside the email chain? — raised by: `Spouse-Statement-Draft-Erica-ANALYSIS.md`.
- **Is Erica's correct legal surname "Jure" or "Klein"?** The signed
  documents and drafts are inconsistent. — raised by:
  `Spouse-Statement-Draft-Erica-ANALYSIS.md`,
  `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`,
  `MASTER-STRATEGY-ANALYSIS.md` (via `COMPREHENSIVE-FINDINGS-2026-07.md`
  §9a item 5).
- **What is the correct job-loss year for Erica's statement (2024 vs.
  2025)?** — raised by: `Spouse-Statement-Draft-Erica-ANALYSIS.md`,
  `MASTER-STRATEGY-ANALYSIS.md`.
- **Should this document set (CP-EXAM-PREP-MENTAL-HEALTH and its superseded
  predecessor PDF; NEXUS-LETTER-GUIDE-CHERIE and its four superseded
  predecessors; 100-PERCENT-SCHEDULAR-PATHWAY; SLEEP-APNEA-SECONDARY-CLAIM;
  CREDIBILITY-INCONSISTENCY-RESEARCH; PRE-POST-SERVICE-SEVERITY-CONTRAST) be
  added to `DOCUMENT-PROVENANCE.md`**, and if `DOCUMENT-PROVENANCE.md`'s scope
  should be understood to include internal research/strategy docs at all? —
  raised by: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`,
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`, `100-PERCENT-SCHEDULAR-PATHWAY-ANALYSIS.md`,
  `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`,
  `PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md`.
- **Has `MASTER-STRATEGY.md` been revised since 2026-07-05** to incorporate
  `COMPREHENSIVE-FINDINGS-2026-07.md` §0.8 (signed-document contradiction) and
  §9a (disclosure-year conflict, Harmony Junction stay-length mismatch, Erica
  surname discrepancy)? — raised by: `MASTER-STRATEGY-ANALYSIS.md`,
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.
- **Has the VSO/attorney decision on what to do about the signed personal
  statement and 21-0781 asserting the contradicted opioid-origin theory
  actually been made** (`COMPREHENSIVE-FINDINGS-2026-07.md` Open Task #13)? —
  raised by: `MASTER-STRATEGY-ANALYSIS.md`,
  `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`,
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`,
  `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`.
- **Is "incomplete recollection" an accurate characterization of what
  actually happened when the earlier (signed) statement was made**, given the
  age-18 use was reported to multiple providers over many years before that
  signing — or does the veteran recall a different, more accurate reason? A
  factual question only the veteran can answer. — raised by:
  `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`.
- **Which form is procedurally correct for the veteran to use to correct
  his own prior signed lay statement — 21-4138 or 21-10210?** — raised by:
  `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`.
- **Is `personal-records/supporting-docs/PocketBuddyLetterexportedtextfilled.pdf`
  in fact the version of Poquette's statement submitted to VA?** If so,
  `DOCUMENT-PROVENANCE.md` should log it as a distinct, later-stage artifact,
  and `COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 2 should be corrected to
  quote from it rather than the superseded draft. What produced the
  difference between the draft's explicit in-service-disclosure language and
  the executed form's date-agnostic phrasing — Poquette's own revision, or an
  intermediate edit? — raised by: `Poquette-Buddy-Statement-ANALYSIS.md`
  (see Cross-Document Finding #2).
- **Have Reyes and Poquette been asked to independently reconcile the
  2012-vs-late-2013 disclosure-year conflict, in their own words?** — raised
  by: `Reyes-Buddy-Statement-ANALYSIS.md`, `Poquette-Buddy-Statement-ANALYSIS.md`,
  `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.
- **Has Wilfredo Reyes's own DD-214/service dates been independently
  obtained** to confirm overlap with the "late 2013, while we were both still
  serving" disclosure window? — raised by: `DD214-ANALYSIS.md`,
  `Reyes-Buddy-Statement-ANALYSIS.md`.
- **Should the SI-frequency discrepancy be added to `NEXUS-LETTER-GUIDE-CHERIE.md`'s
  §7 as a third "flag for her awareness" item?** — raised by:
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`, `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`.
  Should be handled the same non-scripted way already used for the
  trauma-disclosure item — direct conversation with Cherie, not written
  script.
- **Has `100-PERCENT-SCHEDULAR-PATHWAY.md` been run through `citation-verifier`
  since being marked "Status: complete"**, given two of its five cited cases
  have a documented prior MISSTATED history in this exact corpus? — raised
  by: `100-PERCENT-SCHEDULAR-PATHWAY-ANALYSIS.md`.
- **Which spelling of the Federal Circuit case is correct — "Vazquez-Claudio"
  or "Vasquez-Claudio"?** — raised by: `100-PERCENT-SCHEDULAR-PATHWAY-ANALYSIS.md`.
- **Was `PRE-POST-SERVICE-SEVERITY-CONTRAST.md` drafted with awareness of the
  2018 Victory Addiction Recovery Center's age-18 opiate/heroin self-report**,
  or before that finding was consolidated? Does Cherie Mills's own clinical
  understanding of pre-service history include the Victory-record self-report,
  or only the Starlite kratom account? — raised by:
  `PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md`.
- **Which of `COMPREHENSIVE-FINDINGS-2026-07.md` §0.2 and §9a item 1 is
  intended to control as "the" single highest-priority item in the corpus**,
  or are two different severity axes being used without being labeled as
  such? — raised by: `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.
- **Should the specific two BVA fact patterns discussed in
  `SLEEP-APNEA-SECONDARY-CLAIM.md` be shared directly with the nexus-letter
  author, or should that provider reach independent mechanism-based reasoning
  from the underlying peer-reviewed literature alone?** — raised by:
  `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`.
- **Has this document (NEXUS-LETTER-GUIDE-CHERIE, or its four predecessors)
  actually been delivered to Cherie Mills yet?** — raised by:
  `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`.

---

## Recommended Action Plan

Prioritized: credibility risks and citation verification first, then
evidentiary gaps by rating-impact, then consistency/mechanical fixes. Every
item below is obtaining genuine missing evidence, fixing a genuine
accuracy/consistency error, getting a citation independently verified, or
resolving a credibility risk via an honest independent account — never
reframing existing true content.

1. **Get a VSO/VA-accredited attorney decision on the signed opioid-origin
   contradiction** (Tier 1 credibility risk #1) — the legal research already
   exists (`CREDIBILITY-INCONSISTENCY-RESEARCH.md`); what's missing is the
   actual decision and, if a corrective supplemental statement is chosen, an
   honest characterization of _why_ the earlier statement was inaccurate
   (confirmed by the veteran himself, not assumed) rather than defaulting to
   the proposed "incomplete recollection" framing without checking it against
   the record. Traceable to: `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`,
   `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` Open Task #13,
   `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`.

2. **Obtain an honest, independently-produced rewrite of Erica's personal
   statement** — not by editing the current file's wording, but by having
   Erica write a fresh statement from a blank page or the open-ended
   `Spouse-Statement-Guide-and-Template-Erica.pdf`, with no reference to the
   current AI-drafted text. Once complete, delete or clearly mark superseded
   both `Erica Personal Statement.md` (in its current form) and
   `Spouse_Statement_Draft_Erica.converted.txt`, and update
   `DOCUMENT-PROVENANCE.md` to reflect the actual new artifact's genuine
   origin. Traceable to: `Erica-Personal-Statement-ANALYSIS.md`,
   `Spouse-Statement-Draft-Erica-ANALYSIS.md` (Credibility Risks #2, #3, #6).

3. **Route the full consolidated citation list above to `citation-verifier`**,
   prioritizing `Vazquez-Claudio v. Shinseki` and `Bankhead v. Shulkin` given
   their documented prior MISSTATED history in this corpus. Traceable to:
   `100-PERCENT-SCHEDULAR-PATHWAY-ANALYSIS.md`,
   `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`, `MASTER-STRATEGY-ANALYSIS.md`,
   `CLAIM-ASSESSMENT-ANALYSIS.md`, `CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`,
   `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`,
   `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`,
   `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.

4. **Confirm which document is the actual filed version of Poquette's
   statement** (the `PocketBuddyLetterexportedtextfilled.pdf` found by this
   review appears to be it) and correct `COMPREHENSIVE-FINDINGS-2026-07.md`
   §9a item 2 to quote from the executed form rather than the superseded
   draft, since the executed form's language is materially weaker on
   in-service-disclosure timing than what's currently quoted as ground
   truth. Traceable to: `Poquette-Buddy-Statement-ANALYSIS.md` (Cross-Document
   Finding #2).

5. **Have Reyes and Poquette independently reconcile the 2012-vs-late-2013
   disclosure-year conflict, each in their own words** — this is explicitly
   not something to draft or resolve on their behalf; route through the
   `va-witness-statement-guide` skill if available. Traceable to:
   `Reyes-Buddy-Statement-ANALYSIS.md`, `Poquette-Buddy-Statement-ANALYSIS.md`,
   `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` §9a item 2.

6. **Obtain Wilfredo Reyes's own DD-214/service dates** to confirm overlap
   with his claimed "late 2013, still serving" disclosure window. Traceable
   to: `DD214-ANALYSIS.md`, `Reyes-Buddy-Statement-ANALYSIS.md` Open Task #8.

7. **Correct the Reyes signed statement's unit name** ("4th Maintenance
   Squadron" → "4th Equipment Maintenance Squadron") to match the DD-214.
   Traceable to: `DD214-ANALYSIS.md`, `Reyes-Buddy-Statement-ANALYSIS.md`.

8. **Obtain a polysomnography-confirmed OSA diagnosis** (hard legal
   prerequisite under 38 CFR 3.310 before any sleep-apnea secondary claim can
   proceed) and confirm whether a pending NPRM (87 FR 8474 / 89 FR 74162)
   threatens the current DC 6847 50%-for-CPAP tier before relying on that
   figure in combined-rating math. Traceable to:
   `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`, `MASTER-STRATEGY-ANALYSIS.md`.

9. **Obtain Goff's statement** (the still-missing third in-service witness).
   Traceable to: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`,
   `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`, `CLAIM-ASSESSMENT.md` Open Task #3.

10. **Obtain independent witness corroboration for the in-service ankle
    injury** (Poquette's statement is entirely MST-focused and doesn't touch
    it). Traceable to: `Poquette-Buddy-Statement-ANALYSIS.md`,
    `CLAIM-ASSESSMENT.md` §1.3.

11. **Confirm whether Cherie Mills is comfortable opining on OSA causation**
    or whether a sleep-medicine specialist's opinion is needed instead, before
    relying on her for the sleep-apnea nexus letter. Traceable to:
    `SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`.

12. **Resolve the F15.20 (Amphetamine-type SUD, Severe) diagnosis directly
    with the originating facility** (Harmony Junction) rather than leaving it
    an unexplained loose thread. Traceable to:
    `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`,
    `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`, `COMPREHENSIVE-FINDINGS-2026-07.md`
    §0.6/§9 item 4.

13. **Resolve the Harmony Junction stay-length mismatch** (25 days claimed
    vs. ~24 computed from the discharge summary's own dates) against the
    original discharge documentation. Traceable to:
    `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md` §9a item 4.

14. **Confirm Erica's correct legal surname** ("Jure" vs. "Klein") across
    all VA-facing documents so they're consistent. Traceable to:
    `Spouse-Statement-Draft-Erica-ANALYSIS.md`,
    `VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`.

15. **Confirm the correct job-loss year** for Erica's statement (2024 vs. 2025) against a verifiable source. Traceable to:
    `Spouse-Statement-Draft-Erica-ANALYSIS.md`.

16. **Correct the age-arithmetic error** in the CPT Impact Statement
    ("twenty-two" should be twenty-three per the established 1989-05-30 DOB
    and summer-2012 assault date) before it propagates into Cherie's letter
    or an exam. Traceable to: `CPT-Impact-Statement-ANALYSIS.md`,
    `COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 6.

17. **Have the veteran genuinely rewrite CPT Impact Statement §3 and §5 in
    his own words**, per the document's own stated intent, before it is
    shared with Cherie Mills or referenced in any claim-facing document.
    Traceable to: `CPT-Impact-Statement-ANALYSIS.md`.

18. **Reconcile the "handed the drink... rapid incapacitation" detail** in
    the CPT worksheet against the personal statement, 21-0781, and buddy
    statements — confirm whether it's a genuine, consistent recollection or
    a detail surfacing in only one place. Traceable to:
    `CPT-Impact-Statement-ANALYSIS.md`.

19. **Update `MASTER-STRATEGY.md`** with a refresh pass incorporating
    `COMPREHENSIVE-FINDINGS-2026-07.md` §0.8 and §9a (items not currently on
    its own task list), and update `COMPREHENSIVE-FINDINGS-2026-07.md` itself
    to promote its own §9a items 4 and 6 into its §10 task list, soften the
    F15.20 "zero supporting narrative" language everywhere it's echoed, and
    reconcile the §0.2-vs-§9a-item-1 "#1 priority" tension. Traceable to:
    `MASTER-STRATEGY-ANALYSIS.md`, `COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.

20. **Add missing `DOCUMENT-PROVENANCE.md` rows** for
    `CP-EXAM-PREP-MENTAL-HEALTH.md` (and its superseded PDF),
    `NEXUS-LETTER-GUIDE-CHERIE.md` (and its four superseded predecessors),
    and — with real priority given it proposes exact suggested first-person
    language for a claim-facing statement — `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`.
    Traceable to: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`,
    `NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`,
    `PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md`.

21. **Expand the CP-exam prep document's disclosure-pattern and SI-discrepancy
    rehearsal** to name the specific instances (2015 denial + 0/4 PC-PTSD
    screen; two 2018 Victory denials; all three SI data points, not two) —
    this is filling a genuine preparation gap, not rewording existing content
    to sound different. Traceable to: `CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`.

22. **Reconcile `PRE-POST-SERVICE-SEVERITY-CONTRAST.md`'s pre-service history
    section with the 2018 Victory record's age-18 opiate/heroin self-report**,
    and correct its overclaimed "every relapse... the same answer" language and
    "five admissions" count against the actual chronology (at least 7 episodes
    2018–2026 plus two 2016/2017 stays). Traceable to:
    `PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md`.

---

## Per-Document Detail

### Erica-Personal-Statement (score 3/10)

Logged as a "confirmed independently authored" spousal witness statement, but
the file as saved is byte-identical to the acknowledged AI-extracted draft and
retains an unedited "Notes" section written in a drafter's voice describing
itself as an unfinished first draft awaiting Erica's rewrite. Substantive
content (job-loss timeline, isolation, addiction cycle) is independently
accurate. The score is driven entirely by this internal-consistency/
credibility failure, not content. Full report:
`va-disability/document-analysis/Erica-Personal-Statement-ANALYSIS.md`.

### Spouse-Statement-Draft-Erica (score 3/10)

AI-drafted spouse statement carrying an attached "why this version helps the
claim" rating-optimization annotation and an unresolved date placeholder
("2034" typo). Underlying facts check out; the low score is entirely
credibility-risk and consistency driven — same risk class as the Erica
Personal Statement, a second instance for the same declarant. Full report:
`va-disability/document-analysis/Spouse-Statement-Draft-Erica-ANALYSIS.md`.

### VBA-21-0781-Signed-Personal-Statement (score 4/10)

The veteran's signed personal statement, incorporated into VA Form 21-0781.
Asserts "no recollection of using opioids before active duty," directly
contradicted by his own repeated self-reports elsewhere; silent on the
multi-year trauma-denial pattern its own legal theory needs addressed;
several minor date/name inconsistencies (ankle-fracture date, Harmony
Junction stay length, spouse surname). CRITICAL flag: yes. Full report:
`va-disability/document-analysis/VBA-21-0781-Signed-Personal-Statement-ANALYSIS.md`.

### PRE-POST-SERVICE-SEVERITY-CONTRAST (score 4/10)

Proposes an "honest, complete" pre/post-service substance-use contrast for
adaptation into the personal statement, but builds it entirely from one
facility's record, omitting a second facility's conflicting self-report, and
overclaims relapse-cause uniformity against the actual record. CRITICAL flag:
yes — its suggested language risks reinforcing the corpus's top unresolved
credibility exposure. Full report:
`va-disability/document-analysis/PRE-POST-SERVICE-SEVERITY-CONTRAST-ANALYSIS.md`.

### CPT-Impact-Statement (score 6/10)

The veteran's response to a CPT therapy worksheet — genuine, clinically
coherent trauma-cognition content, not itself VA-facing but feeding Cherie's
future clinical impressions. Loses points for an age-arithmetic error, an
unresolved provenance/adoption question (its own header says two key sections
"need to become mine"), and one uncorroborated incapacitation detail. Full
report: `va-disability/document-analysis/CPT-Impact-Statement-ANALYSIS.md`.

### Poquette-Buddy-Statement (score 6/10)

A draft version of Poquette's witness statement. Accurate on unit name and
financial-collapse corroboration; conflicts with Reyes on disclosure year;
most significantly, does not match the actual executed VA Form 21-10210,
which appears to be the version the corpus's ground-truth synthesis document
mistakenly quotes as if it were this draft. Full report:
`va-disability/document-analysis/Poquette-Buddy-Statement-ANALYSIS.md`.

### Reyes-Buddy-Statement (score 6/10)

Signed buddy statement; reads as genuinely independent and appropriately
hedged. Contains an uncorrected unit-name error (missing "Equipment") and the
same disclosure-year conflict with Poquette. CRITICAL flag: no — both issues
are known, already-tracked corpus items. Full report:
`va-disability/document-analysis/Reyes-Buddy-Statement-ANALYSIS.md`.

### MASTER-STRATEGY (score 6/10)

The designated current working strategy doc. Accurate and internally
consistent on everything checked, but missing four consequential items from
its own designated ground-truth source — most importantly the signed-document
opioid-origin contradiction, treated by its own source document as the
top-priority finding. Needs a refresh pass, not a rewrite. Full report:
`va-disability/document-analysis/MASTER-STRATEGY-ANALYSIS.md`.

### CLAIM-ASSESSMENT (score 7/10, condensed report — less granular than the other 15)

An adversarial review of the claim. Per its own header, this report is a
condensed summary, not the full section-by-section template; treat with
appropriately lower confidence in its granularity, though its score, CRITICAL
flag, and citation list are valid. Verdict: well-anchored but omits the
same-day ground-truth document's own top-priority finding (the signed-document
opioid contradiction). CRITICAL flag: yes. Full report:
`va-disability/document-analysis/CLAIM-ASSESSMENT-ANALYSIS.md`.

### CREDIBILITY-INCONSISTENCY-RESEARCH (score 7/10)

Legal research answering how VA treats a claimant correcting a prior signed
statement in tension with the clinical record. Rigorous, self-verifying
citation practice; two internal-consistency slips (a wrong cross-reference,
an unreconciled citation-tier summary) and one substantive flag: its proposed
"incomplete recollection" framing may not fit a record of repeated, multi-year
self-reports. Full report:
`va-disability/document-analysis/CREDIBILITY-INCONSISTENCY-RESEARCH-ANALYSIS.md`.

### CP-EXAM-PREP-MENTAL-HEALTH (score 7/10)

Private C&P exam-prep document; not VA-facing. High accuracy, low
self-generated coaching risk (every instruction conditioned on genuineness).
Closes the prior OCD gap. Loses points for rehearsing known cross-exam
landmines (2015 denial, F15.20, pre-service self-reports) too generically to
serve its own stated purpose. Full report:
`va-disability/document-analysis/CP-EXAM-PREP-MENTAL-HEALTH-ANALYSIS.md`.

### 100-PERCENT-SCHEDULAR-PATHWAY (score 7/10)

Legal/regulatory research memo underlying the strategy documents. Sound
arithmetic and legal separation of rule text vs. practice-pattern inference.
Score capped by an outstanding citation-verifier pass and by restating two
cases (Vazquez-Claudio, Bankhead) with a documented prior MISSTATED history in
this corpus, without evidence of re-derivation from primary source. CRITICAL
flag: yes (citation-verification need). Full report:
`va-disability/document-analysis/100-PERCENT-SCHEDULAR-PATHWAY-ANALYSIS.md`.

### SLEEP-APNEA-SECONDARY-CLAIM (score 8/10)

Legal/medical research on the OSA-secondary-to-PTSD theory. Thorough,
self-correcting citation discipline (documents and fixes its own errors);
flags a real risk (pending NPRM affecting DC 6847) missed elsewhere in the
corpus. Minor gaps: nexus-opinion framing vs. coaching optics, and Cherie's
competency to opine on a sleep/pulmonary mechanism. CRITICAL flag: no. Full
report: `va-disability/document-analysis/SLEEP-APNEA-SECONDARY-CLAIM-ANALYSIS.md`.

### NEXUS-LETTER-GUIDE-CHERIE (score 8/10)

Briefing memo for the treating clinician's nexus letter. Structurally the
model this corpus's other documents should follow — never scripts wording,
hedges every ask, explicitly lists what NOT to ask for. Loses one point
because its own "flag for her awareness" section omits the SI-frequency
discrepancy it elsewhere identifies as content she needs to cover. Full
report: `va-disability/document-analysis/NEXUS-LETTER-GUIDE-CHERIE-ANALYSIS.md`.

### COMPREHENSIVE-FINDINGS-2026-07 (score 8/10)

The most thorough single document in the corpus — full chronology, diagnosis
ledger, evidence inventory, ranked open-task list. Score capped by internal
inconsistency: competing claims about which item is "#1 priority," an
overstated F15.20 claim quietly corrected later without updating the original
or its task-list echo, and its own self-flagged inconsistencies not fully
promoted into its own task list. Full report:
`va-disability/document-analysis/COMPREHENSIVE-FINDINGS-2026-07-ANALYSIS.md`.

### DD214 (score 10/10)

Authentic third-party government service record (DD-214, two copies, plus
companion AF IMT 100). Fully internally consistent; every fact the corpus
attributes to it checks out. The one useful finding from this review is
external to the document itself: it anchors the Reyes buddy-statement
unit-name error as a defect in that other document, not this one. Full
report: `va-disability/document-analysis/DD214-ANALYSIS.md`.
