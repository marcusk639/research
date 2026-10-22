# Private AI

> Status: draft · Started: 2026-10-19 · Facts as of 2026-10-19 · Source: [prompts/init.md](prompts/init.md)

**Summary.** Private AI (working name) is a managed private-AI service for professional firms and industrial businesses in Southwest Louisiana, expanding along I-10 to Lafayette and Baton Rouge. Clients get an AI assistant on a server in their own building that answers from their own documents with citations and comes with the compliance documentation their regulator expects. The base case grows to ~$860K revenue and 19–20 clients in Year 3 on a $400K raise.

## Research Question

How should the Private AI venture be documented, from the founder's consolidated brief, as one consistent reference? It needs to serve the founder's working use, investor and lender materials, and future Claude sessions.

## Key Findings

### The business in one page

- **What it is:** a managed private-AI service, installed in the client's building, never sending client data to an outside AI provider. Two qualifiers: off-site backups and failover ([C9](12-open-questions.md#contradictions-found)), and at TWK, firm-only knowledge runs on Glass under the hybrid decision.
- **Who pays, in order:** CPA firms, then law firms, then the plants and industrial contractors of the Lake Charles–Westlake–Sulphur corridor.
- **Why they buy:** compliance first, then productivity.
  - IRC §7216 and IRS OPR Alert 2026-19 for tax preparers.
  - ABA Formal Opinion 512 for lawyers.
  - Plants won't let process data leave the fence.
- **Why this company wins:**
  - local, in-person installation and support, including after hurricanes;
  - a compliance package no national vendor ships;
  - Microsoft 365 permission-aware retrieval;
  - named vertical workflows;
  - founder credibility;
  - a reference client (TWK) in the first vertical.
- **Founder:** Marcus Klein. Air Force veteran (F-15 mechanic), about 10 years as a senior/staff software engineer including Meta, McNeese alumnus, based in Lake Charles. **Decision (Oct 18, 2026):** Private AI is his primary focus.

### Offers at a glance

| Offer                                   | Price                                                  |
| --------------------------------------- | ------------------------------------------------------ |
| Assessment                              | $2,500, credited to setup                              |
| Setup and implementation                | $15,000–40,000 one-time                                |
| Starter subscription (up to 15 users)   | $2,500/month                                           |
| Professional subscription (16–40 users) | $4,500–6,500/month                                     |
| Workflow add-ons                        | $500–2,000/month each                                  |
| Compliance kit (standalone)             | $3,000–7,000                                           |
| Hardware (client-purchased)             | $25,000–35,000 pass-through, plus 8%                   |
| Industrial projects                     | $15,000–75,000 per project; $400–5,000/month retainers |

Full detail: [03-products-and-services.md](03-products-and-services.md).

### Headline numbers (base case)

|                  | Year 1 | Year 2 | Year 3  |
| ---------------- | ------ | ------ | ------- |
| Clients (ending) | 4      | 11     | 19–20   |
| Revenue          | ~$155K | ~$465K | ~$860K  |
| Gross margin     | ~66%   | ~68%   | ~69%    |
| Founder salary   | $70K   | $100K  | $130K   |
| Operating result | ~−$95K | ~+$15K | ~+$155K |

Capital needed: about $375K (base). The plan raises $400K: debt $150–250K, then equity $150–250K. Details: [09-financials-and-funding.md](09-financials-and-funding.md).

### Status as of 2026-10-19

- TWK is the planned first paying client. No TWK work as of Oct 8; no signed SOW recorded.
- SAM.gov and/or VetCert applications are submitted and pending.
- The legal entity and name are undecided.
- The §7216 attorney opinion is not yet obtained.
- The VA Effective-Date & CUE Engine is parked (Oct 19, 2026).

### Resolved Oct 20, 2026

- **Decision:** TWK runs hybrid. Firm knowledge goes on Glass; client data stays on the appliance.
- **Hiring:** the first W-2 hire moves to about months 15–24, gated on MRR of about $20–25K, with contract backup first.
- **Decision: calendar.** Installs avoid only active storm watches, and setup is billed 50% at signing.
- **Decision: gates and kill rule.** Gates are reset at months 6, 9 and 12, counting signed professional-firm contracts. MRR targets are $5K, $9K and $14K.
- **Regenerated 3-year model** ([model/private-ai-3yr-model-2026-10-20.xlsx](model/private-ai-3yr-model-2026-10-20.xlsx)).
  - The original plan is reproduced by calibration.
  - Base: revenue ~$190K / $507K / $898K; breakeven at month 18; capital need ~$220K against the $400K raise.
  - About $75–85K is needed before the raise closes in month 5.
  - (Superseded: an earlier revenue-only re-run had base Year 1 at ~$210K and MRR ~$14K; the base case only ~$14K MRR at month 12, so it leans on one-time setup fees.)
