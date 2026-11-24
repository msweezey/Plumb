# Retail brand harnesses

Context harnesses for testing AI marketing tools against four real US DTC apparel brands, one per quadrant of expression × positioning. Each harness was built from public material only (site, product feed, Meta ads, Instagram, press). When a brand partners, its own guidelines replace the public build.

| Folder | Brand | Quadrant | Personas (shared set) |
|---|---|---|---|
| `retail-pact/` | Pact | restrained × value | MIL, GX |
| `retail-mml/` | M.M.LaFleur | restrained × premium | GX, MIL |
| `retail-edikted/` | Edikted | expressive × value | GZ, MIL |
| `retail-topo/` | Topo Designs | expressive × premium | MIL, GX |

Results and method: `docs/notes/09`–`13` (`13-retail-four-brand-summary.md` has the outcome table and the 4×4 discrimination matrix).

## What is in each brand folder

| File | What it is |
|---|---|
| `harness.yaml` | Manifest |
| `brief.md`, `guidelines.md`, `rules.json`, `rubric.md` | Brand book: 181 rules in a brand layer (tuned to the brand's real copy) and a compliance layer (stricter than the brand's own copy) |
| `brand_tokens.json` | Colors by hex and fonts, pulled from the live site |
| `catalog_*.csv` | 200 SKUs with trap flags, 10 offers, 12-month price history, 300 reviews |
| `audience_*` | The shared 250-person contact spine plus brand columns; 5 segments |
| `library_claims.md`, `library_copy-bank.md` | 25 claims, 50+ copy lines and boilerplates |
| `history_golden_wave1.md` | 6 golden examples (P1, E1, A1 × 2) |
| `traps.md`, `traps_offbrand_drafts.json` | Conflicts, gaps, decoys, memory traps; 10 drafts with seeded violations |
| `tasks_wave1.md`, `fixtures_*.json` | Task briefs and fixtures |
| `checks.py` | Automatic checker for that brand |
| `realcopy_corpus.json`, `test_report_fidelity.md` | Real brand copy (tuning and held-out splits) and the test results |
| `evidence_log.md`, `assumptions_method-a.md` | Evidence pulled, and the assumptions written before research |

`shared/` holds the four personas, the contact spine, the shared check engine (`checks_engine.py`) and the per-brand settings (`brand_configs.py`).

## Rebuilding

`build/` holds the pipeline and the cleaned evidence it reads (`build/evidence/<brand>/`).

```
python3 harness/build/corpus_build.py                         # real-copy corpora (tuning/held-out split)
python3 harness/build/gen_docs_brand.py mml edikted topo      # data, rules, docs, tests → harness/retail-<brand>/
python3 harness/build/runtests.py                             # fidelity + 4×4 discrimination
```

Builds are deterministic: rerunning reproduces the committed files byte for byte. `build/pact/` holds the original Pact pilot scripts as they were run; they use absolute paths from the build workspace and are kept for reference.

Contacts and reviews are synthetic (`example.com` addresses). Offers and price history are synthetic on the shared structure. Product data comes from each brand's public Shopify product feed.
