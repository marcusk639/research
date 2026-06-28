# Interstate Unemployment Insurance Fraud — Detection & Enforcement

> Status: findings documented · Started: 2026-06-23 · **Verification:** two
> adversarial runs — `wf_eecd32e5-0f2` (federal, 112 agents, 29 sources, 25 claims →
> 25 confirmed / 0 refuted) and `wf_cb020ec3-6f5` (Texas-specific, 105 agents, 23
> sources, 25 claims → 24 confirmed / 1 refuted). Sources are overwhelmingly primary
> (US DOL, DOL-OIG, GAO, NASWA, TWC, Texas Labor Code, DOJ, state UI agencies).

> Scope note: This subject is framed for fraud **detection and enforcement**, not as
> an operational guide to committing or concealing benefits fraud. Findings describe
> _how agencies catch and prosecute_ claimants who work while collecting, and where
> the systemic gaps are that oversight bodies are working to close.

## Research Question

From a fraud-investigator's perspective: how do claimants who collect unemployment
benefits while working (often in another state) evade detection, _why_ do those
schemes sometimes succeed, what red flags and cross-match systems expose them, and
what are the enforcement and detection best practices?

## Key Findings (executive summary)

Interstate UI fraud — collecting benefits in one state (e.g., via the Texas Workforce
Commission) while actually working, often in another state — is caught primarily
through **layered data cross-matches**: the State and National Directories of New
Hires (SDNH/NDNH), the universal quarterly wage/benefit cross-match, the interstate
crossmatch transmitted over the Interstate Connection Network (ICON), employer
responses via SIDES, and NASWA's **Integrity Data Hub (IDH)** with its multi-state
cross-match, suspicious-actor repository, and identity/bank-account verification.

Schemes evade detection mainly because of **timing lags and access gaps**: quarterly
wage data is 4–6 months stale; the NDNH cross-match runs only weekly and trails the
SDNH by 5+ days; the historical interstate crossmatch ran only quarterly with strict
deadlines; and the U.S. Department of Labor itself **cannot access NDNH wage data** —
only state agencies can. Oversight bodies document both the scale and the gaps: GAO
estimated **$100–135 billion (11–15%)** of pandemic UI was likely fraud, and DOL-OIG
found states were **underutilizing** new-hire cross-matches.

The strongest detection and enforcement gains come from **daily SDNH matching,
mandatory NDNH cross-matching, immediate claimant/employer contact on a hit, and
red-flag analytics** (DOL-OIG's 18 indicators include multistate claims and
shared/suspicious emails). Recovery of interstate overpayments is governed by DOL ET
Handbook 392 and its IB-8605 employer-earnings verification workflow.

---

## 1. Scheme Typologies

The classic "working while claiming" scheme is, in DOL's own taxonomy, a
**benefit-year-earnings (BYE) / returned-to-work error**: a claimant continues
certifying for weekly benefits after returning to work and either fails to report or
underreports earnings. BYE errors are a **leading root cause of UI improper
payments** — the _second_ leading cause in 2018 ([DOL UIPL 13-19](https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf)).

The interstate variant — working in one state while collecting in another — is
specifically what the NDNH cross-match exists to catch: "if a claimant in one state
goes to work in another state, this information should be available through an NDNH
cross-match" ([UIPL 13-19](https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf)).
Related typologies the detection stack targets include **fictitious/identity-theft
claims** (Suspicious Actor and Fictitious Employer repositories in the IDH),
**multi-state filings** under one SSN, **deceased-claimant** filings (Death Master
File matches), and **Combined Wage Claim (CWC) program** abuse handled under the
interstate benefit-payment-control framework.

## 2. Why Schemes Evade Detection — Gaps and Lags

The detection gaps are structural and **timing-driven**, not primarily a matter of
investigator skill:

