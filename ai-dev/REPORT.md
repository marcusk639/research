# AI Dev

> Status: draft · Started: 2026-10-21

## Research Question

What is the current state of AI-assisted software development — tools, agent workflows, and
the evidence on their effectiveness — across the software development lifecycle (planning,
coding, review, testing, debugging, documentation, CI/CD, maintenance)? The survey is meant to
support evaluating which development practices are realistic candidates for automation, and
where the evidence says automation helps, hurts, or is still unproven.

## Key Findings

The broad survey hasn't started yet. One deep-dive is complete:

### Testing: automated E2E suite generation for React Native + Firebase (2026-10-21)

Full report: [`e2e-generation_20261021/report.md`](e2e-generation_20261021/report.md). It is a deep-mode run: 216 sources, quote fidelity checked against raw pages, and four-persona red-team plus a second review round (v2.1). The reference target is `~/dev/recovery-platform/regroup`.

- **A one-command `/generate-e2e` is buildable from existing parts, but not as one unattended run.** The realistic design is a resumable pipeline (a Claude Code skill with deterministic scripts and hooks) that ends in a reviewable bundle a human accepts or triages. Among the products surveyed, none reads the codebase, writes a spec, emits a durable RN suite, and asserts Firebase backend state.
- **Execute–rerun–filter is mandatory.** At unit level Meta discards most raw output. Spec-first E2E pipelines did better (around 60% usable) but still reworked about a third.
- **Code-derived oracles bless current behaviour.** Bugs come through implicit oracles (crashes), cross-artifact disagreements (rules vs client access, web vs mobile, docs vs code), and light intent with human triage.
- **The Firebase harness is the hard part of bring-up, and mostly mechanical:** `demo-` projects, routing every service to an emulator, triggering scheduled functions via Pub/Sub, mocking Stripe UI, and state management (persona sessions, listeners, clocks, trigger-aware fixtures).
- **The mobile runner must be chosen by a local spike.** Maestro has the best agent tooling but an open iOS driver bug on Xcode 26. Detox's sync is better, but RN 0.72 is outside its supported range. Use Playwright for the web.
- **Repair loops need mechanical guards.** Reward hacking is documented, so guards should be read-only approved tests, assertion-baseline hashes, and iteration caps, not prompts alone.
- **Regroup findings worth acting on regardless:**
  - The Functions client is never routed to the emulator, so E2E callables hit the real project. No emulator reachability check runs either.
  - Six client-accessed Firestore paths have no rule in the repo.
  - The seed script was lost to an old ignore-all-JS gitignore rule, and the documented Detox suites were likely lost the same way.

## Sources

Per-deep-dive. See each run directory's `sources.jsonl` and bibliography.
