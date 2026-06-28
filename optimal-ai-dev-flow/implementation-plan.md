# New AI Workflow — Executable Implementation Plan

**Strategy source:** `workflow-plan-v2.md`
**Status:** Ready to execute
**Session model:** Each phase is self-contained and can run in a fresh Claude Code context.
**Goal:** Institute 80/15/5 tier routing, Judge-Builder loop, real CI for recovery-platform, and OpenRouter Tier C infrastructure.

---

## Phase 0: Ground Truth (Completed — Reference Only)

**Sources consulted:**

- `/Users/marcus/dev/research/optimal-ai-dev-flow/v1.md` — benchmark analysis, subscription arbitrage
- `/Users/marcus/dev/research/optimal-ai-dev-flow/v2.md` — 80/15/5 rule, Judge-Builder loop, Hermes/OpenRouter stack
- Live repo audits: recovery-platform, rag-system, cpa-consulting

**Confirmed facts (do not re-derive):**

- recovery-platform: NO `ci.yml` exists — only `claude.yml` and `claude-code-review.yml`
- rag-system: real CI exists (`ci.yml` + `e2e.yml`) — no EMBEDDING_PROVIDER env var in e2e.yml
- cpa-consulting: no code, no tests, pure Markdown workspace
- All three repos have CLAUDE.md files — none have a Model Tier Policy block
- recovery-platform has Maestro flows at `e2e-maestro/` and `regroup/mobile/maestro/`
- OpenRouter NOT yet configured anywhere

**Known gaps (what's still needed):**

- OpenRouter API key (user action required — cannot be automated)
- Maestro Cloud API key (user action required for CI integration)
- The `EXECUTION_MODEL` and `TIER_C_MODEL` env vars don't exist yet

---

## Phase 1: Tier Policy — Add to All CLAUDE.md Files

**Estimated time:** 1 session (~30 minutes)
**Context to load:** `workflow-plan-v2.md` sections "Phase 1" and "80/15/5 Tier Policy"
**Repos touched:** recovery-platform, rag-system, cpa-consulting

### 1.1 — What to implement

Append the Model Tier Policy block to each CLAUDE.md. Copy the exact block from `workflow-plan-v2.md:Phase 1.1` — do not rewrite it.

**Files to edit:**

1. `/Users/marcus/dev/recovery-platform/CLAUDE.md` — append root tier policy + recovery-platform calibration (from Phase 1.2)
2. `/Users/marcus/dev/rag-system/CLAUDE.md` — append root tier policy + rag-system calibration (from Phase 1.2)
3. `/Users/marcus/dev/cpa-consulting/CLAUDE.md` — append root tier policy only (no product calibration needed)

**Do NOT edit:**

- Sub-product CLAUDE.md files (`homegroups/CLAUDE.md`, `regroup/CLAUDE.md`, etc.) — root policy cascades down
- `.claude/CLAUDE.md` files — those are tooling config, not agent context

### 1.2 — Verification checklist

- [ ] `grep -n "Model Tier Policy" ~/dev/recovery-platform/CLAUDE.md` returns a match
- [ ] `grep -n "Model Tier Policy" ~/dev/rag-system/CLAUDE.md` returns a match
- [ ] `grep -n "Model Tier Policy" ~/dev/cpa-consulting/CLAUDE.md` returns a match
- [ ] Each block contains "Tier A", "Tier B", "Tier C" headings
- [ ] recovery-platform block contains "Cross-product integration" under Tier A
- [ ] rag-system block contains "Auth provider changes" under Tier A

### 1.3 — Anti-pattern guards

- Do NOT remove existing CLAUDE.md content — append only
- Do NOT add tier policy to `.claude/CLAUDE.md` files (those are for tooling hooks, not model routing)
- Do NOT add product-specific calibrations to rag-system for recovery-platform tasks or vice versa

### 1.4 — Commit

```bash
cd ~/dev/recovery-platform && git add CLAUDE.md && git commit -m "chore(claude): add model tier policy (80/15/5 rule)"
cd ~/dev/rag-system && git add CLAUDE.md && git commit -m "chore(claude): add model tier policy (80/15/5 rule)"
cd ~/dev/cpa-consulting && git add CLAUDE.md && git commit -m "chore(claude): add model tier policy (80/15/5 rule)"
```

---

## Phase 2: OpenRouter Integration — Tier C Infrastructure

**Estimated time:** 1 hour (manual account setup + 15 min config)
**Human action required:** OpenRouter account creation and funding
**Context to load:** `workflow-plan-v2.md` sections "Phase 2"

### 2.1 — Manual steps (you must do these)

1. Go to `openrouter.ai` → create account → fund with $40
2. Generate API key → copy to clipboard
3. Run:

```bash
# Add to ~/.zshrc
echo 'export OPENROUTER_API_KEY="sk-or-PASTE_KEY_HERE"' >> ~/.zshrc
echo 'export TIER_C_MODEL="deepseek/deepseek-v4-flash"' >> ~/.zshrc
echo 'export TIER_B_MODEL="anthropic/claude-3.5-sonnet"' >> ~/.zshrc
source ~/.zshrc
```

4. Verify: `echo $OPENROUTER_API_KEY` should print the key (not empty)

### 2.2 — Add .env.local to each repo

**What to implement:** Create `.env.local` (already gitignored by default) in each repo root.

Verify gitignore first:

```bash
grep -n ".env.local" ~/dev/recovery-platform/.gitignore ~/dev/rag-system/.gitignore
```

If `.env.local` is NOT in .gitignore, add it before creating the file.

Then create each file:

```bash
# recovery-platform
cat > ~/dev/recovery-platform/.env.local << 'EOF'
OPENROUTER_API_KEY="${OPENROUTER_API_KEY}"
EXECUTION_MODEL="deepseek/deepseek-v4-flash"
PLANNING_MODEL="anthropic/claude-3.5-sonnet"
EOF

# rag-system
cat > ~/dev/rag-system/.env.local << 'EOF'
OPENROUTER_API_KEY="${OPENROUTER_API_KEY}"
EXECUTION_MODEL="deepseek/deepseek-v4-flash"
PLANNING_MODEL="anthropic/claude-3.5-sonnet"
EOF
```

### 2.3 — Test OpenRouter is working

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Reply with: OpenRouter Tier C working"}]
  }'
