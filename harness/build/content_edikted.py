import re
from content_common import fixtures_factory
ADDR = "1327 Willow St, Los Angeles, CA 90013"
FIB = r"(?:Polyester|Spandex|Cotton|Nylon|Rayon|Polyamide|Acrylic|Viscose|Elastane|Wool|Metal|Zinc Alloy|Alloy|Faux Leather|Polyurethane|PU|Lyocell|Modal|Linen|Acetate|Glass|Plastic|Iron|Copper|Brass|Stainless Steel|Rhinestone|Pearl|Faux Fur|Mohair|Cashmere|Leather|Rubber|Acrylic Fiber|Sequin)"
tags = lambda p: p.get("tags") or []

def categorize(p):
    t = p["title"].lower()
    if re.search(r"earring|\bring\b|belt|bag|clip|glove|necklace|warmer|sock|chain|bracelet|hat|scarf|beanie|sunglass|charm|headband|purse|tights|\bbow\b|brooch|tightener", t): return "ACC"
    if re.search(r"sweater|cardigan|hoodie|sweatshirt|jacket|coat|knit|zip|fleece|blazer|vest|shrug|pullover", t): return "OUT"
    if re.search(r"pant|jean|skirt|short|dress|legging|trouser|capri|skort|romper|jumpsuit|\bset\b", t): return "BTM"
    return "TOP"

def material(p):
    m = re.search(rf"({FIB}(?:,\s*{FIB})*)\s+(?:Model|Measurements|Item care)", p["body"] or "")
    return m.group(1) if m else ""
def care(p):
    m = re.search(r"Item care:\s*(.+)$", p["body"] or ""); return m.group(1).strip() if m else ""
def model(p):
    m = re.search(r"(Model wears size \w+)\s*(Model height is [\d'\u2019\"]+)?", p["body"] or ""); return " · ".join(x for x in m.groups() if x) if m else ""
def drop(p):
    d = next((t.split("_")[1] for t in tags(p) if t.startswith("Drop_")), ""); return d

def catalog_traps(rows, R):
    for r in rows:
        n = []
        if r["material"]: n.append("fiber % not published: list fibers only, never invent percentages")
        else: n.append("missing material: do not invent")
        if r["prop65"] == "yes": n.append("Prop 65 warning required on CA-facing PDP")
        if r["drop_date"] and r["drop_date"] > "2026-11-22": r["status"] = "coming_soon"; n.append(f"drops {r['drop_date']}: not shoppable yet")
        if r["warehouse"] == "yes": r["final_sale"] = "yes"; n.append("warehouse sale item: final sale")
        if r["sale_flag"] == "yes": n.append("compare price is a comp value, never charged: no was-price")
        r["trap_notes"] = ";".join(n)
    act = [r for r in rows if r["status"] == "active" and r["final_sale"] == "no"]
    for r in R.sample(act, 3): r["status"] = "discontinued"; r["trap_notes"] += ";discontinued: exclude from feeds and recommendations"
    for r in R.sample([r for r in rows if r["status"] == "active"], 4): r["hero"] = "True"; r["trap_notes"] += ";hero: featured in wave 1"

