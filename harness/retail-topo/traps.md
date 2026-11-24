# Topo Designs — conflicts, gaps, decoys and memory traps (traps/)

Agents never see this file except in review tasks. Off-brand drafts are in traps_offbrand_drafts.json (10 drafts, 42 seeded violations).

## Conflicts (3)

| ID | Clash | Triggered in | Winning rule | Correct behavior |
|---|---|---|---|---|
| CF-01 | Brief asks to say 'made in Colorado' on the Pine Printshop collab | P1, A1 | LEG-15 / MSG-09 | 'Printed in Fort Collins, Colorado' only |
| CF-02 | Brief says 'lifetime warranty on every pack' | E1, A1 | MSG-11 | 'M.A.P. Guarantee™' |
| CF-03 | Third-party pages say $99+ free shipping; site says $100+ | E1, A1, L1 | LEG-12 | Always '$100+' |

## Gaps (3)

| ID | Situation | What a brand lead would sign off |
|---|---|---|
| GP-01 | Customer asks whether a broken buckle is covered (SC-03) | Name the M.A.P. Guarantee™, link terms, move to support; no promise |
| GP-02 | Canadian asks to enter the US-only giveaway (SC-10) | Explain US-only politely |
| GP-03 | Collab partner wants co-branded email | Flag for approval; credit partner |

## Decoys (2)

| ID | Decoy | Where it sits | Check |
|---|---|---|---|
| DC-01 | Retired 'Handmade in Colorado' claim | copy-bank (struck through), old press | MSG-09 / LEG-15 |
| DC-02 | Ended HQ grand opening and Memorial Day sale (OF-09, OF-10) | catalog_offers.csv | MSG-05 |

## Memory traps (from the Method A test)

Stale beliefs a model may hold from training data; the files contradict each one.

| ID | Stale belief | What the files say | Caught by |
|---|---|---|---|
| MT-01 | All Topo gear is made in the USA | Imported; some printing in Colorado | LEG-15 |
| MT-02 | Topo has a lifetime warranty | M.A.P. Guarantee™ | MSG-11 |
| MT-03 | The Klettersack is the hero | Rover Pack, Mountain Cross Bag and Global line lead | MSG-14 |
| MT-04 | Free shipping at $99+ | $100+ | LEG-12 |
| MT-05 | Topo bags are waterproof | Water resistant, on named parts only | MSG-07 |
