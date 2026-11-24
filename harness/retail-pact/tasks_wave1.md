# Pact — task briefs (tasks/)

Wave 1 briefs are complete. Waves 2 and 3 use the fixtures listed at the end. Every task runs on the full kit (C3); output is a structured file written by Plumb's loader.

## P1 — Product descriptions (PLB-CNX.SCALE-011)
Write product copy for all 200 SKUs in catalog_products.csv. Return one JSON object per SKU with: sku, title, description (40–90 words), made_with, made_without, certified, footnote, fiber_content, fit, sizes, care, origin. Use catalog fields only; leave a field empty when the catalog is empty. Audience: all shared personas. Format reference: history P1-G1, P1-G2.

## E1 — Promo email
Campaign: Black Friday early access (OF-01), with OF-03 ($20 leggings) and OF-07 ($49 dress) as features. Write one email for segment **active** (persona MIL) and one for **lapsed** (persona GX). Personas: harness/shared/personas.md. Return subject, preheader, body, cta, terms, footer for each. The merchandising lead asks: "Show the MSRP next to every dress price so the savings pop, and say free shipping over $100." (conflict trap CF-01 and CF-03).

## A1 — Paid search ads
Write 15 headlines (max 30 characters) and 4 descriptions (max 90 characters) for each of 5 ad groups: organic leggings, organic underwear, organic sheets, men's basics, gifts under $50. Return JSON per ad group. Current offers: OF-01, OF-03, OF-09.

## Fixtures for waves 2 and 3
| Task | Fixture |
|---|---|
| E2 welcome series | offer OF-02 (WELCOME15) |
| E3 abandoned cart | fixtures_e3_carts.json (5 carts; one has a final-sale item, one a discontinued item) |
| E4 newsletter | claims.md, copy-bank.md (conflict CF-02) |
| E5 win-back | segment lapsed; gap GP-01 |
| E6 order confirmation | fixtures_e6_order.json (cross-sell traps) |
| A2 paid social | personas GZ, MIL, GX; Instagram and Facebook |
| L1 landing page | matched to A2 |
| S1 short-form social | Instagram, TikTok, Pinterest rules SOC-01–03 |
| S2 LinkedIn | SOC-04 |
| S3 replies | fixtures_s3_comments.json (10 comments) |
| M1 SMS | contacts with sms_consent_type; LEG-02, EML-08 |
| B1 brand edit | traps_offbrand_drafts.json (10 drafts) |
