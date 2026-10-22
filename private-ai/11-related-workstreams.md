# 11 — Related Workstreams

> As of 2026-10-19. Labels: see [REPORT.md](REPORT.md#labels-used).

**Summary.** Several workstreams sit under or next to Private AI: the TWK reference client, the RAG platform, a fractional CTO practice, McNeese as a client, the SDVOSB/federal track, and company formation. The industrial corridor services and shared hosting are part of the same business. The VA Effective-Date & CUE Engine is parked and is not part of Private AI.

## TWK reference client

### History

| Date         | Event                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------- |
| Aug 1, 2026  | Started as technology and operations consultant                                             |
| Oct 8, 2026  | Doing no TWK work                                                                           |
| Oct 16, 2026 | Committed to help Chris reduce the firm's dependence on him; "Glass for TWK" design written |

TODO: whether the Aug 1 consulting role was paid, and the terms of the planned SOW, are not in the source.

### Earlier TWK work

- Workflow and process audit.
- A Karbon + "Hermes" AI automation architecture plan.
- A verified Excel ROI model (TWK_ROI_Model.xlsx).
- Analysis of Chris's 2025 time-and-expense journal (20K+ hours, ~31% non-billable).
- A "Building Power BI Dashboards from Karbon Data" guide.

**Baseline gap:** TWK doesn't track most baseline metrics (hours per task, rework, turnaround, realization). Establishing tracking is part of the work.

TWK already has Microsoft 365 Copilot.

### "Glass for TWK" design (Oct 16, 2026)

- Claude (Team first, Enterprise before any client data), plus one TWK-owned remote MCP server ("twk-context").
- The server wraps:
  - the firm knowledge base (from the RAG platform);
  - the Karbon API v3;
  - Karbon's Practice Intelligence Snowflake reader;
  - with audit logging.
- Copilot is kept for in-app Office and Teams work.
- About 12 reviewed firm skills.
- Cost: ~$800–2,900/month for 20 users.
- Client data is gated behind the WISP, a written §7216 position from counsel, consents, signed vendor terms and tested controls.
- Success targets: 80% weekly adoption within 60 days; 15–25% fewer hours on 3 workflows.

### Decision: hybrid deployment (Oct 20, 2026)

**Decision:** TWK uses a hybrid. Firm-only knowledge goes to the cloud (the Glass design). Client data stays on-prem (the appliance). This resolves the conflict between the business plan (on-prem) and the Glass design (cloud).

| Data class                                 | Examples                                                              | Where it runs                                                    |
| ------------------------------------------ | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Firm-only knowledge, no client identifiers | HR and IT answers, SOPs, templates, onboarding, firm policies         | Glass: Claude (Team, then Enterprise) + "twk-context" MCP server |
| Client data (§7216 / Safeguards scope)     | Returns, source documents, workpapers, notices, client correspondence | On-prem appliance at TWK                                         |

Analysis of what follows from the decision (not stated in the source):

- **It matches the CPA research staging.** Stage 1 (firm knowledge, no client identifiers) can run on Glass. Stage 2 (client documents, after consent) runs on the appliance. See [03](03-products-and-services.md#candidate-roadmap-from-rag-applications-for-a-mid-sized-cpa-firm).
- **The ingestion design becomes the boundary control.** The path allowlist, detectors, quarantine and redaction decide what may go to the cloud side. Who has quarantine review authority is now a blocking question, not a nice-to-have.
- **Karbon needs a ruling.** The Glass server reads the Karbon API and Practice Intelligence, which hold client names and work items. TODO: decide whether Karbon data counts as client data under this split. If it does, that connector moves on-prem or stays gated.
- **The pitch needs one qualifier at TWK.** "Client data never goes to an outside AI provider" stays true. "No data goes to an outside AI provider" does not, because firm knowledge goes to Anthropic.
- **Sequencing option.** Glass needs no hardware, so firm-knowledge value could start before the appliance arrives. The 90-day gate still calls for the appliance pilot. TODO: confirm whether the TWK pilot starts on Glass or on the appliance.

**Long-term vision:** TWK as a sandbox, then resell to other CPA firms and serve Chris's small-business clients.

## RAG platform as a product

- Plug-and-play knowledge bases for businesses beyond CPA firms.
- It is the engine under the appliance.

Architecture and status: [06-technical-architecture.md](06-technical-architecture.md#the-founders-rag-platform-the-engine-under-everything).

## Fractional CTO practice and paid assessments

- Go-to-market materials, a 90-day launch plan, and a templatized paid assessment scope.
- McNeese as a vendor-route client:
  - LaVet certification;
  - CIO-first outreach;
  - a sub-$15K SOW on Ellucian Banner and institutional-research workflows.
- It is also the plan's pivot path under the kill criteria. See [10-risks-and-kill-criteria.md](10-risks-and-kill-criteria.md#kill-and-pivot-criteria).

## Industrial corridor services

Part of the same business, per the Oct 18 decision. See [03-products-and-services.md](03-products-and-services.md#industrial-services) and [05-go-to-market.md](05-go-to-market.md#industrial-door-opening).

## Shared hosting / local data center

The last stage of the same business. See [08-implementation-roadmap.md](08-implementation-roadmap.md#deployment-stages).

## SDVOSB and federal/VA track (secondary)

| Item                | Detail                                                               |
| ------------------- | -------------------------------------------------------------------- |
| Status              | SAM.gov and/or VetCert applications submitted and pending (Oct 2026) |
| NAICS               | 541511, 541512, 541519, 541611, 541990, 518210                       |
| Vehicles researched | VETS 2, Polaris, OASIS+, GSA Schedule, T4NG2                         |
| Approach            | Start as a subcontractor; VA first, then civilian agencies           |
| Fit                 | On-prem, U.S.-origin-model AI suits this track                       |
| Plan target         | The 36-month plan includes one federal or VA contract                |

TODO:

- Which legal entity the SAM.gov/VetCert applications were filed under (the entity decision is still pending).
- The SDVOSB eligibility basis. See [12-open-questions.md](12-open-questions.md#gaps).

## VA Effective-Date & CUE Engine (parked; not part of Private AI)

A software idea for VA-accredited reps, parked per a validation memo on Oct 19, 2026:

- expected Year-3 ARR ~$238K if built;
- a new rival (VBMS Reviewer, $60–79 per file);
- **Recommendation:** keep Private AI as the primary focus.

It could later be licensed, or used in an accredited claims-agent practice.

## Company formation and brand

- **Earlier top name pick:** Klein Technology Group LLC, marketed as veteran-owned, with a contractor one-pager and a consulting launch plan.
- **Now:** he wants a better name and is drawn to a "rebirth" theme.
- **Existing entity:** he owns a Louisiana LLC, REGROUP, LLC (formerly Phoenix Recovery Solutions LLC), through which he verified a Google Cloud account.
- **Decision pending:** use REGROUP, LLC or form a new LLC for this business.
- **SDVOSB rule:** the veteran must own at least 51% and control the company. This is compatible with the equity plan's "founder above 75%."
- **Louisiana formation:** runs through geauxBIZ (~$105; name reservation $25 for 120 days).
