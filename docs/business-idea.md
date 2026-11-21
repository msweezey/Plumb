# Plumb: business idea

> **Know what good looks like.**
> Proof, not promises. Scores can't be bought.

Plumb is the standard for AI-native marketing work: **AI marketing evals for AI martech.**

Source of truth: Sweezey's brief of 21 Nov 2026, plus two updates the same day: the eval hierarchy (functions, sub-functions, verticals) and **the task is the unit of evaluation, not the tool**. Anything marked *Proposal* below is a suggestion that fills a gap in the brief and is open for review. Prices are `[Price]` until tested.

---

## 1. The one-line idea

We take real marketing tasks, each a workflow that crosses several tools, and run them three ways: human in the loop (HIL), human on the loop (HOL) and human out of the loop (HOOL). We measure the time, cost and impact of each way, step by step, and practitioners grade the outcome. The Plumb Index is the list of tasks and their results. The playbook behind every task is a forkable Plumb Line.

**The unit is the task, not the tool.** No marketing workflow runs on one tool any more. Tools show up inside the workflows they serve, and their part in each step is measured there.

## 2. The problem

Marketing teams are wiring agents into their stacks. Vendors say their tools are "agent-ready." Nobody measures it.

- Teams can't tell how a given job should now be done: by a person in the tools, by a person directing agents, or by agents alone. Nor what each option costs, how long it takes and how good the result is.
- Buyers can't tell which tools hold up when an agent operates them inside a real workflow, how often it needs a human, or whether it breaks things when it writes.
- Vendors can't prove their tool and MCP server work inside real workflows in a way an enterprise buyer will trust.
- Marketing leaders have no reference for what an AI-native team, stack or workflow should look like, or what numbers to hold it to.
- AI labs need realistic, expert-graded marketing tasks and environments to train and evaluate on, and they don't have them.

## 3. Why now

Major martech vendors now ship official MCP servers (HubSpot, Salesforce Marketing Cloud, Adobe Marketo, Klaviyo, Canva and others). The buyer's question has shifted from **"which tool has the best UI?"** to **"how should this job be done now, and which tools can my agents operate to do it?"** There is no independent answer yet.

## 4. What we do

### Three levels of autonomy

Every task is run at all three levels, so teams see how far they can hand it over and what that changes.

| Level | Setup | What it shows |
|---|---|---|
| **Human in the loop (HIL)** | A marketer uses the SaaS tools' own UIs and built-in AI | The baseline: what the job costs a skilled operator today |
| **Human on the loop (HOL)** | A marketer works from an IDE or assistant (Claude, Antigravity and similar) through MCP connections | Time and cost saved, how often the human steps in |
| **Human out of the loop (HOOL)** | Agents are given the task and run it on their own | End-to-end time, cost and impact, and whether they write safely |

For every task the Index shows the **best way**: *Proposal:* the lowest-cost level whose impact meets the board's standard.

### How an eval works

1. **Task library.** Real marketing-ops workflows that each cross several tools, for example: build a 3-email nurture; pull last month's results and pause the losers; clone and localize a live campaign; route a lead form; clean 500 contacts. Covers B2B and B2C workflows from enterprise down. Boards choose the tasks.
2. **Harness.** Each task × each level × several AI models × each relevant vertical, run in sandbox accounts for every tool in the workflow, connected through their MCP servers. Same tasks, same models, every time.
3. **Scoring.** Every run is scored on:
   - task success
   - accuracy
   - tool calls / steps
   - cost per task
   - time
   - human interventions
   - read vs. write coverage
   - safety (can it write without breaking things)
   - final outcome, graded by practitioners in that discipline
4. **Output.** Each task gets a full breakdown by level: time, cost, impact, human time, interventions and review rounds, for every step and the tool used in it. The headline (impact, time and cost per level, and the best way) goes on the Index. Behind each result sits a full, forkable playbook (a Plumb Line) so anyone can adopt the play.

### Functions, sub-functions and verticals

Evals are organized by marketing function and sub-function, and run across five major verticals. Full hierarchy, IDs and example tasks: [`eval-taxonomy.md`](eval-taxonomy.md) (data: [`../data/eval-taxonomy.json`](../data/eval-taxonomy.json)).

| Function | Sub-functions |
|---|---|
| **Advertising & Promotion** (media strategy) | Media planning & audience targeting · Programmatic & paid media buying · Campaign execution & bid optimization · Creative ad production & DCO |
| **Content & Experience** | Creative strategy · Content creation · Scaled content creation · Web content management & landing page optimization · Email marketing & marketing automation · Website personalization & SEO |
| **Social & Relationships** | Social media publishing & listening · Influencer & creator marketing |
| **Commerce & Sales** | Lead capture, scoring & routing · Account-based marketing · E-commerce merchandising & CRO · Loyalty & referral programs |

**Verticals:** Retail & E-Commerce · Healthcare & Life Sciences · Financial Services & Insurance · Hospitality & Travel · B2B & Industrial/Manufacturing.

Every eval is one task inside a sub-function. It runs in each relevant vertical, at each level, with each model, across whatever tools the workflow needs. Scores roll up from steps to runs to each level of the task.

### Boards

Each function has a **board of practitioners**. Board members:

- choose the tasks
- review results before anything is published
- add the "board take" to each result
- publish content we prepare under their own names

The boards guide the research and are our marketing arm. Their credibility is the product's credibility.

### Knowledge of AI-native marketing

