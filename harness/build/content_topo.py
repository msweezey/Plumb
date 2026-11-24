import re
from content_common import fixtures_factory
ADDR = "York Street Yards, Steele St, Denver, CO 80205"
tags = lambda p: p.get("tags") or []
MAT = r"(?:\d+% )?(?:recycled nylon|recycled polyester|organic cotton|merino wool|recycled wool|cotton canvas|cotton twill|corduroy|nylon|polyester|cotton|wool|leather|canvas|stainless steel|fleece|hemp|ripstop|cordura|spandex|acrylic|suede)"

PARTNERS = ["Pine Printshop", "Toyota", "MiiR", "Puffin", "New Belgium Brewing", "Dinosaur Jr", "Denver Summit", "VAER", "Worn & Wound", "Stranahan's", "Teravail", "Bedrock"]
def categorize(p):
    t = p["type"]
    if t.startswith(("Bags/Backpacks", "Bags/Travel", "Bags/Duffel", "Bags/Briefcases")): return "PAK"
    if t.startswith("Bags"): return "BAG"
    if "Apparel" in t: return "APP"
    if t.startswith("Accessories"): return "ACC"
    return "ACC"

def material(p):
    found = []
    for m in re.findall(MAT, (p["body"] or "").lower()):
        if m not in found and not any(m in f for f in found): found.append(m)
    return ", ".join(found[:3])

def catalog_traps(rows, R):
    for r in rows:
        n = []
        if not r["material"]: n.append("missing material: do not invent")
        if "final sale" in r["name"].lower(): r["final_sale"] = "yes"; n.append("final sale (in product name): say so")
        if r["coming_soon"] == "yes": r["status"] = "coming_soon"; n.append("coming soon: tease only, no 'shop now'")
        if r["collab_partner"]: n.append(f"collaboration with {r['collab_partner']}: name the partner as catalog")
        if r["usa_note"]: n.append("USA wording published for printing/finishing only: never 'Made in USA' for the product")
        if r["water_resistant"] == "yes": n.append("water resistant (never waterproof)")
        if "recycled" in r["material"]: n.append("recycled content: no % unless catalog states it")
        if r["limited_edition"] == "yes": n.append("limited edition: no 'restocking' promises")
        r["trap_notes"] = ";".join(n)
    act = [r for r in rows if r["status"] == "active"]
    for r in R.sample(act, 3): r["status"] = "discontinued"; r["trap_notes"] += ";discontinued: exclude from feeds and recommendations"
    for r in R.sample([r for r in rows if r["status"] == "active" and r["sale_flag"] == "yes"] or act, 2): r["final_sale"] = "yes"; r["trap_notes"] += ";clearance: final sale"
    for r in R.sample([r for r in rows if r["status"] == "active"], 4): r["hero"] = "True"; r["trap_notes"] += ";hero: featured in wave 1"

