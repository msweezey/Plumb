# M.M.LaFleur — harness build and method comparison

Built 22 Nov 2026 on the Pact path: Method A (assumptions written first, then tested) and Method B (brand book reverse-engineered from evidence), then a full dataset and the four tests. Harness files: harness/retail-mml/.

## Headline findings

- Method A got the positioning right and the commercial mechanics wrong: the Bento Box is retired, and Black Friday runs on 10–40% tiers plus an up-to-70% sale section.
- Voice is stricter than assumed: no exclamation marks anywhere, no hashtags, and emoji only as list bullets in two ads.
- The most testable risks come from the product feed, not the copy: 47 dry-clean-only SKUs, 33 partner products, and tiered final-sale rules.
- Rules tuned on real copy pass 98% of tuning assets and 94% of held-out assets; other brands' ads fail MML's brand layer 32/36 (Pact), 30/30 (Edikted) and 28/30 (Topo).

## Method A: assumptions tested

| # | Assumption (conf.) | Verdict | Evidence |
|---|---|---|---|
| A01 | Founded ~2013 in New York by Sarah LaFleur (H) | Confirmed | E08 |
| A02 | DTC-led with showrooms (M) | Confirmed | E01, E08: showrooms, 'Personal styling, in person' ads |
| A03 | Revenue $20–100M; 100–300 staff (L) | Unverified | Estimates range $16.5M–$70M+; staff 78–500 by source |
| A04 | Workwear: dresses, jackets, trousers, knits (H) | Confirmed, wider | Plus partner goods: readers, candles, stationery, luggage |
| A05 | Tops $100–200, dresses $200–300, jackets $300+ (M) | Confirmed | Median $206; blazers $296–$649 |
| A06 | Hero washable dresses; names are first names (M) | Partly | First names yes, plus quoted nicknames and fabric; heroes include Moreland blazer |
| A07 | Bento box styling (H) | **Outdated** | Bento discontinued; styling now in showrooms and virtual |
| A08 | Polished, versatile, easy for busy professionals (H) | Confirmed | 'Live with Purpose, Dress with Ease'; 'Power Casual' |
| A09 | Confident, smart, witty, editorial (M) | Confirmed | Samantha vignettes, quote posts, persona hooks |
| A10 | Words: effortless, polished, versatile, machine washable (M) | Partly | 'polished', 'machine washable', 'suiting', 'wardrobe' yes; 'versatile' rare |
| A11 | Low emoji, few exclamations (M) | Confirmed, stricter | Zero '!' in ads, social and PDP; emoji only as bullets |
| A12 | Sizes 0–22 (M) | Partly | 00–20 on suiting and dresses; XS–XXL on knits |
| A13 | Fewer sales, sample sales (M) | **Wrong** | Black Friday Event with 10–40% tiers plus up to 70% off sale section |
| A14 | Free shipping and returns with a threshold (L) | Partly | $400 shipping threshold (inferred); returns carry an $8.95 fee |
| A15 | Black/white, minimal, deep accent (L) | Confirmed | Black, white, espresso #251001, ivory, rust and sale red |
| A16 | Serif headlines, clean sans body (L) | Confirmed | Geist body; serif variable for headlines |
| A17 | Real professional women, city settings (M) | Unverified | Imagery not analyzed in this pass |
| A18 | Women 30–55, managers to executives (H) | Confirmed | 'Your Executive Wardrobe', 'the woman who leads the room' |
| A19 | Email, IG, Meta, podcasts, LinkedIn (M) | Partly | Meta and IG confirmed; others not checked |
| A20 | Fabric performance and 'made in' claims (M) | Confirmed | Washable, wrinkle-resistant, stretch tags; origin lines in copy |
| A21 | Sustainability secondary (L) | Confirmed | Only fabric names like 'Eco Drape', 'Recycled WonderTex'; no program claims |
| A22 | Customer quotes and press (L) | Unverified | Not in sampled ads |
| A23 | Risk: fabric claims, made-in, reference pricing (M) | Confirmed, wider | Plus partner goods sold as M.M., final-sale rules and restocking fee |

## Method B: the reverse-engineered brand book (summary)

- Essence: Power Casual for women who lead; purpose is fewer decisions and more ease.
- Voice: polished, witty, practical, assured; zero exclamation marks; editorial social devices (quotes, Samantha, 'Some decisions are easy:').
- Mechanics measured on tuning copy: ad reading grade median 5.4 (max 6.9), PDP grade up to 13; 0 hashtags; CTAs 'Shop now'/'Learn more'.
- Visual: black/white/ivory with espresso #251001; Geist sans plus a house serif.
- Commerce: BF tiers 10–40%, sale up to 70%, $400 shipping threshold (inferred), 21-day returns with an $8.95 fee.

## Where the methods differ

Method A scored: 13 confirmed, 5 partly, 2 wrong or outdated, 3 unverified, out of 23. Method B supplied every number the rules need (emoji and caps ranges, reading level, hex values, fonts, thresholds); Method A supplied none of them reliably. The wrong or outdated assumptions became memory traps in traps.md.

## Tests

## Results

| Test | Result | Pact target |
|---|---|---|
| Fidelity, tuning (brand layer) | 41/42 = 98% | ~90% |
| Fidelity, held-out (brand layer) | 16/17 = 94% | ~90% |
| Discrimination: Pact ads + posts rejected by M.M.LaFleur rules | 32/36 = 89% | ≥85% |
| Discrimination: Edikted ads + posts rejected by M.M.LaFleur rules | 30/30 = 100% | ≥85% |
| Discrimination: Topo Designs ads + posts rejected by M.M.LaFleur rules | 28/30 = 93% | ≥85% |
