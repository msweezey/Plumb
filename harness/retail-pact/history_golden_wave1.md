# Pact — golden examples, wave 1 (history/)

Two on-brand examples for each wave 1 task (P1, E1, A1). Each passes every hard rule; the AI judge uses them as 4-anchors. Product facts come from catalog_products.csv; offers from catalog_offers.csv.

## P1 — product descriptions

### P1-G1 · PM-019 Organic Everyday Crew Sock 3-Pack (Neutral Mix)
Trap covered: blend with recycled nylon (not 100% organic cotton).
```json
{
 "sku": "PM-019",
 "title": "Organic Everyday Crew Sock 3-Pack",
 "description": "Socks you'll reach for first. Three pairs of crew socks made with GOTS-certified organic cotton, plus recycled nylon and a little stretch so they keep their shape. The soft, breathable knit sits at crew height, easy under jeans or with sneakers on busy days. Pick your size, pull on a pair and get on with your day.",
 "made_with": "Organic cotton*",
 "made_without": "Harsh chemicals, toxic dyes and PFAS",
 "certified": "GOTS & Fair Trade",
 "footnote": "*Also with 20% recycled nylon and 2% elastane for stretch and recovery.",
 "fiber_content": "78% GOTS-certified organic cotton, 20% recycled nylon, 2% elastane",
 "fit": "Crew height",
 "sizes": "M/L, L/XL",
 "care": "Machine wash cold, tumble dry low",
 "origin": "Imported"
}
```

### P1-G2 · PH-021 Organic Bath Towel Set (White)
Trap covered: qualified USA origin.
```json
{
 "sku": "PH-021",
 "title": "Organic Bath Towel Set",
 "description": "A plush towel set for the everyday reset. Six pieces of 100% GOTS-certified organic cotton terry at 600 GSM, made without harsh chemicals, toxic dyes and PFAS. Hang the full set in your own bath or split it with the guest room. Wash warm and tumble dry low.",
 "made_with": "100% organic cotton",
 "made_without": "Harsh chemicals, toxic dyes and PFAS",
 "certified": "GOTS & Fair Trade",
 "footnote": "",
 "fiber_content": "100% GOTS-certified organic cotton terry, 600 GSM",
 "fit": "Set of 6",
 "sizes": "6-piece",
 "care": "Machine wash warm, tumble dry low",
 "origin": "Cut and sewn in USA from imported organic cotton fabric"
}
```

## E1 — promo email (OF-01 Black Friday early access)

### E1-G1 · Segment: active (persona MIL)
```json
{
 "segment": "active",
 "subject": "Early access: up to 40% off everything",
 "preheader": "Organic essentials for you and your gift list, on sale through Sunday.",
 "body": "Hi {first_name|there},\n\nOur Black Friday sale starts early for you. Everything is up to 40% off through Sunday, Nov 23 at 11:59 pm MT.\n\nRestock what you wear most, from On The Go-To Leggings at $20 to the black Fit & Flare V-Neck Twist Dress at $49. It's all made with organic cotton and made without harsh chemicals, toxic dyes and PFAS.\n\nFree standard shipping on orders $99+.",
 "cta": "Shop the sale",
 "terms": "Up to 40% off sitewide Nov 17-23, 2026, ending 11:59 pm MT. Discount varies by item. Excludes gift cards. Not valid with the welcome offer. $20 price applies to the On The Go-To Legging only, through Nov 30. $49 price applies to the black Fit & Flare V-Neck Twist Dress only, while supplies last.",
 "footer": "Pact · 4725 Walnut St, Boulder, CO 80301 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Pact"
}
```

### E1-G2 · Segment: lapsed (persona GX)
```json
{
 "segment": "lapsed",
 "subject": "It's been a while: up to 40% off",
 "preheader": "Organic sheets, soft layers and everyday basics, on sale through Sunday.",
 "body": "Hi {first_name|there},\n\nIt's good to see you. Our Black Friday sale is here early, with up to 40% off everything through Sunday, Nov 23 at 11:59 pm MT.\n\nIf it's time to refresh the bedroom, our Room Service Sateen and Cool-Air Percale sheets are made with organic cotton in Fair Trade Certified™ factories. Deep pockets fit mattresses up to 16 inches.\n\nPact Balance members earn 5% Pact Credit on orders. See terms.",
 "cta": "Shop bedding",
 "terms": "Up to 40% off sitewide Nov 17-23, 2026, ending 11:59 pm MT. Discount varies by item. Excludes gift cards. Not valid with the welcome offer. Free standard shipping on orders $99+.",
 "footer": "Pact · 4725 Walnut St, Boulder, CO 80301 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Pact"
}
```

## A1 — paid search ads

### A1-G1 · Ad group: organic leggings
```json
{
 "ad_group": "organic leggings",
 "headlines": ["Organic Cotton Leggings","On The Go-To Legging, $20","Made With Organic Cotton","GOTS-Certified Organic Cotton","Gentle on Skin",
               "Breathable Organic Cotton","High Rise, Ankle Length","Sizes XS to 2XL","Up to 40% Off Sitewide","Free Shipping on $99+",
               "Fair Trade Certified™","Soft, Breathable Leggings","Everyday Organic Essentials","Leggings Starting at $20","Dress Yourself Well"],
 "descriptions": ["Organic cotton leggings made without harsh chemicals, toxic dyes and PFAS. Now $20.",
                  "High rise, ankle length and a soft stretch knit for every day. Sizes XS to 2XL.",
                  "Up to 40% off sitewide through Nov 23. Free standard shipping on orders $99+.",
                  "GOTS-certified organic cotton, made in Fair Trade Certified™ factories."]
}
```

### A1-G2 · Ad group: organic sheets
Trap covered: one sheet SKU is GOTS-pending, so the group says "made with organic cotton", not "certified".
```json
{
 "ad_group": "organic sheets",
 "headlines": ["Organic Cotton Sheet Sets","Room Service Sateen Sheets","Cool-Air Percale Sheets","Made With Organic Cotton","300 Thread Count Sateen",
               "Fits Mattresses Up to 16 in","Twin, Full, Queen and King","Gentle on Skin","Up to 40% Off Sitewide","Free Shipping on $99+",
               "Fair Trade Certified™","Soft Sheets, Clean Fabric","Percale or Sateen, Your Pick","Organic Bedding Essentials","Dress Your Bed Well"],
 "descriptions": ["Crisp percale or smooth sateen, made without harsh chemicals, toxic dyes and PFAS.",
                  "Deep pockets fit mattresses up to 16 inches. Twin, Full, Queen and King.",
                  "Up to 40% off sitewide through Nov 23. Free standard shipping on orders $99+.",
                  "Made with organic cotton in Fair Trade Certified™ factories."]
}
```