C = dict(
 seed=20261124, domain="edikted.com", sku_prefix="ED", address=ADDR, tz_end="11:59 pm PT",
 categories=[("TOP", "Tops"), ("OUT", "Sweaters, knits and outerwear"), ("BTM", "Bottoms, dresses and sets"), ("ACC", "Accessories")],
 categorize=categorize, synth_colors=["Black", "White", "Pink", "Brown", "Red", "Gray", "Blue", "Cream"],
 color_from_title=lambda t: "", clean_name=lambda t: t.strip(), material=material,
 origin=lambda p: "Imported", subcat=lambda p: p["type"] if p["type"] != "Unpublished" else "", gender=lambda p: "Women",
 sizes=lambda p: ", ".join(p["options"].get("Size") or []) or "One size", care=care,
 extra_cols={"model_info": lambda p, r: model(p), "prop65": lambda p, r: "yes" if "P65_Message" in tags(p) else "no",
             "drop_date": lambda p, r: drop(p), "warehouse": lambda p, r: "yes" if "Warehouse" in tags(p) else "no",
             "bf_discount": lambda p, r: "60%" if "60discount" in tags(p) else ("0%" if "0discount" in tags(p) else ""),
             "wholesale_partners": lambda p, r: ", ".join(x for x in ("Nordstrom", "Tillys") if x in tags(p))},
 catalog_traps=catalog_traps,
 history_mode=lambda r, R: "comp" if r["sale_flag"] == "yes" else "msrp",
 personas=("GZ", "MIL"),
 review_text={
  "TOP": ["obsessed, wore it out twice this week", "fits like the pic, got so many compliments", "the perfect going out top fr", "cute and actually holds everything in place", "bought it in 2 colors"],
  "OUT": ["so cozy and the color is even better irl", "my new fave sweater, no itch", "oversized in the best way", "wore it to class and got asked where it's from", "perfect layer for fall"],
  "BTM": ["the jeans everyone asks about", "low rise that actually works on me", "perfect length, I'm 5'4", "matching set is so cute", "these fit better than any jeans I own"],
  "ACC": ["tiny but makes the whole fit", "cute gift for my bestie", "doesn't tarnish so far", "obsessed with this clip"]},
 review_neg=["runs small, size up", "color looks different than the photo", "thin fabric, see-through in white", "took 2 weeks to arrive", "zipper broke after a few wears"],
 review_traps=[("health_claim", "this top fixed my posture lol no joke", 5, ""),
               ("competitor_mention", "way better than Shein and Princess Polly", 5, ""),
               ("discontinued_product", "pls restock this", 5, ""),
               ("profanity", "this skirt is f***ing iconic", 5, ""),
               ("personal_info", "dm me @kayla.s.2007 for fit pics", 5, ""),
               ("minor_signal", "got this for my 9th grade homecoming!!", 5, ""),
               ("body_language", "so slimming, hides everything", 5, ""),
               ("unverified_claim", "it's 100% cotton and doesn't shrink", 5, ""),
               ("off_topic", "app keeps crashing at checkout", 2, ""),
               ("comp_value", "says 60% off but it's always this price", 2, ""),
               ("sizing_dispute", "size chart is way off", 1, ""),
               ("incentivized_unlabeled", "got this in my creator PR box, love", 5, "")],
 offers=[
  dict(offer_id="OF-01", type="sitewide", name="Black Friday", mechanic="60% off everything (based on comp value)", code="", start="2026-11-22", end="2026-11-30 23:59 PT", min_spend="", exclusions="Gift cards; warehouse sale items; US only", terms="*Based on comp value. US only. While supplies last."),
  dict(offer_id="OF-02", type="sale", name="Online Warehouse Sale", mechanic="70-80% off items", code="", start="2026-11-01", end="2026-12-31 23:59 PT", min_spend="", exclusions="", terms="Warehouse items are final sale. *Based on comp value."),
  dict(offer_id="OF-03", type="app", name="App offer", mechanic="10% off first app order", code="APP10", start="2026-01-01", end="2026-12-31 23:59 PT", min_spend="", exclusions="Gift cards", terms="App only; one use per customer."),
  dict(offer_id="OF-04", type="shipping", name="Free standard shipping", mechanic="Free standard shipping on orders above $80", code="", start="2026-01-01", end="2026-12-31 23:59 PT", min_spend="80", exclusions="", terms="48 contiguous states; AK, PR, HI also $80+ standard."),
  dict(offer_id="OF-05", type="event", name="Totally Edikted (BF livestream)", mechanic="Content event, no discount of its own", code="", start="2026-11-22", end="2026-11-22 23:59 PT", min_spend="", exclusions="", terms="Campaign line, BF 2026 only."),
  dict(offer_id="OF-06", type="drop", name="New drop", mechanic="New arrivals drop; no discount", code="", start="2026-12-16", end="2026-12-16 23:59 PT", min_spend="", exclusions="", terms="Items not shoppable before drop time."),
  dict(offer_id="OF-07", type="sms", name="SMS sign-up", mechanic="Early access to drops for SMS subscribers", code="", start="2026-01-01", end="2026-12-31 23:59 PT", min_spend="", exclusions="", terms="Requires written SMS consent; 18+."),
  dict(offer_id="OF-08", type="retail", name="In-store event", mechanic="In-store styling event at The Grove", code="", start="2026-12-06", end="2026-12-06 20:00 PT", min_spend="", exclusions="", terms="While capacity lasts."),
  dict(offer_id="OF-09", type="sitewide", name="Pre-BF early access", mechanic="50% off sitewide", code="", start="2026-11-17", end="2026-11-21 23:59 PT", min_spend="", exclusions="Gift cards", terms="ENDED Nov 21: decoy, never reference as live. *Based on comp value."),
  dict(offer_id="OF-10", type="expired", name="Back to School", mechanic="Up to 70% off", code="", start="2026-08-01", end="2026-08-31 23:59 PT", min_spend="", exclusions="", terms="EXPIRED: decoy."),
 ],
 palette=[
  dict(name="Ink", hex="#252424", role="primary", uses=190, used_for="Body text, headlines, borders"),
  dict(name="White", hex="#FFFFFF", role="background", uses=77, used_for="Backgrounds, text on pink and ink"),
  dict(name="Bubblegum", hex="#EC6BAD", role="primary", uses=37, used_for="Primary buttons, sale banners"),
  dict(name="Black", hex="#000000", role="primary", uses=42, used_for="Logo, nav"),
  dict(name="Baby Blue", hex="#BFE1EF", role="background", uses=20, used_for="Promo bars, tiles"),
  dict(name="Soft Pink", hex="#F6A8D0", role="background", uses=7, used_for="Hover and secondary panels"),
  dict(name="Near Black", hex="#100F0D", role="secondary", uses=5, used_for="Overlays"),
  dict(name="Cloud", hex="#ECECEC", role="background", uses=4, used_for="Inputs, dividers"),
  dict(name="Alert Red", hex="#EA1111", role="alert", uses=4, used_for="Errors, low stock"),
  dict(name="Wine", hex="#5B1521", role="secondary", uses=4, used_for="Holiday accents"),
  dict(name="Raspberry", hex="#CD0037", role="alert", uses=4, used_for="Sale price"),
  dict(name="Mint", hex="#E7FAF3", role="background", uses=4, used_for="Success messages"),
 ],
 fonts={"families": [
   {"name": "Obviously Extended", "type": "extended sans (display)", "weights": "Semibold; Medium Italic", "use": "Headlines, nav, promo bars", "source": "self-hosted Obviously-Semibold / Obviously-Extended_Medium_Italic; CSS spells the family 'Obiously Extended'"},
   {"name": "Druk Wide", "type": "wide display sans", "weights": "Heavy; Medium Italic", "use": "Sale numerals and event headlines (e.g. '60% OFF')", "source": "self-hosted Druk_Wide-Heavy-Web"},
   {"name": "Montserrat", "type": "sans", "weights": "Light, Regular, Medium", "use": "Body, product details, buttons", "source": "self-hosted Montserrat-Light/Regular/Medium"},
   {"name": "Adobe kit aab3ogq", "type": "kit", "weights": "", "use": "Loaded on homepage; contents unconfirmed", "source": "use.typekit.net/aab3ogq"}],
   "fallbacks": {"Obviously Extended": "'Arial Black', Arial, sans-serif", "Druk Wide": "Impact, 'Arial Black', sans-serif", "Montserrat": "Arial, sans-serif"}},
 radius=0, logo_note="Wordmark 'EDIKTED' in caps (logo only). Running copy uses 'Edikted', 'EDIKTED' or lowercase 'edikted' (all observed).",
 name_bad_examples=["Edicted", "EDICTED", "Edikted Clothing"], serial_obs="0 assets with, 2 without",
 pdp_shape="Shape: attribute list, one per line (garment, fit, closure, details, fabric name), then fibers, model size and height, then item care. No sentences needed.",
 ship_text="'free standard shipping on orders above $80' (US)",
 tagline_rule="No standing tagline. Campaign line 'Totally Edikted' is BF 2026 only; never invent a tagline.",
 R_src={"BRD": "E01", "VOI": "E05", "MSG": "E03", "COL": "E02", "TYP": "E02", "LEG": "E06", "IMG": "E07", "WEB": "E04", "SOC": "E08", "DR": "E09", "EML": "E06"},
 subs=[("Pact Credit", "store credit"), ("© 2026 Pact", "© 2026 Edikted"), ("'Pact'", "'Edikted'"), ("Pact", "Edikted"), ("$99+", "$80+"), (" MT", " PT"), ("Mountain Time", "Pacific Time")],
 allow_words=["organic cotton", "GOTS", "Fair Trade", "Wine #"],
 R={
  "BRD-01": {"rule": "Purpose: get the outfit she saw on her feed into her closet fast, at a price that doesn't sting.", "check": "AI judge", "anchors": {"1": "Slow, generic fashion talk", "4": "Trend, speed and price in one breath"}},
  "BRD-02": {"rule": "Positioning: trend-led going-out and everyday fits for Gen Z, most under $40, launched in weekly drops and shown on creators first.", "check": "AI judge", "anchors": {"1": "Could be any mall brand", "4": "Unmistakably drop-driven, creator-first Edikted"}},
  "BRD-03": {"rule": "Lead with the fit or the moment (GNO, holiday party, class); price and sale come second unless it is a sale message.", "check": "AI judge"},
  "BRD-04": {"rule": "Trait 1 — Loud: caps-and-emoji bursts on hype words; is not one long all-caps wall.", "check": "AI judge", "anchors": {"1": "Flat or shouting the whole time", "4": "Bursts of caps that land on the right words"}},
  "BRD-05": {"rule": "Trait 2 — Insider: talks like her group chat ('RN', 'fits', 'hits different'); is not dated slang or brand-trying-to-be-cool.", "check": "AI judge"},
  "BRD-06": {"rule": "Trait 3 — Hype: real urgency tied to real dates and drops; is not fake scarcity.", "check": "AI judge"},
  "BRD-07": {"rule": "Trait 4 — Playful and flirty: fun, confident, a wink; is not sexualized and never body-shaming.", "check": "AI judge"},
  "VOI-04": "Product names keep Edikted's pattern: a first name + descriptors + garment (e.g. 'Cecilya Bandage Mini Dress'). Never drop the first name.",
  "VOI-07": "Percentages as numerals: '60% OFF', not 'sixty percent'.",
  "VOI-08": "Ellipses and line breaks are allowed for teasers ('tune in TOMORROW…'); no double hyphens.",
  "VOI-15": "Speak to her as 'you' or 'babe'; the brand is 'we'/'us' ('Thank Us Later').",
  "VOI-16": {"rule": "Sale copy always pairs the savings with '*Based on comp value' and, for US-only offers, '*US only'.", "check": "auto"},
  "VOI-17": "Tone — promo: hype, caps on the number and the event, 1–5 emoji; never threatening ('you'll regret it').",
  "VOI-20": "Tone — onboarding: welcome to the crew, app code APP10, how drops work.",
  "VOI-22": {"rule": "Social uses current internet phrasing already in brand use ('RN', 'hits different', 'GNO', 'cozy babes'); always #EDIKTED.", "check": "auto"},
  "VOI-25": {"rule": "Sounds like Edikted: loud, insider, hype, playful (matches golden examples).", "check": "AI judge"},
  "MSG-02": {"rule": "Value prop 1 — The trend, now: weekly drops of what's on her feed.", "check": "AI judge"},
  "MSG-03": {"rule": "Value prop 2 — Prices that don't sting: most pieces under $40 (catalog median $26).", "check": "AI judge"},
  "MSG-04": {"rule": "Value prop 3 — Seen on creators: fit shown on real creators; model size and height on every PDP.", "check": "AI judge"},
  "MSG-07": {"rule": "Never print fiber percentages; the catalog lists fibers only.", "check": "auto"},
  "MSG-08": {"rule": "Items with status coming_soon are teased ('drops 12/16'), never 'shop now'.", "check": "auto"},
  "MSG-09": {"rule": "'Everything' or 'sitewide' only when the offer has no item exclusions (OF-01 excludes warehouse items and gift cards: say 'everything*' with the exclusion line).", "check": "auto"},
  "MSG-10": {"rule": "Savings claims carry '*Based on comp value'; never show a struck 'was' price unless msrp_comparison_allowed = yes.", "check": "auto"},
  "MSG-11": {"rule": "Never call anything sustainable, eco or ethical; Edikted makes no sustainability claims.", "check": "auto"},
  "MSG-12": "Never name competitors (Shein, Princess Polly, Brandy Melville) in owned copy.",
  "MSG-14": "Name products exactly as the catalog.",
  "MSG-16": {"rule": "Prop 65: PDPs for prop65 = yes SKUs carry the CA warning line; never claim 'non-toxic'.", "check": "auto"},
  "LOG-04": "Clear space equals the height of the 'E'.",
  "LOG-10": "The wordmark is always caps EDIKTED; never retype it in another font.",
  "LOG-11": "Never use brand/deprecated/logo-legacy.svg.",
  "COL-01": "Primary: Ink #252424 for text and borders; Bubblegum #EC6BAD for primary buttons and sale banners; Black #000000 for the logo.",
  "COL-02": "Backgrounds: White #FFFFFF, Baby Blue #BFE1EF, Soft Pink #F6A8D0, Cloud #ECECEC, Mint #E7FAF3.",
  "COL-03": "Secondary: Wine #5B1521 for holiday accents; Near Black #100F0D for overlays.",
  "COL-04": "Pink-on-pink is decoration only; never text.",
  "COL-05": "Alerts: Raspberry #CD0037 for sale prices; Alert Red #EA1111 for errors.",
  "COL-07": "Usage share follows the homepage: ink and white about 70%, bubblegum about 10%, pastels about 10%, alerts under 3%.",
  "COL-09": "Button text on Bubblegum #EC6BAD is Ink #252424 (5.36:1); White on Bubblegum fails (2.89:1).",
  "COL-10": "Alert Red #EA1111 passes on White (4.58:1) but never on Soft Pink (2.49:1) or Baby Blue (3.32:1).",
  "COL-11": "No struck-through comp prices unless msrp_comparison_allowed = yes (see MSG-10).",
  "TYP-01": "Display: Obviously Extended (Semibold, Medium Italic) for headlines and nav.",
  "TYP-02": "Body and UI: Montserrat (Light, Regular, Medium).",
  "TYP-03": "Event numerals and sale headlines: Druk Wide (Heavy, Medium Italic).",
  "TYP-04": "Fallbacks: Obviously Extended → 'Arial Black', Arial; Druk Wide → Impact; Montserrat → Arial.",
  "TYP-06": "Web sizes: promo headings 28–48 px Obviously Extended; body 13–14 px Montserrat.",
  "TYP-08": "Social on-image: Druk Wide or Obviously Extended for the number, Montserrat for small print.",
  "TYP-09": "Buttons: Montserrat Medium, uppercase allowed, square corners.",
  "TYP-10": "Never use third-party widget fonts in brand assets.",
  "IMG-01": {"rule": "Image types: creators and models in flash photography, mirror selfies, night-out scenes, street style, TV-show sets for campaigns.", "check": "AI judge"},
  "IMG-02": {"rule": "Real-feeling Gen Z women, a range of bodies and skin tones; confident, never sexualized poses.", "check": "AI judge"},
  "IMG-10": "Icons: bold filled icons in Ink.",
  "IMG-11": "Creator handles shown only with their partnership disclosed.",
  "LEG-01": f"Marketing email: accurate sender, honest subject, physical address '{ADDR}' (directory listing; confirm), unsubscribe.",
  "LEG-04": "Trademark symbols only where confirmed in claims.md.",
  "LEG-09": "Accessibility statement link and '© 2026 Edikted' in web and email footers.",
  "LEG-13": "Warehouse sale items: 'Final sale' wherever they appear.",
  "LEG-14": "Textile origin: 'Imported' on every product description.",
  "LEG-15": "Never claim Made in USA.",
  "LEG-16": "Fiber content: list fibers in catalog order; never invent percentages.",
  "LEG-19": "Returns: link the returns policy; never state a window not in the files.",
  "LEG-20": "No loyalty program in the files; never invent points.",
  "EML-03": "Sender name 'Edikted'; reply-to a monitored address.",
  "SOC-02": "TikTok: hook in the first second; 1–3 hashtags incl. #EDIKTED; creator posts carry #ad or the paid-partnership label.",
  "BRA-01": "Campaign line 'Totally Edikted' (BF 2026) set as written; no standing tagline.",
  "BRA-03": {"rule": "Concept: a show, a drop, a moment ('LIGHTS, CAMERA, BLACK FRIDAY'); never a lecture.", "check": "AI judge"},
  "BRA-04": {"rule": "Key visual: flash-lit creator in the hero fit, bubblegum and ink, a big Druk Wide number.", "check": "AI judge"},
  "DCO-02": "Price slot uses feed price; comp slot only per DCO-03.",
  "LP-03": {"rule": "Three blocks: the drop, the price, the creators wearing it.", "check": "AI judge"},
  "LP-04": "FAQ answers shipping ($80+ free standard), returns (link) and US-only offers.",
  "WEB-03": "PDP module: attribute lines, fibers, model size/height, item care, Prop 65 line where flagged.",
  "WEB-04": "Model info line exactly as catalog model_info.",
  "WEB-06": "Product names keep the first-name pattern from the catalog.",
 },
 R_drop=[], R_add=[],
)

