# Edikted — golden examples, wave 1 (history/)

Two on-brand examples per wave 1 task (P1, E1, A1). Each passes every automatic rule (validated by checks.py); the AI judge uses them as 4-anchors.

## P1 — product descriptions

### P1-G1 · EDT-001 Nogi Overlap V Neck Long Sleeve Top (BLACK)
Trap covered: Fibers listed without percentages; comp value not shown as a was-price.
```json
{
 "sku": "EDT-001",
 "title": "Nogi Overlap V Neck Long Sleeve Top",
 "description": "Long sleeve top\nOverlap V neckline\nSlim fit\nSoft stretch jersey, made for layering under every fit\nCotton, Spandex\nModel wears size S · Model height is 5’7\nItem care: Machine wash at maximum 30ºC, do not bleach, tumble dry low, iron at a maximum of 110ºC, do not dry clean",
 "fiber_content": "Cotton, Spandex",
 "model_info": "Model wears size S · Model height is 5’7",
 "sizes": "XS, S, M, L, XL",
 "origin": "Imported",
 "warnings": ""
}
```

### P1-G2 · EDA-011 Rounded Textured Brooch (GOLD)
Trap covered: Prop 65 line required; no material in catalog, so none is written.
```json
{
 "sku": "EDA-011",
 "title": "Rounded Textured Brooch",
 "description": "Brooch\nRounded textured design\nGold-tone finish\nPin it on a blazer, bag or beanie\nItem care: Avoid direct contact with perfume, soap or creams\nWARNING: This product can expose you to chemicals known to the State of California to cause cancer or reproductive harm. Prop 65 info at P65Warnings.ca.gov.",
 "fiber_content": "",
 "model_info": "",
 "sizes": "OS",
 "origin": "Imported",
 "warnings": "Prop 65"
}
```

## E1 — promo email (Black Friday (OF-01), 60% off with comp-value disclosure)

### E1-G1 · Segment: active (persona GZ)
```json
{
 "segment": "active",
 "subject": "BLACK FRIDAY IS LIVE 🖤 60% OFF your faves*",
 "preheader": "The biggest sale of the year is here. Check out your cart RN.",
 "body": "Hey babe 🖤\n\nBLACK FRIDAY IS LIVE. Take 60% OFF your faves* and shop the fits you've been saving 💥\n\nThe Cecilya Bandage Mini Dress for GNO, cozy knits for the holidays, new sets for every plan.\n\nFree standard shipping on orders above $80. Thank us later 💋",
 "cta": "Shop the sale",
 "terms": "*Based on comp value. 60% off all items Nov 22-30, 2026, ending 11:59 pm PT, except warehouse sale items and gift cards. US only. While supplies last.",
 "footer": "Edikted · 1327 Willow St, Los Angeles, CA 90013 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Edikted"
}
```

### E1-G2 · Segment: lapsed (persona MIL)
```json
{
 "segment": "lapsed",
 "subject": "It's been a minute. 60% OFF your faves*",
 "preheader": "Our biggest sale of the year is live, with new fits for every plan.",
 "body": "Hi {first_name|babe} ✨\n\nWe saved you a spot. Black Friday is live with 60% OFF your faves*.\n\nNew knits, going out tops and matching sets just dropped. Grab your fits before they're gone.\n\nNew to the app? Use APP10 for 10% off your first app order.",
 "cta": "Shop new fits",
 "terms": "*Based on comp value. 60% off all items Nov 22-30, 2026, ending 11:59 pm PT, except warehouse sale items and gift cards. US only. While supplies last. APP10: 10% off first app order, app only, one use per customer.",
 "footer": "Edikted · 1327 Willow St, Los Angeles, CA 90013 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Edikted"
}
```

## A1 — paid search ads

### A1-G1 · Ad group: going out tops
```json
{
 "ad_group": "going out tops",
 "headlines": [
  "Going Out Tops RN",
  "Black Friday Is Live",
  "60% OFF Your Faves*",
  "Corset Tops for GNO",
  "New Drops Every Week",
  "Shop Edikted Tops",
  "Fits You Saw on TikTok",
  "Lace Tops Under $30",
  "Strapless Tops for Fall",
  "Holiday Party Fits",
  "Free Shipping Over $80",
  "Your Next GNO Fit",
  "Satin Tops That Hit",
  "The BIGGEST Sale",
  "Thank Us Later"
 ],
 "descriptions": [
  "BLACK FRIDAY: 60% off your faves*. *Based on comp value. US only.",
  "Going out tops for every plan. New drops every week.",
  "Corsets, lace and satin tops you saw on your feed.",
  "Free standard shipping on orders above $80."
 ]
}
```

### A1-G2 · Ad group: baggy jeans
```json
{
 "ad_group": "baggy jeans",
 "headlines": [
  "Baggy Jeans RN",
  "Low Rise Baggy Jeans",
  "Black Friday Is Live",
  "60% OFF Your Faves*",
  "Wide Leg Jeans",
  "Jeans for Every Fit",
  "Shop Edikted Denim",
  "New Denim Drops",
  "Jeans Under $50",
  "The Jeans Everyone Asks About",
  "Free Shipping Over $80",
  "Baggy Fits for Fall",
  "Holiday Fits RN",
  "The BIGGEST Sale",
  "Thank Us Later"
 ],
 "descriptions": [
  "BLACK FRIDAY: 60% off your faves*. *Based on comp value. US only.",
  "Low rise, baggy and wide leg jeans for every fit.",
  "The denim you saw on your feed. New drops every week.",
  "Free standard shipping on orders above $80."
 ]
}
```
