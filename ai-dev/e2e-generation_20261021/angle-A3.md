# Angle A3 — Code-to-specification: getting from source to a trustworthy behavioral spec

Worker: A3 · Run date: 2026-10-21 · Tools: built-in WebSearch + WebFetch only. Every evidence row below was fetched; search snippets are not used as evidence.

## Sources

A3-S1 | https://arxiv.org/abs/2307.03172 | Lost in the Middle: How Language Models Use Long Contexts (Liu et al.) | TACL / arXiv | 2023-07-06 (accepted 2023-11-20) | primary
A3-S2 | https://www.trychroma.com/research/context-rot | Context Rot: How Increasing Input Tokens Impacts LLM Performance (Hong, Troynikov, Huber) | Chroma | 2025-07-14 | secondary (vendor technical report, open replication code)
A3-S3 | https://arxiv.org/abs/2505.07897 | LongCodeBench: Evaluating Coding LLMs at 1M Context Windows (Rando et al.) | arXiv | 2025-05-12 (v3 2025-10-22) | primary
A3-S4 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Effective context engineering for AI agents | Anthropic | 2025-09-29 | secondary (vendor about own practice)
A3-S5 | https://www.anthropic.com/engineering/multi-agent-research-system | How we built our multi-agent research system | Anthropic | 2025-06-13 | secondary (vendor about own product)
A3-S6 | https://code.claude.com/docs/en/sub-agents | Create custom subagents (Claude Code docs) | Anthropic | accessed 2026-10-21 | secondary (vendor docs)
A3-S7 | https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/ | Settling the RAG Debate: Why Claude Code Dropped Vector DB-Based RAG | SmartScope blog (quotes Boris Cherny on X) | 2026-03-23 | blog (the underlying X post was not fetched directly)
A3-S8 | https://aider.chat/docs/repomap.html | Repository map | Aider | undated, accessed 2026-10-21 | secondary (vendor docs)
A3-S9 | https://arxiv.org/html/2410.14684v2 | RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph (Ouyang et al.) | ICLR 2025 / arXiv | 2024-10-03 (rev. 2025-03-18) | primary
A3-S10 | https://pldi16.sigplan.org/event/soap-2016-papers-on-the-unsoundness-of-static-analysis-for-android-guis | On the Unsoundness of Static Analysis for Android GUIs (Wang, Zhang, Rountev) | SOAP @ PLDI 2016 | 2016 | primary
A3-S11 | https://arxiv.org/abs/2105.03144 | What do all these Buttons do? Statically Mining Android User Interfaces at Scale (Frontmatter; Kuznetsov … Zeller) | arXiv / MSR | 2021-05-07 | primary
A3-S12 | https://arxiv.org/html/2606.27665 | LLM-Assisted Model-Based GUI Testing for Vue.js Web Applications (LLMVue; Li et al.) | arXiv | 2026-06-26 | primary (preprint)
A3-S13 | https://reactnavigation.org/docs/static-vs-dynamic | Static vs Dynamic API (React Navigation 7.x) | React Navigation | accessed 2026-10-21 | secondary (official docs)
A3-S14 | https://stately.ai/docs/xstate-test | @xstate/test (model-based testing) | Stately | accessed 2026-10-21 | secondary (official docs)
A3-S15 | https://plse.cs.washington.edu/daikon/ | The Daikon invariant detector | Univ. of Washington PLSE | accessed 2026-10-21 | primary (tool home page)
A3-S16 | https://arxiv.org/abs/2401.08807 | SpecGen: Automated Generation of Formal Program Specifications via LLMs (Ma et al.) | ICSE 2025 / arXiv | v5 2025-02-25 | primary
A3-S17 | https://arxiv.org/abs/2310.01831 | Can LLMs Transform Natural Language Intent into Formal Method Postconditions? (nl2postcond; Endres et al.) | FSE 2024 / arXiv | v2 2024-04-15 | primary
A3-S18 | https://arxiv.org/abs/2410.21136 | Do LLMs generate test oracles that capture the actual or the expected program behaviour? (Konstantinou, Degiovanni, Papadakis) | arXiv | 2024-10-28 | primary (preprint)
A3-S19 | https://arxiv.org/abs/2509.19587 | Reverse Engineering User Stories from Code using LLMs (Ouf et al.) | CASCON 2025 / arXiv | 2025-09-23 | primary
A3-S20 | https://arxiv.org/abs/2609.22719 | From Code to Requirements: Agentic Reverse Engineering of Business Rules at Enterprise Scale (Agrawal et al.) | arXiv | 2026-09-19 | primary (preprint, industry authors)
A3-S21 | https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl (Birgitta Böckeler) | martinfowler.com (Thoughtworks) | 2025-10-15 | secondary (practitioner hands-on evaluation)
A3-S22 | https://github.com/github/spec-kit | github/spec-kit README | GitHub | accessed 2026-10-21 | secondary (vendor about own product)
A3-S23 | https://kiro.dev/docs/specs/ | Specs (Kiro docs) | AWS Kiro | page updated 2026-10-15 | secondary (vendor docs)

