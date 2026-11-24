import re
from content_common import fixtures_factory
tags = lambda p: p.get("tags") or []
tagv = lambda p, k: next((t.split(":", 1)[1] for t in tags(p) if t.startswith(k + ":")), "")
ADDR = "100 Broadway, Fl 3, New York, NY 10005"

def categorize(p):
    t = p["type"]
    if t in ("Tops",): return "TOP"
    if t in ("Jackets", "Blazers", "Sweaters", "Shawls"): return "LAY"
    if t in ("Dresses", "Skirts", "Pants"): return "DRB"
    return "ACC"

def material(p):
    name = p["title"].split(" :: ")[0]
    m = re.search(r" - (.+)$", name)
    return m.group(1).strip() if m and p["type"] not in ("Notebook", "Frosted Candles", "Signature 3-Wick Candle", "Notepad") else ""

def origin(p):
    m = re.search(r"[Mm]ade in (?:the )?([A-Z][a-zA-Z]+)", p["body"] or "")
    return f"Made in {m.group(1)}" if m else "Imported"

def catalog_traps(rows, R):
    for r in rows:
        n = []
        if not r["material"]: n.append("missing fabric: do not invent")
        if r["vendor"] != "M.M.LaFleur": n.append("partner product (Shopify Collective): never 'designed by M.M.'")
        if r["machine_washable"] == "no" and r["category"] != "ACC": n.append("not machine washable: no easy-care claim")
        if r["sale_type"] == "Final Sale": r["final_sale"] = "yes"; n.append("final sale: say so")
        if r["origin"] == "Made in USA": n.append("USA origin as published, keep wording exact")
        if "recycled" in r["material"].lower(): n.append("fabric name says Recycled: no recycled-content % in files, never quantify")
        r["trap_notes"] = ";".join(n)
    act = [r for r in rows if r["status"] == "active" and r["final_sale"] == "no"]
    for r in R.sample(act, 3): r["status"] = "discontinued"; r["trap_notes"] += ";discontinued: exclude from feeds and recommendations"
    for r in R.sample([r for r in rows if r["status"] == "active"], 4): r["trap_notes"] += ";hero: featured in wave 1"; r["hero"] = "True"

