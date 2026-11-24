# Pact — rubric (rubric.md)

Generated from rules.json plus the universal criteria in the Eval & Rubric Spec. Scoring runs in four steps: (1) gate — any critical miss fails the asset; (2) adherence 0–100 — share of applicable rules met, major weighted 3 and minor 1; (3) craft 0–100 — AI-judged 1–4 criteria rescaled; (4) quality gate — no critical miss, adherence 90+, craft 3.0+.

AI judge: fixed model, rubric anchors plus golden examples (history_golden_wave1.md), 3 runs, median. Human review: calibration each cycle, 10% sample, every critical flag, and any asset where judge runs differ by more than 1 point.

## Craft criteria (AI judge, 1–4)

| Rule | Criterion | 1 looks like | 4 looks like |
|---|---|---|---|
| BRD-01 | Purpose: make getting dressed an act of self-care, with clothes made to clear, certified standards. | Reads as generic basics or fast fashion | Ties the product to everyday wellness and verified standards |
| BRD-02 | Positioning: certified organic essentials that are gentle on skin and priced for everyday life. | Positions as luxury or as cheapest | Clean, certified, and within reach in one idea |
| BRD-03 | Lead with personal wellness (what touches your skin); planet and people benefits support, never lead. | Opens on saving the planet | Opens on skin, comfort or daily routine, then proof |
| BRD-04 | Personality trait 1 — Caring: is warm and reassuring; is not preachy or guilt-driven. | Shames the reader's current choices | Invites, never scolds |
| BRD-05 | Personality trait 2 — Clear: is plain about what's in the clothes; is not technical or jargon-heavy. | Stacks certifications and acronyms | Explains one standard in plain words |
| BRD-06 | Personality trait 3 — Grounded: is honest about limits; is not absolute or perfectionist. | Claims perfection | Committed to progress, specific about what is verified |
| BRD-07 | Personality trait 4 — Easygoing: is relaxed and a little playful; is not slangy or try-hard outside social. | Slang in email or PDP | Light touch, fits the channel |
| VOI-17 | Tone — promo: upbeat and direct about the deal, never frantic. | Countdown panic, stacked urgency | Clear deal, calm confidence |
| VOI-18 | Tone — service: practical, specific, owns the next step. | Vague or defensive | Names the fix and the timeline |
| VOI-19 | Tone — apology: brief, sincere, no excuses, one concrete remedy. | Blames others | Owns it and offers a fix |
| VOI-20 | Tone — onboarding: welcoming, explains what makes Pact different in one idea per message. | Info dump | One clear idea, one next step |
| VOI-21 | Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines. | Sells during bad news | Facts, impact, what to do |
| VOI-22 | Social may use light internet phrases already in brand use (e.g. 'girl math', 'restock'); never slurs, body comments or slang that mocks. | Slang that punches down | Playful, kind |
| VOI-25 | Sounds like Pact: warm, clear, grounded, easy (matches golden examples). | Could be any brand | Indistinguishable from golden examples |
| MSG-02 | Value prop 1 — Gentle on skin: certified organic cotton made without harsh chemicals, toxic dyes and PFAS. | Missing or wrong proof | Prop plus one proof point |
| MSG-03 | Value prop 2 — Verified standards: GOTS-certified organic cotton, made in Fair Trade Certified™ factories. | Vague 'sustainable' | Names the certification |
| MSG-04 | Value prop 3 — Organic for everyday life: essentials priced for real routines (proof: prices from catalog). | Positions as premium | Price proof from the catalog |
| MSG-15 | Message fits the shared persona (GZ, MIL, GX, BB) and segment named in the task. | Generic | Clearly for that persona, uses a relevant proof |
| SOC-07 | Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md. | Argues or makes a health claim | Kind, specific, on-claim |
| SOC-08 | Video hook: first 2 seconds name the benefit or the price; never fake urgency. | Slow or clickbait | Benefit or price immediately |
| BRA-03 | Concept extends 'what touches your skin matters'; never planet-guilt as the lead. | Off-idea | Extends the brand idea |
| BRA-04 | Key visual: warm neutral palette, one product hero, generous white space. | Busy, off-palette | Calm, on-palette |
| LP-03 | Three benefit blocks map to the three value props. | Random benefits | One block per value prop with proof |

## Gate rules (critical; any miss fails the asset)

