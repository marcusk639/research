# 03 — Products and Services

> As of 2026-10-19. Labels: see [REPORT.md](REPORT.md#labels-used).

**Summary.** Professional firms buy in a fixed sequence: assessment, then setup, then a monthly subscription, with workflow add-ons after the first quarter. Industrial clients buy fixed-fee projects that convert to monthly retainers. Hardware is always the client's, paid directly or passed through at cost plus 8%.

## Engagement sequence and packaging rules

- Every engagement goes assessment, then setup, then subscription. Add-ons come after the first quarter.
- Hardware is a separate line the client pays for directly, or passed through at cost plus 8%. The company never carries inventory.
- Contracts are 12 months, auto-renewing, with a 5% escalator (the MSP norm is 5–8%).
- **Decision (Oct 20, 2026):** setup and implementation fees are billed 50% at signing and 50% at acceptance ([14](14-revised-plan-2026-10-20.md#6-revised-gates-and-kill-criterion)).
- Industrial pricing stays under the buyer's approval limit (typically $25–50K) by phasing larger work.
- Offer a 10–15% discount for case-study and reference rights on the first three clients per vertical.

## Core professional-firm offers

| Offer                                   | What's included                                                                                                         | Price                                                  | Notes                                               |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------- |
| Assessment                              | Half-day review of documents, systems and compliance gaps; written plan                                                 | $2,500, credited to setup                              | Low-risk first yes                                  |
| Setup and implementation                | Appliance install, Microsoft 365 sync with permissions, document loading, 2–3 workflows, compliance kit, staff training | $15,000–40,000 one-time                                | Scales with document volume and integrations        |
| Starter subscription (up to 15 users)   | Monitoring, model updates, backups, support, usage reports                                                              | $2,500/month                                           | 12-month term, 5% annual escalator                  |
| Professional subscription (16–40 users) | Same, plus quarterly workflow reviews                                                                                   | $4,500–6,500/month                                     |                                                     |
| Workflow add-ons                        | Tax research memos, document intake, contract review, discovery summaries, SOP Q&A, bid drafting                        | $500–2,000/month each                                  | Built once per vertical, resold to every client     |
| Compliance kit (standalone)             | AI use policy, WISP addendum, §7216 or Rule 1.6 vendor file, access logs                                                | $3,000–7,000                                           | Also sold to firms that keep Copilot                |
| Training                                | Half-day staff sessions                                                                                                 | $1,500–3,000                                           | Drives adoption, which drives renewal               |
| Hardware                                | Client-purchased appliance: one 96GB GPU server, UPS, install                                                           | $25,000–35,000 pass-through, plus 8%                   | Small-office tier (DGX Spark class) at about $5,000 |
| Industrial projects                     | Knowledge capture, bad-actor studies, PSM documentation, turnaround tooling, contractor compliance                      | $15,000–75,000 per project; $400–5,000/month retainers | See industrial services below                       |

TODO: no tier or price is given for firms above 40 users. CPA targets run to 50 staff.

The "$15,000–75,000 per project" range doesn't match the industrial service prices below, several of which start lower. See [12-open-questions.md](12-open-questions.md#contradictions-found).

## Hardware tiers

| Tier         | Hardware                                                         | Users    | Price                                |
| ------------ | ---------------------------------------------------------------- | -------- | ------------------------------------ |
| Standard     | One 96GB GPU server (RTX Pro 6000 Blackwell class), UPS, install | 10–50    | $25,000–35,000 pass-through, plus 8% |
| Small office | DGX Spark-class box                                              | Under 10 | About $5,000                         |

Technical detail: [06-technical-architecture.md](06-technical-architecture.md#design-decisions).

## Compliance kit contents

| Vertical | Contents                                                                                                                                                                |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPA      | AI use policy, WISP addendum, §7216 vendor file, access logs. Separately, §7216 consent templates are provided to every CPA client, regardless of the attorney opinion. |
| Law      | AI use policy, vendor due-diligence file, verification and incident logs, client communication language (Rule 1.6 / ABA 512 kit)                                        |

The Rule 1.6 kit sells standalone and opens the door for the appliance. Legal basis: [07-compliance-and-legal.md](07-compliance-and-legal.md).

## Industrial services

Fixed-fee projects come first, then convert to subscriptions.

| #   | Service                       | What the buyer gets                                                                                                                                                                      | Price                                                                    | Margin | Delivery                                       | Likelihood of first sale                                     |
| --- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------ | ---------------------------------------------- | ------------------------------------------------------------ |
| 1   | Contractor compliance package | ISNetworld/Avetta/Veriforce questionnaires drafted and maintained; written safety programs; certificate and orientation tracking with expiry alerts; certificate-of-insurance gap checks | $2,500–6,000 setup, then $400–900/month                                  | 75–85% | 2–3 weeks                                      | Highest                                                      |
| 2   | Bid and RFP automation        | Private assistant trained on past bids, safety stats and capabilities that drafts responses and prequalification packages                                                                | $8–15K setup, $750–1,500/month                                           | 70–80% | 4–6 weeks                                      | High for contractors chasing LNG work                        |
| 3   | Tribal-knowledge capture      | Interviews and walkdowns with retiring operators/mechanics, turned into troubleshooting guides, procedure updates and an on-site assistant                                               | $25–75K per unit or group of 3–5 experts; $1,500–3,000/month to maintain | 55–70% | 8–16 weeks                                     | Medium; strongest differentiation and highest lifetime value |
| 4   | PSM documentation support     | Procedure drafting/reformatting, MOC packages, PSSR checklists, 3-year audit prep on a private assistant trained on the site's PSI                                                       | $15–40K per project; $2,500–5,000/month retainer                         | 60–70% | 6–12 weeks                                     | Medium                                                       |
| 5   | Reliability bad-actor study   | Analysis of 3–5 years of SAP/Maximo work orders: top 20 bad actors, repeat failures, cost by unit, recommended actions                                                                   | $15–30K fixed                                                            | 75–85% | 4–6 weeks                                      | Medium-high                                                  |
| 6   | Turnaround support tooling    | Daily progress, permit and headcount dashboards; contractor onboarding tracker                                                                                                           | $20–50K per event                                                        | 65–75% | 2–4 weeks build, then on site during the event | Medium; sell 3–6 months ahead                                |
| 7   | Training content              | Procedure walk-throughs, troubleshooting scenarios, new-hire modules                                                                                                                     | $10–30K per module set                                                   | 70–80% | 4–8 weeks                                      | Medium-high at new LNG terminals                             |

**Benchmark:** compliance consultants charge $150–300/hour, or about $5,000/year for ISNetworld upkeep [Estimate; vendor listing].

**Industrial terms:** 50% on start, 50% on acceptance. Every deliverable is marked "draft for qualified review."

### Bundles

| Bundle             | Services | For                                                   |
| ------------------ | -------- | ----------------------------------------------------- |
| "Contractor-ready" | 1 + 2    | Firms chasing LNG construction work                   |
| "Turnaround-ready" | 6 + 7    | Sold to the plant and its lead contractor together    |
| "Retirement-ready" | 3 + 4    | Units with known retirements in the next 12–24 months |

### Small first jobs that open doors

| Offer                                                                                     | Price  |
| ----------------------------------------------------------------------------------------- | ------ |
| Contractor "paperwork audit" (2 hours)                                                    | Free   |
| Pilot bad-actor study on one unit, delivered in two weeks                                 | $5,000 |
| One retiring-mechanic interview turned into a 10-page troubleshooting guide (paid sample) | $3–5K  |

**Most likely first sales:** service 1 (by a local contractor) and service 5 (by a plant reliability engineer).

**Industrial track target:**

- $150K–$250K of industrial revenue from 6–10 engagements in 12 months;
- first paid industrial engagement within 90 days;
- first plant PO within 6 months;
- one case study by month 9.

**Revised (Oct 20, 2026):** the realistic Year-1 industrial base case is $35–60K from 7–9 engagements, led by contractor compliance. The first plant PO is expected in months 7–12. Above $60K is upside. See [14-revised-plan-2026-10-20.md](14-revised-plan-2026-10-20.md#4-industrial-revenue-the-realistic-plan).

## Workflow library

### First three CPA workflows (implementation plan)

1. Document intake and classification by form type and tax year.
2. Tax research memo drafting with citations.
3. Client-notice response drafting.

### Candidate roadmap (from "RAG Applications for a Mid-Sized CPA Firm")

The research catalogued 20 candidate RAG applications for a 15–25-person CPA firm, in staged order. Numbers in parentheses are the research's application numbers.

**Recommendation:** no comparison showed a custom build beating a bought product. Buy tax-authority research and source-document extraction rather than build them.

| Stage                                           | Contents                                                                                                                                                                                                                                                                        |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stage 0 (prerequisites)                         | Audit content and measure use of the existing bot; adopt an AI policy; decide the §7216 basis, defaulting to consent, with a counsel-drafted form and a consent register; inventory what the tax, document and practice-management systems can export; name a second maintainer |
| Stage 1 (firm knowledge, no client identifiers) | HR and IT answers (4); feedback loop and gap analytics (1); template-grounded drafting with placeholders (5); SOP capture (2); onboarding mode (3), only if cheap                                                                                                               |
| Stage 2 (client documents, after consent)       | Notice response (10); advisory narratives from a completed return (13); review checklist assistant (12); pilots: firm memo library (14) and bookkeeping playbooks (18)                                                                                                          |
| Stage 3 (connector-dependent)                   | Pre-meeting brief with one-client prior-work search (7, 9); missing-items check (11); law-change monitor (16); meeting debrief (6) and email drafting (8): buy first                                                                                                            |
| Later or deferred                               | Firm-metrics Q&A (17), approval-gated actions (20), client-facing assistant (19)                                                                                                                                                                                                |
| Alongside Stage 1                               | Citation checker (15), if sent only citations                                                                                                                                                                                                                                   |

**Calendar assumption:** consent forms are ready for the December–January engagement mailing; no new tooling February to mid-April.

## Future products

- **RAG platform as plug-and-play knowledge bases** for businesses beyond CPA firms. See [11-related-workstreams.md](11-related-workstreams.md#rag-platform-as-a-product).
- **Shared hosting** (Stage 2) for clients who want private AI without owning a server. See [08-implementation-roadmap.md](08-implementation-roadmap.md#deployment-stages).
