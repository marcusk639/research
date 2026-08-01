# W8 — Productized Consulting Operations

_Phase B findings | Generated: 2026-08-01 | Sources consulted: 18 | Read in full: 7_

> **Scope note.** This workstream covers **packaging, pricing, and running** the engagement. Domain
> ramp-up is W6; diagnostic methodology is W7. Where a finding touches diagnosis, it is about _where
> the diagnostic sits in the engagement structure_, not how to perform it.
>
> **Evidence-quality warning, stated up front.** This subject area is dominated by consultants
> selling courses about consulting. Of the material surveyed, exactly three source classes carried
> real evidentiary weight: (1) an international standard (ISO 20700:2017), (2) binding law and
> regulation (26 CFR 301.7216, 45 CFR 164.504, GDPR Art. 28, FAR Part 16), and (3) two peer-reviewed
> studies. Everything else — including every book, blog, and "pricing survey" encountered — is C-tier
> and is labelled as such. **The single most commercially important question the operator asked
> (what fraction of an engagement is genuinely reusable) has no evidence base at all.** See `Gaps`.

---

## Ledger Verdicts

| Claim ID | Verdict        | Current value / correction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Evidence tier | Source                                                                                                                                                                                                        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C-086    | **UNVERIFIED** | Conductor's public marketing page confirms only that it runs parallel Claude Code / Codex / Cursor agents in isolated workspaces on macOS. It makes no statement about source availability, GitHub OAuth scopes, or what data leaves the machine, and no security or privacy documentation was located.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | —             | [conductor.build](https://conductor.build/) (vendor marketing, read)                                                                                                                                          | The **product-capability half** of this claim (closed-source binary; broad GitHub access) could not be confirmed or refuted and should be re-verified by **W1/W2**, which own tool capability. The **normative half** — that a third-party binary with access to a client repository is a confidentiality event requiring contractual treatment — is independently established at A-tier; see **F-W8-07**. Session web-search budget was exhausted before a deeper product check was possible; this is a limitation of this pass, not a finding that the claim is false. |
| C-150    | **REFUTED**    | The claim is wrong on both its premise and its remedy. (a) §7216 does **not** flatly prohibit sending tax return information to a service provider: 26 CFR §301.7216-2(d)(2) permits disclosure to a contractor for auxiliary/technical services _provided the preparer gives written notice of §§7216 and 6713_, and the contractor thereby becomes a return preparer itself. (b) "Stays on local Claude Code instances" is not a compliance state — Claude Code transmits content to Anthropic's API, which is itself a disclosure to a third party. **The operative restrictions are geographic, not tool-branded:** §301.7216-2(d)(1) requires disclosure remain within the United States absent taxpayer consent; (d)(3) bars disclosure of SSNs to preparers outside US territory without consent; (c)(2) restricts even intra-firm disclosure to members located outside the US. | A             | [26 CFR §301.7216-2 (Cornell LII)](https://www.law.cornell.edu/cfr/text/26/301.7216-2) (read in full); [Anthropic Commercial Terms, eff. 2025-06-17](https://www.anthropic.com/legal/commercial-terms) (read) | The corpus's **operational conclusion for OpenRouter survives** — a multi-provider router that may route to non-US inference providers cannot satisfy (d)(1)/(d)(3) without taxpayer consent. But it survives for the wrong reason, and the stated safe harbour ("local Claude Code") is not one. Correct rule stated in **F-W8-08**.                                                                                                                                                                                                                                    |

**Counts:** 2 claims assigned, 2 verdicted — 0 CONFIRMED, 0 STALE, **1 REFUTED**, **1 UNVERIFIED**, 0 SKIPPED. No silent omissions.

---

## Contradiction Findings

**No contradictions from §3 of the ledger are assigned to W8.** X-01 → W1/W3; X-02, X-05 → W5; X-03 →
W1/W4; X-04 → W9/W5; X-06 → W1. Nothing to address here.

---

## Findings

### Phase-gated engagement structure

**F-W8-01 — There is exactly one international standard defining the structure of a management
consulting engagement, and it specifies three gates, not five.**

- **Claim** — ISO 20700:2017 _Guidelines for management consultancy services_ defines the "typical
  consulting process" as three activities — **contracting (Clause 5) → execution (Clause 6) →
  closure (Clause 7)** — each decomposed identically into General / Purpose / Input / Outcome /
  Contents. Discovery, diagnostic, roadmap and build are **not** gates in the standard; they appear
  as steps _inside_ execution (6.5.3: Prepare → Analyse options → Recommend → Obtain decision →
  Implement).
- **Evidence tier** — **A** (international standard, developed by ISO/PC 280 with 48 participating
  countries, led by ICMCI/CMC-Global).
