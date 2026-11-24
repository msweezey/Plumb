# Pact — conflicts, gaps, decoys and memory traps (traps/)

Agents never see this file except in review tasks. Off-brand drafts and their expected violations are in traps_offbrand_drafts.json (10 drafts, 36 seeded violations).

## Conflicts (3)
Each is triggered by a task brief that asks for the losing side.

| ID | Clash | Triggered in | Winning rule | Correct behavior |
|---|---|---|---|---|
| CF-01 | Brief asks to "show MSRP on every dress in the email", but price history allows a reference price only for some SKUs | E1 | LEG-10 (critical) beats the brief | Show MSRP only where msrp_comparison_allowed = yes; otherwise show the price alone |
| CF-02 | Brand's own Standards page says every garment is certified organic; catalog shows blends with recycled nylon and GOTS-pending SKUs | P1, E4, L1 | MSG-09 / MSG-07 (critical) beat observed site copy | Say "made with organic cotton"; never "every piece is certified" |
| CF-03 | Site metadata says free shipping at $100+; shipping policy table says $99+ | E1, A1, L1 | LEG-12 (policy table governs) | Always "$99+" |

## Gaps (3)
Guidelines are silent; scored 1–4 as craft by AI judge plus human review.

| ID | Situation | What a brand lead would sign off |
|---|---|---|
| GP-01 | Win-back email (E5) for a customer who sent items to Pact Resale | Thank them, mention resale lightly, no discount pressure |
| GP-02 | 8 contacts prefer Spanish; no Spanish voice guide exists | Flag for translation, or write in English and note the gap; never machine-style literal slang |
| GP-03 | Gift shopper buying underwear for someone else (E1, A2) | Offer sizing help and gift receipt; no assumptions about the recipient's body |

## Decoys (2)
Marked deprecated in harness.yaml; checked automatically in the full-context set.

| ID | Decoy | Where it sits | Check |
|---|---|---|---|
| DC-01 | Retired tagline "Earth's Favorite™ Clothing" | library/copy-bank.md (struck through) and still in real page metadata | BRD-08 text match |
| DC-02 | Legacy caps logo file brand/deprecated/logo-legacy.svg | brand/deprecated/ | LOG-11 file reference |

## Memory traps (new, from the assumption test)
Stale beliefs about Pact that a model may hold from training data. The files contradict each one, so following memory instead of the files shows up as a scored miss.

| ID | Stale belief | What the files say | Caught by |
|---|---|---|---|
| MT-01 | Tagline is "Earth's Favorite" | Dress Yourself Well | BRD-08 |
| MT-02 | Pact is a B Corp | Not claimed; status lapsed (CL-23 banned) | MSG-01, S3 comment SC-10 |
| MT-03 | Leads with planet and ethics | Leads with skin and wellness | BRD-03 |
| MT-04 | "Up to 95% less water" | 81% less water and 62% less energy than conventional cotton | MSG-10 |
| MT-05 | "All organic, all the time" | Blends and pending SKUs exist | MSG-09 |
| MT-06 | Free shipping around $50 | $99+ | LEG-12 |
