# CONTEXT — Briefing for Claude Sessions

> As of 2026-10-20 (files 01–13 as of 2026-10-19). Read this first; it is short on purpose. Labels: see [REPORT.md](REPORT.md#labels-used).

**Summary.** Private AI (working name) is Marcus Klein's managed private-AI business in Lake Charles, Louisiana. It installs client-owned AI appliances for CPA firms, then law firms, then industrial plants and contractors. Treat [prompts/init.md](prompts/init.md) as the single source of truth, use the financial-model figures, and never put client data in these files.

## What the business is

- An on-prem AI assistant in the client's building.
  - Open-weight model on one 96GB GPU.
  - Answers from the client's documents with citations.
  - Microsoft 365 permission-aware.
  - Client data never goes to an outside AI provider. At TWK, firm-only knowledge runs on Glass (Anthropic) under the hybrid decision.
- Sold as assessment ($2,500), then setup ($15,000–40,000), then subscription ($2,500/month Starter; $4,500–6,500/month Professional), plus add-ons.
- Industrial track: fixed-fee projects (contractor compliance, bad-actor studies, knowledge capture, PSM documentation) that convert to retainers.
- Market: SWLA first, then Lafayette and Baton Rouge in Year 2.

## Key decisions and plans

- Private AI is the founder's primary focus (Oct 18, 2026).
- Plan: solo in Year 1.
- Plan: raise outside capital ($400K planned).
- Plan: a "decent salary" within 3 years.
- Use existing open-weight models; no own model training.
- Industrial services are part of the same business (Oct 18). The later hosting stages are too, under one brand (plan rule).
- The VA CUE Engine is parked (Oct 19) and not part of Private AI.

## Hard rules for any writing or work

1. **No confidential client data.** TWK appears only as a named reference client with the facts in the source.
2. **§7216 pitch guardrail.** Say "dramatically simplifies consent," never "no consent needed," until a tax-practice attorney signs off.
3. **Never touch a plant's OT network.** Industrial data arrives only as exports.
4. **Clients buy the hardware.** The company never carries inventory.
5. **The model is a configuration setting.** U.S.-origin model for federal, DoD-linked, LNG and critical-infrastructure clients.
6. **Every deliverable is "draft for qualified review."** Never promise regulatory outcomes.
7. **No hire before the hiring triggers are met.** MRR of about $20–25K is mandatory, plus one other signal (see file 14).
8. **Keep labels.** Keep [Estimate] and [To verify]; keep figures exactly as given; mark decisions vs recommendations; write TODO for missing facts.
9. **Don't browse the web unless asked.** Log outside-confirmation items in [12-open-questions.md](12-open-questions.md).

## Canonical figures (base case)

|                  | Year 1 | Year 2 | Year 3  |
| ---------------- | ------ | ------ | ------- |
| Clients (ending) | 4      | 11     | 19–20   |
| Revenue          | ~$155K | ~$465K | ~$860K  |
| Gross margin     | ~66%   | ~68%   | ~69%    |
| Operating result | ~−$95K | ~+$15K | ~+$155K |

Capital need ~$375K (base); raise $400K. The early-brief figures (~$160K/$455K/$800K; $350–500K raise) are superseded.

## Current status (2026-10-19)

- TWK is the planned first paying client, but no TWK work as of Oct 8 and no signed SOW recorded.
- SAM.gov and/or VetCert applications are submitted and pending.
- The legal entity and name are undecided (REGROUP, LLC or a new LLC).
- The §7216 attorney opinion is not yet obtained.

## Resolved Oct 20, 2026

1. **Decision:** TWK runs hybrid. Firm-only knowledge goes on Glass (cloud) and client data on the appliance.
2. **Hiring revised:** the first W-2 hire is expected in months 15–24, with MRR of about $20–25K mandatory plus one other signal, and a contract engineer before then. The second hire is expected in months 28–32.
3. **Industrial revised:** Year-1 base is $35–60K, not $150–250K. The first plant PO is expected in months 7–12.
4. **Decision: calendar.** Installs avoid only active named-storm watches (prefer May–July and November–December for CPA installs). Setup is billed 50% at signing and 50% at acceptance.
5. **Decision: gates and kill rule.** Gates at months 6, 9 and 12 count signed professional-firm contracts (1, 2 and 3 beyond TWK) and all-track MRR ($5K, $9K and $14K). The month-12 kill rule counts signed CPA/law contracts, not industrial retainers.
6. **Regenerated 3-year model** ([model/private-ai-3yr-model-2026-10-20.xlsx](model/private-ai-3yr-model-2026-10-20.xlsx)).
   - Base: revenue ~$190K / $507K / $898K; operating result −$66K / +$78K / +$217K; breakeven at month 18; capital need ~$220K.
   - Every scenario needs ~$75–85K of founder capital or bridge before the raise closes in month 5.

Details: [14-revised-plan-2026-10-20.md](14-revised-plan-2026-10-20.md). Where it conflicts with files 01–13, file 14 wins.

## Unresolved, most important first

1. Size founder capital or an early partial close for the ~$75–85K needed before month 5.
2. Karbon data classification under the hybrid split.
3. Price-test contractor compliance retainers.

Full list: [12-open-questions.md](12-open-questions.md).

## Where to look

| Need                                 | File                                                           |
| ------------------------------------ | -------------------------------------------------------------- |
| One-page overview and index          | [REPORT.md](REPORT.md)                                         |
| Idea, founder, positioning           | [01-business-overview.md](01-business-overview.md)             |
| Pricing logic, unit economics        | [02-business-model.md](02-business-model.md)                   |
| Every offer and price                | [03-products-and-services.md](03-products-and-services.md)     |
| Market, targets, competition         | [04-market-and-clients.md](04-market-and-clients.md)           |
| Sales tracks and process             | [05-go-to-market.md](05-go-to-market.md)                       |
| Appliance and integrations           | [06-technical-architecture.md](06-technical-architecture.md)   |
| §7216, ABA 512, PSM, contracts       | [07-compliance-and-legal.md](07-compliance-and-legal.md)       |
| Phases, hiring, metrics              | [08-implementation-roadmap.md](08-implementation-roadmap.md)   |
| Financials and raise                 | [09-financials-and-funding.md](09-financials-and-funding.md)   |
| Risks and kill rules                 | [10-risks-and-kill-criteria.md](10-risks-and-kill-criteria.md) |
| TWK, RAG platform, SDVOSB, entity    | [11-related-workstreams.md](11-related-workstreams.md)         |
| Decisions, to-verify, contradictions | [12-open-questions.md](12-open-questions.md)                   |
| Provenance                           | [13-sources.md](13-sources.md)                                 |
| Revised plan (Oct 20)                | [14-revised-plan-2026-10-20.md](14-revised-plan-2026-10-20.md) |
| Terms                                | [glossary.md](glossary.md)                                     |