```

Expected: JSON response with `"content": "OpenRouter Tier C working"` (or similar)

### 2.4 — Verification checklist

- [ ] `echo $OPENROUTER_API_KEY` returns non-empty value in new terminal
- [ ] `echo $TIER_C_MODEL` returns `deepseek/deepseek-v4-flash`
- [ ] OpenRouter test curl returns a valid response
- [ ] `.env.local` exists in recovery-platform and rag-system
- [ ] `.env.local` is gitignored (not in `git status` output)

### 2.5 — Anti-pattern guards

- NEVER commit `.env.local` or any file containing the API key
- Do NOT add OPENROUTER_API_KEY to `.env` (that may be committed) — only `.env.local`
- Do NOT run OpenRouter calls with cpa-consulting client financial data (§7216 constraint)

---

## Phase 3: Judge-Builder Skill — recovery-platform

**Estimated time:** 1 session (~45 minutes)
**Context to load:** `workflow-plan-v2.md` sections "Phase 3", plus `~/dev/recovery-platform/.claude/skills/` to understand existing skill format
**Repos touched:** recovery-platform only

### 3.1 — Discover the existing skill format

Before writing the new skill, read one existing skill to copy its frontmatter format:

```bash
ls ~/dev/recovery-platform/.claude/skills/
cat ~/dev/recovery-platform/.claude/skills/$(ls ~/dev/recovery-platform/.claude/skills/ | head -1)/SKILL.md 2>/dev/null \
  || cat ~/dev/recovery-platform/.claude/skills/$(ls ~/dev/recovery-platform/.claude/skills/ | head -1) 2>/dev/null
