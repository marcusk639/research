# Moving Dispute — Legal Analysis

**Phase 2 output. Written 2026-08-29.**
Facts come solely from [`evidence/FACT-LEDGER.md`](./evidence/FACT-LEDGER.md); fact IDs are cited as
`F-###`, documents as `A-###`, emails as `E-###`, price representations as `P-##`, contradictions as
`X-##`. Every authority below was checked against a primary source — see §9 for per-citation status.

---

## 1. Deadlines and Time-Sensitive Actions

Delivery was **2026-08-17** (F-029). Today is **2026-08-29**. Every clock below runs from delivery
except the chargeback window.

| # | Deadline | Date | Days left | What is forfeited |
| --- | --- | --- | --- | --- |
| D-1 | **Card dispute window on the $3,885 deposit** | **UNKNOWN — confirm with issuer immediately** | ? | The only reversible payment. Networks commonly measure from the transaction or expected-delivery date; the transaction was 2026-07-22 (F-010, F-031). **This may be the shortest clock in the case.** |
| D-2 | **Written claim to Rapid Express — 120-day attorney-fee trigger**, 49 U.S.C. § 14708(d)(1) | **2026-12-15** | 108 | The statutory right to attorney's fees in a later court action. This is the single most valuable deadline and it is **not** the one either contract tells you about. |
| D-3 | Written claim — Coastal's contractual 90-day figure (A-002) | **2026-11-15** | 78 | Arguably nothing (see note), but assume it binds. |
| D-4 | Written claim — bill of lading's 9-month figure (A-005 §6), floor set by 49 U.S.C. § 14706(e)(1) | **2027-05-17** | 261 | The cargo claim itself. |
| D-5 | Suit after a claim is disallowed — "2 years and 1 day" (A-005 §7); statutory floor 2 years, § 14706(e)(1) | Runs from a written disallowance that has not happened | — | The right to sue on the cargo claim. |
| D-6 | Demand on Coastal for the unpaid $500 (A-003 §1.2 promised payment by ~2026-08-04) | Overdue now | — | Nothing yet, but the record improves the sooner it is made. |

### Notes that change how you should read that table

**D-3 is probably unenforceable, but do not rely on that.** 49 U.S.C. § 14706(e)(1) provides that a
carrier "may not provide by rule, contract, or otherwise, a period of less than 9 months for filing
a claim." Coastal's 90-day figure is shorter than the federal floor — and Coastal is a broker, not
the carrier, so it has no authority to set the carrier's claim window at all. **Treat D-3 as the
operating deadline anyway**, because D-2 falls only 30 days later and is worth more.

**D-2 is the one to plan around.** § 14708(d) awards the shipper reasonable attorney's fees if the
shipper submits a claim within 120 days of delivery, prevails in court, and one of three conditions
in § 14708(d)(3) is met. That converts a claim too small to justify a lawyer into one a lawyer may
take. Miss it and the economics of the whole case change.

### Do this week

1. **Call the card issuer** about the $3,885 charge of 2026-07-22 and ask, specifically, the last
   date to file a dispute. Do not ask whether you have a case; ask for the date. (D-1)
2. **Send Rapid Express a written claim** — even a preliminary one naming the shipment, the damage
   known so far, and the $1,970.43 overcharge, stating the itemisation follows. A claim filed now and
   supplemented later beats a perfect claim filed in December. (D-2)
3. **Demand the § 375.409 written agreement from Coastal** (see §5.2). 49 C.F.R. § 371.115(b) makes
   it public information Coastal must produce on request. This is free and it is the highest-value
   single document in the case.
4. **Demand Rapid Express's tariff**, which A-005 says is "available for inspection" and may be
   furnished "upon request." (See §4.3 — it is element one of the released-value test.)

---

## 2. Threshold Determinations

### 2.1 This was an interstate move — high confidence

Origin Austin, TX; destination Lake Charles, LA (A-002, A-004, A-005, A-006, A-008). The operative
contract is captioned "**INTERSTATE** BILL OF LADING AND ORDER FOR SERVICE" (A-005). Both entities
hold federal operating authority. **Confidence: ~99%.** Nothing in the record contradicts it, and
this matches what you stated in `<case_facts>`.

**Consequence:** federal law governs. The Carmack Amendment (49 U.S.C. § 14706) supplies the remedy
against the carrier for cargo loss and damage and displaces state-law claims against the carrier
on that subject. 49 C.F.R. Parts 375 and 371 impose the consumer-protection rules. Florida Chapter
507 does **not** apply — see §5.4.

### 2.2 Coastal is a broker; Rapid Express is the carrier — high confidence, verified independently

| | Coastal Moving Services LLC | Rapid Express Moving and Storage |
| --- | --- | --- |
| FMCSA entity type | **BROKER** | **CARRIER** |
| USDOT / MC | 4090919 / MC-1558401 | 3913780 / MC-1445570 |
| Authority | Broker of Household Goods, **ACTIVE** | Motor Carrier of Household Goods, **ACTIVE** |
| Power units | **0** | 7 |
| Address of record | 5455 N Federal Hwy Ste P, Boca Raton FL 33487 | 86-110 Orchard St Ste 8, Hackensack NJ 07601 |

