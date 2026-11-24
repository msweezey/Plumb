# M.M.LaFleur — rubric (rubric.md)

Same scoring as every Plumb harness: (1) gate — any critical miss fails; (2) adherence 0–100, major weighted 3, minor 1; (3) craft 1–4 by AI judge against the anchors below and the golden examples; (4) human review on a 10% sample and every critical flag.

## Craft criteria (AI judge, 1–4)

| Rule | Criterion | 1 looks like | 4 looks like |
|---|---|---|---|
| BRD-01 | Purpose: help women who lead get dressed with ease, so their attention goes to the work and the life, not the closet. | Fashion-for-fashion's-sake or generic workwear | Ties the piece to her day: what it lets her do, with less effort |
| BRD-02 | Positioning: 'Power Casual' — polished, easy-care pieces designed in New York for real working days, with personal styling. | Could be any office-wear brand | Polished + easy-care + designed for her whole day, unmistakably M.M. |
| BRD-03 | Lead with her day (meetings, travel, dinner after); fabric performance is the proof, never the headline alone. | Spec dump | Moment first, proof second |
| BRD-04 | Trait 1 — Polished: composed, precise sentences; is not stiff or corporate. | Sloppy or stiff | Composed and warm |
| BRD-05 | Trait 2 — Witty: dry, knowing humor ('A generous spirit, technically.'); is not jokey, slangy or meme-driven. | Slang or forced jokes | A light, intelligent turn |
| BRD-06 | Trait 3 — Practical: specific about fabric, care, pockets and fit; is not fashion jargon. | Vague adjectives | Concrete, useful details |
| BRD-07 | Trait 4 — Assured: speaks to a capable woman as a peer; is not pushy, bossy or flattering. | Pushy or sycophantic | Peer-to-peer confidence |
| VOI-16 | Recurring devices may be used as written: 'Some decisions are easy:' outfit posts, 'Samantha' vignettes, quote posts with attribution, and quoted product nicknames. | Device misused (unattributed quote, Samantha in an ad) | Device used in its native channel with its native form |
| VOI-17 | Tone — promo: calm and confident about the offer; never frantic or countdown-driven. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-18 | Tone — service: practical, specific, owns the next step. | Vague or defensive | Names the fix and the timeline |
| VOI-19 | Tone — apology: brief, sincere, no excuses, one concrete remedy. | Blames others | Owns it and offers a fix |
| VOI-20 | Tone — onboarding: introduce one idea per message (Power Casual, easy care, styling), in that order. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| VOI-21 | Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines. | Sells during bad news | Facts, impact, what to do |
| VOI-25 | Sounds like M.M.LaFleur: polished, witty, practical, assured (matches golden examples). | Generic or off-register | Indistinguishable from M.M.'s best ads |
| MSG-02 | Value prop 1 — Designed for her whole day: easy-care fabrics (machine washable, wrinkle-resistant, stretch) that go meeting to dinner to flight. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-03 | Value prop 2 — Power Casual: tailored lines in comfortable fabrics; polished without the stiffness. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-04 | Value prop 3 — Help getting dressed: complimentary personal styling in showrooms and virtually; outfits shown as complete looks. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| MSG-15 | Message fits the shared persona (GZ, MIL, GX, BB) and segment named in the task. | Generic | Clearly for that persona, uses a relevant proof |
| LOG-10 | Never retype the wordmark or drop its periods ('MM LaFleur'). | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| IMG-01 | Image types: complete looks on figure, studio and city settings, outfit flat lays, detail shots of fabric and pockets. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| IMG-02 | Real working women of a range of ages (30s–60s), sizes and skin tones; composed, not fashion-editorial poses. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| SOC-07 | Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md. | Argues or makes a health claim | Kind, specific, on-claim |
| SOC-08 | Video hook: first 2 seconds name the benefit or the price; never fake urgency. | Slow or clickbait | Benefit or price immediately |
| BRA-03 | Concept extends 'dress with ease so you can lead'; never fashion-as-status. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| BRA-04 | Key visual: complete look on a real woman, warm neutral set, espresso and ivory palette. | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |
| LP-03 | Three benefit blocks map to the three value props (whole day, Power Casual, styling). | Ignores or contradicts this rule | Does this clearly, at the level of the golden examples |