C = dict(
 seed=20261125, domain="topodesigns.com", sku_prefix="TD", address=ADDR, tz_end="11:59 pm MT",
 categories=[("PAK", "Backpacks, travel and duffels"), ("BAG", "Crossbody, hip packs and organization"), ("APP", "Apparel"), ("ACC", "Hats, accessories and drinkware")],
 categorize=categorize, synth_colors=["Black", "Pond Blue", "Olive", "Clay", "Natural", "Navy"],
 color_from_title=lambda t: "", clean_name=lambda t: t.strip(), material=material,
 origin=lambda p: "Imported", subcat=lambda p: p["type"].split("/")[-1].replace("-", " "),
 gender=lambda p: "Men" if "Mens/" in p["type"] else "Women" if "Womens/" in p["type"] else "Unisex",
 sizes=lambda p: ", ".join(p["options"].get("Size") or []) or "One size",
 care=lambda p: "Machine wash" if "machine wash" in (p["body"] or "").lower() else "",
 extra_cols={"water_resistant": lambda p, r: "yes" if re.search(r"water[- ]resistant", (p["body"] or "").lower()) else "no",
             "collab_partner": lambda p, r: " x ".join(x for x in PARTNERS if x.lower() in p["title"].lower()),
             "usa_note": lambda p, r: (re.search(r"(USA-made[^.]*|[Pp]rinted[^.]*Colorado[^.]*|[Hh]and-printed[^.]*Colorado[^.]*)", p["body"] or "").group(1)[:90] if re.search(r"USA-made|[Pp]rinted[^.]*Colorado", p["body"] or "") else ""),
             "coming_soon": lambda p, r: "yes" if "coming-soon" in tags(p) else "no",
             "limited_edition": lambda p, r: "yes" if "limited-edition" in tags(p) else "no",
             "personalizable": lambda p, r: "yes" if "collection-personalized" in tags(p) else "no",
             "guarantee": lambda p, r: "M.A.P. Guarantee™"},
 catalog_traps=catalog_traps,
 history_mode=lambda r, R: "msrp",
 personas=("MIL", "GX"),
 review_text={
  "PAK": ["Took it through three airports and up a trail. Still looks new.", "Fits my 16\" laptop and a jacket with room to spare.", "The colors are so good. People ask about it.", "Comfortable straps on a long day in the city.", "Packs like a dream for weekend trips."],
  "BAG": ["My everyday crossbody now. Holds more than it looks.", "Great on the bike, stays put.", "Perfect size for dog walks and errands.", "Love the key clip inside.", "Bought one for my partner too."],
  "APP": ["Softest shirt I own, and it held up through a whole camping season.", "Fits true to size with room to layer.", "Wore it hiking and to dinner after.", "The fabric gets better every wash.", "Pockets are in the right places."],
  "ACC": ["Great gift, came quickly.", "Keeps coffee hot through the morning hike.", "Simple and well made.", "The hat fits and the patch is great."]},
 review_neg=["Strap started fraying after a year.", "Color was a bit duller than the photo.", "Runs a little short in the torso.", "Wish it had a water bottle pocket.", "Shipping took longer than expected."],
 review_traps=[("health_claim", "This pack fixed my back pain completely.", 5, ""),
               ("competitor_mention", "Way better built than Patagonia and Cotopaxi.", 5, ""),
               ("discontinued_product", "Bring this colorway back!", 5, ""),
               ("profanity", "Damn good bag, survived a f***ing monsoon.", 5, ""),
               ("personal_info", "Text me at 720-555-0144 if you want my old one.", 5, ""),
               ("waterproof_claim", "Completely waterproof, I dunked it in a river.", 5, ""),
               ("made_in_usa", "Love that it's all made in Colorado.", 5, ""),
               ("warranty_claim", "Lifetime warranty means I'll never buy another.", 5, ""),
               ("off_topic", "Website search is clunky.", 2, ""),
               ("price_complaint", "Too expensive for nylon.", 1, ""),
               ("sizing_dispute", "Hoodie is way bigger than the chart.", 2, ""),
               ("incentivized_unlabeled", "Got this from a Topo ambassador kit. Love it.", 5, "")],
 offers=[
  dict(offer_id="OF-01", type="sitewide", name="Black Friday sale", mechanic="Up to 50% off select styles", code="", start="2026-11-20", end="2026-12-01 23:59 MT", min_spend="", exclusions="New arrivals, limited editions, collaborations, gift cards", terms="Discount varies by item, max 50%. While supplies last."),
  dict(offer_id="OF-02", type="welcome", name="Join The Topo Crew", mechanic="10% off your first order", code="CREW10", start="2026-01-01", end="2026-12-31 23:59 MT", min_spend="", exclusions="Sale items, gift cards", terms="New email subscribers only."),
  dict(offer_id="OF-03", type="shipping", name="Free U.S. shipping", mechanic="Free U.S. shipping on $100+ and exchanges", code="", start="2026-01-01", end="2026-12-31 23:59 MT", min_spend="100", exclusions="", terms="Contiguous US."),
  dict(offer_id="OF-04", type="guarantee", name="M.A.P. Guarantee™", mechanic="We guarantee everything we make", code="", start="2026-01-01", end="2026-12-31 23:59 MT", min_spend="", exclusions="Terms on guarantee page (not retrieved: page blocked)", terms="Name it exactly; link terms; never 'lifetime warranty'."),
  dict(offer_id="OF-05", type="collab", name="Puffin x Topo Designs, round 2", mechanic="Collab launch; full price", code="", start="2026-11-19", end="2026-12-31 23:59 MT", min_spend="", exclusions="", terms="No discount."),
  dict(offer_id="OF-06", type="limited", name="2026 Limited Edition Solar Hiker Kit", mechanic="VAER x Topo Designs x Worn & Wound; full price", code="", start="2026-10-01", end="2026-12-31 23:59 MT", min_spend="", exclusions="", terms="Limited quantities."),
  dict(offer_id="OF-07", type="giveaway", name="Dream bike giveaway", mechanic="Enter to win a Surly Straggler build", code="", start="2026-11-01", end="2026-11-22 23:59 MT", min_spend="", exclusions="", terms="US participants only. No purchase necessary. Rules linked in bio. Ends 11/22/26."),
  dict(offer_id="OF-08", type="gift", name="Holiday Gift Guide", mechanic="Curated gifts; no discount of its own", code="", start="2026-11-10", end="2026-12-24 23:59 MT", min_spend="", exclusions="", terms=""),
  dict(offer_id="OF-09", type="retail", name="HQ storefront grand opening", mechanic="New store at York Street Yards", code="", start="2026-11-08", end="2026-11-15 23:59 MT", min_spend="", exclusions="", terms="ENDED: decoy."),
  dict(offer_id="OF-10", type="expired", name="Memorial Day sale", mechanic="Up to 40% off", code="", start="2026-05-22", end="2026-05-26 23:59 MT", min_spend="", exclusions="", terms="EXPIRED: decoy."),
 ],
 palette=[
  dict(name="Bone", hex="#F5F4EF", role="background", uses=71, used_for="Page background"),
  dict(name="Black", hex="#000000", role="primary", uses=84, used_for="Logo, icons, headlines"),
  dict(name="Topo Charcoal", hex="#241F20", role="primary", uses=53, used_for="Body text, buttons, footer"),
  dict(name="White", hex="#FFFFFF", role="background", uses=56, used_for="Cards, text on dark"),
  dict(name="Topo Red", hex="#E31B23", role="accent", uses=20, used_for="Accent buttons, badges, sale"),
  dict(name="Deep Red", hex="#A80A10", role="accent", uses=7, used_for="Red hover state"),
  dict(name="Brick", hex="#B0161C", role="accent", uses=6, used_for="Pressed state, sale text"),
  dict(name="Oxblood", hex="#881015", role="accent", uses=6, used_for="Dark red panels"),
  dict(name="Stone", hex="#6E6C63", role="secondary", uses=7, used_for="Secondary text"),
  dict(name="Sand", hex="#EFEEE6", role="background", uses=4, used_for="Tiles, inputs"),
  dict(name="Fog", hex="#CCCCCC", role="neutral", uses=7, used_for="Borders"),
  dict(name="Lake", hex="#6E9FC6", role="secondary", uses=4, used_for="Links on dark, illustrations"),
 ],
 fonts={"families": [
   {"name": "New Spirit Condensed", "type": "condensed serif (display)", "weights": "Regular, SemiBold Condensed, Compressed", "use": "Headings (--header-first-font)", "source": "theme.css @font-face and --header-first-font"},
   {"name": "IBM Plex Sans", "type": "sans", "weights": "Regular–Bold + italics", "use": "Body (--paragraph-first-font)", "source": "theme.css"},
   {"name": "IBM Plex Sans Condensed", "type": "condensed sans", "weights": "ExtraLight–Bold + italics", "use": "Labels, nav, buttons", "source": "theme.css @font-face"},
   {"name": "Inter", "type": "sans", "weights": "400, 600", "use": "Shopify theme fallback files", "source": "homepage woff2 refs"}],
   "fallbacks": {"New Spirit Condensed": "Georgia, serif", "IBM Plex Sans": "Arial, sans-serif", "IBM Plex Sans Condensed": "'Arial Narrow', Arial, sans-serif"}},
 radius=0, logo_note="Wordmark 'TOPO DESIGNS' with mountain mark; logo only. Running copy 'Topo Designs', short form 'Topo'.",
 name_bad_examples=["TopoDesigns", "TOPO DESIGNS (in running copy)", "Topo Design"], serial_obs="27 assets with, 16 without",
 pdp_shape="Shape: a short hook, what it carries or does (laptop size, capacity, pockets), materials, then where it goes (town, trail, travel).",
 ship_text="'Free U.S. shipping on $100+' (site banner; older third-party pages say $99+)",
 tagline_rule="Current line is 'Made for anywhere on your map.' Never say products are 'handmade in Colorado' or 'all made in the USA' (retired, pre-2015 claims).",
 R_src={"BRD": "E01", "VOI": "E05", "MSG": "E03", "COL": "E02", "TYP": "E02", "LEG": "E06", "IMG": "E07", "WEB": "E04", "SOC": "E08", "DR": "E09", "EML": "E06"},
 subs=[("Pact Credit", "store credit"), ("© 2026 Pact", "© 2026 Topo Designs"), ("'Pact'", "'Topo Designs'"), ("Pact", "Topo Designs"), ("$99+", "$100+")],
 allow_words=["organic cotton"],
 R={
  "BRD-01": {"rule": "Purpose: get everyone outside, without the gatekeeping that holds people back (co-founder Jedd Rose).", "check": "AI judge", "anchors": {"1": "Hardcore or exclusive outdoor talk", "4": "Welcoming: town or trail, everyone belongs"}},
  "BRD-02": {"rule": "Positioning: durable, classic, functional bags and apparel designed in Colorado since 2008, for town and trail.", "check": "AI judge", "anchors": {"1": "Generic outdoor gear", "4": "Classic design + durability + anywhere use"}},
  "BRD-03": {"rule": "Lead with where it goes and what it carries; materials and features are the proof.", "check": "AI judge"},
  "BRD-04": {"rule": "Trait 1 — Friendly: 'our friends', thank-yous, community; is not corporate.", "check": "AI judge"},
  "BRD-05": {"rule": "Trait 2 — Easygoing outdoors: trailheads and tailgates alike; is not hardcore, technical-only or gatekeeping.", "check": "AI judge"},
  "BRD-06": {"rule": "Trait 3 — Crafted: specific about materials, capacity and features; is not a spec-sheet dump.", "check": "AI judge"},
  "BRD-07": {"rule": "Trait 4 — Playful: light humor and a few emoji on social; is not goofy in ads.", "check": "AI judge"},
  "VOI-04": "Product names keep the family pattern: collection + item (+ size), e.g. 'Mountain Cross Bag', 'Rover Pack Classic', 'Global Briefcase'. Collabs: 'Topo Designs x Partner Item' or 'Partner x Topo Designs Item' as catalog.",
  "VOI-07": "Percentages and sizes as numerals: '50%', '26L', '16\" laptop'.",
  "VOI-08": "Use spaced em dashes or ellipses for asides; no double hyphens.",
  "VOI-15": "Speak to 'you'; the brand is 'we', 'Topo' or 'Topo Designs'; the community is 'the Topo Crew'.",
  "VOI-16": {"rule": "Collab copy names the partner, credits them as 'our friends', and says what each side brought.", "check": "AI judge"},
  "VOI-17": "Tone — promo: relaxed and honest about the deal ('The days are shorter. So is this sale.'); never frantic.",
  "VOI-20": "Tone — onboarding: welcome to the Topo Crew, 10% off the first order, the M.A.P. Guarantee™.",
  "VOI-22": {"rule": "Social may use light emoji (up to 4) and plain hashtags-free captions; 'link in bio' for links.", "check": "auto"},
  "VOI-25": {"rule": "Sounds like Topo Designs: friendly, easygoing, crafted, playful (matches golden examples).", "check": "AI judge"},
  "MSG-02": {"rule": "Value prop 1 — Built to last: durable materials (recycled nylon, organic cotton, wool) backed by the M.A.P. Guarantee™.", "check": "AI judge"},
  "MSG-03": {"rule": "Value prop 2 — Made for anywhere: one bag from commute to trailhead to carry-on.", "check": "AI judge"},
  "MSG-04": {"rule": "Value prop 3 — Colorado design and friends: designed in Colorado since 2008; collaborations with brands we like.", "check": "AI judge"},
  "MSG-07": {"rule": "'Water resistant' only for SKUs with water_resistant = yes; never 'waterproof' or 'weatherproof'.", "check": "auto"},
  "MSG-08": {"rule": "Coming-soon SKUs are teased with the date, never 'shop now'.", "check": "auto"},
  "MSG-09": {"rule": "Never say all products are made in the USA or handmade in Colorado; printed-in-Colorado items say exactly that.", "check": "auto"},
  "MSG-10": {"rule": "Recycled content: name the recycled material as catalog; no percentage unless the catalog states one.", "check": "auto"},
  "MSG-11": {"rule": "Guarantee: 'M.A.P. Guarantee™' exactly; 'We guarantee everything we make' allowed; never 'lifetime warranty'.", "check": "auto"},
  "MSG-12": "Never name competitors (Patagonia, Cotopaxi, Fjällräven) in owned copy.",
  "MSG-14": "Name products exactly as the catalog.",
  "MSG-16": {"rule": "Limited editions: never promise restocks.", "check": "auto"},
  "LOG-04": "Clear space equals the height of the mountain mark.",
  "LOG-10": "Wordmark caps belong to the logo only; never retype it.",
  "LOG-11": "Never use brand/deprecated/logo-legacy.svg.",
  "COL-01": "Primary: Topo Charcoal #241F20 for text and buttons; Black #000000 for logo and icons.",
  "COL-02": "Backgrounds: Bone #F5F4EF (default page), White #FFFFFF, Sand #EFEEE6.",
  "COL-03": "Accent: Topo Red #E31B23 for accent buttons and badges; Deep Red #A80A10 hover; Brick #B0161C pressed; Oxblood #881015 panels.",
  "COL-04": "Neutrals: Fog #CCCCCC for borders only.",
  "COL-05": "Sale prices use Brick #B0161C (6.4:1 on Bone); Topo Red #E31B23 is 4.29:1 on Bone, so large type and fills only.",
  "COL-07": "Usage share follows the homepage: bone, white and charcoal about 75%; reds about 12%.",
  "COL-09": "Never set body text in Fog or Lake on light backgrounds.",
  "COL-10": "Topo Red #E31B23 on Bone is large text only (4.29:1).",
  "COL-11": "Struck-through prices in Stone #6E6C63.",
  "TYP-01": "Display: New Spirit Condensed (headings), SemiBold Condensed for big promo heads.",
  "TYP-02": "Body: IBM Plex Sans.",
  "TYP-03": "Labels, nav and buttons: IBM Plex Sans Condensed.",
  "TYP-04": "Fallbacks: New Spirit → Georgia; IBM Plex Sans → Arial; Condensed → 'Arial Narrow'.",
  "TYP-06": "Web sizes: headings 32–56 px New Spirit Condensed; body 16 px IBM Plex Sans.",
  "TYP-08": "Social on-image: New Spirit Condensed headline, Plex for details.",
  "TYP-09": "Buttons: IBM Plex Sans Condensed, uppercase with tracking, square corners.",
  "TYP-10": "Never use third-party widget fonts in brand assets.",
  "IMG-01": {"rule": "Image types: gear on people in town and outdoors, trailheads, road trips, bikes, camp, flat lays of what fits inside.", "check": "AI judge"},
  "IMG-02": {"rule": "Real people with friends and dogs, a range of ages and bodies; warm natural light; color-forward gear.", "check": "AI judge"},
  "IMG-10": "Icons: simple line icons in Charcoal.",
  "IMG-11": "Partner logos appear only on collaboration products.",
  "LEG-01": f"Marketing email: accurate sender, honest subject, physical address '{ADDR}' (suite to confirm), unsubscribe.",
  "LEG-04": "Trademarks: 'M.A.P. Guarantee™' with ™ on every mention.",
  "LEG-09": "Accessibility statement link and '© 2026 Topo Designs' in web and email footers.",
  "LEG-13": "Clearance items: 'Final sale' wherever they appear.",
  "LEG-14": "Origin: 'Imported' on every product description unless catalog says otherwise.",
  "LEG-15": "Made in USA: never, unless all or virtually all of the product is made in the US and claims.md says so; printing in Colorado is not Made in USA.",
  "LEG-16": "Materials as catalog; no invented deniers, capacities or percentages.",
  "LEG-19": "Returns: free exchanges; link the returns policy for anything else.",
  "LEG-20": "Topo Crew is an email list, not a points program; never invent points.",
  "EML-03": "Sender name 'Topo Designs'; reply-to a monitored address.",
  "SOC-02": "TikTok and Reels: gear in use, collab drops; no hashtags (observed).",
  "BRA-01": "Line 'Made for anywhere on your map.' set as written.",
  "BRA-03": {"rule": "Concept: places on the map, friends along the way; never extreme-sport bravado.", "check": "AI judge"},
  "BRA-04": {"rule": "Key visual: color-forward bag on a person outdoors, bone and charcoal frame, a red accent.", "check": "AI judge"},
  "DCO-02": "Price slot uses feed value with trailing zeros stripped.",
  "LP-03": {"rule": "Three blocks map to built to last, made for anywhere, Colorado design and friends.", "check": "AI judge"},
  "LP-04": "FAQ answers shipping ($100+ free U.S.), exchanges, and the M.A.P. Guarantee™ (link).",
  "WEB-03": "PDP module: Features (capacity, laptop size, pockets), Materials (catalog), Origin, M.A.P. Guarantee™ link.",
  "WEB-04": "Collab PDPs credit the partner in the first sentence.",
  "WEB-06": "Product names keep the collection family names from the catalog.",
 },
 R_drop=[], R_add=[],
)