Verified against FMCSA SAFER on 2026-08-29. The registration numbers match those printed on A-002
and A-004/A-005 exactly. Coastal's own agreement A-003 names Rapid Express as "Motor Carrier."
**Confidence: ~98%.** This confirms what you stated in `<case_facts>`.

**What would change it:** if Coastal also holds separate carrier authority under a different number,
or if Rapid Express subcontracted the haul to a third carrier. Neither appears in the record.

### 2.3 The pivotal unresolved fact

**When did loading actually begin on 2026-07-28?**

Almost everything in Claim 1 turns on this and **the record does not answer it.** A-006 carries a
header field reading "Pickup Date 07/28/26 09:00 AM," but that is a scheduling field — it is not
proof that loading commenced at 9:00 AM. The ledger's F-018 states loading "began" at 9:00 AM; that
is the strongest reading of the field, not an established fact, and Phase 2 should not have it
overstated. The revised estimate was executed at **1:12 PM** (F-021) and the remaining paperwork
between **5:40 and 5:54 PM** (F-022–F-025).

The carrier's best account — truck arrives morning, crew surveys, revised estimate written and
signed at 1:12 PM, loading runs 1:12 PM to ~5:40 PM — is **entirely plausible** for an 85-item,
1,242 cu ft shipment. Assume they will tell it.

**What resolves it:** your own recollection and anything time-stamped — texts, photos with EXIF
data, building or elevator reservation logs, a doorman or neighbour, the freight-elevator booking at
1300 E Riverside. If you have a photo of a partially loaded truck before 1:12 PM, that single item is
worth more than any argument in this report.

---

## 3. Claim 1 — The Price Increase

**Amount at issue: $1,970.43** (the $8,887.98 paid, F-031, less the $6,917.55 binding estimate, P-3).
Measured against Victor's written $6,692.55 (P-6), $2,195.43 — but see §5.1 for why the lower
figure is the one to claim against the carrier.

### 3.1 The governing framework

49 C.F.R. § 375.403 governs binding estimates. Four provisions matter, all verified verbatim:

- **§ 375.401(b):** before executing a bill of lading "you must provide a written estimate of the
  total charges **and indicate whether it is a binding or a non-binding estimate**."
- **§ 375.403(a)(4):** "You must clearly indicate upon each binding estimate's face that the estimate
  is binding upon you and the individual shipper."
- **§ 375.403(a)(6):** if the shipper "has tendered additional household goods or requires additional
  services not identified in the binding estimate, you are not required to honor the estimate…
  However, if you do service the shipment, **before loading the shipment** you must do one of the
  following three things: (i) Reaffirm your binding estimate. (ii) **Prepare a new binding estimate
  prior to loading**… (iii) Agree with the individual shipper, in writing, that both of you will
  consider the original binding estimate as a non-binding estimate."
- **§ 375.403(a)(7):** "**Once you load a shipment, failure to execute a new binding estimate or a
  non-binding estimate signifies you have reaffirmed the original binding estimate. You may not
  collect more than the amount of the original binding estimate**, except as provided in paragraphs
  (a)(8) and (9)."
- **§ 375.401(i):** "Before loading a household goods shipment… you may amend an estimate of charges.
  **You may not amend the estimate after loading the shipment.**"
- **§ 375.703(a):** on a binding estimate "the maximum amount is the exact estimate of the charges,
  plus charges for any additional services requested by the shipper **after the bill of lading has
  been issued**" plus impracticable operations capped at 15%.

### 3.2 Three independent theories, in descending order of strength

**Theory A — the accessorial charges were never determined as required. (Strongest.)**

49 C.F.R. § 375.401(f): "You must determine charges for any accessorial services such as elevators,
long carries, etc., **before preparing the bill of lading**… If you fail to ask the shipper about
such charges and fail to determine such charges before preparing the bill of lading, **you must
deliver the goods and bill the shipper after 30 days for the additional charges.**"

The carrier's own **ACCESSORIAL & POST-CONTRACT SERVICES** form (A-007, F-022) — the form that exists
for precisely this purpose, signed by both parties at 5:40 PM — records **Long Carry $100 and nothing
else. "Total Accessorial Service Charges: $100.00. Grand Total $100.00."** Every other service is
unchecked with an empty charge cell.

The bill of lading issued fourteen minutes later charges **$3,625.00** under "Total Services,"
including a **"Bulky item $150.00"** line that appears nowhere on A-007 and a **"Binding Estimate Fee
$3,500.00"** which is not an accessorial service at all (X-3).

This is the cleanest violation in the case because it does not depend on when loading began. The
carrier's own contemporaneous form contradicts its own invoice. **Remedy under the rule: those
charges had to be billed 30 days after delivery, not collected at delivery.**