## Gate rules (critical)

- VOI-21 — Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines.
- MSG-01 — Use only claims listed in library/claims.md, worded as approved.
- MSG-05 — 'Starting at $X' only when an active, in-stock SKU is currently priced at $X.
- MSG-06 — 'Up to X% off' only with the maximum stated in offers.csv for that offer.
- MSG-07 — Say 'machine washable' only for SKUs with machine_washable = yes; 'wrinkle-resistant' only with wrinkle_resistant = yes. Never 'wrinkle-proof'.
- MSG-08 — Partner products (vendor = Partner) are never called 'designed by M.M.' or 'our fabric'; name the maker.
- MSG-09 — Never say every M.M. piece is machine washable; 47 SKUs in the feed are dry-clean only.
- MSG-10 — Fabric origin claims ('Italian fabric', 'Japanese crepe') only when in claims.md for that fabric.
- MSG-11 — Fiber percentages ('100% cashmere') only when the catalog material says so for that SKU.
- MSG-16 — Body-type tags (e.g. 'Middle-friendly') are internal merchandising data; never print them as body-fixing copy.
- IMG-07 — No medical or clinical imagery (lab coats, dermatology visuals) implying health benefits.
- IMG-11 — Partner logos appear only on partner products and collaborations.
- IMG-13 — AI-image policy: AI-generated people may not appear in ads; AI-generated product images are labeled and never replace real product shots on PDPs.
- IMG-14 — Reviews shown in imagery use real review text from reviews.csv only.
- LEG-01 — Marketing email: accurate sender, honest subject, physical address '100 Broadway, Fl 3, New York, NY 10005' (directory listing; confirm), unsubscribe.
- LEG-02 — SMS: send only where sms_consent_type = 'prior express written consent'; include brand name and 'Reply STOP to opt out'; send 8am-8pm recipient local time.
- LEG-05 — Every objective claim has substantiation listed in claims.md.
- LEG-06 — Endorsements: creators and partners disclose the material connection (#ad, 'Paid partnership' label, or 'gifted') in the first line; brand reposts keep the disclosure.
- LEG-07 — Reviews: quote only reviews from reviews.csv with usable_in_marketing = yes; label incentivized reviews as incentivized; never use insider or edited reviews.
- LEG-08 — AI content: disclose AI-generated or AI-altered realistic people or scenes, and declare AI creative in Meta, Google and TikTok ad settings.
- LEG-10 — Reference prices: show 'MSRP' or a was-price only when catalog_price_history.csv says msrp_comparison_allowed = yes (charged at MSRP at least 3 of the last 12 months).
- LEG-14 — Textile origin: every product description states origin ('Imported' or the 'Made in X' line from catalog).
- LEG-15 — Made in USA: only for SKUs with origin 'Made in USA', word for word.
- LEG-16 — Fabric: use catalog fabric name; never invent fiber percentages.
- LEG-17 — No health, disease or skin-condition claims (eczema, rashes, infections, allergies, 'hypoallergenic', 'detox').
- LEG-19 — Returns: 21 days for full-price, unworn items; $8.95 restocking fee on US mail returns; exchanges and in-store returns free. State exactly or link.
- EML-05 — Footer: address, unsubscribe, preferences, privacy, accessibility, '© 2026 M.M.LaFleur'.
- EML-07 — Transactional emails (order, shipping) lead with order facts; at most one product recommendation, below the order details.
- SOC-06 — Giveaways state eligibility, end date, 'not affiliated with Instagram' and link to rules.
- SOC-07 — Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md.
- DR-01 — Search headlines max 30 characters; descriptions max 90.
- DR-03 — No product superlatives ('best', '#1', 'softest') unless listed in claims.md. 'Best deals' and 'best sellers' are allowed.
- DR-06 — Ad copy matches the landing page offer, price and dates.
- DCO-02 — Price slot uses feed value as listed.
- DCO-03 — compare_price slot renders only when msrp_comparison_allowed = yes; otherwise it is empty.
- LP-05 — Legal footer present with offer terms, privacy and accessibility links.
- WEB-05 — Never invent fit, fabric weight, thread count or features not in catalog.