def pdp_extra(o, p):
    v = []; d = o["description"].lower()
    if "water resistant" in d or "water-resistant" in d:
        if p["water_resistant"] != "yes": v.append(("MSG-07", "water resistant claim"))
    if re.search(r"made in (the )?usa|made in colorado|handmade in colorado|usa-made", d): v.append(("MSG-09", "USA claim"))
    if re.search(r"\d+% recycled", d) and "%" not in p["material"]: v.append(("MSG-10", "recycled %"))
    if p["collab_partner"] and p["collab_partner"].split()[0].lower() not in d: v.append(("WEB-04", "partner not credited"))
    if p["status"] == "coming_soon" and "shop now" in d: v.append(("MSG-08", "coming soon"))
    if p["final_sale"] == "yes" and "final sale" not in d: v.append(("LEG-13", "final sale"))
    return v
def email_extra(o, P):
    v = []; t = (o["body"] + " " + o["terms"]).lower()
    if "memorial day" in t or "grand opening" in t: v.append(("MSG-05", "ended offer"))
    if "lifetime warranty" in t: v.append(("MSG-11", "lifetime warranty"))
    if re.search(r"was \$|msrp|compare at", t): v.append(("LEG-10", "reference price"))
    return v
def ads_extra(o):
    t = " ".join(o["headlines"] + o["descriptions"]).lower(); v = []
    if re.search(r"made in (the )?usa|made in colorado|handmade", t): v.append(("MSG-09", "USA claim"))
    if "lifetime" in t: v.append(("MSG-11", "lifetime"))
    return v
