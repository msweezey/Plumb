# M.M.LaFleur — fidelity and discrimination tests (test_report_fidelity.md)

Run 22 Nov 2026 with checks.py (shared Plumb engine + M.M.LaFleur config). Real copy was split before tuning: **T** (tuning) and **H** (held out). Rules were tuned on T only.

## Results

| Test | Result | Pact target |
|---|---|---|
| Fidelity, tuning (brand layer) | 41/42 = 98% | ~90% |
| Fidelity, held-out (brand layer) | 16/17 = 94% | ~90% |
| Discrimination: Pact ads + posts rejected by M.M.LaFleur rules | 32/36 = 89% | ≥85% |
| Discrimination: Edikted ads + posts rejected by M.M.LaFleur rules | 30/30 = 100% | ≥85% |
| Discrimination: Topo Designs ads + posts rejected by M.M.LaFleur rules | 28/30 = 93% | ≥85% |
| Goldens pass all automatic rules | 6/6 | 6/6 |
| Seeded trap violations detected | 40/40 | all |

## Brand-layer misses on the brand's own copy

These are the brand's own inconsistencies (kept as findings, not tuned away):

- T · ad: VOI-10 — “ | Which one are you choosing, Player 1 or Player 2?  M.M. pieces seen in this v”
- H · pdp: VOI-02 — “Evangeline "The Duchess" Blazer - Boucle :: Burgundy / Ivory | Our take on the i”

## Compliance findings on real copy

Compliance rules flagged 5 tuning and 1 held-out assets. This is expected: compliance is stricter than the brand's own practice.

## Calibration notes

- One engine (checks.py) for all four brands; brand differences live in config only (emoji and caps ranges, vocabulary, off-voice words, category boundaries, reading level, thresholds).
- Held-out results were inspected after the first tuning round. Any later change was justified by a tuning-split asset, and is noted in the cross-brand summary.
