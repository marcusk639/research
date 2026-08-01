# W7 — Diagnosing Internal Process and Org Problems Before Automating

_Phase B findings | Generated: 2026-08-01 | Sources consulted: 31 | Read in full: 8_

---

## Ledger Verdicts

**No claims were assigned to W7.**

`corpus-ledger.md` contains 211 extracted claims across seven corpus documents. A search of the
entire ledger for "W7" returns exactly one hit, at line 586, inside §5's coverage-gaps note, which
records that the corpus never addresses "dysfunction before recommending automation (W7)." No claim
row in §1's Claims Register carries `W7` in its **Verify in** column, and no contradiction in §3 is
assigned to W7.

| Claim ID | Verdict | Current value / correction | Evidence tier | Source | Notes                                 |
| -------- | ------- | -------------------------- | ------------- | ------ | ------------------------------------- |
| —        | —       | —                          | —             | —      | No claims assigned to this workstream |

This is a true zero, not an omission: the seven corpus documents are entirely about AI coding
harnesses, model routing, and cost arbitrage. There is no prior art in the corpus on process
diagnosis, organizational diagnosis, Lean/Six Sigma, Theory of Constraints, process mining, or
decision-rights mapping. The whole of this file is original research.

## Contradiction Findings

No contradictions from §3 of the ledger are assigned to W7.

One contradiction surfaced _during_ this research that Phase C should carry forward, because it is
the central live dispute in the subject area:

**X-W7-A — "Fix the process first" vs. "automate the happy path and optimise later."** Both
positions are held by credentialed sources with real delivery experience, and both are C-to-B tier.
See F-W7-07 (fix-first) against F-W7-14 (automate-first). The evidence is genuinely mixed, and the
split is characterised in the Direct Answers section rather than resolved. Neither side has a
controlled study. What separates them is not evidence quality but scope: fix-first sources are
arguing about _end-to-end process outcomes_, automate-first sources are arguing about _time to
first delivered bot_. They are not measuring the same dependent variable.

---

## Findings

### Part 1 — The failure-rate evidence base

#### F-W7-01 — The most-cited automation failure statistic ("30–50% of initial RPA projects fail") originates in one unsourced sentence of a 2016 EY marketing brochure, and its sample is explicitly selected on failure.

- **Evidence tier:** **C** (the statistic). **A** for the provenance determination — I read the
  originating document in full and the sentence is verbatim reproduced below.