```

### 3.2 — What to implement

Create a new skill directory:

```bash
mkdir -p ~/dev/recovery-platform/.claude/skills/judge-review
```

Create `~/dev/recovery-platform/.claude/skills/judge-review/SKILL.md` with the exact content from `workflow-plan-v2.md:Phase 3.2`.

Key fields to include:

- `name: judge-review`
- `description:` adversarial review for recovery-platform patterns
- The check list: logic errors, type safety, Firebase security rule violations, cross-product coupling, missing error handling, Stripe webhook risks, Redux mutations, missing Zod validation, missing tests
- JSON return schema: `{ issues: [...], verdict: "approve"|"revise" }`
- Tier guidance: use `TIER_C_MODEL` for judge pass; escalate to Tier B if change touches auth/payments/cross-product

### 3.3 — Create the rag-system judge variant

Create `~/dev/rag-system/.claude/skills/judge-review/SKILL.md` using the rag-system checklist from `workflow-plan-v2.md:Phase 3.4`:

- Missing Zod validation on new API routes
- Auth middleware not applied to new endpoints
- Missing pg-boss error handler on new job types
- Drizzle query without await
- New MCP tools missing input schema validation
- LocalEmbeddingProvider dimension mismatch risks

### 3.4 — Verification checklist

- [ ] `ls ~/dev/recovery-platform/.claude/skills/judge-review/SKILL.md` exists
- [ ] `ls ~/dev/rag-system/.claude/skills/judge-review/SKILL.md` exists
- [ ] `grep "judge-review" ~/dev/recovery-platform/.claude/skills/judge-review/SKILL.md` matches the name field
- [ ] Both SKILL.md files contain a JSON return schema with `verdict` field
- [ ] recovery-platform skill mentions "Firebase security rule violations"
- [ ] rag-system skill mentions "pg-boss error handler"

### 3.5 — Manual usage test

After creating the skills, open a new Claude Code session in recovery-platform and invoke:

```
/judge-review [paste a recent diff or a small code block]
```

Confirm the skill returns structured JSON with `issues` and `verdict` fields.

### 3.6 — Anti-pattern guards

- Do NOT write a judge skill that calls back to Claude Max for every review (defeats the cost purpose)
- The judge skill should explicitly instruct use of `TIER_C_MODEL` (OpenRouter Flash)
- Do NOT make the judge skill block commits automatically — it should return findings for review, not gate the workflow

### 3.7 — Commit

```bash
cd ~/dev/recovery-platform && git add .claude/skills/judge-review/ && git commit -m "feat(claude): add judge-review skill for adversarial pre-review pass"
cd ~/dev/rag-system && git add .claude/skills/judge-review/ && git commit -m "feat(claude): add judge-review skill for adversarial pre-review pass"
```

---

## Phase 4: CI Pipeline — recovery-platform

**Estimated time:** 1 session (~1 hour)
**Context to load:** `workflow-plan-v2.md:Phase 4`, plus `~/dev/rag-system/.github/workflows/ci.yml` as the reference implementation
**Repos touched:** recovery-platform only

### 4.1 — Read the reference CI

Before writing anything, read rag-system's CI as the template:

```bash
cat ~/dev/rag-system/.github/workflows/ci.yml
```

### 4.2 — What to implement

Create `~/dev/recovery-platform/.github/workflows/ci.yml`.

The recovery-platform CI must handle a **monorepo with 4 distinct TypeScript sub-projects**, each with different package managers and dependency trees. Do NOT write a single-package CI — it will fail.

Structure (adapt from workflow-plan-v2.md:Phase 4.1):

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  # Job per compilable package
  recovery-api:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: cd recovery-api && npm ci
      - run: cd recovery-api && npx tsc --noEmit
      - run: cd recovery-api && npm test -- --passWithNoTests

  homegroups-functions:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: cd homegroups/functions && npm ci
      - run: cd homegroups/functions && npx tsc --noEmit
      - run: cd homegroups/functions && npm test -- --passWithNoTests

  regroup-functions:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: cd regroup/functions && npm ci
      - run: cd regroup/functions && npx tsc --noEmit
      - run: cd regroup/functions && npm test -- --passWithNoTests

  detox-recovery:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: cd detox-recovery && npm ci
      - run: cd detox-recovery && npx tsc --noEmit
      - run: cd detox-recovery && npm test -- --passWithNoTests
```