Unreachable: https://visualstudiomagazine.com/articles/2025/09/16/github-spec-kit-experiment-a-lot-of-questions.aspx (HTTP 403). Original Boris Cherny X post (x.com/bcherny/status/2017824286489383315) not fetched; quoted only through A3-S7.

## Evidence

A3-E1 | A3-S1 | "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts" | abstract
A3-E2 | A3-S2 | "Models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows." | report summary/conclusion
A3-E3 | A3-S2 | "18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models" | report intro
A3-E4 | A3-S3 | "long-context remains a weakness for all models, with performance drops such as from 29% to 3% for Claude 3.5 Sonnet, or from 70.2% to 40% for Qwen2.5" | abstract
A3-E5 | A3-S4 | "As the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases." | section on context rot
A3-E6 | A3-S4 | "Agents built with the 'just in time' approach maintain lightweight identifiers...and use these references to dynamically load data into context at runtime using tools." | just-in-time context section
A3-E7 | A3-S4 | "Each subagent might explore extensively...but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)." | sub-agent architectures section
A3-E8 | A3-S4 | "Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window." | long-horizon tasks section
A3-E9 | A3-S5 | "Multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%" | benefits section (internal research eval)
A3-E10 | A3-S5 | "multi-agent systems use about 15× more tokens than chats" | benefits/costs section
A3-E11 | A3-S5 | "Most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time" | limitations section
A3-E12 | A3-S6 | "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions." | overview
A3-E13 | A3-S6 | "A fast, read-only agent optimized for searching and analyzing codebases." | built-in subagents: Explore
A3-E14 | A3-S7 | "Early versions of Claude Code used RAG + a local vector db, but we found pretty quickly that agentic search generally works better." | quoted X post by Boris Cherny
A3-E15 | A3-S8 | "a concise map of your whole git repository that includes the most important classes and functions along with their types and call signatures" | intro
A3-E16 | A3-S8 | "using a graph ranking algorithm, computed on a graph where each source file is a node and edges connect files which have dependencies" | "Optimizing the map"
A3-E17 | A3-S8 | "The token budget is influenced by the `--map-tokens` switch, which defaults to 1k tokens." | "Optimizing the map"
A3-E18 | A3-S9 | "RepoGraph boosts the success rate of existing methods for both agent and procedural frameworks by achieving an average relative improvement of 32.8%." | intro/results (SWE-bench, 4 frameworks)
A3-E19 | A3-S10 | "Android software presents exciting new challenges for the static analysis community. However, static analyses for Android are typically unsound." | abstract
A3-E20 | A3-S10 | "the static modeling of control/data flow due to interactions of the user with the application's GUI" | abstract (scope: FlowDroid, IccTA, GATOR compared against runtime callback sequences)
A3-E21 | A3-S11 | "all declared screens, the user interface elements, their textual and graphical features, as well as Android APIs invoked by interacting with them" | abstract
A3-E22 | A3-S12 | "LLMVue follows a three-stage pipeline: (I) Static Graph Extraction; (II) LLM-based Semantic Refinement; and (III) Graph Normalization." | approach section
A3-E23 | A3-S12 | "across the ten projects, LLMVue achieves an average precision of 94.57%, recall of 88.79%, and F1-score of 91.25%" | evaluation (RQ on PTG quality)
A3-E24 | A3-S12 | "Transition candidates, which are spread across router configurations and single-file components (SFCs), must be concretized and normalized into an executable page transition graph (PTG)" | abstract
A3-E25 | A3-S13 | "The main limitation of the static API is that the navigation structure must be static. This means that you cannot create the list of screens dynamically." | static vs dynamic (7.x)
A3-E26 | A3-S14 | "`testPath.test()` executes each step in `testPath.segments` by: 1. Verifying that the SUT is in `segment.state` 2. Executing the event for `segment.event`" | test paths section
A3-E27 | A3-S14 | "the latest version of the model-based testing utilities (prev. `@xstate/test`) are now part of the latest `@xstate/graph` package" | page banner
A3-E28 | A3-S15 | "can detect properties in C, C++, C#, Eiffel, F#, Java, Perl, and Visual Basic programs; in spreadsheet files; and in other data sources" | home page
A3-E29 | A3-S16 | "existing methods usually rely on predefined templates or grammar, making them struggle to accurately describe the behavior and functionality of complex real-world programs" | abstract
A3-E30 | A3-S16 | "SpecGen succeeds in generating verifiable specifications for 279 out of 385 programs, outperforming the existing purely LLM-based approaches and conventional specification generation tools like Houdini and Daikon" | abstract
A3-E31 | A3-S17 | "nl2postcond generated postconditions were able to catch 64 real-world historical bugs from Defects4J" | abstract
A3-E32 | A3-S18 | "LLM-based test generation approaches mainly capture the actual program behavior making bug detection difficult." | abstract
A3-E33 | A3-S18 | "LLMs are better at generating oracles than classifying them." | abstract
A3-E34 | A3-S19 | "all models achieve, on average, an F1 score of 0.8 for code up to 200 NLOC" | abstract
A3-E35 | A3-S19 | "a single illustrative example enables the smallest model (8B) to match the performance of a much larger 70B model" | abstract
A3-E36 | A3-S20 | "Seven specialized agents collaborate to discover user journeys, extract business rules" | abstract
A3-E37 | A3-S20 | "overseen by human reviewers at controlled escalation points" | abstract
A3-E38 | A3-S20 | "Extracted rules independently corroborated against real production defect records" | abstract
A3-E39 | A3-S21 | "the workflow was like using a sledgehammer to crack a nut" | Kiro section (small bug became 4 user stories with 16 acceptance criteria)
A3-E40 | A3-S21 | spec-kit produced "a LOT of markdown files" that were "repetitive" and "tedious to review" | spec-kit section
A3-E41 | A3-S21 | "non-determinism in action" | Tessl section (same spec, repeated generations differ)
A3-E42 | A3-S22 | "Define what to build and why, then turn the specification into a plan, tasks, and working code." | README intro
A3-E43 | A3-S23 | "requirements.md (or bugfix.md) - Captures user stories, acceptance criteria, or bug analysis in structured notation" | spec files section

