---
name: va-rating-math
description: Deterministically compute the VA combined disability rating (38 CFR 4.25 "whole person" math, plus the 4.26 bilateral factor) for a given set of individual condition ratings. Use whenever a rating changes or a new condition is added and you need the current combined percentage and monthly compensation, or when asked "what's my combined rating now", "recompute the VA math", or to check whether a claimed combined percentage is arithmetically correct.
disable-model-invocation: true
---

# VA Rating Math

Compute 38 CFR 4.25 combined ratings deterministically, so the number is derived the same
way every time rather than hand-calculated fresh (and potentially inconsistently) in each
strategy document. This is arithmetic, not research — no web search needed unless
compensation-rate dollar figures are also requested (see step 4).

## When to use this

Any time a rating changes, a new condition is added or resolved, or a document asserts a
combined percentage — recompute it here rather than trusting the asserted number. Several
of this claim's own documents (`100-PERCENT-SCHEDULAR-PATHWAY.md` §7,
`CLAIM-EXECUTION-PLAN.md` Phase 0) have hand-derived this math independently; use this
skill to keep future derivations consistent with those, and flag if a past one turns out
to be wrong.

## The algorithm (38 CFR 4.25)

Disabilities do **not** add. VA uses "whole person theory" — remaining, not gross, capacity.

1. **Rank every individual rating highest to lowest.**
2. **Apply the bilateral factor first, if applicable** (see below) — this changes the
   inputs to the combining step, not something layered on after.
3. **Combine sequentially:** start with the highest rating as the "already-disabled"
   percentage. For each next rating (in descending order), the person has
   `(100 - already-disabled)` percent of "remaining efficiency" left. The next rating
   applies to that remaining efficiency, not to the full 100:

   ```
   combined = already_disabled + (next_rating / 100) × (100 - already_disabled)
   ```

   Repeat for every rating in the list, carrying the running combined value (unrounded)
   into the next step each time.

4. **Round only once, at the very end** — standard rounding (down for 1-4, up for 5-9) to
   the nearest 10. Never round intermediate steps.

### Worked example

Ratings: 70, 50, 20, 10 (already sorted).

- Start: 70.
- Add 50: 70 + 0.50 × (100 − 70) = 70 + 15 = 85.
- Add 20: 85 + 0.20 × (100 − 85) = 85 + 3 = 88.
- Add 10: 88 + 0.10 × (100 − 88) = 88 + 1.2 = 89.2.
- Round: 89.2 → take the ones digit of the whole-number part (89 → ones digit **9** → 5-9
  rounds up) → **90%**. **Always double-check against the official VA combined-ratings
  table for values near a rounding boundary rather than trusting pure arithmetic** — VA
  publishes an explicit lookup table, and boundary cases should be confirmed against it,
  not re-derived from the formula alone.

## Bilateral factor (38 CFR 4.26)

Applies **only** when two or more disabilities affect **paired extremities** (both arms,
both legs — e.g., both ankles, or an ankle plus a secondary knee on the _other_ leg).

1. Combine the paired ratings with each other first, using the normal combining step above.
2. Add **10% of that combined paired value** to itself (i.e. multiply by 1.10).
3. Use that adjusted figure as a single input into the main combining sequence with all
   other (non-paired) ratings.
4. **Favorable-to-veteran exception:** if combining the paired disabilities _without_ the
   bilateral rule (i.e., just folding each into the main sequence individually) produces a
   _higher_ combined result, use that instead — the bilateral factor is a floor benefit,
   never a penalty.

A single condition in one limb only (e.g., one ankle, nothing rated on the other leg) gets
**no** bilateral factor.

## Steps to run this

1. **Get the current list of individual ratings** from the latest `COMPREHENSIVE-FINDINGS-*.md`
   or by asking directly — don't assume a document's stated list is current; conditions
   change status (pending → granted → increased) over time.
2. **Identify any paired-extremity ratings** and apply the bilateral factor first if
   applicable.
3. **Run the sequential combining algorithm** above, showing each step's running total
   (unrounded) so the arithmetic is auditable, not just the final answer.
4. **Round once, at the end.** State the combined percentage.
5. **If compensation dollar amounts are also wanted:** don't reason from training data —
   confirm the current effective-year rate table via `va.gov` (rates adjust annually via
   COLA), then multiply. Cite the effective date.
6. **Cross-check against any percentage already asserted** in the corpus for the same
   condition set — if it disagrees, flag the discrepancy rather than silently overwriting
   it, and show your work so it's easy to see which one has the arithmetic error.

## Guardrails

- Never present a combined percentage without showing the sequential steps — the whole
  point is auditability, not just a number.
- Never guess at a rounding-boundary case — when a computed value lands within ~0.5 of a
  10% boundary, cross-check against VA's published combined-ratings table rather than
  trusting the formula's rounding alone.
- Compensation dollar figures are annual (COLA-adjusted) — always confirm the effective
  year via a current source before quoting a monthly amount.
- This is arithmetic assistance, not legal advice — the underlying individual ratings
  still need to be correct and current for the combined math to mean anything.