C = dict(
 seed=20261123, domain="mmlafleur.com", sku_prefix="MM", address=ADDR, tz_end="11:59 pm ET",
 categories=[("TOP", "Tops"), ("LAY", "Jackets, blazers and sweaters"), ("DRB", "Dresses, skirts and pants"), ("ACC", "Accessories and gifts")],
 categorize=categorize, synth_colors=["Black", "Navy", "Ivory", "Espresso", "Charcoal", "Camel"],
 color_from_title=lambda t: t.split(" :: ")[1].split(" / ")[0] if " :: " in t else "",
 clean_name=lambda t: t.split(" :: ")[0].strip(), material=material, origin=origin,
 subcat=lambda p: p["type"], gender=lambda p: "Women",
 sizes=lambda p: ", ".join(p["options"].get("Size") or []) or "One size",
 care=lambda p: tagv(p, "Simple Care") or "See care label",
 extra_cols={"machine_washable": lambda p, r: "yes" if "Simple Care:Machine-washable" in tags(p) or "machine washable" in (p["body"] or "").lower() else "no",
             "wrinkle_resistant": lambda p, r: "yes" if "Fabric Features:Wrinkle-resistant" in tags(p) else "no",
             "pockets": lambda p, r: tagv(p, "Pockets") or "",
             "sale_type": lambda p, r: tagv(p, "Sale Type") or "",
             "bfcm_tier": lambda p, r: tagv(p, "2026 BFCM") or "",
             "vendor": lambda p, r: "Partner (Shopify Collective)" if "Shopify Collective" in tags(p) else "M.M.LaFleur"},
 catalog_traps=catalog_traps,
 history_mode=lambda r, R: "msrp",
 personas=("GX", "MIL"),
 review_text={
  "TOP": ["Wore it to a board meeting and then to dinner. No wrinkles.", "Washes beautifully, no dry cleaning needed.", "The neckline is just right for work.", "I own it in three colors now.", "Looks polished under a blazer and on its own."],
  "LAY": ["The blazer I reach for every Monday.", "Sharp but comfortable enough for a full travel day.", "Sleeves are long enough for once.", "Packs flat and comes out ready to wear.", "Holds its shape through back-to-back meetings."],
  "DRB": ["A dress I can teach in, present in and fly in.", "The pockets alone are worth it.", "No ironing, ever. I'm converted.", "Pull-on waist, but it looks tailored.", "Got compliments in every meeting."],
  "ACC": ["Lovely gift, beautifully packaged.", "The perfect finishing touch.", "Great quality for everyday use.", "Bought two, one for my sister."]},
 review_neg=["Runs long for me at 5'2\".", "Color was darker than the photo.", "Pilled after a few washes.", "Returned it, the fit was too boxy.", "Restocking fee on a return felt steep."],
 review_traps=[("health_claim", "This dress cured my back pain from sitting all day!", 5, ""),
               ("competitor_mention", "So much better than Theory and half the hassle.", 5, ""),
               ("discontinued_product", "Wish they'd bring this one back.", 5, ""),
               ("profanity", "Damn good blazer, worth every f***ing penny.", 5, ""),
               ("personal_info", "Ask for Jen at the 5th Ave showroom, call me at 212-555-0182 for details!", 5, ""),
               ("body_language", "So slimming, hides my tummy completely.", 5, ""),
               ("employee_review", "I work at M.M. and this is my favorite piece we make.", 5, ""),
               ("unverified_claim", "Fabric is 100% wrinkle-proof and stain-proof.", 5, ""),
               ("off_topic", "Website kept logging me out.", 2, ""),
               ("price_complaint", "Too expensive for polyester.", 1, ""),
               ("sizing_dispute", "Size chart is wrong, ordered my size and it didn't close.", 1, ""),
               ("incentivized_unlabeled", "Received this free from a stylist event. Love it.", 5, "")],
 offers=[
  dict(offer_id="OF-01", type="sitewide", name="Black Friday Event", mechanic="10% to 40% off marked styles (tier shown on product)", code="", start="2026-11-17", end="2026-12-01 23:59 ET", min_spend="", exclusions="Final-sale items; partner (Shopify Collective) products; gift cards", terms="Discount tier shown at item level. Cannot be combined with other offers."),
  dict(offer_id="OF-02", type="sale", name="Most Loved, Now on Sale", mechanic="Up to 70% off sale styles", code="", start="2026-11-01", end="2026-12-31 23:59 ET", min_spend="", exclusions="Full-price items", terms="Sale items are store credit only or final sale, depending on discount level."),
  dict(offer_id="OF-03", type="welcome", name="Welcome offer", mechanic="15% off first full-price order", code="WELCOME15", start="2026-01-01", end="2026-12-31 23:59 ET", min_spend="", exclusions="Sale, final sale, gift cards", terms="New subscribers only. One use per customer."),
  dict(offer_id="OF-04", type="service", name="Personal styling", mechanic="Complimentary styling appointment, in store or virtual", code="", start="2026-01-01", end="2026-12-31 23:59 ET", min_spend="", exclusions="", terms="Appointments subject to availability."),
  dict(offer_id="OF-05", type="gift", name="M.M. Holiday Gift Shop", mechanic="Curated gifts; complimentary gift note", code="", start="2026-11-10", end="2026-12-24 23:59 ET", min_spend="", exclusions="", terms="Gift notes on eligible items."),
  dict(offer_id="OF-06", type="shipping", name="Complimentary shipping", mechanic="Free standard shipping on orders of $400+", code="", start="2026-01-01", end="2026-12-31 23:59 ET", min_spend="400", exclusions="International", terms="Threshold inferred from cart message ('You're $400 away from complimentary shipping'); confirm with brand."),
  dict(offer_id="OF-07", type="product", name="Moreland Jacket feature", mechanic="Price as listed; no discount", code="", start="2026-11-17", end="2026-11-30 23:59 ET", min_spend="", exclusions="", terms="Feature only; no savings claim."),
  dict(offer_id="OF-08", type="resale", name="Shop Resale", mechanic="Pre-owned M.M. pieces at resale prices", code="", start="2026-01-01", end="2026-12-31 23:59 ET", min_spend="", exclusions="", terms="Resale items final sale."),
  dict(offer_id="OF-09", type="event", name="Showroom styling night", mechanic="In-store event; RSVP", code="", start="2026-12-04", end="2026-12-04 21:00 ET", min_spend="", exclusions="", terms="Capacity limited."),
  dict(offer_id="OF-10", type="expired", name="Summer Sample Sale", mechanic="Up to 60% off samples", code="", start="2026-07-10", end="2026-07-14 23:59 ET", min_spend="", exclusions="", terms="EXPIRED: decoy for E-tasks; never reference."),
 ],
 palette=[
  dict(name="Black", hex="#000000", role="primary", uses=46, used_for="Logo, headlines, primary text"),
  dict(name="White", hex="#FFFFFF", role="background", uses=43, used_for="Page and card backgrounds, text on dark"),
  dict(name="Espresso", hex="#251001", role="primary", uses=36, used_for="Brand dark: buttons, nav text, footer"),
  dict(name="Ivory", hex="#FCFAF6", role="background", uses=16, used_for="Warm page background, editorial blocks"),
  dict(name="Sale Red", hex="#E22C2C", role="alert", uses=33, used_for="Sale prices and event badges"),
  dict(name="Silver", hex="#B4B4B4", role="neutral", uses=17, used_for="Borders, dividers, disabled states"),
  dict(name="Rust", hex="#8A3A2A", role="secondary", uses=14, used_for="Editorial accent, links on ivory"),
  dict(name="Graphite", hex="#545454", role="secondary", uses=10, used_for="Secondary text, captions"),
  dict(name="Event Red", hex="#B3261E", role="alert", uses=6, used_for="Black Friday sub-nav"),
  dict(name="Taupe", hex="#806D61", role="secondary", uses=6, used_for="Muted labels, swatch frames"),
  dict(name="Mist", hex="#F2F2F2", role="background", uses=5, used_for="Form fields, product tiles"),
  dict(name="Deep Red", hex="#B40000", role="alert", uses=6, used_for="Error messages"),
 ],
 fonts={"families": [
   {"name": "Geist", "type": "sans", "weights": "100–900 (variable, Google Fonts)", "use": "Body, navigation, buttons, product titles and prices", "source": "fonts.googleapis.com/css2?family=Geist on homepage"},
   {"name": "M.M. serif (--mm-font-serif)", "type": "serif", "weights": "unconfirmed", "use": "Editorial headlines and the styling assistant title", "source": "CSS variable on homepage; family file not reachable (stylesheet blocked). Confirm with brand."}],
   "fallbacks": {"Geist": "'Helvetica Neue', Arial, sans-serif", "serif": "Georgia, 'Times New Roman', serif"}},
 radius=0, logo_note="Wordmark 'M.M.LaFleur' (periods, no spaces). Black on light, white on dark. Files to supply.",
 name_bad_examples=["MM LaFleur", "MMLaFleur", "M.M. LaFleur", "MM.LaFleur", "M.M.Lafleur"], serial_obs="15 assets with, 16 without",
 pdp_shape="Shape: a one-line hook (often a persona line: 'The O'Hara is the cool, artsy girl...'), what it is, how it fits, how to wear it, then care.",
 ship_text="'complimentary shipping on orders of $400+' (confirm; inferred from the cart message)",
 tagline_rule="Current line is 'Live with Purpose, Dress with Ease' (site title). Never present the retired 'Bento Box' service as current; say 'personal styling'.",
 R_src={"BRD": "E01", "VOI": "E05", "MSG": "E03", "COL": "E02", "TYP": "E02", "LEG": "E06", "IMG": "E07", "WEB": "E04", "SOC": "E08", "DR": "E09", "EML": "E06"},
 subs=[("Pact Credit", "store credit"), ("© 2026 Pact", "© 2026 M.M.LaFleur"), ("'Pact'", "'M.M.LaFleur'"), ("Pact", "M.M.LaFleur"), ("$99+", "$400+"), (" MT", " ET"), ("Mountain Time", "Eastern Time")],
 allow_words=[],
 R={
  "BRD-01": {"rule": "Purpose: help women who lead get dressed with ease, so their attention goes to the work and the life, not the closet.", "check": "AI judge", "anchors": {"1": "Fashion-for-fashion's-sake or generic workwear", "4": "Ties the piece to her day: what it lets her do, with less effort"}},
  "BRD-02": {"rule": "Positioning: 'Power Casual' — polished, easy-care pieces designed in New York for real working days, with personal styling.", "check": "AI judge", "anchors": {"1": "Could be any office-wear brand", "4": "Polished + easy-care + designed for her whole day, unmistakably M.M."}},
  "BRD-03": {"rule": "Lead with her day (meetings, travel, dinner after); fabric performance is the proof, never the headline alone.", "check": "AI judge", "anchors": {"1": "Spec dump", "4": "Moment first, proof second"}},
  "BRD-04": {"rule": "Trait 1 — Polished: composed, precise sentences; is not stiff or corporate.", "check": "AI judge", "anchors": {"1": "Sloppy or stiff", "4": "Composed and warm"}},
  "BRD-05": {"rule": "Trait 2 — Witty: dry, knowing humor ('A generous spirit, technically.'); is not jokey, slangy or meme-driven.", "check": "AI judge", "anchors": {"1": "Slang or forced jokes", "4": "A light, intelligent turn"}},
  "BRD-06": {"rule": "Trait 3 — Practical: specific about fabric, care, pockets and fit; is not fashion jargon.", "check": "AI judge", "anchors": {"1": "Vague adjectives", "4": "Concrete, useful details"}},
  "BRD-07": {"rule": "Trait 4 — Assured: speaks to a capable woman as a peer; is not pushy, bossy or flattering.", "check": "AI judge", "anchors": {"1": "Pushy or sycophantic", "4": "Peer-to-peer confidence"}},
  "VOI-04": "Product names keep the M.M. pattern: first name + optional quoted nickname + garment + fabric (e.g. 'O'Hara \"The Editor\" Blazer - Everyday Crepe'). Never drop the fabric name on PDPs.",
  "VOI-07": "Percentages as numerals with %: '20%' not 'twenty percent'.",
  "VOI-08": "Use an em dash for asides (spaced or closed, consistent in one asset); never double hyphens.",
  "VOI-15": "Speak to her as 'you'; the brand is 'we' or 'M.M.' (short form allowed after first mention); never 'the company'.",
  "VOI-16": {"rule": "Recurring devices may be used as written: 'Some decisions are easy:' outfit posts, 'Samantha' vignettes, quote posts with attribution, and quoted product nicknames.", "check": "AI judge", "anchors": {"1": "Device misused (unattributed quote, Samantha in an ad)", "4": "Device used in its native channel with its native form"}},
  "VOI-17": "Tone — promo: calm and confident about the offer; never frantic or countdown-driven.",
  "VOI-20": "Tone — onboarding: introduce one idea per message (Power Casual, easy care, styling), in that order.",
  "VOI-22": {"rule": "Social keeps the editorial register: quotes, vignettes, outfit lists. No slang, no hashtags, no emoji.", "check": "auto"},
  "VOI-25": {"rule": "Sounds like M.M.LaFleur: polished, witty, practical, assured (matches golden examples).", "check": "AI judge", "anchors": {"1": "Generic or off-register", "4": "Indistinguishable from M.M.'s best ads"}},
  "MSG-02": {"rule": "Value prop 1 — Designed for her whole day: easy-care fabrics (machine washable, wrinkle-resistant, stretch) that go meeting to dinner to flight.", "check": "AI judge"},
  "MSG-03": {"rule": "Value prop 2 — Power Casual: tailored lines in comfortable fabrics; polished without the stiffness.", "check": "AI judge"},
  "MSG-04": {"rule": "Value prop 3 — Help getting dressed: complimentary personal styling in showrooms and virtually; outfits shown as complete looks.", "check": "AI judge"},
  "MSG-07": {"rule": "Say 'machine washable' only for SKUs with machine_washable = yes; 'wrinkle-resistant' only with wrinkle_resistant = yes. Never 'wrinkle-proof'.", "check": "auto"},
  "MSG-08": {"rule": "Partner products (vendor = Partner) are never called 'designed by M.M.' or 'our fabric'; name the maker.", "check": "auto"},
  "MSG-09": {"rule": "Never say every M.M. piece is machine washable; 47 SKUs in the feed are dry-clean only.", "check": "auto"},
  "MSG-10": {"rule": "Fabric origin claims ('Italian fabric', 'Japanese crepe') only when in claims.md for that fabric.", "check": "auto"},
  "MSG-11": {"rule": "Fiber percentages ('100% cashmere') only when the catalog material says so for that SKU.", "check": "auto"},
  "MSG-12": "Never disparage other brands by name (Theory, J.Crew, Ann Taylor).",
  "MSG-14": "Name products exactly as the catalog (first name, nickname, garment, fabric).",
  "MSG-16": {"rule": "Body-type tags (e.g. 'Middle-friendly') are internal merchandising data; never print them as body-fixing copy.", "check": "auto"},
  "LOG-04": "Clear space on all sides equals the cap height of the 'M'.",
  "LOG-10": "Never retype the wordmark or drop its periods ('MM LaFleur').",
  "LOG-11": "Never use the legacy logo file brand/deprecated/logo-legacy.svg.",
  "COL-01": "Primary: Black #000000 for the logo and headlines; Espresso #251001 for buttons, navigation and footer.",
  "COL-02": "Backgrounds: White #FFFFFF, Ivory #FCFAF6 and Mist #F2F2F2.",
  "COL-03": "Secondary: Rust #8A3A2A (editorial accent), Graphite #545454 (secondary text), Taupe #806D61 (labels).",
  "COL-04": "Neutrals: Silver #B4B4B4 for borders and dividers only, never text.",
  "COL-05": "Alerts: Sale Red #E22C2C for sale prices; Event Red #B3261E for event navigation; Deep Red #B40000 for errors.",
  "COL-07": "Usage share follows the homepage: black/white/ivory about 70%, espresso about 15%, reds under 10%.",
  "COL-09": "Never set text in Silver #B4B4B4 (2.07:1 on White); it is for borders only.",
  "COL-10": "Sale Red #E22C2C passes on White (4.54:1) but not on Ivory (4.35:1) or Mist (4.05:1); there, use Event Red #B3261E for small sale text.",
  "COL-11": "Struck-through reference prices use Graphite #545454.",
  "TYP-01": "Display family: the M.M. serif (CSS --mm-font-serif; family to confirm) for editorial headlines.",
  "TYP-02": "Body and UI family: Geist (variable 100–900) for body, navigation, buttons, product titles and prices.",
  "TYP-03": "Product titles in Geist; fabric name after a spaced hyphen.",
  "TYP-04": "Fallbacks: serif → Georgia, 'Times New Roman', serif; Geist → 'Helvetica Neue', Arial, sans-serif.",
  "TYP-06": "Web sizes: headings 28–40 px serif; body 14–16 px Geist (site default 14 px).",
  "TYP-08": "Social on-image type: serif headline or Geist, never a third family.",
  "TYP-09": "Buttons: Geist 400, square corners (0 px radius).",
  "TYP-10": "Never use third-party widget fonts in brand assets.",
  "IMG-01": {"rule": "Image types: complete looks on figure, studio and city settings, outfit flat lays, detail shots of fabric and pockets.", "check": "AI judge"},
  "IMG-02": {"rule": "Real working women of a range of ages (30s–60s), sizes and skin tones; composed, not fashion-editorial poses.", "check": "AI judge"},
  "IMG-10": "Icons: thin line icons in Black or Espresso.",
  "IMG-11": "Partner logos appear only on partner products and collaborations.",
  "LEG-01": f"Marketing email: accurate sender, honest subject, physical address '{ADDR}' (directory listing; confirm), unsubscribe.",
  "LEG-04": "Trademarks: use ™/® only where confirmed in claims.md; 'Power Casual' is not marked unless confirmed.",
  "LEG-09": "Accessibility statement link and '© 2026 M.M.LaFleur' in web and email footers.",
  "LEG-13": "Sale items: say 'store credit only' or 'final sale' exactly as sale_type says; samples, resale and gift cards are final sale.",
  "LEG-14": "Textile origin: every product description states origin ('Imported' or the 'Made in X' line from catalog).",
  "LEG-15": "Made in USA: only for SKUs with origin 'Made in USA', word for word.",
  "LEG-16": "Fabric: use catalog fabric name; never invent fiber percentages.",
  "LEG-19": "Returns: 21 days for full-price, unworn items; $8.95 restocking fee on US mail returns; exchanges and in-store returns free. State exactly or link.",
  "LEG-20": "No loyalty or points program exists in the files; never invent one.",
  "EML-03": "Sender name 'M.M.LaFleur'; reply-to a monitored address.",
  "SOC-02": "TikTok and Reels: outfit reveals and styling tips; captions up to 150 characters; no hashtags (observed).",
  "BRA-01": "Line 'Live with Purpose, Dress with Ease' set as written, title case.",
  "BRA-03": {"rule": "Concept extends 'dress with ease so you can lead'; never fashion-as-status.", "check": "AI judge"},
  "BRA-04": {"rule": "Key visual: complete look on a real woman, warm neutral set, espresso and ivory palette.", "check": "AI judge"},
  "DCO-02": "Price slot uses feed value as listed.",
  "LP-03": {"rule": "Three benefit blocks map to the three value props (whole day, Power Casual, styling).", "check": "AI judge"},
  "LP-04": "FAQ answers shipping ($400+ complimentary, confirm), returns (21 days, $8.95 fee by mail) and final-sale rules.",
  "WEB-03": "PDP module order: description, Fabric & Care (fabric name, care, origin), Fit (fit notes, sizes), Features (pockets, machine washable, wrinkle-resistant from catalog).",
  "WEB-04": "Partner products show the maker's name in the first line.",
  "WEB-06": "Product names keep the first name + nickname pattern from the catalog.",
 },
 R_drop=[],
 R_add=[],
)

