# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repository holds **deep research tasks and their results**. It is a knowledge
repository, not a software project — there is no build, lint, or test step.

## Structure Convention

**Each top-level subdirectory is one research subject.** The directory name is the
subject slug (e.g. `va-disability/`). All research artifacts for a subject —
reports, source notes, data, drafts — live inside that subject's directory.

When starting research on a new subject:

- Create a new top-level directory named with a kebab-case slug for the subject.
- Keep everything for that subject self-contained within its directory.
- Do not scatter a subject's files across the repo root or other subjects.

Prefer the project skills over doing this by hand:

- `/new-subject <name>` — scaffolds `<slug>/REPORT.md`; refuses to clobber an existing subject.
- `/source-capture` — captures and files source material into the active subject.

## Conducting Research

Use the `deep-research` skill for substantive research tasks. It fans out web
searches, fetches sources, adversarially verifies claims, and synthesizes a cited
report. Before invoking it, confirm the question is specific enough; if it is
underspecified, ask 2–3 clarifying questions to narrow scope first.

Research output should be written as Markdown into the relevant subject directory.
Cite sources inline so claims are traceable. The primary synthesis for a subject lives at `<slug>/REPORT.md`.

## Session Memory (`.remember/`)

Each subject directory and the repo root contain a `.remember/` folder used by the
remember tooling for session handoffs and logs. The handoff target for the active
subject is written to `<subject>/.remember/remember.md`.

- `.remember/logs/` and `.remember/tmp/` are tooling state — do not edit by hand.
- Write session handoffs to the path the session-start hook reports, not elsewhere.
- A subject dir containing only `.remember/` (no `REPORT.md`) is hook state, not a real subject yet — safe to scaffold into.
