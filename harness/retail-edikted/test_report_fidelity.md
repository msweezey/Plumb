# Edikted — fidelity and discrimination tests (test_report_fidelity.md)

Run 22 Nov 2026 with checks.py (shared Plumb engine + Edikted config). Real copy was split before tuning: **T** (tuning) and **H** (held out). Rules were tuned on T only.

## Results

| Test | Result | Pact target |
|---|---|---|
| Fidelity, tuning (brand layer) | 47/47 = 100% | ~90% |
| Fidelity, held-out (brand layer) | 19/19 = 100% | ~90% |
| Discrimination: Pact ads + posts rejected by Edikted rules | 36/36 = 100% | ≥85% |
| Discrimination: M.M.LaFleur ads + posts rejected by Edikted rules | 23/23 = 100% | ≥85% |
| Discrimination: Topo Designs ads + posts rejected by Edikted rules | 30/30 = 100% | ≥85% |
| Goldens pass all automatic rules | 6/6 | 6/6 |
| Seeded trap violations detected | 42/42 | all |

## Brand-layer misses on the brand's own copy

These are the brand's own inconsistencies (kept as findings, not tuned away):


## Compliance findings on real copy

Compliance rules flagged 15 tuning and 5 held-out assets. This is expected: compliance is stricter than the brand's own practice.

## Calibration notes

- One engine (checks.py) for all four brands; brand differences live in config only (emoji and caps ranges, vocabulary, off-voice words, category boundaries, reading level, thresholds).
- Held-out results were inspected after the first tuning round. Any later change was justified by a tuning-split asset, and is noted in the cross-brand summary.
