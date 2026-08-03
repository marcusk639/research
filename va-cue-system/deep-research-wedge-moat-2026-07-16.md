# Follow-up Deep Research — Wedge & Moat Verification (2026-07-16)

> Focused follow-up closing the two load-bearing gaps left by the first pass
> (`deep-research-findings-2026-07-16.md`). 106 agents, 6 angles, 23 sources → 92
> claims → 25 adversarially verified: **25 confirmed, 0 refuted.** Synthesis
> completed cleanly this run. Every claim below is cited; where the research did
> not resolve something, it is listed as an open question rather than assumed.

## Executive summary

- **WEDGE — CONFIRMED (for the verified set only).** None of the four tools deep-verified this pass — **VA Claim Helper (VCH), Vala, VeteranAi, Dodonai** — performs effective-date _reconstruction_ (earliest-effective-date argumentation), CUE _viability analysis_, or point-in-time "law as it read then" application. The strongest near-miss is **VCH**, which as of ~Jan–Mar 2026 builds a chronological claims timeline and answers document Q&A like _"What is the earliest effective date for this veteran's PTSD claim?"_ — but that is date **extraction + document citation**, not argument construction against a final decision. **Caveat:** only four tools were verified; the wedge is _not_ proven across the whole market (see open questions).
- **MOAT — GENUINE and doable, grounded in a real legal requirement.** CUE review is _legally required_ to apply "the evidentiary record and the law that existed when that decision was made" (38 C.F.R. § 3.105(a)(1)(iii); _Russell v. Principi_; M21-1), and a successful CUE relates back to the original decision date (the earliest-effective-date payoff). § 3.105 alone was amended ~10× between 1961 and 2019, so the operative text genuinely differs by decision date. GovInfo machine-ingestible CFR XML only reaches **1997** (Title 38 practically; 1996 is partial) — so **pre-1997 point-in-time sourcing is the real, defensible gap-fill work.** **Caveat:** whether commercial vendors already sell pre-2017 point-in-time CFR was _not_ resolved — decisive and still open.
- **Biggest surprise / time-sensitivity:** the closest competitor (VCH) is already touching effective-date extraction and shipping fast (timeline Jan 2026, effective-date Q&A Mar 2026). The gap between "extract the date" and "argue the earliest date / detect CUE" is narrowing — this window is not static.

## Competitor matrix

| Tool                                                                   | Facing                                             | Eff-date reconstruction?                | CUE analysis? | Point-in-time law? | Pricing                                                                 | Confidence                                 | Source                                       |
| ---------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------- | ------------- | ------------------ | ----------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------- |
| **VA Claim Helper (VCH)**                                              | Professional (accredited only)                     | **No** — extracts dates from docs only  | **No**        | **No**             | (from pass 1: ~$33–150/mo)                                              | High (comprehensive docs)                  | vaclaimhelper.com/blog/documentation/        |
| **Vala**                                                               | Professional                                       | **No** (as advertised)                  | **No**        | **No**             | not published                                                           | Med — landing page, scoped to "advertised" | valaclaims.com                               |
| **VeteranAi**                                                          | Veteran self-service (+ County VSO seat licensing) | **No**                                  | **No**        | **No**             | Free + $25/mo Pro                                                       | High                                       | veteranai.co / /va-cfile-analyzer            |
| **Dodonai**                                                            | Cross-domain (SSDI/LTD/VA) records org             | **No**                                  | **No**        | **No**             | not found                                                               | High                                       | dodon.ai/practice-areas/disability-benefits/ |
| Caliber/Flagship, claim.vet, ClaimClam, VetClaims.ai, Vetlex, RepScout | —                                                  | **UNVERIFIED**                          | UNVERIFIED    | UNVERIFIED         | —                                                                       | —                                          | not resolved this pass                       |
| Legal-AI incumbents (Harvey, CoCounsel, Legora, Clearbrief, EvenUp)    | —                                                  | **UNVERIFIED** (VA vertical unresolved) | UNVERIFIED    | UNVERIFIED         | (pass 1: Harvey ~$1,200+/seat, 20–50 seat min; CoCounsel ~$225/user/mo) | —                                          | not resolved this pass                       |

**VCH near-miss detail:** VCH's Claims History Timeline reads the C-File to "pull event dates and document types" and extract "conditions, disability percentages, and effective dates," organizing filings/C&P exams/rating decisions/appeals/BVA decisions chronologically as a _reference document_. Its C-File AI Q&A (≈Mar 27, 2026) answers effective-date questions with exact page citations. Both are **document search/extraction**; the only date-analytic function is appeal-deadline tracking (365-day window). Neither constructs retroactive-entitlement or CUE arguments against prior final decisions — which is _functionally opposite_ to CUE (CUE attacks already-final decisions). (Source: vaclaimhelper.com/blog/)

## Wedge verdict

**Confirmed for VCH, Vala, VeteranAi, and Dodonai** — the wedge (effective-date reconstruction + CUE + point-in-time law) is genuinely unoccupied by these tools. The strongest counter-evidence is VCH's fast movement into effective-date _extraction and Q&A_; a founder should treat the extraction→analysis gap as the thing being raced for, not a permanent moat. The verdict does **not** extend to the unverified competitors or to a possible legal-AI VA vertical — those remain the live risk to the thesis.

## Pre-2017 point-in-time regulatory sourcing (the moat)

**Why it's real:** CUE is a black-letter requirement to apply the law as it read at the prior decision (§ 3.105(a)(1)(iii); _Russell v. Principi_, 3 Vet. App. 310 (1992); M21-1), and § 3.105's authority note shows ~10 amendments 1961→2019 (26 FR 1569 … 84 FR 167). So the historical-text need is genuine, not manufactured.

