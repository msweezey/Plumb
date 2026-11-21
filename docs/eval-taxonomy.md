# Plumb eval taxonomy

How every Plumb eval is organized, from the Index down to a single step in a single run. Machine-readable version: [`data/eval-taxonomy.json`](../data/eval-taxonomy.json).

Source: Sweezey, 21 Nov 2026. This replaces the four focus areas in the original brief (Strategy, Email, Creative & content, Ads & media). Example tasks and the ID format are *Proposals*.

## 1. The hierarchy

The **task** is the unit. It is a workflow that crosses several tools. Three axes describe **what** is tested; three describe **how** it was run.

```
WHAT                                   HOW
Function                               Vertical   (5)
 └─ Sub-function                       Level      (3: HIL / HOL / HOOL)
     └─ Task (workflow)                Model      (several AI models)
         └─ Step → tool used
```

One **eval** is one task. One **eval cell** is that task in one vertical, at one level, with one model. Each cell runs several times, and each **run** is broken into **steps**. Each step records the tool it used, so tools are measured inside the workflows they serve.

```
Index
└─ Function                    Advertising & Promotion
   └─ Sub-function             Programmatic & Paid Media Buying
      └─ Task (eval)           PLB-ADV.BUY-003  Pull last month's results and pause losers
         ├─ HIL / HOL / HOOL   time · cost · impact, and the best way
         └─ Cell               Retail & E-Commerce × HOL × Model 2
            └─ Run             r1, r2, r3
               └─ Step         1. Pull results (ad platforms)  2. Join revenue (analytics)  3. Rank  4. Pause
```

Scores roll up the same path: steps → run → cell → level → task. The Index lists tasks; each task shows impact, time and cost at each level. Results can be filtered by function, sub-function, vertical and model, and cut by tool across tasks for vendor reports.

## 2. Functions and sub-functions

Functions are the Index's top-level tabs. Each function has a practitioner board.

### Advertising & Promotion (Media strategy) · `ADV`

| ID | Sub-function | Example task (*Proposal*) |
|---|---|---|
| `ADV.PLAN` | Media Planning & Audience Targeting | Build a quarter's media plan and audiences from a brief and budget |
| `ADV.BUY` | Programmatic & Paid Media Buying (search, social, display, retail media) | Pull last month's results and pause losers |
| `ADV.OPT` | Campaign Execution & Bid Optimization | Launch a campaign from a spec and adjust bids to a target CPA |
| `ADV.DCO` | Creative Ad Production & Dynamic Creative Optimization (DCO) | Produce ad variants for 3 audiences and set up a DCO test |

### Content & Experience · `CNX`

| ID | Sub-function | Example task (*Proposal*) |
|---|---|---|
| `CNX.CSTRAT` | Creative Strategy | Turn a product launch brief into a creative platform and messaging matrix |
| `CNX.CREATE` | Content Creation | Write and design a launch blog post with on-brand assets |
| `CNX.SCALE` | Scaled Content Creation | Produce 200 product descriptions to brand guidelines |
| `CNX.CMS` | Web Content Management (CMS) & Landing Page Optimization | Build a landing page in the CMS and set up an A/B test |
| `CNX.EMAIL` | Email Marketing & Marketing Automation | Build a 3-email nurture · Clone and localize a live campaign |
| `CNX.PERS` | Website Personalization & SEO | Set up a returning-visitor personalization rule and fix on-page SEO issues |

### Social & Relationships · `SOC`

| ID | Sub-function | Example task (*Proposal*) |
|---|---|---|
| `SOC.PUB` | Social Media Publishing & Listening | Schedule a week of posts across channels and summarize brand mentions |
| `SOC.INF` | Influencer & Creator Marketing | Shortlist creators for a brief, draft outreach and track deliverables |

### Commerce & Sales · `COM`

| ID | Sub-function | Example task (*Proposal*) |
|---|---|---|
| `COM.LEAD` | Lead Capture, Scoring & Routing | Route a lead form · Clean 500 contacts |
| `COM.ABM` | Account-Based Marketing (ABM) | Build a target account list and launch a tiered ABM program |
| `COM.CRO` | E-Commerce Merchandising & Conversion Rate Optimization (CRO) | Re-merchandise a category page and launch a checkout test |
| `COM.LOY` | Loyalty & Referral Programs | Set up a referral offer and a points-expiry reminder flow |

**4 functions · 16 sub-functions.**

## 3. Verticals

| ID | Vertical |
|---|---|
| `RET` | Retail & E-Commerce |
| `HLS` | Healthcare & Life Sciences |
| `FSI` | Financial Services & Insurance |
| `HOS` | Hospitality & Travel |
| `B2B` | B2B & Industrial/Manufacturing |

Verticals change the sandbox data, the rules a task must respect (consent, claims, regulated language) and what the board grades as a good outcome. Not every sub-function runs in every vertical. For example, `COM.ABM` is mostly `B2B` and `COM.CRO` is mostly `RET` and `HOS`.

## 4. Levels

| ID | Level | Setup |
|---|---|---|
| `HIL` | Human in the loop | Human using the SaaS tool with its built-in AI |
| `HOL` | Human on the loop | Human operating from an IDE or assistant through MCP connections |
| `HOOL` | Human out of the loop | Agents given the task to run on their own |

## 5. What every run records

Headline per level: **time, cost and impact** (the outcome graded 0–100 by practitioners against the board's standard). Also recorded: task success, accuracy, tool calls, human time, interventions, read vs. write coverage and safety. Time, cost, review rounds, the tool used and who did the work are recorded per step.

## 6. IDs (*Proposal*)

- Eval: `PLB-{function}.{sub-function}-{nnn}`, e.g. `PLB-CNX.EMAIL-014`
- Run: `{eval}/{vertical}/{level}/{model}/{run}`, e.g. `PLB-CNX.EMAIL-014/RET/HOL/model-2/r1`
- Plumb Line: `PL-{function}.{sub-function}-{nnn}`, matching its eval

## 7. Open questions

- Strategy was a focus area in the brief. It now lives inside sub-functions (media strategy in `ADV`, creative strategy in `CNX.CSTRAT`). Should there be a separate cross-functional strategy area?
- Which vertical × sub-function pairs to skip as not meaningful.
- Board structure: one board per function (assumed here) or per function × vertical.
