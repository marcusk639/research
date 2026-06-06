---
name: source-capture
description: Fetch a web URL and save it as cleaned, citable Markdown into the current research subject directory. Use when the user shares a source URL to archive, says "capture this source", "save this page", or wants a web page preserved for citation.
---

# source-capture

Turn a web source into a local, citable Markdown artifact inside a research subject
directory, so claims in a report can be traced to preserved sources.

## Steps

1. **Determine the target subject.** Identify which subject directory the source
   belongs to (ask if unclear). All captured sources live under
   `<subject>/sources/`.

2. **Fetch and clean.** Retrieve the URL as Markdown. Prefer, in order:
   - `firecrawl-scrape` (or `mcp__firecrawl__firecrawl_scrape`)
   - the `web-to-markdown` skill
   - `WebFetch` as a fallback

3. **Write the artifact** to `<subject>/sources/<slug>.md`, where `<slug>` is a
   kebab-case version of the page title. Prepend a citation header:

   ```markdown
   ---
   source_url: <original URL>
   captured: <today's date>
   title: <page title>
   ---

   <cleaned Markdown content>
   ```

4. **Report the local path** so it can be cited from the subject's `REPORT.md`.

## Constraints

- Never save sources outside the owning subject's `sources/` directory.
- Preserve the original `source_url` in every captured file — citations depend on it.
- Don't summarize or alter the source content during capture; capture verbatim
  (cleaned of boilerplate). Synthesis happens in `REPORT.md`, not here.
