# 14 — Revised Plan: TWK Architecture, Hiring, Industrial Revenue

> As of 2026-10-20. Labels: see [REPORT.md](REPORT.md#labels-used). Unlike files 01–13, this file uses outside research (Oct 20, 2026) plus analysis. Figures are tagged **[Sourced]** (with a link), **[Analysis]** (derived or assumed in this file) or **[Estimate]** (an estimate in the founder's source, kept as given). Where it conflicts with the original source targets, this file supersedes them.

**Summary.** TWK goes hybrid (firm knowledge on Glass, client data on the appliance), and the first W-2 hire moves from months 9–12 to about months 15–24, gated on about $20–25K MRR plus one sign of real overload, with a contract engineer covering installs and backup until then. Year-1 industrial revenue is realistically $35–60K in the base case, not $150–250K, led by $2,500–6,000 contractor compliance packages; with the adopted calendar rules, the regenerated model's base case gives ~$190K / $507K / $898K revenue over Years 1–3, but only ~$13K MRR at month 12, so the gates and kill rule are reset.

## 1. TWK deployment: hybrid

**Decision (founder, Oct 20, 2026):** hybrid. Firm-only knowledge goes to the cloud (Glass); client data stays on-prem (the appliance). Details and consequences: [11-related-workstreams.md](11-related-workstreams.md#decision-hybrid-deployment-oct-20-2026).

The headline pitch needs one qualifier: "client data never goes to an outside AI provider." At TWK, firm knowledge does go to Anthropic.

## 2. The calendar that drives everything

Two rules in the source squeeze CPA installs into very few months:

- No CPA work January–April (tax season).
- "Schedule on-site work outside June–November" (the hurricane risk response).

Taken literally, together they leave only May and December. **[Analysis]** That would push almost all professional-firm setup revenue and subscription starts past month 12. Year 1 runs Oct 19, 2026 to Oct 18, 2027, assuming week 1 = Oct 19.

**Decision (founder, Oct 20, 2026): adopted.** These were first proposed as recommendations; the founder approved them the same day.

1. **Narrow the hurricane rule.** Don't schedule installs during an active named-storm watch for Calcasieu or Cameron. Prefer May–July and November–December. Keep the storm-watch shutdown runbook.
   - An indoor server install takes days, not weeks, and can move if a storm forms. Client #10 takes a day, per the plan.
   - The source's stronger wording reads as a risk response, not a ban.
2. **Bill half the setup fee at signing**, as the industrial terms already do (50% on start, 50% on acceptance). Setup cash then lands when a deal closes, not when the install happens.

Without these changes, most professional-firm revenue would have moved into Year 2, leaving Year 1 at roughly TWK plus industrial, well below the model's ~$155K. **[Analysis]**

## 3. Hiring: the realistic plan

### Why the original plan doesn't hold

The first hire's trigger and its timing conflict:

- The trigger is "8–10 clients AND 3 months of payroll in the bank".
- The target timing is months 9–12.
- But the plan has only 4–5 clients at month 12. ([08](08-implementation-roadmap.md#hiring))

The second hire has the same problem: it needs 15–20 clients by months 22–26, but Year 2 ends with 11.

The client ramp is also slower than the plan's gates assume. **[Analysis]**

- With a 5-month average sales cycle and the January–April blackout, CPA closes before May 2027 (month 7) are unlikely.
- Referrals through Chris could shorten that.
- A realistic month-12 count is TWK plus 2–4 clients.

### Research findings

| Topic                      | Finding                                                                                                                                                                                                                                                                                                                                                                                                                                                | Quality                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Lake Charles pay, support  | Computer user support specialists (15-1232): 140 employed; median $26.23/hr; mean $54,480 (May 2023 data) [Sourced: [BLS OEWS Lake Charles MSA, May 2023](https://www.bls.gov/oes/2023/may/oes_29340.htm), checked directly]                                                                                                                                                                                                                           | High; the data are about 3.4 years old  |
| Lake Charles pay, sysadmin | Network and computer systems administrators (15-1244): 50 employed; median $41.28/hr; mean $92,430 (May 2023 data) [Sourced: same table]                                                                                                                                                                                                                                                                                                               | High; about 3.4 years old               |
| Loaded cost                | At establishments with 1–49 workers, wages are 74.1% and benefits 25.9% of total compensation (March 2026), about a 1.35× multiplier on wages [Sourced: [BLS ECEC, June 12, 2026](https://www.bls.gov/news.release/archives/ecec_06122026.htm)]                                                                                                                                                                                                        | High; checked directly                  |
| MSP technician load        | About 350 managed endpoints per technician is cited as a benchmark [Sourced: [Acronis](https://www.acronis.com/en-us/blog/posts/un-break-your-business-model-benchmarks-and-tools-for-msps)]. Survey answers vary widely (101–250 to 750+) [Sourced: [Kaseya 2023](https://www.kaseya.com/blog/2023-msp-benchmark-survey-findings/)]                                                                                                                   | Low-medium; vendor sources              |
| When MSPs hire             | Advice is qualitative: hire at 60+ hour weeks; hire the next person once the last one generates close to double their cost [Sourced: [Chartec](https://chartec.net/msp-growth-when-and-who-to-hire/)]. No sourced "hire at $X MRR" rule was found.                                                                                                                                                                                                     | Low; single source                      |
| Contract help              | Fractional senior DevOps median about $110/hr [Sourced: [Go Fractional](https://www.gofractional.com/insights/rates/senior-devops-engineer)]. A Linux DevOps contract posting at $42–52/hr [Sourced: [Insight Global](https://insightglobal.com/jobs/find_a_job/job-498457)]                                                                                                                                                                           | Low; national, unverified for Louisiana |
| Student workers            | IT interns average about $18.66/hr (range $12–30) [Sourced: [Payscale](<https://www.payscale.com/research/US/Job=Information_Technology_(IT)_Intern/Hourly_Rate/6092e990/Entry-Level>)]                                                                                                                                                                                                                                                                | Low                                     |
| Key-person risk            | SBA lenders may require life insurance when the business depends on one person, often 1–1.5× the loan balance [Sourced: [Coleman Report on SOP 50 10 8](https://colemanreport.com/a-review-evaluation-and-interpretation-of-the-sba-life-insurance-requirements-across-the-three-most-recent-sba-standard-operating-procedures-including-sop-50-10-8-5-29-25), [Lendistry](https://lendistry.com/why-life-insurance-is-often-required-for-sba-loans/)] | Medium; lender sources                  |

No public benchmark was found for "clients per engineer" on on-prem GPU and RAG appliances. The plan's figures of ~10 clients per person and ~20 per first hire are unsupported until measured.

### Analysis

All points in this subsection are [Analysis].

1. **Support load is not the bottleneck; installs are.**
   - MSP ratios of hundreds of endpoints per technician mean steady-state support for 5–10 firms of 15–40 users each is well under one full-time person.
   - The real load is setup work: appliance install, Microsoft 365 permissions, document loading, 2–3 workflows and training.
   - The calendar bunches that work, which suits contract help better than a salaried hire.
2. **The plan's salary is at the low end for the skills.**
   - Annual medians: support ~$54.6K, sysadmin ~$85.9K ($26.23 and $41.28 × 2,080 hours).
   - The image-based install is designed so a support-level person can run it. A hire who can also handle Linux, GPU serving and Microsoft 365 sits between those two medians.
   - At 1.35×, a $55–75K base costs about $74–101K loaded, or $6.2–8.4K a month. That is slightly above the plan's ~$70–95K.
3. **The affordability test.**
   - Assumption: a hire is affordable when its loaded cost is no more than about a third of MRR. This is a working rule, not a benchmark; Chartec's "close to double their cost" heuristic is stricter.
   - On that rule the hire needs MRR of about $20–25K.
   - At a blended $3,000–3,500 per client, that is 6–8 clients. At the ~$2,600 average the model may imply (see [C14](12-open-questions.md#contradictions-found)), it is 8–10 clients, the original trigger.
   - Count in dollars of MRR, not in clients.
4. **The trigger must not fire too early.**
   - At a 55–60 hour week, the Year-1 split (40% delivery, 20% support) is already about 33–36 hours of delivery and support.
   - Overlapping installs are likely in peak months.
   - The 3-month payroll gate is easy to meet right after a $375–400K raise.
   - So MRR has to be the mandatory trigger.
5. **Key-person risk needs an answer before a hire.**
   - Lenders, and CPA and law clients, will ask who can restore service if the founder is unavailable.
   - A contracted backup engineer with sealed emergency access answers that from the first non-TWK client.

### Revised hiring plan

**Recommendation** (replaces the hiring triggers and timing in [08](08-implementation-roadmap.md#hiring)):

| Stage                                               | When                                                                          | What                                                                                                                                                                                                                                                                                                        | Cost [Analysis]                                                 |
| --------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Backup and runbooks                                 | Months 1–6, from the first non-TWK client                                     | A contract Linux/GPU engineer with sealed emergency access and the runbooks; term life and disability cover                                                                                                                                                                                                 | Small retainer plus hourly use at $60–110/hr                    |
| Contract install help                               | Months 6–14, around installs                                                  | Contract engineer for about 10–20 hours a month in install months; a McNeese student worker for documentation and light setup (no access to client data)                                                                                                                                                    | $600–2,200/month contract; student $15–20/hr for 10–15 hrs/week |
| First W-2 hire: support and implementation engineer | Expected months 15–24; the earlier end if the blended subscription is $3,000+ | **Mandatory:** MRR of about $20–25K, plus 3 months of payroll in the bank. **Plus one of:** (b) founder spending more than ~35 hrs/week on delivery and support for 8 weeks, measured in a time log; (c) two client installs overlapping in the pipeline; (d) a client contract requiring a named P1 backup | Base $55–75K; loaded ~$74–101K                                  |
| Convert contractor to W-2 early                     | Any time                                                                      | If contract spend exceeds about $4–5K a month for two months and the MRR trigger is near                                                                                                                                                                                                                    | —                                                               |
| Second hire: engineer or sales lead                 | Expected months 28–32                                                         | MRR of about $45K+ (about 15 clients at a $3,000+ blend) AND operating profit in the trailing quarter                                                                                                                                                                                                       | Plan's $65–90K base, at ~1.35× loaded                           |
| Override                                            | Any time                                                                      | Risk-register rule stays: fewer than 15 sales conversations a month for two months → pull the hire forward                                                                                                                                                                                                  | —                                                               |

**Effect on the numbers [Analysis]:**

- The first hire still lands inside Year 2, so "Staff: Year 2 = 1, Year 3 = 2" in the model stays directionally right.
- The $25K "first hire, months 9–12" use-of-funds line becomes Year-1 contract engineering, student help and key-person insurance.
- Contract plus student costs over months 6–14 come to about $11–31K. That can use up the full $25K, so don't count on a remainder for the buffer.
- The hire's Year-2 salary must come from revenue, as in the original model.
- TODO: re-run the 3-year model with these changes.

## 4. Industrial revenue: the realistic plan

### Why the original target doesn't hold

The industrial target is $150K–$250K from 6–10 engagements in 12 months.

- That is roughly equal to or above total Year-1 company revenue in the financial model (~$155K).
- It implies about $15–42K per engagement, around $25K at the midpoint.

The likeliest first sales are smaller: the contractor compliance package ($2,500–6,000 setup plus $400–900 a month) and a $5,000 pilot study ([03](03-products-and-services.md#industrial-services)). **[Analysis]** The engagement count is plausible; the dollars per engagement are not.

### Research findings

| Topic                                      | Finding                                                                                                                                                                                                                                                                                                                                                                                                                                   | Quality                                          |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| What contractors already pay the platforms | ISNetworld about $1,700–5,000/yr by headcount plus a setup fee [Sourced: [ISN FAQ via FitGap summary](https://us.fitgap.com/products/isnetworld)]. Avetta about $450–900 per supplier per year [Sourced: [ERP Research](https://erpresearch.com/erp-add-ons/supplier-management/avetta/pricing)]                                                                                                                                          | Low-medium; secondary sources, not opened        |
| Consultant pricing for ISN upkeep          | No published rates found. The source's own benchmark (about $5,000/yr; $150–300/hr) stays [Estimate; vendor listing]                                                                                                                                                                                                                                                                                                                      | Gap                                              |
| Plant vendor setup                         | A refinery example: vendor profile and W-9; ISNetworld is the "source of truth" for service providers; safety reviews at several stages [Sourced: [Delek US supplier page](https://delekus.com/business-operations/refining/supply-chain/becoming-a-supplier/default.aspx)]. Generic supplier onboarding takes 2–4 weeks, or 4–12 for complex vendors [Sourced: [ProcureKey](https://www.procurekey.com/blog/supplier-onboarding-guide/)] | Medium for the Delek example; low for the timing |
| Industrial sales cycles                    | 6–18 months for industrial buyers in general [Sourced: [Salesmotion](https://salesmotion.io/blog/how-to-sell-to-manufacturing)]                                                                                                                                                                                                                                                                                                           | Low; generic                                     |
| Reliability consultant rates               | Oilfield reliability consultants at $1,150–1,550/day (4–9 years) and $1,650–2,250/day (10+ years) [Sourced: [Rigzone](https://www.rigzone.com/insights/salary-1/how-much-does-a-reliability-consultant-earn-in-oilfield-operations-147/)]                                                                                                                                                                                                 | Low; single source                               |
| AI pilot conversion                        | 68% of manufacturers are still in pilots or proofs of concept; 7% have AI in core operations [Sourced: [HiveMQ](https://www.hivemq.com/blog/industrial-ai-pilot-why-68-percent-manufacturers-cant-scale-past-poc/)]                                                                                                                                                                                                                       | Low; vendor marketing, directional               |
| Solo consultant ramp                       | 58% serve 6 or fewer clients a year; more than half reach their prior income within 2 years [Sourced, from a search summary: [Consulting Success](https://www.consultingsuccess.com/?p=59883)]                                                                                                                                                                                                                                            | Low; survivor bias                               |
| Local demand timing                        | Louisiana industrial construction labor demand projected to peak at about 20,500 workers in late 2026 to early 2027, led by Woodside Louisiana LNG and CP2 [Sourced: [10/12 Industry Report](https://www.1012industryreport.com/?p=129096)]                                                                                                                                                                                               | Medium; trade press                              |

The industrial research worked from search-result summaries; most pages were not opened. Treat these as directional, and don't quote them to investors until each is checked.

### Analysis

All points in this subsection are [Analysis].

1. **Contractor compliance is the only fast, real buyer in Year 1.**
   - Owner-operated contractors decide alone and buy on a handshake.
   - LNG construction labor demand peaks late 2026 to early 2027, so contractors are being prequalified now.
   - The window narrows as construction winds down in 2027–28.
2. **Retainer pricing needs testing.**
   - Contractors already pay the platform about $1,700–5,000 a year.
   - A $400–900 monthly retainer ($4,800–10,800 a year) sits on top of that. The source's own ISN-upkeep benchmark is about $5,000 a year.
   - Expect retainers toward the $400–600 end until there is proof.
3. **Plant work has a long critical path.**
   - The company needs, for itself:
     - BOP and TWIC;
     - site orientations;
     - insurance that may need $2–5M limits (as the source says);
     - its own vendor registration, likely including ISNetworld (the Delek example).
   - Only then can the plant cycle start, and plant cycles are long.
   - A first plant PO at months 7–12 is the base case. Months 4–6 is a stretch that needs a plant contact sponsoring a small PO.
   - Most plant data arrives as exports, so the hurricane window matters less here than for installs.
4. **Larger projects need a track record.**
   - Tribal-knowledge capture ($25–75K), PSM documentation ($15–40K) and turnaround tooling ($20–50K) need a case study and repeat plant relationships.
   - The source says to sell turnaround work 3–6 months ahead. Expect these in Year 2.
5. **Industrial's real Year-1 job is timing.**
   - It's the one track besides law that can sell and deliver in January–April, while CPA firms are blacked out.
   - It is the cash and calendar complement to the CPA track, not the main revenue line.

### Founder time budget

All figures in this subsection are [Analysis]; the hours per task are assumptions to replace with the time log.

- **Capacity:** about 50 hours a week × 48 weeks × 40% delivery ≈ 960 delivery hours in Year 1.

| Work                                                                                                                  | Assumed hours |
| --------------------------------------------------------------------------------------------------------------------- | ------------- |
| TWK pilot: appliance v1, evaluation set, Microsoft 365 integration, 3 CPA workflows, compliance kit v1, install image | 450–550       |
| 2–4 CPA/law setups from the image (~60–100 hrs each)                                                                  | 120–400       |
| Industrial base: 5–7 compliance packages (~20–40 hrs each), one pilot study (~40), one paid sample (~20–30)           | 160–350       |
| **Total**                                                                                                             | **730–1,300** |

- **The base case only fits** if compliance packages stay light and setups come off the image.
- **The stretch case does not fit** without the contract engineer from section 3.

### Revised industrial plan

**Recommendation** (replaces the industrial track target in [03](03-products-and-services.md#industrial-services)). Each compliance client is worth about $5.5–7.5K in Year 1: a ~$4K average setup, plus 4–6 months of retainer at $400–600. **[Analysis]**

| Case                   | Year-1 industrial revenue | Engagements | Mix [Analysis]                                                                                                 |
| ---------------------- | ------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| Conservative           | $10–25K                   | 3–5         | 3–4 compliance setups at the low end ($2,500–3,500) with few retainer months (~$9–19K); possibly one $5K pilot |
| **Base (plan figure)** | **$35–60K**               | **7–9**     | 5–7 compliance clients (~$27–52K); one $5K pilot bad-actor study; one $3–5K knowledge-capture sample           |
| Stretch                | $80–120K                  | 9–12        | Base, plus one or two $15–30K plant-sponsored studies or an $8–15K bid-automation job                          |

Research view for comparison: the industrial research agent's own estimate was $8–20K conservative, $25–50K base and $70–100K stretch. This plan sits slightly higher because of the LNG prequalification peak.

**Revised milestones:**

| Milestone                                              | Original                                         | Revised                                                                                                      |
| ------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| First paid industrial engagement                       | Within 90 days                                   | Months 2–4: a contractor compliance package through the friends network. Keep the 90-day goal as the target. |
| Own vendor setup (ISN, insurance limits, orientations) | Not scheduled                                    | Start in month 1; on the critical path                                                                       |
| First plant PO                                         | Within 6 months (weeks 11–12 in the weekly plan) | Base months 7–12; stretch months 4–6 with a sponsor                                                          |
| Case study                                             | Month 9                                          | Months 9–12 (contractor compliance case study first)                                                         |
| Industrial revenue, 12 months                          | $150K–$250K                                      | $35–60K base; above that is upside                                                                           |
| Year 2                                                 | —                                                | $75–125K: 10–15 compliance retainers plus 1–3 plant projects [Analysis]                                      |
| Year 3                                                 | 15% of ~$860K (~$129K)                           | $120–180K; the model's ~$129K is defensible [Analysis]                                                       |

**Price test:** run the first 5–10 contractor compliance packages as fixed-price offers, with a case-study discount, to confirm what retainers they'll pay before printing the price sheet.

## 5. Regenerated 3-year model

The original spreadsheet wasn't available, so the model was rebuilt on Oct 20, 2026.

- **Files:** [model/private-ai-3yr-model-2026-10-20.xlsx](model/private-ai-3yr-model-2026-10-20.xlsx), generated by [model/build_model.py](model/build_model.py) with [model/calib.json](model/calib.json).
- **Structure:** a 36-month, formula-driven model (6,772 formulas, zero errors) with four scenarios side by side. Every input is on the Inputs and Schedules sheets, with its source.
- **Labels:** every figure in this section is **[Analysis]**.

### How the original plan was reconstructed

The "Original plan" scenario is calibrated to the founder brief. It reproduces the source revenue (Year 1 within $2,702; Years 2–3 within $35) and operating results (−$95K / +$15K / +$155K). Gross margin comes out at 65.0% / 67.3% / 68.6%, against the source's 66% / 68% / 69%.

| What was calibrated             | Value                        | How                                                                                                                      |
| ------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Average subscription per client | ~$2,490/month                | From the source's Year-3 mix (subscriptions 55% of ~$860K)                                                               |
| Setup per client                | ~$19,100                     | Setup 20% of Year 3 ÷ 9 new clients                                                                                      |
| Add-on adoption                 | ~52% of clients              | Workflows 10% of Year 3                                                                                                  |
| Industrial project revenue      | $0 / ~$92K / ~$109K          | Fills the gap to the source revenue totals; Year 3 lands at 12.7%, not 15%, because hardware margin also sits in revenue |
| Unitemized costs                | ~$33K / ~$43K / ~$58K a year | Fills the gap to the source operating results after itemized costs; itemize when the original spreadsheet turns up       |

**Two validations:**

- The calibrated original plan independently reproduces the source's operating breakeven at month 24 (source: months 23–24).
- It confirms [C14](12-open-questions.md#contradictions-found): the original model assumed roughly Starter-level pricing (~$2,490), not the $4,500 used in the unit economics.

### Scenario design

- **Base:** uses the original model's implied pricing (~$2,500/month, ~$19,000 setup). The difference from the original plan is therefore only the Oct 20 revisions: CPA calendar timing, half of setup billed at signing, industrial mix, contract help and later hires.
- **Conservative:** fewer clients, $15,000 setup and 25% add-on adoption.
- **Stretch:** more clients at a half-Starter, half-Professional blend ($3,500/month, $25,000 setup).
- **Hire dates:** each scenario's first hire starts the month after its MRR first reaches about $20K.

Signings by month are on the Schedules sheet.

### Results

| Metric                                              | Original plan            | Conservative            | **Base**                     | Stretch                   |
| --------------------------------------------------- | ------------------------ | ----------------------- | ---------------------------- | ------------------------- |
| Revenue, Years 1 / 2 / 3                            | $158K / $465K / $860K    | $113K / $292K / $529K   | **$190K / $507K / $898K**    | $298K / $867K / $1,528K   |
| Operating result, Years 1 / 2 / 3                   | −$95K / +$15K / +$155K   | −$119K / −$34K / +$32K  | **−$66K / +$78K / +$217K**   | +$6K / +$283K / +$625K    |
| Industrial revenue, Years 1 / 2 / 3                 | $0 / $92K / $109K        | $20K / $61K / $79K      | **$51K / $115K / $156K**     | $97K / $222K / $281K      |
| Professional clients incl. TWK, months 12 / 24 / 36 | 4 / 11 / 20              | 3 / 8 / 14              | **4 / 11 / 20**              | 5 / 14 / 25               |
| MRR, months 6 / 12 / 24 / 36                        | $7K / $13K / $29K / $60K | $4K / $8K / $21K / $41K | **$6K / $13K / $39K / $69K** | $7K / $21K / $63K / $116K |
| MRR first reaches $20K                              | Month 20                 | Month 23                | **Month 16**                 | Month 12                  |
| First hire (model input)                            | Month 10                 | Month 26                | **Month 17**                 | Month 14                  |
| Breakeven (trailing 12 months positive)             | Month 24                 | Month 30                | **Month 18**                 | Month 12                  |
| Cash trough before funding                          | −$186K                   | −$264K                  | **−$123K**                   | −$83K                     |
| Capital needed (trough + 6-month buffer)            | $285K                    | $361K                   | **$220K**                    | $180K                     |
| Lowest cash with the $400K raise (closing month 5)  | −$86K                    | −$84K                   | **−$79K**                    | −$73K                     |
| Cash, month 36                                      | $356K                    | $161K                   | **$511K**                    | $1,196K                   |

### What the model shows

1. **The base case beats the original plan.** It's ahead on every year at the same prices and client counts. The gains come from earlier cash (setup billed at signing), the industrial compliance retainers, and contract help instead of a month-10 hire.
2. **But its recurring revenue at month 12 is about the same** (~$13K), short of the original gate of $20K. Revenue is front-loaded.
3. **The $400K raise covers every scenario's capital need,** including the conservative case at ~$361K.
4. **Every scenario needs about $75–85K before the raise closes.**
   - Costs start in month 1 (salary, appliance, formation), while debt and equity close in month 5.
   - Bridge it with founder capital, which the source plans for "weeks 1–2" but never sizes. Or close part of the raise earlier, or defer the $35K demo appliance as the source's own under-$250K fallback suggests.
5. **The conservative case is the real risk.**
   - It loses money through Year 2 and breaks even only in month 30.
   - It trips the month-12 kill criterion (3 professional clients including TWK = 2 beyond TWK).
   - The kill criterion is doing its job here.
6. **The trough reconciliation is still open.** The calibrated original plan's trough (−$186K) is deeper than the source's ~$155K. The source's capital decomposition still doesn't reconcile ([C6](12-open-questions.md#contradictions-found)).

### Main simplifications

- The 5% escalator applies per model year, not per client anniversary.
- No churn.
- Interest and principal hit cash, not the operating result.
- The unitemized costs apply to every scenario.
- The demo appliance is expensed to cash in month 1.
- Debt is $200K at 10.5% over 10 years [To verify SBA terms]; equity is $200K; both close in month 5.

Founder capital is set to $0 until it's known (TODO).

## 6. Revised gates and kill criterion

**Decision (founder, Oct 20, 2026): adopted.** This replaces the 90-day / 6-month / 12-month gates in [08](08-implementation-roadmap.md#plan-on-a-page) where they differ.

Client-count gates count **signed professional-firm contracts** (CPA or law, beyond TWK). MRR gates count **all recurring revenue**, including industrial retainers.

| Horizon                            | What done looks like                                                                                                                                                | Gate to the next phase                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 90 days (unchanged, with one edit) | As in [08](08-implementation-roadmap.md#plan-on-a-page), plus own vendor setup started (ISN registration, insurance limits, orientations)                           | TWK staff use it weekly with measured time savings; one non-TWK invoice paid (expected from contractor compliance) |
| 6 months (mid-April 2027)          | Funding closed; attorney opinion on §7216 and founder access; two MSP partners signed; 1 professional client beyond TWK signed; 3+ contractor compliance clients    | MRR of $5K; pipeline of 15 named buyers                                                                            |
| 9 months (mid-July 2027)           | 2 professional clients beyond TWK signed; first case study published (contractor compliance or TWK)                                                                 | MRR of $9K                                                                                                         |
| 12 months (mid-October 2027)       | 3 professional clients beyond TWK signed; 5–7 contractor compliance clients; first plant PO; Lafayette outreach started; SDVOSB certified; founder time log running | MRR of $14K                                                                                                        |
| First hire (expected months 15–24) | Support and implementation engineer running installs; founder out of first-line support                                                                             | MRR of $20–25K, plus the other hiring conditions in [section 3](#revised-hiring-plan)                              |
| 36 months                          | Unchanged; re-check after the model re-run                                                                                                                          | Unchanged                                                                                                          |

**Weekly metric targets, revised:** MRR of $5K by month 6, $9K by month 9 and $14K by month 12. The regenerated model's base case gives ~$5.8K / ~$8.8K / ~$12.8K, so the month-12 target sits slightly above the base case. These replace "$10K by month 6; $20K by month 12".

**Kill criterion, revised:** if there are fewer than 3 **signed** professional-firm contracts (CPA or law) beyond TWK at month 12, pivot to fractional CTO and project work, and stop the appliance offer. Industrial retainers don't count, because they test a different offer. The other kill criteria are unchanged.

**Hurricane rule, revised:** don't schedule installs or on-site work during an active named-storm watch for Calcasieu or Cameron. Prefer May–July and November–December for CPA installs. Keep the shutdown runbook. This replaces "schedule on-site work outside June–November".

**Setup billing, revised:** 50% at signing and 50% at acceptance, for every setup and implementation fee.

## Open items created by this revision

- Size founder capital, or an early partial close, to bridge the ~$75–85K needed before month 5.
- When the original spreadsheet turns up, itemize the calibrated "unitemized" costs and recheck the trough.
- Price-test contractor compliance retainers with 5–10 contractors.
- Confirm plant insurance minimums and vendor-registration steps at Citgo and Sasol.
- Get BLS May 2025 Lake Charles wages; the codes didn't parse from the current table when tried on Oct 20.
- Start a founder time log from the first install, to test the ~10-clients-per-person assumption and the hours in the time budget.
- Record TWK's discount and tier; the re-run assumes about $20,000 setup and $3,800 a month.
