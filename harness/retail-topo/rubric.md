# Topo Designs — rubric (rubric.md)

Same scoring as every Plumb harness: (1) gate — any critical miss fails; (2) adherence 0–100, major weighted 3, minor 1; (3) craft 1–4 by AI judge against the anchors below and the golden examples; (4) human review on a 10% sample and every critical flag.

## Craft criteria (AI judge, 1–4)

| Rule | Criterion | 1 looks like | 4 looks like |
|---|---|---|---|
| BRD-01 | Purpose: get everyone outside, without the gatekeeping that holds people back (co-founder Jedd Rose). | Hardcore or exclusive outdoor talk | Welcoming: town or trail, everyone belongs |
| BRD-02 | Positioning: durable, classic, functional bags and apparel designed in Colorado since 2008, for town and trail. | Generic outdoor gear | Classic design + durability + anywhere use |
| BRD-03 | Lead with where it goes and what it carries; materials and features are the proof. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-04 | Trait 1 — Friendly: 'our friends', thank-yous, community; is not corporate. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-05 | Trait 2 — Easygoing outdoors: trailheads and tailgates alike; is not hardcore, technical-only or gatekeeping. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-06 | Trait 3 — Crafted: specific about materials, capacity and features; is not a spec-sheet dump. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-07 | Trait 4 — Playful: light humor and a few emoji on social; is not goofy in ads. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-16 | Collab copy names the partner, credits them as 'our friends', and says what each side brought. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-17 | Tone — promo: relaxed and honest about the deal ('The days are shorter. So is this sale.'); never frantic. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-18 | Tone — service: practical, specific, owns the next step. | Vague or defensive | Names the fix and the timeline |
| VOI-19 | Tone — apology: brief, sincere, no excuses, one concrete remedy. | Blames others | Owns it and offers a fix |
| VOI-20 | Tone — onboarding: welcome to the Topo Crew, 10% off the first order, the M.A.P. Guarantee™. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-21 | Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines. | Sells during bad news | Facts, impact, what to do |
| VOI-25 | Sounds like Topo Designs: friendly, easygoing, crafted, playful (matches golden examples). | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-02 | Value prop 1 — Built to last: durable materials (recycled nylon, organic cotton, wool) backed by the M.A.P. Guarantee™. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-03 | Value prop 2 — Made for anywhere: one bag from commute to trailhead to carry-on. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-04 | Value prop 3 — Colorado design and friends: designed in Colorado since 2008; collaborations with brands we like. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-15 | Message fits the shared persona (GZ, MIL, GX, BB) and segment named in the task. | Generic | Clearly for that persona, uses a relevant proof |
| LOG-10 | Wordmark caps belong to the logo only; never retype it. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| IMG-01 | Image types: gear on people in town and outdoors, trailheads, road trips, bikes, camp, flat lays of what fits inside. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| IMG-02 | Real people with friends and dogs, a range of ages and bodies; warm natural light; color-forward gear. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| SOC-07 | Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md. | Argues or makes a health claim | Kind, specific, on-claim |
| SOC-08 | Video hook: first 2 seconds name the benefit or the price; never fake urgency. | Slow or clickbait | Benefit or price immediately |
| BRA-03 | Concept: places on the map, friends along the way; never extreme-sport bravado. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRA-04 | Key visual: color-forward bag on a person outdoors, bone and charcoal frame, a red accent. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| LP-03 | Three blocks map to built to last, made for anywhere, Colorado design and friends. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |

## Gate rules (critical)

- VOI-21 — Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines.
- MSG-01 — Use only claims listed in library/claims.md, worded as approved.
- MSG-05 — 'Starting at $X' only when an active, in-stock SKU is currently priced at $X.
- MSG-06 — 'Up to X% off' only with the maximum stated in offers.csv for that offer.
- MSG-07 — 'Water resistant' only for SKUs with water_resistant = yes; never 'waterproof' or 'weatherproof'.
- MSG-08 — Coming-soon SKUs are teased with the date, never 'shop now'.
- MSG-09 — Never say all products are made in the USA or handmade in Colorado; printed-in-Colorado items say exactly that.
- MSG-10 — Recycled content: name the recycled material as catalog; no percentage unless the catalog states one.
- MSG-11 — Guarantee: 'M.A.P. Guarantee™' exactly; 'We guarantee everything we make' allowed; never 'lifetime warranty'.
- MSG-16 — Limited editions: never promise restocks.
- IMG-07 — No medical or clinical imagery (lab coats, dermatology visuals) implying health benefits.
- IMG-11 — Partner logos appear only on collaboration products.
- IMG-13 — AI-image policy: AI-generated people may not appear in ads; AI-generated product images are labeled and never replace real product shots on PDPs.
- IMG-14 — Reviews shown in imagery use real review text from reviews.csv only.
- LEG-01 — Marketing email: accurate sender, honest subject, physical address 'York Street Yards, Steele St, Denver, CO 80205' (suite to confirm), unsubscribe.
- LEG-02 — SMS: send only where sms_consent_type = 'prior express written consent'; include brand name and 'Reply STOP to opt out'; send 8am-8pm recipient local time.
- LEG-05 — Every objective claim has substantiation listed in claims.md.
- LEG-06 — Endorsements: creators and partners disclose the material connection (#ad, 'Paid partnership' label, or 'gifted') in the first line; brand reposts keep the disclosure.
- LEG-07 — Reviews: quote only reviews from reviews.csv with usable_in_marketing = yes; label incentivized reviews as incentivized; never use insider or edited reviews.
- LEG-08 — AI content: disclose AI-generated or AI-altered realistic people or scenes, and declare AI creative in Meta, Google and TikTok ad settings.
- LEG-10 — Reference prices: show 'MSRP' or a was-price only when catalog_price_history.csv says msrp_comparison_allowed = yes (charged at MSRP at least 3 of the last 12 months).
- LEG-14 — Origin: 'Imported' on every product description unless catalog says otherwise.
- LEG-15 — Made in USA: never, unless all or virtually all of the product is made in the US and claims.md says so; printing in Colorado is not Made in USA.
- LEG-16 — Materials as catalog; no invented deniers, capacities or percentages.
- LEG-17 — No health, disease or skin-condition claims (eczema, rashes, infections, allergies, 'hypoallergenic', 'detox').
- LEG-19 — Returns: free exchanges; link the returns policy for anything else.
- EML-05 — Footer: address, unsubscribe, preferences, privacy, accessibility, '© 2026 Topo Designs'.
- EML-07 — Transactional emails (order, shipping) lead with order facts; at most one product recommendation, below the order details.
- SOC-06 — Giveaways state eligibility, end date, 'not affiliated with Instagram' and link to rules.
- SOC-07 — Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md.
- DR-01 — Search headlines max 30 characters; descriptions max 90.
- DR-03 — No product superlatives ('best', '#1', 'softest') unless listed in claims.md. 'Best deals' and 'best sellers' are allowed.
- DR-06 — Ad copy matches the landing page offer, price and dates.
- DCO-02 — Price slot uses feed value with trailing zeros stripped.
- DCO-03 — compare_price slot renders only when msrp_comparison_allowed = yes; otherwise it is empty.
- LP-05 — Legal footer present with offer terms, privacy and accessibility links.
- WEB-05 — Never invent fit, fabric weight, thread count or features not in catalog.