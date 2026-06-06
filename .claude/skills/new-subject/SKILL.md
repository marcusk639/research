---
name: new-subject
description: Scaffold a new research subject directory with a report skeleton. Use when starting research on a new topic in this repo, or when the user says "new subject", "new research topic", or "set up research for X".
disable-model-invocation: true
---

# new-subject

Scaffold a new research subject in this repository. Each subject is a self-contained
top-level directory named with a kebab-case slug.

## Steps

1. **Derive the slug.** Take the subject the user names and convert it to kebab-case
   (lowercase, words joined by `-`, no punctuation). Example: "VA Disability Claims"
   → `va-disability-claims`. Confirm the slug with the user if it's ambiguous.

2. **Refuse to clobber.** If a directory with that slug already exists at the repo
   root, stop and tell the user — do not overwrite existing research.

3. **Create the directory and report skeleton** at `<slug>/REPORT.md`:

   ```markdown
   # <Subject Title>

   > Status: draft · Started: <date>

   ## Research Question

   <one or two sentences scoping exactly what is being investigated>

   ## Key Findings

   _Synthesis goes here once research is done._

   ## Sources

   _Cited inline above; full list maintained here._
   ```

   Fill `<Subject Title>` and `<date>` (today's date). Leave the body sections as
   placeholders.

4. **Scope check before researching.** If the research question is underspecified,
   ask 2–3 clarifying questions to narrow it before any web research begins.

5. **Point to the workflow.** Tell the user the subject is ready and that
   substantive research should run through the `deep-research` skill, writing cited
   Markdown into `<slug>/`.

## Constraints

- Everything for a subject stays inside its directory — never scatter files at the
  repo root or into other subjects.
- Do not start web research as part of scaffolding; this skill only sets up the
  structure.
