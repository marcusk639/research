# VA Claim Document Analysis: DD-214 (Certificate of Release or Discharge from Active Duty)

**Source:** `va-disability/personal-records/supporting-docs/DD214 2.pdf` · **Classification:** evidentiary form
**Provenance:** Not logged in `DOCUMENT-PROVENANCE.md` — gap (expected/low-risk for this category: that log tracks _authorship_ of claim-facing content; a DD-214 is a third-party government record with no authorship question, but the gap should still be logged for completeness).
**Checked against:** `COMPREHENSIVE-FINDINGS-2026-07.md`

## Summary

A 5-page scanned PDF containing two DD Form 214 copies — "MEMBER-1" (pp. 1–2, near-duplicate scans) and "MEMBER-4" (p. 3, which additionally carries the Special Additional Information block: character of service, separation/reentry codes, narrative reason) — plus a 2-page AF IMT 100 "Request and Authorization for Separation" (pp. 4–5), the underlying administrative order producing the discharge. This is the veteran's primary official service record and the fixed reference point every other corpus document (personal statement, buddy statements, nexus-letter guides) must stay internally consistent with. Its evidentiary purpose is strictly factual corroboration — service dates, unit, rank, decorations, discharge characterization — not any clinical or stressor claim.

## Score: 10/10 (accuracy · completeness-for-purpose · consistency · credibility — NOT persuasiveness)

Authentic third-party government record, not veteran-authored, so the usual axes largely resolve to "internally consistent, and does it match what the corpus already treats as ground truth from it." All fields are identical across the three included copies and consistent with the companion AF IMT 100. Every fact `COMPREHENSIVE-FINDINGS-2026-07.md` §1 attributes to "per DD-214" is in fact present and accurately stated — confirmed by direct line-by-line comparison, not assumed. No credibility risk, no internal contradiction, complete for its stated purpose. Only deduction-worthy point is external to this document (see Gaps).

## Strengths

- Three copies within the same PDF (pp. 1, 2, 3) show byte-for-byte consistent data across every block (dates, unit, SSN, DOB, awards) — no internal drift.
- The Member-4 copy (p. 3) includes blocks 23–30 (Type of Separation: "RELEASE FROM ACTIVE DUTY"; Character of Service: "HONORABLE"; Separation Authority: "AFI 36-3208"; Separation Code: "MBK"; Reentry Code: "1J"; Narrative Reason: "COMPLETION OF REQUIRED ACTIVE SERVICE") — the more useful copy for a compensation claim; Member-1 (pp. 1–2) omits this block.
- The companion AF IMT 100 (pp. 4–5) independently corroborates unit ("ACC 4 EQUIPMENT MAINT SQ FFD4Y0, SEYMOUR JOHNSON NC"), the 22 NOV 2013 effective date, and "HONORABLE" character of service — cross-document agreement within the same PDF rules out an OCR/transcription error on the unit name.

## Weaknesses

None identified — authentic government record, no internal inconsistency across its three copies or the companion authorization.

## Gaps

- **This document alone cannot resolve the Reyes disclosure-timing question** (`COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 2 / open task #8, "Confirm Reyes's own DD-214/service-date overlap through late 2013"). This PDF fixes only Marcus Klein's own separation date (2013-11-22, block 12b, all copies) — it cannot speak to Wilfredo Reyes's service dates. Flagging so it isn't mistaken for resolved just because "the DD-214 is in the file."
- No STR content is present, so this document cannot corroborate/contradict the in-service ankle-fracture date (`COMPREHENSIVE-FINDINGS` §2, "2011-05 ... /disputed") — outside this form's purpose.

## Credibility Risk Assessment

- None identified in the document itself. Government-issued, CAC/PKI-signed (block 22a: "DUNCAN CHRISTINA ANN," Separations Documentation Technician). Veteran's own signature is absent (block 21a: "MEMBER NOT AVAILABLE TO SIGN," date "N/A") — a routine out-processing artifact, not evidence of tampering.
- The one downstream exposure this document _creates_ (passively, by being the accurate reference point): it fixes "4 EQUIPMENT MAINT SQ" (4th **Equipment** Maintenance Squadron) as ground truth (block 8a, all copies; AF IMT 100 block 16), while the signed `VA-Buddy-Form_reyes_complete 2.pdf` (06/16/2026) still reads "4th Maintenance Squadron" — omitting "Equipment." Per `CLAIM-ASSESSMENT.md` line 65 and `COMPREHENSIVE-FINDINGS-2026-07.md` §9a item 3, this fix was flagged before but not yet applied to the signed document. The DD-214 is accurate; the risk lives entirely in the other document.

## Citations Needing Verification

None found — a military administrative form contains no legal/CFR/USC/case citations.

## Consistency Check vs. COMPREHENSIVE-FINDINGS

- **Confirms:** Name/SSN/DOB ("KLEIN MARCUS EDWARD," 435-75-5617, 1989-05-30, blocks 1/3/5) matches §1.
- **Confirms:** Discharge characterization "HONORABLE" (block 24, p.3; AF IMT 100 block 14) matches §1.
- **Confirms:** Separation/reentry codes and narrative reason "MBK"/"1J"/"COMPLETION OF REQUIRED ACTIVE SERVICE" (blocks 25–28, p.3) matches §1 verbatim.
- **Confirms:** Unit "4 EQUIPMENT MAINT SQ (ACC)" / "SEYMOUR JOHNSON NC" (block 8a; AF IMT 100 block 16) matches §1's "4th Equipment Maintenance Squadron (ACC), Seymour Johnson AFB, NC."
- **Confirms:** Rank/AFSC "SRA"/"E4"/"2A333... 3 YEARS AND 10 MONTHS" (blocks 4a/4b/11) matches §1.
- **Confirms:** Service dates 2009-11-23 to 2013-11-22 (block 12a/12b; AF IMT 100 block 13) matches §2 chronology.
- **Confirms:** Awards list (block 13) matches §1 exactly.
- **Diverges:** None found within this document.
- **External divergence anchored by this document:** Reyes buddy statement's "4th Maintenance Squadron" vs. this document's "4th Equipment Maintenance Squadron" — see Credibility Risk Assessment.

## Notable Remarks

- Prefer the Member-4 copy (p. 3) over Member-1 (pp. 1–2) if only one copy is ever submitted — it's the one carrying the Special Additional Information block VA adjudicators most need.
- Reserve Obligation Termination Date 2017-06-11 (block 6) and IRR/ARPC Denver reserve-transfer fields (AF IMT 100 block 20) are standard post-active-duty administrative artifacts, not referenced elsewhere in the corpus — noted for completeness only.

## Assumptions Made

- Interpreted "unit-name and service-date consistency issues already flagged in this corpus" as referring to `COMPREHENSIVE-FINDINGS-2026-07.md` §9a items 2–3 and `CLAIM-ASSESSMENT.md` lines 65/120 — both checked above.
- Treated the PDF's three DD-214 copies plus the AF IMT 100 as one logical target document for this single invocation, since they're one file at one path.

## Open Questions for the User

- Whether Wilfredo Reyes's own DD-214/service dates have been independently obtained to confirm overlap with the "late 2013, while we were both still serving" disclosure window — this document only fixes Marcus's own 2013-11-22 separation date as one side of that comparison (carried forward from `COMPREHENSIVE-FINDINGS-2026-07.md` open task #8, not new).
