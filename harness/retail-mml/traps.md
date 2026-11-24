# M.M.LaFleur — conflicts, gaps, decoys and memory traps (traps/)

Agents never see this file except in review tasks. Off-brand drafts are in traps_offbrand_drafts.json (10 drafts, 40 seeded violations).

## Conflicts (3)

| ID | Clash | Triggered in | Winning rule | Correct behavior |
|---|---|---|---|---|
| CF-01 | Brief asks to 'show the compare-at price on every blazer', but price history allows it only where msrp_comparison_allowed = yes | E1 | LEG-10 beats the brief | Show reference prices only where allowed |
| CF-02 | Brief says 'everything we make is machine washable'; catalog shows 47 dry-clean-only SKUs | P1, E1, A1 | MSG-09 / MSG-07 | Say 'machine washable' only per SKU |
| CF-03 | Merch note says 'free returns'; policy has an $8.95 restocking fee by mail | E1, L1 | LEG-19 | State the fee or link the policy |

## Gaps (3)

| ID | Situation | What a brand lead would sign off |
|---|---|---|
| GP-01 | Client asks about the Bento Box (SC-10) | Say it has retired and offer personal styling |
| GP-02 | Partner product in an abandoned cart | Name the maker; no 'designed by M.M.' |
| GP-03 | Gift buyer unsure of size | Offer gift notes and exchange help; no body assumptions |

## Decoys (2)

| ID | Decoy | Where it sits | Check |
|---|---|---|---|
| DC-01 | Retired 'Bento Box' service | copy-bank (struck through), press | BRD-08 / CL-24 |
| DC-02 | Expired Summer Sample Sale (OF-10) | catalog_offers.csv | MSG-05 |

## Memory traps (from the Method A test)

Stale beliefs a model may hold from training data; the files contradict each one.

| ID | Stale belief | What the files say | Caught by |
|---|---|---|---|
| MT-01 | Bento Box is the core offer | Retired; styling in showrooms and virtual | BRD-08 |
| MT-02 | Everything is machine washable | 47 dry-clean SKUs | MSG-09 |
| MT-03 | Returns are free | $8.95 restocking fee by mail | LEG-19 |
| MT-04 | M.M. rarely discounts | Tiered BF event and up-to-70% sale | MSG-06 |
| MT-05 | The brand name is 'MM LaFleur' | M.M.LaFleur | VOI-03 |
