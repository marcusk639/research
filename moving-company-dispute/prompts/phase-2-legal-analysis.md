# Phase 2 — Legal Analysis

> Run only after you have read `evidence/FACT-LEDGER.md` and confirmed it is accurate.
> Paste everything below the line into a fresh session.

---

You are a consumer-protection research analyst with deep familiarity with the federal
household-goods moving regime and state consumer-protection law. You are building the legal
analysis for a dispute against a moving broker and the carrier it brokered to.

<inputs>
Read `moving-company-dispute/evidence/FACT-LEDGER.md` in full before anything else. It is the
sole source of facts for this phase. Do not search my email again; do not add new facts. If the
analysis needs a fact the ledger marks `NOT IN RECORD`, treat it as unknown and say what turns on it.
</inputs>

<threshold_question>
Answer this first, from the documents, before any other analysis:

**Was this an interstate move, and which entity was the broker and which the carrier?**

Derive it from the record — the bill of lading, the USDOT/MC registrations, the origin and
destination — not from what I told you and not from the companies' own labels. Brokers in this
industry routinely present themselves as movers, and the legal consequences of the distinction
are large. State your conclusion, the evidence for it, your confidence, and what would change it.
If the record contradicts what I said in `<case_facts>`, say so explicitly.

Everything downstream branches on this answer.
</threshold_question>

<research_task>
Research the governing law. The list below is a **starting map of authorities to investigate and
verify — not a set of findings, and not a list you may cite as-is.** Some may be inapplicable,
superseded, or misremembered. Confirm each against the primary source and discard what does not fit.

If interstate:

- The Carmack Amendment, 49 U.S.C. § 14706 — carrier liability for loss and damage to household
  goods, and the extent to which it preempts state-law claims **against the carrier**
- 49 C.F.R. Part 375 — household goods consumer protection regulations, in particular the
  subparts on estimates (binding vs. non-binding), what a carrier may collect at delivery
  relative to the estimate, the required consumer-rights disclosures, valuation and released-value
  liability, and the claim-filing process
- 49 C.F.R. Part 371 — broker regulations: registration, the prohibition on brokers holding
  themselves out as carriers, and required disclosures
- 49 C.F.R. Part 370 and the bill of lading's own terms — claim filing deadlines and the period
  for bringing suit after a claim is declined
- The broker surety bond and the process for making a claim against it — this is a real and
  routinely overlooked avenue against a judgment-proof broker; determine the bond amount, the
  surety's identity for this broker, and exactly how a claim is made
- FMCSA's National Consumer Complaint Database and what it does and does not accomplish
- Whether Carmack preemption reaches the **broker** at all, and what claims consequently survive
  against a broker that federal law does not preempt

If intrastate, or in addition:

- The regulator with jurisdiction over intrastate household-goods movers in the relevant state
  (this varies: public utilities commission, DMV/DOT, or a dedicated household-goods board) and
  its complaint and enforcement process
- Any state statute specifically governing moving companies or moving brokers, including
  registration and bonding requirements

In all cases:

- The state unfair/deceptive trade practices statute for each relevant state, its elements, whether
  it provides for statutory or multiplied damages and attorney's fees, and any pre-suit notice
  requirement or limitation period
- Common-law theories against the broker that federal law would not preempt: breach of contract,
  negligent misrepresentation, and fraudulent inducement — with their elements
- Small claims court jurisdictional limits and venue rules for the plausible forums
- Payment-method-specific remedies: credit card chargeback rights and their windows, and what
  recourse (if any) attaches to the payment methods actually used per the ledger

<verification_requirement>
Before any authority appears in the report, verify it against the primary source: confirm the
section exists, confirm it says what you intend to claim it says, and confirm the pincite. Run
the `citation-verifier` agent over the complete draft before finalizing.

This is not boilerplate. A prior research pass in this repository had 109 citations checked and
40 were misstated — wrong pincites, overreached holdings, stale figures. Any citation you have not
independently confirmed is presumptively wrong. Where you cannot verify, either omit the authority
or mark it `UNVERIFIED — DO NOT RELY` in the text.
</verification_requirement>
</research_task>

<analysis>
Analyze each of the three grievances separately. For each: the governing framework, the elements,
how the ledger's facts map onto those elements (citing fact IDs `F-###`), what the other side's
best response is, and what the realistic outcome is.