| Source                                                      | Earliest coverage                       | Format                                                      | Granularity                | Cost                                      |
| ----------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------- | -------------------------- | ----------------------------------------- |
| eCFR versioner API                                          | ~Jan 2017                               | XML/JSON                                                    | day-level                  | Free                                      |
| GovInfo annual CFR (XML)                                    | 1997 (Title 38 practical); 1996 partial | XML/PDF/text                                                | annual (Title 38 = July 1) | Free                                      |
| GovInfo 1996                                                | partial XML / full PDF                  | XML+PDF                                                     | annual                     | Free                                      |
| **Pre-1997 editions**                                       | print/scan → **OCR required**           | PDF/scan                                                    | annual                     | Free source, high build cost              |
| Federal Register final rules                                | 1990s+ online                           | reconcile via authority notes for **exact effective dates** | per-rule                   | Free                                      |
| Commercial (HeinOnline, Westlaw, LexisNexis, vLex/Fastcase) | **UNRESOLVED**                          | —                                                           | —                          | **not answered — decisive open question** |

**Effort / defensibility:** The differentiator is **not** the post-1997 XML (GovInfo already provides it free) — it's (a) OCR + structuring of pre-1997 38 C.F.R./38 U.S.C. editions, (b) reconciling each amendment to its **exact Federal Register effective date**, and (c) **corpus hygiene** — e.g., the research flagged a false positive: the 2007 Part 3→Part 5 rewrite (E7-9542, RIN 2900-AM01) was a _proposed rule that never became law_; an engine that ingested it would apply text that was never in force. Verdict: **genuine, defensible, doable — but its defensibility hinges on the unresolved commercial-availability question.** If Hein/Westlaw/Lexis already sell point-in-time historical CFR retrieval, the moat shrinks to the veterans-specific reasoning layer.

## Verification ledger (25/25 confirmed, 0 refuted)

| Claim                                                                                   | Verdict                            | Source                                 |
| --------------------------------------------------------------------------------------- | ---------------------------------- | -------------------------------------- |
| VCH stops at extraction/form-filling/Q&A; no CUE or point-in-time law                   | Confirmed (3-0)                    | vaclaimhelper.com/blog/documentation/  |
| VCH timeline + effective-date Q&A = extraction/citation, not argumentation              | Confirmed (3-0)                    | vaclaimhelper.com/blog/                |
| Vala advertises evidence-surfacing + auto-forms; no eff-date/CUE (as advertised)        | Confirmed (3-0)                    | valaclaims.com                         |
| VeteranAi is veteran self-service ($25/mo); C-File Analyzer prospective only            | Confirmed (3-0)                    | veteranai.co                           |
| Dodonai = medical-chronology/records-org, VA only a submission destination              | Confirmed (3-0)                    | dodon.ai                               |
| CUE legally requires the record + law as it existed at the prior decision; relates back | Confirmed (3-0)                    | § 3.105(a)(1)(iii); M21-1              |
| § 3.105 amended ~10× 1961–2019 (text differs by decision date)                          | Confirmed (3-0)                    | GovInfo CFR-2023 §3.105 authority note |
| Machine-ingestible CFR XML only ~1996-97; Title 38 practically 1997                     | Confirmed (3-0, one component 2-1) | govinfo.gov/help/cfr                   |
| E7-9542 (Part 3→Part 5 rewrite) was a PROPOSED rule, never in force                     | Confirmed (3-0)                    | federalregister.gov E7-9542            |

_(Minor corrections noted by the run: § 3.105 amendments are ~10, not "a dozen"; the 1996 CFR is "complete" only as PDF, XML is partial.)_

## Open questions (what remains unverified — and matters)

1. **The unverified competitors** — Caliber/Flagship (vaclaims.us), claim.vet, ClaimClam, VetClaims.ai, Vetlex, RepScout produced no surviving claims. Until checked, the wedge is confirmed only for the four verified tools.
2. **Legal-AI incumbents' VA plans** — whether Harvey / CoCounsel / Legora / Clearbrief / EvenUp have or plan a VA vertical with point-in-time retrieval. This is the most credible well-capitalized fast-follow and was not resolved.
3. **Is the pre-2017 point-in-time CFR moat already commoditized?** — HeinOnline / Westlaw / LexisNexis / vLex historical/point-in-time CFR retrieval and startup licensing cost were _not_ answered. **Decisive for the moat verdict.**
4. **True pre-1997 build cost** — OCR/scan effort for 1980s–1990s (and earlier) 38 C.F.R./38 U.S.C. editions reconciled to Federal Register effective dates remains unestimated. This is the actual differentiator work.

## Sources (primary unless noted)

- vaclaimhelper.com/ , /blog/ , /blog/documentation/ (primary)
- valaclaims.com/ (primary — landing page)
- veteranai.co/ , /va-cfile-analyzer (primary)
- dodon.ai/practice-areas/disability-benefits/ (primary)
- claim.vet/blog/ai-va-disability-claims/ (blog)
- govinfo.gov/help/cfr , /app/collection/cfr/1996 , /bulkdata/CFR/1996/title-47 (primary)
- govinfo.gov CFR-2023-title38-vol1 §3.105 PDF (primary)
- federalregister.gov E7-9542 (primary)
- M21-1 Part X (CUE) — knowva.ebenefits.va.gov (primary)
- guides.jenkinslaw.org historical-cfr; fclawlib fastcase; nyulawglobal fee-based DBs; vaquill.ai westlaw-vs-vlex (secondary/blog — commercial-dataset angle, not decisive)

---

_Research assistance, not legal advice. Competitor findings are mid-2026 marketing/documentation snapshots and should be re-checked before any launch decision — the wedge is narrowing fastest at VCH._