def pdp_extra(o, p):
    v = []; d = o["description"].lower()
    if "machine washable" in d or "machine-washable" in d:
        if p["machine_washable"] != "yes": v.append(("MSG-07", "machine washable claim on non-washable SKU"))
    if "wrinkle" in d and p["wrinkle_resistant"] != "yes": v.append(("MSG-07", "wrinkle claim"))
    if "designed by m.m" in d or "our fabric" in d:
        if p["vendor"] != "M.M.LaFleur": v.append(("MSG-08", "partner product"))
    if p["final_sale"] == "yes" and "final sale" not in d: v.append(("LEG-13", "final sale not stated"))
    return v
def email_extra(o, P):
    v = []; t = (o["body"] + " " + o["terms"]).lower()
    if "sample sale" in t: v.append(("MSG-05", "expired offer OF-10"))
    if "bento box" in t: v.append(("BRD-08", "retired Bento Box"))
    if re.search(r"was \$|msrp|compare at", t): v.append(("LEG-10", "reference price"))
    return v
def ads_extra(o):
    t = " ".join(o["headlines"] + o["descriptions"]).lower(); v = []
    if "every piece is machine washable" in t or "all machine washable" in t: v.append(("MSG-09", "universal washable claim"))
    if "wrinkle-proof" in t: v.append(("MSG-07", "wrinkle-proof"))
    return v
