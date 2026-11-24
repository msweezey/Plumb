# M.M.LaFleur — golden examples, wave 1 (history/)

Two on-brand examples per wave 1 task (P1, E1, A1). Each passes every automatic rule (validated by checks.py); the AI judge uses them as 4-anchors.

## P1 — product descriptions

### P1-G1 · MML-001 Moreland "The Traveler" Blazer - OrigamiTech (Aubergine)
Trap covered: Event price and a real compare-at; washable and wrinkle-resistant both = yes.
```json
{
 "sku": "MML-001",
 "title": "Moreland \"The Traveler\" Blazer - OrigamiTech",
 "description": "The blazer that keeps up with a travel day. The Moreland is cut in OrigamiTech, a machine washable, wrinkle-resistant fabric with stretch, so it comes out of a carry-on ready for the meeting. A clean, single-button front and real pockets keep it polished over a knit or a dress. Wear it with the Bia trouser for a suit, or over jeans on Friday.",
 "fiber_content": "OrigamiTech",
 "care": "Machine-washable",
 "fit": "Tailored; pockets",
 "sizes": "00, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20",
 "origin": "Made in China"
}
```

### P1-G2 · MMD-001 Valencia Power Dress - Luxe Flex Suiting (Dark Forest)
Trap covered: Published origin 'Made in Portugal' kept word for word; no fiber percentages exist.
```json
{
 "sku": "MMD-001",
 "title": "Valencia Power Dress - Luxe Flex Suiting",
 "description": "One of those dresses that does the deciding for you. The Valencia is a sleeveless sheath in Luxe Flex Suiting, with enough stretch to sit through a long day and a clean line that reads polished from the first meeting to the last. It is machine washable. Add a blazer for the boardroom, or a statement earring for dinner after.",
 "fiber_content": "Luxe Flex Suiting",
 "care": "Machine-washable",
 "fit": "Sheath, sleeveless",
 "sizes": "00, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20",
 "origin": "Made in Portugal"
}
```

## E1 — promo email (Black Friday Event (OF-01), featuring the Moreland blazer and Lancia Travel Dress)

### E1-G1 · Segment: active (persona GX)
```json
{
 "segment": "active",
 "subject": "The Black Friday Event starts now",
 "preheader": "Event pricing on marked styles, including the Moreland blazer.",
 "body": "Hi {first_name|there},\n\nOur Black Friday Event is here, with 10% to 40% off marked styles through Monday, December 1.\n\nIf one piece earns its place this season, make it the Moreland \"The Traveler\" Blazer in OrigamiTech. It is machine washable and wrinkle-resistant, and it is $296 during the event. Pair it with the Bia Pleated Trouser and you have a suit that packs flat.\n\nNot sure what to choose? Book a complimentary styling appointment, in a showroom or virtually.",
 "cta": "Shop the event",
 "terms": "Black Friday Event Nov 17 to Dec 1, 2026, ending 11:59 pm ET. Discount tier shown on each product; final-sale items, partner products and gift cards excluded. Cannot be combined with other offers.",
 "footer": "M.M.LaFleur · 100 Broadway, Fl 3, New York, NY 10005 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 M.M.LaFleur"
}
```

### E1-G2 · Segment: lapsed (persona MIL)
```json
{
 "segment": "lapsed",
 "subject": "It has been a while. Here is a good reason",
 "preheader": "Event pricing on the pieces our clients wear most, through December 1.",
 "body": "Hi {first_name|there},\n\nSome decisions are easy. Our Black Friday Event takes 10% to 40% off marked styles, and the Lancia Travel Dress in OrigamiTech is $220 while it lasts.\n\nIt is wrinkle-resistant, machine washable and has pockets, which is most of what a working week asks for.\n\nWhen you want a second opinion, our stylists are a free appointment away.",
 "cta": "See what is new",
 "terms": "Black Friday Event Nov 17 to Dec 1, 2026, ending 11:59 pm ET. Discount tier shown on each product; final-sale items, partner products and gift cards excluded. Cannot be combined with other offers.",
 "footer": "M.M.LaFleur · 100 Broadway, Fl 3, New York, NY 10005 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 M.M.LaFleur"
}
```

## A1 — paid search ads

### A1-G1 · Ad group: women's suiting
```json
{
 "ad_group": "women's suiting",
 "headlines": [
  "Suiting for Your Whole Day",
  "Machine Washable Suiting",
  "The Moreland Blazer",
  "Wrinkle-Resistant Blazers",
  "Designed in New York",
  "Polished, Not Stiff",
  "Suits That Pack Flat",
  "Blazers With Pockets",
  "Power Casual Workwear",
  "Book a Free Stylist",
  "Black Friday Event",
  "Sizes 00 to 20",
  "Shop the Bia Trouser",
  "Workwear That Travels",
  "M.M.LaFleur Suiting"
 ],
 "descriptions": [
  "Tailored suiting in easy-care fabrics. Meeting to dinner to flight.",
  "The Moreland blazer: machine washable, wrinkle-resistant, with real pockets.",
  "Black Friday Event: 10% to 40% off marked styles through Dec 1.",
  "Free personal styling, in a showroom or virtually."
 ]
}
```

### A1-G2 · Ad group: work dresses
```json
{
 "ad_group": "work dresses",
 "headlines": [
  "Work Dresses With Pockets",
  "Dresses for Your Whole Day",
  "The Valencia Power Dress",
  "Machine Washable Dresses",
  "Travel Dresses That Work",
  "Polished in One Piece",
  "Designed in New York",
  "Sizes 00 to 20",
  "Meeting to Dinner",
  "Book a Free Stylist",
  "Black Friday Event",
  "Wrinkle-Resistant Styles",
  "Power Casual Dresses",
  "Shop Work Dresses",
  "M.M.LaFleur Dresses"
 ],
 "descriptions": [
  "Dresses designed for working women. Easy care, polished lines.",
  "The Lancia Travel Dress is wrinkle-resistant and machine washable.",
  "Black Friday Event: 10% to 40% off marked styles through Dec 1.",
  "Not sure what fits? Our stylists will help, free."
 ]
}
```