**Critical gotcha:** Do NOT include `regroup/web` in CI — it uses Angular 9 with `NODE_OPTIONS=--openssl-legacy-provider` workarounds and a legacy build that is likely to fail on modern Node. Exclude it explicitly.

### 4.3 — Verification checklist

- [ ] `cat ~/dev/recovery-platform/.github/workflows/ci.yml` exists and is valid YAML
- [ ] File contains 4 separate jobs (not a matrix)
- [ ] `regroup/web` is NOT included in any job
- [ ] Each job uses `--passWithNoTests` flag on jest (so no tests ≠ CI failure)
- [ ] Push to a branch and confirm GitHub Actions triggers and all 4 jobs turn green
- [ ] The existing `claude-code-review.yml` is NOT modified

### 4.4 — Anti-pattern guards

- Do NOT use `npm test` without `--passWithNoTests` — some packages have zero tests and would fail
- Do NOT add `regroup/web` — the Angular 9 / `openssl-legacy-provider` setup will break in CI
- Do NOT modify the existing `claude.yml` or `claude-code-review.yml` — those are working and separate
- Do NOT run `npm run build` for mobile packages in CI — they require Xcode/Android SDK

### 4.5 — Commit

```bash
cd ~/dev/recovery-platform
git add .github/workflows/ci.yml
git commit -m "ci: add typecheck and unit test pipeline for TS packages"
git push
```

Then watch GitHub Actions on the next push to confirm all 4 jobs pass.

---

## Phase 5: rag-system — LocalEmbeddingProvider in CI

**Estimated time:** 15 minutes
**Context to load:** `~/dev/rag-system/.github/workflows/e2e.yml` + `~/dev/rag-system/packages/rag/src/` to confirm LocalEmbeddingProvider export name
**Repos touched:** rag-system only

### 5.1 — Confirm the LocalEmbeddingProvider env var name

Read the LocalEmbeddingProvider source to confirm the exact env var it reads:

```bash
find ~/dev/rag-system -name "*.ts" | xargs grep -l "LocalEmbedding" 2>/dev/null | head -5
grep -n "process.env\|EMBEDDING_PROVIDER\|EMBEDDING_MODEL" ~/dev/rag-system/packages/rag/src/embeddings/*.ts 2>/dev/null | head -20
```

### 5.2 — What to implement

Add `EMBEDDING_PROVIDER: local` to the `e2e.yml` env block (the outer `env:` at the job level, not inside the service container).

Copy the existing env block pattern from `e2e.yml`:

```yaml
# Add to the existing env: block in e2e.yml
EMBEDDING_PROVIDER: local
# Only add EMBEDDING_MODEL if LocalEmbeddingProvider reads it; confirm in step 5.1
```

**Do NOT change** the Postgres service container env — those are for the DB, not the app.

### 5.3 — Verification checklist

- [ ] `grep -n "EMBEDDING_PROVIDER" ~/dev/rag-system/.github/workflows/e2e.yml` returns a match
- [ ] The e2e test suite still passes locally after: `EMBEDDING_PROVIDER=local pnpm e2e`
- [ ] No Gemini API key error in CI logs after the change
- [ ] `grep -n "GEMINI_API_KEY" ~/dev/rag-system/.github/workflows/e2e.yml` returns nothing (key should not be needed with local provider)

### 5.4 — Anti-pattern guards

- Do NOT set `EMBEDDING_PROVIDER=local` in production Docker config — production should use Gemini
- Do NOT remove the existing Postgres env vars from the e2e.yml service block
- Confirm LocalEmbeddingProvider is fully implemented before adding to CI — if Phase A-1 is still in progress, this phase must wait

### 5.5 — Commit