def social_extra(o):
    t = o["caption"].lower(); v = []
    if o.get("partner") and not re.search(r"#ad\b|paid partnership", t): v.append(("LEG-06", "creator disclosure"))
    if "giveaway" in t or "enter to win" in t:
        if not ("us participants only" in t or "us only" in t) or "rules" not in t: v.append(("SOC-06", "giveaway terms"))
    return v
def sms_extra(o):
    c = o["contact"]; v = []
    if c.get("sms_consent_type") != "prior express written consent": v.append(("LEG-02", "no written SMS consent"))
    return v
C.update(pdp_extra=pdp_extra, email_extra=email_extra, ads_extra=ads_extra, social_extra=social_extra, sms_extra=sms_extra)
C["fixtures"] = fixtures_factory("TOPO", 100, "OF-01", "America/Denver",
  [{"id": "SC-01", "type": "praise", "text": "My Rover Pack has been to 14 countries and it still looks new 🙌"},
   {"id": "SC-02", "type": "question", "text": "Is the Mountain Cross Bag waterproof? Biking in rain a lot."},
   {"id": "SC-03", "type": "question", "text": "Does the M.A.P. Guarantee cover a broken buckle?"},
   {"id": "SC-04", "type": "complaint", "text": "Zipper broke after 2 months, not impressed."},
   {"id": "SC-05", "type": "complaint", "text": "Ordered during the sale, still hasn't shipped."},
   {"id": "SC-06", "type": "troll", "text": "Instagram gear for people who never go outside lol"},
   {"id": "SC-07", "type": "made_in", "text": "Are these still made in Colorado?"},
   {"id": "SC-08", "type": "competitor", "text": "Why not just buy Patagonia?"},
   {"id": "SC-09", "type": "personal_info", "text": "@topodesigns order 33018 my address is 1412 Clay St Denver, where is it"},
   {"id": "SC-10", "type": "giveaway", "text": "Can I enter the bike giveaway from Canada?"}],
  ["", "Two items; check $100 threshold", "Clearance item: final sale", "Discontinued item: suggest one active alternative", "Coming-soon item: tease date only"])