## Claims

A3-C1 | Putting more tokens into context reliably degrades retrieval/reasoning; the degradation depends on position and is non-uniform, so "load the whole repo" is not a sound comprehension strategy even with 1M-token windows. | support: A3-E1, A3-E2, A3-E3, A3-E4, A3-E5 | independent_sources: 4 (S1, S2, S3, S4) | high
A3-C2 | On code specifically, long-context performance drops sharply at the 1M-token scale (e.g., Claude 3.5 Sonnet 29%→3% on LongCodeBench). A 212k-LOC app (roughly a few million tokens) is beyond what any single context can hold reliably. | support: A3-E4 | independent_sources: 1 | medium (single benchmark, older models; the direction matches C1)
A3-C3 | Anthropic's guidance for large tasks: just-in-time agentic retrieval through tools, subagents in isolated contexts that return condensed summaries of about 1–2k tokens, and structured notes persisted outside the context. | support: A3-E6, A3-E7, A3-E8, A3-E12 | independent_sources: 1 (Anthropic, two documents) | medium (vendor guidance, not an independent eval)
A3-C4 | Claude Code moved from a RAG/vector index to agentic (grep and read) search because it worked better. | support: A3-E14 | independent_sources: 1 (secondhand blog quoting the developer) | medium-low
A3-C5 | Multi-agent orchestration beat a single agent by 90.2% on Anthropic's internal research eval, at about 15× chat token cost. Anthropic itself cautions that coding tasks parallelize less well than research. | support: A3-E9, A3-E10, A3-E11 | independent_sources: 1 | medium (vendor internal eval; the transfer to code comprehension is unproven)
A3-C6 | Feature-by-feature comprehension of a repo is a read-mostly, highly parallel task, which is closer to "research" than to "coding" in A3-E11's sense. This makes it a better fit for subagent fan-out than code edits are. | support: A3-E11, A3-E13 (inference) | independent_sources: 1 | low (analyst inference)
A3-C7 | Deterministic structural indexes (a tree-sitter repo map ranked by a dependency graph; repository code graphs) measurably help LLM agents. RepoGraph reports +32.8% average relative improvement across 4 frameworks on SWE-bench. | support: A3-E15, A3-E16, A3-E17, A3-E18 | independent_sources: 2 (S8 vendor, S9 peer-reviewed) | medium-high
A3-C8 | Static GUI/navigation models are useful but unsound. Static analyses for Android, GATOR included, systematically miss runtime GUI control flow, so a statically extracted screen graph must be treated as a candidate set and confirmed at runtime. | support: A3-E19, A3-E20, A3-E21 | independent_sources: 2 | high
A3-C9 | A hybrid works well on web SPAs: high-recall static extraction from router config and components, then LLM semantic refinement, then deterministic normalization. LLMVue reached P 94.57% / R 88.79% / F1 91.25% on 10 Vue projects. No ablation isolates the LLM's contribution. | support: A3-E22, A3-E23, A3-E24 | independent_sources: 1 | medium (single preprint, GPT-4o, Vue rather than RN)
A3-C10 | React Navigation's static API (v7+) gives a machine-readable route graph, but only when the whole structure is static. An app on RN 0.72 most likely uses the dynamic, component-based API (v6 era), so its route graph must be recovered from JSX/AST plus conditional (role/auth) rendering. | support: A3-E25 | independent_sources: 1 | medium (the v6 usage is an inference about the target app; verify in repo)
A3-C11 | Model-based testing tools take an explicit state machine whose states carry assertions and whose events carry executors, and they generate covering paths automatically. The @xstate/test utility has been folded into @xstate/graph. | support: A3-E26, A3-E27 | independent_sources: 1 | high (doc fact)
A3-C12 | Classic dynamic invariant mining (Daikon) does not support JavaScript/TypeScript, so it is not usable off the shelf for an RN/Angular/Functions stack. | support: A3-E28 | independent_sources: 1 | high (doc fact)
A3-C13 | LLMs can produce verifiable formal specs and postconditions with useful bug-finding power when verification closes the loop (SpecGen 279/385, verifier-checked) or when the natural-language intent is clear (nl2postcond caught 64 Defects4J bugs). | support: A3-E29, A3-E30, A3-E31 | independent_sources: 2 | medium-high (function-level, Java/Python, not app-level E2E)
A3-C14 | The core epistemic risk is empirically real: LLM-generated oracles mostly capture the program's actual behaviour, not its expected behaviour. A spec mined purely from code tends to bless existing bugs. | support: A3-E32, A3-E33 | independent_sources: 1 | medium (single preprint, unit-level; consistent with the known limits of regression oracles)
A3-C15 | LLMs recover user stories from small code units well (F1 about 0.8 up to 200 NLOC). One worked example closes much of the gap between small and large models, which implies a feature-sliced, few-shot extraction design. | support: A3-E34, A3-E35 | independent_sources: 1 | medium (snippet-level; performance at larger units is not reported in the abstract)
A3-C16 | Industrial agentic code→requirements pipelines exist (7 agents, user journeys + business rules). They rely on human reviewers at escalation points and validate against production defect records rather than trusting the output. | support: A3-E36, A3-E37, A3-E38 | independent_sources: 1 | medium-low (fresh preprint, industry self-report)
A3-C17 | Current spec-driven-development tools (Spec Kit, Kiro, Tessl) are built for forward generation (spec→code), not for recovering specs from code. Hands-on evaluation found verbose, repetitive Markdown with a heavy review burden, agents that ignore the spec, and nondeterministic regeneration. | support: A3-E39, A3-E40, A3-E41, A3-E42, A3-E43 | independent_sources: 2 (S21 independent; S22/S23 vendor) | medium-high
A3-C18 | Spec formats in current SDD tools are Markdown user stories with acceptance criteria (Kiro requirements.md; Spec Kit specify). These are human-reviewable but not machine-executable without a further translation step. | support: A3-E42, A3-E43 | independent_sources: 2 (both vendor) | medium

