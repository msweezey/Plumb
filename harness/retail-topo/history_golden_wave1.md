# Topo Designs — golden examples, wave 1 (history/)

Two on-brand examples per wave 1 task (P1, E1, A1). Each passes every automatic rule (validated by checks.py); the AI judge uses them as 4-anchors.

## P1 — product descriptions

### P1-G1 · TDP-012 Mountain Duffel 40L (Grid / Very Peri)
Trap covered: Water resistance applies to the lining only; no denier or recycled claim in catalog.
```json
{
 "sku": "TDP-012",
 "title": "Mountain Duffel 40L",
 "description": "Built for weekend trips and gym days alike. The Mountain Duffel 40L carries a long weekend of gear, with removable backpack straps for the walk from the trailhead and padded nylon grab handles for everything else. A water-resistant lining, a front zip pocket, interior mesh pockets, a top valuables pocket and a key clip keep the small stuff sorted.",
 "fiber_content": "nylon",
 "care": "",
 "fit": "40L",
 "sizes": "One size",
 "origin": "Imported"
}
```

### P1-G2 · TDB-042 Topo Designs x Pine Printshop Classic Canvas Tote - Catalog
Trap covered: Printed in Colorado is not Made in USA; partner credited first; limited edition, no restock promise.
```json
{
 "sku": "TDB-042",
 "title": "Topo Designs x Pine Printshop Classic Canvas Tote - Catalog",
 "description": "Our friends at Pine Printshop laid out the Catalog graphic like a vintage outdoor mail-order page, numbered gear listings and all. It is printed with water-based inks in Fort Collins, Colorado, on a 10L cotton canvas tote with a roomy main compartment and reinforced straps for carry over the shoulder. Made for market runs, daily hauls and weekend trips. Limited edition.",
 "fiber_content": "cotton canvas",
 "care": "",
 "fit": "10L",
 "sizes": "One size",
 "origin": "Imported"
}
```

## E1 — promo email (Black Friday sale (OF-01), up to 50% off select styles)

### E1-G1 · Segment: active (persona MIL)
```json
{
 "segment": "active",
 "subject": "The days are shorter. So is this sale.",
 "preheader": "Up to 50% off select bags and layers, through Monday, Dec 1.",
 "body": "Hi {first_name|there},\n\nOur Black Friday sale is on: up to 50% off select styles through Monday, Dec 1.\n\nIt is a good time to grab the layers you will live in this winter, like the Global Wool Sweater, or a new everyday bag for the commute and the trailhead.\n\nEverything we make is backed by the M.A.P. Guarantee™, and shipping is free in the U.S. on orders of $100+.",
 "cta": "Shop the sale",
 "terms": "Up to 50% off select styles Nov 20 to Dec 1, 2026, ending 11:59 pm MT. Discount varies by item, max 50%. Excludes new arrivals, limited editions, collaborations and gift cards. While supplies last. Free U.S. shipping on $100+.",
 "footer": "Topo Designs · York Street Yards, Steele St, Denver, CO 80205 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Topo Designs"
}
```

### E1-G2 · Segment: lapsed (persona GX)
```json
{
 "segment": "lapsed",
 "subject": "Been a while. Your next trip needs a bag.",
 "preheader": "Up to 50% off select styles, made for anywhere on your map.",
 "body": "Hi {first_name|there},\n\nIt has been a minute, so here is a good reason to come back: up to 50% off select styles through Dec 1.\n\nThe Mountain Duffel 40L is ready for road trips, gym days and everything in between, with backpack straps and a water-resistant lining.\n\nWe guarantee everything we make. That is the M.A.P. Guarantee™.",
 "cta": "Find your bag",
 "terms": "Up to 50% off select styles Nov 20 to Dec 1, 2026, ending 11:59 pm MT. Discount varies by item, max 50%. Excludes new arrivals, limited editions, collaborations and gift cards. While supplies last. Free U.S. shipping on $100+.",
 "footer": "Topo Designs · York Street Yards, Steele St, Denver, CO 80205 · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Topo Designs"
}
```

## A1 — paid search ads

### A1-G1 · Ad group: crossbody bags
```json
{
 "ad_group": "crossbody bags",
 "headlines": [
  "Crossbody Bags for Anywhere",
  "The Mountain Cross Bag",
  "Fits a 14 Inch Laptop",
  "Everyday Carry, Sorted",
  "Recycled Nylon Bags",
  "Town to Trail Crossbody",
  "Up to 50% Off Select Bags",
  "Free U.S. Shipping $100+",
  "Designed in Colorado",
  "M.A.P. Guarantee™",
  "Slim Crossbody Bags",
  "Bike and Commute Bags",
  "Gifts Under $100",
  "Topo Designs Bags",
  "Made for Anywhere"
 ],
 "descriptions": [
  "Crossbody bags that carry your daily essentials, from commute to trailhead.",
  "The Mountain Cross Bag keeps a slim profile and fits a 14 inch laptop.",
  "Black Friday: up to 50% off select styles through Dec 1.",
  "Free U.S. shipping on $100+. Backed by the M.A.P. Guarantee™."
 ]
}
```

### A1-G2 · Ad group: travel backpacks
```json
{
 "ad_group": "travel backpacks",
 "headlines": [
  "Travel Backpacks Built to Last",
  "The Rover Pack Classic",
  "Global Travel Backpacks",
  "Carry-On Ready Packs",
  "Laptop Backpacks",
  "Commute to Trailhead",
  "Up to 50% Off Select Packs",
  "Free U.S. Shipping $100+",
  "Designed in Colorado",
  "M.A.P. Guarantee™",
  "Packs for Weekend Trips",
  "Classic Packs Since 2008",
  "Recycled Nylon Packs",
  "Topo Designs Packs",
  "Made for Anywhere"
 ],
 "descriptions": [
  "Travel backpacks with smart organization for flights, trains and road trips.",
  "Classic Topo designs in durable materials, for town and trail.",
  "Black Friday: up to 50% off select styles through Dec 1.",
  "Free U.S. shipping on $100+. Backed by the M.A.P. Guarantee™."
 ]
}
```
