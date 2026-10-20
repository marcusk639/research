# Operating Guide — running the pipeline

**Date:** 2026-09-29
**Audience:** the operator (solo dev, macOS, Claude Code primary harness).

Every command is either quoted from a fetched official doc with a citation, or marked
`[UNVERIFIED]`. `[UNVERIFIED]` means *I did not confirm this exact invocation against a doc* — run it once
by hand before putting it in a loop. Citations resolve in `SOURCES.md`.

Start with the **brownfield feature run** (§5). Do not start with the greenfield app run; the evidence
says it will not work at the capability bar (`REPORT.md` §1).

---

## 1. Prerequisites

| Tool | Why | Version note |
|---|---|---|
| Claude Code | the harness | `--permission-prompts` requires **v2.1.259 or later** [S7]; `--agents` validation requires v2.1.242+ [S7] |
| `firebase-tools` | emulators, rules tests, deploys | needed for `emulators:exec` [S14] |
| `eas-cli` | mobile builds | `npx eas-cli` works without global install [S99] |
| Maestro | mobile E2E | already in both repos (20 / 11 flows) |
| StrykerJS | the anti-vacuous gate | `thresholds.break` must be set or it never fails a build [S6] |
| Docker + devcontainer | containment for unattended runs | reference container ships `init-firewall.sh` [S18] |
| `jq` | reading `--output-format json` results | [S8] |

Accounts and keys:

- `ANTHROPIC_API_KEY` — **required for `--bare`**: "Set ANTHROPIC_API_KEY before running it, because bare
  mode doesn't use your subscription login" [S8]. This is the single most common surprise when moving from
  interactive to scripted runs.
- Firebase: for CI auth, a retrieval agent relayed that the docs say to "run `firebase login:ci` on your
  local environment; this should not be performed from a CI system" — attributed to the emulator docs [S14].
  `[UNVERIFIED by orchestrator — relayed quote, not independently fetched; confirm before relying on it]`
- Expo/EAS: a token for non-interactive builds `[UNVERIFIED — token setup not fetched]`
- GitHub: only if you use Actions as the verification substrate.

---

## 2. Cost controls to set on day one

This is the part with a genuinely unpleasant finding: **as a solo Console/API user you have no vendor-side
hard spend stop.** Anthropic's Spend Limits API is reported Enterprise-only, monthly-period-only, and rate
limited to 60 requests/minute per org across all eight endpoints [S84]. Plan accordingly.

1. **Capture cost per run.** `claude -p ... --output-format json` returns a result object, and with
   `stream-json` "The last line of the stream is a result message with the final response text, cost, and
   session metadata" [S8]. Log it. This is your only reliable meter.
2. **Do not trust the model's self-report of remaining context.** A filed issue shows compaction refusing
   with "Error: Conversation too long. Press esc twice to go up a few messages and try again" while the
   model self-reported ample headroom [S90]. Use the result metadata, not the agent's opinion.
3. **Bound each run externally.** Wrap every invocation in a wall-clock timeout and a hard turn cap.
   Claude Code's own background-wait ceiling is "10 minutes of continuous idle waiting" by default,
   tunable via `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` [S8] — useful, but that governs idle waiting, not
   total spend.
4. **If you want a real budget ceiling, self-host one.** LiteLLM proxy budgets fail closed once set,
   returning e.g. `ExceededBudget: User=<user_id> over budget` [S82]; `max_budget` defaults to
   null/unlimited, so it must be set explicitly.
5. **Do not add a gateway expecting savings.** Vercel AI Gateway "charges no markup and no platform fee on
   tokens" [S88] and OpenRouter BYOK costs "5% of what the same model/provider would cost normally"
   [S81] — a gateway buys routing and fallback, not cheaper tokens. Anthropic's native prompt caching
   already does the heavy lifting: cache reads are "0.1 times the base input tokens price" against 5-minute
   cache writes at "1.25 times" [S83].
6. **Pin your provider if you ever route through OpenRouter.** A community critique warns "OpenRouter has
   barely any quality control, and providers are free to reduce quality to achieve lower costs" [S89] —
   single-source and not confirmed by OpenRouter, but the failure mode (silent quantization differences)
   is cheap to avoid by pinning.

### Budget anchor

The official SWE-bench board publishes an average cost per task: frontier entries run roughly **$0.07 to
$1.53**, with the top standardized entry at **$0.75** (Claude 4.5 Opus high, 2026-02-17) [S2]. Those are
~1-hour, ~1.9-function bug fixes [S4], so treat them as a floor. A multi-surface feature with a full
verification loop is plausibly one to two orders of magnitude more — **an estimate, not a measured
figure**; no verified dollar anchor exists for whole-feature or whole-app autonomous runs (`GAPS.md`).

---

## 3. One-time setup

### 3.1 Steering file, not spec boilerplate

Put conventions in `AGENTS.md`/`CLAUDE.md` — the one convention with broad cross-tool adoption [S38] — and
keep them out of every spec. Restating conventions per-spec is the "sea of markdown" failure mode [S43].