## Conflicts & gaps

- **Long context: vendor vs evidence.** Large context windows are marketed (1M tokens), while A3-S1/S2/S3 and Anthropic's own A3-S4 document degradation. No conflict on direction. The magnitude for current-generation models (2026) on _code comprehension_ is not established. LongCodeBench's numbers are for 2024–25 models.
- **Multi-agent for code.** A3-S5 reports large gains for research and also warns that coding parallelizes poorly. Whether _read-only comprehension_ behaves like research has not been tested publicly (C6 is inference).
- **Agentic search vs indexes.** A3-S7 (agentic grep beats a vector DB) and A3-S9/S8 (structural graphs help) do not conflict. The first concerns _embedding_ retrieval, the second _deterministic structure_. No source directly compares grep-only against grep plus code graph for spec extraction.
- **React Native specifics: major gap.** I found no fetched source on static extraction of React Navigation v6 route graphs, Redux Toolkit action/slice maps, Firestore collection-access maps, or callable-invocation graphs for RN. GATOR/Frontmatter are Android-native (bytecode) and do not apply to JS bundles. LLMVue (Vue) is the closest analogue. A tree-sitter/TS-compiler-API extractor for this stack would have to be custom-built.
- **Firestore security rules as an oracle source.** Not covered by fetched evidence here. Rules are an explicit, declarative statement of _intended_ access policy per role, which plausibly makes them the highest-value intent artifact in this stack. Defer to the angle covering Firebase.
- **App-level spec mining.** SpecGen, nl2postcond and Konstantinou et al. are all function/unit-level (Java/Python). No fetched evidence on how accurately an LLM recovers _multi-screen, multi-role user flows_ from a ~200k-LOC app. A3-S20 claims this at enterprise scale but publishes no accuracy figure in the abstract.
- **Spec Kit brownfield.** The README advertises an existing-codebase guide (A3-S22). The independent evaluation (A3-S21) found brownfield adoption particularly hard. Unresolved; no quantitative study.
- **Unreachable:** Visual Studio Magazine Spec Kit hands-on (403).

