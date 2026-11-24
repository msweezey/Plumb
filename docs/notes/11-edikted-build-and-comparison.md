# Edikted — harness build and method comparison

Built 22 Nov 2026 on the Pact path: Method A (assumptions written first, then tested) and Method B (brand book reverse-engineered from evidence), then a full dataset and the four tests. Harness files: harness/retail-edikted/.

## Headline findings

- Method A was strongest here: the brand is loud, emoji-led and sale-driven, as expected.
- The surprise is legal: every sale claim depends on 'comp value' prices that the store almost never charges, 15 products need Prop 65 warnings, and 40 products are tagged for a future drop.
- Edikted's brand layer is the easiest to fingerprint: emoji and caps are required, not just allowed. Its own copy passes 100% (tuning and held-out); every other brand's ads fail it.
- Compliance stays stricter than the brand: Edikted's real 'SHOP 60% OFF EVERYTHING *US only' posts are flagged for missing the comp-value line and for 'everything' with exclusions.

## Method A: assumptions tested

| # | Assumption (conf.) | Verdict | Evidence |
|---|---|---|---|
| A01 | Founded ~2018, Los Angeles (M) | Partly | 2020; LA HQ with Israeli roots |
| A02 | DTC with a few pop-ups (L) | Partly | 11 stores by 2025 plus wholesale (Nordstrom, Tillys tags) |
| A03 | Revenue $100M+ (L) | Unverified | Estimates $42M–$300M |
| A04 | Gen Z trend apparel, Y2K (H) | Confirmed | Tops, knits, low-rise denim, corsets, sets, accessories |
| A05 | Prices $15–70, most $25–45 (M) | Confirmed | Median $26 on sale prices |
| A06 | Heroes: baby tees, low-rise, minis (L) | Partly | Low-rise jeans and going-out tops yes; corsets prominent |
| A07 | Trend-led, affordable, creator-driven (H) | Confirmed | Influencers Monthly tag; creator posts |
| A08 | Loud, slangy, caps, heavy emoji (H) | Confirmed | 100% of ads have emoji and caps words |
| A09 | Frequent big discounts (H) | Confirmed | 60% off everything BF; 70–80% warehouse |
| A10 | Creator and TikTok marketing (H) | Confirmed | E07, E08 |
| A11 | No sustainability claims (M) | Confirmed | None in sampled copy |
| A12 | Black, white, bright pink (L) | Confirmed | #252424 ink, #EC6BAD bubblegum, baby blue |
| A13 | Bold or condensed display type (L) | Partly | Extended/wide display (Obviously Extended, Druk Wide) |
| A14 | Flash photography, creators (M) | Unverified | Imagery not analyzed |
| A15 | Women 16–25 (H) | Confirmed, risk | Teen reach is real; SMS and ads need 18+ handling |
| A16 | Free shipping $50–100 (L) | Confirmed | $80 |
| A17 | SMS heavy (M) | Unverified | Not observed directly |
| A18 | Risks: urgency, comp value, creators, SMS (M) | Confirmed, wider | Plus Prop 65 warnings and 'everything' with exclusions |
| A19 | Uses 'comp value' (L) | Confirmed | '*Based on comp value' on every sale ad |
| A20 | Sizes XXS–XL (L) | Partly | XS–XL; OS accessories |

## Method B: the reverse-engineered brand book (summary)

- Essence: the trend from your feed, now, at a price that doesn't sting.
- Voice: loud, insider, hype, playful; emoji and caps required in ads (min 1 each), #EDIKTED on every post.
- Mechanics measured on tuning copy: ad grade median 7.7; 100% of ads have emoji; CTA always 'Shop now'.
- Visual: ink #252424 and bubblegum #EC6BAD with pastel panels; extended and wide display type.
- Commerce: weekly drops, 60% off BF (comp value), warehouse 70–80%, $80 free shipping, APP10.

## Where the methods differ

Method A scored: 12 confirmed, 5 partly, 0 wrong or outdated, 3 unverified, out of 20. Method B supplied every number the rules need (emoji and caps ranges, reading level, hex values, fonts, thresholds); Method A supplied none of them reliably. The wrong or outdated assumptions became memory traps in traps.md.

## Tests

## Results

| Test | Result | Pact target |
|---|---|---|
| Fidelity, tuning (brand layer) | 47/47 = 100% | ~90% |
| Fidelity, held-out (brand layer) | 19/19 = 100% | ~90% |
| Discrimination: Pact ads + posts rejected by Edikted rules | 36/36 = 100% | ≥85% |
| Discrimination: M.M.LaFleur ads + posts rejected by Edikted rules | 23/23 = 100% | ≥85% |
| Discrimination: Topo Designs ads + posts rejected by Edikted rules | 30/30 = 100% | ≥85% |
