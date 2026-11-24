# Edikted — rubric (rubric.md)

Same scoring as every Plumb harness: (1) gate — any critical miss fails; (2) adherence 0–100, major weighted 3, minor 1; (3) craft 1–4 by AI judge against the anchors below and the golden examples; (4) human review on a 10% sample and every critical flag.

## Craft criteria (AI judge, 1–4)

| Rule | Criterion | 1 looks like | 4 looks like |
|---|---|---|---|
| BRD-01 | Purpose: get the outfit she saw on her feed into her closet fast, at a price that doesn't sting. | Slow, generic fashion talk | Trend, speed and price in one breath |
| BRD-02 | Positioning: trend-led going-out and everyday fits for Gen Z, most under $40, launched in weekly drops and shown on creators first. | Could be any mall brand | Unmistakably drop-driven, creator-first Edikted |
| BRD-03 | Lead with the fit or the moment (GNO, holiday party, class); price and sale come second unless it is a sale message. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-04 | Trait 1 — Loud: caps-and-emoji bursts on hype words; is not one long all-caps wall. | Flat or shouting the whole time | Bursts of caps that land on the right words |
| BRD-05 | Trait 2 — Insider: talks like her group chat ('RN', 'fits', 'hits different'); is not dated slang or brand-trying-to-be-cool. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-06 | Trait 3 — Hype: real urgency tied to real dates and drops; is not fake scarcity. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRD-07 | Trait 4 — Playful and flirty: fun, confident, a wink; is not sexualized and never body-shaming. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-17 | Tone — promo: hype, caps on the number and the event, 1–5 emoji; never threatening ('you'll regret it'). | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-18 | Tone — service: practical, specific, owns the next step. | Vague or defensive | Names the fix and the timeline |
| VOI-19 | Tone — apology: brief, sincere, no excuses, one concrete remedy. | Blames others | Owns it and offers a fix |
| VOI-20 | Tone — onboarding: welcome to the crew, app code APP10, how drops work. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-21 | Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines. | Sells during bad news | Facts, impact, what to do |
| VOI-25 | Sounds like Edikted: loud, insider, hype, playful (matches golden examples). | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-02 | Value prop 1 — The trend, now: weekly drops of what's on her feed. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-03 | Value prop 2 — Prices that don't sting: most pieces under $40 (catalog median $26). | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-04 | Value prop 3 — Seen on creators: fit shown on real creators; model size and height on every PDP. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-15 | Message fits the shared persona (GZ, MIL, GX, BB) and segment named in the task. | Generic | Clearly for that persona, uses a relevant proof |
| LOG-10 | The wordmark is always caps EDIKTED; never retype it in another font. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| IMG-01 | Image types: creators and models in flash photography, mirror selfies, night-out scenes, street style, TV-show sets for campaigns. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| IMG-02 | Real-feeling Gen Z women, a range of bodies and skin tones; confident, never sexualized poses. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| SOC-07 | Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md. | Argues or makes a health claim | Kind, specific, on-claim |
| SOC-08 | Video hook: first 2 seconds name the benefit or the price; never fake urgency. | Slow or clickbait | Benefit or price immediately |
| BRA-03 | Concept: a show, a drop, a moment ('LIGHTS, CAMERA, BLACK FRIDAY'); never a lecture. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRA-04 | Key visual: flash-lit creator in the hero fit, bubblegum and ink, a big Druk Wide number. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| LP-03 | Three blocks: the drop, the price, the creators wearing it. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |

## Gate rules (critical)

- VOI-21 — Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines.
- MSG-01 — Use only claims listed in library/claims.md, worded as approved.
- MSG-05 — 'Starting at $X' only when an active, in-stock SKU is currently priced at $X.
- MSG-06 — 'Up to X% off' only with the maximum stated in offers.csv for that offer.
- MSG-07 — Never print fiber percentages; the catalog lists fibers only.
- MSG-08 — Items with status coming_soon are teased ('drops 12/16'), never 'shop now'.
- MSG-09 — 'Everything' or 'sitewide' only when the offer has no item exclusions (OF-01 excludes warehouse items and gift cards: say 'everything*' with the exclusion line).
- MSG-10 — Savings claims carry '*Based on comp value'; never show a struck 'was' price unless msrp_comparison_allowed = yes.
- MSG-11 — Never call anything sustainable, eco or ethical; Edikted makes no sustainability claims.
- MSG-16 — Prop 65: PDPs for prop65 = yes SKUs carry the CA warning line; never claim 'non-toxic'.
- IMG-07 — No medical or clinical imagery (lab coats, dermatology visuals) implying health benefits.
- IMG-11 — Creator handles shown only with their partnership disclosed.
- IMG-13 — AI-image policy: AI-generated people may not appear in ads; AI-generated product images are labeled and never replace real product shots on PDPs.
- IMG-14 — Reviews shown in imagery use real review text from reviews.csv only.
- LEG-01 — Marketing email: accurate sender, honest subject, physical address '1327 Willow St, Los Angeles, CA 90013' (directory listing; confirm), unsubscribe.
- LEG-02 — SMS: send only where sms_consent_type = 'prior express written consent'; include brand name and 'Reply STOP to opt out'; send 8am-8pm recipient local time.
- LEG-05 — Every objective claim has substantiation listed in claims.md.
- LEG-06 — Endorsements: creators and partners disclose the material connection (#ad, 'Paid partnership' label, or 'gifted') in the first line; brand reposts keep the disclosure.
- LEG-07 — Reviews: quote only reviews from reviews.csv with usable_in_marketing = yes; label incentivized reviews as incentivized; never use insider or edited reviews.
- LEG-08 — AI content: disclose AI-generated or AI-altered realistic people or scenes, and declare AI creative in Meta, Google and TikTok ad settings.
- LEG-10 — Reference prices: show 'MSRP' or a was-price only when catalog_price_history.csv says msrp_comparison_allowed = yes (charged at MSRP at least 3 of the last 12 months).
- LEG-14 — Textile origin: 'Imported' on every product description.
- LEG-15 — Never claim Made in USA.
- LEG-16 — Fiber content: list fibers in catalog order; never invent percentages.
- LEG-17 — No health, disease or skin-condition claims (eczema, rashes, infections, allergies, 'hypoallergenic', 'detox').
- LEG-19 — Returns: link the returns policy; never state a window not in the files.
- EML-05 — Footer: address, unsubscribe, preferences, privacy, accessibility, '© 2026 Edikted'.
- EML-07 — Transactional emails (order, shipping) lead with order facts; at most one product recommendation, below the order details.
- SOC-06 — Giveaways state eligibility, end date, 'not affiliated with Instagram' and link to rules.
- SOC-07 — Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md.
- DR-01 — Search headlines max 30 characters; descriptions max 90.
- DR-03 — No product superlatives ('best', '#1', 'softest') unless listed in claims.md. 'Best deals' and 'best sellers' are allowed.
- DR-06 — Ad copy matches the landing page offer, price and dates.
- DCO-02 — Price slot uses feed price; comp slot only per DCO-03.
- DCO-03 — compare_price slot renders only when msrp_comparison_allowed = yes; otherwise it is empty.
- LP-05 — Legal footer present with offer terms, privacy and accessibility links.
- WEB-05 — Never invent fit, fabric weight, thread count or features not in catalog.