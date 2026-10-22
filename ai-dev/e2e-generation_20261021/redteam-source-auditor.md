# Red-team — Source-Quality Auditor (persona 3), 2026-10-21

Independent verifier agent. Every quote was checked against the raw cache, with curl re-fetches where the cache was truncated. The regroup repo was re-checked at `3355a81`. A numeric script compared every number-bearing sentence with its cited sources.

**Verdicts:** R1 NARROW · R2 STANDS · R3 NARROW · R4 NARROW · R5 NARROW · R6 NARROW · R7 NARROW (near REFUTE) · R8 STANDS · R9 NARROW · R10 STANDS · R11 STANDS · R12 NARROW · R13 NARROW · R14 NARROW · R15 NARROW · R16 STANDS · R17 NARROW · R18 NARROW · R19 STANDS · R20 NARROW · R21 NARROW · R22 NARROW · R23 NARROW · R24 STANDS

**Numeric check:** one genuine miss: "best effort" / 0.72 is not in S13; the source's wording is "we do our best". The S156 figures were confirmed via `?m=1`. Six numbers are present in their source but misstated:

- S56: 32K→256K, not the 1M scale
- S148: o3 only
- S44: averages, not a ceiling (per-app specificity reaches 0.76)
- S62: a relative improvement
- S30: per class, "at least one" test
- S174: resolve gain misframed

**Citation defects (21), condensed:**

1. "best effort" put in quotation marks, attributed to S13 (fabricated quote)
2. The "self-contradictory" quote is in S151, not S31
3. "Meaningful identifiers" comes from S41, not S42
4. The intent mitigation should cite S42 only (S41 only speculates)
5. S56's scale is misstated
6. S174 misframed
7. S62 needs "relative"
8. S30 metric needs "at least one test per class"
9. S148 needs "o3"
10. S44 needs "average"
11. S171 merges two separate statements
12. "Industry name 'self greening'" rests on one community glossary (S130)
13. S163 omits "There are some internal benchmarks also"
14. Disputes is not the most-documented feature (chores has 100 vs 91)
15. `paywall` is client-read, not client-written
16. Drop S85 from the topic-mapping citation (only S86 has it)
17. "Silently" is not in S76
18. #3538's later evidence omitted (rerun-after-crash commits; fixed-port lifecycle)
19. S155 (unreliable tier) does primary work for a claim
20. Partial rows carry numbers (all re-verified; a process inconsistency only)
21. S55 should be marked as a vendor source

**Circularity:** none in the strict sense. Maestro's case leans heavily on mobile.dev's own material (S2, S8, S114, S115).
