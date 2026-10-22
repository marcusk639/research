# 02 — Business Model

> As of 2026-10-19. Labels: see [REPORT.md](REPORT.md#labels-used).

**Summary.** It's priced as a compliance-driven managed service with a monthly minimum, at an effective $125–175 per user per month. Subscriptions carry the business, setup fees fund the first year, and workflows and industrial projects lift margin. Gross margin runs about 66–69% because the client owns the inference hardware.

## How it makes money

- **Subscriptions carry the business.**
- **Setup fees fund the first year.**
- **Workflows and industrial projects lift margin.**

## Pricing position

- It sits between commodity Copilot ($21 per user) and premium legal AI ($225–650 per user per month).
- Effective pricing is $125–175 per user per month.
- Anchor: a 20-person professional firm already spends about $2,200–3,700/month on managed IT, at $110–170 per user. That anchors what an AI subscription can cost.

The legal-AI figure and the managed-IT range differ slightly from the competition table; see [12-open-questions.md](12-open-questions.md#contradictions-found).

Prices for every offer: [03-products-and-services.md](03-products-and-services.md).

## Gross margin

|              | Year 1 | Year 2 | Year 3 |
| ------------ | ------ | ------ | ------ |
| Gross margin | ~66%   | ~68%   | ~69%   |

This is in line with niche MSPs (65–70%). It is above AI-product averages (~52%) because the client owns the inference hardware.

Target margin by line (Year 1 metrics): subscription 70%, setup 55%, industrial 60%+.

## Unit economics: one Professional client, at list prices

| Line                                         | Year 1            | Years 2–3 (per year)   | Gross margin |
| -------------------------------------------- | ----------------- | ---------------------- | ------------ |
| Setup fee                                    | $25,000           | —                      | 55%          |
| Subscription at $4,500/month                 | $54,000           | $56,700 (5% escalator) | 70%          |
| Workflow add-ons (1–2 after first quarter)   | $6,000            | $12,000                | 85%          |
| Hardware pass-through margin (8% on $28,000) | $2,240            | —                      | 100%         |
| **Total revenue**                            | **$87,240**       | **$68,700**            |              |
| **Gross profit**                             | **$54,000 (62%)** | **$49,900 (73%)**      |              |

**Flag: Year-1 gross profit mismatch.** The stated Year-1 gross profit ($54,000, 62%) doesn't match the line-item margins:

- $13,750 + $37,800 + $5,100 + $2,240 = $58,890.

The stated figure is kept here as given. Confirm it against the spreadsheet. Years 2–3 reconcile: $39,690 + $10,200 = $49,890 ≈ $49,900. Tracked in [12-open-questions.md](12-open-questions.md#contradictions-found).

## Lifetime value and acquisition cost

- **Three-year lifetime value:** about $190–225K of revenue and $135–160K of gross profit per client (realized versus list).
- **Customer acquisition cost:** about $5,000 (MSP benchmark ~$4,200, with a 7-month payback).

## Year-3 revenue mix target

Hardware margin is excluded.

| Line                          | Share |
| ----------------------------- | ----- |
| Subscriptions                 | 55%   |
| Setup and implementation      | 20%   |
| Workflows and compliance kits | 10%   |
| Industrial projects           | 15%   |

## Why margins hold

- Inference runs on client hardware.
- Installs come from a repeatable image (client #10 takes a day).
- Workflows are built once per vertical.
- Support is scoped (business hours, 4-hour P1 response). One person carries ~10 clients, and a first hire ~20.

## What compresses margin, and the rule for each

| Pressure                           | Rule                             |
| ---------------------------------- | -------------------------------- |
| Custom integrations priced too low | Quote integrations separately    |
| Unbilled on-site hours             | On-site time is in the setup fee |
| Hardware on the company's books    | Hardware is never inventory      |

## Contract terms

- 12-month term, auto-renewing.
- 5% annual escalator (the MSP norm is 5–8%).
- **Decision (Oct 20, 2026):** setup billed 50% at signing, 50% at acceptance ([14](14-revised-plan-2026-10-20.md#6-revised-gates-and-kill-criterion)).
- Hardware is a separate line the client pays for directly, or passed through at cost plus 8%. The company never carries inventory.

The contract framework (MSA, SOW, DPA) is in [07-compliance-and-legal.md](07-compliance-and-legal.md#contracts).