## Analyst assessment

_(Analyst synthesis. This section goes beyond the sourced claims and is not itself evidence.)_

**Comprehension strategy.** Do not try to "understand the app" in one context. C1–C2 make that a known failure mode at 212k LOC. Use a three-layer design:

1. **Deterministic fact layer first (no LLM).** Build a TS-compiler/tree-sitter pass that emits JSON: navigator tree and screen→component map (from `createStackNavigator`/`<Stack.Screen>` JSX, including conditional/role-gated branches); `navigate('X')` call sites as edges; RTK slices, thunks and actions; every `collection()/doc()` path with read/write mode; every `httpsCallable('name')` and its server handler; triggers; Angular routes and guards; and a parsed `firestore.rules` match tree. This is the RN analogue of LLMVue's stage I and of Aider's repo map (C7, C9). Treat it as high-recall and unsound (C8).
2. **Feature-sliced LLM interpretation.** Partition by feature (screen cluster plus its slices, collections and callables) and fan out read-only subagents, each with the fact JSON for its slice, returning a capped (~2k-token) structured summary written to disk as notes (C3, C6, C15). One worked example per prompt (C15).
3. **Runtime confirmation.** Before trusting the graph, crawl it against the emulator-backed app (C8). Unreached edges get flagged, not silently dropped.

**Spec format.** Use a two-tier artifact:

- A machine-checkable **flow model** per feature: a statechart-like YAML with states holding screen assertions plus `testID`s, events holding actions, roles as guards, and Firestore/callable side-effects as postconditions. Something like XState's state-assertion/event-executor shape (C11) works, without necessarily adopting the library. Paths through it become E2E cases.
- A human-readable **Given/When/Then rendering** generated _from_ that model for review. Do not use Markdown-first SDD tooling as the source of truth. It is built for the opposite direction and its review burden is documented (C17–C18).

**The epistemic problem cannot be automated away.** Code-derived specs bless existing bugs (C14). Mitigations, in decreasing trust:

1. Prefer intent-bearing artifacts as oracles over implementation logic: security rules, existing tests, PRDs/docs, issue tracker, commit messages.
2. Have the LLM tag every spec assertion with its provenance (`rule`, `doc`, `test`, `code-only`) and confidence.
3. Mandatory human checkpoints. Review is cheapest at the per-feature flow-model level, before test generation, focused on `code-only` assertions and on any place where code and docs/rules disagree. Those disagreements are the most valuable output: each is either a bug or a stale doc.

Industrial practice already includes such escalation points (C16). A one-command tool should therefore be "one command plus a review gate", not fully autonomous.

**Cost note:** multi-agent fan-out costs roughly 15× chat tokens (C5). Budget per-feature runs rather than full regenerations, and cache the fact layer by file mtime as Aider does.