- **Industrial:** the Year-1 base is $35–60K, and the first plant PO is expected in months 7–12.

See [14-revised-plan-2026-10-20.md](14-revised-plan-2026-10-20.md).

### Top open issues

1. Size founder capital or an early partial close for the ~$75–85K needed before month 5.
2. Karbon data classification under the hybrid split.
3. Price-test contractor compliance retainers.

Everything else: [12-open-questions.md](12-open-questions.md).

## Document map

| File                                                                                     | Purpose                                                                             |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [CONTEXT.md](CONTEXT.md)                                                                 | Short briefing for future Claude sessions                                           |
| [01-business-overview.md](01-business-overview.md)                                       | Idea, why now, why this founder, positioning                                        |
| [02-business-model.md](02-business-model.md)                                             | Revenue model, pricing, unit economics, margins                                     |
| [03-products-and-services.md](03-products-and-services.md)                               | Every offer, bundle, tier and add-on, with prices                                   |
| [04-market-and-clients.md](04-market-and-clients.md)                                     | Segments, sizing, named targets, buyer roles, TWK, competition                      |
| [05-go-to-market.md](05-go-to-market.md)                                                 | Sales tracks, channel partners, process, door-opening, objections                   |
| [06-technical-architecture.md](06-technical-architecture.md)                             | Appliance stack, design rules, integrations, RAG platform                           |
| [07-compliance-and-legal.md](07-compliance-and-legal.md)                                 | §7216, Safeguards, ABA 512, PSM, contracts, insurance, model origin                 |
| [08-implementation-roadmap.md](08-implementation-roadmap.md)                             | Horizons, phases, 90-day plans, hiring, runbooks, metrics, stages                   |
| [09-financials-and-funding.md](09-financials-and-funding.md)                             | 3-year model, capital need, raise structure, use of funds                           |
| [10-risks-and-kill-criteria.md](10-risks-and-kill-criteria.md)                           | Risk register and pivot rules                                                       |
| [11-related-workstreams.md](11-related-workstreams.md)                                   | TWK, RAG platform, fractional CTO, SDVOSB, VA CUE, entity                           |
| [12-open-questions.md](12-open-questions.md)                                             | Pending decisions, items to verify, contradictions and gaps                         |
| [13-sources.md](13-sources.md)                                                           | Source documents and outside sources                                                |
| [model/private-ai-3yr-model-2026-10-20.xlsx](model/private-ai-3yr-model-2026-10-20.xlsx) | Regenerated 3-year financial model (four scenarios)                                 |
| [14-revised-plan-2026-10-20.md](14-revised-plan-2026-10-20.md)                           | Oct 20 decisions and research-based revisions (supersede 01–13 where they conflict) |
| [glossary.md](glossary.md)                                                               | Terms and abbreviations                                                             |
| [prompts/init.md](prompts/init.md)                                                       | The prompt and source material these docs were written from                         |

## Labels used

| Label              | Meaning                                                            |
| ------------------ | ------------------------------------------------------------------ |
| [Estimate]         | An estimate in the source, kept as given                           |
| [Sourced]          | File 14 only: from outside research, linked inline                 |
| [Analysis]         | File 14 only: derived or assumed in that file, not from the source |
| [To verify]        | Flagged for checking before use                                    |
| **Decision**       | Something the founder decided                                      |
| **Plan**           | Something the founder plans, not yet a firm decision               |
| **Recommendation** | A recommendation from research, not a decision                     |
| TODO               | A fact the section needs that the source doesn't give              |

Figures are kept exactly as given, with their ranges. Files 01–13 are as of 2026-10-19; file 14 is as of 2026-10-20.

## Sources

Single source of truth: [prompts/init.md](prompts/init.md). Provenance of the underlying artifacts and outside sources: [13-sources.md](13-sources.md).
