# Pact — rule calibration against real copy (test report)

Run 22 Nov 2026. Goal: make the brand rules describe how Pact actually writes, while compliance rules stay stricter than Pact's own copy.

## Method
- **Corpus:** 49 real Pact assets: 29 live Meta ads (two pages of the ad library), 7 Instagram captions, 6 site sections, 3 page-metadata lines, 2 product descriptions and 2 "Wellness ingredients" modules (realcopy_corpus.json).
- **Split:** tuning set (39 assets) used to adjust rules; held-out set (10 assets: 7 ads from the second ad-library page, one product page) never used for tuning.
- **Two layers:** every rule is tagged **brand** (118 rules: voice, style, format) or **compliance** (63 rules: legal, claims, accessibility, safety). A brand-layer failure on Pact's real copy means the rule is wrong or Pact is inconsistent. A compliance-layer failure is a real risk in Pact's copy, which is expected.
- **Four tests:** (1) fidelity on the tuning set, (2) fidelity on the held-out set, (3) discrimination: the same brand rules on other brands' live ads (Edikted, M.M.LaFleur), (4) regression: golden examples must pass and seeded trap violations must be caught.
- One shared check engine (checks.py) runs all four, so tests and grading can't drift apart.

## Results

| Test | Before calibration | After |
|---|---|---|
| Brand rules pass Pact tuning copy | 33 of 39 (85%) | **36 of 39 (92%)** |
| Brand rules pass Pact held-out copy | 8 of 10 (80%) | **9 of 10 (90%)** |
| Brand rules reject Edikted ads | 17 of 20 | **19 of 20** |
| Brand rules reject M.M.LaFleur ads | 6 of 15 | **13 of 15** |
| Golden examples pass | 6 of 6 | 6 of 6 |
| Seeded trap violations caught | 36 of 36 | 36 of 36 |

The remaining brand misses are real inconsistencies in Pact's own material, not rule errors: the retired "Earth's Favorite™" line in two pages' metadata, one ad that writes "PACT", and one SEO paragraph that mixes comma styles.

## Rule changes

| Rule | Before | After | Evidence |
|---|---|---|---|
| VOI-05 serial comma | Never use | Optional; consistent within an asset | 13 lists with, 9 without |
| VOI-13 reading level | Grade 8 max, all copy | Grade 10 max, copy of 3+ sentences; social judged | Ads median 7.9, p90 8.9 |
| VOI-14 sentence length | 15 words | 18 words; spaced em dash and emoji count as breaks | Ads median 10 |
| VOI-16 "made without" | Exact 3-item phrase | Any subset of the 3 approved items, any order; "free from" and "no" count | 10 lists, 5 orderings |
| VOI-12 exclamations | PDP, web, email | Adds ads: none | 0 of 29 ads |
| VOI-02 brand vocabulary | Per line | Per asset; sale-only messages exempt | In 29 of 29 Pact ads; 3 of 15 M.M.LaFleur; 1 of 20 Edikted |
| SOC-01 hashtags | 3–5 | 0–3, #organiccotton when any are used | 0–2 on 7 posts |
| DR-03 superlatives | Any "best" | Product superlatives only; "best deals" allowed | "our best deals" in ads |
| DR-04 ad length | Primary text 125 visible | First sentence within 125; CTA "Shop now" | 8 ads exceed 125 overall |
| DR-05 headline case | Title Case | Title Case or sentence case; never all caps | 23 of 29 Title Case |
| MSG-06 discounts | Any "% off" needs "up to" | Must match offers.csv; only the variable sitewide 40% needs "up to" | False hit on "15% off your first order" |
| MSG-16 (new) | — | Never imply no dyes ("no PFAS or dyes") | Held-out ad |
| MSG-17 (new) | — | No comparative or superiority claims ("better than denim", "the leading brand") | Held-out product page, site metadata |

## Compliance findings in Pact's own copy (14)
These stay as rules; they are the risks Plumb exists to catch.

| Rule | Finding | Count |
|---|---|---|
| LEG-18 | Unqualified "sustainable" (bedding ad, category page, site metadata) | 3 |
| MSG-11 | "Carbon neutral" without saying it's through offsets | 2 |
| MSG-09 | Absolute organic claims ("every garment we make is certified organic", "every piece is GOTS-certified") | 2 |
| MSG-17 | Superiority or comparative claims ("the leading brand", "better than denim") | 2 |
| DR-03 | Product superlative on Instagram ("the softest, coziest…") | 1 |
| VOI-01 | "Non-Toxic Clothing" | 1 |
| MSG-10 | Water saving claim with no comparison | 1 |
| LEG-12 | Free shipping stated as $100+ (policy is $99+) | 1 |
| MSG-16 | "no PFAS or dyes" implies undyed clothing | 1 |

## Limits
- Automated brand checks catch mechanics and vocabulary, not voice. 2 of 15 M.M.LaFleur ads still pass them; the AI judge on the soft voice rules (BRD, VOI-17 to VOI-25) has to do the rest, and it isn't calibrated yet.
- The corpus has no email, SMS or search-ad copy (Pact's email archive was unreachable) and only two product pages, so those channels' rules are calibrated less.
- 49 assets is enough to fix obvious errors, not to set tight thresholds. Re-run when the partner supplies its own copy.
- Data cost for these tests: about $0.03.