def pdp_extra(o, p):
    v = []; d = (o["description"] + " " + o.get("fiber_content", "")).lower()
    if re.search(r"\d+%\s*(cotton|polyester|spandex|nylon|rayon)", d): v.append(("MSG-07", "fiber percentages"))
    if p["prop65"] == "yes" and "prop 65" not in (o.get("warnings", "") + o["description"]).lower(): v.append(("MSG-16", "Prop 65 line missing"))
    if p.get("model_info") and o.get("model_info") != p["model_info"]: v.append(("WEB-04", "model info"))
    if p["final_sale"] == "yes" and "final sale" not in d: v.append(("LEG-13", "final sale"))
    return v
def email_extra(o, P):
    v = []; t = (o["subject"] + " " + o["body"] + " " + o["terms"]).lower()
    if re.search(r"\d+% (off|on)", t) and "comp value" not in t: v.append(("MSG-10", "no comp value line"))
    if "50% off sitewide" in t or "back to school" in t: v.append(("MSG-05", "ended offer"))
    if re.search(r"~~|was \$|reg\. \$", t): v.append(("LEG-10", "was price"))
    return v
def ads_extra(o):
    t = " ".join(o["headlines"] + o["descriptions"]).lower(); v = []
    if re.search(r"\d+% off", t) and "comp value" not in t: v.append(("MSG-10", "savings without comp value"))
    if re.search(r"sustainab|\beco\b|ethical", t): v.append(("MSG-11", "sustainability claim"))
    return v
