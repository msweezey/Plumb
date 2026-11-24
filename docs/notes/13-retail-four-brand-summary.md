# Retail test brands: four-brand build and test summary

Built 22 Nov 2026. Pact was the base. M.M.LaFleur, Edikted and Topo Designs were then built and tested the same way, with what we learned from Pact applied up front:

1. Write Method A assumptions first.
2. Gather evidence: site HTML and CSS, the Shopify product feed, Meta ads, Instagram, policy pages and press.
3. Reverse-engineer the brand book (Method B).
4. Build the full dataset.
5. Calibrate the rules against the brand's real copy.
6. Run the same four tests.

The files are in `harness/retail-<brand>/`, and the per-brand write-ups are claude/10 to claude/12.

## Outcomes

| Brand | Quadrant | Fidelity, tuning | Fidelity, held-out | Other brands' copy rejected | Goldens | Seeded traps caught |
|---|---|---|---|---|---|---|
| Pact (base) | restrained × value | 37/39 (95%) | 10/10 (100%) | 80/83 (96%) | 6/6 | 36/36 |
| M.M.LaFleur | restrained × premium | 41/42 (98%) | 16/17 (94%) | 90/96 (94%) | 6/6 | 40/40 |
| Edikted | expressive × value | 47/47 (100%) | 19/19 (100%) | 89/89 (100%) | 6/6 | 42/42 |
| Topo Designs | expressive × premium | 47/48 (98%) | 17/18 (94%) | 83/89 (93%) | 6/6 | 42/42 |

How to read the table:
- **Fidelity** is the share of the brand's own real copy that passes its brand-layer rules.
- **Rejected** counts other brands' ads and posts that fail this brand's brand-layer rules.
- All four brands meet the Pact targets: about 90% fidelity on both splits, at least 85% rejection, 6/6 goldens and every seeded trap caught.
- The Pact row uses the shared engine. Pact's own engine scored 92% on tuning and 90% on held-out, against slightly different rules.

## Discrimination matrix (brand layer)

| Copy from ↓ / rules of → | Pact | M.M.LaFleur | Edikted | Topo Designs |
|---|---|---|---|---|
| Pact | — | 32/36 (89%) | 36/36 (100%) | 32/36 (89%) |
| M.M.LaFleur | 23/23 (100%) | — | 23/23 (100%) | 22/23 (96%) |
| Edikted | 29/30 (97%) | 30/30 (100%) | — | 29/30 (97%) |
| Topo Designs | 28/30 (93%) | 28/30 (93%) | 30/30 (100%) | — |

**Easy cells:** expressive copy against restrained rules. Emoji and all-caps limits catch it almost every time, in both directions. Edikted's rules *require* emoji and caps, so calm copy fails them.

**Hard cells:** the restrained pairs (Pact ↔ MML, Pact → Topo). Mechanics barely differ there. What separates them is vocabulary and category:
- Pact's wellness register ("skincare you wear", "clean fabrics") is off-voice for M.M.LaFleur.
- Suiting, cashmere and tweed are off-category for Pact.
- Pack, trail and carry words belong to Topo.

## What changed from the Pact method

- **One engine, four configs.** `harness/shared/checks_engine.py` is the Pact check engine with every brand value moved into `harness/shared/brand_configs.py`. Configs hold emoji, caps and exclamation ranges per channel, reading level, sentence length, vocabulary, off-voice words, category boundaries, offer percentages, the shipping threshold and compliance patterns. Each harness's `checks.py` bundles the engine with that brand's config.
- **Minimums as well as maximums.** Pact only needed caps on emoji and caps. Edikted needs floors: an Edikted ad with no emoji is off-brand.
- **A category-boundary rule (BRD-09).** This rule is what separates restrained brands from each other.
- **Channel-split voice.** Topo's ads use no emoji and Title Case, while its Instagram uses 1–3 emoji. MML allows emoji only as list bullets.
- **Brand devices.** MML's quote posts with attribution pass its vocabulary rule. The same quote fails the other brands' rules.
- **The catalog comes from the real product feed.** Each brand has 200 SKUs drawn from 250 Shopify products. Store tags became trap columns:
  - **MML:** machine-washable and wrinkle-resistant flags, final-sale tiers and partner (Shopify Collective) goods.
  - **Edikted:** Prop 65 warnings, future drop dates and comp-value pricing.
  - **Topo:** coming-soon and limited-edition tags, collab partners and printed-in-Colorado notes.

## Calibration log

1. **First pass with shared rules, before any tuning.**
   - Edikted already passed 100% of its own copy, because its loud mechanics leave little room for error.
   - MML failed many product pages and quote posts on the vocabulary rule.
   - Discrimination was weak in the restrained cells, around 60–80%.
2. **Category boundaries and sharper vocabulary.**
   - Generic words ("designed", "everyday", "favorite") were dropped from Topo's vocabulary.
   - Off-voice lists were added, along with a product-page vocabulary for MML.
   - Rejection in the restrained cells rose to 89–96%.
3. **Over-tightening, then undoing it.** "luxe", "organic" and "breathable" broke MML's own product pages ("Luxe Flex Suiting", "Pima Cotton", "Tropical Wool"), and "stylish" broke a Topo ad. All four words were removed again.
4. **Held-out leakage, disclosed.** After round 1, held-out results were inspected. One later fix, collab naming ("Topo Designs x …"), came from a tuning-split post ("Puffin x Topo Designs", "@topodesigns x @puffindrinkwear"). It also fixed two held-out product pages, so Topo's held-out score is slightly optimistic.
5. **A golden example caught a bad rule.** MML's golden blazer copy said "comes out of a carry-on", which "carry-on" in the off-category list blocked. MML sells a partner carry-on, so the term was removed.

## Remaining brand misses (the brands' own inconsistencies)

- **Pact:** "PACT" in caps in one ad, and the retired "Earth's Favorite™" line on the About page.
- **MML:** one video ad with five fruit emoji as bullets, and one boucle blazer page with no brand or product vocabulary.
- **Topo:** a 28-word single-sentence pants ad, and an exclamation mark on the Burrito Bag product page.

## Biggest findings per brand

- **Pact:** the "100% organic" scope, was-prices shown during sitewide sales, and the retired tagline (see claude/09).
- **M.M.LaFleur:** the Bento Box is retired. 47 SKUs are dry-clean only. Returns carry an $8.95 fee by mail. 33 partner products must not be presented as M.M. designs.
- **Edikted:** comp values are almost never charged (191 of 200 SKUs fail the was-price check). Its own "60% OFF EVERYTHING" posts drop the comp-value line and ignore exclusions. 15 products need Prop 65 warnings. The audience has real under-18 reach.
- **Topo Designs:** "handmade in Colorado" and "lifetime warranty" are stale. The correct terms are "printed in Fort Collins" and the M.A.P. Guarantee™. Water resistance applies to named parts only. Collaborations are 39 of 250 feed products (30 of 200 harness SKUs).

## Open items (all brands)

- Confirm the physical addresses: MML and Edikted come from directory listings, and Topo's suite number is unknown.
- Confirm MML's $400 shipping threshold and its serif font name.
- Fetch Topo's guarantee terms. The page was blocked.
- Supply logo files and an image library, and analyze imagery.
- Calibrate the AI judge, which covers about 22% of rules.
- Write wave 2 and 3 golden examples.
- Get legal review of the compliance layers.