Every eval also teaches us how AI-native marketing work is actually done: stacks, playbooks, team structure, roles and responsibilities, and job descriptions. We package that so teams can build it.

## 5. Who buys (in priority order)

| # | Buyer | What they need | What they buy |
|---|---|---|---|
| 1 | **Martech and AI tool vendors** moving upmarket | Independent proof their tool works when agents run it inside real workflows, to win enterprise deals | Certification ("Plumbed"), full results, fix lists |
| 2 | **Enterprise marketing teams** | AI-native playbooks, stack information and benchmarks to target. Replaces traditional analyst services | Enterprise: playbooks, teams, roles, JDs, stack and vendor analysis, benchmarks |
| 3 | **AI labs** | Realistic task suites and environments for training and evals | Licensed task suites, rubrics and sandbox environments, directly or through partners such as Mercor or Surge |
| 4 | **Agencies and integrators** | A neutral basis for stack recommendations | Benchmarks and certification |

**Not a fit:** small brands without ops teams; pre-revenue tools.

## 6. Products

| Product | What it is | Who it's for | Price |
|---|---|---|---|
| **The Plumb Index** | Free public list of tasks by function and sub-function, filterable by vertical, with impact, time and cost at each level | Everyone; top of funnel | Free |
| **Plumb Lines** | Machine-readable, forkable playbooks with a full readout for humans. Followed, forked and graded by the community | Practitioners, teams, agents | Free (*Proposal:* the open layer) |
| **Plumbed certification** | How a vendor's tool and MCP server perform inside each workflow they serve: full results, fix list, and the "Plumbed" mark when the standard is met | Vendors, agencies | `[Price]` |
| **Enterprise** | AI-native marketing playbooks including teams, roles, JDs, stack and vendor analysis, and benchmarks | Enterprise marketing teams | `[Price]` |
| **Labs licensing** | Task suites, rubrics, sandbox environments | AI labs, data partners | `[Price]` |
| **Monthly report** | Report by eval set × vertical | Enterprise teams, vendors, agencies | `[Price]` |

## 7. How the pieces reinforce each other

One eval engine produces everything:

1. Boards pick tasks → we build sandboxes and rubrics.
2. Runs produce scores → **Index** (free, public) and **monthly report**.
3. Winning runs become **Plumb Lines** → the community forks and grades them, which improves the tasks.
4. Results and Plumb Lines roll up into the **Enterprise** kit (stack, team, roles, JDs, benchmarks).
5. Vendors whose tools slow down or break workflows buy **certification** testing and fix lists to get there.
6. The same expert-graded suites and sandboxes are licensed to **AI labs** behind the scenes.

Public results are what make the paid products credible. Labs licensing is what funds depth in the task library.

## 8. Integrity rules

"Scores can't be bought" has to be true in the mechanics, not just the copy. *Proposal:*

- The public Index runs every task with the tools teams actually use, whether or not those vendors pay.
- Vendors pay for testing, full results and fix lists. They never pay for a score, a rank or a board take.
- "Plumbed" is awarded only when a tool meets a published standard set by the board. No vendor sits on a board.
- Every score shows its method and sample beside it: models, runs, tasks, date.
- Results are reviewed by the board before publishing. Vendors see their own results before publication for factual corrections only.
- Labs licensing never includes vendor-confidential results.

## 9. Go to market

*Proposal*, built from the brief:

- **Boards first.** Recruit one board per function. Their names, posts and board takes are the launch.
- **Index as the hook.** Launch with one sub-function (Email marketing & marketing automation is the most MCP-ready) in one or two verticals, a dozen tasks, published free.
- **Monthly report** as the recurring reason to come back and the first paid touch.
- **Vendor motion.** Every vendor whose tool appears in a task gets its step-level results; those that hold workflows back are offered certification testing and fix lists.
- **Enterprise motion.** Lead with benchmarks for the buyer's vertical, then the playbooks, team design and JDs.
- **Labs motion.** Package the task suites and sandboxes once two functions are live; sell directly and through data partners.

## 10. What the website needs to do

The mockup in [`site/index.html`](../site/index.html) is deliberately short:

1. Hero: "Every marketing task, run three ways," with the three levels explained
2. The Plumb Index: a list of tasks, filtered by function and vertical. Each row shows impact, time and cost for HIL, HOL and HOOL, and marks the best way
3. One task, broken down: the tools in the workflow, a card per level (time, cost, impact against the standard, human time, interventions, unsafe writes), time by step, and the board take with the Plumb Line
4. Method and who it's for, with `[Price]`s

All data in the mockup is sample data with anonymized tools. People, quotes and prices are placeholders.

## 11. Open questions

- Prices for certification, enterprise, labs licensing and the report.
- Launch sub-function, verticals and the first tasks to run.
- How "impact" is defined per task (practitioner grade only, or also a business outcome such as projected lift).
- How the best way is chosen when no level meets the standard.
- Board composition, compensation and conflict-of-interest policy.
- How often each eval re-runs (monthly with the Index, or on each vendor MCP release).
- Which models sit in the harness, and how we handle model updates.
- Whether Plumb Lines are free and open by default (assumed here).
- Strategy: a separate cross-functional area, or only inside sub-functions as now (see the taxonomy doc).
- Which vertical × sub-function pairs to skip.

## 12. Out of scope

Plumb is **not** a brand-ranking index, an agentic commerce index, a paid/owned/earned tracker or a CMO strategy readout. Those were earlier directions and are retired. Agentic commerce is context only.