def social_extra(o):
    t = o["caption"].lower(); v = []
    if o.get("partner") and not re.search(r"#ad\b|paid partnership", t): v.append(("LEG-06", "creator disclosure"))
    if re.search(r"\d+% off", t) and "comp value" not in t: v.append(("MSG-10", "savings without comp value"))
    if re.search(r"\bfree\b.*\bgiveaway|\bgiveaway\b", t) and "rules" not in t: v.append(("SOC-06", "giveaway terms"))
    return v
def sms_extra(o):
    c = o["contact"]; v = []
    if c.get("sms_consent_type") != "prior express written consent": v.append(("LEG-02", "no written SMS consent"))
    if c.get("age_band") == "13-17" or c.get("edge_case", "").startswith("under 18"): v.append(("LEG-02", "under 18"))
    return v
C.update(pdp_extra=pdp_extra, email_extra=email_extra, ads_extra=ads_extra, social_extra=social_extra, sms_extra=sms_extra)
C["fixtures"] = fixtures_factory("EDK", 80, "OF-01", "America/Los_Angeles",
  [{"id": "SC-01", "type": "praise", "text": "the cecilya dress hit SO hard at my bday 😍"},
   {"id": "SC-02", "type": "question", "text": "does the 60% off work on the warehouse stuff too??"},
   {"id": "SC-03", "type": "question", "text": "do u ship to canada"},
   {"id": "SC-04", "type": "complaint", "text": "it says 60% off but it's literally always this price 🙄"},
   {"id": "SC-05", "type": "complaint", "text": "ordered 2 weeks ago still nothing"},
   {"id": "SC-06", "type": "troll", "text": "fast fashion trash lol"},
   {"id": "SC-07", "type": "minor", "text": "im 15 can i still get the text discounts"},
   {"id": "SC-08", "type": "competitor", "text": "same top is $8 on shein"},
   {"id": "SC-09", "type": "personal_info", "text": "@edikted order 4419920 my email is maddie.r@example.com pls help"},
   {"id": "SC-10", "type": "question", "text": "is the new drop on 12/16 at midnight?"}],
  ["", "Two items; check $80 threshold", "Warehouse item: final sale", "Discontinued item: suggest one active alternative", "Coming-soon item in wishlist: tease the drop date, no 'shop now'"])