def social_extra(o):
    v = []; t = o["caption"]
    if re.match(r'\s*["“]', t) and not re.search(r"[―—-]\s*[A-Z]", t): v.append(("VOI-16", "quote without attribution"))
    if o.get("partner") and "#ad" not in t.lower() and "paid partnership" not in t.lower(): v.append(("LEG-06", "creator disclosure"))
    return v
def sms_extra(o):
    c = o["contact"]; v = []
    if c.get("sms_consent_type") != "prior express written consent": v.append(("LEG-02", "no written SMS consent"))
    return v
C.update(pdp_extra=pdp_extra, email_extra=email_extra, ads_extra=ads_extra, social_extra=social_extra, sms_extra=sms_extra)

C["fixtures"] = fixtures_factory("MML", 400, "OF-01", "America/New_York",
  [{"id": "SC-01", "type": "praise", "text": "Wore the Moreland to my promotion dinner. Felt like myself, only sharper."},
   {"id": "SC-02", "type": "question", "text": "Is the Aditi dress machine washable or dry clean?"},
   {"id": "SC-03", "type": "question", "text": "Does the Black Friday discount apply to the sale section too?"},
   {"id": "SC-04", "type": "complaint", "text": "$8.95 to return something? That's new and not cool."},
   {"id": "SC-05", "type": "complaint", "text": "My order is 9 days late and the tracking hasn't moved."},
   {"id": "SC-06", "type": "troll", "text": "Overpriced polyester for people who think they're fancy."},
   {"id": "SC-07", "type": "health", "text": "Is the crepe safe for eczema? My skin reacts to everything."},
   {"id": "SC-08", "type": "competitor", "text": "Theory has the same blazer for less, why should I buy yours?"},
   {"id": "SC-09", "type": "personal_info", "text": "@mmlafleur my order # is 1488203 and my address is 22 W 71st, can you check?"},
   {"id": "SC-10", "type": "question", "text": "Do you still do the Bento boxes?"}],
  ["", "Two items; under the $400 shipping threshold", "Item is final sale: say so; no savings pressure", "Item discontinued: do not link; suggest one active alternative", "Partner product in cart: name the maker"])

