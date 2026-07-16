# Mock Rating Reports

Dated output of `/rate-claim` runs: `YYYY-MM-DD-rating-report.md`, one per run.
Reports are cumulative — never overwritten — so baseline → final runs can be
diffed as evidence is added to `supporting-docs/`.

Every report is a mock, records-only adjudication: **the score is conditional on
the actual C&P exam**, which this harness cannot substitute for. Reports are
research assistance, not legal or medical advice.

No reports exist yet: the first run requires explicit user authorization
(spec: Validation section — blind-rediscovery acceptance test gates trust in the
first score).

**PHI:** generated reports quote and cite the evidence record (names, clinical
detail, treatment history), so `*.md` reports here are gitignored — only this
README is tracked. Do not force-add a report to git.