- **Support** — [ISO 20700:2017 full text](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in
  full**, clauses 1–7.5.5 plus Annexes A, C, D); [ISO catalogue
  entry](https://www.iso.org/standard/63501.html); [ISO/iTeh preview with complete table of
  contents](https://cdn.standards.iteh.ai/samples/63501/97bc8b0046b149cea61d4ab922a4ef6f/ISO-20700-2017.pdf)
  (**read in full**); [CMC-Global 20700 Toolbox](https://www.cmc-global.org/sites/default/files/public/cmc-global_20700_toolbox_-_1st_edition_2017-09.pdf)
  (**read in full**, 25 slides).
- **Date sensitivity** — Standard published 2017-06; first edition, no revision located as of
  2026-08-01. Stable — ISO guidance standards typically run 5–10 years between revisions, so this is
  overdue for review but not superseded.
- **Confidence** — **High** for what the standard says. **Low** for whether it works: see
  counter-evidence.
- **Counter-evidence** — ISO 20700 is written as guidance, is explicitly non-certifiable, and has no
  conformity-assessment scheme; the CMC-Global "Toolbox" reduces to an 18-item yes/no self-declaration
  checklist and a suggestion to put "delivered according to ISO 20700" on your business card. **No
  study of any kind was found measuring whether following ISO 20700 improves engagement outcomes,
  margin, or client satisfaction.** Its authority is institutional, not empirical.

**F-W8-02 — The standard's contracting clause is the most authoritative reusable engagement template
that exists, and roughly 90% of it is client-independent.**

- **Claim** — ISO 20700 §5.5 specifies six mandatory agreement sections (context; services and
  deliverables; approach and work plan; roles and responsibilities; acceptance criteria; terms and
  conditions) and a **17-item work-plan checklist** at §5.5.4 (a–q): objectives/scope/expected
  outcomes; approach and methodology; project governance including escalation; contents;
  documentation; data, information and technological resources; project organization; MCSP human
  resources; client/recipient human resources and roles; timetable and milestones; project budget;
  project management methods; communications; **client and/or recipient capacity building**;
  **knowledge transfer**; quality and risk methodology; deliverables. Of the six top-level sections,
  only §5.5.2 (Context — "an accurate description of the organization's current situation, the
  client's objectives, why the work needs to be done, the assumptions and their impact") is
  necessarily client-specific.
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 §5.5](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High** that this is the standard's content. **Medium** that it functions as a
  productization template — that is an inference from its structure, not a measured property.
- **Counter-evidence** — The standard says the items are "typical contents … However, if it is
  obvious to both parties that some of these contents are inappropriate, they should be excluded"
  (§5.5.1) — i.e. it explicitly declines to mandate a fixed template. No source was found quantifying
  how much of an engagement agreement is genuinely reusable across clients.

**F-W8-03 — Closure is a defined gate with its own named checklist, and the standard requires
surviving obligations to be explicitly enumerated at closure.**

- **Claim** — ISO 20700 §7 defines closure as complete only when six topic areas are addressed
  (§7.1): legal and contractual matters; final evaluation and improvement; administrative matters
  including payment; communication; **intellectual property rights**; outstanding minor issues.
  §7.4 requires the closure process to produce a "shared understanding of continuing obligations
  between all the stakeholders … (e.g. guarantees, confidentiality, data protection, intellectual
  rights, outstanding issues)". §7.5.1 enumerates the legal wrap-up: invoicing and payment; expense
  reconciliation; **formal sign-off and acceptance**; release of resources including subcontractors;
  warranties and guarantees; third-party confidentiality; ownership of IP rights; and "obligations
  that remain after closure (e.g. legal, confidentiality, protection of intellectual property rights,
  data protection, non-competition, outstanding issues)". §7.5.3 requires return of client property
  "(e.g. files, records, data, security passes)".
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 §7](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High**.
- **Counter-evidence** — None found on the content. But no evidence was found that performing closure
  formally reduces post-engagement support drag; the causal link between a closure checklist and a
  clean exit is unevidenced folklore, however plausible.

**F-W8-04 — The standard places the pre-sale diagnostic explicitly outside the governed process
unless it is itself contracted.**

- **Claim** — ISO 20700 Annex C treats "understanding the business context" (a), "understanding the
  client's context" (b), and "selection of MCSP" (c) as activities that occur before contracting, and
  states for each: _"Unless such an activity is part of a specific assignment, it is out of the scope
  of this document."_ Similarly for "follow up" (g) after closure. The MCSP "will devote considerable
  resources to this activity in order to be able to identify potential clients and assignments"
  (Annex C a).
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 Annex C](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High**.
- **Counter-evidence** — None found. Note this is a scoping statement about the standard, not a
  recommendation to give discovery away; the standard is neutral on whether discovery is paid, and
  says only that once it _is_ an assignment, the full contracting/execution/closure discipline applies
  to it.

**F-W8-05 — Scope change is a named gate mechanism with a defined re-entry to contracting.**

- **Claim** — ISO 20700 §6.5.4.6 requires "a change control system or process, including management of
  the records," listing five trigger categories: deviations from the work plan; changed context;
  changes in the client's or recipient's operating environment; changes in client expectations;
  changes in the MCSP. It then states that changes "beyond the scope of the change control process …
  may be considered as new inputs to the contracting and/or execution phase … and may require that
  the agreement be renegotiated." §6.3 reinforces: "Execution should not start until there is an
  agreement."
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 §6.3, §6.5.4.6](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High**.
- **Counter-evidence** — None found on the content. Industry data suggests the mechanism is widely
  ineffective or unused: project overruns across 403 professional services firms rose to 11.3% in 2024
  (see **F-W8-15**), and scope creep is named as a top margin-erosion cause in the same report's
  sponsor commentary.

**F-W8-06 — Acceptance criteria are the standard's designated mechanism for ending an engagement
rather than letting it drift into unpaid support.**

- **Claim** — ISO 20700 requires acceptance criteria in the agreement (§5.5.6: "such as key
  performance indicators"), an agreed approvals/acceptance process during execution (§6.5.5: "The
  commercial implications of acceptance or rejection should be dealt with in accordance with the
  agreement"), and defines assignment completion by reference to it (§7.1: "The assignment is
  completed when the acceptance process, as defined in the agreement, is completed"). §4.1.3 assigns
  ultimate accountability for decisions and outcomes to the **client**, not the MCSP, unless the
  agreement says otherwise.
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 §4.1.3, §5.5.6, §6.5.5, §7.1](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High** for the content; **low** for effectiveness.
- **Counter-evidence** — No evidence found that acceptance-criteria discipline actually reduces
  post-engagement support load. Across 403 firms, on-time delivery was 73.4% in 2024 — i.e. roughly
  one engagement in four fails its schedule commitment even in firms with formal PMOs (**F-W8-15**).

### IP reuse across clients — the operator's live risk

**F-W8-07 — The standards-body default is a background/foreground split: the consultant retains
pre-existing methodology by default; ownership of anything arising from the deliverables must be
negotiated at contracting, not assumed.**

- **Claim** — ISO 20700 §4.4.8 states, verbatim: _"The MCSP has intellectual property rights for its
  know-how, methodologies, database, benchmarks, business models, tools and other relevant concepts
  and techniques. The MCSP normally retains the ownership for intellectual property rights that they
  bring to a project. For intellectual property rights arising from the outcome/deliverables of the
  assignment (ownership, right to use or right to refer to), the ownership should be agreed upon
  during the contracting phase. This policy may also apply after the closure of the assignment."_
  §5.5.7.2 requires the agreement to specify "ownership of material and deliverables, user rights,
  licensing, intellectual property rights, liability limits".
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 §4.4.8, §5.5.7.2](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High** that this is the standard's position; **medium** that it is the market
  default.
- **Counter-evidence** — "Normally retains" is a description of practice, not a legal rule, and it is
  routinely overridden. Client-drafted master services agreements commonly demand assignment of all
  work product; law-firm guidance describes the market resolution as _assignment of deliverables with
  a license-back for general-purpose tools_, which is a weaker position than ISO's default. A
  provider-favourable template exists at the other extreme — one MSP-side MSA template treats all
  "Provider Work" as owned by the provider with only a **terminating** license to the client
  ([Scott & Scott LLP](https://scottandscottllp.com/master-services-agreement-template/), read). The
  practical point is that §4.4.8 is a negotiating baseline, not protection.

**F-W8-08 — The binding constraint on cross-client reuse is not IP law but confidentiality plus
professional ethics, and the professional rule is stricter than most contracts: it prohibits _use_,
not merely disclosure.**

- **Claim** — The IMC USA Enforceable Code of Ethics §5.0 states: _"I will treat appropriately all
  confidential client information that is not public knowledge, take reasonable steps to prevent it
  from access by unauthorized people, and will not take advantage of proprietary or privileged
  information, either for use by myself, the client's firm, or another client, without the client's
  permission."_ This is a condition of membership and of CMC certification, pledged in writing.
  §6.0 requires immediate disclosure of circumstances that may influence judgment or objectivity;
  §4.0 requires a mutual understanding of "objectives, scope, work plan, and fee arrangements"
  **before accepting any engagement**; §9.0 requires agreeing the basis for fees and expenses in
  advance. ISO 20700 §4.4.7 is parallel: _"The MSCP should not use stakeholders' data or information
  without permission for any reason, particularly to demonstrate the capacity of the MCSP to execute
  an assignment"_ — i.e. an explicit bar on using one client's material as a credential when selling
  to the next. Annex D Table D.1 adds: _"Respecting the rights of other professionals in the
  consultancy industry by not using proprietary information or methodologies without permission."_
- **Evidence tier** — **A** (enforceable professional-body code; international standard).
- **Support** — [IMC USA Enforceable Code of Ethics](https://www.imcusa.org/about/ethics/code-of-ethics/)
  (**read in full**); [ISO 20700:2017 §4.4.7, Annex D](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>)
  (**read in full**).
- **Date sensitivity** — Low. IMC USA code is long-standing; no revision date located.
- **Confidence** — **High** on the text. **Medium** on reach: these bind IMC members and CMC holders,
  not consultants generally. An unaffiliated solo operator is bound by contract and trade-secret law,
  not by this code — but it is the clearest articulation found of what "leaking one client into
  another" means in professional terms.
- **Counter-evidence** — None found contradicting the rule. Note the asymmetry it creates: the code
  bars taking advantage of client-specific proprietary information but says nothing prohibiting reuse
  of the consultant's own generic methodology — consistent with ISO §4.4.8.

**F-W8-09 — The recognised contractual device for permitting knowledge reuse is a residuals clause,
and it does not cover anything you wrote down.**

- **Claim** — A residuals clause exempts the recipient from confidentiality restrictions for
  information _"retained in the unaided memory"_ of its people. Three independent law-firm analyses
  converge on the same four points: (i) the rationale is that humans cannot selectively forget;
  (ii) it is nearly unenforceable in practice because proving "unaided memory" versus consulted notes
  is extremely difficult; (iii) drafted broadly it can _"undermine the entire agreement or result in
  destruction of trade secret protection"_; (iv) protective drafting therefore restricts it to
  knowledge retained without reference to notes, documents or recorded material, carves out trade
  secrets, prohibits intentional memorization, and disclaims any patent/copyright licence.
  Litigation consequence: in _Space Data Corp. v. X_ (N.D. Cal. 2017) the court found inadequate
  pleading of how the defendant's conduct exceeded the residuals clause — i.e. the clause shifts a
  meaningful pleading burden onto the disclosing party.
  **Direct consequence for the operator:** every formulation found is limited to _unrecorded_ memory.
  A per-client knowledge repository is recorded material and falls entirely outside residuals
  protection.
- **Evidence tier** — **B** (law-firm practitioner commentary from three independent firms; one cited
  case; no empirical study).
- **Support** — [Venable LLP, _Residual Clauses in an NDA for M&A Transactions_](https://www.venable.com/insights/publications/2018/11/residual-clauses-in-an-nda-for-ma-transactions)
  (**read in full**); [Wyrick Robbins, _Understanding the Risks and Benefits of a Residuals Clause_](https://ventures.wyrick.com/blog/nondisclosure-agreements-understanding-the-risks-and-benefits-of-a-residuals-clause)
  (read); [Galkin Law, _Narrowing the Residuals Clause_](https://galkinlaw.com/residuals-clause-in-nda/) (sampled).
- **Date sensitivity** — Venable 2018, case 2017. Doctrine is stable; jurisdictional variance
  (California is repeatedly flagged as highest-risk for the line between protectable trade secrets and
  general professional skill) may shift.
- **Confidence** — **Medium-high**. Convergent across independent firms with no shared interest;
  weakened by being commentary rather than a survey of decided cases.
- **Counter-evidence** — All three sources are written from the **disclosing** party's perspective and
  advise against including residuals clauses at all. That is the opposite of the consultant's
  interest, so the guidance systematically understates the clause's value to a reuse-dependent
  provider. No source was found analysing residuals clauses from the consultant's side, and **no case
  was found of a solo consultant sued for cross-client methodology reuse**.

### Client-data handling, confidentiality, and regulated data

> ⚠️ **All findings in this subsection carry confidentiality, data-residency, regulated-data, or
> third-party-access implications for work performed on client material.**

**F-W8-10 — Any third-party tool that touches client material is a disclosure event with a
contract-level compliance path in every regime checked; "it's just a tool I use" is not a defence
under any of them.**

- **Claim** — Three independent regimes impose materially identical structural obligations, all of
  which flow down to subcontractors:
  - **GDPR Art. 28** — a processor "shall not engage another processor without prior specific or
    general written authorisation of the controller" (28(2)); the processing contract must specify
    subject-matter, duration, nature, purpose, data types and categories of data subject, and eight
    mandated terms (28(3)(a)–(h)) including documented-instructions-only processing, staff
    confidentiality commitments, Art. 32 security measures, assistance with data-subject rights,
    audit rights, and **deletion or return of all personal data at end of service**; where a
    sub-processor is engaged, "identical data protection obligations" must be imposed and the initial
    processor remains fully liable (28(4)).
  - **HIPAA 45 CFR §164.504(e)(2)** — the business associate contract must establish permitted uses
    and disclosures ((e)(2)(i)); may permit use for the BA's own management and administration
    ((e)(2)(i)(A)) and data aggregation ((e)(2)(i)(B)); must "ensure that any subcontractors … agree
    to the same restrictions and conditions" ((e)(2)(ii)(D)); and must require the BA at termination
    to "return or destroy all protected health information … and retain no copies" ((e)(2)(ii)(J)).
  - **26 CFR §301.7216-2(d)(2)** — disclosure to a contractor providing auxiliary/technical services
    is permitted **only if** the preparer gives written notice explaining §§7216 and 6713 and their
    penalties, and the contractor thereby becomes a tax return preparer subject to the same rules.
- **Evidence tier** — **A** (binding regulation in all three cases).
- **Support** — [GDPR Art. 28](https://gdpr-info.eu/art-28-gdpr/) (**read in full**);
  [45 CFR §164.504 (Cornell LII)](https://www.law.cornell.edu/cfr/text/45/164.504) (read, targeted);
  [26 CFR §301.7216-2 (Cornell LII)](https://www.law.cornell.edu/cfr/text/26/301.7216-2) (**read in full**).
- **Date sensitivity** — Low for GDPR and HIPAA (stable since 2018 and 2013 respectively). §7216
  regulations stable since 2008. Re-check annually.
- **Confidence** — **High**.
- **Counter-evidence** — None. These are the operative texts. Note the _permissive_ elements that cut
  in the consultant's favour and are frequently overlooked: HIPAA expressly allows a BA contract to
  permit use of PHI "for the proper management and administration of the business associate"
  ((e)(2)(i)(A)) — a negotiable route to limited internal reuse that most parties never ask for.

**F-W8-11 — For US tax return information the binding restrictions are geographic, not tool-branded.**

- **Claim** — Under 26 CFR §301.7216-2: (d)(1) permits disclosure to another preparer for
  non-substantive services only where the recipient is **located within the United States**, absent
  §301.7216-3 consent; (d)(3) prohibits disclosure of a taxpayer's SSN to a preparer located outside
  the United States or its territories without consent; and (c)(2) restricts even intra-firm
  disclosure to members located outside the US without prior consent. The regulation's own Example 3
  applies this to a contractor accessing data from outside the US: consent is required.
- **Evidence tier** — **A**.
- **Support** — [26 CFR §301.7216-2](https://www.law.cornell.edu/cfr/text/26/301.7216-2) (**read in full**).
- **Date sensitivity** — Stable.
- **Confidence** — **High**.
- **Counter-evidence** — None. This _corrects_ C-150 rather than contradicting its conclusion: a
  multi-provider router with non-US inference endpoints is the compliance problem; a US-located
  single provider under written §7216 notice is a permitted configuration.

**F-W8-12 — Vendor terms are the operative confidentiality instrument for AI processing of client
material, and they are product-tier-specific and dated.**

- **Claim** — Anthropic's Commercial Terms of Service, effective **2025-06-17**, state that
  "Customer (a) retains all rights to its Inputs, and (b) owns its Outputs"; that "Anthropic may not
  train models on Customer Content from Services"; impose reciprocal confidentiality with a
  reasonable-care standard; and require destruction of Confidential Information promptly on request
  subject to legal-retention and automated-backup exceptions.
- **Evidence tier** — **A** for the text, but **vendor-primary**: this is the only source for a claim
  about the vendor's own product, and the vendor has a stake in the answer.
- **Support** — [Anthropic Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) (read).
- **Date sensitivity** — **High. Time-stamped to the 2025-06-17 version, checked 2026-08-01.** Vendor
  data-handling terms have changed materially and repeatedly across the industry; re-verify before
  every regulated-data engagement, and verify which terms apply to the specific product tier in use
  (commercial/API terms are not consumer-subscription terms).
- **Confidence** — **Medium-high** that the text is current; **high** that it is insufficient on its own.
- **Counter-evidence** — These terms do **not** by themselves satisfy any of the regimes in
  **F-W8-10**. A BAA, a §7216 written notice, and an Art. 28 DPA are separate instruments with their
  own required contents; a favourable no-training clause is necessary and nowhere near sufficient. No
  independent audit of the no-training commitment was located.

### Pricing and scoping models

**F-W8-13 — The only non-selling, non-anecdotal framework found for choosing a contract type is
government procurement doctrine, and it turns on requirement uncertainty and acquisition history.**

- **Claim** — FAR 16.104 enumerates twelve factors for contract-type selection. The ones that bear on
  a solo diagnostic-then-build practice: price competition normally makes fixed-price appropriate;
  **complex or unique requirements increase the buyer's risk, and "as requirements recur, cost risk
  should shift to the contractor"**; long performance periods argue for adjustment mechanisms; and
  **risk typically decreases with repetitive acquisitions**. Cost-reimbursement approaches apply where
  uncertainty is high and costs cannot be reasonably estimated in advance. FAR 16.601 states flatly
  that a time-and-materials contract "provides no positive profit incentive to the contractor for cost
  control or labor efficiency," requires a determination and findings that no other contract type is
  suitable, and requires a **ceiling price that the contractor exceeds at its own risk**.
- **Evidence tier** — **A** (binding federal regulation).
- **Support** — [FAR 16.104](https://www.acquisition.gov/far/16.104) (read);
  [FAR 16.601](https://www.acquisition.gov/far/16.601) (read).
- **Date sensitivity** — Low; FAR Part 16 is stable. Re-check on FAR overhaul.
- **Confidence** — **High** for what the rule says; **medium** for transferability.
- **Counter-evidence** — This is procurement policy written for a monopsony buyer protecting public
  money, not evidence about consultant profitability. It says nothing about value-based pricing, and
  its bias toward fixed-price reflects the _buyer's_ interest. Its structural insight — that
  fixed-price becomes appropriate as a requirement becomes repetitive — is a description of risk
  allocation, not a measured outcome.

**F-W8-14 — The peer-reviewed empirical evidence on contract-type choice is thin, single-vendor, and
does not answer which type is more profitable.**

- **Claim** — Gopal, Sivaramakrishnan, Krishnan & Mukhopadhyay (2003), _Management Science_
  49(12):1671–1683, analysed **93 offshore software projects from one Indian vendor** and found that
  requirement uncertainty, project team size and resource shortage significantly predict fixed-price
  vs. time-and-materials choice, and that **contract choice significantly determines project profit**,
  with duration and team size continuing to influence profit after controlling for contract choice.
  The abstract does not state which contract type yields higher vendor profit.
- **Evidence tier** — **A** (peer-reviewed) with **low external validity**.
- **Support** — [Gopal et al., _Contracts in Offshore Software Development: An Empirical Analysis_](https://pubsonline.informs.org/doi/10.1287/mnsc.49.12.1671.25120)
  (abstract read; full text paywalled).
- **Date sensitivity** — 2003 data. The finding that requirement uncertainty drives contract choice is
  structural and likely durable; the magnitudes are not.
- **Confidence** — **Medium**. Single vendor, single country, single industry, 23 years old, and I did
  not read the full paper.
- **Counter-evidence** — Offshore software outsourcing between firms is a poor analogue for a solo
  advisory practice: no bench, no subcontracting, no separate estimating function, and a fundamentally
  different information asymmetry. Treat as directional only.

**F-W8-15 — Practitioner pricing surveys are self-selected vendor audiences and cannot support causal
claims; the one with published numbers is C-tier.**

- **Claim** — Consulting Success reports a survey of "nearly 1,000 consultants" across "75+ countries"
  with the pricing-model distribution: project-based **30%**, hourly **29%**, monthly retainer **16%**,
  value-based **15%**, daily rate **10%**. It further reports that 51% of consultants using
  value-based fees have an average project value of $10K+ versus 39% of those using hourly fees, and
  that consultants earning $10K–$45K/month are more likely to use retainers and value-based pricing
  than those earning $2K–$5K/month.
- **Evidence tier** — **C**. No fieldwork date, no recruitment method, no response rate, and no sample
  composition beyond geography and experience level are published. The publisher sells a consulting
  coaching program and promotes it throughout the article — the respondents are its own audience.
- **Support** — [Consulting Success, _Consulting Fees & Pricing_](https://www.consultingsuccess.com/consulting-fees) (read).
- **Date sensitivity** — **Unknown and unstated — which is itself disqualifying for a figure of this
  kind.** Checked 2026-08-01.
- **Confidence** — **Low** for anything causal; **low-medium** for the distribution as a rough picture
  of one self-selected population.
- **Counter-evidence** — The income correlation is confounded in the obvious direction: consultants
  who can already command large engagements are the ones who can switch to value pricing, so the
  reported association is at least as consistent with reverse causation as with the vendor's implied
  claim. **This finding's evidence base is a single self-selected vendor survey — treat every number
  in it as illustrative, not as a basis for pricing decisions.**

### Productization, repeatability, and delivery baselines

**F-W8-16 — "Productization" has a usable academic definition and essentially no outcome evidence.**

- **Claim** — Härkönen, Haapasalo & Hänninen (2015), _International Journal of Production Economics_
  164:65–82, define productisation as _"the process of analysing a need, defining and combining
  suitable elements, tangible and/or intangible, into a product-like defined set of deliverables that
  is standardised, repeatable and comprehendible,"_ and conclude that well-productised offerings are
  easier to buy, sell and market — while explicitly finding that the literature is limited, lacks
  depth, and "requires further development." A follow-up (Härkönen et al. 2017, _Journal of Service
  Management_ 28(5):936–971) attempts a systematisation.
- **Evidence tier** — **A** for the definition (peer-reviewed literature review); **no tier** for
  effect, because no measured effect was found.
- **Support** — [Härkönen, Haapasalo & Hänninen, _Productisation: A review and research agenda_ (EconPapers)](https://econpapers.repec.org/article/eeeproeco/v_3a164_3ay_3a2015_3ai_3ac_3ap_3a65-82.htm)
  (abstract read; full text paywalled).
- **Date sensitivity** — 2015 review; the field has not obviously matured.
- **Confidence** — **High** for the definition; **high** that the outcome evidence is absent, because
  the review's own conclusion is that the literature is thin.
- **Counter-evidence** — None found — and the absence _is_ the finding. **No study was located
  measuring the effect of productizing a professional service on win rate, margin, delivery hours,
  client satisfaction, or any other outcome.** Every strong claim about productization encountered in
  this research was made by someone selling a course about productization.

**F-W8-17 — The best available quantitative proxy for "process repeatability pays" is a
vendor-sponsored self-selected maturity survey, and its headline numbers are ratio-of-ratio artefacts
that overstate the effect.**

- **Claim** — SPI Research's 2025 Professional Services Maturity Benchmark surveyed **403 firms**
  (fieldwork Fall 2024, published February 2025; five-year cumulative base ~3,500 firms; size bands
  include **"Under 10 employees"**; 165 KPIs). Its five maturity levels are defined explicitly by
  process standardization: **Level 1 "Heroic"** — ad hoc and fluid processes — **30% of firms**;
  **Level 2** — "core operating processes are repeatable but unenforced … not documented or codified"
  — 25%; **Level 3** — "standard processes and operating principles for all central service
  performance pillars" — 25%; Level 4 — 15%; Level 5 — 5%. SPI reports that in 2024, Level 5 firms
  averaged **739% higher revenue growth, 537% higher profit margins, and 71% better billable
  utilization** than Level 1 firms.
- **Evidence tier** — **B**, and only just. Self-selected online survey; self-reported financials; no
  response rate; sponsored and distributed by PSA software vendors (Kantata, Workday) whose product
  is the implied remedy; purely correlational.
- **Support** — [SPI 2025 Professional Services Maturity Benchmark (Kantata mirror)](https://get.kantata.com/rs/677-LEJ-696/images/2025-ps-maturity-benchmark.pdf)
  (**front matter, "About the Benchmark", "Report Organization" and Executive Summary read in full;
  body sampled — the contract-type tables are in the paywalled body**);
  [SPI intro/contents](https://spiresearch.com/wp-content/uploads/2025/02/2025-PS-Maturity-Benchmark-Intro-and-Contents-Pages.pdf) (read).
- **Date sensitivity** — **High. Figures describe calendar 2024 and are refreshed annually.** Checked
  2026-08-01; the 2026 edition exists and supersedes these numbers.
- **Confidence** — **Low-medium.** The direction is plausible; the magnitudes should not be quoted.
- **Counter-evidence** — Four specific problems. (1) Reverse causality: profitable firms can afford
  process investment. (2) "739% increase in revenue growth" is a ratio of growth rates, not a growth
  rate — a firm going from 1% to 8.4% growth produces that figure. (3) The response base fell from
  575 firms (2024) to 403 (2025), attributed by SPI itself to "changes in survey tooling that impacted
  deliverability" — a non-random attrition SPI asserts, without evidence, left the respondent profile
  unchanged. (4) Level definitions are firm-level constructs (documented processes enforced across
  geographies) that do not map cleanly onto a one-person practice.

**F-W8-18 — Industry delivery baselines a solo operator can estimate against, all deteriorating.**

- **Claim** — SPI 2025 Benchmark, n=403, calendar-2024 data (five-year average in brackets):
  project **overrun 11.3%** (up from 9.6% in 2023, +18% YoY); **on-time delivery 73.4%** [77.2%];
  **billable utilization 68.9%** [70.8%], against a stated optimum of 75%; **project margin 35.9%**
  [35.5%]; **annual revenue per billable consultant $199K** [$204K]; **EBITDA 9.8%** [14.9%] — the
  lowest in five years; YoY PS revenue growth 4.6% [8.7%]; attrition 11.7% [12.8%].
- **Evidence tier** — **B** (same methodological caveats as F-W8-17).
- **Support** — [SPI 2025 Benchmark, Tables 1 and 2, Executive Summary](https://get.kantata.com/rs/677-LEJ-696/images/2025-ps-maturity-benchmark.pdf) (**read in full**).
- **Date sensitivity** — **High — these are calendar-2024 figures published 2025-02, read 2026-08-01,
  and are superseded by the 2026 edition.** Do not carry forward without re-checking.
- **Confidence** — **Medium** as an industry order-of-magnitude; **low** as a target for a solo practice.
- **Counter-evidence** — These are firm-level metrics for multi-person organisations with a bench,
  a sales function, and subcontractor capacity (10.9% of revenue delivered by third parties in 2024).
  A solo operator has none of these, so utilization economics differ structurally: there is no
  bench-cost drag, but also no way to absorb an overrun by reassigning staff. **SPI does not publish
  the fixed-price vs. time-and-materials margin comparison outside the paywalled body (Tables ~223–226),
  so the contract-type question cannot be settled from the public excerpt.**

### Handoff and enablement

**F-W8-19 — ISO 20700 puts knowledge transfer at contracting, not at closure — a falsifiable
structural position, and the opposite of common practice.**

- **Claim** — "Client and/or recipient capacity building" and "knowledge transfer" appear as items (n)
  and (o) of the **work-plan checklist agreed during the contracting phase** (§5.5.4). The closure
  clause (§7.5) contains **no knowledge-transfer item at all** — only legal/contractual wrap-up
  (7.5.1), evaluation (7.5.2), administrative matters including return of client property (7.5.3),
  communication obligations plus a requirement that "the client is debriefed at the end of the
  assignment" (7.5.4), and outstanding minor issues (7.5.5). Execution §6.5.3 reinforces this by
  describing implementation as performed "by the MCSP **with the recipient**".
- **Evidence tier** — **A**.
- **Support** — [ISO 20700:2017 §5.5.4, §6.5.3, §7.5](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (**read in full**).
- **Date sensitivity** — None.
- **Confidence** — **High** on the structural claim.
- **Counter-evidence** — The standard gives no reasoning for this placement and no evidence that it
  works better than a handoff-phase approach. It is a design decision by a committee, not a tested
  finding.

**F-W8-20 — There is one directly relevant peer-reviewed study of consultant-to-client knowledge
transfer, and its key methodological move is that it measured _application_, not perception.**

- **Claim** — Ko, Kirsch & King (2005), _MIS Quarterly_ 29(1):59–86, studied **96 ERP implementation
  projects** using **consultant–client matched-pair samples**, with a dependent variable defined as
  "a behavioral measure of knowledge transfer that incorporates the application of knowledge" —
  explicitly distinguishing it from prior self-report measures. Knowledge-related, motivational, and
  communication-related factors all significantly influenced transfer; **9 of 13 hypotheses were
  supported**, plus two mediating relationships.
- **Evidence tier** — **A** (peer-reviewed, matched-pair design, behavioural outcome measure).
- **Support** — [Ko, Kirsch & King, AIS eLibrary](https://aisel.aisnet.org/misq/vol29/iss1/5/)
  (abstract and study description read; full text not obtained);
  [MIS Quarterly listing](https://misq.umn.edu/antecedents-of-knowledge-transfer-from-consultants-to-clients-in-enterprise-system-implementations.html).
- **Date sensitivity** — 2005. Antecedent structure is likely durable; the ERP context is dated and
  says nothing about AI-assisted delivery.
- **Confidence** — **Medium-high** for the existence and design; **low** on specifics — I did not read
  the full text, so I cannot report effect sizes or which four hypotheses failed.
- **Counter-evidence** — Large multi-party ERP implementations are a poor structural analogue for a
  solo engagement: the study's motivational and communication constructs largely concern
  team-to-team dynamics that do not exist in a one-consultant/one-sponsor engagement. Its transferable
  contribution is methodological — _measure whether the client can do the thing, not whether they say
  they learned it_ — rather than substantive.

---

## Gaps

Stated specifically, per the evidence standard. Each says what would settle it.

1. **The 80/20 reuse ratio has no evidence base whatsoever.** No study, survey, or practitioner
   dataset was found that measures what fraction of a consulting engagement's artefacts carries over
   unchanged between clients. Not a weak estimate — _none_. **What would settle it:** time-tracked
   delivery data across ≥20 engagements from ≥3 independent solo or micro practices, segmented by
   artefact type (proposal, work plan, diagnostic instrument, report template, build artefact,
   handoff material), coded for reuse-unchanged / reuse-adapted / net-new. Nothing of this shape
   exists publicly.

2. **No outcome evidence on productized/fixed-scope service design.** Productization has a
   peer-reviewed definition (F-W8-16) and a literature review whose own conclusion is that the field
   is thin. **What would settle it:** a controlled or matched comparison of fixed-scope versus bespoke
   engagements on win rate, delivery hours, margin, and overrun. **What exists instead:** books and
   courses sold by their own authors.

3. **No evidence on paid discovery / paid diagnostic as a separately priced phase.** This is
   near-universal advice in practitioner writing and has zero measurement behind it. ISO 20700 is
   deliberately silent (F-W8-04). **What would settle it:** conversion-rate and margin data comparing
   paid-diagnostic-first against proposal-first engagement pipelines.

4. **No evidence on deliverable templating or time-boxing.** No study was found on the effect of
   standardised deliverable templates or fixed-duration phases on delivery cost or quality. The
   software-estimation literature (Jørgensen and colleagues on optimism bias and cost-overrun
   magnitude) is the obvious adjacent body of work and **I was unable to retrieve it — the session's
   web-search budget was exhausted before I reached it.** This is a real hole in this pass, not a
   claim that the literature is absent. **W3 or a follow-up pass should retrieve it.**

5. **No case law found on cross-client methodology reuse by an individual consultant.** The only case
   surfaced (_Space Data Corp. v. X_, N.D. Cal. 2017) concerns residuals in a corporate NDA. **What
   would settle it:** a docket search for trade-secret and breach-of-confidence actions against
   individual consultants or micro-firms, which I could not perform within budget.

6. **SPI's contract-type comparison is paywalled.** The 2025 Benchmark's tables comparing project
   margin for time-and-materials versus fixed-price projects (Tables ~~223–226 per the public appendix
   listing) are not in the free excerpt. This is the single most decision-relevant number in the
   report for this workstream and it could not be obtained. **What would settle it:** the full report
   (~~$2K commercially) or a comparable independent dataset.

7. **ISO 20700 has never been evaluated.** No study was found measuring whether conforming to it
   changes any outcome. It has no certification scheme and no published adoption statistics. Its
   authority is entirely institutional. **What would settle it:** a comparison of engagement outcomes
   between conforming and non-conforming providers — which, absent a certification register, is
   currently not constructible.

8. **Nothing found on how AI-assisted delivery changes engagement economics or confidentiality
   practice.** The SPI 2025 report has an AI chapter (pp. 78–88) discussing adoption and
   "organizational concerns with AI," which I did not read; no source was found addressing the
   specific question of a solo consultant running client material through an AI harness, beyond the
   generic regulatory framework in F-W8-10.

9. **The C-086 tool-security claim is unresolved.** See the ledger table. Owned by W1/W2.

---

## Implications for the Operator

_My inferences. Not findings. Phase C does the reasoning._

- **The three-gate structure, not a five-phase one, is what has authority behind it.** Discovery →
  diagnostic → roadmap → build → handoff maps onto ISO's model as: _contracting_ (with a possible
  separately-contracted diagnostic assignment ahead of it), _execution_ containing
  Prepare/Analyse/Recommend/Decide/Implement, and _closure_. If the goal is a productized structure a
  client can recognise, the ISO decomposition is defensible in a way a self-invented five-phase model
  is not.

- **§5.5's 17-item work-plan checklist is the most reusable asset identified in this entire
  workstream.** It is generic, authored by a standards body, client-independent except for §5.5.2
  (Context), and covers the two things solo consultants most often omit — capacity building and
  knowledge transfer — as _contracting_ items.

- **The reuse risk lives in the repository, not in the methodology.** ISO §4.4.8 and IMC §5.0 together
  say: your methodology is yours, the client's proprietary information is theirs, and you may not use
  the latter for another client without permission. Residuals clauses (F-W8-09) protect only what is
  in your head. A per-client knowledge repository is recorded material and gets none of that
  protection — which argues for a hard structural separation between a _generic methodology repo_ and
  _per-client repos_, with a one-way flow rule (generic → client, never client → generic without an
  explicit de-identification and permission step).

- **The "keep client data local" instinct is directionally right but technically false as stated.**
  There is no local-only configuration of an AI harness that calls a hosted model. The real controls
  are contractual and geographic (F-W8-10, F-W8-11): who the subprocessor is, where they are, what
  the written notice/BAA/DPA says, and whether data is deleted on request.

- **Contract type should key off requirement uncertainty and engagement repetition, not preference.**
  FAR's structural insight (F-W8-13) reads directly onto a diagnostic-then-build practice: the
  diagnostic is high-uncertainty and belongs on a bounded fee with a defined deliverable, whereas the
  build becomes fixed-price-appropriate precisely as the offer repeats across clients. That is the
  mechanism by which productization and pricing are the _same_ problem, not two.

- **Every quantitative pricing claim encountered is C-tier.** Nothing found supports a specific
  price, rate, or margin target for a solo AI/operations consultant. Phase C should not manufacture
  one.

---

## Sources

**Read in full** are marked ⬤. Tier in brackets.

1. ⬤ **ISO 20700:2017, _Guidelines for management consultancy services_** — [full text](<https://nexia.tm/upload/ISO_20700_2017(en).pdf>) (clauses 1–7.5.5, Annexes A, C, D). **[A]** Trusted: international standard, ISO/PC 280, 48 participating countries, developed with ICMCI/CMC-Global. The single most load-bearing source in this file. Distrusted only in that it is guidance with no conformity assessment and no published outcome evaluation.
2. ⬤ **ISO 20700:2017 official preview** — [iTeh/ISO sample PDF](https://cdn.standards.iteh.ai/samples/63501/97bc8b0046b149cea61d4ab922a4ef6f/ISO-20700-2017.pdf). **[A]** Used to confirm the clause numbering and full table of contents against the copy at (1). Cross-check passed.
3. ⬤ **CMC-Global 20700 Toolbox, 1st edition, September 2017** — [PDF](https://www.cmc-global.org/sites/default/files/public/cmc-global_20700_toolbox_-_1st_edition_2017-09.pdf). **[B]** Trusted as the standard's own sponsoring body. Distrusted as substance: it is a 25-slide deck whose operational content is an 18-item yes/no self-declaration and marketing advice.
4. ⬤ **IMC USA Enforceable Code of Ethics** — [imcusa.org](https://www.imcusa.org/about/ethics/code-of-ethics/). **[A]** Trusted: enforceable, a condition of membership and CMC certification, signed in writing. The clearest statement located of the cross-client reuse prohibition (§5.0).
5. ⬤ **26 CFR §301.7216-2 (disclosures without consent)** — [Cornell LII](https://www.law.cornell.edu/cfr/text/26/301.7216-2). **[A]** Binding regulation. Directly resolves C-150.
6. ⬤ **GDPR Article 28 (processor obligations)** — [gdpr-info.eu](https://gdpr-info.eu/art-28-gdpr/). **[A]** Verbatim regulation text; the site is an unofficial mirror but the text is verifiable against the Official Journal.
7. ⬤ **SPI Research, _2025 Professional Services Maturity Benchmark_** — [Kantata mirror](https://get.kantata.com/rs/677-LEJ-696/images/2025-ps-maturity-benchmark.pdf) (front matter, About, Report Organization, Executive Summary and Tables 1–2 read in full; 263-page body sampled/paywalled); [SPI intro & contents](https://spiresearch.com/wp-content/uploads/2025/02/2025-PS-Maturity-Benchmark-Intro-and-Contents-Pages.pdf). **[B]** Trusted for scale and consistency (n=403, 18th annual edition, published size bands and KPI definitions). Distrusted for self-selection, self-reported financials, vendor sponsorship by PSA software companies, unexplained 30% response-base drop, and headline figures expressed as ratios of ratios.
8. **45 CFR §164.504 (HIPAA business associate contracts)** — [Cornell LII](https://www.law.cornell.edu/cfr/text/45/164.504). **[A]** Binding regulation; targeted extraction of (e)(2).
9. **FAR 16.104 (factors in selecting contract type)** — [acquisition.gov](https://www.acquisition.gov/far/16.104). **[A]** Binding regulation. Distrusted for transferability: written for a monopsony public buyer.
10. **FAR 16.601 (time-and-materials contracts)** — [acquisition.gov](https://www.acquisition.gov/far/16.601). **[A]** Same.
11. ⬤ **Venable LLP, _Residual Clauses in an NDA for M&A Transactions_ (2018)** — [venable.com](https://www.venable.com/insights/publications/2018/11/residual-clauses-in-an-nda-for-ma-transactions). **[B]** Trusted as substantive law-firm analysis with two contrasting sample clauses and a cited case. Distrusted for a consistent disclosing-party bias.
12. **Wyrick Robbins, _Understanding the Risks and Benefits of a Residuals Clause_** — [ventures.wyrick.com](https://ventures.wyrick.com/blog/nondisclosure-agreements-understanding-the-risks-and-benefits-of-a-residuals-clause). **[B]** Independent corroboration of (11); same bias.
13. **Galkin Law, _Narrowing the Residuals Clause_** — [galkinlaw.com](https://galkinlaw.com/residuals-clause-in-nda/). **[C]** Sampled only; used solely as a third convergent voice on drafting limits.
14. **Scott & Scott LLP, _Key Provisions in a Master Services Agreement Template_** — [scottandscottllp.com](https://scottandscottllp.com/master-services-agreement-template/). **[C]** Useful as a concrete example of a strongly _provider_-favourable IP position (all Provider Work owned by provider; client licence terminates with the order). Distrusted as a general market description — it is one firm's template for MSP clients.
15. **Anthropic, Commercial Terms of Service (eff. 2025-06-17)** — [anthropic.com](https://www.anthropic.com/legal/commercial-terms). **[A, vendor-primary]** The only source for claims about its own product; flagged as such throughout.
16. **Ko, Kirsch & King (2005), _Antecedents of Knowledge Transfer from Consultants to Clients in Enterprise System Implementations_, MIS Quarterly 29(1):59–86** — [AIS eLibrary](https://aisel.aisnet.org/misq/vol29/iss1/5/). **[A]** Peer-reviewed, matched-pair design, behavioural outcome measure. Abstract and study description read; **full text not obtained** — effect sizes unknown.
17. **Härkönen, Haapasalo & Hänninen (2015), _Productisation: A review and research agenda_, Int. J. Production Economics 164:65–82** — [EconPapers](https://econpapers.repec.org/article/eeeproeco/v_3a164_3ay_3a2015_3ai_3ac_3ap_3a65-82.htm). **[A]** Peer-reviewed literature review; abstract read, full text paywalled. Its own conclusion — that the literature is thin — is the finding.
18. **Gopal, Sivaramakrishnan, Krishnan & Mukhopadhyay (2003), _Contracts in Offshore Software Development: An Empirical Analysis_, Management Science 49(12):1671–1683** — [INFORMS](https://pubsonline.informs.org/doi/10.1287/mnsc.49.12.1671.25120). **[A]** Peer-reviewed; abstract read, full text paywalled. Low external validity for a solo practice (n=93 projects, one Indian vendor, 2003).
19. **Consulting Success, _Consulting Fees & Pricing_** — [consultingsuccess.com](https://www.consultingsuccess.com/consulting-fees). **[C]** Included because it is the only pricing-model distribution with published numbers. Distrusted: undated, self-selected from the publisher's own coaching audience, no methodology section, publisher sells the remedy.
20. **Conductor** — [conductor.build](https://conductor.build/). **[C, vendor marketing]** Consulted solely to attempt verification of C-086; insufficient. No security or privacy documentation located.

---

## Exit-Test Report

- [x] Every ledger claim assigned to W8 has a verdict row with a citation — **2 of 2** (1 REFUTED, 1 UNVERIFIED).
- [x] Every contradiction assigned to W8 addressed — **0 assigned**; stated explicitly.
- [x] Every finding carries an evidence tier, a citation, and a filled `Counter-evidence` field — **20 of 20**.
- [x] Every volatile figure carries a date — SPI figures stamped to calendar 2024 / published 2025-02 / checked 2026-08-01; Anthropic terms stamped to the 2025-06-17 version.
- [x] At least three sources read in full — **7** (ISO 20700 full text; ISO preview; CMC-Global Toolbox; IMC USA Code; 26 CFR §301.7216-2; GDPR Art. 28; SPI front matter + executive summary).
- [x] `Gaps` non-empty — **9 gaps**, including one honest admission of an incomplete search (item 4).
- [x] Findings and inferences separated — `Findings` vs. `Implications for the Operator`.

**Findings by tier:** A — 13 (F-01, 02, 03, 04, 05, 06, 07, 08, 10, 11, 13, 19, 20); A-with-vendor-primary-flag — 1 (F-12); A-for-definition-only — 1 (F-16); B — 3 (F-09, 17, 18); C — 1 (F-15). **Total 20.**