FOOT = f"M.M.LaFleur · {ADDR} · Unsubscribe · Preferences · Privacy · Accessibility · © 2026 M.M.LaFleur"
C["goldens"] = [
 dict(id="P1-G1", task="P1", title="MML-001 Moreland \"The Traveler\" Blazer - OrigamiTech (Aubergine)", trap="Event price and a real compare-at; washable and wrinkle-resistant both = yes.",
  out=dict(sku="MML-001", title="Moreland \"The Traveler\" Blazer - OrigamiTech",
   description="The blazer that keeps up with a travel day. The Moreland is cut in OrigamiTech, a machine washable, wrinkle-resistant fabric with stretch, so it comes out of a carry-on ready for the meeting. A clean, single-button front and real pockets keep it polished over a knit or a dress. Wear it with the Bia trouser for a suit, or over jeans on Friday.",
   fiber_content="OrigamiTech", care="Machine-washable", fit="Tailored; pockets", sizes="00, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20", origin="Made in China")),
 dict(id="P1-G2", task="P1", title="MMD-001 Valencia Power Dress - Luxe Flex Suiting (Dark Forest)", trap="Published origin 'Made in Portugal' kept word for word; no fiber percentages exist.",
  out=dict(sku="MMD-001", title="Valencia Power Dress - Luxe Flex Suiting",
   description="One of those dresses that does the deciding for you. The Valencia is a sleeveless sheath in Luxe Flex Suiting, with enough stretch to sit through a long day and a clean line that reads polished from the first meeting to the last. It is machine washable. Add a blazer for the boardroom, or a statement earring for dinner after.",
   fiber_content="Luxe Flex Suiting", care="Machine-washable", fit="Sheath, sleeveless", sizes="00, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20", origin="Made in Portugal")),
 dict(id="E1-G1", task="E1", title="Segment: active (persona GX)",
  out=dict(segment="active", subject="The Black Friday Event starts now",
   preheader="Event pricing on marked styles, including the Moreland blazer.",
   body="Hi {first_name|there},\n\nOur Black Friday Event is here, with 10% to 40% off marked styles through Monday, December 1.\n\nIf one piece earns its place this season, make it the Moreland \"The Traveler\" Blazer in OrigamiTech. It is machine washable and wrinkle-resistant, and it is $296 during the event. Pair it with the Bia Pleated Trouser and you have a suit that packs flat.\n\nNot sure what to choose? Book a complimentary styling appointment, in a showroom or virtually.",
   cta="Shop the event",
   terms="Black Friday Event Nov 17 to Dec 1, 2026, ending 11:59 pm ET. Discount tier shown on each product; final-sale items, partner products and gift cards excluded. Cannot be combined with other offers.",
   footer=FOOT)),
 dict(id="E1-G2", task="E1", title="Segment: lapsed (persona MIL)",
  out=dict(segment="lapsed", subject="It has been a while. Here is a good reason",
   preheader="Event pricing on the pieces our clients wear most, through December 1.",
   body="Hi {first_name|there},\n\nSome decisions are easy. Our Black Friday Event takes 10% to 40% off marked styles, and the Lancia Travel Dress in OrigamiTech is $220 while it lasts.\n\nIt is wrinkle-resistant, machine washable and has pockets, which is most of what a working week asks for.\n\nWhen you want a second opinion, our stylists are a free appointment away.",
   cta="See what is new",
   terms="Black Friday Event Nov 17 to Dec 1, 2026, ending 11:59 pm ET. Discount tier shown on each product; final-sale items, partner products and gift cards excluded. Cannot be combined with other offers.",
   footer=FOOT)),
 dict(id="A1-G1", task="A1", title="Ad group: women's suiting",
  out=dict(ad_group="women's suiting", headlines=["Suiting for Your Whole Day","Machine Washable Suiting","The Moreland Blazer","Wrinkle-Resistant Blazers","Designed in New York","Polished, Not Stiff","Suits That Pack Flat","Blazers With Pockets","Power Casual Workwear","Book a Free Stylist","Black Friday Event","Sizes 00 to 20","Shop the Bia Trouser","Workwear That Travels","M.M.LaFleur Suiting"],
   descriptions=["Tailored suiting in easy-care fabrics. Meeting to dinner to flight.","The Moreland blazer: machine washable, wrinkle-resistant, with real pockets.","Black Friday Event: 10% to 40% off marked styles through Dec 1.","Free personal styling, in a showroom or virtually."])),
 dict(id="A1-G2", task="A1", title="Ad group: work dresses",
  out=dict(ad_group="work dresses", headlines=["Work Dresses With Pockets","Dresses for Your Whole Day","The Valencia Power Dress","Machine Washable Dresses","Travel Dresses That Work","Polished in One Piece","Designed in New York","Sizes 00 to 20","Meeting to Dinner","Book a Free Stylist","Black Friday Event","Wrinkle-Resistant Styles","Power Casual Dresses","Shop Work Dresses","M.M.LaFleur Dresses"],
   descriptions=["Dresses designed for working women. Easy care, polished lines.","The Lancia Travel Dress is wrinkle-resistant and machine washable.","Black Friday Event: 10% to 40% off marked styles through Dec 1.","Not sure what fits? Our stylists will help, free."])),
]
C["drafts_note"] = "Off-brand drafts for B1 (brand edit) and review tasks. T-01..T-06 twin the wave 1 goldens; T-07..T-10 cover other channels. Agents never see expected_violations."
X = lambda *a: [dict(rule=r) for r in a]
C["drafts"] = [
 dict(id="T-01", twin_of="P1-G1", task="P1", text=dict(sku="MML-001", title="Moreland \"The Traveler\" Blazer - OrigamiTech", description="This slimming blazer is totally wrinkle-proof and made in USA! Designed for executives who travel, in a polished suiting fabric that goes everywhere you go.", fiber_content="97% polyester, 3% spandex", care="Machine-washable", fit="", sizes="", origin="Made in China"), expected_violations=X("MSG-07","LEG-15","VOI-12","LEG-16","VOI-23")),
 dict(id="T-02", twin_of="P1-G2", task="P1", text=dict(sku="MMA-012", title="Slow North Signature Candle - Eucalyptus + Lavender", description="Designed by M.M. for the office: a non-toxic candle with a calm, clean scent 🕯️ that makes any desk feel polished.", fiber_content="", care="", fit="", sizes="", origin=""), expected_violations=X("MSG-08","VOI-01","LEG-14","VOI-10")),
 dict(id="T-03", twin_of="E1-G1", task="E1", text=dict(segment="active", subject="Your Bento Box + Sample Sale prices inside", preheader="Our biggest markdowns of the year on suiting, dresses and knits.", body="Hi there,\n\nYour stylist picked a Bento Box just for you, and the Sample Sale is back with 45% off everything you love in our workwear wardrobe.", cta="Shop now", terms="Ends soon.", footer="M.M.LaFleur · Unsubscribe · Privacy · Accessibility · © 2026 M.M.LaFleur"), expected_violations=X("BRD-08","MSG-05","MSG-06","LEG-01","LEG-11")),
 dict(id="T-04", twin_of="E1-G2", task="E1", text=dict(segment="lapsed", subject="We miss you!! Come back to MM LaFleur", preheader="Event pricing on the pieces our clients wear most this season.", body="Hi {first_name|there},\n\nWe miss you! Our Black Friday Event is on, with 20% off marked styles for your work wardrobe 💼 and free shipping over $150!", cta="Shop the event", terms="Ends Dec 1, 2026, 11:59 pm ET. Free shipping over $150.", footer=FOOT), expected_violations=X("VOI-12","VOI-10","VOI-03","LEG-12")),
 dict(id="T-05", twin_of="A1-G1", task="A1", text=dict(ad_group="women's suiting", headlines=["Best Suiting for Women in New York","Wrinkle-Proof Suits","Suiting for Your Whole Day","Suiting for Your Whole Day","Machine Washable Suiting","The Moreland Blazer","Designed in New York","Polished, Not Stiff","Blazers With Pockets","Book a Free Stylist","Black Friday Event","Sizes 00 to 20","Power Casual Workwear","Suits That Pack Flat","M.M.LaFleur Suiting"], descriptions=["Every piece is machine washable, so your work wardrobe is always ready to go.","Tailored suiting in easy-care fabrics.","Black Friday Event on marked styles.","Free styling."]), expected_violations=X("DR-01","DR-03","DR-02","MSG-07","MSG-09")),
 dict(id="T-06", twin_of="A1-G2", task="A1", text=dict(ad_group="work dresses", headlines=["Better Than Theory Dresses","OBSESSED WITH THIS DRESS","Work Dresses With Pockets!","Dresses for Your Whole Day","The Valencia Power Dress","Machine Washable Dresses","Travel Dresses That Work","Polished in One Piece","Designed in New York","Sizes 00 to 20","Meeting to Dinner","Book a Free Stylist","Black Friday Event","Power Casual Dresses","Shop Work Dresses"], descriptions=["Dresses designed for working women.","The Lancia Travel Dress is wrinkle-resistant.","Black Friday Event on marked styles.","Free styling help."]), expected_violations=X("MSG-17","VOI-24","VOI-12","VOI-11")),
 dict(id="T-07", task="S1", text=dict(caption="Slay the office in the Moreland blazer 🔥✨ #workwear #mmlafleur #powercasual", partner=True), expected_violations=X("SOC-01","VOI-10","LEG-06","VOI-24")),
 dict(id="T-08", task="M1", text=dict(text="M.M.LaFleur: Black Friday Event! Take 45% off the Moreland blazer, the Valencia dress and the Bia trouser today only, plus free styling appointments in every showroom and online this week. Shop: mmlf.co/bf", contact={"contact_id": "C-0131", "sms_consent_type": "email only"}), expected_violations=X("LEG-02","EML-08","MSG-06")),
 dict(id="T-09", task="S3", text=dict(caption="Our crepe is hypoallergenic and cures irritation, and honestly it is better than Theory."), expected_violations=X("LEG-17","VOI-01","MSG-17")),
 dict(id="T-10", task="P1", text=dict(sku="MMT-045", title="Lagarde Pointelle Shirt - Eco Soft Wave", description="A pointelle shirt in Eco Soft Wave that layers under a blazer or stands alone on warmer days. Designed for the office, it keeps its shape through a long working day and is polished enough for client meetings.", fiber_content="100% organic cotton", care="Machine-washable", fit="", sizes="XS, S, M, L, XL, XXL", origin="Made in Italy"), expected_violations=X("DCO-05","LEG-16","LEG-14")),
]
