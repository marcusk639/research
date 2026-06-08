---
name: new-subject
description: Scaffold a new research subject directory with a report skeleton. Use when starting research on a new topic in this repo, or when the user says "new subject", "new research topic", or "set up research for X".
disable-model-invocation: true
---

# new-subject

Scaffold a new research subject in this repository. Each subject is a self-contained
directory named with a kebab-case slug.

## Steps

1. **Determine the target location.** Subjects normally scaffold at the repo root.
   But when the current working directory is a nested research collection — one that
   groups subjects under a theme (e.g. `businesses/`, identifiable by its own
   `CLAUDE.md`) — scaffold the new subject **inside that directory**, not at the repo
   root. Default rule: create the subject under the current working directory. If
   that puts it somewhere unexpected, confirm the parent path with the user first.

2. **Derive the slug.** Take the subject the user names and convert it to kebab-case
   (lowercase, words joined by `-`, no punctuation). Example: "VA Disability Claims"
   → `va-disability-claims`. Confirm the slug with the user if it's ambiguous.

3. **Refuse to clobber.** If a directory with that slug already exists in the target
   location, stop and tell the user — do not overwrite existing research.

4. **Create the directory and report skeleton** at `<target>/<slug>/REPORT.md`,
   where `<target>` is the location chosen in step 1:

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

5. **Scope check before researching.** If the research question is underspecified,
   ask 2–3 clarifying questions to narrow it before any web research begins.

6. **Point to the workflow.** Tell the user the subject is ready and that
   substantive research should run through the `deep-research` skill, writing cited
   Markdown into `<slug>/`.

## Constraints

- Everything for a subject stays inside its directory — never scatter files into the
  parent location or into other subjects.
- Do not start web research as part of scaffolding; this skill only sets up the
  structure.
