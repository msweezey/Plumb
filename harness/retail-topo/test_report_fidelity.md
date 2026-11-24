# Topo Designs — fidelity and discrimination tests (test_report_fidelity.md)

Run 22 Nov 2026 with checks.py (shared Plumb engine + Topo Designs config). Real copy was split before tuning: **T** (tuning) and **H** (held out). Rules were tuned on T only.

## Results

| Test | Result | Pact target |
|---|---|---|
| Fidelity, tuning (brand layer) | 47/48 = 98% | ~90% |
| Fidelity, held-out (brand layer) | 17/18 = 94% | ~90% |
| Discrimination: Pact ads + posts rejected by Topo Designs rules | 32/36 = 89% | ≥85% |
| Discrimination: M.M.LaFleur ads + posts rejected by Topo Designs rules | 22/23 = 96% | ≥85% |
| Discrimination: Edikted ads + posts rejected by Topo Designs rules | 29/30 = 97% | ≥85% |
| Goldens pass all automatic rules | 6/6 | 6/6 |
| Seeded trap violations detected | 42/42 | all |

## Brand-layer misses on the brand's own copy

These are the brand's own inconsistencies (kept as findings, not tuned away):

- T · ad: VOI-14 — “Shop Men's Pants | A daily staple, our pants give you a broken-in-feel from the ”
- H · pdp: VOI-12 — “Burrito Bag | The Burrito Bag, made from 100% recycled nylon, is here to make yo”

## Compliance findings on real copy

Compliance rules flagged 4 tuning and 0 held-out assets. This is expected: compliance is stricter than the brand's own practice.

## Calibration notes

- One engine (checks.py) for all four brands; brand differences live in config only (emoji and caps ranges, vocabulary, off-voice words, category boundaries, reading level, thresholds).
- Held-out results were inspected after the first tuning round. Any later change was justified by a tuning-split asset, and is noted in the cross-brand summary.
