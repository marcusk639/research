# 06 — Technical Architecture

> As of 2026-10-19. Labels: see [REPORT.md](REPORT.md#labels-used).

**Summary.** Each client gets one appliance, built from a single scripted image of mostly open-source or source-available parts, serving an open-weight model on a 96GB GPU in the client's building. Retrieval respects Microsoft 365 permissions, and every answer cites its source or says the answer isn't there. The client owns the box and the keys; the company has application-level access only, and nothing ever touches a plant's OT network.

## Operating rules

1. Clients buy the hardware.
2. The model is a configuration setting, never an architecture decision.
3. Nothing touches a plant's OT network, ever. Industrial data arrives only as exports: SAP/Maximo work-order extracts, PI historian reports, PDF procedures.
4. No hire before the trigger is met.
5. Every deliverable is marked "draft for qualified review."

## Appliance stack

The appliance is built from a single scripted image.

| Component                           | Choice                                                                         | License note                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| OS and runtime                      | Ubuntu LTS, Docker Compose                                                     | Open                                                                                                   |
| Model serving                       | vLLM (OpenAI-compatible API); Ollama for development and the small-office tier | Apache 2.0                                                                                             |
| Default model                       | Qwen3.8-27B (FP8 weights ~31 GB)                                               | Apache 2.0                                                                                             |
| U.S.-origin alternative, pre-staged | Gemma 4 31B or gpt-oss-120b (Apache 2.0); Mistral Small 4 as an EU option      | Default for federal, DoD-linked, LNG and critical-infrastructure clients                               |
| Embeddings and reranker             | Local open-weight models, benchmarked on the evaluation set                    | Never a cloud embedding API                                                                            |
| Document parsing                    | Docling or Unstructured                                                        | MIT / Apache 2.0; OCR quality decides answer quality                                                   |
| Vector and metadata store           | Postgres + pgvector (Qdrant if scale demands)                                  | PostgreSQL License                                                                                     |
| Chat interface                      | Open WebUI with branding kept, later the company's own front end               | Branding can't be removed above 50 users without a license                                             |
| Workflow automation                 | n8n on each client's own instance, or an Apache-licensed alternative           | Sustainable Use License: never host one n8n for multiple clients; confirm with n8n before productizing |
| Remote access                       | WireGuard or Tailscale/Headscale                                               | No inbound ports                                                                                       |
| Monitoring                          | Prometheus and Grafana, unmodified                                             | Don't modify and expose Grafana as a service                                                           |
| Backups                             | restic to U.S. object storage, client-held keys                                | Nightly; restore tested quarterly                                                                      |

Open items, all tracked in [12-open-questions.md](12-open-questions.md):

- Gemma 4's license [To verify]. The source's "(Apache 2.0)" may apply only to gpt-oss-120b.
- How gpt-oss-120b fits on one 96GB GPU, and how much context it leaves. The source doesn't say.
- n8n resale terms [To verify].
- Embedding and reranker benchmarks [To verify].

Model-origin policy: [07-compliance-and-legal.md](07-compliance-and-legal.md#model-origin-policy).

## Design decisions

- **One GPU per office.** One 96GB GPU (RTX Pro 6000 Blackwell class) serves an office.
  - A 27B model in FP8 leaves 50–60 GB for context, enough for 10–50 users.
  - The small-office tier uses a DGX Spark-class box for under 10 users.
- **Permission-aware retrieval is non-negotiable.** SharePoint and file permissions are stored with every chunk and filtered at query time.
- **Citations on every answer.** When the answer isn't in the documents, the system says so.
- **Client IT owns the box.** The client holds the admin credentials, encryption keys and physical server. The company has application-level access only, through a private tunnel.

## Hurricane posture

- Nightly encrypted backups.
- A shutdown runbook on storm watch.
- Optional temporary failover to a rented U.S. cloud GPU, only with written client approval, because it changes the data-location claim.

**Note on the "never leaves your building" claim.** Three parts of the design move data or access off-site:

- nightly backups to U.S. object storage (encrypted, client-held keys);
- remote application access through a private tunnel;
- optional cloud failover.

Sales language ("data never leaves your plant", "it never leaves your building") should be qualified to match. Tracked in [12-open-questions.md](12-open-questions.md#contradictions-found).

## Microsoft 365 integration

- Entra ID SSO.
- Graph connectors for SharePoint and OneDrive, using Sites.Selected permissions.
- Permission-aware retrieval.
- A sideloaded Outlook add-in for drafting replies.

[To verify] Microsoft Graph scopes and Outlook add-in sideloading.

## Integrations by vertical

| Vertical   | Integrations                                                                                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CPA        | Microsoft 365; QuickBooks Online API (open); file-based ingestion from CCH Axcess, UltraTax and Drake exports (their APIs are closed); Karbon or Canopy where used |
| Law        | Microsoft 365; Clio API (open); NetDocuments and iManage, via partner programs or exports                                                                          |
| Industrial | Exports only                                                                                                                                                       |

## Build order

1. Image and runbooks.
2. Evaluation harness.
3. Microsoft 365 connector with permissions.
4. The three CPA workflows.
5. Outlook add-in.
6. The company's own front end.

The Phase 1 schedule puts "install image and runbooks v1" in weeks 8–12, after the workflows. See [08-implementation-roadmap.md](08-implementation-roadmap.md#phase-1-product-and-reference-client) and [12-open-questions.md](12-open-questions.md#contradictions-found).

## Evaluation set

- 50 real questions with known answers from TWK's documents.
- Nothing ships that scores lower than the last version.

## Security answer pack

Needed before the first plant or large-firm conversation:

- network diagram and access model;
- encryption at rest and in transit;
- backup and restore design;
- logging and retention;
- incident response plan;
- subcontractor list (none);
- insurance certificates;
- a one-page data-flow statement.

## The founder's RAG platform (the engine under everything)

**Status:**

- Already built.
- Designed generically for any business, not only CPA firms.
- Currently backs a knowledge-base Q&A bot with source citations, plus a Microsoft Teams integration.
- He also wants to sell it as plug-and-play knowledge bases to other businesses. See [11-related-workstreams.md](11-related-workstreams.md#rag-platform-as-a-product).

**Ingestion design for TWK's SharePoint knowledge base** (§7216-aware, meant to hold firm-only data):

- path allowlist;
- detectors and a quarantine workflow;
- redaction;
- evaluation harness;
- audit schema.

**Open items:**

- TWK's Microsoft 365 license tier, which decides Microsoft Purview versus self-hosted Presidio for detection;
- path allowlist confirmation;
- who has quarantine review authority.

**Multi-tenant design notes** (from the Glass guide):

- PostgreSQL with tenant_id;
- per-tenant Entra configuration;
- SOC 2-style controls before resale;
- don't build billing yet.