- **Support:** EY, _Get ready for robots: Why planning makes the difference between success and
  disappointment_, © 2016 EYGM Limited, EYG no. 03746-164Gbl, author Chris Lamberton (EY UK)
  ([PDF](https://eyfs.ie/wp-content/uploads/2016/11/ey-get-ready-for-robots.pdf) — **read in full,
  12 pp**). Page 2, verbatim: _"We have delivered RPA projects across 20 countries and are often
  called upon to help companies when their first attempt failed. While RPA can transform the
  economics and service level of current manual operations, we have seen as many as 30 to 50% of
  initial RPA projects fail."_
  The document states no sample size, no time window, no definition of "fail," no counting rule,
  and no methodology of any kind. The preceding clause states the observation base directly: EY is
  "often called upon to help companies when their first attempt failed" — i.e. the population EY
  observes is conditioned on having already failed. The same document positions EY as "one of the
  largest RPA consultancies," and every one of its ten named failure causes maps to a service EY
  sells.
- **Date sensitivity:** The figure is from 2016 and has not been re-derived by EY or anyone else in
  the ten years since; it is now cited as though it were a standing industry rate. Treat the number
  as permanently stale, not as a 2026 measurement.
- **Confidence:** **High** that this is the origin and that it has no methodology. I traced ten
  downstream citations (FutureCIO, Pega, MetaSource, Flobotics, Xenith, EISMD, Axiant, and others)
  and every one either cites EY or cites a page that cites EY. No independent derivation exists.
- **Counter-evidence:** EY genuinely has large delivery volume across 20 countries, so the estimate
  is informed by real engagement exposure even if unmeasured — it is not fabricated, it is
  unquantified. And an anchored practitioner estimate is not worthless; it is just not a rate. I
  found no source that contradicts the 30–50% band with a better-measured band; the honest position
  is that no adequately measured band exists at all (see F-W7-05).

#### F-W7-02 — The "70% of change/reengineering efforts fail" figure was self-described as unscientific by its authors, disowned by Hammer within two years, and has no empirical basis.

- **Evidence tier:** **A** for the provenance chain (primary quotes from both books plus a
  peer-reviewed critique). **C** for the statistic itself.
- **Support:** Hammer & Champy, _Reengineering the Corporation_ (1993): _"Our unscientific estimate
  is that as many as 50 per cent to 70 per cent of the organizations that undertake a reengineering
  effort do not achieve the dramatic results they intended."_ Hammer, _The Reengineering Revolution_
  (1995): _"There is no inherent success or failure rate for reengineering"_ — adding that his
  observation had been "widely misrepresented and transmogrified and distorted into a normative
  statement." Mark Hughes (2011), _Journal of Change Management_: _"Whilst the existence of a
  popular narrative of 70 per cent organizational change failure is acknowledged, the absence of
  valid and reliable empirical evidence to support such a narrative is highlighted."_ Provenance
  traced and quoted at [StrategyU](https://strategyu.co/do-70-percent-of-change-initiatives-really-fail/)
  (**read in full**); corroborated by
  [Entrepreneur](https://www.entrepreneur.com/living/debunked-the-myth-that-70-percent-of-change-initiatives/354801)
  and [ACL Institute](https://aclinstitute.com/newsroom/70-change-fail/).
- **Date sensitivity:** None — this is a settled historical determination.
- **Confidence:** **High.** Two primary-source quotes and one peer-reviewed critique agree.
- **Counter-evidence:** None found. I looked specifically for a post-1995 study establishing a
  measured reengineering or change-programme failure rate and found none. Hughes' "nesting dolls"
  characterisation — each source citing another rather than data — matches what I observed
  independently while tracing F-W7-01.

#### F-W7-03 — The best-methodology automation data available shows the failure mode is not project failure but failure to scale: 3% of organisations reached 50+ bots; 63% missed their time-to-implement expectations.

- **Evidence tier:** **B** (vendor survey, but with disclosed n, disclosed method, disclosed
  question wording, and figures that cut against the vendor's commercial interest).
- **Support:** Deloitte, _The robots are ready. Are you? Untapped advantage in your digital
  workforce_ (2017 survey, published 2018)
  ([PDF](https://werkflo.com.au/assets/files/Deloitte-us-cons-global-rpa-survey-2018S.pdf) — **read
  in full for methodology, executive summary, and all headline figures, pp. 2–9**). Method, stated
  verbatim on the methodology page: _"In September 2017, Deloitte invited organizations globally to
  take part in an online survey on their use of RPA. We received responses from over 400 individuals
  across many industries with combined value of $1.8 trillion."_ Charts report n=424 for 2017 and
  n=143 for 2016. Figures:
  - **3%** are "already scaling it (50+ robots)"; 8% at 11–50; 12% at 6–10; 30% at 1–5 (PoC).
  - Payback: those piloting expect **9.3 months**; those who implemented or scaled achieved
    **11.5 months**.
  - **63% said their expectations of time to implement were not met**; **37% said their
    expectations of cost to implement were not met.**
  - **≥85%** reported RPA met or exceeded expectations on accuracy, timeliness, flexibility and
    compliance; **61%** on cost reduction.
- **Date sensitivity:** **Time-stamped 2017 survey / 2018 publication.** The scaling figure moved
  to 4% in the following wave — effectively flat. Do not present as a 2026 figure. The absolute
  numbers are stale; the _shape_ (works at pilot, doesn't scale) is the durable finding.
- **Confidence:** **High** on the internal figures (disclosed n and method); **medium** on
  generalisation, because respondents are self-selected large enterprises, not SMBs, and the
  survey is run by a firm that sells RPA implementation.
- **Counter-evidence:** The same survey is unambiguously positive on per-project outcomes — payback
  under 12 months and 85% meeting non-financial expectations. Anyone citing this survey as evidence
  that "RPA fails" is misreading it. It is evidence that RPA _works at small scale and stalls at
  large scale_, which is a different claim with different remediation.

#### F-W7-04 — In the only survey I found that asked directly, process standardisation was named the top challenge at the proof-of-concept and pilot stages of automation.

- **Evidence tier:** **B** (same survey, same caveats).
- **Support:** Deloitte 2018, p. 5, verbatim: _"Process standardization and change management are
  reported as the main challenges in the proof of concept and pilot stages of the RPA journey. As
  organizations move to pilot, implementation and scaling, integration with other IT systems and
  flexibility of the RPA solution are often quoted as challenges."_ (**read in full**)
- **Date sensitivity:** 2017 survey. Time-stamped.
- **Confidence:** **Medium.** This is the closest thing to direct survey evidence for the fix-first
  thesis that I found anywhere. But it is a ranked-challenge question, not an outcome measurement:
  it tells you what practitioners _report as hard_, not what _causes failure_. Reported difficulty
  and causal contribution are different quantities.
- **Counter-evidence:** The survey does not test whether organisations that standardised first got
  better outcomes than those that did not. It cannot, by design. That test does not exist in the
  literature (see Gaps).

#### F-W7-05 — Neither the RPA literature nor the Theory of Constraints literature contains published failure cases, so no failure rate can be computed from the academic record at all.

- **Evidence tier:** **A** (both reviews state the absence explicitly).
- **Support:**
  - Wewerka & Reichert, _Robotic Process Automation — A Systematic Literature Review and Assessment
    Framework_, Ulm University, arXiv:2012.11951 (**read in full, pp. 1–16**), §6 Discussion, item
    4, verbatim: _"the literature covers only successful RPA projects, leaving room for further
    research on failed projects."_ Item 5: _"Only a minority is critical towards RPA. One reason can
    be the novelty of RPA … due to which the technology is hyped and negative effects do not want to
    be seen."_ The review screened 1,510 results down to **63 publications** (15 case studies, 22
    methods, 2 reviews, 24 research papers), using Kitchenham's SLR protocol.
  - Mabin & Balderstone, _The performance of the theory of constraints methodology_, _International
    Journal of Operations & Production Management_ 23(6), 2003 — meta-analysis of **80+ TOC
    applications**. The review reports that **despite extensive searches, no reports of failures
    were found.**
    ([Emerald](https://www.emerald.com/ijopm/article-abstract/23/6/568/139893/The-performance-of-the-theory-of-constraints),
    [Semantic Scholar](https://www.semanticscholar.org/paper/The-performance-of-the-theory-of-constraints-and-of-Mabin-Balderstone/97c74e4a7282d55ea77bd04f51ccd5a4647585ff))
- **Date sensitivity:** The RPA SLR's search closed June 2020; the TOC review is 2003. Both are
  stale as inventories. The structural finding — that the denominator is missing — has not been
  fixed by anything I could find since.
- **Confidence:** **High.** Two independent systematic reviews, in two different methodological
  traditions, both report the same absence.
- **Counter-evidence:** Absence of published failures is not evidence of absence of failures; it is
  evidence of publication bias, which cuts _against_ both the reported success rates and any
  attempt to compute a failure rate. It does not, on its own, tell you the true rate is high. It
  tells you the true rate is unknown.

### Part 2 — What the evidence says about the automation gate

#### F-W7-06 — There is a converged, multi-source, peer-reviewed set of process-selection criteria for automation, and process standardisation and exception-handling volume are load-bearing members of it.

- **Evidence tier:** **A** (systematic review aggregating criteria across 63 publications, with
  per-criterion citation counts to primary papers).
- **Support:** Wewerka & Reichert 2020, §3.2 (**read in full**). Verbatim criteria as stated:
  - _"the process to be automated shall be standardised, run in a stable environment, and only
    require limited exception handling"_ (cited to 8 primary publications: P02, P06, P14, P28, P31,
    P46, P62, P63)
  - **Repetitiveness** — high transaction volume, most frequently mentioned criterion (11 primary
    publications)
  - **Complexity** — _"All publications agree that the lower the complexity, the better the process
    is suited for RPA"_
  - **High manual effort**, **duration of process execution**, and: _"the inputs and outputs are
    digital and structured"_, _"the process only requires a limited number of human interventions"_
  - The IEEE 2017 standard definition, quoted in the review, builds the gate into the definition
    itself: RPA uses _"business rules and predefined activity choreography"_ with _"human exception
    management."_
  - The review's Figure 2 gives the operative shape: on axes of _number of process variants_ (x) and
    _case frequency_ (y), low-variant/high-frequency work is RPA territory, and high-variant work
    _"can only be performed by humans."_
- **Date sensitivity:** Criteria are structural, not volatile. The tool landscape referenced (Blue
  Prism, UiPath) is 2019–2020 vintage and stale.
- **Confidence:** **High** that this is the field's consensus. **Medium** that it is _empirically
  validated_ rather than repeatedly asserted — the SLR aggregates what papers claim, and explicitly
  declined to apply quality-assessment criteria (§2.5: _"applying rigid quality assessment questions
  would probably exclude relevant publications. Therefore, we decide against the introduction of
  additional quality criteria."_). That is a real weakness: the consensus may be a citation cascade.
- **Counter-evidence:** The SLR itself records disagreement on volume predictability — P06 says
  processes with unpredictable peaks are _suited_ to RPA, P31 says volumes should be predictable.
  And P51 states the maximalist opposite of a selectivity gate: _"any activity that a person
  performs with mouse and keyboard can be carried out by a software robot."_

#### F-W7-07 — Two published methods make process maturity/standardisation a hard Step 1 gate that must pass before automation potential is even assessed; a third explicitly argues against automating the as-is process.

- **Evidence tier:** **B** (primary methods papers, reported via the SLR; I read the SLR's account,
  not the underlying papers).
- **Support:** Wewerka & Reichert 2020, §3.4 Analysis Stage (**read in full**):
  - **P39** — _"develops a four-step method to analyse a business process based on its criteria:
    first, to be eligible for RPA, the process has to be mature and standardised (Step 1). Step 2
    assesses the RPA potential … Step 3 evaluates the RPA relevance based on the volume of
    transactions and the degree of complexity."_ Maturity is a precondition, not a scoring factor.
  - **P22** — _"emphasises the importance of not automating the as-is process, but to optimise it
    before. Thus, the authors propose a framework for process re-engineering."_
  - **P57** — prioritises processes on _"execution frequency, execution time, degree of
    standardisation, stability (i.e., small number of exceptions in the process) failure rate, and
    automation rate."_ Note the explicit operationalisation of stability as **exception count**.
  - **P48** — technical criteria _"degree of rule-basedness, human intervention, digitalisation, and
    structuredness of data"_; potential criteria include _"number of process exceptions … and
    process maturity."_
  - **P20** — three-step: select on criteria → _"the process is modified, e.g., considering data
    standardisation"_ → then implement.
- **Date sensitivity:** Structural.
- **Confidence:** **Medium.** These are proposed methods, not validated ones. The SLR does not
  report that any of them was empirically tested against a control.
- **Counter-evidence:** These are a minority of the 63 publications. The SLR's own summary of the
  process-selection cluster (§6, item 3) does not mention maturity or prior redesign at all: _"Best
  suited for an RPA automation are repetitive, rule-based and complex business processes demanding
  for high manual efforts."_ The fix-first gate is present in the literature but is not its
  headline.

#### F-W7-08 — Automation tooling supports the operation phase far better than the analysis phase, so the diagnosis step is where tools help least.

- **Evidence tier:** **B** (mapping study, read via the SLR's summary of it).
- **Support:** Enriquez et al. 2020, systematic mapping of **14 commercial RPA tools** against **48
  functionalities** mapped to RPA lifecycle phases, as reported in Wewerka & Reichert 2020 §5:
  _"the Operation phase is covered by over 80% of the RPA tools, whereas support for the Analysis
  phase is below 15%."_
- **Date sensitivity:** **2020 tool landscape — stale by six years.** The direction (analysis is
  under-tooled relative to execution) may or may not still hold; process-mining vendors and LLM
  tooling have both moved into the analysis phase since. Flag for re-measurement.
- **Confidence:** **Medium-low** as a 2026 statement; **high** as a 2020 statement.
- **Counter-evidence:** The same SLR documents an active research push into exactly this gap —
  robotic process mining (P34–P37), UI-log-based routine discovery (P05, P15, P36), and SVM-based
  task classification (P38). If that research shipped, the 15% figure will have moved. I found no
  post-2020 re-measurement.

#### F-W7-09 — Process mining has a hard, cheaply checkable data prerequisite, and it is a real gate rather than a nice-to-have.

- **Evidence tier:** **A** for the requirement (it is definitional and stated identically across
  vendor documentation and the academic literature).
- **Support:** Fluxicon, _Process Mining Book_ 3.1, "Assess the Suitability of Your Data"
  ([link](https://fluxicon.com/book/read/datasuitability/) — **read in full**). Required:
  1. Structured tabular data (Excel/CSV/DB).
  2. A **case ID** column where _"the same case ID appears in multiple rows."_
  3. An **activity name** column whose value _"changes over time"_ for a given case.
  4. A **timestamp** with differing values across a case, or rows already sorted in occurrence order.

  Disqualifying conditions, verbatim: case IDs where every identifier _"appears just exactly once"_;
  an activity field that _"never changes over the course of a case"_; timestamps that don't _"change
  over time for the same case"_; and over-aggregated data with _"one event for each case"_ showing
  only _"end result or current status."_ Also: ERP and database systems organised around _"business
  objects rather than processes"_ require custom correlation work first.
  Corroborated academically: the minimum triple of case ID, timestamp and activity label is the
  standard definition (see e.g. [Extended Event Log, arXiv:2412.18012](https://arxiv.org/pdf/2412.18012)),
  and event-log imperfection taxonomies classify issues along type (incorrect / irrelevant /
  imprecise / missing) × entity (case, event, timestamp, resource, …).

- **Date sensitivity:** None — this is definitional.
- **Confidence:** **High.**
- **Counter-evidence:** None on the requirement itself. The counter-argument is practical: event
  logs can be _manufactured_ where they don't exist (screen/UI recording, EDF-style interactive
  event-log generation tools for SMEs). That converts a hard gate into a cost, but the cost is
  real and lands before any analysis begins.

#### F-W7-10 — For SMBs specifically, the event-log prerequisite is usually the binding constraint, and the literature names data access as the barrier.

- **Evidence tier:** **B** (peer-reviewed conference paper and related SME studies; I read
  abstract-level summaries and a paywalled chapter listing, not the full text).
- **Support:** Kipping et al., _Applying Process Mining in Small and Medium Sized IT Enterprises —
  Challenges and Guidelines_, BPM 2022
  ([Springer](https://link.springer.com/chapter/10.1007/978-3-031-16103-2_11) — paywalled;
  **abstract and summary only**). Reported challenges: a _"constraining data access barrier"_
  negatively affecting event-log availability; _"incomplete de jure processes and related systems"_;
  data-privacy concerns and distrust of cross-departmental event data; and the requirement that
  management _"shift manpower or hire experts."_ Corroborating: _EDF: An Interactive Tool for Event
  Log Generation for Enabling Process Mining in Small and Medium-sized Enterprises_ (2024) — the
  existence of a purpose-built SME event-log _generation_ tool is itself evidence that SMEs
  generally lack usable logs. General ERP position: event log data _"is typically not readily
  available in ERP systems, and instead must be extracted from different database tables using
  customized extraction scripts. Access to databases and detailed knowledge about the database
  schema is required, which is often not available."_
- **Date sensitivity:** 2022–2024. SaaS-native SMB stacks (which log more by default) may improve
  this over time; on-prem/spreadsheet/email-driven SMBs will not.
- **Confidence:** **Medium.** The direction is well supported; I have no quantified base rate for
  what fraction of SMBs have a minable event log. That number does not appear to exist.
- **Counter-evidence:** SMBs on a single modern SaaS system of record (e.g. one CRM or one PSA tool
  that stamps status transitions) can have a perfectly usable log with no extraction work. The
  barrier is a function of stack fragmentation, not of company size per se. I found no study that
  separates those two variables.

#### F-W7-11 — Theory of Constraints has the largest reported effect sizes of any methodology in this set, from a review that simultaneously reports finding zero failures — so the effect sizes are upper bounds, not estimates.

- **Evidence tier:** **B** (published meta-analysis in a peer-reviewed operations journal, but of a
  self-selected published-case population with acknowledged absence of negative cases).
- **Support:** Mabin & Balderstone 2003, IJOPM 23(6):568 — 80+ documented TOC applications with
  quantitative data. Reported means: **inventory −49%**, **lead/cycle time improved >60%** (a
  separately reported figure gives **flow time −63%**), **throughput +44%**, **financial performance
  improved >60%.** ([Emerald](https://www.emerald.com/ijopm/article-abstract/23/6/568/139893/The-performance-of-the-theory-of-constraints);
  book-length version: _The World of the Theory of Constraints_, Routledge.)
- **Date sensitivity:** 2003 review of 1990s cases. **Stale as a current estimate.**
- **Confidence:** **Low-to-medium** on the magnitudes (publication bias is severe and acknowledged);
  **high** that TOC's core structural claim is sound, because it is not an empirical claim at all —
  that a non-constraint's improvement cannot raise system throughput follows from the definition of
  a constraint and is reproducible in any queueing model. Goldratt's formulation: _"an hour saved at
  a non-bottleneck is a mirage."_
- **Counter-evidence:** The zero-failure finding is disqualifying for the effect sizes. Any honest
  reading is: TOC's _logic_ is the most defensible thing in this workstream; TOC's _numbers_ are the
  least defensible.

#### F-W7-12 — Value stream mapping's systematic-review evidence is directionally positive on time metrics and methodologically weak throughout: every included study was uncontrolled before/after.

- **Evidence tier:** **B** (PRISMA-conformant systematic review) reporting on **C-to-B** primary
  studies.
- **Support:** Sunder et al. / Forsberg et al., _Does Value Stream Mapping affect the structure,
  process, and outcome quality in care facilities? A systematic review_, _Systematic Reviews_ (2017)
  ([PMC5571664](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5571664/)) — 903 articles screened, 22
  met inclusion, 11 used for the research question. Conclusion: VSM has positive effects on the time
  dimension of process and outcome quality (waiting time, length of stay). Explicit limitation:
  _"All study designs were before and after studies without control, and methodologically
  sophisticated studies are missing."_ Manufacturing effect sizes vary enormously by context: lead
  time 89.50 h → 50.55 h in one automotive case; **37.14%** lead-time reduction in a heater-industry
  case; **5.3%** in car repair services.
- **Date sensitivity:** Structural. Case-level percentages are context-specific and not
  transferable.
- **Confidence:** **Medium.** VSM reliably produces _a shared picture of where time goes_. Whether
  the improvement is attributable to VSM rather than to the attention paid is untested — that is
  exactly what uncontrolled before/after cannot separate.
- **Counter-evidence:** The 5.3% car-repair result sits in the same literature as the 43% automotive
  result. A method whose reported effect ranges across an order of magnitude with no moderator
  analysis is not yet an estimator.

#### F-W7-13 — Job and role design is the only methodology in this set with a large-sample meta-analytic evidence base, and it is strong.

- **Evidence tier:** **A** (meta-analysis, top-tier journal, very large N).
- **Support:** Humphrey, Nahrgang & Morgeson (2007), _Integrating Motivational, Social, and
  Contextual Work Design Features: A Meta-Analytic Summary and Theoretical Extension of the Work
  Design Literature_, _Journal of Applied Psychology_ 92(5):1332–1356
  ([PDF](http://www.morgeson.com/downloads/humphrey_nahrgang_morgeson_2007.pdf)). **259 studies,
  219,625 participants.** 14 work characteristics explained on average **43% of variance** across 19
  worker attitudes and behaviours. Motivational characteristics explained 25% of variance in
  subjective performance, 34% in job satisfaction, 24% in organisational commitment. Social
  characteristics added incremental variance of 24% in turnover intentions and 40% in organisational
  commitment.
- **Date sensitivity:** 2007. Work-design meta-analyses are stable; the constructs have not been
  overturned. Low drift risk.
- **Confidence:** **High** for the association. **Medium** for causal direction — the corpus is
  dominated by cross-sectional self-report designs, which inflate common-method variance.
- **Counter-evidence:** Cross-sectional dominance and self-reported job characteristics are the
  standard critique of this literature. The variance explained is partly a measurement artefact of
  asking the same person about both their job and their satisfaction. The _social_ characteristics
  result (40% of commitment variance) is where this bias is most likely to bite.

#### F-W7-14 — Bainbridge's "ironies of automation" establishes a structural, non-obvious cost of automating a partially-understood process: the residue left to humans is by construction the hardest part, and human skill at it decays.

- **Evidence tier:** **A** (foundational peer-reviewed paper, 4,700+ citations, conceptually
  reproduced across four decades of human-factors research).
- **Support:** Lisanne Bainbridge, _Ironies of Automation_, _Automatica_ 19(6), 1983
  ([overview](https://en.wikipedia.org/wiki/Ironies_of_Automation),
  [human-factors treatment](https://humanfactors101.com/2020/05/24/the-ironies-of-automation/)).
  Core: _"By taking away the easy parts of [the] task, automation can make the difficult parts of
  the human operator's task more difficult."_ The designer who tries to eliminate the operator still
  leaves the operator the tasks the designer could not automate — by definition the hardest ones.
  Consequence: operators no longer practise the skills as routine work, so they need **more**
  training for rarer, more critical interventions, not less.
- **Date sensitivity:** None — 43 years old and reinforced rather than superseded.
- **Confidence:** **High** conceptually. **Low** quantitatively — Bainbridge gives no effect sizes,
  and I found no study quantifying skill decay in a business-process (as opposed to
  aviation/process-control) setting.
- **Counter-evidence:** The original context is safety-critical continuous-process control with
  rare, high-stakes interventions. Transfer to a five-person back office processing invoices is an
  inference, not a demonstrated result. The mechanism (residue is the hard part) transfers cleanly;
  the _severity_ may not.

### Part 3 — What the AI harness can and cannot do

#### F-W7-15 — Current LLMs produce syntactically and structurally competent process models but remain measurably behind humans on semantic correctness, and valid-output rates are poor enough to require a verification loop.

- **Evidence tier:** **A** (published benchmark with disclosed dataset, disclosed protocol, and
  8,925 generations).
- **Support:** _Assessing the Business Process Modeling Competences of Large Language Models_,
  arXiv:2601.21787v2 (**read in full**). **17 open-source LLMs** from Llama3, Qwen2.5, Qwen3,
  Falcon3, Phi4 and DeepSeek-R1 families, released April 2024 – April 2025, 0.5B–405B parameters,
  evaluated on **105 curated text→BPMN pairs**, five runs each at temperature 0.1 with one refinement
  attempt, **8,925 total generations**. Result: only **11 of 17** models produced enough valid output
  (≥30 valid BPMN files) to be analysable at all. Models were strong on syntactic and pragmatic
  quality (best near 0.8) and **notably weaker on semantic quality, where the paper states humans
  outperform LLMs**. Authors' conclusion: _"valid BPMN-XML generation remains a major challenge for
  current LLMs"_; LLMs show _"competitive potential"_ but the role is complementary, not
  replacement. A companion framework (BEF4LLM) defines **39 metrics** across syntactic, pragmatic,
  semantic and validity dimensions.
- **Date sensitivity:** **Highly volatile — models tested through April 2025, evaluated 2026.**
  Re-check within two quarters.
- **Confidence:** **High** for what was tested. **Low** for transfer to the operator's actual
  situation, for one decisive reason in the Counter-evidence field.
- **Counter-evidence:** **No frontier proprietary model was tested.** The benchmark is
  open-source-only, and the largest models tested top out at 405B open weights. The operator will be
  running a frontier commercial model, on which this benchmark is silent. Second: the benchmark
  measures text→BPMN transcription, where the process description is _given_. It measures nothing
  about eliciting the process in the first place, which is the actual hard part of diagnosis.

#### F-W7-16 — Discovery-interview volume has a real empirical anchor, and it is small: thematic saturation typically lands between 9 and 17 interviews, with metathemes visible by 6.

- **Evidence tier:** **A** (widely replicated methodological study plus subsequent saturation
  literature).
- **Support:** Guest, Bunce & Johnson (2006), _How Many Interviews Are Enough? An Experiment with
  Data Saturation and Variability_, _Field Methods_ 18(1)
  ([Sage](https://journals.sagepub.com/doi/10.1177/1525822X05279903)): analysing 60 interviews,
  _"saturation occurred within the first twelve interviews, although basic elements for metathemes
  were present as early as six."_ Subsequent work (Hennink et al.) distinguishes **code saturation
  at 9–17 interviews** from **meaning saturation at 16–24**. For elicitation specifically, Davis et
  al. (2006) systematic review finds **structured interviews among the most effective elicitation
  techniques**
  ([review](https://www.researchgate.net/publication/221222514_Effectiveness_of_Requirements_Elicitation_Techniques_Empirical_Results_Derived_from_a_Systematic_Review)).
- **Date sensitivity:** Structural methodological finding; low drift.
- **Confidence:** **High** for homogeneous populations and a narrow, well-defined topic — which is
  exactly the condition Guest studied (60 interviews, women in two African countries, one narrow
  health topic).
- **Counter-evidence:** The saturation numbers are conditioned on **homogeneity and narrow scope**.
  A small business with heterogeneous roles — owner, ops lead, bookkeeper, front-line staff — is a
  _stratified_ population, and saturation is per-stratum, not global. Transferring "12 interviews" to
  a cross-functional business diagnosis is an over-reach the source does not support. Also note the
  whole SMB may only _have_ 9–17 people, which collapses the sampling question into a census.

#### F-W7-17 — Hammer's original evidence for "don't pave the cow paths" is two self-reported consultant case studies, and it contains the only quantified head-to-head between automating-as-is and redesigning that I could find.

- **Evidence tier:** **A** for what the article says (primary source, read in full); **C** for the
  numbers as evidence, because they are consultant-reported single cases with no counterfactual.
- **Support:** Michael Hammer, _Reengineering Work: Don't Automate, Obliterate_, _Harvard Business
  Review_, July–August 1990, Reprint 90406
  ([PDF](https://folk.idi.ntnu.no/thomasos/paper/hammer_reengineering.pdf) — **read in full, 8 pp**).
  Disclosure printed in the article: Hammer is president of Hammer and Company, an IT consulting
  firm, and the article _"is based in part on work performed in association with the Index Group
  also a Cambridge-based consultancy."_ Key passages, verbatim:
  - _"It is time to stop paving the cow paths. Instead of embedding outdated processes in silicon
    and software, we should obliterate them and start over."_
  - **The head-to-head, Ford accounts payable:** North America employed _"more than 500 people."_
    _"Management thought that by rationalizing processes and installing new computer systems, it
    could reduce the head count by some 20%."_ After radical redesign: _"Ford has achieved a 75%
    reduction in head count, not the 20% it would have gotten with a conventional program."_ The
    trigger for the reframe was an external benchmark: Mazda's equivalent function had **5 people**.
  - **The touch-time datum, Mutual Benefit Life:** applications went through _"as many as 30 discrete
    steps, spanning 5 departments and involving 19 people,"_ best case 24 hours, typical 5–25 days,
    _"most of the time spent passing information from one department to the next."_ And, crucially:
    _"Another insurer estimated that while an application spent 22 days in process, it was actually
    worked on for just 17 minutes."_ After redesign: _"as little as four hours,"_ average 2–5 days,
    100 field positions eliminated, case managers handling _"more than twice the volume."_
  - **The stated principle:** _"It should use information technology not to automate an existing
    process but to enable a new one."_
- **Date sensitivity:** 1990. The cases are historical; the diagnostic ratio is not.
- **Confidence:** **High** that this is what the article says. **Low** that 20%-vs-75% generalises —
  n=1, self-reported, no control, and the 20% is a _projection_ that was never run, not a measured
  alternative arm.
- **Counter-evidence:** Hammer's 1990 article states **no failure rate at all** — the 70% figure
  people attribute to him came three years later, in the book, self-labelled unscientific (F-W7-02).
  The article also concedes the enabling condition that undermines portability to a small business:
  _"one factor that is necessary for reengineering to succeed: executive leadership with real
  vision"_ and _"Reengineering cannot be planned meticulously and accomplished in small and cautious
  steps. It's an all-or-nothing proposition."_ Whatever else that is, it is not an incremental method
  that a solo consultant can time-box.

#### F-W7-18 — The direct opposite of fix-first is advocated by sources with equal delivery credibility, and it is not a fringe position.

- **Evidence tier:** **C** (consultancy guidance) to **B** (peer-reviewed characterisation of RPA as
  deliberately non-invasive).
- **Support:**
  - EY 2016 (**read in full**), issue 7, verbatim: _"The best way to view RPA initially is as the
    ultimate 'helper,' carrying out the basic work in a process and enabling humans to do more.
    Automating 70% of a process that is the lowest-value, and leaving the high-value 30% to humans is
    a good initial target. It's always possible to back and optimize the process later."_ Issue 6:
    _"RPA rarely changes existing systems."_ Issue 5 gives the sizing gate: _"Low or medium
    complexity processes or sub-processes are the best initial target for RPA, with a minimum of 0.5
    FTE savings."_
  - Wewerka & Reichert 2020: the SLR records **non-invasiveness** as a defining RPA property (P06,
    P46, P51) — _"RPA does not change the underlying application systems"_ — and notes the
    lightweight/heavyweight IT distinction in which RPA is deliberately an outside-in overlay.
    Simultaneously it records the critique: P19 characterises RPA solutions as **workarounds**; P02
    and P18 call RPA a **temporary solution**.
- **Date sensitivity:** EY 2016 is stale as guidance; the structural argument is not.
- **Confidence:** **Medium.** This is a real, coherent, practitioner-backed position: automate the
  standardised majority of a messy process cheaply, capture the payback inside 12 months, and use the
  proceeds and the resulting event data to fund the redesign.
- **Counter-evidence:** It is advocated by a firm selling RPA delivery, and it is precisely the
  behaviour that produces the Deloitte pattern in F-W7-03 — bots that work at pilot and never scale.
  The two findings are consistent with each other: automate-first _works_, and then stops working.

#### F-W7-19 — "Standardise before you automate" is near-universally repeated and, as far as I can establish, has never been tested.

- **Evidence tier:** **C** — and this finding is that there is no better tier available.
- **Support / non-support:** I searched specifically for measured outcomes comparing
  standardise-then-automate against automate-as-is. Every result was a consultancy or vendor blog:
  [Auxiliobits](https://www.auxiliobits.com/blog/process-standardization-before-automation-why-its-critical/),
  [K&B Global](https://kandbglobal.com/2026/06/13/process-standardization-before-automation/),
  [Reliability Academy](https://reliabilityacademy.com/articles/general/standardise-process-before-automating),
  [MoldMaking Technology](https://www.moldmakingtechnology.com/articles/standardize-before-you-automate),
  [Mapex](https://mapex.io/en/news/process-standardization/). Every one of them sells either
  automation implementation or standardisation consulting. The strongest thing any of them offers is
  an unattributed anecdote ("the cost of harmonizing intake workflows after the fact exceeded the
  original automation budget"). No n, no source, no comparison group.
  The nearest thing to an authoritative statement of the principle in a non-selling source is the
  Lean tradition's prerequisite claim — Lean Enterprise Institute's lexicon
  ([link](https://www.lean.org/lexicon-terms/kaizen/), **read in full**) states standardised work as
  a precondition for improvement, quoting Taiichi Ohno: _"There can be no kaizen without a
  standard."_ That is an assertion of method, not a measured result, and it is about _improvement_,
  not about _automation_.
- **Date sensitivity:** None.
- **Confidence:** **High** that the maxim is unevidenced in the sense of having no controlled study.
  **Medium** that it is nonetheless correct — the mechanism is plausible and F-W7-04, F-W7-06 and
  F-W7-07 all point the same way without closing the loop.
- **Counter-evidence:** F-W7-18. Also: the maxim is unfalsifiable as usually stated, because
  "standardised enough" is never operationalised. The one source that does operationalise it —
  P57 in the SLR, defining stability as **small number of exceptions** — is the version worth
  keeping.

#### F-W7-20 — The 2025–2026 generation of AI-automation failure statistics repeats the 2016 pattern: forecast and contested figures circulating as measurements.

- **Evidence tier:** **C** for both figures; **A/B** for the fact of their contestation.
- **Support:**
  - Gartner, press release 2025-06-25: _"Over 40% of agentic AI projects will be canceled by the end
    of 2027, due to escalating costs, unclear business value or inadequate risk controls"_
    ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)).
    This is a **prediction**, not an observation, and is routinely re-reported as though it were
    measured. Gartner's related 2026 Hype Cycle data point — 17% of organisations have deployed AI
    agents, >60% expect to within two years — is a survey figure and is the more usable number.
  - MIT NANDA, _The GenAI Divide: State of AI in Business 2025_ — the "95% of GenAI pilots fail"
    figure. Basis: 52 executive interviews, 153 survey responses, 300 public deployments. Criticised
    for methodological fragility and, materially, for an undisclosed conflict: the report's
    recommended remedy is the NANDA project's own offering
    ([Futuriom](https://www.futuriom.com/articles/news/why-we-dont-believe-mit-nandas-werid-ai-study/2025/08)).
- **Date sensitivity:** **Highly volatile.** Gartner's prediction window closes end-2027; expect a
  measured retrospective then, and treat everything before it as forecast.
- **Confidence:** **High** that these are not measurements of automation-over-dysfunction outcomes.
- **Counter-evidence:** Gartner's failure _reasons_ — escalating cost, unclear business value,
  inadequate risk controls — are consistent with the Deloitte-observed pattern and with EY's
  business-case findings. The causal story may well be right even though the number is a forecast.

#### F-W7-21 — SIPOC, RACI, and MECE/issue trees: no reliable evidence found.

- **Evidence tier:** n/a — this is a negative finding.
- **Support:** I searched for empirical validation of SIPOC as a diagnostic instrument, for measured
  outcomes from RACI or decision-rights mapping, and for evidence that MECE issue-tree structuring
  improves diagnostic accuracy. I found: instructional material, certification-body content, and
  consulting-firm advocacy. I found no study measuring whether producing a SIPOC changes any
  downstream outcome; no study measuring whether a RACI matrix reduces handoff delay or rework; and
  no study of issue-tree structuring outside general judgement-and-decision-making research that
  does not use the MECE construct. The nearest adjacent evidence is Bain's decision-rights work
  (Rogers & Blenko, _"Who Has the D?"_, HBR January 2006
  ([HBR](https://hbr.org/2006/01/who-has-the-d-how-clear-decision-roles-enhance-organizational-performance)))
  — I attempted the full text and it is paywalled; I could not verify the survey n or the
  decision-effectiveness/financial-performance correlation the firm cites, so I am not reporting it
  as evidence.
- **What would settle it:** a randomised or matched comparison in which teams diagnose the same
  process with and without the artefact, measured on a downstream outcome (time to correct root
  cause; rework rate after redesign). Nothing of the kind appears to exist for any of the three.
- **Confidence:** **High** that the evidence is absent. **Low** confidence that the tools are
  worthless — absence of evidence here is genuinely uninformative, because these are cheap
  communication artefacts whose value is coordination, and coordination artefacts are rarely studied.
- **Counter-evidence:** SIPOC and RACI are embedded in Six Sigma and PMI bodies of knowledge that
  themselves rest on the Lean/Six Sigma evidence base; someone could argue the parent methodology's
  evidence transfers. It does not — none of the Lean Six Sigma reviews isolate the contribution of
  any single tool.

---

## Direct Answers

### Q1 — What test tells you a process must be fixed before it is automated?

**No single published, validated test exists.** Nobody has run the study. What does exist is a set
of individually-evidenced gates that can be assembled into a rule. Below, each gate is tagged with
whether it is _stated in a source_ or _constructed by me from cited evidence_. The construction is
my inference; the components are not.

Run in order. Any gate that fails means the answer to "automate now?" is no.

| #   | Gate                                 | Test                                                                                                                         | Status                                 | Evidence                                                                                                                                                                                                                        |
| --- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Constraint**                       | Is the step you propose to automate the system constraint?                                                                   | **Constructed** from TOC               | Throughput cannot rise by improving a non-constraint — true by definition of a constraint, reproducible in any queueing model. Effect sizes: F-W7-11                                                                            |
| 2   | **Touch-time ratio**                 | Divide hands-on work time by elapsed time. If it is tiny, the process is queueing- and authority-bound, not execution-bound. | **Constructed**; the _datum_ is stated | Hammer 1990: an application spent **22 days in process, worked on for 17 minutes** (≈0.05%). Automating execution speed cannot move a 0.05% denominator. F-W7-17                                                                |
| 3   | **Exception rate / standardisation** | What fraction of volume follows the dominant path, and can you state the rule that covers it?                                | **Stated**                             | RPA literature converges: process must be _"standardised, run in a stable environment, and only require limited exception handling"_ (8 primary papers). P57 operationalises stability as **exception count**. F-W7-06, F-W7-07 |
| 4   | **Variant count**                    | Plot process variants against case frequency. High-variant work is human/BPM territory, not automation territory.            | **Stated**                             | Wewerka & Reichert Fig. 2. F-W7-06                                                                                                                                                                                              |
| 5   | **Measurability**                    | Does an event log exist — recurring case ID, activity that changes, timestamp that varies?                                   | **Stated**                             | Fluxicon data-suitability criteria. If this fails, gates 1–4 cannot be answered from data and you are relying on interviews, which is a _weaker but not invalid_ basis. F-W7-09, F-W7-10                                        |
| 6   | **Residue**                          | After automation, what is left for the human, and is anyone trained for it?                                                  | **Constructed** from Bainbridge        | The residue is by construction the hardest part of the job, and routine practice at it disappears. F-W7-14                                                                                                                      |

**The single sharpest test, if only one can be run: Gate 2.** It requires no event log, no tooling
and no methodology training — a stopwatch and one walk-through gives you touch time, and any
timestamped record gives elapsed time. It discriminates directly between the two failure modes:
a high touch-time ratio means work is genuinely slow and automation may help; a low ratio means the
delay lives in queues, handoffs and approvals, and automating the work steps will change nothing the
client can perceive. Hammer's 22-days-vs-17-minutes is the canonical instance, and the ratio is
falsifiable in a way that "is the process broken?" is not.

**What is _not_ an evidence-based test, despite being universally recommended:** "is the process
standardised?" asked qualitatively. It is unfalsifiable until you replace it with a number, and the
only numeric version in the literature is P57's exception count. **No source anywhere gives a
threshold** — no "automate if ≥X% of cases follow the happy path." I looked; that number does not
exist. EY's 70/30 heuristic (F-W7-18) is the closest thing, and it is a target for how much of a
process to automate, not a gate for whether to.

### Q2 — What does the evidence say about the failure rate and cost of automating a broken process?

**There is no sound measured failure rate for automating a broken process. None. The question has
not been studied.** Below is every circulated figure I could trace, with its actual provenance.

| Figure                                                                                                                        | Actual provenance                                                                                                                                                                                                                                          | Tier              | Verdict                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------- |
| **"30–50% of initial RPA projects fail"**                                                                                     | One sentence, 2016 EY marketing brochure. No n, no method, no definition of failure. Population explicitly selected on failure ("often called upon to help companies when their first attempt failed"). Author sells RPA remediation.                      | **C**             | Not a rate. An anchored guess.                                                      |
| **"70% of change/reengineering fails"**                                                                                       | Hammer & Champy 1993, self-labelled _"our unscientific estimate"_ of 50–70%. Hammer disowned it in 1995: _"There is no inherent success or failure rate for reengineering."_ Hughes (2011) found no empirical basis in any of the five most-cited sources. | **C**             | Disowned by its own author. Do not use.                                             |
| **"40% of agentic AI projects cancelled by end 2027"**                                                                        | Gartner press release, 2025-06-25. A **forecast**.                                                                                                                                                                                                         | **C as evidence** | Not a measurement. Re-check after end-2027.                                         |
| **"95% of GenAI pilots fail"**                                                                                                | MIT NANDA 2025: 52 interviews, 153 survey responses, 300 public deployments. Methodology contested; undisclosed conflict of interest (report's remedy is NANDA's own $250k offering).                                                                      | **C**             | Contested. Do not cite as fact.                                                     |
| **3% scaled to 50+ bots; 63% missed time expectations; 37% missed cost expectations; payback 11.5 mo actual vs 9.3 expected** | Deloitte 2017 online survey, **n=424**, disclosed method, disclosed question wording.                                                                                                                                                                      | **B**             | **The only defensible numbers in this table.** Time-stamped 2017.                   |
| **20% (automate as-is) vs 75% (redesign) headcount reduction**                                                                | Hammer 1990, Ford accounts payable. n=1, consultant-reported, and the 20% is a _projection never executed_, not a measured control arm.                                                                                                                    | **C**             | The only quantified head-to-head that exists, and it is one case from 36 years ago. |

**Three things can be said with confidence:**

1. **The academic denominator does not exist.** Wewerka & Reichert, having screened 1,510 papers to
   63: _"the literature covers only successful RPA projects, leaving room for further research on
   failed projects."_ Mabin & Balderstone, across 80+ TOC cases: no failure reports found despite
   extensive searches. You cannot compute a failure rate from a literature that has systematically
   excluded failures — and this is true of _both_ the automation literature and the
   process-improvement literature, which means neither side of the fix-first debate can appeal to
   outcome data.

2. **The observed failure mode is not project failure — it is arrested scaling.** Deloitte's n=424
   shows automation projects _succeeding_ individually (≥85% met or exceeded non-financial
   expectations, payback under 12 months) while almost never propagating (3% at 50+ bots). The
   costly failure is not a bot that doesn't work. It is a portfolio of bots that each work, each
   encode a different local variant of a process nobody standardised, and collectively cannot be
   extended or maintained. That is the concrete form "automating a broken process" actually takes,
   and it is compatible with every project in the portfolio having passed its own business case.

3. **On cost, the only quantified figure is about delivery-method error, not process brokenness.**
   EY's "multiplier effect" table gives a worked scenario: a simple data-cleanse automation that
   should take **2–4 weeks** takes **10–15 weeks** when three common issues co-occur — the paper
   summarises this as duration increasing _"four-or five-fold."_ That is C-tier, illustrative rather
   than measured, and — importantly — its three issues are wrong delivery methodology, under-skilled
   staff, and over-automating; none of them is "the underlying process was broken." **I found no
   quantification anywhere of the cost of automating a broken process specifically.**

---

## Methodology Assessment

For each: what it produces, duration at SMB scale, how much an AI harness can genuinely do unaided,
and where a human must be physically present.

**Duration figures carry a health warning.** Except where marked, timeboxes below are practitioner
convention, not measured data — I found no study measuring how long any of these takes at SMB scale.
The one exception is the kaizen event, whose five-day box is a stated convention of the Lean
Enterprise Institute (**A** for the convention, not for its optimality).

| Method                             | Produces                                                                                   | SMB duration                                                                | AI unaided                                                                                                                                                               | Human must be in the room for                                                                                                  | Evidence on the method itself                                                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Theory of Constraints**          | Identification of the single binding constraint; a subordination plan                      | 1–3 days to locate the constraint if flow data exists; weeks if not         | **Low.** AI can compute where queues accumulate _given_ data. It cannot see the informal constraint (one person who approves everything, one licence, one relationship). | Observing where work actually waits; the constraint is usually social and undocumented                                         | Logic is definitional and sound (**A**); reported effect sizes are from a zero-failure literature (**B**, upper bounds) — F-W7-11                                                                     |
| **Value stream mapping**           | Current-state map with touch time vs elapsed time per step; value-add ratio                | 2–5 days including the walk (kaizen-event convention)                       | **Medium-low.** AI can draft the map from an interview transcript and compute ratios. It cannot walk the floor.                                                          | The walk itself. The map's value is that people who do the work agree on it in one room — a consensus artefact, not a document | Systematic review positive on time dimensions; **all included studies uncontrolled before/after** (**B**) — F-W7-12                                                                                   |
| **DMAIC / Lean Six Sigma**         | Defined problem, baseline measurement, root cause, controlled change, holding mechanism    | Weeks to months; disproportionate ceremony below ~20 staff                  | **Medium** on Measure/Analyse if data exists; **low** on Define and Control                                                                                              | Define (framing what counts as a defect) and Control (whether the standard survives contact)                                   | Many systematic reviews, mostly healthcare, mostly uncontrolled; reviews repeatedly note _"a lack of empirical evidence"_ (**B/C**)                                                                   |
| **BPMN modelling**                 | Formal, unambiguous process model                                                          | Hours to days once the process is known                                     | **High** for transcription — benchmarked. **Not** for elicitation.                                                                                                       | Nowhere, once the description exists. The prerequisite description is the human part.                                          | Benchmarked: 17 open-source LLMs, 105 pairs, 8,925 generations; strong syntactically, **humans still better semantically**, validity a major challenge (**A**) — F-W7-15                              |
| **Process mining**                 | Discovered as-is model, variant frequencies, bottleneck and rework loops, conformance gaps | 1–2 days if a clean log exists; **weeks to indefinite** if it must be built | **High** _conditional on a log_. Zero without one.                                                                                                                       | Interpreting whether a discovered variant is a defect or a legitimate case type                                                | Requirement is definitional (**A**); SME data-access barrier is documented (**B**); **the log is a hard gate most SMBs fail** — F-W7-09, F-W7-10                                                      |
| **SIPOC**                          | One-page scope boundary: suppliers, inputs, process, outputs, customers                    | 1–2 hours                                                                   | **High** as a draft; it is a structured summary                                                                                                                          | Validating that the named customer is the real customer                                                                        | **No reliable evidence found** — F-W7-21                                                                                                                                                              |
| **RACI / decision-rights mapping** | Explicit map of who decides, who is consulted, where approval queues form                  | 0.5–1 day                                                                   | **Medium.** AI can build the matrix from interviews and flag conflicts. It cannot get people to concede authority.                                                       | The conversation where someone loses a decision right. This is the part that fails, and it fails in person.                    | **No reliable evidence found** for RACI specifically; Bain's decision-rights survey data is paywalled and unverified — F-W7-21                                                                        |
| **Issue trees / MECE**             | Decomposed problem structure with testable branches                                        | Hours                                                                       | **High.** This is close to a pure structured-generation task.                                                                                                            | Nowhere; but AI-generated trees inherit the framing they were given, so the framing must be human-checked                      | **No reliable evidence found** — F-W7-21                                                                                                                                                              |
| **Discovery interviews**           | The undocumented process, the workarounds, the informal constraint                         | 45–90 min each; saturation ~9–17 for a homogeneous group                    | **Low.** AI can generate protocols, code transcripts, and flag contradictions across interviews — that last one is genuinely valuable. It cannot conduct the interview.  | The interview. What matters is disclosed only after trust, and often only off-topic.                                           | Saturation quantified (**A**); structured interviews rated among the most effective elicitation techniques (**A**) — F-W7-16. Caveat: saturation numbers assume homogeneity; SMB roles are stratified |
| **Job / role design**              | Redesigned roles: task variety, autonomy, feedback, whole-task ownership                   | Days to design; months to embed                                             | **Medium** for design against known constructs; **none** for the political reality                                                                                       | Any conversation about who owns what after automation removes the routine work                                                 | **The strongest evidence base in this workstream:** 259 studies, 219,625 participants, 14 characteristics explain ~43% of variance across 19 outcomes (**A**) — F-W7-13                               |

**Cross-cutting capability finding:** as of the last measurement I could find (2020), automation
tooling covered the operation phase at >80% and the analysis phase at **<15%** — the diagnosis step
is the least tool-supported part of the pipeline (F-W7-08). That figure is six years stale and the
gap is exactly where LLM tooling has since been pushed, so it should be re-measured rather than
relied upon.

---

## Gaps

Specific things I could not establish, and what would settle each.

1. **No study compares standardise-then-automate against automate-as-is.** This is the central
   question of the workstream and it has no experimental or quasi-experimental answer. Every source
   advocating fix-first is selling either diagnosis or implementation. What would settle it: a
   matched-pair or stepped-wedge design across comparable processes, measuring 24-month total cost
   of ownership and rework rate, not go-live date.

2. **No threshold exists for "standardised enough."** The literature says "limited exception
   handling" and "small number of exceptions" and never gives a number. What would settle it: a
   dose-response study of exception rate against automation maintenance cost. Until it exists, any
   percentage a consultant quotes for this is invented.

3. **No base rate for SMB event-log availability.** The SME process-mining literature says data
   access is a barrier; nobody reports what fraction of small businesses actually have a minable log,
   or how that varies with stack fragmentation versus headcount. What would settle it: a survey of
   n≥200 SMBs auditing systems of record against the four Fluxicon criteria.

4. **The failure denominator is structurally missing.** Two independent systematic reviews report
   that failures are simply not published — in RPA and in TOC. Any failure rate computed from the
   academic literature is uncomputable in principle. What would settle it: registry-style reporting
   of automation initiatives at inception rather than at publication.

5. **No SMB-scale timing data for any methodology here.** Every duration in the table above is
   convention. What would settle it: engagement-level time tracking published against process
   complexity — which no consultancy has commercial incentive to publish.

6. **No frontier proprietary model has been benchmarked on process modelling.** The one rigorous
   benchmark tested open-source models only, through April 2025. The operator will not be using
   those models. What would settle it: running the same 105-pair BPMN benchmark against current
   frontier models — this is cheap and reproducible, and the protocol is published.

7. **No benchmark exists for the harder half of the task — AI-assisted process _elicitation_.**
   Everything measured to date assumes the process description is given. Nothing measures whether an
   AI can extract a correct process description from raw interview transcripts, emails, and system
   exports. What would settle it: a benchmark with ground-truth processes and realistic
   noisy-artefact inputs.

8. **RACI, SIPOC and MECE have no outcome evidence of any kind.** Not weak evidence — none found.
   See F-W7-21.

9. **Bain's decision-rights survey data could not be verified.** The HBR source is paywalled; I
   could not confirm the sample size or the claimed correlation between decision effectiveness and
   financial performance, so it is excluded rather than reported. Access to the full article or the
   underlying Bain research would settle it.

10. **The 22-days/17-minutes touch-time ratio has no distribution behind it.** It is one insurer,
    reported second-hand by Hammer in 1990. I could find no study establishing typical touch-time
    ratios for administrative processes, which would be needed to know what counts as an alarming
    ratio. What would settle it: process-mining datasets published with touch-time and elapsed-time
    both instrumented.

---

## Implications for the Operator

_My inferences. Not findings. Phase C does the reasoning._

- The strongest defensible position is narrower and more useful than "fix the process first." It is:
  **automation of a step that is not the constraint, or whose elapsed time is dominated by queueing,
  cannot produce a benefit the client will perceive — regardless of how well the automation works.**
  That is arguable from first principles, survives the publication-bias problem, and is falsifiable
  on the client's own numbers.
- Gate 2 (touch-time ratio) is the cheapest instrument here and probably the most commercially
  valuable. It costs one walk-through, produces a single number, and reframes an engagement from
  "build me a bot" to "your work is waiting, not running" using the client's own data. It requires
  no event log, which matters because most SMBs will fail Gate 5.
- The event-log gate is the practical fork in engagement design. Log present → process mining is
  fast, AI-heavy, and largely delegable. Log absent → the engagement is interview-driven, human-time
  dominated, and its cost is set by the operator's calendar, not by tooling. These are two different
  products with two different cost structures and should probably not be sold as one.
- Where AI genuinely earns its place in diagnosis: transcript coding, cross-interview contradiction
  detection, BPMN transcription from an agreed description, and issue-tree generation. Where it does
  not: the walk, the interview, and any conversation in which someone gives up a decision right.
  The review-capacity constraint bites less here than in code work, because the volume of artefacts
  is small — but the _human-presence_ constraint bites much harder, and it does not parallelise at
  all. Diagnosis engagements cannot be run three-at-a-time the way worktrees can.
- Job and role design is the most evidence-backed methodology in this set and the one least likely
  to be in a technical consultant's default kit. Bainbridge's residue argument and the work-design
  meta-analysis point at the same thing: the question "what is this person's job after the bot ships"
  is both the best-evidenced and the most commonly skipped part of an automation engagement.
- Every widely-quoted automation failure statistic is unusable in client-facing material. Citing
  "30–50% of RPA projects fail" to a client who later traces it to a 2016 EY brochure is a
  credibility loss, not a persuasion win. The Deloitte n=424 figures are the only ones that survive
  a client's own due diligence — and they say something more interesting anyway.
- **Client-safe flag:** process mining requires exporting operational event data — which for
  healthcare, legal, or financial clients means PHI, privileged material, or regulated financial
  records leaving their system of record and passing through a consultant's tooling and possibly a
  third-party model API. The SME process-mining literature already records data-privacy concerns and
  distrust of cross-departmental event data as adoption barriers. Any productised process-mining
  offer needs a data-handling answer before it is sold, not after.

---

## Sources

**Read in full** (8):

1. **Michael Hammer, _Reengineering Work: Don't Automate, Obliterate_, HBR July–August 1990, Reprint
   90406** — [PDF](https://folk.idi.ntnu.no/thomasos/paper/hammer_reengineering.pdf). **Tier A** as a
   primary source for what Hammer actually wrote; **C** for its case numbers as evidence. Trusted
   because it is the primary document and it discloses its own consulting interest. Distrusted for
   generalisation: two self-reported cases, no controls, and the article contains no failure rate at
   all — contrary to what is widely attributed to it.
2. **EY, _Get ready for robots: Why planning makes the difference between success and
   disappointment_, © 2016 EYGM, author Chris Lamberton** —
   [PDF](https://eyfs.ie/wp-content/uploads/2016/11/ey-get-ready-for-robots.pdf). **Tier C.** Read in
   full specifically to establish provenance of the 30–50% figure. Distrusted as evidence: no
   methodology, sample selected on failure, and every diagnosis maps to a billable service. Trusted
   as an artefact: it is unambiguously the origin of the industry's most-repeated statistic.
3. **Wewerka & Reichert, _Robotic Process Automation — A Systematic Literature Review and Assessment
   Framework_, Ulm University, arXiv:2012.11951 (Dec 2020)** —
   [arXiv](https://arxiv.org/abs/2012.11951). **Tier A** for method (Kitchenham protocol, 1,510 → 63
   publications, documented inclusion/exclusion). Read pp. 1–16 (full body). Trusted: transparent
   method, and it reports findings against the field's interest (zero failure cases, hype bias).
   Distrusted on one point it discloses itself — §2.5 declined to apply quality-assessment criteria,
   so the aggregated criteria may be a citation cascade rather than independent findings.
4. **Deloitte, _The robots are ready. Are you? Untapped advantage in your digital workforce_ (2017
   survey, n=424; published 2018)** —
   [PDF](https://werkflo.com.au/assets/files/Deloitte-us-cons-global-rpa-survey-2018S.pdf). **Tier
   B.** Read pp. 2–9 in full. Trusted because n, method, question wording and per-chart sample sizes
   are all disclosed, and because several headline figures cut against the publisher's commercial
   interest. Distrusted for self-selected large-enterprise respondents and a publisher who sells RPA
   implementation.
5. **_Assessing the Business Process Modeling Competences of Large Language Models_,
   arXiv:2601.21787v2** — [arXiv](https://arxiv.org/html/2601.21787v2). **Tier A.** Trusted:
   disclosed dataset (105 pairs), disclosed protocol (5 runs, temp 0.1), 8,925 generations, and
   negative results reported. Distrusted for scope: **open-source models only**, none frontier, and
   it measures transcription rather than elicitation.
6. **Fluxicon, _Process Mining Book_ 3.1, "Assess the Suitability of Your Data"** —
   [link](https://fluxicon.com/book/read/datasuitability/). **Tier A** for the data requirement
   (definitional and matched by the academic literature). Vendor-authored, but the content is a set
   of disqualifying conditions that _reduce_ the vendor's addressable market — a source arguing
   against its own interest.
7. **StrategyU, _Do 70% of change initiatives really fail?_** —
   [link](https://strategyu.co/do-70-percent-of-change-initiatives-really-fail/). **Tier B** as a
   provenance trace; the primary quotes it reproduces (Hammer & Champy 1993, Hammer 1995, Hughes 2011) are **Tier A**. Trusted because it quotes primaries verbatim and its conclusion is
   corroborated independently by Entrepreneur and ACL Institute.
8. **Lean Enterprise Institute, Lean Lexicon — kaizen** —
   [link](https://www.lean.org/lexicon-terms/kaizen/). **Tier B** for the five-day kaizen-event
   convention and the standardised-work-as-prerequisite doctrine. Trusted as the authoritative
   statement of Lean doctrine. Distrusted as evidence — it states method, not measured outcome.

**Sampled / abstract-level** (23, principal ones listed):

9. Mabin & Balderstone (2003), _The performance of the theory of constraints methodology_, IJOPM
   23(6):568 — [Emerald](https://www.emerald.com/ijopm/article-abstract/23/6/568/139893/The-performance-of-the-theory-of-constraints).
   **Tier B.** Trusted for the transparency of its zero-failure disclosure; distrusted for the effect
   sizes that disclosure invalidates as estimates.
10. Humphrey, Nahrgang & Morgeson (2007), _JAP_ 92(5):1332–1356 —
    [PDF](http://www.morgeson.com/downloads/humphrey_nahrgang_morgeson_2007.pdf). **Tier A.** The
    strongest evidence base cited anywhere in this file. Standard caveat: cross-sectional,
    self-report, common-method variance.
11. Guest, Bunce & Johnson (2006), _How Many Interviews Are Enough?_, _Field Methods_ 18(1) —
    [Sage](https://journals.sagepub.com/doi/10.1177/1525822X05279903). **Tier A**, scoped to
    homogeneous populations and narrow topics.
12. Systematic review of VSM in care facilities, _Systematic Reviews_ (2017) —
    [PMC5571664](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5571664/). **Tier B** review of **C**
    primaries; trusted for candidly reporting that all included designs were uncontrolled.
13. Bainbridge (1983), _Ironies of Automation_, _Automatica_ 19(6) —
    [overview](https://en.wikipedia.org/wiki/Ironies_of_Automation),
    [human-factors treatment](https://humanfactors101.com/2020/05/24/the-ironies-of-automation/).
    **Tier A** conceptually; 4,700+ citations. Original context is safety-critical control, not
    back-office process.
14. Kipping et al. (2022), _Applying Process Mining in Small and Medium Sized IT Enterprises_, BPM
    2022 — [Springer](https://link.springer.com/chapter/10.1007/978-3-031-16103-2_11). **Tier B**,
    paywalled; abstract and secondary summary only.
15. Gartner press release, 2025-06-25, agentic AI cancellations —
    [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027).
    **Tier C as evidence** — a forecast, routinely mis-reported as measurement.
16. Futuriom critique of MIT NANDA _GenAI Divide_ —
    [link](https://www.futuriom.com/articles/news/why-we-dont-believe-mit-nandas-werid-ai-study/2025/08).
    **Tier B** as a methodological critique; the underlying report is **Tier C** with an undisclosed
    conflict of interest.
17. _Extended Event Log: Towards a Unified Standard for Process Mining_, arXiv:2412.18012 —
    [arXiv](https://arxiv.org/pdf/2412.18012). **Tier A** for the minimum event-log triple.
18. Hughes, M. (2011), _Do 70 Per Cent of All Organizational Change Initiatives Really Fail?_,
    _Journal of Change Management_ — accessed via quotation in source 7. **Tier A**, secondhand.
    19–31. Consultancy and vendor material on "standardise before automating" (Auxiliobits, K&B Global,
    Reliability Academy, MoldMaking Technology, Mapex, Yempik), downstream repetitions of the EY
    30–50% figure (FutureCIO, Pega, MetaSource, Flobotics, Xenith, EISMD, Axiant), and Rogers &
    Blenko, _"Who Has the D?"_, HBR Jan 2006
    ([paywalled](https://hbr.org/2006/01/who-has-the-d-how-clear-decision-roles-enhance-organizational-performance)).
    **All Tier C**, all distrusted — every one sells a service that the cited claim justifies, and
    none contains a sample size, a method, or a comparison group. Enumerated here because
    establishing that this _is_ the entire available evidence base for the fix-first maxim is itself
    a finding (F-W7-19).

---

## Exit-Test Counts

- **Ledger claims verdicted:** 0 assigned, 0 outstanding. Verified by direct search of
  `corpus-ledger.md`.
- **Contradictions addressed:** 0 assigned; 1 new contradiction surfaced and characterised
  (X-W7-A), not manufactured into a verdict.
- **Findings:** 21 total — **Tier A: 9** (F-W7-02 provenance, 05, 06, 09, 13, 14, 15, 16, 17
  primary-source reading) · **Tier B: 8** (03, 04, 07, 08, 10, 11, 12, 18) · **Tier C / negative:
  4** (01, 19, 20, 21).
- **Findings with a filled `Counter-evidence` field:** 21 / 21.
- **Volatile figures dated:** all — Deloitte (2017 survey), EY (2016), Gartner (forecast to 2027),
  MIT NANDA (2025), LLM benchmark (models to April 2025), RPA tool coverage (2020), TOC
  meta-analysis (2003).
- **Sources read in full:** **8** (requirement: ≥3).
- **"No reliable evidence found" declarations:** 3 (SIPOC, RACI/decision-rights, MECE/issue trees —
  F-W7-21) plus 1 for the fix-first maxim's outcome evidence (F-W7-19).
- **Gaps section:** 10 entries, each with a stated settling condition.