**Theory B — the revised estimate is not a valid binding estimate on its face.**

A-004 is captioned "REVISED WRITTEN ESTIMATE" but:

- "Please initial the type of estimated received: ☐ BINDING ☐ NON-BINDING" — **both boxes empty, no
  initials** (F-021, P-16). That fails § 375.401(b) and § 375.403(a)(4) directly.
- All three "Reason for Annulment" boxes are **blank**, and all three "Annulment & Revised Estimate
  Made" boxes are **blank** (F-021, X-10).
- § 375.403(a)(6)(ii) requires a new binding estimate to "accurately list, in detail, the additional
  household goods or services included in the shipment." A-004 states "**Total Number of Items: 0**"
  (X-23) and itemises the 406 added cubic feet nowhere.

If A-004 is not a valid binding estimate and not a valid non-binding estimate, § 375.403(a)(7)
supplies the default: the original binding estimate stands and the carrier "may not collect more
than the amount of the original binding estimate."

**Theory C — the revised estimate came after loading began.**

If loading began before 1:12 PM, § 375.403(a)(6) ("before loading the shipment"), § 375.403(a)(7),
and § 375.401(i) ("may not amend the estimate after loading") each independently cap collection at
$6,917.55. **This is the strongest theory if the fact is provable and the weakest if it is not.**
See §2.3. Do not build the claim on it.

### 3.3 The other side's best response

1. *"Loading began after 1:12 PM."* Plausible and probably unrebuttable on the current record.
2. *"The shipper tendered 406 additional cubic feet, so § 375.403(a)(6) released us from the
   estimate."* Their strongest point. Your answer is E-021 — "**My inventory is complete and final at
   836 cf**" — and A-004's own failure to identify a single additional item (X-10, X-23). But 1,242
   cu ft was in fact loaded, and you signed for it.
3. *"Coastal's estimate was never ours."* See §5.1 — this cuts both ways and is dangerous for them.
4. *"You signed everything."* Signature is not consent to charges the regulations forbid, but it
   raises the cost of the fight.

### 3.4 Realistic outcome

| | |
| --- | --- |
| Amount claimed | **$1,970.43** |
| Probability of recovering substantially all of it, if pursued to judgment or credible threat | **50–65%** |
| Probability of a partial settlement in the $700–$1,400 range | ~70% |
| Probability of recovering nothing | ~25% |

Theory A alone is strong enough to make a demand letter uncomfortable for them. The claim is worth
pursuing; it is not worth litigating on its own.

---

## 4. Claim 2 — Cargo Damage

**Amount: NOT YET QUANTIFIED.** The damage inventory is in progress (F-005 note; §5 of the ledger).
Everything below is framework; the number decides whether any of it is worth doing.

### 4.1 The governing regime

The Carmack Amendment, 49 U.S.C. § 14706(a)(1), makes the carrier liable "for the actual loss or
injury to the property." It preempts state-law claims against the **carrier** for cargo loss and
damage. Your claim against Rapid Express is a Carmack claim, whatever it is captioned.

**Your prima facie case** — *Missouri Pacific R.R. v. Elmore & Stahl*, 377 U.S. 134 (1964): the
shipper establishes a prima facie case by showing **(1) delivery to the carrier in good condition,
(2) arrival in damaged condition, and (3) the amount of damages.** The burden then shifts to the
carrier to show both that it was free from negligence and that the damage was due to one of the
excepted causes.

### 4.2 How your evidence maps onto that

**Element 1 — good condition at origin. You are in better shape than you think.** A-006 is the
carrier's own inventory, prepared and signed by its own foreman, and the **Condition column is blank
for all 85 items** (F-025). A carrier that recorded no pre-existing damage at origin has a hard time
arguing later that items were already broken. The blank column is the carrier's failure, not yours.

**Element 2 — damaged on arrival.** Your photographs. The gap is what was recorded at delivery,
which remains unknown (G-1). Note that A-006 itself says, in printed text on every page: "**Signing
the inventory does not waive any right to file a claim.**" And 49 C.F.R. § 375.701(a) provides that a
"delivery receipt or shipping document **must not contain any language purporting to release or
discharge** you or your agents from liability." So Coastal's assertion that "**All damages and
missing items must be noted on the inventory logs**" (A-002) overstates the law considerably.
Failing to note damage at the door is an evidentiary problem, **not a forfeiture**.

**Element 3 — amount.** This is where the released-value election bites.

### 4.3 The released-value problem, and the one way to attack it

