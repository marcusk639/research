# 01 — Business Overview

> As of 2026-10-19. Labels: **[Estimate]**, **[To verify]**, **Decision**, **Recommendation**, **TODO**. See [REPORT.md](REPORT.md#labels-used).

**Summary.** Private AI (working name) is a managed private-AI service for professional firms and industrial businesses in Southwest Louisiana. The client gets an AI assistant that runs on a server in their own building, answers from their own documents with citations, and never sends data to an outside AI provider. It wins on compliance, local in-person support and vertical workflows, starting with CPA firms and a reference client the founder's brother owns.

## The idea

- A managed private-AI service for professional firms and industrial businesses in Southwest Louisiana (SWLA).
- It expands along I-10 to Lafayette and Baton Rouge.
- **What clients get:** an AI assistant on a server in their own building. It:
  - answers from their own documents, with citations;
  - plugs into Microsoft 365;
  - never sends client data to an outside AI provider.

  See [06-technical-architecture.md](06-technical-architecture.md) for the limits on that last claim (backups, remote access, failover).

## Who pays, in order

1. CPA firms
2. Law firms
3. Plants and industrial contractors of the Lake Charles–Westlake–Sulphur corridor

## Why they buy

Compliance first, then productivity.

| Buyer         | Compliance driver                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tax preparers | Criminal exposure under IRC §7216 for disclosing client data to third parties. IRS OPR Alert 2026-19 (June 24, 2026) says client data belongs only in secure, enterprise-approved AI systems. |
| Lawyers       | Need informed consent before putting client information into third-party AI (ABA Formal Opinion 512).                                                                                         |
| Plants        | Won't let process data leave the fence.                                                                                                                                                       |

An appliance the client owns answers all three. Details: [07-compliance-and-legal.md](07-compliance-and-legal.md).

## Why now

- **Shadow AI is already here.** 74% of professionals use AI several times a week. 34% use tools their organization hasn't sanctioned (Thomson Reuters Future of Professionals 2026).
- **The regulator has spoken.** IRS OPR Alert 2026-19 (June 24, 2026) maps Circular 230 duties onto AI.
- **The corridor is building.** $64.4B of projects are under construction in SWLA. New LNG terminals must write procedures, train operators and qualify contractors from scratch.
- **Experienced workers are retiring.** Gulf Coast surveys put 34–40% of the petrochemical workforce over 50 or within a decade of retirement.

Full evidence: [04-market-and-clients.md](04-market-and-clients.md).

## Why this founder

| Item             | Fact                                                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Name             | Marcus Klein                                                                                                                             |
| Location         | Lake Charles, Louisiana (relocated from Austin, Texas). Married.                                                                         |
| Military         | U.S. Air Force veteran, F-15/tactical aircraft mechanic; 4-year enlistment, honorable discharge                                          |
| Engineering      | About 10 years as a senior/staff software engineer: Meta, MNTN, DISQO, American Tower, CGI, Kustomer. Last tech job ended June 30, 2026. |
| Training         | Describes himself as FedRAMP-trained                                                                                                     |
| Education        | Computer science background from McNeese State University (local alumni network)                                                         |
| Self-description | Highly adaptable, fast learner, extremely persistent, strong seller                                                                      |
| Local network    | Friends who work in the plants, and friends and family who know people higher up                                                         |

**Key relationship.**

- His brother Chris owns Terranova Williams Klein CPAs, LLC (TWK) in Lake Charles: about 534 clients and 15–25 staff.
- TWK is the planned first (reference) client, and Chris is an active referral partner.
- TWK also does Marcus's accounting.
- Related-party handling: see [12-open-questions.md](12-open-questions.md#gaps).

## Founder decisions and plans (Oct 18, 2026)

- **Decision:** Private AI is his primary focus.
- **Plan:** Stay solo in Year 1.
- **Plan:** Raise outside capital.
- **Plan:** Earn a "decent salary" within 3 years.
- **Decision:** Do not build or train his own models; use existing open-weight models.
- **Decision:** The industrial corridor services are part of the same business.

## Positioning

**Positioning statement:**

> "The only Southwest Louisiana provider that installs a private AI system in your building, documents it for your regulator, and answers the phone from Lake Charles."

"The only" provider is a claim to confirm before use [To verify]. The source says none of the local MSPs markets private AI ([04](04-market-and-clients.md#competition)).

**The sales pitch:**

> "Your staff are already pasting client data into ChatGPT. This gives them something better that lives in your building, cites the page every answer came from, and comes with the policy and documentation your regulator expects."

**Industrial positioning line** (from the corridor strategy):

> "I spent four years keeping fighter jets flying and ten years building software at Meta. I turn what your best people know into systems the next shift can use, and the data never leaves your plant."

[To verify] The line implies all ten engineering years were at Meta. They span several companies, so reword it before use.

**Pitch guardrails:**

- Whether an on-prem system removes the §7216 consent requirement is a legal interpretation, not settled guidance.
- Marketing says "dramatically simplifies consent," never "no consent needed," until a tax-practice attorney signs off.
- The founder's own admin access must be structured as IT maintenance under a confidentiality agreement.

## Why this company wins

- Local, in-person installation and support, including after hurricanes.
- A compliance package no national vendor ships.
- Microsoft 365 permission-aware retrieval.
- Named vertical workflows.
- Founder credibility: former Meta engineer, Air Force aircraft mechanic, McNeese alumnus.
- A reference client in the first vertical.

National appliance vendors sell boxes. SaaS vendors move data off-site. Neither shows up in Sulphur.

**Moat over time:**

- vertical workflow libraries;
- refined compliance templates;
- documented case studies;
- relationships inside plants that out-of-town vendors can't replicate.

## Long-term shape

The "local data center" idea is the last stage of the same business, not a separate venture:

1. appliances in client buildings (now);
2. a shared colocation rack (Years 2–3);
3. an own facility, only if Stage 2 fills.

One business, one brand ("private AI, local"). See [08-implementation-roadmap.md](08-implementation-roadmap.md#deployment-stages).