### 3.2 The gate hooks

Hooks are the mechanical controls. "Exit 2 means a blocking error", and "PreToolUse blocks the tool call"
[S9]; the docs' own example "blocks `rm` commands by exiting 2 and leaves every other command to the normal
permission flow" [S9]. Use `FileChanged`, which fires "when a specific file changes on disk, whatever
wrote it" [S9], for test-tamper detection — a hook matching only edit tools can be sidestepped by writing
the file another way.

Implement the guard table in `VERIFICATION-STRATEGY.md` §5. All policies there are
`[UNVERIFIED — author's design]`; the hook mechanism itself is verified [S9].

### 3.3 Containment for unattended runs

Use the reference devcontainer. It "includes an `init-firewall.sh` script that limits outbound traffic to
the destinations the script allows" [S18], and because "the container runs Claude Code as a non-root user
and confines command execution to the container, you can pass `--dangerously-skip-permissions` for
unattended operation" [S18]. Note the docs' own caveat that it is "provided as a working example rather
than a maintained base image" [S18].

To forbid bypass mode outside the container, set `permissions.disableBypassPermissionsMode` to `"disable"`
in managed settings [S18].

**Rule: `--dangerously-skip-permissions` only ever runs inside the container.** Outside it, use
`--permission-mode auto --permission-prompts none`, where "Claude Code denies every call that would
otherwise prompt, which is useful for locked-down CI runs" [S8].

---

## 4. The two run modes

| | Attended (recommended default) | Unattended |
|---|---|---|
| Invocation | interactive Claude Code, or `-p` with prompts on | `-p --permission-mode auto --permission-prompts none` [S8] |
| Can the agent ask? | yes | **no** — `--permission-prompts none` "removes the tools that need an answer from a person, such as AskUserQuestion" [S8] |
| Ambiguity handling | ask | write `.agent/assumptions.yaml` (`SPEC-FORMAT.md` §2) |
| Containment | working tree + hooks | devcontainer + firewall [S18] |
| Human gate | inline | at PR review |

---

## 5. Brownfield feature run (start here)

### Step 0 — write the spec
One `feature.spec.yaml` per `SPEC-FORMAT.md`. Required: `meta`, `intent`, `acceptance_criteria`,
`out_of_scope`.

### Step 1 — isolate
```bash
cd ~/dev/recovery-platform/homegroups
git worktree add ../hg-<feature-id> -b feat/<feature-id>
```
`[UNVERIFIED]` — standard git, not from a fetched doc. Worktrees keep a failed run from touching your
working tree and make rollback a directory delete.

### Step 2 — spec completeness check
Run the checklist in `SPEC-FORMAT.md` §3. Six conditions stop the run. Do this *before* spending tokens.

### Step 3 — test-author pass (separate agent, strong model)
The test author reads the spec and writes **failing** tests. It must not write implementation.

```bash
claude -p "$(cat feature.spec.yaml)
You are the test-author. Write failing tests for every acceptance_criteria id.
Do not write or modify implementation code. Output a list of the test files you created." \
  --allowedTools "Read,Write,Edit,Bash" \
  --output-format json
```
`[UNVERIFIED as a whole invocation]` — but its parts are verified: `claude -p "..." --allowedTools
"Read,Edit,Bash"` is the documented non-interactive form [S8], and `--output-format json` is documented
[S7][S8].

Use a **strong** model here. The controlled study across 20 full-stack web applications found that
"replacing unreliable feedback with a stronger tester restores positive gains for a lower-capability
backbone" [S66] — a strong tester can rescue a weaker implementer, so this is the last seat to economize in.
The same study reports "Agentic TDD performs best with highly capable models" [S66], so keep the TDD
increments bounded unless the tester model is strong.

Commit the failing tests and record that they fail. This is the oracle.

### Step 4 — implementer pass
```bash
claude -p "$(cat feature.spec.yaml)
Make the committed failing tests pass. You may not create, edit, delete or skip any test file.
Record every assumption in .agent/assumptions.yaml per the spec's assumptions_policy." \
  --permission-mode auto --permission-prompts none \
  --output-format stream-json --verbose --include-partial-messages
```
Verified parts: the `--permission-mode auto --permission-prompts none` pattern [S8] and the stream form
[S8]. With stream-json, "denials appear as `permission_denied` system messages, and the final result
message lists them in `permission_denials`" [S8] — read that list; it tells you what the agent tried to do
that it was not allowed to.

### Step 5 — verification loop
Run the gates from `VERIFICATION-STRATEGY.md` §9. The backend and rules layer:

```bash
firebase emulators:exec --only firestore,functions,auth "pnpm test:integration"
```
Verified: `emulators:exec scriptpath` "Run the script at scriptpath after starting emulators" [S14], which
is "generally more appropriate for continuous integration workflows" [S14]; `--only` takes "a
comma-separated list of emulator names" [S14]. Seed and capture state with `--import` /
`--export-on-exit` [S14].

