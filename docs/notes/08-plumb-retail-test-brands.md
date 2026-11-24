# Plumb — Retail Test Brands (pointer)

The live, editable version is the master:
**https://claude.ai/artifact/RaHJ82w9qPE42o1ZcQf74x** ("Plumb — Retail Test Brands")

Decided 22 Nov 2026: retail uses real mid-sized US DTC apparel brands, built from public material first; partner-supplied guidelines replace the public build later. All brands run under their real names only (no renamed runs). No well-known control brand for now (Cotopaxi was considered and dropped).

| Quadrant | Brand | Primary personas (shared set) | Harness |
|---|---|---|---|
| Restrained × Value | Pact | MIL (primary), GX | harness/retail-pact/ (notes/09) |
| Restrained × Premium | M.M.LaFleur | GX (primary), MIL | harness/retail-mml/ (notes/10) |
| Expressive × Value | Edikted | GZ (primary), MIL | harness/retail-edikted/ (notes/11) |
| Expressive × Premium | Topo Designs | MIL (primary), GX | harness/retail-topo/ (notes/12) |

Personas are shared, not per brand (decided 22 Nov 2026): GZ (Gen Z, 18–29), MIL (Millennial, 30–45), GX (Gen X, 46–61), BB (Boomer, 62–80), defined in harness/shared/personas.md and tagged on every contact in harness/shared/contacts_spine_v2.csv. Each brand brief names a primary and secondary persona.

Status 22 Nov 2026: all four harnesses built the Pact way (Method A assumptions, evidence, Method B brand book, full dataset, calibration on real copy) and tested the same way. Every brand meets the Pact outcome targets: fidelity on tuning and held-out copy at 94% or higher, at least 89% of each other brand's copy rejected, goldens 6/6, and all seeded traps caught. Summary and 4×4 discrimination matrix: notes/13-retail-four-brand-summary.md. Shared check engine and per-brand configs: harness/shared/checks_engine.py and harness/shared/brand_configs.py.

Catalogs for MML, Edikted and Topo are built from each brand's real Shopify product feed (200 of 250 products), with store tags turned into trap columns. Offers, price history, reviews and contacts are synthetic on the shared structure.

Selection check: US brand-name search volume (SE Ranking, Nov 2026) plus a Claude recall probe. GPT/Gemini recognition check still to run.
Replaces the earlier fictional briefs (Plainfold, Aldermere, LOUDLOT, Ridgeborn).