```bash
cd ~/dev/rag-system
git add .github/workflows/e2e.yml
git commit -m "ci(e2e): use LocalEmbeddingProvider in CI to eliminate Gemini API dependency"
git push
```

---

## Phase 6: cpa-consulting — Tier Annotations in Prompts

**Estimated time:** 30 minutes
**Context to load:** `workflow-plan-v2.md:Phase 7`, `~/dev/cpa-consulting/prompts/`
**Repos touched:** cpa-consulting only

### 6.1 — Discover the prompts directory structure

```bash
ls -la ~/dev/cpa-consulting/prompts/
head -20 ~/dev/cpa-consulting/prompts/$(ls ~/dev/cpa-consulting/prompts/ | head -1)
```

### 6.2 — What to implement

Add a tier annotation header to each file in `prompts/`. Pattern to copy:

```markdown
<!-- Tier: C | Model: deepseek/deepseek-v4-flash | Escalate to: B if output needs synthesis across multiple docs -->
<!-- Tier: B | Model: anthropic/claude-3.5-sonnet | Escalate to: A if financial figures are generated -->
<!-- Tier: A | Model: claude-opus | DO NOT downgrade — client-facing output -->
```

Apply the tier assignments from `workflow-plan-v2.md:Phase 7.1`:

| Document type                        | Tier  |
| ------------------------------------ | ----- |
| Strategy doc initial draft           | C → B |
| Client-facing advisory output        | A     |
| Collateral format variations         | C     |
| Financial figure validation          | A     |
| Interview capture → structured notes | C     |
| RAG KB question testing              | B     |
| CLAUDE.md context updates            | C     |

### 6.3 — Verification checklist

- [ ] `grep -rn "Tier:" ~/dev/cpa-consulting/prompts/` returns results for every .md file
- [ ] At least one file is annotated `Tier: A`
- [ ] No financial-output prompts are annotated below Tier A
- [ ] Annotations are HTML comments (`<!-- -->`) so they don't appear in rendered output

### 6.4 — Commit

```bash
cd ~/dev/cpa-consulting
git add prompts/
git commit -m "docs(prompts): add model tier annotations for cost-routing discipline"
```

---

## Phase 7: Maestro Cloud CI Integration

**Estimated time:** 2–3 hours (includes app build)
**Prerequisite:** Phase 4 CI is green, Maestro Cloud account exists
**Human action required:** Maestro Cloud API key, built .ipa/.apk artifacts
**Context to load:** `workflow-plan-v2.md:Phase 4.2`, Maestro docs at `https://docs.maestro.dev`

### 7.1 — Manual steps (you must do these first)

1. Run `maestro login` or set `MAESTRO_CLOUD_API_KEY` env var
2. Add `MAESTRO_CLOUD_API_KEY` as a GitHub Actions secret in recovery-platform repo settings
3. Build one app artifact to test with (start with regroup iOS or homegroups iOS)

### 7.2 — What to implement

Add `maestro-smoke` job to `~/dev/recovery-platform/.github/workflows/ci.yml`:

```yaml
maestro-smoke:
  needs: [recovery-api, homegroups-functions, regroup-functions, detox-recovery]
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request' # Only on PRs, not every push
  steps:
    - uses: actions/checkout@v4
    - name: Maestro smoke — regroup
      uses: mobile-dev-inc/action-maestro-cloud@v1
      with:
        api-key: ${{ secrets.MAESTRO_CLOUD_API_KEY }}
        app-file: # path to pre-built .apk
        flow-file: e2e-maestro/regroup/login-and-view-dashboard.yaml
    - name: Maestro smoke — homegroups
      uses: mobile-dev-inc/action-maestro-cloud@v1
      with:
        api-key: ${{ secrets.MAESTRO_CLOUD_API_KEY }}
        app-file: # path to pre-built .apk or .ipa
        flow-file: e2e-maestro/homegroups/login-and-join-group.yaml
```

**Existing flows ready to use (no changes needed):**