- **Quarterly wage data is stale.** The universal wage/benefit cross-match relies on
  quarterly wage records that aren't available until roughly **two quarters (4–6
  months)** after the reported quarter, allowing overpayments to persist undetected
  ([UIPL 36-00](https://oui.doleta.gov/dmstree/uipl/uipl2k/uipl_3600.htm); [GAO-02-697](https://www.gao.gov/assets/a235100.html)).
- **The NDNH cross-match itself lags.** Employer-reported W-4 data hits the SDNH
  **5+ days before** the NDNH, and the NDNH cross-match runs only **weekly** versus
  daily/any-day SDNH matching — so a state relying on NDNH alone loses a week or more
  of preventable overpayment ([UIPL 13-19](https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf)).
- **The historical interstate crossmatch was quarterly.** Circa 2002, the Interstate
  Crossmatch ran only quarterly on 4–6-month-old data, and the Interstate Inquiry
  system worked **one claimant at a time** and required an investigator's prior
  suspicion ([GAO-02-697](https://www.gao.gov/assets/a235100.html)). _(Historical —
  superseded by later reforms; see Caveats.)_
- **DOL has no NDNH access.** Statutorily (Social Security Act §453), **only state UI
  agencies** can access NDNH wage data — **DOL/ETA cannot** — so the federal layer
  can't directly run national new-hire/wage cross-matches and must rely on state
  action ([GAO-23-106696](https://www.gao.gov/assets/gao-23-106696.pdf)).
- **State underutilization.** Even where the tools exist, states underuse them:
  DOL-OIG named **17 states** underutilizing new-hire directories and found untimely
  overpayment determinations and incomplete reporting ([DOL-OIG 04-18-003-03-315,
  2018](https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf)).
- **Remote/gig/1099 blind spot.** _(Open question, not verified here.)_ Traditional
  W-2 new-hire (W-4) and quarterly wage reporting don't cleanly capture platform/gig
  and 1099 work — a coverage gap the verified primary sources did not address.

## 3. Detection Mechanisms Agencies Use

| Mechanism                              | What it does                                                                                                                                                                       | Cadence / limit                                   | Source                                                                                                             |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **NDNH new-hire cross-match**          | Surfaces a claimant who started work (incl. in another state); all states + federal agencies report W-4 data                                                                       | Weekly; trails SDNH by 5+ days                    | [UIPL 13-19](https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf)                   |
| **SDNH (state) new-hire match**        | Same, at state level; SDNH transmits to NDNH within 3 business days                                                                                                                | Daily/any-day — fastest                           | [UIPL 36-00](https://oui.doleta.gov/dmstree/uipl/uipl2k/uipl_3600.htm)                                             |
| **Quarterly wage/benefit cross-match** | Matches paid benefits against employer-reported wages                                                                                                                              | Quarterly; 4–6 mo stale                           | [GAO-02-697](https://www.gao.gov/assets/a235100.html)                                                              |
| **Interstate crossmatch (over ICON)**  | Matches Liable-State claims against Agent/Residence-State wage/benefit files; routed to a HUB                                                                                      | Quarterly, strict deadline                        | [ET Handbook 392 §IX](https://oui.doleta.gov/dmstree/handbooks/392/392_2sect9.pdf)                                 |
| **SIDES**                              | Electronic employer exchange of separation reasons + weekly work/earnings accounting                                                                                               | On-demand; participation not universally mandated | [DOL Building Resilience AA4](https://oui.doleta.gov/unemploy/pdf/transfplan/Building_Resilience_Action_area4.pdf) |
| **NASWA Integrity Data Hub (IDH)**     | Multi-state cross-match (same-SSN multi-state filings), Suspicious Actor Repository, Fictitious Employer alerts, identity scoring, bank-account verification, foreign-filing flags | Continuous; ~$3.5B prevented as of Sept 2023      | [NASWA IDH](https://www.naswa.org/integrity-center/integrity-data-hub)                                             |
| **Death Master File match**            | Flags claims filed under deceased identities                                                                                                                                       | —                                                 | [GAO-23-106696](https://www.gao.gov/assets/gao-23-106696.pdf)                                                      |
| **IB-8605 employer verification**      | On a wage-crossmatch hit, investigators send IB-8605 to each employer for exact hours/dates/weeks/earnings                                                                         | Per-hit                                           | [ET Handbook 392 §IX](https://oui.doleta.gov/dmstree/handbooks/392/392_2sect9.pdf)                                 |

The **most effective** strategy for BYE/returned-to-work fraud, per DOL, is
NDNH/SDNH cross-matching **followed by immediate contact with the claimant and the
employer** on a match — speed of follow-up is what converts a match into a stopped
overpayment ([UIPL 13-19](https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf)).

## 4. Red-Flag Indicators

DOL-OIG's analytics applied **18 fraud indicators**, explicitly including **multistate
claims** and **shared or suspicious email addresses**; its case sampling cross-matched
against the **Death Master File** (deceased claimants) and the **NDNH** (unreported
wages) ([GAO-23-106696](https://www.gao.gov/assets/gao-23-106696.pdf)). State new-hire
cross-matches (e.g., Missouri DES, run **weekly** against State and Federal New Hire
databases) specifically target **claimants who keep filing after their
employer-reported hire date** ([Missouri DES](https://labor.mo.gov/des/employers/crossmatch-process)).
Commercial integrity vendors add **IP/geolocation anomalies, bank-account anomaly
analytics, and identity proofing** (e.g., ID.me-type services) on top of the federal
data layer.

## 5. Enforcement, Penalties & Recovery

- **Interstate overpayment control** is governed by **DOL ET Handbook 392**: it
  defines prevention, detection, and recovery under the Interstate Benefit Payment
  Plan and the CWC program — including **locating and recovering from claimants who
  relocate** to another state — and specifies the ICON-routed crossmatch and the
  **IB-8605** employer-earnings verification workflow ([ET Handbook 392 §IX](https://oui.doleta.gov/dmstree/handbooks/392/392_2sect9.pdf)).
- **Scale of the problem.** In 2001, of $30B in UI paid, ~$2.4B were overpayments
  with $577M (24%) fraud/abuse — yet states officially reported only $650M, showing
  massive **under-detection** ([GAO-02-697](https://www.gao.gov/assets/a235100.html)).
  During the pandemic (Apr 2020–May 2023), GAO estimated **$100–135B (11–15%)** of UI
  was likely fraud across 53 jurisdictions ([GAO-23-106696](https://www.gao.gov/assets/gao-23-106696.pdf)).
- **Detection ROI.** When one state added SDNH matching it detected ~**6,700
  overpayments over $4M** (Jul 2000–Dec 2001) and cut the average detected
  overpayment from **$2,800 to $750** by catching working claimants sooner
  ([GAO-02-697](https://www.gao.gov/assets/a235100.html)).
- **Prosecution.** Federal cases confirm criminal exposure for working-while-claiming
  and interstate schemes — e.g., DOL-OIG's case of a Californian sentenced to **18
  months** for unlawfully collecting ~$100K in UI **while employed** ([DOL-OIG press release](https://www.oig.dol.gov/public/Press%20Releases/Californian%20Sentenced%20to%2018%20Months%20Imprisonment%20for%20Unlawfully%20Collecting%20100K%20in%20UI%20Benefits%20Du.pdf)); a former Fort Worth
  resident sentenced to **five years** federal prison ([DOJ NDTX](https://www.justice.gov/usao-ndtx/pr/former-fort-worth-resident-sentenced-five-years-federal-prison-unemployment-benefits));
  and a Massachusetts man who pleaded guilty to collecting ~$18K **while working**
  ([Mass.gov](https://www.mass.gov/news/cambridge-man-pleads-guilty-sentenced-for-collecting-nearly-18000-in-unemployment-benefits-while-working)).
- **Texas-specific** TWC fraud, overpayment, and criminal-prosecution procedures were
  _fetched but not in the verified claim set_ — see TWC source links in Sources and
  Open Questions below.

## 6. Recommendations / Best Practices for Closing Gaps

1. **Mandate state cross-matching against the NDNH.** DOL's transformation plan / the
   President's FY2025 budget proposes _requiring_ states to cross-match the NDNH
   specifically to catch those who keep claiming after returning to work ([DOL Building
   Resilience AA4](https://oui.doleta.gov/unemploy/pdf/transfplan/Building_Resilience_Action_area4.pdf)).
   _(The 2024 UI Integrity and Accessibility Act moved this from proposal toward
   mandate — see Caveats.)_
2. **Match daily at the SDNH level**, not just weekly at the NDNH — recovers the 5+
   day / one-week-plus head start.
3. **Immediate claimant + employer contact** on every match (the verified
   most-effective BYE control).
4. **Full IDH adoption** — multi-state cross-match, suspicious-actor and
   fictitious-employer repositories, identity and bank-account verification.
5. **Universal SIDES employer participation** to get weekly work/earnings accounting
   electronically and interrupt claims faster.
6. **Close the federal access gap** so oversight can run national matches rather than
   depending on uneven state action.

## 7. Texas-Specific (TWC) Detection, Penalties & Prosecution

> Added 2026-06-23 from a second adversarial run (`wf_cb020ec3-6f5`, 105 agents, 23
> sources, 25 claims → **24 confirmed / 1 refuted**). Sources are primary (TWC, Texas
> Labor Code / TUCA, Texas State Auditor, DOJ, DOL-OIG, CRS).

**Detection.** TWC detects unreported earnings and interstate work primarily through
**new-hire cross-matching**: under PRWORA (42 U.S.C. §653a), Texas employers must
report every new hire/rehire (name, SSN, address) within **20 days** to the state
directory, and TWC cross-matches that data against benefit-claim records and
overpayment lists, referring discrepancies to its **fraud detection unit** to stop
benefits and recover overpayments ([TWC fraud reduction](https://efte.twc.texas.gov/fraud_reduction.html);
[TWC new-hire reporting](https://www.twc.texas.gov/employer-resources/new-hire-reporting);
[TWC fraud](https://www.twc.texas.gov/programs/unemployment-benefits/fraud)). New-hire
matching surfaces fraud **3–4 months earlier** than quarterly wage reporting, and
DOL-OIG found it recovers far more: **44%** of new-hire-detected overpayments were
recovered in full within 90 days vs. **12%** for the wage/UI cross-match ([DOL-OIG
05-04-002-03-315, 2004](https://www.oig.dol.gov/public/reports/oa/2004/05-04-002-03-315.pdf)).

**The interstate gap — and how the NDNH closes it.** A _single-state_ new-hire match
**cannot** catch a claimant hired by a multi-state employer who designates a different
reporting state (PRWORA lets multi-state employers pick one state). The national
**NDNH** cross-match closes this — in the federal NDNH pilot, TWC detected **50% more
potential-fraud cases in one quarter** than the state match alone ([Texas State
Auditor 06-008](https://sao.texas.gov/Reports/Main/06-008.pdf); [CRS RS22889](https://www.congress.gov/crs-product/RS22889)).
The NDNH spans three files — new-hires (W-4), quarterly wage, and the UI claims file
populated by state workforce agencies — which is precisely what lets it flag someone
**collecting in one state while working in another**.

**Penalties & recovery (Texas Labor Code Ch. 214 / 213).**

- **Mandatory 15% fraud penalty** — on benefits obtained by willful nondisclosure/
  misrepresentation, the claimant forfeits the benefit and remaining benefit-year
  rights, and TWC "shall require" a penalty equal to **15% of the amount forfeited**
  (Sec. 214.003) ([TUCA statute](https://www.twc.texas.gov/sites/default/files/ui/docs/tuca-2025-twc.pdf)).
- **Retroactive disqualification** — ineligible for **all** benefits received _after
  the first incident of fraud_, not just the misreported weeks ([TWC fraud](https://www.twc.texas.gov/programs/unemployment-benefits/fraud)).
- **Recovery mechanisms** (Sec. 214.002) — deduction from future benefits, refund
  from the claimant, or Chapter 213 collection methods including **tax liens** (the
  same used against delinquent employers), **plus the federal Treasury Offset Program
  (TOP)** intercepting IRS refunds ([TWC overpayments](https://www.twc.texas.gov/programs/unemployment-benefits/overpayments);
  [Treasury TOP](https://fiscal.treasury.gov/files/top/TOP-rules-reqs-fact-sheet.pdf)).

**Criminal prosecution.**

- **Forum** — criminal violations are prosecuted by the **county prosecutor** where
  the violation occurred (Sec. 213.002); civil enforcement runs through a designated
  assistant AG (Sec. 213.001) ([Tex. Labor Code Ch. 213](https://statutes.capitol.texas.gov/Docs/LA/htm/LA.213.htm)).
- **The interstate statutory hook** — Sec. **214.001** makes it a **Class A
  misdemeanor** to knowingly make a false statement / omit a material fact to obtain
  benefits, _expressly including_ benefits "under the **unemployment compensation law
  of another state**" — the direct hook for prosecuting working-across-state-lines
  fraud ([Tex. Labor Code Ch. 214](https://statutes.capitol.texas.gov/Docs/LA/htm/LA.214.htm)).
- **Theft charging** — TWC also prosecutes under Penal Code 31.03 (theft), graded by
  amount from Class A misdemeanor up to state-jail / third-degree felony; 2025
  dispositions include deferred adjudication + restitution ([TWC criminal prosecutions](https://www.twc.texas.gov/programs/unemployment-benefits/criminal-prosecutions)).
- **Named ring case** — _U.S. v. Jose Luis Gonzalez_ (SDTX): a decade-long scheme of
  ~50 fraudulent claims totaling **$531,161** using **fictitious employer accounts**
  to falsely confirm employment and trigger funded debit cards; Gonzalez got **74
  months** federal prison + full restitution, with nine co-conspirators (recruited via
  Facebook) also sentenced ([DOJ SDTX](https://www.justice.gov/usao-sdtx/pr/leader-sent-prison-unemployment-insurance-fraud-scam)).
  _(Note: this is an intrastate identity/employer-verification ring, not a
  working-in-another-state example.)_

**Gig/1099 blind spot — confirmed at the national level.** The NDNH "generally does
not gather information on self-employed workers (e.g., independent contractors)," and
a 2019 HHS/ASPE study found only **~16 states** require any independent-contractor
income reporting ([CRS RS22889](https://www.congress.gov/crs-product/RS22889)).
**Refuted:** the specific framing that _Texas_ new-hire reporting is "W-4-keyed" and
therefore excludes 1099 workers was **killed 0-3** — the gig gap is real and
well-documented at the **NDNH/national** level, but that precise Texas mechanism was
not substantiated.

**Identity-fraud routing.** UI identity fraud is reported to the DOJ National Center
for Disaster Fraud, which notifies **DOL-OIG** — the lead federal investigative
agency for UI fraud ([TWC fraud](https://www.twc.texas.gov/programs/unemployment-benefits/fraud);
[DOL UI ID theft](https://www.dol.gov/agencies/eta/UIIDtheft)).

---

## Caveats & Source Vintage

- Several structural findings rest on **older primary sources** — GAO-02-697 (2002)
  and ET Handbook 392 (March 1997) — which accurately describe long-standing program
  architecture but predate reforms. Most notably, the 2002 finding that state NDNH
  access was "legally restricted" has been **superseded**: the **2024 UI Integrity and
  Accessibility Act** now mandates NDNH cross-matching, and DOL's FY2025 package
  pushed the same direction. Past-tense findings remain valid as historical
  documentation of the gaps.
- The single-source, **2-1** finding on 2002-era interstate-tool gaps is the weakest
  and should be treated as historical.
- The DOL-OIG 2018 audit was verified via the authoritative **UIPL 13-19** synthesis
  (which quotes the report's title, number, and date exactly) rather than the OIG PDF
  directly.
- The GAO pandemic estimate ($100–135B) is **contested by DOL** as possibly
  overstated; GAO defended its 95%-CI methodology.
- The corpus is built largely on **federal/national** sources plus Missouri as a state
  exemplar; **TWC-specific** procedures and named TWC prosecution outcomes were not
  directly verified in this claim set.

## Open Questions (next research)

_Resolved by the Texas run (§7): TWC procedures, the 15% penalty and recovery
mechanisms, and the criminal-prosecution framework + a named ring case. Still open:_

1. A named, verified prosecution of the **specific interstate pattern** — working in
   another state while collecting Texas benefits — to illustrate Sec. 214.001's
   "another state" hook in practice. (The Gonzalez ring is intrastate; the federal
   run's "while employed" cases aren't TX-interstate.)
2. **Dollar thresholds / decision rules** that move a TWC case from administrative
   recovery to criminal referral, and the federal (DOL-OIG/DOJ) vs. county-prosecutor
   split.
3. **2024 UI Integrity and Accessibility Act** — actual implementation status across
   states as of 2026, and whether it closed the DOL-no-NDNH-access and
   state-underutilization gaps. _(No 2024–2026 statute-implementation claim survived
   verification in either run — genuinely unresolved.)_
4. Whether any state (or Texas) has deployed detection reaching **gig/1099/platform**
   earnings — e.g., gig-platform data-sharing or 1099 cross-matches — and its
   effectiveness. (The _gap_ is confirmed; mitigations are not.)

## Sources

**Primary — federal detection & oversight:**

- DOL UIPL 13-19 (NDNH cross-match; BYE errors; DOL-OIG 2018 audit synthesis) — https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2019/UIPL_13-19_acc.pdf
- DOL UIPL 36-00 (PRWORA SDNH→NDNH 3-day rule; quarterly-wage lag) — https://oui.doleta.gov/dmstree/uipl/uipl2k/uipl_3600.htm
- DOL ET Handbook 392 §IX (interstate benefit payment control; ICON crossmatch; IB-8605) — https://oui.doleta.gov/dmstree/handbooks/392/392_2sect9.pdf
- DOL "Building Resilience" Action Area 4 (IDH, SIDES, NDNH-mandate proposal) — https://oui.doleta.gov/unemploy/pdf/transfplan/Building_Resilience_Action_area4.pdf
- DOL UIPL 28-20 (pandemic-era integrity guidance) — https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2020/UIPL_28-20.pdf
- GAO-02-697 (2002 baseline; cross-match gaps; SDNH ROI) — https://www.gao.gov/assets/a235100.html
- GAO-23-106696 (pandemic fraud $100–135B; DOL no NDNH access; 18 indicators) — https://www.gao.gov/assets/gao-23-106696.pdf
- GAO-24-107471 (UI fraud / red-flag analytics) — https://www.gao.gov/assets/gao-24-107471.pdf
- GAO-25-108172 — https://files.gao.gov/reports/GAO-25-108172/index.html
- DOL-OIG UI oversight work index — https://www.oig.dol.gov/doloiguioversightwork.htm
- DOL-OIG report 19-25-007-03-315 (2025) — https://www.oig.dol.gov/public/reports/oa/2025/19-25-007-03-315.pdf
- NASWA Integrity Data Hub — https://www.naswa.org/integrity-center/integrity-data-hub
- NASWA ICON crossmatches tech session — https://www.naswa.org/system/files/2023-02/iconprogrammertechtalkssession12crossmatches.pdf
- Missouri DES crossmatch process (state exemplar) — https://labor.mo.gov/des/employers/crossmatch-process

**Primary — Texas / TWC & Texas law (verified in §7):**

- TWC — Unemployment Benefits Fraud (15% penalty; retroactive disqualification; NCDF→DOL-OIG routing) — https://www.twc.texas.gov/programs/unemployment-benefits/fraud
- TWC — Overpayments (recovery mechanisms; TOP IRS-refund interception) — https://www.twc.texas.gov/programs/unemployment-benefits/overpayments
- TWC — Criminal Prosecutions (theft charging; 2025 dispositions) — https://www.twc.texas.gov/programs/unemployment-benefits/criminal-prosecutions
- TWC EFTE — fraud reduction (new-hire cross-match procedure) — https://efte.twc.texas.gov/fraud_reduction.html
- TWC — New Hire Reporting (20-day PRWORA reporting) — https://www.twc.texas.gov/employer-resources/new-hire-reporting
- TWC — TUCA statute text 2025 (Tex. Labor Code Ch. 213/214; §§214.001–214.003) — https://www.twc.texas.gov/sites/default/files/ui/docs/tuca-2025-twc.pdf
- Tex. Labor Code Ch. 213 (criminal/civil enforcement forum) — https://statutes.capitol.texas.gov/Docs/LA/htm/LA.213.htm
- Tex. Labor Code Ch. 214 (offenses; "another state" interstate hook) — https://statutes.capitol.texas.gov/Docs/LA/htm/LA.214.htm
- Texas State Auditor Report 06-008 (NDNH pilot; +50% cases/quarter) — https://sao.texas.gov/Reports/Main/06-008.pdf
- CRS RS22889 (NDNH three-file structure; gig/1099 self-employment gap) — https://www.congress.gov/crs-product/RS22889
- DOL-OIG 05-04-002-03-315, 2004 (new-hire detection superiority; 44% vs 12% recovery) — https://www.oig.dol.gov/public/reports/oa/2004/05-04-002-03-315.pdf
- Treasury — TOP rules/requirements fact sheet — https://fiscal.treasury.gov/files/top/TOP-rules-reqs-fact-sheet.pdf
- DOL — UI identity-theft routing — https://www.dol.gov/agencies/eta/UIIDtheft

**Primary — prosecution / enforcement examples:**

- DOL-OIG — Californian sentenced 18 mo, ~$100K UI while employed — https://www.oig.dol.gov/public/Press%20Releases/Californian%20Sentenced%20to%2018%20Months%20Imprisonment%20for%20Unlawfully%20Collecting%20100K%20in%20UI%20Benefits%20Du.pdf
- DOJ NDTX — former Fort Worth resident sentenced 5 years — https://www.justice.gov/usao-ndtx/pr/former-fort-worth-resident-sentenced-five-years-federal-prison-unemployment-benefits
- Mass.gov — Cambridge man, ~$18K UI while working — https://www.mass.gov/news/cambridge-man-pleads-guilty-sentenced-for-collecting-nearly-18000-in-unemployment-benefits-while-working
- DOJ EDVA — Mineral man sentenced 4+ years, COVID UI fraud — https://www.justice.gov/usao-edva/pr/mineral-man-sentenced-over-four-years-prison-covid-era-unemployment-insurance-fraud
- DOL-OIG — 15 people sentenced for defrauding UI agencies during COVID-19 — https://www.oig.dol.gov/public/Press%20Releases/Fifteen%20People%20Sentenced%20For%20Defrauding%20Unemployment%20Insurance%20Agencies%20During%20Covid-19%20Pandemic.pdf
- DOJ — COVID-19 Fraud Enforcement Task Force 2024 report — https://www.justice.gov/archives/opa/pr/covid-19-fraud-enforcement-task-force-releases-2024-report
- DOJ SDTX — _U.S. v. Jose Luis Gonzalez_ ring (74 mo; $531,161; fictitious-employer scheme) — https://www.justice.gov/usao-sdtx/pr/leader-sent-prison-unemployment-insurance-fraud-scam

**Secondary / vendor (red-flag analytics):**

- LexisNexis Risk — UI fraud prevention & protection — https://risk.lexisnexis.com/government/unemployment-insurance-programs/fraud-prevention-and-protection
- Thomson Reuters — ID verification & preventing fraud — https://www.thomsonreuters.com/en-us/posts/investigation-fraud-and-risk/id-verification-preventing-fraud/