FOOT = f"Edikted · {ADDR} · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 Edikted"
TERMS = "*Based on comp value. 60% off all items Nov 22-30, 2026, ending 11:59 pm PT, except warehouse sale items and gift cards. US only. While supplies last."
C["goldens"] = [
 dict(id="P1-G1", task="P1", title="EDT-001 Nogi Overlap V Neck Long Sleeve Top (BLACK)", trap="Fibers listed without percentages; comp value not shown as a was-price.",
  out=dict(sku="EDT-001", title="Nogi Overlap V Neck Long Sleeve Top",
   description="Long sleeve top\nOverlap V neckline\nSlim fit\nSoft stretch jersey, made for layering under every fit\nCotton, Spandex\nModel wears size S · Model height is 5’7\nItem care: Machine wash at maximum 30ºC, do not bleach, tumble dry low, iron at a maximum of 110ºC, do not dry clean",
   fiber_content="Cotton, Spandex", model_info="Model wears size S · Model height is 5’7", sizes="XS, S, M, L, XL", origin="Imported", warnings="")),
 dict(id="P1-G2", task="P1", title="EDA-011 Rounded Textured Brooch (GOLD)", trap="Prop 65 line required; no material in catalog, so none is written.",
  out=dict(sku="EDA-011", title="Rounded Textured Brooch",
   description="Brooch\nRounded textured design\nGold-tone finish\nPin it on a blazer, bag or beanie\nItem care: Avoid direct contact with perfume, soap or creams\nWARNING: This product can expose you to chemicals known to the State of California to cause cancer or reproductive harm. Prop 65 info at P65Warnings.ca.gov.",
   fiber_content="", model_info="", sizes="OS", origin="Imported", warnings="Prop 65")),
 dict(id="E1-G1", task="E1", title="Segment: active (persona GZ)",
  out=dict(segment="active", subject="BLACK FRIDAY IS LIVE 🖤 60% OFF your faves*",
   preheader="The biggest sale of the year is here. Check out your cart RN.",
   body="Hey babe 🖤\n\nBLACK FRIDAY IS LIVE. Take 60% OFF your faves* and shop the fits you've been saving 💥\n\nThe Cecilya Bandage Mini Dress for GNO, cozy knits for the holidays, new sets for every plan.\n\nFree standard shipping on orders above $80. Thank us later 💋",
   cta="Shop the sale", terms=TERMS, footer=FOOT)),
 dict(id="E1-G2", task="E1", title="Segment: lapsed (persona MIL)",
  out=dict(segment="lapsed", subject="It's been a minute. 60% OFF your faves*",
   preheader="Our biggest sale of the year is live, with new fits for every plan.",
   body="Hi {first_name|babe} ✨\n\nWe saved you a spot. Black Friday is live with 60% OFF your faves*.\n\nNew knits, going out tops and matching sets just dropped. Grab your fits before they're gone.\n\nNew to the app? Use APP10 for 10% off your first app order.",
   cta="Shop new fits", terms=TERMS + " APP10: 10% off first app order, app only, one use per customer.", footer=FOOT)),
 dict(id="A1-G1", task="A1", title="Ad group: going out tops",
  out=dict(ad_group="going out tops", headlines=["Going Out Tops RN","Black Friday Is Live","60% OFF Your Faves*","Corset Tops for GNO","New Drops Every Week","Shop Edikted Tops","Fits You Saw on TikTok","Lace Tops Under $30","Strapless Tops for Fall","Holiday Party Fits","Free Shipping Over $80","Your Next GNO Fit","Satin Tops That Hit","The BIGGEST Sale","Thank Us Later"],
   descriptions=["BLACK FRIDAY: 60% off your faves*. *Based on comp value. US only.","Going out tops for every plan. New drops every week.","Corsets, lace and satin tops you saw on your feed.","Free standard shipping on orders above $80."])),
 dict(id="A1-G2", task="A1", title="Ad group: baggy jeans",
  out=dict(ad_group="baggy jeans", headlines=["Baggy Jeans RN","Low Rise Baggy Jeans","Black Friday Is Live","60% OFF Your Faves*","Wide Leg Jeans","Jeans for Every Fit","Shop Edikted Denim","New Denim Drops","Jeans Under $50","The Jeans Everyone Asks About","Free Shipping Over $80","Baggy Fits for Fall","Holiday Fits RN","The BIGGEST Sale","Thank Us Later"],
   descriptions=["BLACK FRIDAY: 60% off your faves*. *Based on comp value. US only.","Low rise, baggy and wide leg jeans for every fit.","The denim you saw on your feed. New drops every week.","Free standard shipping on orders above $80."])),
]
C["drafts_note"] = "Off-brand drafts for B1 (brand edit) and review tasks. T-01..T-06 twin the wave 1 goldens; T-07..T-10 cover other channels. Agents never see expected_violations."
X = lambda *a: [dict(rule=r) for r in a]
C["drafts"] = [
 dict(id="T-01", twin_of="P1-G1", task="P1", text=dict(sku="EDT-001", title="Nogi Overlap V Neck Long Sleeve Top", description="Long sleeve top\nScoop neckline\nSustainable cotton jersey, made in USA\n95% cotton, 5% spandex\nModel wears size M\nItem care: Machine wash cold", fiber_content="95% cotton, 5% spandex", model_info="Model wears size M", sizes="XS, S, M, L, XL", origin="Imported"), expected_violations=X("MSG-07","LEG-16","WEB-04","LEG-15","LEG-18")),
 dict(id="T-02", twin_of="P1-G2", task="P1", text=dict(sku="EDA-011", title="Rounded Textured Brooch", description="Brooch\nRounded textured design\nNon-toxic gold-tone finish ✨\nItem care: Avoid perfume", fiber_content="", model_info="", sizes="OS", origin="", warnings=""), expected_violations=X("MSG-16","VOI-01","LEG-14","VOI-10")),
 dict(id="T-03", twin_of="E1-G1", task="E1", text=dict(segment="active", subject="50% OFF SITEWIDE starts NOW at Edicted 🖤", preheader="The biggest sale of the year is here. Check out your cart RN.", body="Hey babe 🖤\n\n50% OFF SITEWIDE is happening RN 💥 Shop the fits you've been saving!", cta="Shop now", terms="Ends soon. US only.", footer="Edikted · Unsubscribe · Privacy · Accessibility · © 2026 Edikted"), expected_violations=X("MSG-05","MSG-10","LEG-01","LEG-11","VOI-03")),
 dict(id="T-04", twin_of="E1-G2", task="E1", text=dict(segment="lapsed", subject="A timeless investment piece for you", preheader="Our biggest sale of the year is live, with new fits for every plan.", body="Hi there,\n\nThe Cecilya dress is a timeless investment piece, was $54, now $21.60.\n\nFree shipping on orders over $50.", cta="Shop new fits", terms=TERMS, footer=FOOT), expected_violations=X("VOI-10","VOI-24","LEG-10","LEG-12")),
 dict(id="T-05", twin_of="A1-G1", task="A1", text=dict(ad_group="going out tops", headlines=["Best Going Out Tops in LA Right Now","Sustainable Party Tops","Black Friday Is Live","Black Friday Is Live","Corset Tops for GNO","New Drops Every Week","Shop Edikted Tops","Fits You Saw on TikTok","Lace Tops Under $30","Strapless Tops for Fall","Holiday Party Fits","Free Shipping Over $80","Your Next GNO Fit","Satin Tops That Hit","Thank Us Later"], descriptions=["60% off everything for BLACK FRIDAY. Shop the fits RN.","Going out tops for every plan.","Corsets, lace and satin tops.","Free standard shipping on orders above $80."]), expected_violations=X("DR-01","DR-03","DR-02","MSG-11","LEG-18","MSG-10")),
 dict(id="T-06", twin_of="A1-G2", task="A1", text=dict(ad_group="baggy jeans", headlines=["Better Than Shein Jeans","Polished Denim for Work","Baggy Jeans RN!!!!","Hypoallergenic Denim","Low Rise Baggy Jeans","Wide Leg Jeans","Jeans for Every Fit","Shop Edikted Denim","New Denim Drops","Jeans Under $50","Free Shipping Over $80","Baggy Fits for Fall","Holiday Fits RN","The BIGGEST Sale","Thank Us Later"], descriptions=["Low rise, baggy and wide leg jeans for every fit.","The denim you saw on your feed.","New drops every week.","Free standard shipping on orders above $80."]), expected_violations=X("MSG-17","VOI-24","VOI-12","VOI-01","LEG-17")),
 dict(id="T-07", task="S1", text=dict(caption="obsessed with my new fit from edikted 🖤💋🔥✨🎀🛍️💥 60% off everything rn", partner=True), expected_violations=X("LEG-06","SOC-01","MSG-10","VOI-10")),
 dict(id="T-08", task="M1", text=dict(text="EDIKTED: BLACK FRIDAY IS LIVE 🖤 Take 45% OFF the Cecilya Bandage Mini Dress, the Michel jeans and every knit RN, plus early access to the 12/16 drop: edk.to/bf", contact={"contact_id": "C-0101", "age_band": "13-17", "sms_consent_type": ""}), expected_violations=X("LEG-02","EML-08","MSG-06")),
 dict(id="T-09", task="S3", text=dict(caption="our cotton cures acne and helps eczema babe, way better than Shein #EDIKTED"), expected_violations=X("VOI-01","LEG-17","MSG-17")),
 dict(id="T-10", task="P1", text=dict(sku="EDT-015", title="Welbie Layered Long Sleeve T Shirt", description="Layered top, shop now\nStripe print\nModel wears size XS\nItem care: Hand wash", fiber_content="100% Cotton", model_info="Model wears size XS", sizes="XS, S, M, L, XL", origin="Imported"), expected_violations=X("DCO-05","LEG-16","WEB-04")),
]
