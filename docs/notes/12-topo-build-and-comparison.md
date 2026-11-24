# Topo Designs — harness build and method comparison

Built 22 Nov 2026 on the Pact path: Method A (assumptions written first, then tested) and Method B (brand book reverse-engineered from evidence), then a full dataset and the four tests. Harness files: harness/retail-topo/.

## Headline findings

- Method A's picture of Topo was a decade old: 'handmade in Colorado' and 'lifetime warranty' are both wrong today, and the type is a condensed serif, not a retro sans.
- Topo is two voices: ads are calm, Title Case and emoji-free; Instagram is chatty with 1–3 emoji. The rules split by channel.
- Collaborations are frequent (39 of 250 feed products), so partner credit and 'printed in Colorado is not Made in USA' are the main traps.
- Rules pass 98% of tuning copy and 94% held-out; Pact and MML ads fail Topo's brand layer 32/36 and 22/23.

## Method A: assumptions tested

| # | Assumption (conf.) | Verdict | Evidence |
|---|---|---|---|
| A01 | Founded ~2008, Denver (M) | Confirmed | 2008, Fort Collins start, Denver HQ |
| A02 | DTC plus wholesale, a few stores (M) | Confirmed | REI, Nordstrom history; Denver stores and new HQ storefront |
| A03 | Revenue $20–40M (L) | Unverified | Not public |
| A04 | Packs, bags, apparel, accessories (H) | Confirmed, wider | Plus drinkware and many collabs |
| A05 | Packs $80–200; apparel $60–250 (M) | Confirmed | Median $69; roller bag $399 |
| A06 | Heroes Klettersack and Rover Pack (H) | Partly | Rover Pack yes; Mountain Cross Bag and Global line lead ads |
| A07 | Retro, design-forward, town and trail (H) | Confirmed | 'Made for anywhere on your map' |
| A08 | Friendly, playful, nostalgic, short (M) | Confirmed | 'our friends', light emoji on social |
| A09 | Some made in Colorado/USA (M) | **Mostly outdated** | Only printing/finishing in Colorado now; products imported |
| A10 | Recycled materials (L) | Confirmed | Recycled nylon on many bags |
| A11 | Lifetime warranty (L) | **Wrong name** | 'M.A.P. Guarantee™', not a lifetime warranty |
| A12 | Bold retro colors (L) | Partly | Site chrome is bone, charcoal and red; product colorways carry the retro palette |
| A13 | Retro or rounded sans (L) | **Wrong** | Condensed serif headings (New Spirit) with IBM Plex Sans |
| A14 | Outdoors and town imagery (M) | Unverified | Imagery not analyzed |
| A15 | Outdoorsy urbanites 25–45 (M) | Confirmed | Commuter and travel collections |
| A16 | Frequent collaborations (M) | Confirmed | 39 of 250 feed products are collabs |
| A17 | Moderate seasonal sales (L) | Confirmed | Up to 50% off select styles |
| A18 | Free shipping $50–100 (L) | Confirmed | $100+ |
| A19 | Risks: Made in USA, recycled, warranty, waterproof (M) | Confirmed | All four show up in catalog traps |
| A20 | Instagram primary (L) | Partly | IG plus heavy Meta ads (226) |

## Method B: the reverse-engineered brand book (summary)

- Essence: outdoor gear without the gatekeeping, made for anywhere on your map.
- Voice: friendly, easygoing, crafted, playful; ads emoji-free and Title Case, social 1–3 emoji and no hashtags.
- Mechanics measured on tuning copy: ad grade median 6.8; 0 emoji in ads; 89% of IG posts use emoji; CTA 'Shop now'.
- Visual: bone #F5F4EF and charcoal #241F20 with Topo Red #E31B23; New Spirit Condensed headings, IBM Plex Sans body.
- Commerce: up to 50% off select styles, Topo Crew 10%, free U.S. shipping $100+, M.A.P. Guarantee™, many collabs.

## Where the methods differ

Method A scored: 12 confirmed, 3 partly, 3 wrong or outdated, 2 unverified, out of 20. Method B supplied every number the rules need (emoji and caps ranges, reading level, hex values, fonts, thresholds); Method A supplied none of them reliably. The wrong or outdated assumptions became memory traps in traps.md.

## Tests

## Results

| Test | Result | Pact target |
|---|---|---|
| Fidelity, tuning (brand layer) | 47/48 = 98% | ~90% |
| Fidelity, held-out (brand layer) | 17/18 = 94% | ~90% |
| Discrimination: Pact ads + posts rejected by Topo Designs rules | 32/36 = 89% | ≥85% |
| Discrimination: M.M.LaFleur ads + posts rejected by Topo Designs rules | 22/23 = 96% | ≥85% |
| Discrimination: Edikted ads + posts rejected by Topo Designs rules | 29/30 = 97% | ≥85% |