- `e2e-maestro/homegroups/login-and-join-group.yaml`
- `e2e-maestro/regroup/login-and-view-dashboard.yaml`
- `regroup/mobile/maestro/` — in-product flows

### 7.3 — Verification checklist

- [ ] Maestro Cloud API key is set as a GitHub Actions secret (repo settings → Secrets)
- [ ] A test run on Maestro Cloud completes without auth errors
- [ ] The `needs:` block ensures unit CI passes before Maestro runs
- [ ] Maestro job only runs on PRs (`if: github.event_name == 'pull_request'`)
- [ ] Both existing yaml flows pass on Maestro Cloud before wiring to CI

### 7.4 — Anti-pattern guards

- Do NOT run Maestro on every push to main — only on PRs (saves Maestro Cloud credits)
- Do NOT modify the existing Maestro yaml flows — they are already working (`login-and-join-group.yaml`, `login-and-view-dashboard.yaml`)
- Do NOT gate this phase on a perfect CI run — ship Phase 4 CI first, add Maestro separately

---

## Final Phase: Verification — Confirm All Phases Delivered

Run these checks in one session after all phases complete:

```bash
# Phase 1 — Tier policy in all CLAUDE.md files
grep -c "Model Tier Policy" \
  ~/dev/recovery-platform/CLAUDE.md \
  ~/dev/rag-system/CLAUDE.md \
  ~/dev/cpa-consulting/CLAUDE.md
# Expected: each line shows "1"

# Phase 2 — OpenRouter configured
echo $OPENROUTER_API_KEY | cut -c1-8  # should print "sk-or-v1" (first 8 chars, no full key)
ls ~/dev/recovery-platform/.env.local ~/dev/rag-system/.env.local
# Both files should exist

# Phase 3 — Judge skills exist
ls ~/dev/recovery-platform/.claude/skills/judge-review/SKILL.md
ls ~/dev/rag-system/.claude/skills/judge-review/SKILL.md

# Phase 4 — CI file exists
ls ~/dev/recovery-platform/.github/workflows/ci.yml
# Check GitHub Actions: open recovery-platform repo → Actions tab → CI workflow

# Phase 5 — LocalEmbeddingProvider in rag-system CI
grep "EMBEDDING_PROVIDER" ~/dev/rag-system/.github/workflows/e2e.yml

# Phase 6 — Tier annotations in prompts
grep -c "Tier:" ~/dev/cpa-consulting/prompts/*.md 2>/dev/null | grep -v ":0"

# Phase 7 — Maestro CI (check manually in GitHub Actions)
cat ~/dev/recovery-platform/.github/workflows/ci.yml | grep -A5 "maestro"
```

**All-green checklist:**

- [ ] All 3 CLAUDE.md files show `"1"` for tier policy grep
- [ ] `.env.local` exists in both dev repos
- [ ] Both `judge-review/SKILL.md` files exist
- [ ] recovery-platform `ci.yml` exists and GitHub Actions shows green
- [ ] rag-system e2e.yml has `EMBEDDING_PROVIDER`
- [ ] cpa-consulting prompts have tier annotations
- [ ] Maestro smoke job exists in recovery-platform CI (or is in progress)

---

## Quick Reference: Phase Order and Dependencies

```
Phase 1 (Tier Policy) ─────────────────────────────────── No deps — start here
Phase 2 (OpenRouter)  ─────────────────────────────────── No deps — do in parallel with Phase 1
Phase 3 (Judge skill) ─── depends on: Phase 2 (needs TIER_C_MODEL env var concept)
Phase 4 (CI pipeline) ─────────────────────────────────── No deps — do any time
Phase 5 (LocalEmbed)  ─── depends on: LocalEmbeddingProvider Phase A-1 merged in rag-system
Phase 6 (CPA prompts) ─────────────────────────────────── No deps — do any time
Phase 7 (Maestro CI)  ─── depends on: Phase 4 green + Maestro Cloud account
```

**Parallel execution possible:** Phases 1, 2, 4, and 6 have no dependencies. Run them in the same day.