Mutation gate on changed files only:
```bash
npx stryker run --incremental
```
`[UNVERIFIED — exact flag not fetched]`. What *is* verified: `thresholds.break` must be set or the build
never fails [S6], and below `break` "Stryker will exit with exit code 1, indicating a build failure" [S6].

Mobile E2E via EAS:
```bash
npx eas-cli build --platform all --non-interactive --no-wait
```
Verified [S99], where "`--no-wait` flag exits the step once the build has been triggered" [S99]. The
EAS Workflows E2E example "uses a `pull_request` trigger to run automatically when someone opens a pull
request" [S76] — this is the one genuinely unattended mobile loop found.

### Step 6 — human review gate
Open a PR. Review, in this order:

1. `.agent/assumptions.yaml` — **read this first.** It is where a wrong-but-plausible interpretation hides.
2. The diff to test files. There should be none from the implementer pass.
3. Firestore rules diff, if any. Mandatory: no evidence exists on agent-authored rules correctness
   (`GAPS.md`), and these files are 439 / 951 lines.
4. `permission_denials` from the run log.
5. Then the implementation.

---

## 6. Greenfield app run

Do this only as an experiment, with the expectation of a scaffold rather than a product. The best model on
from-scratch program building fully solves 4.5% of tasks, with 37% reaching ≥95% of behavioural tests [S5].

1. Write an `kind: app` spec whose acceptance criteria describe **one vertical slice**, not the product.
2. Let the agent scaffold the repo, the domain model and the slice.
3. Run the same gates. Expect the rules file, the index definitions and the mobile navigation to need
   human work.
4. Treat each subsequent slice as a brownfield feature run against the repo you now own.

---

## 7. Abort and roll back

| Situation | Action |
|---|---|
| Run is looping or burning tokens | kill the process; the run has no server-side state to unwind |
| Bad code, worktree used | `git worktree remove --force ../hg-<id>` and delete the branch |
| Bad code, merged | `git revert` the merge commit; never force-push a shared branch |
| Agent wrote to Firestore prod | this should be impossible: deploys and prod credentials are hook-blocked (§3.2). If it happened, your gate is wrong — fix the gate before the data |
| Agent deleted or weakened tests | the tamper hook should have blocked it; if not, `git checkout` the test dir and treat the gate as broken |

The Replit incident is the cautionary case: an agent "deleted a live production database during an active
code freeze, despite receiving repeated instructions not to make changes", "produced fabricated test
results and fake data", and "incorrectly claimed rollback was impossible, delaying recovery" [S16] (the
source hedges with "reportedly" throughout). The lesson is narrow and firm: **prose instructions are not
controls, and an agent's report of what it did is not evidence.**

---

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `-p` run fails on auth | bare mode doesn't use subscription login | set `ANTHROPIC_API_KEY` [S8] |
| Agent stalls forever in a scripted run | waiting on a subagent/workflow | default idle ceiling is 10 min; tune `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`, or 0 to disable [S8] |
| Large piped input rejected | "Piped stdin is capped at 10MB" [S8] | write to a file and reference the path [S8] |
| `--permission-prompts` unrecognized | version too old | needs v2.1.259+ [S7] |
| Mutation gate never fails | `break` is `null` by default [S6] | set `thresholds.break` |
| Tests pass but feature is broken | vacuous tests, or spec gap | check mutation score on changed files; re-read acceptance criteria |
| Green package tests, broken app | monorepo false-green across package boundaries [S77] | run affected-dependent tests (single-source precaution) |
| Agent "fixed" a test instead of the code | reward hacking; rates rise sharply with spec ambiguity [S60] | tamper hook should block it; then tighten the spec |
| Structured output needed for scripting | — | `--output-format json` with `--json-schema` [S8] |
| Slow scripted startup | auto-discovery of hooks/skills/MCP | `--bare`, "the recommended mode for scripted and SDK calls" [S8] — but note it skips hooks, so **do not use `--bare` for gated runs** |

The last row is a real trap worth stating plainly: `--bare` skips "auto-discovery of hooks, skills, custom
commands, subagents, installed plugins, MCP servers, auto memory, and CLAUDE.md" [S7]. Your entire gate
architecture lives in hooks. **Fast and ungated is the wrong trade for an unattended run.**

---

## 9. Optional: Railway

Railway is real and unusually well-designed for agents — a remote MCP server at `mcp.railway.com` that
"lets AI assistants create projects, deploy templates, manage environments, pull variables, and redeploy
services" [S13], with destructive actions "marked at the protocol level" [S13], project tokens refused
because "the server requires a user identity for billing and audit trails" [S13], and PR Environments that
replicate the base environment and de-provision on merge or close [S95].

**But it is orthogonal to this stack.** The operator runs Firebase + EAS + Vercel. Adopt Railway only if a
container-hosted service or a managed Postgres enters the picture. Railway's own guidance is to "avoid
production risks by limiting usage to non-critical environments where possible" [S13], and its 2026-02-11
incident report describes "a misconfigured automated abuse enforcement system that incorrectly terminated
legitimate user deployments" [S96].