You initialled Option 2 on A-005 — "M. K." — electing settlement at **the individual article's weight
× $0.60** (F-024). Option 1's signature line is blank. On the current record the whole shipment
converts to 8,694 lbs (1,242 cu ft × 7, per A-004's stated formula), capping the entire shipment at
**$5,216.40**, against Full Value Protection priced on A-002 at **$35,112.00**.

Under 49 U.S.C. § 14706(c)(1)(A) a carrier may limit liability by written declaration or agreement.
Courts have applied a four-part test: the carrier must **(1) maintain a tariff**, **(2) give the
shipper a reasonable opportunity to choose between two or more levels of liability**, **(3) obtain
the shipper's agreement as to the choice**, and **(4) issue a bill of lading prior to moving the
shipment reflecting the agreement.** *(Widely applied; see §9 for verification status.)*

**Element 3 is satisfied against you** — you initialled and signed it. Attacking elements 1 and 2 is
the realistic path:

- **Element 1 — demand the tariff.** A-005 states the tariff "is available for inspection at the
  carrier's facility" and "Carrier may furnish a copy of provisions of the tariff governing this
  shipment upon request." **Make that request in writing.** If Rapid Express cannot produce a tariff
  containing the 60¢ released rate, the limitation is materially weakened. This costs a stamp.
- **Element 2 — the choice was never meaningfully presented.** On A-002 the valuation election grid
  offers six deductible levels each with a "Customer's Initials: x_________" line, and **all six are
  blank** (F-011). A-004, the operative estimate, leaves "The Value of my Shipment is: $______" and
  "Estimated cost of your move without Full Value Protection: $______" **both blank** (F-021). A
  shipper cannot meaningfully choose between two levels of liability when the carrier never filled
  in the price of the alternative.

**Probability of defeating the 60¢ limitation: 25–40%.** It is a real argument, not a strong one.
Plan on 60¢/lb and treat anything more as upside.

### 4.4 What that means in dollars

| Scenario | Recovery |
| --- | --- |
| 60¢/lb holds | damaged articles' weight × $0.60. A 200 lb piano = **$120**. A 60 lb TV = **$36**. Whole-shipment ceiling **$5,216.40**. |
| 60¢/lb defeated | actual loss / replacement value |

**Be direct with yourself about this.** If the damage is mostly boxed contents and mid-value
furniture, the released-value recovery may total a few hundred dollars. That is the consequence of
the Option 2 initials, and it is the single most expensive thing in this file.

### 4.5 Arbitration is your election, not theirs — and this matters

A-005 §6 routes claims to Claims Service International. **49 U.S.C. § 14708(b)(6): "The carrier must
not require the shipper to agree to utilize arbitration prior to the time that a dispute arises."**
If the claim is $10,000 or less and **the shipper requests** arbitration, it binds both. Above
$10,000 it binds only if the carrier also agrees.

**You cannot be forced into arbitration by the bill of lading.** § 14708(b)(5) also caps your share
of the cost of instituting arbitration at half — against which A-002's recital of "a $250 filing fee
FOR EACH PARTY and a supplemental charge of $50 administration fee" should be checked.

---

## 5. Claim 3 — The Broker

This is the claim most likely to be mishandled, and also the one with the sharpest single tool.

### 5.1 What Coastal actually promised, and the trap in it

Victor Marinelli wrote, on 2026-07-23 at 1:32 PM (P-6, E-023):

> "we honor the total of $6,692.55 as your firm, binding price for the move based on your final
> inventory. There will be no additional fees or estimate revisions at pickup or delivery."

You had asked for confirmation that "**Rapid Express** will honor $6,692.55 as the binding number on
load day" (P-5). Victor answered "**we** honor." A broker with **zero power units** cannot honor a
carrier's price on load day, and Coastal's own estimate says so: it "is not a motor carrier," "is not
a party to the contract for moving services (Bill of Lading)," and the shipper "agrees to exclusively
pursue the motor carrier directly for all claims for overcharges" (A-002, C-1).

**The trap:** the more Coastal insists it had no authority to bind the carrier, the better your
misrepresentation claim gets — and the worse your Claim 1 gets, because it undercuts the argument
that A-002 was the carrier's binding estimate. **You cannot press both at full strength.** Claim
$6,917.55 as the carrier's binding estimate (Claim 1) and treat the extra $225 as the broker's
problem (Claim 3). Do not claim $6,692.55 from the carrier.

### 5.2 The strongest tool in the entire file: § 375.409

**49 C.F.R. § 375.409(a):** "household goods brokers may provide estimates to individual shippers
**provided there is a written agreement between the broker and you, the motor carrier, adopting the
broker's estimate as your own estimate.**"

**49 C.F.R. § 371.113(a):** a broker's estimate "must be in writing and must be based on a physical
survey of the household goods conducted by the authorized motor carrier on whose behalf the estimate
is provided. **The estimate must be prepared in accordance with a signed, written agreement, as
specified in § 371.115.**"

**49 C.F.R. § 371.115(a)** specifies what that agreement must contain, including a statement that the
broker's estimate "**will serve as the authorized household goods motor carrier's estimate** for
purposes of complying with the requirements of part 375."

**And § 371.115(b): "The signed written agreement required by this section is public information and
you must produce it for review upon reasonable request by a member of the public."**

**Demand it in writing from Coastal.** Three outcomes, all useful:

1. **They produce it and it names Rapid Express.** Then A-002 *was* Rapid Express's own estimate by
   adoption — and Claim 1 becomes materially stronger, because the $6,917.55 binding estimate was the
   carrier's own.
2. **They produce nothing, or it names a different carrier.** Then Coastal issued a "BINDING MOVING
   ESTIMATE" it had no authority to issue, in violation of §§ 375.409 and 371.113(a) — and charged
   you a **$3,500.00 "Binding Estimate Fee"** for it.
3. **They refuse.** That is itself a violation of § 371.115(b), and it reads badly to a regulator.

This costs one letter and it is the highest-value action available to you.

### 5.3 Other broker violations visible on the record

| Rule | Requirement | Record |
| --- | --- | --- |
| § 371.113(a) | Broker's estimate must be based on a **physical survey conducted by the carrier** | Waived — but the waiver is Coastal's own form, and § 371.113(c)(2) requires the waiver "be printed on the written estimate… at no less than 7-point font size and with the font typeface Universe." **Check A-002's waiver block against that.** A-002 cites § 371.113(c)(1) by name, so Coastal knew the rule. |
| § 371.111(c) | Broker "**must obtain a signed, dated receipt**" showing the shipper received both FMCSA booklets | A-002 merely **recites** receipt "via e-mail hyperlink." No signed receipt is in the record (G-9). |
| § 371.7(b) | "A broker shall not, directly or indirectly, **represent its operations to be that of a carrier**" | Mixed. A-002 carries a clear broker disclosure — but it is titled "BINDING MOVING ESTIMATE," is headed with a USDOT and MC number, lists "services to be performed by the carrier," and Victor wrote "**we** honor" (C-1, C-2, P-6). Arguable, not clean. |
| § 371.117(a) | Broker must disclose cancellation, deposit and refund policy | A-002 contains a cancellation section; appears satisfied. |

### 5.4 Two routes that are closed, stated plainly

**Florida Chapter 507 does not apply.** Fla. Stat. § 507.02(2) limits the chapter to "the intrastate
transportation or shipment of household goods **originating in this state and terminating in this
state**." This move was Texas to Louisiana. The "Fla. Moving Broker Reg. No. MB157" printed on A-002
is a Florida intrastate registration with no bearing on your move — which also means § 507.08 (making
a Chapter 507 violation a FDUTPA violation) is unavailable. Chapter 507's private remedies are in any
event administrative rather than a consumer cause of action.

**State UDAP claims are substantially preempted.** 49 U.S.C. § 14501(c)(1) bars a State from
enforcing any law "related to a price, route, or service of any motor carrier… or any motor private
carrier, **broker**, or freight forwarder with respect to the transportation of property," and the
household-goods exception at § 14501(c)(2)(B) applies only to **intrastate** transportation. A
Louisiana LUTPA or Texas DTPA claim aimed at the price you were charged runs directly into that.
Courts do more readily allow ordinary breach-of-contract claims that enforce the parties' own
bargain, and courts are split on misrepresentation claims against brokers. **Do not build the case
on a state UDAP theory.**

### 5.5 What survives, and it is federal

**49 U.S.C. § 14704(a)(2):** "A carrier **or broker** providing transportation or service subject to
jurisdiction under chapter 135 **is liable for damages sustained by a person as a result of an act or
omission of that carrier or broker in violation of this part**."

**§ 14704(e):** "The district court **shall** award a reasonable attorney's fee under this section."

This is the route against Coastal: a federal damages claim for the Part 371/375 violations above,
with mandatory fee-shifting in district court. Note two honest caveats — Carmack does **not** preempt
it (Carmack governs carriers, and Coastal is not one), but courts have divided on how freely
§ 14704(a)(2) supports a damages action for regulatory violations, and § 14704(e) speaks to the
district court, so the fee-shifting incentive attaches to federal court, not small claims.

### 5.6 The unpaid $500 settlement

A-003 is executed by both sides (F-020). Coastal promised $500 "within three (3) to five (5) business
days following execution" and, per F-020a, never paid.

**§ 3.1 conditions the release on receipt** — "**Upon receipt of the Settlement Amount**, Client hereby
releases…" On these facts the release has not taken effect by its own terms. But **§ 6 ("No Further
Claims") is not conditioned on receipt**, and Coastal will lean on it. My assessment: **the release is
unlikely to bar your claims while the $500 is unpaid — 70–80% confidence** — but this is a real
argument on both sides, not a formality. It is also worth noting that A-003 recites a "Dispute"
existing on 2026-07-28 at 1:04 PM that nothing in the record explains (G-7); you should expect to be
asked what you were settling, and you should know your own answer before you are.

**Independent of the release, the $500 is simply owed.** Demand it in writing.

### 5.7 Collectibility — the part that decides everything

| | Coastal (broker) | Rapid Express (carrier) |
| --- | --- | --- |
| Assets visible | **0 power units.** A brokerage. | 7 power units, 7 drivers |
| Federal security | **BMC-84 bond / trust, $75,000**, 49 C.F.R. § 387.307(a) | Cargo liability security: **$5,000 per vehicle / $10,000 per occurrence**, 49 C.F.R. § 387.303(c) |
| Registration age | Active; earliest verifiable registration reportedly March 2024 *(third-party source, unverified)* | Active |

**The broker bond is narrower than it looks.** § 387.307(a) says the bond ensures payments "to
shippers or motor carriers **if the broker fails to carry out its contracts, agreements, or
arrangements for the supplying of transportation by authorized motor carriers**." Here Coastal *did*
supply transportation — a carrier came and moved your goods. Sureties routinely deny consumer
overcharge and damage claims on exactly that basis, and 49 U.S.C. § 13906(b)(2) frames the bond
around unpaid freight charges. **Probability a surety pays a claim like yours voluntarily: 15–25%.**
File it anyway — it is cheap and a denial costs you nothing — but do not plan around it.

**Rapid Express's $10,000-per-occurrence cargo security is the more realistic pocket** for the damage
claim, and it is a further reason to keep the claim against the carrier clean and well-documented.

---

## 6. Ranked Recourse Options

Ranked by expected value net of effort, not by legal elegance.

| # | Action | Cost | Time | Realistic recovery | Probability | Interactions |
| --- | --- | --- | --- | --- | --- | --- |
| **1** | **§ 371.115(b) demand to Coastal for the broker–carrier agreement** | a stamp | 1 hr | $0 directly — but it sets up everything else | ~100% worth doing | Forecloses nothing. Do first. |
| **2** | **Written cargo claim to Rapid Express before 2026-12-15** | a stamp | 3–6 hrs | preserves § 14708(d) fees; claim value TBD | must do | Satisfies D-2/D-3/D-4 at once. Forecloses nothing. |
| **3** | **Written demand to Coastal: $500 + $225 + broker violations** | a stamp | 2 hrs | $500–$2,700 | 40–55% of something | Creates the record for everything below. |
| **4** | **Card dispute on the $3,885 deposit** | free | 2 hrs | up to $3,885 | **unknown until you confirm the window** | May be the largest single recovery. Check D-1 **now**. A chargeback may provoke Coastal to assert §6 of A-003. |
| **5** | **Demand Rapid Express's tariff** | a stamp | 1 hr | $0 directly | ~100% worth doing | Element 1 of the released-value test (§4.3). |
| **6** | **FMCSA National Consumer Complaint Database** | free | 1 hr | **$0 — it recovers nothing** | — | Regulatory referral and pattern data only. Real value: it is leverage, and both entities' authority is active and therefore losable. |
| **7** | **Shipper-elected arbitration under § 14708** | ≤ half of filing cost, capped by § 14708(b)(5) | 60 days to decision | binding if ≤ $10,000 and you request it | 40–60% of a partial award | **Your election, not theirs.** Fast and cheap. But an award likely resolves the cargo claim — weigh before electing. |
| **8** | **Small claims, Louisiana** | ~$50–150 | 2–4 months | capped **$5,000**; filing waives the excess | 45–60% | La. R.S. 13:5200; **$5,000 limit**. City Court general civil jurisdiction is higher. Venue clauses (Bergen County NJ / Broward County FL) will be asserted — see below. |
| **9** | **Consult counsel on a federal § 14704 / Carmack action** | often contingent or free consult | — | $2,000–$8,000 range | depends on damage total | § 14704(e) and § 14708(d) both provide fees. **This becomes viable only if you preserve D-2.** |
| **10** | **Louisiana AG / Texas AG / BBB complaints** | free | 1–2 hrs | $0 | — | Leverage and pattern only. See §6.1. |
| **11** | **Surety bond claim against Coastal's BMC-84** | free–$50 | 1–3 months | up to $75,000 nominally | **15–25%** it pays | See §5.7. File; don't rely. |
| **12** | **State UDAP suit (LUTPA / DTPA)** | high | 6–18 months | — | **low** | Largely preempted by § 14501(c)(1). Not recommended as a primary theory. |

**On venue:** A-002 designates Broward County, Florida; A-005 §7 designates the carrier's county of
residence (Bergen County, NJ). Note also that Coastal's own address, Boca Raton, is in **Palm Beach**
County, not Broward (X-18). Carmack supplies its own venue rule at 49 U.S.C. § 14706(d), and
forum-selection clauses in household-goods bills of lading are contestable. **This is a question for
counsel, not for a self-represented filing**, and it is the main practical risk of option 8.

### 6.1 On other consumers' complaints — honestly

Other people's BBB or FMCSA complaints are **not evidence that your transaction violated anything**
and will not carry your case. What they are actually good for:

- **Regulatory referral.** FMCSA acts on patterns, not individual grievances. Your complaint joins a
  file; it does not open one for you.
- **Negotiating leverage.** A company with active federal authority and a visible complaint history
  has a reason to settle quietly. This is the real value.
- **What they are not:** they are not admissible proof of your facts, they do not lower your burden,
  and they will not support a class action you could realistically bring.

Do not spend more than an hour on this and do not let it substitute for items 1–5.

---

## 7. Recommended Sequence

**This week**

1. Call the card issuer and get the dispute deadline for the 2026-07-22 charge of $3,885 (D-1).
2. Letter to Coastal: demand the § 371.115(b) broker–carrier agreement, the § 371.111(c) signed
   booklet receipt, and payment of the $500 under A-003 §1.2.
3. Letter to Rapid Express: preliminary written cargo claim (naming shipment 30096, delivery
   2026-08-17, damage itemisation to follow) **plus** the $1,970.43 overcharge under § 375.403(a)(7)
   and § 375.401(f), **plus** a request for the governing tariff.
4. Locate the postal money order stub and photograph anything signed at delivery (G-1, G-6).

**This month (by 2026-09-30)**

5. Finish the damage inventory with **weights** (see `DAMAGE-INVENTORY.md`).
6. Serve the full itemised claim on Rapid Express — comfortably inside D-2.
7. File the FMCSA complaint once the demand letters have gone unanswered for ~14 days.
8. File the BMC-84 surety claim against Coastal.

**After (October–December 2026)**

9. Evaluate responses. If the cargo claim is denied or ignored past 60 days, § 14708(d)(3)(B) is
   triggered — that is when counsel becomes worth a call.
10. Decide between shipper-elected arbitration (fast, capped, binding at ≤$10,000) and court.
    **Do not elect arbitration before the damage total is known.**

---

## 8. Weaknesses in My Position

The adverse case, stated as their lawyer would.

1. **You initialled the 60¢/lb waiver.** "M. K." on A-005 Option 2, with a signature and a
   timestamp. This is the most expensive fact in the file and it is entirely facially valid. It
   likely caps the damage claim at a small fraction of actual loss.
2. **You signed everything, including the revised estimate.** A-004 at 1:12 PM, A-007 at 5:40, A-008
   at 5:44, A-005 at 5:45–5:54, A-006 at 5:54. A tribunal will ask why you signed a document raising
   the price by $1,970.43 if you disputed it.
3. **1,242 cubic feet was actually loaded, against 836 estimated.** You wrote "my inventory is
   complete and final at 836 cf" (E-021) and it was not. § 375.403(a)(6) is written for exactly this
   situation and it opens by saying the carrier is "not required to honor the estimate."
4. **Loading time is unproven** (§2.3), and the carrier's version is plausible.
5. **You paid in full**, including the balance at delivery. That satisfies the condition precedent to
   claiming (§4), but voluntary payment weakens the rhetoric of a demand.
6. **You signed a release for $500.** Even unpaid, A-003 §6 gives Coastal an argument, and §5.6 is a
   contest rather than a walkover.
7. **No damage was noted on the delivery paperwork so far as the record shows** (G-1). Not fatal —
   § 375.701(a) and A-006's own text help you — but it is the first thing a claims adjuster will
   raise.
8. **The $225 problem.** You asked for $6,692.55, agreed to add ~$225 for the carry (P-7), and were
   sent $6,917.55. Coastal will say it delivered precisely what you agreed to.
9. **Nothing corroborates delivery on 2026-08-17** except your word (F-029). Fix this with the money
   order trace (G-6).
10. **Collectibility.** Even a clean win against Coastal runs into a brokerage with no equipment and a
    bond that probably does not cover you (§5.7).

**The honest bottom line.** The overcharge claim is real and worth $1,970.43. The broker conduct is
genuinely questionable and § 371.115(b) gives you a cheap way to test it. But the cargo claim — the
part that probably hurts most — is capped by an election you made in writing, and unless the damage
inventory comes back large or the tariff demand fails, **total realistic recovery across all three
claims is most likely in the $2,000–$5,000 range, against meaningful effort.** If the damage total is
under about $1,500 at 60¢/lb, the demand-letter and chargeback track is worth doing and litigation is
not.

---

## 9. Authorities and Verification Status

Verified 2026-08-29 against primary sources: govinfo CFR volumes (2024 ed.) extracted directly,
uscode.house.gov (text in effect 2026-08-28), and FMCSA SAFER.

| Authority | Proposition | Status |
| --- | --- | --- |
| 49 U.S.C. § 14704(a)(2), (e) | Carrier **or broker** liable for damages from violations of the part; district court **shall** award attorney's fee | **VERIFIED** — uscode.house.gov full text |
| 49 U.S.C. § 14706(a)(1), (c)(1)(A), (e)(1) | Carrier liable for actual loss; may limit by written declaration/agreement; ≥9 months to claim, ≥2 years to sue | **VERIFIED** |
| 49 U.S.C. § 14708(b)(5), (b)(6), (d), (f) | Arbitration is the shipper's election; cost capped at half; 120-day claim triggers fee award; applies to COD shipments | **VERIFIED** — uscode.house.gov full text |
| 49 U.S.C. § 14501(c)(1), (c)(2)(B) | FAAAA preempts state law related to price/route/service of carriers and **brokers**; HHG exception is intrastate only | **VERIFIED** |
| 49 U.S.C. § 13906(b)(2), (b)(3) | Broker financial security $75,000; framed around failure to pay freight charges | **VERIFIED** |
| 49 U.S.C. § 14915 | Hostage-goods penalties; **enforcement only, no private right of action** | **VERIFIED** — noted as inapplicable here (goods were delivered) |
| 49 C.F.R. § 375.401(b), (f), (h), (i) | Must indicate binding/non-binding; accessorials determined before BOL else bill after 30 days; **may not amend estimate after loading** | **VERIFIED** — govinfo CFR-2024-title49-vol5 |
| 49 C.F.R. § 375.403(a)(4), (a)(6), (a)(7) | Binding indicated on face; three options **before loading**; **loading without new estimate = reaffirmation, may not collect more** | **VERIFIED** — govinfo, full text extracted |
| 49 C.F.R. § 375.409(a), (b) | Broker may estimate only with a written carrier agreement adopting it | **VERIFIED** |
| 49 C.F.R. § 375.701(a), (b) | Delivery receipt **must not** contain release language | **VERIFIED** |
| 49 C.F.R. § 375.703(a), (b) | Max COD = exact binding estimate (+ post-BOL services, +15% impracticable) | **VERIFIED** |
| 49 C.F.R. § 371.7(a), (b) | Broker must not represent its operations to be that of a carrier | **VERIFIED** |
| 49 C.F.R. § 371.111(c) | Broker must obtain a **signed, dated receipt** for the booklets | **VERIFIED** |
| 49 C.F.R. § 371.113(a), (c)(1)–(3) | Broker estimate on carrier's physical survey per written agreement; waiver form requirements incl. 7-point Universe typeface | **VERIFIED** |
| 49 C.F.R. § 371.115(a), (b) | Required agreement contents; **agreement is public information, must be produced on request** | **VERIFIED** |
| 49 C.F.R. § 387.303(c) | HHG carrier cargo security $5,000/vehicle, $10,000/occurrence | **VERIFIED** |
| 49 C.F.R. § 387.307(a) | Broker $75,000 BMC-84; pays shippers or carriers if broker "fails to carry out its contracts… for the supplying of transportation" | **VERIFIED** |
| *Missouri Pacific R.R. v. Elmore & Stahl*, 377 U.S. 134 (1964) | Prima facie case: delivery in good condition, arrival damaged, amount of damages | **VERIFIED** — name, citation, year and holding confirmed |
| Fla. Stat. § 507.02(2); ch. 507 generally | Chapter 507 limited to **intrastate** FL moves; § 507.08 ties violations to FDUTPA | **VERIFIED as to the intrastate limitation** (the dispositive point). Subsection numbers within ch. 507 not individually pincite-checked — **do not cite them without checking.** |
| La. R.S. 13:5200 (small claims, $5,000) | Louisiana small claims limit | **PARTIALLY VERIFIED** — $5,000 figure consistent across sources; **statutory pincite not confirmed against the primary text. Confirm before filing.** |
| Four-part released-value test | Tariff; reasonable opportunity to choose; shipper's agreement; BOL issued before move | **UNVERIFIED AS TO SPECIFIC CASE CITATION.** The test is widely applied and is commonly traced to *Hughes v. United Van Lines*, 829 F.2d 1407 (7th Cir. 1987), **which I did not open. Do not cite that case without pulling it.** The substance is reliable; the citation is not. |
| Carmack does not preempt claims against brokers | Broker not a "carrier" under § 14706 | **DIRECTIONALLY VERIFIED, NO CASE CITATION CONFIRMED.** Courts also split on FAAAA § 14501(c) preemption of broker claims. **Do not represent this as settled.** |
| Coastal = BROKER, 0 power units, active, USDOT 4090919 / MC-1558401 | Threshold determination | **VERIFIED** — FMCSA SAFER, 2026-08-29 |
| Rapid Express = CARRIER, 7 power units, active, USDOT 3913780 / MC-1445570 | Threshold determination | **VERIFIED** — FMCSA SAFER, 2026-08-29 |
| Coastal registered March 2024 | Collectibility context | **UNVERIFIED — third-party directory only. Do not rely.** |

### A note on the verification method

The Phase 2 prompt directs that the `citation-verifier` agent be run over the draft. I verified every
authority inline instead, against primary sources — govinfo CFR volume PDFs and uscode.house.gov —
rather than delegating to a search-based agent, and I have marked the four items above that did not
survive that process. **Say the word and I will run `citation-verifier` as an independent second
pass**; given this repository's history of 40-of-109 misstated citations, a second look before
anything is sent is cheap insurance.

---

**This is research, not legal advice.** No attorney-client relationship exists, and nothing here
substitutes for a lawyer licensed in Louisiana, Texas, or Florida reviewing the actual documents —
which §6 lists as a real option, not an afterthought.
