# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

`businesses/` is a research repository for **potential entrepreneurial business
ventures**. Each venture under investigation gets its own self-contained
subdirectory holding all of its research — market analysis, competitor teardowns,
business-model notes, sources, and a synthesized go/no-go report.

This is a knowledge repository, not a software project: no build, lint, or test
step. The output is cited Markdown, not code.

## Relationship to the parent repo

This directory lives inside the `research/` repo and inherits its conventions from
`../CLAUDE.md`. The parent's rules still apply here — **one subdirectory per
subject**, everything self-contained, `REPORT.md` as the primary synthesis, and the
`.remember/` session-memory layout. The difference is scope: here a "subject" is a
**business venture**, so each venture's report is written to evaluate, not just
describe.

## Structure Convention

- Each top-level subdirectory of `businesses/` is **one venture**, named with a
  kebab-case slug (e.g. `addiction-recovery/`, `bh-rcm-copilot/`).
- All artifacts for a venture stay inside its directory. Captured sources go in
  `<venture>/sources/`. Never scatter a venture's files across `businesses/` or into
  another venture.
- The primary synthesis for a venture is `<venture>/REPORT.md`.

## Workflow

Prefer the project skills over doing scaffolding or capture by hand:

- `/new-subject <venture name>` — scaffolds `<slug>/REPORT.md`; refuses to clobber an
  existing venture. Run from the `businesses/` directory so the venture lands here.
- `/source-capture` — fetches a URL and files it as cited Markdown into the active
  venture's `sources/`.
- `deep-research` skill — the workhorse for substantive investigation: fans out web
  searches, fetches and verifies sources, and synthesizes a cited report. Before
  invoking it, confirm the venture question is specific enough; if underspecified,
  ask 2–3 clarifying questions to narrow scope first.

## Venture REPORT.md orientation

The `new-subject` skill produces a generic report skeleton (Research Question / Key
Findings / Sources). For a venture, extend the body to support an investment-style
decision. Cover, at minimum:

- **Problem & customer** — who has the pain, how acute, how they solve it today.
- **Market** — size, growth, segments, and how those numbers were derived.
- **Competition** — direct and indirect players, their positioning and gaps.
- **Business model** — how it makes money, unit economics, pricing.
- **Risks & unknowns** — what would kill it; the riskiest unvalidated assumptions.
- **Verdict** — a clear go / no-go / needs-more-research call with rationale.

Cite sources inline so every market figure and competitor claim is traceable; keep
the full list in the report's Sources section.

## Session Memory (`.remember/`)

As in the parent repo, write session handoffs to the path the session-start hook
reports — do not edit `.remember/logs/` or `.remember/tmp/` by hand. A subdirectory
containing only `.remember/` (no `REPORT.md`) is hook state, not a real venture yet —
safe to scaffold into.
