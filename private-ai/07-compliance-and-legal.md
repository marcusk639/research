# 07 — Compliance and Legal

> As of 2026-10-19. Labels: see [REPORT.md](REPORT.md#labels-used). This file summarizes positions in the source material. It is not legal advice; attorney review items are marked.

**Summary.** Compliance is the reason clients buy: IRC §7216 for tax preparers, ABA Formal Opinion 512 for lawyers, and OSHA PSM / EPA RMP for plants. The on-prem appliance arguably avoids a §7216 disclosure to an AI provider, but the founder's admin access is the weak point, so no marketing claim relies on it until a tax attorney signs off. Contracts, insurance and a model-origin policy round out the package.

## CPA / tax

### Penalties

| Statute   | Type     | Penalty                                                     |
| --------- | -------- | ----------------------------------------------------------- |
| IRC §7216 | Criminal | Up to a $1,000 fine and/or one year in prison per violation |
| IRC §6713 | Civil    | $250 per disclosure, up to $10,000 a year                   |

### IRS OPR Alert 2026-19 (June 24, 2026)

It maps Circular 230 duties onto AI:

- §10.22 due diligence applies.
- Every AI citation and calculation must be verified.
- §§6713/7216 data goes only into secure, enterprise-approved systems.
- Specific signed consent is generally required before sharing §7216 data with an AI tool.
- It doesn't require telling clients that AI was used.

No IRS guidance yet classifies AI under the §7216 exceptions (as of July 2026) [To verify that this is still true as of 2026-10-19].

### Consent requirements

- Treas. Reg. §301.7216-3 says consent must be knowing, voluntary, written and obtained beforehand.
- Individual returns use the Rev. Proc. 2013-14 format.
- The AICPA publishes sample forms.

**Practitioner view:** the §7216 disclosure happens when data leaves the preparer's control, regardless of whether the vendor retains it (Tom Gorczynski, Tom Talks Taxes).

### The on-prem argument

- Firm-owned hardware with no model vendor arguably means no disclosure to an AI provider.
- That would avoid naming OpenAI or Microsoft, and avoid collecting ~534 consent forms at TWK.
- **The weak point is the founder's admin access.**

**Mitigations:**

- IT-maintenance confidentiality agreement;
- platform-only access, not content;
- break-glass logging;
- client-held keys;
- documented in the firm's WISP;
- a tax-attorney opinion before any marketing claim.

**Recommendation (CPA research):** decide the §7216 basis, defaulting to consent, with a counsel-drafted form and a consent register.

**Plan:** §7216 consent templates are provided to every CPA client regardless of the opinion. This sits in tension with the on-prem argument's goal of avoiding consent collection; see [12-open-questions.md](12-open-questions.md#contradictions-found).

### Pitch guardrail

- Whether on-prem removes the §7216 consent requirement is a legal interpretation, not settled guidance.
- Marketing says "dramatically simplifies consent," never "no consent needed," until a tax-practice attorney signs off.
- The founder's admin access must be structured as IT maintenance under a confidentiality agreement.

### FTC Safeguards Rule and AICPA

- **FTC Safeguards Rule (16 CFR Part 314):** preparers need a written information security program (WISP) and must oversee service providers. The WISP addendum is a sellable, recurring artifact.
- **AICPA Code 1.700.001** on confidentiality also applies.

## Law

- **ABA Formal Opinion 512 (July 2024):** informed client consent is needed before client information goes into a self-learning generative AI tool, and boilerplate isn't enough.
  - The one-page overview phrases this as "third-party AI." The opinion's wording here is "self-learning generative AI tool." See [12-open-questions.md](12-open-questions.md#contradictions-found).
- **Louisiana:** the Supreme Court sent a letter on Jan 22, 2024. The LSBA has issued no formal AI opinion (as of September 2026) [To verify as of 2026-10-19].
- **Oregon Formal Opinion 2025-205:** closed models inherently give greater confidentiality protection, but that alone doesn't settle the question.
- **Kit:** AI use policy, vendor due-diligence file, verification and incident logs, client communication language.

## Industrial

- **Rules:** OSHA PSM (29 CFR 1910.119) and EPA RMP.
  - An RMP rollback was proposed Feb 24, 2026, with a final rule expected late 2026.
  - PSM is unchanged.
- **Deliverables are always "draft for qualified review."** The MSA states that the client's PSM process owns approval.
- **Never promise regulatory outcomes.**

## Contracts

The Master Services Agreement, SOW and Data Processing Addendum are drafted with a Louisiana business attorney.

| Term               | Position                                                                                |
| ------------------ | --------------------------------------------------------------------------------------- |
| Ownership          | The client owns the hardware and data; the company owns the platform IP and licenses it |
| Liability          | Capped at 12 months of fees, with carve-outs up to insurance limits                     |
| Training           | No training on client data                                                              |
| Deletion           | Within 30 days of termination                                                           |
| Breach notice      | 72 hours                                                                                |
| Models             | Model-origin disclosure and a swap clause                                               |
| Term               | 12 months, auto-renewing, 5% annual escalator                                           |
| Industrial payment | 50% on start, 50% on acceptance                                                         |
| Setup payment      | 50% at signing, 50% at acceptance (decision, Oct 20, 2026)                              |

## Insurance

Bound before the first client conversation.

| Coverage              | Limit                                          |
| --------------------- | ---------------------------------------------- |
| General liability     | $1M/$2M                                        |
| Tech E&O              | $1M                                            |
| Cyber                 | $1M                                            |
| Workers' compensation | Gate policies require it even for a sole owner |
| Auto                  | TODO: limit not given                          |

- Budget $6–10K in Year 1.
- Large plant MSAs may require $2–5M limits, so keep umbrella coverage available.

## Company security

The company keeps its own WISP and uses:

- MFA everywhere;
- EDR;
- encrypted devices;
- no client data on founder devices;
- client-held encryption keys;
- an annual review of each client's model and license.

## Model-origin policy

Chinese-origin models (Qwen, DeepSeek, Kimi) face pending U.S. scrutiny: the FIREWALL Act, NDAA provisions, and House committee proposals.

- **Default to a U.S.-origin model** for federal, DoD-linked, LNG and critical-infrastructure clients.
- **Review quarterly.**
- **Switch affected clients within 30 days** under the swap clause.

The source doesn't say whether every chemical plant counts as "critical infrastructure." If they all do, the Qwen default applies only to professional firms. TODO: confirm. See [12-open-questions.md](12-open-questions.md#gaps).

## Regulatory watch list

- IRS guidance on §7216 and AI.
- The final EPA RMP rule.
- Any LSBA formal AI opinion.
- Federal procurement restrictions on Chinese-origin models.

Compliance deliverable timing (opinion, templates, kits, contracts) is in [08-implementation-roadmap.md](08-implementation-roadmap.md#compliance-workstream-timing).