FOOT = f"Topo Designs · {ADDR} · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Topo Designs"
TERMS = "Up to 50% off select styles Nov 20 to Dec 1, 2026, ending 11:59 pm MT. Discount varies by item, max 50%. Excludes new arrivals, limited editions, collaborations and gift cards. While supplies last. Free U.S. shipping on $100+."
C["goldens"] = [
 dict(id="P1-G1", task="P1", title="TDP-012 Mountain Duffel 40L (Grid / Very Peri)", trap="Water resistance applies to the lining only; no denier or recycled claim in catalog.",
  out=dict(sku="TDP-012", title="Mountain Duffel 40L",
   description="Built for weekend trips and gym days alike. The Mountain Duffel 40L carries a long weekend of gear, with removable backpack straps for the walk from the trailhead and padded nylon grab handles for everything else. A water-resistant lining, a front zip pocket, interior mesh pockets, a top valuables pocket and a key clip keep the small stuff sorted.",
   fiber_content="nylon", care="", fit="40L", sizes="One size", origin="Imported")),
 dict(id="P1-G2", task="P1", title="TDB-042 Topo Designs x Pine Printshop Classic Canvas Tote - Catalog", trap="Printed in Colorado is not Made in USA; partner credited first; limited edition, no restock promise.",
  out=dict(sku="TDB-042", title="Topo Designs x Pine Printshop Classic Canvas Tote - Catalog",
   description="Our friends at Pine Printshop laid out the Catalog graphic like a vintage outdoor mail-order page, numbered gear listings and all. It is printed with water-based inks in Fort Collins, Colorado, on a 10L cotton canvas tote with a roomy main compartment and reinforced straps for carry over the shoulder. Made for market runs, daily hauls and weekend trips. Limited edition.",
   fiber_content="cotton canvas", care="", fit="10L", sizes="One size", origin="Imported")),
 dict(id="E1-G1", task="E1", title="Segment: active (persona MIL)",
  out=dict(segment="active", subject="The days are shorter. So is this sale.",
   preheader="Up to 50% off select bags and layers, through Monday, Dec 1.",
   body="Hi {first_name|there},\n\nOur Black Friday sale is on: up to 50% off select styles through Monday, Dec 1.\n\nIt is a good time to grab the layers you will live in this winter, like the Global Wool Sweater, or a new everyday bag for the commute and the trailhead.\n\nEverything we make is backed by the M.A.P. Guarantee™, and shipping is free in the U.S. on orders of $100+.",
   cta="Shop the sale", terms=TERMS, footer=FOOT)),
 dict(id="E1-G2", task="E1", title="Segment: lapsed (persona GX)",
  out=dict(segment="lapsed", subject="Been a while. Your next trip needs a bag.",
   preheader="Up to 50% off select styles, made for anywhere on your map.",
   body="Hi {first_name|there},\n\nIt has been a minute, so here is a good reason to come back: up to 50% off select styles through Dec 1.\n\nThe Mountain Duffel 40L is ready for road trips, gym days and everything in between, with backpack straps and a water-resistant lining.\n\nWe guarantee everything we make. That is the M.A.P. Guarantee™.",
   cta="Find your bag", terms=TERMS, footer=FOOT)),
 dict(id="A1-G1", task="A1", title="Ad group: crossbody bags",
  out=dict(ad_group="crossbody bags", headlines=["Crossbody Bags for Anywhere","The Mountain Cross Bag","Fits a 14 Inch Laptop","Everyday Carry, Sorted","Recycled Nylon Bags","Town to Trail Crossbody","Up to 50% Off Select Bags","Free U.S. Shipping $100+","Designed in Colorado","M.A.P. Guarantee™","Slim Crossbody Bags","Bike and Commute Bags","Gifts Under $100","Topo Designs Bags","Made for Anywhere"],
   descriptions=["Crossbody bags that carry your daily essentials, from commute to trailhead.","The Mountain Cross Bag keeps a slim profile and fits a 14 inch laptop.","Black Friday: up to 50% off select styles through Dec 1.","Free U.S. shipping on $100+. Backed by the M.A.P. Guarantee™."])),
 dict(id="A1-G2", task="A1", title="Ad group: travel backpacks",
  out=dict(ad_group="travel backpacks", headlines=["Travel Backpacks Built to Last","The Rover Pack Classic","Global Travel Backpacks","Carry-On Ready Packs","Laptop Backpacks","Commute to Trailhead","Up to 50% Off Select Packs","Free U.S. Shipping $100+","Designed in Colorado","M.A.P. Guarantee™","Packs for Weekend Trips","Classic Packs Since 2008","Recycled Nylon Packs","Topo Designs Packs","Made for Anywhere"],
   descriptions=["Travel backpacks with smart organization for flights, trains and road trips.","Classic Topo designs in durable materials, for town and trail.","Black Friday: up to 50% off select styles through Dec 1.","Free U.S. shipping on $100+. Backed by the M.A.P. Guarantee™."])),
]
C["drafts_note"] = "Off-brand drafts for B1 (brand edit) and review tasks. T-01..T-06 twin the wave 1 goldens; T-07..T-10 cover other channels. Agents never see expected_violations."
X = lambda *a: [dict(rule=r) for r in a]
C["drafts"] = [
 dict(id="T-01", twin_of="P1-G1", task="P1", text=dict(sku="TDP-012", title="Mountain Duffel 40L", description="A waterproof duffel made in Colorado and built for every trip, with backpack straps for the walk from the trailhead. Covered by our lifetime warranty.", fiber_content="1000D Cordura", care="", fit="40L", sizes="One size", origin="Imported"), expected_violations=X("LEG-21","LEG-15","MSG-09","LEG-22","LEG-16")),
 dict(id="T-02", twin_of="P1-G2", task="P1", text=dict(sku="TDB-042", title="Topo Designs x Pine Printshop Classic Canvas Tote - Catalog", description="A USA-made canvas tote printed with non-toxic inks 🎨 Built for daily hauls, market runs and weekend trips.", fiber_content="cotton canvas", care="", fit="10L", sizes="One size", origin=""), expected_violations=X("WEB-04","MSG-09","VOI-01","LEG-14","VOI-10")),
 dict(id="T-03", twin_of="E1-G1", task="E1", text=dict(segment="active", subject="Memorial Day deals are back at TopoDesigns", preheader="Our biggest markdowns of the year on packs, bags and layers.", body="Hi there,\n\nThe Memorial Day sale is back with up to 40% off. Every pack comes with a lifetime warranty.", cta="Shop now", terms="Ends soon.", footer="Topo Designs · Unsubscribe · Privacy · Accessibility · © 2026 Topo Designs"), expected_violations=X("MSG-05","MSG-11","LEG-22","LEG-01","LEG-11","VOI-03")),
 dict(id="T-04", twin_of="E1-G2", task="E1", text=dict(segment="lapsed", subject="We are obsessed with this sale, come back", preheader="Up to 50% off select styles, made for anywhere on your map.", body="Hi {first_name|there},\n\nHuge news! Take 50% off everything in our gear lineup! Free shipping over $75!", cta="Find your bag", terms=TERMS, footer=FOOT), expected_violations=X("MSG-06","VOI-12","LEG-12","VOI-24")),
 dict(id="T-05", twin_of="A1-G1", task="A1", text=dict(ad_group="crossbody bags", headlines=["Best Crossbody Bag Ever Made, Period","Made in USA Crossbody Bags","Crossbody Bags for Anywhere","Crossbody Bags for Anywhere","The Mountain Cross Bag","Fits a 14 Inch Laptop","Everyday Carry, Sorted","Recycled Nylon Bags","Town to Trail Crossbody","Free U.S. Shipping $100+","Designed in Colorado","Slim Crossbody Bags","Bike and Commute Bags","Gifts Under $100","Made for Anywhere"], descriptions=["Crossbody bags that carry your daily essentials.","The Mountain Cross Bag keeps a slim profile.","Black Friday: up to 50% off select styles.","Free U.S. shipping on $100+."]), expected_violations=X("DR-01","DR-02","DR-03","LEG-15","MSG-09")),
 dict(id="T-06", twin_of="A1-G2", task="A1", text=dict(ad_group="travel backpacks", headlines=["Better Than Patagonia Packs","Waterproof Travel Packs","OMG Travel Backpacks","Carry-On Ready 🎒✈️","The Rover Pack Classic","Global Travel Backpacks","Laptop Backpacks","Commute to Trailhead","Free U.S. Shipping $100+","Designed in Colorado","Packs for Weekend Trips","Classic Packs Since 2008","Recycled Nylon Packs","Topo Designs Packs","Made for Anywhere"], descriptions=["Travel backpacks with smart organization.","Classic Topo designs in durable materials.","Black Friday: up to 50% off select styles.","Free U.S. shipping on $100+."]), expected_violations=X("MSG-17","LEG-21","VOI-24","VOI-10")),
 dict(id="T-07", task="S1", text=dict(caption="Giveaway time! 🚲🎉🏔️🎒✨🙌 Win a full bike build from Topo and friends. Tag 3 friends to enter. #topodesigns #giveaway", partner=True), expected_violations=X("SOC-06","SOC-01","LEG-06","VOI-10")),
 dict(id="T-08", task="M1", text=dict(text="Topo Designs: take 35% off the Rover Pack Classic, the Mountain Cross Bag and every Global Wool Sweater through Monday night, plus free U.S. shipping on $100+ orders: topo.co/bf", contact={"contact_id": "C-0131", "sms_consent_type": "email only"}), expected_violations=X("LEG-02","EML-08","MSG-06")),
 dict(id="T-09", task="S3", text=dict(caption="Yep, everything is still made in Colorado, eco-friendly and better than Patagonia."), expected_violations=X("LEG-15","MSG-17","VOI-01")),
 dict(id="T-10", task="P1", text=dict(sku="TDP-006", title="Daypack Classic", description="Our classic Daypack, an ideal travel companion and workmate for the daily hike in the hills. Shop now in Bone White, with natural leather lash tabs for extra gear.", fiber_content="recycled nylon", care="", fit="", sizes="One size", origin="Imported"), expected_violations=X("MSG-08","DCO-05","LEG-16")),
]