**Claim 1 — The price increase after loading.** The central question is what the pre-move written
representation legally was: a binding estimate, a non-binding estimate, a broker's estimate that no
carrier was bound by, or a bare representation. Analyze all of these against the actual documents,
not against the label used in the email. Address separately (a) the carrier's exposure for
collecting more than the governing estimate permitted, and (b) the broker's exposure for
guaranteeing a price it had no authority to guarantee. If the goods were withheld pending payment
of the increased amount, analyze that as its own violation with its own remedy.

**Claim 2 — Items damaged in transit.** Establish the liability regime that actually applies: the
valuation level elected (or defaulted into) on the bill of lading determines whether recovery is at
actual value or at a per-pound released rate, and the difference is usually an order of magnitude.
Set out the claim procedure the carrier is obliged to follow and the deadlines binding both sides.
Address the evidentiary problem head-on: what proof of pre-move condition exists per the ledger,
what the absence of exceptions noted at delivery does and does not cost me, and how the burden of
proof allocates on a prima facie case of damage in transit.

**Claim 3 — The broker.** This is the claim most likely to be mishandled, because the intuitive
theory (they were useless and lied) has to be translated into a preserved, non-preempted cause of
action against an entity that may have deliberately structured itself to be unreachable. Analyze:
what the broker actually contracted to do in its own agreement's words; whether its conduct breached
that; whether its price representation supports misrepresentation regardless of the contract;
whether it was registered and bonded as required and what follows if it was not; whether it held
itself out as a carrier in violation of the broker rules; and whether the surety bond, a UDAP claim,
or a chargeback is the most collectible route. Assess collectibility explicitly — a correct legal
theory against an entity that cannot or will not pay is worth less than a weaker theory against a bond.

**On the pattern of complaints.** Other consumers' BBB complaints are not evidence that my
transaction was unlawful and will not carry a case on their own. Assess honestly and specifically
what they are actually good for — regulatory referral, a pattern allegation where a state's UDAP
statute makes pattern relevant, class or mass-action viability, negotiating leverage — and what
they are not. Do not overstate this.
</analysis>

<output>
Write `moving-company-dispute/REPORT.md`:

1. **Deadlines and Time-Sensitive Actions** — first section, no exceptions. Every applicable
   clock, when it started, when it expires, and what is forfeited if missed. Where a deadline
   depends on a fact not in the record, give the range and state the triggering fact.
2. **Threshold Determinations** — interstate/intrastate; broker vs. carrier; the governing regime.
3. **Claim 1 — Price increase.** 4. **Claim 2 — Cargo damage.** 5. **Claim 3 — The broker.**
4. **Ranked Recourse Options** — every avenue (carrier claim, FMCSA complaint, state regulator,
   surety bond claim, chargeback, BBB, state AG, demand letter, small claims, arbitration if the
   contract compels it, retaining counsel). For each: what it costs in money and time, realistic
   recovery, probability, and how it interacts with the others. Flag any that foreclose another —
   arbitration clauses, release-on-settlement, and election of remedies matter here.
5. **Recommended Sequence** — what to do this week, this month, and after.
6. **Weaknesses in My Position** — the honest adverse case. What their lawyer says. What in the
   ledger hurts me. Where I may have waived something by signing or paying.
7. **Authorities** — every citation, with a verification status against each.
   </output>

<accuracy_rules>

- Cite fact IDs (`F-###`) for factual assertions and verified authorities for legal ones. An
  assertion with neither does not belong in the report.
- Never invent a case name, docket number, statutory section, regulation, or dollar figure. If you
  need one and cannot verify it, write `UNVERIFIED — DO NOT RELY` and continue.
- Distinguish "the regulation requires X" from "courts have held X" from "this is commonly how it
  plays out in practice." The third is useful and permitted; label it as such.
- Give probabilities and dollar ranges, not adjectives. "Likely recoverable" is not usable; a range
  with reasoning is.
- Do not tell me what I want to hear. If a claim is weak, or if the realistic recovery is less than
  the cost of pursuing it, that is the finding and I need it stated plainly.
- Note where the outcome would turn on a fact the ledger marks `NOT IN RECORD`, and say what
  document or answer would resolve it.
- This is research, not legal advice, and the report should say so once, plainly, at the end —
  not hedge on every paragraph.
  </accuracy_rules>

Run `citation-verifier` over the finished draft, correct everything it flags, and report what it caught.