- VOI-21 — Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines.
- MSG-01 — Use only claims listed in library/claims.md, worded as approved.
- MSG-05 — 'Starting at $X' only when an active, in-stock SKU is currently priced at $X.
- MSG-06 — 'Up to X% off' only with the maximum stated in offers.csv for that offer.
- MSG-07 — Say 'made with organic cotton' for blends; say '100% organic cotton' only when material is 100% organic cotton.
- MSG-08 — Call a product 'GOTS-certified' only when gots_certified = yes. Pending SKUs: 'made with organic cotton'.
- MSG-09 — Never say every Pact product is certified organic or 100% organic; socks and blends contain recycled nylon or elastane.
- MSG-10 — Water and energy claim: only '81% less water and 62% less energy than conventional cotton', with the comparison. The 95% water figure is retired.
- MSG-11 — Carbon claims must say how: 'carbon neutral through verified offsets with SimpliZero'. Never 'zero emissions' alone.
- MSG-16 — Never imply the clothes have no dyes; say 'toxic dyes', not 'dyes'.
- IMG-07 — No medical or clinical imagery (lab coats, dermatology visuals) implying health benefits.
- IMG-11 — Certification marks (GOTS, Fair Trade) appear only next to certified SKUs and at official artwork.
- IMG-13 — AI-image policy: AI-generated people may not appear in ads; AI-generated product images are labeled and never replace real product shots on PDPs.
- IMG-14 — Reviews shown in imagery use real review text from reviews.csv only.
- LEG-01 — Marketing email: accurate sender, honest subject, physical address '4725 Walnut St, Boulder, CO 80301', working unsubscribe honored within 10 business days.
- LEG-02 — SMS: send only where sms_consent_type = 'prior express written consent'; include brand name and 'Reply STOP to opt out'; send 8am-8pm recipient local time.
- LEG-05 — Every objective claim has substantiation listed in claims.md.
- LEG-06 — Endorsements: creators and partners disclose the material connection (#ad, 'Paid partnership' label, or 'gifted') in the first line; brand reposts keep the disclosure.
- LEG-07 — Reviews: quote only reviews from reviews.csv with usable_in_marketing = yes; label incentivized reviews as incentivized; never use insider or edited reviews.
- LEG-08 — AI content: disclose AI-generated or AI-altered realistic people or scenes, and declare AI creative in Meta, Google and TikTok ad settings.
- LEG-10 — Reference prices: show 'MSRP' or a was-price only when catalog_price_history.csv says msrp_comparison_allowed = yes (charged at MSRP at least 3 of the last 12 months).
- LEG-14 — Textile origin: every online product description states origin ('Imported' or the qualified USA line from catalog).
- LEG-15 — Made in USA: only the qualified line from catalog ('Cut and sewn in USA from imported organic cotton fabric'); never unqualified 'Made in USA'.
- LEG-16 — Fiber content: list fibers by percentage, in descending order, exactly as catalog material. If material is blank, do not state fiber content.
- LEG-17 — No health, disease or skin-condition claims (eczema, rashes, infections, allergies, 'hypoallergenic', 'detox').
- LEG-19 — 'Made without PFAS' only for SKUs with pfas_free = yes; never 'PFAS-free guaranteed' or 'tested free of all chemicals'.
- EML-05 — Footer: address, unsubscribe, preferences, privacy, accessibility, '© 2026 Pact'.
- EML-07 — Transactional emails (order, shipping) lead with order facts; at most one product recommendation, below the order details.
- SOC-06 — Giveaways state eligibility, end date, 'not affiliated with Instagram' and link to rules.
- SOC-07 — Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md.
- DR-01 — Search headlines max 30 characters; descriptions max 90.
- DR-03 — No product superlatives ('best', '#1', 'softest') unless listed in claims.md. 'Best deals' and 'best sellers' are allowed.
- DR-06 — Ad copy matches the landing page offer, price and dates.
- DCO-02 — Price slot uses the feed value with trailing zeros stripped ('$98').
- DCO-03 — compare_price slot renders only when msrp_comparison_allowed = yes; otherwise it is empty.
- LP-05 — Legal footer present with offer terms, privacy and accessibility links.
- WEB-05 — Never invent fit, fabric weight, thread count or features not in catalog.

## Wave 1 task mapping

| Task | Rules in scope (applies_to) |
|---|---|
| P1 product descriptions | 93 rules: BRD-01, BRD-02, BRD-03, BRD-04, BRD-05, BRD-06, BRD-07, BRD-08, VOI-01, VOI-02, VOI-03, VOI-05, VOI-06, VOI-07, VOI-08, VOI-09, VOI-12, VOI-13, VOI-14, VOI-15, VOI-16, VOI-17, VOI-18, VOI-19, VOI-20, VOI-21, VOI-23, VOI-24, VOI-25, MSG-01, MSG-02, MSG-03, MSG-04, MSG-05, MSG-06, MSG-07, MSG-08, MSG-09, MSG-10, MSG-11, MSG-12, MSG-13, MSG-14, MSG-16, MSG-17, MSG-15, IMG-01, IMG-02, IMG-03, IMG-04, IMG-05, IMG-06, IMG-07, IMG-08, IMG-09, IMG-10, IMG-11, IMG-12, IMG-13, IMG-14, IMG-15, ACC-01, ACC-02, ACC-03, ACC-04, ACC-05, ACC-06, ACC-07, ACC-08, ACC-09, ACC-10, ACC-11, ACC-12, LEG-04, LEG-05, LEG-07, LEG-10, LEG-11, LEG-12, LEG-13, LEG-14, LEG-15, LEG-16, LEG-17, LEG-18, LEG-19, LEG-20, WEB-01, WEB-02, WEB-03, WEB-04, WEB-05, WEB-06 |
| E1 promo email | 137 rules: BRD-01, BRD-02, BRD-03, BRD-04, BRD-05, BRD-06, BRD-07, BRD-08, VOI-01, VOI-02, VOI-03, VOI-05, VOI-06, VOI-07, VOI-08, VOI-09, VOI-12, VOI-13, VOI-14, VOI-15, VOI-16, VOI-17, VOI-18, VOI-19, VOI-20, VOI-21, VOI-23, VOI-24, VOI-25, MSG-01, MSG-02, MSG-03, MSG-04, MSG-05, MSG-06, MSG-07, MSG-08, MSG-09, MSG-10, MSG-11, MSG-12, MSG-13, MSG-14, MSG-16, MSG-17, MSG-15, LOG-01, LOG-02, LOG-03, LOG-04, LOG-05, LOG-06, LOG-07, LOG-08, LOG-09, LOG-10, LOG-11, LOG-12, COL-01, COL-02, COL-03, COL-04, COL-05, COL-06, COL-07, COL-08, COL-09, COL-10, COL-11, COL-12, TYP-01, TYP-02, TYP-03, TYP-04, TYP-05, TYP-06, TYP-07, TYP-08, TYP-09, TYP-10, IMG-01, IMG-02, IMG-03, IMG-04, IMG-05, IMG-06, IMG-07, IMG-08, IMG-09, IMG-10, IMG-11, IMG-12, IMG-13, IMG-14, IMG-15, LAY-01, LAY-02, LAY-03, LAY-04, LAY-05, LAY-06, LAY-07, LAY-08, ACC-01, ACC-02, ACC-03, ACC-04, ACC-05, ACC-06, ACC-07, ACC-08, ACC-09, ACC-10, ACC-11, ACC-12, LEG-01, LEG-03, LEG-04, LEG-05, LEG-07, LEG-09, LEG-10, LEG-11, LEG-12, LEG-13, LEG-15, LEG-17, LEG-18, LEG-19, LEG-20, EML-01, EML-02, EML-03, EML-04, EML-05, EML-06, EML-07 |
| A1 paid search | 127 rules: BRD-01, BRD-02, BRD-03, BRD-04, BRD-05, BRD-06, BRD-07, BRD-08, VOI-01, VOI-02, VOI-03, VOI-05, VOI-06, VOI-07, VOI-08, VOI-11, VOI-12, VOI-13, VOI-14, VOI-15, VOI-16, VOI-17, VOI-18, VOI-19, VOI-20, VOI-21, VOI-23, VOI-24, VOI-25, MSG-01, MSG-02, MSG-03, MSG-04, MSG-05, MSG-06, MSG-07, MSG-08, MSG-09, MSG-10, MSG-11, MSG-12, MSG-13, MSG-14, MSG-16, MSG-17, MSG-15, LOG-01, LOG-02, LOG-03, LOG-04, LOG-05, LOG-06, LOG-07, LOG-08, LOG-09, LOG-10, LOG-11, LOG-12, COL-01, COL-02, COL-03, COL-04, COL-05, COL-06, COL-07, COL-08, COL-09, COL-10, COL-11, COL-12, TYP-01, TYP-02, TYP-03, TYP-04, TYP-05, TYP-06, TYP-07, TYP-08, TYP-09, TYP-10, IMG-01, IMG-02, IMG-03, IMG-04, IMG-05, IMG-06, IMG-07, IMG-08, IMG-09, IMG-10, IMG-11, IMG-12, IMG-13, IMG-14, IMG-15, ACC-01, ACC-02, ACC-03, ACC-04, ACC-05, ACC-06, ACC-07, ACC-08, ACC-09, ACC-10, ACC-11, ACC-12, LEG-04, LEG-05, LEG-06, LEG-07, LEG-08, LEG-10, LEG-11, LEG-12, LEG-13, LEG-15, LEG-17, LEG-18, LEG-19, LEG-20, DR-01, DR-02, DR-03, DR-04, DR-05, DR-06 |