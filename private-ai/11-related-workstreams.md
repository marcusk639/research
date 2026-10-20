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

**Top contradiction to resolve.** This business plan assumes an on-prem appliance at TWK. The Glass design is Claude-based, in the cloud. A hybrid would put firm-only knowledge in the cloud and client data on-prem. The two TWK documents assume different architectures. See [12-open-questions.md](12-open-questions.md#pending-decisions).

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
