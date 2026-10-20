You are documenting a business I am building, called (for now) the Private AI venture. Everything you need is in the SOURCE MATERIAL section below. You have no other access to my past conversations or documents, so treat that section as the single source of truth.

Your task

Create a complete, well-organized Markdown documentation set for this business in docs/private-ai/ (create the folder if it doesn't exist). The documentation must cover:

the business idea
the business model
the implementation strategy
products and services
potential clients
all other relevant data in the source material

It should serve three uses: my own working reference, the base for investor and lender materials, and context for future Claude sessions.

How to work (follow this order)
Plan first and wait for my approval. Before writing any files, show me:
the file list, with a one-line purpose for each file
the section outline for each file
any contradictions or gaps you found in the source material
Do not write files until I approve.
Write the files one at a time, in the approved order.
Review, then fix, and repeat until clean. After all files are written:
check every number, date, price and name against the SOURCE MATERIAL;
check that no file contradicts another;
check that every relative link resolves;
fix anything you find, then re-check until nothing is left.
End with a short report of what you checked and what you fixed.
Rules
Do not invent facts. If something isn't in the source material, don't add it. If a section needs it, write TODO: and say what's missing.
Keep the labels. Mark estimates as [Estimate] and anything flagged for checking as [To verify]. Keep figures exactly as given, with their ranges. Note that facts are as of 2026-10-19.
Keep my voice and decisions. Where the source says I decided something, state it as a decision. Where it was a recommendation from research, label it as a recommendation.
No confidential client data. Never put client tax return information or any client's confidential details in these files. TWK appears only as a named reference client with the facts given here.
Don't browse the web unless I ask. Put anything needing outside confirmation in the open-questions file.
Writing style. Plain English, short sentences, tables for comparisons and prices, no marketing fluff. Each file opens with a 2–3 sentence summary of its main point.
Suggested file structure (adjust in your plan if you see a better one)
docs/private-ai/
  README.md                      Index + one-page overview of the business
  CONTEXT.md                     Short (~1 page) briefing for future Claude sessions
  01-business-overview.md        Idea, why now, why this founder, positioning
  02-business-model.md           Revenue model, pricing, unit economics, margins
  03-products-and-services.md    Every offer, bundle, tier and add-on, with prices
  04-market-and-clients.md       Segments, sizing, named targets, buyer roles, TWK
  05-go-to-market.md             Sales tracks, channel partners, process, events, objections
  06-technical-architecture.md   Appliance stack, design rules, integrations, RAG platform
  07-compliance-and-legal.md     §7216, Safeguards, ABA 512, PSM, contracts, insurance
  08-implementation-roadmap.md   Phases, gates, 90-day plans, hiring, runbooks, metrics
  09-financials-and-funding.md   3-year model, capital need, raise structure, use of funds
  10-risks-and-kill-criteria.md  Risk register and pivot rules
  11-related-workstreams.md      Workstreams under or next to Private AI
  12-open-questions.md           Decisions pending, items to verify, contradictions found
  13-sources.md                  Source documents and outside sources named below
  glossary.md                    Terms (TRI, §7216, WISP, PSM, MOC, BOP, TWIC, RAG, MRR...)
SOURCE MATERIAL (as of 2026-10-19)
A. Founder
Name: Marcus Klein. Based in Lake Charles, Louisiana (relocated from Austin, Texas). Married.
Military: U.S. Air Force veteran, F-15/tactical aircraft mechanic; 4-year enlistment, honorable discharge.
Engineering: about 10 years as a senior/staff software engineer (Meta, MNTN, DISQO, American Tower, CGI, Kustomer). Last tech job ended June 30, 2026. Describes himself as FedRAMP-trained.
Education: computer science background from McNeese State University (local alumni network).
Self-description: highly adaptable, fast learner, extremely persistent, strong seller.
Venture status: on Oct 18, 2026 he decided to make Private AI his primary focus. He plans to stay solo in Year 1, to raise outside capital, and to earn a "decent salary" within 3 years. He will not build or train his own models; he will use existing open-weight models.
Key relationship: his brother Chris owns Terranova Williams Klein CPAs, LLC (TWK) in Lake Charles: about 534 clients and 15–25 staff. TWK is the planned first (reference) client, and Chris is an active referral partner. TWK also does Marcus's accounting.
B. The business in one page
What it is: a managed private-AI service for professional firms and industrial businesses in Southwest Louisiana (SWLA), expanding along I-10 to Lafayette and Baton Rouge.
What clients get: an AI assistant that runs on a server in their own building. It answers from their own documents with citations, plugs into Microsoft 365, and never sends data to an outside AI provider.
Who pays:
CPA firms first
then law firms
then the plants and industrial contractors of the Lake Charles–Westlake–Sulphur corridor
Why they buy: compliance first, then productivity.
Tax preparers face criminal exposure under IRC §7216 for disclosing client data to third parties. IRS OPR Alert 2026-19 (June 24, 2026) says client data belongs only in secure, enterprise-approved AI systems.
Lawyers need informed consent before putting client information into third-party AI (ABA Formal Opinion 512).
Plants won't let process data leave the fence.
An appliance the client owns answers all three.
Why this company wins:
local, in-person installation and support, including after hurricanes;
a compliance package no national vendor ships;
Microsoft 365 permission-aware retrieval;
named vertical workflows;
founder credibility: former Meta engineer, Air Force aircraft mechanic, McNeese alumnus;
a reference client in the first vertical.
National appliance vendors sell boxes, SaaS vendors move data off-site, and neither shows up in Sulphur.
The sales pitch:

"Your staff are already pasting client data into ChatGPT. This gives them something better that lives in your building, cites the page every answer came from, and comes with the policy and documentation your regulator expects."

Positioning statement:

"The only Southwest Louisiana provider that installs a private AI system in your building, documents it for your regulator, and answers the phone from Lake Charles."

Industrial positioning line, from the corridor strategy:

"I spent four years keeping fighter jets flying and ten years building software at Meta. I turn what your best people know into systems the next shift can use, and the data never leaves your plant."

[To verify] The line implies all ten engineering years were at Meta. The founder's ~10 years span several companies, so reword it before use.
Pitch guardrail: whether an on-prem system removes the §7216 consent requirement is a legal interpretation, not settled guidance.
Marketing says "dramatically simplifies consent," never "no consent needed," until a tax-practice attorney signs off.
The founder's own admin access must be structured as IT maintenance under a confidentiality agreement.
C. Market and potential clients
Segment sizing
Segment	Statewide	SWLA estimate	Target profile
CPA firms	1,724–1,797 permitted firms; 7,160–7,250 active CPAs (State Board of CPAs, Oct 2024 minutes)	70–100 firms; 10–20 with 10–50 staff	10–50 staff, tax-heavy, Microsoft 365
Law firms	19,047 resident active attorneys (2025, ABA)	~1,000 attorneys across the five SWLBA parishes; 10–20 firms of target size	Litigation/transactional, 5–40 lawyers
Plants and LNG terminals	25 LAIA member facilities in SWLA; $64.4B under construction	10–15 operating sites; 3 terminals under construction	Reliability, PSM, training and turnaround managers
Industrial contractors and fabricators	Dozens serve the corridor; Turner alone has 20,000+ employees	20–40 owner-operated specialty firms of 10–150 staff	Scaffolding, insulation, E&I, NDT, coatings, fabrication

Other market facts:

Lake Charles capacity: Lake Charles alone supports roughly 15–25 good-fit clients at maturity [Estimate]. The I-10 corridor (Lafayette, Baton Rouge) is therefore the Year 2 market, not a stretch goal.
Calcasieu Parish: 4,705 employer establishments and 75,412 employees (2023), with employment up 6.4% year over year (Census QuickFacts).
CPA consolidation: CPA firm counts are shrinking (1,980 in 2019 to about 1,724–1,797 now), which means consolidation into the larger firms this business targets.
IT spend anchor: a 20-person professional firm already spends about $2,200–3,700/month on managed IT, at $110–170 per user. That anchors what an AI subscription can cost.
Demand evidence
Thomson Reuters Future of Professionals 2026 (1,816 professionals, March–April 2026):
74% use AI several times a week;
34% use tools their organization hasn't sanctioned (35–37% in tax and audit);
41% lack professional-grade AI;
66% at firms with an AI strategy say AI meets expectations, versus 22% at firms without one.
Tax and audit professionals: 81% use AI weekly, and 48% think their firm would lose clients within two years without clear AI-enabled value.
Clio 2026 (solo and small law firms): 71% of solos and 75% of small firms use AI. But 55–57% have no AI policy, 43–48% rely on generic ChatGPT/Copilot, and fewer than 33% report revenue gains.
Dissenting view: The Legal Stack estimates regular, workflow-integrated use at firms under 20 lawyers at only 28–35% (Q3 2026).
What this means: the pain is unsanctioned "shadow AI" plus no AI policy, not lack of interest. The sale is "replace the ChatGPT your staff already use with a governed system and a written policy." Firms judge it on time saved, so hours recovered must be measured and reported.
Named industrial targets (SWLA Industrial Corridor Sales Strategy)

Operating plants (OSHA PSM and EPA RMP covered):

Sasol Lake Charles Chemical Complex
Westlake (Lake Charles North/South, Petrochemicals)
Citgo Lake Charles Refinery: a $310M Depentanizer project through 2029 adds contract work, and an acquisition by Amber Energy may shake loose budgets
Phillips 66 Lake Charles
Lotte Chemical, Indorama, LyondellBasell
Entergy Nelson and the industrial gas suppliers

LNG terminals (PHMSA Part 193, USCG, TWIC):

Operating: Cheniere Sabine Pass (30+ mtpa; 20 mtpa expansion pre-FID); Venture Global Calcasieu Pass (10 mtpa)
Under construction:
CP2: first LNG 2027, ~400 permanent jobs
Woodside Louisiana LNG: first production 2029, 500–1,000 permanent jobs, 8,000 construction jobs
Commonwealth LNG: FID May 2026, startup 2030
Cameron LNG's expansion targets 2027.
Each new terminal must write operating procedures, train operators and qualify contractors from scratch.

Contractors:

Turner Industries (Sulphur), Performance Contractors, Brock, Cajun, Zachry
the LNG EPCs: Bechtel, Technip Energies, Kiewit
dozens of local specialty firms, which are owner-operated and buy on a handshake

Regional context:

$64.4B of projects are under construction, including CP2 ($20.7B), Woodside Louisiana LNG ($17.5B) and Commonwealth LNG ($13B) (American Press, Oct 9, 2026).
Lake Charles is forecast to lead the state in job growth: 5.6%, or 6,000 jobs, over two years.
Gulf Coast surveys put 34–40% of the petrochemical workforce over 50 or within a decade of retirement.

Priority for the first 90 days:

Local specialty contractors
Citgo and Sasol, through personal contacts
LNG operations-readiness teams, once he holds a TWIC card and a site orientation

The founder has friends who work in the plants, and friends and family who know people higher up.

Buyer roles

At a plant, buy as "services" on a purchase order. Department managers can often approve up to ~$30K and general managers up to ~$50K [Estimate; confirm per plant].

Role	Pain	First offer
Reliability engineer / reliability manager	Repeat failures, no time to mine work-order history	Bad-actor study
Maintenance manager / superintendent	Losing experienced mechanics, slow troubleshooting	Knowledge capture for one unit
PSM coordinator / process safety lead	Audits due, procedures out of date, MOC backlog	PSM documentation support
Turnaround manager	Tracking thousands of contractors and permits	Turnaround dashboards
Training coordinator / operations readiness manager	New hires replacing retirees; new terminals hiring from zero	Training modules
HSE manager	Contractor paperwork and compliance gaps	Contractor onboarding tracker

At a contractor, the owner, general manager or operations manager decides alone.

Avoid early: corporate IT, procurement, and anything touching control systems or the OT network. Plant managers are sponsors, not buyers.

Professional-firm targets: the 10–20 SWLA CPA firms of 10–50 staff first, then Lafayette and Baton Rouge in Year 2. Law firms of 5–40 lawyers. TWK's ~534 business clients are the best referral list in the region.

D. Products, services and pricing

Price it as a compliance-driven managed service with a monthly minimum. It sits between commodity Copilot ($21 per user) and premium legal AI ($225–650 per user per month); effective pricing is $125–175 per user per month.

Core professional-firm offers
Offer	What's included	Price	Notes
Assessment	Half-day review of documents, systems and compliance gaps; written plan	$2,500, credited to setup	Low-risk first yes
Setup and implementation	Appliance install, Microsoft 365 sync with permissions, document loading, 2–3 workflows, compliance kit, staff training	$15,000–40,000 one-time	Scales with document volume and integrations
Starter subscription (up to 15 users)	Monitoring, model updates, backups, support, usage reports	$2,500/month	12-month term, 5% annual escalator
Professional subscription (16–40 users)	Same, plus quarterly workflow reviews	$4,500–6,500/month	
Workflow add-ons	Tax research memos, document intake, contract review, discovery summaries, SOP Q&A, bid drafting	$500–2,000/month each	Built once per vertical, resold to every client
Compliance kit (standalone)	AI use policy, WISP addendum, §7216 or Rule 1.6 vendor file, access logs	$3,000–7,000	Also sold to firms that keep Copilot
Training	Half-day staff sessions	$1,500–3,000	Drives adoption, which drives renewal
Hardware	Client-purchased appliance: one 96GB GPU server, UPS, install	$25,000–35,000 pass-through, plus 8%	Small-office tier (DGX Spark class) at about $5,000
Industrial projects	Knowledge capture, bad-actor studies, PSM documentation, turnaround tooling, contractor compliance	$15,000–75,000 per project; $400–5,000/month retainers	See industrial services below
Packaging rules
Every engagement goes assessment, then setup, then subscription. Add-ons come after the first quarter.
Hardware is quoted as a separate line the client pays for directly, or passed through at cost plus 8%. The company never carries inventory.
Contracts are 12 months, auto-renewing, with a 5% escalator (the MSP norm is 5–8%).
Industrial pricing stays under the buyer's approval limit (typically $25–50K) by phasing larger work.
Offer a 10–15% discount for case-study and reference rights on the first three clients per vertical.
Industrial services (fixed-fee projects first, then convert to subscriptions)
#	Service	What the buyer gets	Price	Margin	Delivery	Likelihood of first sale
1	Contractor compliance package	ISNetworld/Avetta/Veriforce questionnaires drafted and maintained; written safety programs; certificate and orientation tracking with expiry alerts; certificate-of-insurance gap checks	$2,500–6,000 setup, then $400–900/month	75–85%	2–3 weeks	Highest
2	Bid and RFP automation	Private assistant trained on past bids, safety stats and capabilities that drafts responses and prequalification packages	$8–15K setup, $750–1,500/month	70–80%	4–6 weeks	High for contractors chasing LNG work
3	Tribal-knowledge capture	Interviews and walkdowns with retiring operators/mechanics, turned into troubleshooting guides, procedure updates and an on-site assistant	$25–75K per unit or group of 3–5 experts; $1,500–3,000/month to maintain	55–70%	8–16 weeks	Medium; strongest differentiation and highest lifetime value
4	PSM documentation support	Procedure drafting/reformatting, MOC packages, PSSR checklists, 3-year audit prep on a private assistant trained on the site's PSI	$15–40K per project; $2,500–5,000/month retainer	60–70%	6–12 weeks	Medium
5	Reliability bad-actor study	Analysis of 3–5 years of SAP/Maximo work orders: top 20 bad actors, repeat failures, cost by unit, recommended actions	$15–30K fixed	75–85%	4–6 weeks	Medium-high
6	Turnaround support tooling	Daily progress, permit and headcount dashboards; contractor onboarding tracker	$20–50K per event	65–75%	2–4 weeks build, then on site during the event	Medium; sell 3–6 months ahead
7	Training content	Procedure walk-throughs, troubleshooting scenarios, new-hire modules	$10–30K per module set	70–80%	4–8 weeks	Medium-high at new LNG terminals

The compliance-consultant benchmark is $150–300/hour, or about $5,000/year for ISNetworld upkeep [Estimate; vendor listing].

Bundles:

"Contractor-ready" (1 + 2), for firms chasing LNG construction work
"Turnaround-ready" (6 + 7), sold to the plant and its lead contractor together
"Retirement-ready" (3 + 4), for units with known retirements in the next 12–24 months

Small first jobs that open doors:

a free 2-hour contractor "paperwork audit"
a $5,000 pilot bad-actor study on one unit, delivered in two weeks
one retiring-mechanic interview turned into a 10-page troubleshooting guide, as a paid $3–5K sample

Most likely first sales: service 1 (by a local contractor) and service 5 (by a plant reliability engineer).

Industrial track target: $150K–$250K of industrial revenue from 6–10 engagements in 12 months; first paid industrial engagement within 90 days; first plant PO within 6 months; one case study by month 9.

Workflow library candidates (from "RAG Applications for a Mid-Sized CPA Firm")

The research catalogued 20 candidate RAG applications for a 15–25-person CPA firm, in staged order. No comparison showed a custom build beating a bought product, so buy tax-authority research and source-document extraction rather than build them.

Stage 0 (prerequisites):
audit content and measure use of the existing bot;
adopt an AI policy;
decide the §7216 basis, defaulting to consent, with a counsel-drafted form and a consent register;
inventory what the tax, document and practice-management systems can export;
name a second maintainer.
Stage 1 (firm knowledge, no client identifiers):
HR and IT answers (4)
feedback loop and gap analytics (1)
template-grounded drafting with placeholders (5)
SOP capture (2)
onboarding mode (3), only if cheap
Stage 2 (client documents, after consent):
notice response (10)
advisory narratives from a completed return (13)
review checklist assistant (12)
pilots: firm memo library (14) and bookkeeping playbooks (18)
Stage 3 (connector-dependent):
pre-meeting brief with one-client prior-work search (7, 9)
missing-items check (11)
law-change monitor (16)
meeting debrief (6) and email drafting (8): buy first
Later or deferred: firm-metrics Q&A (17), approval-gated actions (20), client-facing assistant (19).
Citation checker (15): can run alongside Stage 1 if sent only citations.
Calendar assumption: consent forms are ready for the December–January engagement mailing; no new tooling February to mid-April.

The first three CPA workflows in the implementation plan are:

document intake and classification by form type and tax year;
tax research memo drafting with citations;
client-notice response drafting.
Deployment stages (the "local data center" idea is the last stage of the same business)
Stage 1 (now): appliances in clients' buildings, plus the industrial services.
Stage 2 (Years 2–3): a shared rack in existing colocation (DartPoints in Baton Rouge or Shreveport, or Houston) for clients who want private AI without owning a server: contractors, small firms, and hurricane failover. About $50–100K of hardware, fundable from revenue.
Stage 3 (only if Stage 2 fills): an own facility near Lake Charles, ideally with a partner that already owns power and space, such as the proposed Azimuth project in Moss Bluff. This stage goes in a separate legal entity.

Rules for the stages:

One business, one brand ("private AI, local").
Keep plant data and CPA tax data on-prem; offer hosting only to clients whose compliance story allows it.
The current raise funds Stage 1 only.
Training an own base model is rejected. Louisiana data-center incentives don't fit, because they need 50+ jobs and $200M of investment.
E. Business model and unit economics

How it makes money:

Subscriptions carry the business.
Setup fees fund the first year.
Workflows and industrial projects lift margin.

Gross margin:

about 66% in Year 1, 68% in Year 2 and 69% in Year 3;
in line with niche MSPs (65–70%), and above AI-product averages (~52%) because the client owns the inference hardware.

Unit economics for one Professional client, at list prices:

Line	Year 1	Years 2–3 (per year)	Gross margin
Setup fee	$25,000	—	55%
Subscription at $4,500/month	$54,000	$56,700 (5% escalator)	70%
Workflow add-ons (1–2 after first quarter)	$6,000	$12,000	85%
Hardware pass-through margin (8% on $28,000)	$2,240	—	100%
Total revenue	$87,240	$68,700	
Gross profit	$54,000 (62%)	$49,900 (73%)	

Lifetime value and acquisition cost:

Three-year lifetime value is about $190–225K of revenue and $135–160K of gross profit per client (realized versus list).
Customer acquisition cost is about $5,000 (MSP benchmark ~$4,200, with a 7-month payback).

Year-3 revenue mix target: subscriptions 55%, setup and implementation 20%, workflows and compliance kits 10%, industrial projects 15%. Hardware margin is excluded.

Why margins hold:

inference runs on client hardware;
installs come from a repeatable image (client #10 takes a day);
workflows are built once per vertical;
support is scoped (business hours, 4-hour P1 response), so one person carries ~10 clients and a first hire ~20.

What compresses margin, each handled by a rule:

custom integrations priced too low → quote integrations separately;
unbilled on-site hours → on-site time is in the setup fee;
hardware on the company's books → hardware is never inventory.
F. Competition
Type	Examples	Price	Where this company wins
Bundled cloud AI (the real competitor)	Microsoft 365 Copilot Business ($21/user on top of a $14–22 M365 license), Copilot Chat (free), ChatGPT Business ($20/user)	Cheapest	Compliance documentation, data residency, vertical workflows, in-person support
Vertical AI for CPAs	Thomson Reuters CoCounsel Tax, Blue J, Karbon (~$59/user), Canopy	$500–1,200/month for a small firm's stack	Firm's own documents and history; one governed system instead of five tools
Vertical AI for law	Clio Duo ($49/user), CoCounsel, Lexis+ ($225–650/month), GC AI and Harvey ($500+/user)	Mid to premium	Price for 5–40-lawyer firms; closed system; local
Private AI appliances	Iternal Turnkey AI (from $697/user perpetual), LLM.co, ibl.ai, HPE and Lenovo private AI	Enterprise quotes	They ship boxes; this company installs, integrates, documents and shows up after a hurricane
Local MSPs	Perftech, Server At Work, Advanced Office Products, SmartIT, Southern Technologies, Rapid I.T. (Lake Charles area); InfoTECH, Vital Integrators, Duhon, General Informatics (Lafayette/statewide)	$110–185/user managed IT	None markets private AI; they are channel partners, not competitors

Moat over time:

vertical workflow libraries
refined compliance templates
documented case studies
relationships inside plants that out-of-town vendors can't replicate
G. Go-to-market

There are three tracks, each on its own clock:

CPA firms: sold May–December, because tax season blacks out January–April.
Law firms: year-round.
Industrial: timed to turnaround and audit calendars.
Track 1: CPA firms (the reference vertical)
Agree a referral arrangement with TWK that complies with AICPA commission and referral-fee disclosure rules.
Run CPE sessions through the Society of Louisiana CPAs on §7216, OPR Alert 2026-19 and AI governance. The call to action is a free 2-hour assessment.
Track 2: Law firms
Give a CLE talk at the Southwest Louisiana Bar Association on ABA 512, Rule 1.6 and the Louisiana Supreme Court's AI letter.
The Rule 1.6 kit sells standalone and opens the door for the appliance.
Track 3: Industrial

Sell to contractors first, then plants, then LNG readiness teams.

Channel partners

Approach two or three Lake Charles and Lafayette MSPs in the first six months. They keep the IT contract and earn 10–15% of first-year subscription on referrals. The company supplies the appliance, platform and workflows.

Sales process
Paid assessment ($2,500, credited to setup), or a free 2-hour paperwork audit for contractors.
A two-page proposal, never a deck, containing:
the problem in their words, with their numbers;
the deliverable;
scope and schedule in weeks, including their experts' time;
a fixed price (industrial terms: 50% on start, 50% on acceptance) and the optional retainer;
data handling in three sentences;
credentials.
Setup, then subscription, then add-ons.
Targets and budget
Year 1 activity: 20 conversations a month; 4 proposals a month; a 25% close rate; a 5-month average sales cycle.
New clients: 4 in Year 1, 7 in Year 2, 9 in Year 3.
Budget: about $25K a year for memberships (ABC, Chamber SWLA, SLCPA), events (Americas LNG Summit, SLCPA chapters), I-10 travel and collateral.
Industrial door-opening

Credentials, in the first 30 days:

Basic Orientation Plus (BOP) at HASC Louisiana in Sulphur: ~$120, one day, valid a year [To verify price];
a TWIC card (it can take weeks);
site-specific orientations for the first two plants;
OSHA 30;
drug-testing consortium enrollment;
a certificate of insurance.

Contacts playbook:

Ask floor-level friends, "what wastes your time?"
Ask friends and family who know leadership for a 20-minute introduction to one named department manager.
Hand over a one-page sheet: background, three services, and an offer of a free 2-hour assessment.
After every meeting, ask for two more names: one inside the plant and one trusted contractor.

Organizations:

HASC Louisiana
Lake Area Industry Alliance (LAIA)
ABC Pelican Chapter
SWLA Economic Development Alliance and SEED Center (houses LEEA, the LNG trade group)
McNeese LNG Center of Excellence
the annual Americas LNG Summit in Lake Charles
supplier-diversity programs at Sasol, Westlake, Citgo, Phillips 66 and Cheniere (register once SDVOSB/VOSB certified)

Discovery questions:

Who on your crew is within three years of retirement, and what do they know?
When something trips at 2 a.m., where does the new operator look first?
How many procedures are past review, and when is the next PSM audit?
What did the last turnaround overrun cost?
(Contractors) Which plants can't you work at right now, and what's your ISNetworld grade?
What has IT said about AI tools?
What is the largest purchase you can approve without corporate?

Objection answers:

Objection	Answer
"Corporate IT must approve software"	It's a documentation and engineering service on a server you own, on the business network, with no connection to control systems.
"We have a procedures vendor"	Keep them; I capture what isn't written down.
"AI hallucinated"	Every answer cites the page of your own document, or says the answer isn't there.
"Our data is proprietary"	It never leaves your building; you hold the keys.
"You're a one-man shop"	You get a fixed price, a named person on site, full insurance, and deliverables your staff can maintain.
"No budget"	Scope the pilot to land in the next turnaround or audit window.

Industrial 90-day weekly plan:

Week 1: form or confirm the LLC; bind insurance; register for BOP; apply for TWIC; draft the one-pager.
Week 2: take BOP; hold five contact conversations; list the contractors your friends work beside.
Week 3: five more conversations; build the compliance-package checklist and the bad-actor study template.
Week 4: run two free paperwork audits; write the price sheet; join ABC.
Weeks 5–6: quote the first compliance package and first pilot study; take two site orientations.
Weeks 7–8: deliver the first paid job; attend one LAIA or ABC event; finish the vendor security answer pack.
Weeks 9–10: pitch the bad-actor study and a knowledge-capture sample to the two warmest plant contacts.
Weeks 11–12: close the first plant PO; draft the case study; review the pipeline and decide on a first hire.

Weekly metrics: conversations held, named buyers in pipeline, proposals out, dollars quoted, dollars invoiced, days on site.

H. Technical architecture
Operating rules
Clients buy the hardware.
The model is a configuration setting, never an architecture decision.
Nothing touches a plant's OT network, ever. Industrial data arrives only as exports: SAP/Maximo work-order extracts, PI historian reports, PDF procedures.
No hire before the trigger is met.
Every deliverable is marked "draft for qualified review."
Appliance stack

The appliance is built from a single scripted image:

Component	Choice	License note
OS and runtime	Ubuntu LTS, Docker Compose	Open
Model serving	vLLM (OpenAI-compatible API); Ollama for development and the small-office tier	Apache 2.0
Default model	Qwen3.8-27B (FP8 weights ~31 GB)	Apache 2.0
U.S.-origin alternative, pre-staged	Gemma 4 31B or gpt-oss-120b (Apache 2.0); Mistral Small 4 as an EU option	Default for federal, DoD-linked, LNG and critical-infrastructure clients
Embeddings and reranker	Local open-weight models, benchmarked on the evaluation set	Never a cloud embedding API
Document parsing	Docling or Unstructured	MIT / Apache 2.0; OCR quality decides answer quality
Vector and metadata store	Postgres + pgvector (Qdrant if scale demands)	PostgreSQL License
Chat interface	Open WebUI with branding kept, later the company's own front end	Branding can't be removed above 50 users without a license
Workflow automation	n8n on each client's own instance, or an Apache-licensed alternative	Sustainable Use License: never host one n8n for multiple clients; confirm with n8n before productizing
Remote access	WireGuard or Tailscale/Headscale	No inbound ports
Monitoring	Prometheus and Grafana, unmodified	Don't modify and expose Grafana as a service
Backups	restic to U.S. object storage, client-held keys	Nightly; restore tested quarterly
Design decisions
One 96GB GPU (RTX Pro 6000 Blackwell class) serves an office. A 27B model in FP8 leaves 50–60 GB for context, enough for 10–50 users. The small-office tier uses a DGX Spark-class box for under 10 users.
Permission-aware retrieval is non-negotiable. SharePoint and file permissions are stored with every chunk and filtered at query time.
Citations on every answer. When the answer isn't in the documents, the system says so.
Client IT owns the box. The client holds the admin credentials, encryption keys and physical server. The company has application-level access only, through a private tunnel.
Hurricane posture:
nightly encrypted backups;
a shutdown runbook on storm watch;
optional temporary failover to a rented U.S. cloud GPU, only with written client approval, because it changes the data-location claim.
Microsoft 365 integration
Entra ID SSO.
Graph connectors for SharePoint and OneDrive, using Sites.Selected permissions.
Permission-aware retrieval.
A sideloaded Outlook add-in for drafting replies.
Integrations by vertical
CPA:
Microsoft 365
QuickBooks Online API (open)
file-based ingestion from CCH Axcess, UltraTax and Drake exports (their APIs are closed)
Karbon or Canopy where used
Law:
Microsoft 365
Clio API (open)
NetDocuments and iManage, via partner programs or exports
Industrial: exports only.

Build order:

image and runbooks
evaluation harness
Microsoft 365 connector with permissions
the three CPA workflows
Outlook add-in
the company's own front end

Evaluation set: 50 real questions with known answers from TWK's documents. Nothing ships that scores lower than the last version.

Security answer pack (needed before the first plant or large-firm conversation):

network diagram and access model
encryption at rest and in transit
backup and restore design
logging and retention
incident response plan
subcontractor list (none)
insurance certificates
a one-page data-flow statement
The founder's RAG platform (the engine under everything)
Already built. Designed generically for any business, not only CPA firms.
Currently backs a knowledge-base Q&A bot with source citations, plus a Microsoft Teams integration.
He also wants to sell it as plug-and-play knowledge bases to other businesses.
Ingestion design for TWK's SharePoint knowledge base (§7216-aware), meant to hold firm-only data:
path allowlist
detectors and a quarantine workflow
redaction
evaluation harness
audit schema
Open items:
TWK's Microsoft 365 license tier, which decides Microsoft Purview versus self-hosted Presidio for detection;
path allowlist confirmation;
who has quarantine review authority.
Multi-tenant design notes (from the Glass guide):
PostgreSQL with tenant_id;
per-tenant Entra configuration;
SOC 2-style controls before resale;
don't build billing yet.
I. Compliance and legal
CPA / tax
IRC §7216 (criminal) and §6713 (civil):
§7216: up to a $1,000 fine and/or one year in prison per violation;
§6713: $250 per disclosure, up to $10,000 a year.
IRS OPR Alert 2026-19 (June 24, 2026) maps Circular 230 duties onto AI:
§10.22 due diligence applies;
every AI citation and calculation must be verified;
§§6713/7216 data goes only into secure, enterprise-approved systems;
specific signed consent is generally required before sharing §7216 data with an AI tool;
it doesn't require telling clients that AI was used.
No IRS guidance yet classifies AI under the §7216 exceptions (as of July 2026).
Consent requirements: Treas. Reg. §301.7216-3 says consent must be knowing, voluntary, written and obtained beforehand. Individual returns use the Rev. Proc. 2013-14 format. The AICPA publishes sample forms.
Practitioner view: the §7216 disclosure happens when data leaves the preparer's control, regardless of whether the vendor retains it (Tom Gorczynski, Tom Talks Taxes).
On-prem argument: firm-owned hardware with no model vendor arguably means no disclosure to an AI provider. That would avoid naming OpenAI or Microsoft and collecting ~534 consent forms at TWK.
The weak point is the founder's admin access.
Mitigations:
IT-maintenance confidentiality agreement;
platform-only access, not content;
break-glass logging;
client-held keys;
documented in the firm's WISP;
a tax-attorney opinion before any marketing claim.
FTC Safeguards Rule (16 CFR Part 314): preparers need a written information security program (WISP) and must oversee service providers. The WISP addendum is a sellable, recurring artifact.
AICPA Code 1.700.001 on confidentiality also applies.
Law
ABA Formal Opinion 512 (July 2024): informed client consent is needed before client information goes into a self-learning generative AI tool, and boilerplate isn't enough.
Louisiana: the Supreme Court sent a letter on Jan 22, 2024. The LSBA has issued no formal AI opinion (as of September 2026).
Oregon Formal Opinion 2025-205: closed models inherently give greater confidentiality protection, but that alone doesn't settle the question.
Kit: AI use policy, vendor due-diligence file, verification and incident logs, client communication language.
Industrial
OSHA PSM (29 CFR 1910.119) and EPA RMP. An RMP rollback was proposed Feb 24, 2026, with a final rule expected late 2026; PSM is unchanged.
Deliverables are always "draft for qualified review." The MSA states that the client's PSM process owns approval.
Never promise regulatory outcomes.
Contracts (Master Services Agreement, SOW and Data Processing Addendum, drafted with a Louisiana business attorney)
The client owns the hardware and data; the company owns the platform IP and licenses it.
Liability is capped at 12 months of fees, with carve-outs up to insurance limits.
No training on client data.
Deletion within 30 days of termination.
72-hour breach notice.
Model-origin disclosure and a swap clause.
Insurance (before the first client conversation)
general liability ($1M/$2M)
tech E&O ($1M)
cyber ($1M)
workers' compensation (gate policies require it even for a sole owner)
auto

Budget $6–10K in Year 1. Large plant MSAs may require $2–5M limits, so keep umbrella coverage available.

Company security

The company keeps its own WISP and uses:

MFA everywhere
EDR
encrypted devices
no client data on founder devices
client-held encryption keys
an annual review of each client's model and license
Model-origin policy

Chinese-origin models (Qwen, DeepSeek, Kimi) face pending U.S. scrutiny: the FIREWALL Act, NDAA provisions, and House committee proposals.

Default to a U.S.-origin model for federal, DoD-linked, LNG and critical-infrastructure clients.
Review quarterly.
Switch affected clients within 30 days under the swap clause.
Regulatory watch list
IRS guidance on §7216 and AI
the final EPA RMP rule
any LSBA formal AI opinion
federal procurement restrictions on Chinese-origin models
J. Implementation roadmap
Plan on a page
Horizon	What done looks like	Gate to the next phase
90 days	LLC, insurance and bank set up; SBA and equity applications filed; TWK pilot live on a client-owned appliance; install image and runbooks v1; compliance kit v1; first contractor compliance package sold; BOP and TWIC in hand	TWK staff use it weekly with measured time savings; one non-TWK invoice paid
6 months	Funding closed; 3 paying clients beyond TWK; attorney opinion on §7216 and founder access; two MSP partners signed; first plant PO; case study published	MRR of $10K; pipeline of 15 named buyers
12 months	4–5 total clients plus 2–3 industrial projects; first hire running installs; Lafayette outreach started; SDVOSB certified	MRR of $20K; founder out of first-line support
36 months	19–20 clients across Lake Charles, Lafayette and Baton Rouge; two staff; revenue ~$860K; founder salary $130K; one federal or VA contract in progress	Operating profit; decide between growth capital and steady-state ownership
Phase 0: Foundation (weeks 1–6; under $10K combined)
Form the LLC (or finalize an existing one), get an EIN, and register with Calcasieu Parish Sales and Use Tax and the City of Lake Charles.
Open a bank account and credit line; set up bookkeeping with TWK.
Bind insurance.
Apply for SBA VetCert and register in SAM.gov (UEI).
Draft the MSA, SOW and DPA.
Engage a tax attorney for the §7216 opinion.
File the SBA application.
Get BOP and TWIC.
Buy the demo/lab appliance (~$25–35K).
Set up the company WISP, MFA and a password manager.
Phase 1: Product and reference client (weeks 1–12; TWK as a paying client at a discount with a signed SOW)
Weeks	Deliverable
1	Baseline timings on three tasks: finding a prior-year workpaper, drafting a research memo, answering a notice email
1–2	Evaluation set (50 questions)
2–4	Appliance v1
3–6	Microsoft 365 integration
5–9	Three CPA workflows
6–10	Compliance kit v1
8–12	Install image and runbooks v1 (rebuild in under a day)
12	Two-page case study
Compliance workstream timing
Item	Weeks
§7216 opinion	2–8
WISP addendum template	4–10
§7216 consent templates (provided to every CPA client regardless of the opinion)	4–8
ABA 512 / Rule 1.6 kit, with Louisiana ethics counsel review	8–14
MSA, SOW and DPA	1–6
Model-origin policy	6, then quarterly
Company WISP	1–4
Hiring (both triggers must be true)
Hire	Triggers	Target month	Base pay	Loaded cost	Takes over
Support and implementation engineer	8–10 clients AND 3 months of payroll in the bank	9–12	$55–75K	~$70–95K	Installs from the image, support queue, hurricane runbook
Second engineer or sales lead	15–20 clients AND breakeven in sight	22–26	$65–90K	~$80–115K	Lafayette/Baton Rouge delivery, or outbound sales
Contract documentation specialist	More than 2 PSM/knowledge-capture projects a quarter	As needed	$60–90/hour	Project-billed	Expert interviews and procedure drafting
McNeese CS and engineering interns are the recruiting pipeline.
What the founder stops doing, in order: installs (months 9–12), first-line support (month 12), workflow configuration (Year 2), then delivery entirely (Year 3). He keeps sales, product and key accounts.
Year 1 time split: about 40% selling, 40% delivery and build, 20% support and admin.
Bookkeeping, legal and insurance are outsourced.

Runbooks:

install from image
update and model swap
backup, restore and quarterly restore test
hurricane shutdown and recovery
client onboarding and offboarding
incident response
vendor security questionnaire answers

Support standards:

business hours;
P1 (system down): 4-hour response; P2: next business day;
best-effort uptime on client-owned hardware, with a spare-parts plan;
a monthly usage and health report to each client.
Weekly metrics (Year 1 targets)
Metric	Target
Conversations	20 a month
Named buyers in pipeline	15 by month 6
Proposals out / close rate	4 a month / 25%
MRR	$10K by month 6; $20K by month 12
Gross margin by line	Subscription 70%, setup 55%, industrial 60%+
Support hours per client	Under 6 a month
Client concentration	No client above 20% of revenue after Year 1
Evaluation score	Never lower than the previous release
K. Financials and funding (base case, from the 3-year financial model with Low/Base/High scenarios)
	Year 1	Year 2	Year 3
New clients (ending count)	4 (4)	7 (11)	9 (19–20)
Revenue	~$155K	~$465K	~$860K
Gross margin	~66%	~68%	~69%
Founder salary	$70K	$100K	$130K
Staff	0 (first hire months 9–12)	1	2
Operating result	~−$95K	~+$15K	~+$155K

Capital required:

Base case: about $375K, covering a cash trough of ~$155K (after the demo appliance and debt service) plus a six-month operating buffer.
Low scenario: ~$510K, and it never breaks even within three years.
High scenario: ~$420K, because it hires earlier.
The plan raises $400K.

What moves the numbers most, in order:

new clients per year
average subscription price
founder salary timing
first-hire timing

Hardware prices barely matter, because clients buy the hardware.

Founder salary context:

A remote staff engineer's market rate is likely $180–250K [Estimate]. This plan trades 2–3 years of lower pay for ownership.
$180–250K total compensation becomes plausible at 35–45 clients across the I-10 corridor, mostly through distributions.

Faster routes outside the plan:

one federal or VA SDVOSB award ($250–500K) would change the picture within a year;
keeping contract engineering work at one day a week adds $60–80K.
Raise structure

Layer 1: debt ($150–250K). Apply first; it takes 60–90 days.

An SBA 7(a) or Express loan through a Louisiana lender, using Veterans Advantage fee relief [To verify current terms].
LED's Small Business Loan Guaranty Program backs loans of $5K–$1.5M; its rule was updated May 20, 2026.
Collateral is thin. Lenders will look at income history, the TWK contract, and 2–3 letters of intent.

Layer 2: equity ($150–250K) from friends, family or local angels.

A SAFE with a $1.5–2.5M cap or a convertible note, keeping the founder above 75%.
Or a revenue-share note that repays 1.5–2x.
Louisiana's 25% Angel Investor Tax Credit sunset on June 30, 2026, so pitch on cash returns.

Layer 3: non-dilutive upside, not plan capital.

Veteran grants, usually under $25K each: Warrior Rising, Hivers & Strivers, PenFed Foundation, Second Service Foundation, Bunker Labs.
LED's Digital Interactive Media and Software Development credit (25% of in-state payroll) [To verify eligibility].
SDVOSB via SBA VetCert: free, ~12 days of processing, valid 3 years.
Use of funds ($400K)
Use	Amount
Founder salary shortfall, Years 1–2	$170,000
Demo and lab appliance, tools, software	$35,000
First hire, months 9–12	$25,000
Insurance, legal, formation, SDVOSB	$20,000
Marketing, events, memberships, travel	$30,000
Six-month operating buffer	$120,000
Funding timeline
When	Step
Weeks 1–2	Founder capital in; TWK contract signed; SBA lender meetings
Weeks 2–4	SBA application filed
Weeks 4–8	Equity conversations; SAFE drafted; LOIs gathered
Months 3–6	Debt and equity close; six months of runway before any hire
Month 12	Review at MRR $20K
Months 23–24	Operating breakeven
Month 36	Decide between growth capital and steady-state ownership

If the raise comes in under $250K:

defer the demo appliance and use TWK's system for demos;
push the first hire to month 15;
lean on industrial and contractor work.
L. Risks and kill criteria
Risk	Trigger	Response
Clients won't pay a compliance premium over Copilot	Two quarters of deals lost on price	Lead with the standalone compliance kit; partner with MSPs; raise the industrial share
§7216 opinion is unfavorable	Attorney says consent is still required	Ship consent templates with every install; reposition on security, residency and productivity
GPU prices keep rising (RTX Pro 6000 went from ~$7,600 to $16,000 in 18 months; DGX Spark $3,999 → $4,699 by Aug 2026)	Standard appliance cost above $40K	Promote the small-office tier; cloud burst design; refresh clauses
Chinese-model restrictions widen	Any rule or client policy barring Qwen	Switch to the U.S.-origin model within 30 days
Hurricane	Named-storm watch for Calcasieu or Cameron	Shutdown runbook; schedule on-site work outside June–November
Sales cycle longer than 5 months	Average pipeline age above 6 months	Free contractor audits; paid assessments; sell to decision-makers only
Founder consumed by delivery	Fewer than 15 conversations a month for two months	Freeze custom work; pull the hire forward; raise prices
Client security incident	Any confirmed breach	Pause sales; third-party review; 72-hour notice; engage the insurer
Funding shortfall	Less than $250K closed by month 6	Defer the appliance and the hire; prioritize industrial cash work; revenue-share note
Local market saturates	Fewer than 5 qualified CPA/law prospects left in SWLA	Start Lafayette outreach immediately
Bundled cloud AI is "good enough"	—	Sell compliance and workflows, not chat; integrate with Microsoft 365 rather than fight it
Kill and pivot criteria
Fewer than 3 paying clients (beyond TWK) by month 12: pivot to fractional CTO and project work, and stop the appliance offer.
MRR under $15K by month 18: no second hire; consider selling the client base to a partner MSP.
Gross margin under 50% for two quarters: fix pricing or drop the lowest-margin line.
Any security incident caused by the company: pause sales, get a third-party review, then decide.
Founder stop-loss: if by month 18 the business can't pay a $100K salary on a credible 12-month forecast, take contract engineering work and run the business part-time for existing clients.
M. Related workstreams (under or next to Private AI)
TWK reference client.
Started August 1, 2026 as technology and operations consultant. He was doing no TWK work as of Oct 8, 2026. On Oct 16 he committed to help Chris reduce the firm's dependence on him.
Earlier TWK work:
workflow and process audit
a Karbon + "Hermes" AI automation architecture plan
a verified Excel ROI model (TWK_ROI_Model.xlsx)
analysis of Chris's 2025 time-and-expense journal (20K+ hours, ~31% non-billable)
a "Building Power BI Dashboards from Karbon Data" guide
TWK doesn't track most baseline metrics (hours per task, rework, turnaround, realization), so establishing tracking is part of the work.
TWK already has Microsoft 365 Copilot.
"Glass for TWK" design (Oct 16, 2026): Claude (Team first, Enterprise before any client data) plus one TWK-owned remote MCP server ("twk-context").
The server wraps the firm knowledge base (from the RAG platform), the Karbon API v3, and Karbon's Practice Intelligence Snowflake reader, with audit logging.
Copilot is kept for in-app Office and Teams work.
About 12 reviewed firm skills.
Cost: ~$800–2,900/month for 20 users.
Client data is gated behind the WISP, a written §7216 position from counsel, consents, signed vendor terms and tested controls.
Success targets: 80% weekly adoption within 60 days; 15–25% fewer hours on 3 workflows.
Long-term vision: TWK as a sandbox, then resell to other CPA firms and serve Chris's small-business clients.
RAG platform as a product. Plug-and-play knowledge bases for businesses beyond CPA firms; the engine under the appliance.
Fractional CTO practice and paid assessments.
Go-to-market materials, a 90-day launch plan, and a templatized paid assessment scope.
McNeese as a vendor-route client: LaVet certification, CIO-first outreach, a sub-$15K SOW on Ellucian Banner and institutional-research workflows.
It is also the plan's pivot path under the kill criteria.
Industrial corridor services. Covered above; part of the same business, per the Oct 18 decision.
Shared hosting / local data center. The last stage of the same business (section D).
SDVOSB and federal/VA track (secondary).
SAM.gov and/or VetCert applications submitted and pending (Oct 2026).
NAICS 541511, 541512, 541519, 541611, 541990, 518210.
Vehicles researched: VETS 2, Polaris, OASIS+, GSA Schedule, T4NG2.
Plan to start as a subcontractor; VA first, then civilian agencies.
On-prem, U.S.-origin-model AI suits this track. The 36-month plan includes one federal or VA contract.
VA Effective-Date & CUE Engine. A software idea for VA-accredited reps. Parked per a validation memo on Oct 19, 2026:
expected Year-3 ARR ~$238K if built;
a new rival (VBMS Reviewer, $60–79 per file);
recommendation to keep Private AI as the primary focus.
Could later be licensed, or used in an accredited claims-agent practice. Not part of Private AI.
Company formation and brand.
Earlier top name pick: Klein Technology Group LLC, marketed as veteran-owned, with a contractor one-pager and a consulting launch plan.
He now wants a better name, drawn to a "rebirth" theme.
He also owns an existing Louisiana LLC, REGROUP, LLC (formerly Phoenix Recovery Solutions LLC), through which he verified a Google Cloud account.
Decision pending: use REGROUP, LLC or form a new LLC for this business. For SDVOSB, the veteran must own at least 51% and control the company.
Louisiana formation runs through geauxBIZ (~$105; name reservation $25 for 120 days).
N. Open questions, items to verify, and contradictions to flag

Pending decisions:

Legal entity and name (section M.8).
TWK deployment model: on-prem appliance (this business plan) versus Claude-based "Glass" (cloud) versus a hybrid with firm-only knowledge in the cloud and client data on-prem. The two TWK documents assume different architectures. Flag this as the top contradiction to resolve.
TWK's engagement status and signed SOW: no TWK work as of Oct 8, but TWK is the planned first paying client.
TWK's Microsoft 365 license tier.
The §7216 opinion on on-prem AI and founder access.

To verify:

Census County Business Patterns counts (NAICS 5411, 5412, 5413, 238) for Calcasieu Parish and the Lake Charles MSA.
Current SBA Veterans Advantage terms.
LED software incentive eligibility.
2–3 live server quotes (Dell, Supermicro, Lambda, Exxact).
Lake Charles salaries for a support engineer.
BOP price.
Plant approval limits and budget-owner titles.
Contractor headcounts.
Supplier-diversity registration steps.
LNG readiness staffing timelines.
Microsoft Graph scopes and Outlook add-in sideloading.
n8n resale terms.
Embedding and reranker benchmarks on the evaluation set.

Wording fix: the industrial positioning line implies ten years at Meta.

Two sets of financial figures exist:

an early research brief: ~$160K/$455K/$800K revenue and a $350–500K raise;
the corrected financial model: ~$155K/$465K/$860K and $375K needed against a $400K raise.

Use the financial-model figures.

Unit-economics mismatch: the Year-1 gross profit in section E ($54,000, 62%) doesn't match its own line-item margins, which work out to about $58,900. Keep the stated figure, flag the mismatch, and confirm it against the spreadsheet. Years 2–3 ($49,900) do reconcile.

O. Source documents (claude.ai artifacts; for provenance only, you can't open them)
Private AI Services Business Model: https://claude.ai/artifact/VzceDMaC14ZC61yVHpDThH
Private AI Services Implementation Plan: https://claude.ai/artifact/Be4q39wF3JvrnZX8yMvMqw
SWLA Industrial Corridor Sales Strategy: https://claude.ai/artifact/8BjZPBQ7JovmgoqqQKH3ut
3-year financial model spreadsheet (Low/Base/High scenarios): companion to the business model; location TODO
RAG Applications for a Mid-Sized CPA Firm: https://claude.ai/artifact/JFVCZAFpsepRxj3usYSk7Y
Glass for TWK: Implementation Guide: https://claude.ai/artifact/QEH11hhmcMQeFW2cqSxyNU
Foot-in-the-Door Plan: Lake Charles Industrial Tech: https://claude.ai/artifact/7MsXuCjF8UZC9F1FD9xErx
Klein Technology Group: Consulting Launch Plan: https://claude.ai/artifact/En7EYjmBJJtTfEtebGaNnk
Klein Technology Group: Contractor One-Pager: https://claude.ai/artifact/J9KhfusH4jazLLjvpL3YMa
SDVOSB Contracting Plan: https://claude.ai/artifact/3KrPfkfe2SwfNv2MCvJrRk
VA Effective-Date & CUE Engine: Validation Memo: https://claude.ai/artifact/AZmDKTU94FnEJPoBf2LWwT

Outside sources named in those documents (opened Oct 18, 2026):

Thomson Reuters Future of Professionals 2026
Clio 2026 solo and small firm report
Thomson Reuters on IRS OPR Alert 2026-19
Tom Talks Taxes on AI and §7216
ABA on generative AI and confidentiality
State Board of CPAs of Louisiana minutes
ABA lawyer population survey
Census QuickFacts (Calcasieu)
MSP pricing and margin benchmarks
Copilot pricing guide
legal AI pricing roundup
TechSpot on the RTX Pro 6000 price increase
Qwen3.8 licensing
House committees on Chinese models
SBA veteran programs and SDVOSB guide
IT-consultant insurance benchmarks
Open WebUI license notes
n8n license discussion
Westlake contractor gate requirements
HASC Louisiana
American Press (projects and jobs)
Citgo project and KPLC on Amber Energy
Sabine Pass 10-Q
ENR on CP2
Woodside and Commonwealth LNG announcements
Turner Industries
LAIA
AIChE 2026 on tribal knowledge
Gulf Coast workforce data
EPA proposed RMP rollback
PrequalPilot (ISNetworld consultant pricing)

Start with step 1: show me your plan and wait for my approval.