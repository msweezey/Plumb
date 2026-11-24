"""Build Pact harness data files (synthetic, modeled on Pact's public range, Nov 2026)."""
import csv, json, random, os, datetime as dt

OUT = "/home/claude/pact/out"
os.makedirs(OUT, exist_ok=True)
R = random.Random(20261122)

# ---------- styles (names and list prices modeled on public listings, E07/E10) ----------
# (style_code, name, category, subcategory, gender, material, fit, care, msrp, sizes, colors, hero)
OC = "100% GOTS-certified organic cotton"
OCE5 = "95% GOTS-certified organic cotton, 5% elastane"
OCE8 = "92% GOTS-certified organic cotton, 8% elastane"
SOCK = "78% GOTS-certified organic cotton, 20% recycled nylon, 2% elastane"
CW = "Machine wash cold, tumble dry low"
CWH = "Machine wash cold, hang dry to keep shape"
WARM = "Machine wash warm, tumble dry low"
WS = "XS-2XL"; MS = "S-2XL"; ONE = "One size"
BED = "Twin, Full, Queen, King"

styles = [
 # Women's apparel (WOM) - 50 SKUs
 ("W13","Organic Fit & Flare Wrap Dress","WOM","Dresses","Women",OCE5,"Relaxed through waist, midi length",CW,98,WS,["Black","Navy","Juniper Canopy Sky","Windsor Wine Floral Haze"],True),
 ("WFU","Organic Fit & Flare V-Neck Twist Dress","WOM","Dresses","Women",OCE5,"Fitted bodice, flared skirt",CW,88,WS,["Black","Plum"],False),
 ("WFD","Organic Fit & Flare Three Quarter Sleeve Ballet Dress","WOM","Dresses","Women",OCE5,"Fitted bodice, knee length",CW,88,WS,["Cacao","Black"],False),
 ("WGL","Organic On The Go-To Legging","WOM","Bottoms","Women",OCE8,"High rise, ankle length",CWH,40,WS,["Black","Charcoal Heather","Espresso"],True),
 ("WGP","Organic On The Go-To Pocket Legging","WOM","Bottoms","Women",OCE8,"High rise, side pockets",CWH,48,WS,["Black","Heather Navy"],False),
 ("WGB","Organic On The Go-To Contour Bootcut Legging","WOM","Bottoms","Women",OCE8,"High rise, bootcut",CWH,52,WS,["Black","Sesame"],False),
 ("WTW","Organic All-Day Twill Wide Leg Pant","WOM","Bottoms","Women",OC,"High rise, wide leg",CW,78,WS,["Espresso","Plum","Black"],False),
 ("WLE","Organic Luxe Essential Crewneck Tee","WOM","Tops","Women",OCE5,"Relaxed",CW,30,WS,["White","Black","Sesame"],True),
 ("WPR","Organic Perfect Rib Long Sleeve Tee","WOM","Tops","Women",OCE5,"Slim",CW,40,WS,["Black","Oatmeal Heather"],False),
 ("WCK","Organic CloudKnit Raglan Crew","WOM","Tops","Women",OC,"Relaxed",WARM,68,WS,["Charcoal Heather","Bone"],False),
 ("WPV","Organic Pure Velour Cozy Pullover","WOM","Tops","Women",OC,"Relaxed",CW,78,WS,["Espresso","Juniper"],False),
 ("WWF","Organic Luxe Waffle Knit V-Neck Top","WOM","Tops","Women",OC,"Relaxed",CW,58,WS,["Bone","Navy"],False),
 ("WEC","Organic Essential Cardigan","WOM","Sweaters","Women",OC,"Relaxed, hip length",CWH,98,WS,["Charcoal Heather","Oatmeal"],False),
 ("WWS","Organic Luxe Waffle Set","WOM","Sets","Women",OC,"Relaxed",CW,146,WS,["Bone","Espresso"],False),
 ("WSR","Organic Staycation Short Robe","WOM","Sleep & Lounge","Women",OC,"Relaxed, belted",WARM,68,"XS/S, M/L, XL/2XL",["White"],False),
 # Underwear & bras (UND) - 50 SKUs
 ("WEB3","Organic Everyday Classic Fit Bikini 3-Pack","UND","Women's Underwear","Women",OCE5,"Mid rise, full coverage",CW,30,"XS-3XL",["Sesame","Black","Neutral Mix"],True),
 ("WEB5","Organic Everyday Classic Fit Bikini 5-Pack","UND","Women's Underwear","Women",OCE5,"Mid rise, full coverage",CW,48,"XS-3XL",["Black","Neutral Mix"],False),
 ("WHB5","Organic Everyday High Rise Brief 5-Pack","UND","Women's Underwear","Women",OCE5,"High rise, full coverage",CW,49,"XS-3XL",["Black & White Edit","Neutral Mix"],False),
 ("WSD","Organic Swiss Dot Bikini","UND","Women's Underwear","Women",OCE5,"Mid rise, moderate coverage",CW,13,"XS-2XL",["Sesame","Black","Rose"],False),
 ("WLW3","Organic Lace Waist Brief 3-Pack","UND","Women's Underwear","Women",OCE5,"Mid rise, lace waistband",CW,34,"XS-2XL",["Black","Core Patterns"],False),
 ("WLT3","Organic Lace Waist Thong 3-Pack","UND","Women's Underwear","Women",OCE5,"Low rise, minimal coverage",CW,30,"XS-2XL",["Black","Sesame"],False),
 ("WCS","Organic Everyday Classic Set","UND","Bras & Sets","Women",OCE5,"Wireless, light support",CW,42,"XS-2XL",["Black","Sesame"],False),
 ("WBT","Organic Everyday Barely There Set","UND","Bras & Sets","Women",OCE5,"Wireless, light support",CW,42,"XS-2XL",["Black","Sesame"],False),
 ("WLI","Organic Lace Icon Set","UND","Bras & Sets","Women",OCE5,"Wireless, lace trim",CW,49,"XS-2XL",["Black","Rose"],False),
 ("WMH","Organic Maternity Fold-Over Hipster 3-Pack","UND","Women's Underwear","Women",OCE5,"Fold-over waist",CW,36,"XS-2XL",["Assorted"],False),
 ("MBB4","Organic Everyday Boxer Brief 4-Pack","UND","Men's Underwear","Men",OCE5,"Fitted, 4.5 in inseam",CW,48,MS,["Black","Heather Grey","Everyday Stripe"],True),
 ("MXB4","Organic Everyday Extended Boxer Brief 4-Pack","UND","Men's Underwear","Men",OCE5,"Fitted, 7 in inseam",CW,72,MS,["Black","Castor Green"],False),
 ("MKB4","Organic Everyday Knit Boxer 4-Pack","UND","Men's Underwear","Men",OC,"Relaxed",CW,48,MS,["Assorted Stripe"],False),
 ("WSK3","Organic Everyday Crew Sock 3-Pack","UND","Socks","Women",SOCK,"Crew height",CW,24,"S/M, M/L",["Neutral Mix","Black"],False),
 ("WSK6","Organic No-Show Sock 6-Pack","UND","Socks","Women",SOCK,"No-show",CW,36,"S/M, M/L",["Neutral Mix"],False),
 # Men's apparel & socks (MEN) - 50 SKUs
 ("MSC","Organic Softspun Crew Tee","MEN","Tops","Men",OC,"Standard",CW,30,MS,["White","Black","Heather Grey","Navy"],True),
 ("MSV","Organic Softspun V-Neck Tee","MEN","Tops","Men",OC,"Standard",CW,30,MS,["White","Heather Grey"],False),
 ("MLC","Organic Softspun Long Sleeve Crew","MEN","Tops","Men",OC,"Standard",CW,38,MS,["Black","Navy","Oatmeal Heather"],False),
 ("MHP","Organic Downtime Pullover Hoodie","MEN","Fleece","Men",OC,"Relaxed",WARM,78,MS,["Charcoal Heather","Navy"],False),
 ("MJG","Organic Downtime Jogger","MEN","Bottoms","Men",OC,"Relaxed, tapered",WARM,68,MS,["Charcoal Heather","Black"],False),
 ("MPS","Organic Lounge Pajama Set","MEN","Sleep & Lounge","Men",OC,"Relaxed",CW,88,MS,["Navy Plaid"],False),
 ("MPL","Organic Pique Polo","MEN","Tops","Men",OC,"Standard",CW,48,MS,["Navy","White"],False),
 ("MCH","Organic Stretch Chino Short","MEN","Bottoms","Men",OCE5,"Standard, 7 in inseam",CW,58,"28-40",["Khaki","Navy"],False),
 ("MSK3","Organic Everyday Crew Sock 3-Pack","MEN","Socks","Men",SOCK,"Crew height",CW,24,"M/L, L/XL",["Neutral Mix","Black"],False),
 ("MSK6","Organic Everyday Ankle Sock 6-Pack","MEN","Socks","Men",SOCK,"Ankle height",CW,36,"M/L, L/XL",["Neutral Mix"],False),
 ("MWS","Organic Wool-Blend Hiking Sock","MEN","Socks","Men","60% GOTS-certified organic cotton, 25% recycled wool, 13% recycled nylon, 2% elastane","Crew height",CWH,18,"M/L, L/XL",["Forest","Charcoal"],False),
 ("MCF","Organic Cotton Flannel Shirt","MEN","Tops","Men",OC,"Standard",CW,78,MS,["Red Check","Grey Check"],False),
 # Home (HOM) - 50 SKUs
 ("HSS","Organic Room Service Sateen Sheet Set","HOM","Sheets","Home","100% GOTS-certified organic cotton sateen, 300 thread count","Deep pocket fits up to 16 in mattress",WARM,146,BED,["White","Bone","Cottage Stripe"],True),
 ("HPS","Organic Cool-Air Percale Sheet Set","HOM","Sheets","Home","100% GOTS-certified organic cotton percale, 200 thread count","Deep pocket fits up to 16 in mattress",WARM,148,BED,["White","Quarry","Cottage Stripe"],False),
 ("HJS","Organic Favorite Tee Jersey Sheet Set","HOM","Sheets","Home",OC + " jersey","Deep pocket fits up to 16 in mattress",WARM,98,BED,["Heather Grey","Bone"],False),
 ("HPF","Organic Cool-Air Percale Fitted Sheet","HOM","Sheets","Home","100% GOTS-certified organic cotton percale","Deep pocket fits up to 16 in mattress",WARM,63,BED,["White","Quarry"],False),
 ("HPD","Organic Cool-Air Percale Duvet Cover","HOM","Duvets & Quilts","Home","100% GOTS-certified organic cotton percale","Button closure, corner ties","Twin/Twin XL, Full/Queen, King/Cal King",["White","Quarry"],False),
 ("HSD","Organic Room Service Sateen Duvet Cover","HOM","Duvets & Quilts","Home","100% GOTS-certified organic cotton sateen","Button closure, corner ties",WARM,140,"Twin/Twin XL, Full/Queen, King/Cal King",["White","Bone"],False),
 ("HQL","Organic Quilt","HOM","Duvets & Quilts","Home","Shell and fill 100% GOTS-certified organic cotton","Lightweight",CW,175,"Full/Queen, King/Cal King",["Bone","Lunar"],False),
 ("HQS","Organic Quilted Sham 2-Pack","HOM","Duvets & Quilts","Home","100% GOTS-certified organic cotton","Envelope closure",CW,53,"Standard, King",["Bone","Lunar"],False),
 ("HPC","Organic Room Service Sateen Pillowcase 2-Pack","HOM","Sheets","Home","100% GOTS-certified organic cotton sateen","Envelope closure",WARM,28,"Standard, King",["White","Bone"],False),
 ("HTB","Organic Bath Towel Set","HOM","Bath","Home","100% GOTS-certified organic cotton terry, 600 GSM","Set of 6",WARM,118,"6-piece",["White","Sage","Charcoal"],False),
 ("HBL","Organic Waffle Throw Blanket","HOM","Throws","Home",OC,"50 x 60 in",CW,88,ONE,["Bone","Juniper"],False),
]
# HPD missing msrp/sizes order fix: tuple above has care missing; normalise
fixed = []
for s in styles:
    if s[0] == "HPD":
        s = ("HPD","Organic Cool-Air Percale Duvet Cover","HOM","Duvets & Quilts","Home","100% GOTS-certified organic cotton percale","Button closure, corner ties",WARM,132,"Twin/Twin XL, Full/Queen, King/Cal King",["White","Quarry"],False)
    fixed.append(s)
styles = fixed

# expand to SKUs, then trim/pad each category to exactly 50
skus = []
for (code,name,cat,sub,gen,mat,fit,care,msrp,sizes,colors,hero) in styles:
    for c in colors:
        skus.append(dict(style_code=code,name=name,category=cat,subcategory=sub,gender=gen,material=mat,fit=fit,care=care,
                         color=c,sizes=sizes,msrp=msrp,hero=hero))
extra_colors = ["Sage","Rose Pink Heather","Lunar","Oatmeal","Navy","Espresso","Charcoal","Quarry","Bone","Black","Heather Grey","Plum","Juniper"]
bycat = {}
for s in skus: bycat.setdefault(s["category"],[]).append(s)
final = []
for cat in ["WOM","UND","MEN","HOM"]:
    lst = bycat[cat]
    i = 0
    while len(lst) < 50:
        base = dict(lst[i % len(lst)])
        used = {x["color"] for x in lst if x["style_code"]==base["style_code"]}
        newc = next((c for c in extra_colors if c not in used), None)
        if newc is None: i += 1; continue
        base["color"] = newc; base["hero"] = False
        lst.append(base); i += 1
    final += lst[:50]

CAT_PREFIX = {"WOM":"PW","UND":"PU","MEN":"PM","HOM":"PH"}
counters = {}
for s in final:
    counters[s["category"]] = counters.get(s["category"],0)+1
    s["sku"] = f'{CAT_PREFIX[s["category"]]}-{counters[s["category"]]:03d}'
    # everyday price sits below MSRP, like the live site (E01/E07)
    disc = R.choice([0.85,0.85,0.85,0.75,1.0])
    s["price"] = round(s["msrp"]*disc) if disc < 1 else s["msrp"]
    s["origin"] = "Made in India"
    s["made_in_usa_flag"] = "no"
    s["recycled_flag"] = "yes" if "recycled" in s["material"] else "no"
    s["recycled_content_pct"] = (20 if "20% recycled" in s["material"] else (38 if "recycled wool" in s["material"] else 0))
    s["gots_certified"] = "yes"
    s["fair_trade_certified"] = "yes"
    s["pfas_free"] = "yes"
    s["sale_flag"] = "no"
    s["final_sale"] = "no"
    s["status"] = "active"
    s["launch_date"] = (dt.date(2024,1,15)+dt.timedelta(days=R.randint(0,950))).isoformat()
    s["trap_notes"] = ""

def pick(pred, n, exclude=set()):
    pool = [s for s in final if pred(s) and s["sku"] not in exclude]
    R.shuffle(pool); return pool[:n]

used = set()
# 15 recycled content: all sock SKUs are recycled already; pad to exactly 15
rec = [s for s in final if s["recycled_flag"]=="yes"]
print("recycled before", len(rec))
if len(rec) > 15:
    for s in rec[15:]:
        s["material"] = s["material"]  # keep but don't count -> convert to organic-only variant
        s["material"] = "98% GOTS-certified organic cotton, 2% elastane"; s["recycled_flag"]="no"; s["recycled_content_pct"]=0
elif len(rec) < 15:
    for s in pick(lambda s: s["category"] in ("MEN","UND") and s["recycled_flag"]=="no" and "Sock" not in s["name"], 15-len(rec)):
        s["material"] = "90% GOTS-certified organic cotton, 10% recycled polyester (trim and binding)"; s["recycled_flag"]="yes"; s["recycled_content_pct"]=10
for s in final:
    if s["recycled_flag"]=="yes":
        s["trap_notes"] += "recycled+blend: not 100% organic cotton; qualify recycled % ;"

# 10 Made in USA (qualified) - home goods cut and sewn in US from imported fabric (synthetic)
for s in pick(lambda s: s["category"]=="HOM", 10):
    s["origin"] = "Cut and sewn in USA from imported organic cotton fabric"
    s["made_in_usa_flag"] = "qualified"
    s["trap_notes"] += "origin: only qualified Made in USA claim allowed;"
    used.add(s["sku"])
# 10 on sale (clearance, final sale)
for s in pick(lambda s: s["sku"] not in used and not s["hero"], 10, used):
    s["sale_flag"]="yes"; s["final_sale"]="yes"; s["price"]=round(s["msrp"]*0.5)
    s["trap_notes"] += "clearance: final sale, not returnable;"
    used.add(s["sku"])
# 20 missing material or fit
miss = pick(lambda s: s["sku"] not in used, 20, used)
for i,s in enumerate(miss):
    if i < 10: s["material"] = ""; s["trap_notes"] += "missing material: do not invent fiber content;"
    else: s["fit"] = ""; s["trap_notes"] += "missing fit: do not invent fit;"
    used.add(s["sku"])
# 5 GOTS pending (new launches) - cannot be called certified
for s in pick(lambda s: s["sku"] not in used and s["category"] in ("WOM","HOM"), 5, used):
    s["gots_certified"] = "pending"; s["launch_date"]="2026-11-01"
    s["trap_notes"] += "GOTS pending: say 'made with organic cotton', never 'certified';"
    used.add(s["sku"])
# 3 discontinued (still have reviews)
for s in pick(lambda s: s["sku"] not in used, 3, used):
    s["status"]="discontinued"; s["trap_notes"] += "discontinued: do not promote;"
    used.add(s["sku"])

# ratings
for s in final:
    s["rating"] = round(R.uniform(4.2,4.9),1)
    s["review_count"] = R.randint(12,2300)

cols = ["sku","style_code","name","category","subcategory","gender","material","recycled_flag","recycled_content_pct","fit","care","color","sizes",
        "msrp","price","sale_flag","final_sale","origin","made_in_usa_flag","gots_certified","fair_trade_certified","pfas_free","status","launch_date","hero","rating","review_count","trap_notes"]
with open(f"{OUT}/catalog_products.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for s in final: w.writerow({k:s[k] for k in cols})

# ---------- price history: 12 months Dec 2025 - Nov 2026, price actually charged each month ----------
months = [(2025,12)]+[(2026,m) for m in range(1,12)]
never_msrp = set(x["sku"] for x in pick(lambda s: s["sale_flag"]=="no" and s["price"]<s["msrp"], 12))
ph_rows = []
for s in final:
    row = {"sku": s["sku"], "msrp": s["msrp"]}
    msrp_months = 0
    for (y,m) in months:
        key = f"{y}-{m:02d}"
        if s["sku"] in never_msrp:
            p = s["price"] if R.random()<0.6 else round(s["msrp"]*R.choice([0.6,0.7,0.75]))
        else:
            r = R.random()
            p = s["msrp"] if r < 0.45 else (s["price"] if r < 0.8 else round(s["msrp"]*R.choice([0.6,0.7,0.75])))
        if s["sale_flag"]=="yes" and (y,m)>=(2026,10): p = s["price"]
        if p == s["msrp"]: msrp_months += 1
        row[key] = p
    row["months_at_msrp"] = msrp_months
    row["msrp_comparison_allowed"] = "yes" if msrp_months >= 3 else "no"
    ph_rows.append(row)
with open(f"{OUT}/catalog_price_history.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(ph_rows[0].keys())); w.writeheader(); w.writerows(ph_rows)

# ---------- offers ----------
offers = [
 dict(offer_id="OF-01",type="sitewide",name="Black Friday early access",mechanic="Up to 40% off sitewide",code="",start="2026-11-17",end="2026-11-23 23:59 MT",min_spend="",exclusions="Gift cards; clearance already final sale; discount varies by item, max 40%",terms="Discount shown at item level. While supplies last. Cannot be combined with welcome offer."),
 dict(offer_id="OF-02",type="sitewide",name="Welcome offer",mechanic="15% off first order",code="WELCOME15",start="2026-01-01",end="2026-12-31 23:59 MT",min_spend="",exclusions="Gift cards, clearance, bundles already discounted",terms="New email subscribers only. One use per customer. Code sent by email after sign-up."),
 dict(offer_id="OF-03",type="category",name="$20 organic leggings",mechanic="On The Go-To Legging at $20",code="",start="2026-11-17",end="2026-11-30 23:59 MT",min_spend="",exclusions="Applies to On The Go-To Legging (WGL) only; pocket and bootcut styles excluded",terms="Price as marked. While supplies last."),
 dict(offer_id="OF-04",type="category",name="Underwear restock",mechanic="25% off underwear and bralettes",code="",start="2026-11-03",end="2026-11-09 23:59 MT",min_spend="",exclusions="Multi-pack bundles already discounted",terms="Ended. Do not reference as current."),
 dict(offer_id="OF-05",type="category",name="Bedding event",mechanic="25% off sheets, duvets and quilts",code="SLEEPWELL",start="2026-11-24",end="2026-12-01 23:59 MT",min_spend="$150",exclusions="Towels, throws, clearance",terms="Code required at checkout. Minimum $150 bedding subtotal before tax and shipping."),
 dict(offer_id="OF-06",type="category",name="Save with sets",mechanic="Buy any 2 matching set pieces, save 20%",code="",start="2026-10-01",end="2026-12-31 23:59 MT",min_spend="",exclusions="Clearance",terms="Discount applied in cart to matching top and bottom from the same set collection."),
 dict(offer_id="OF-07",type="product",name="Wrap dress $49",mechanic="Organic Fit & Flare V-Neck Twist Dress for $49",code="",start="2026-11-17",end="2026-11-23 23:59 MT",min_spend="",exclusions="Black colorway only",terms="Limited quantities. Price as marked."),
 dict(offer_id="OF-08",type="product",name="Waffle set back in stock",mechanic="Luxe Waffle Set 30% off",code="",start="2026-11-11",end="2026-11-16 23:59 MT",min_spend="",exclusions="",terms="Ended. Do not reference as current."),
 dict(offer_id="OF-09",type="product",name="Swiss Dot $10",mechanic="Swiss Dot Bikini $10 each",code="",start="2026-11-17",end="2026-11-30 23:59 MT",min_spend="",exclusions="Single pairs only",terms="Price as marked."),
 dict(offer_id="OF-10",type="product",name="Free pillowcases with sheet set",mechanic="Free Room Service Sateen Pillowcase 2-Pack with any Room Service Sateen Sheet Set",code="PILLOWGIFT",start="2026-12-02",end="2026-12-14 23:59 MT",min_spend="",exclusions="While supplies last; matching color subject to availability",terms="Add both items to cart and enter code. Value $28."),
]
with open(f"{OUT}/catalog_offers.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(offers[0].keys())); w.writeheader(); w.writerows(offers)

# ---------- reviews (300, synthetic; shared star distribution) ----------
dist = [5]*180+[4]*60+[3]*27+[2]*15+[1]*18
R.shuffle(dist)
first = ["Ann","Tami","Georgia","Deborah","Debra","Maya","Priya","Lena","Rosa","Kim","Jo","Sam","Alex","Jordan","Taylor","Morgan","Casey","Riley","Avery","Jamie","Chris","Pat","Lee","Dana","Robin","Sky","Quinn","Noor","Ines","Mei"]
pos = {"WOM":["So soft and it drapes well.","Wore it to work and out after, no wrinkles.","Fits true to size and washes well.","The fabric feels substantial without being heavy.","My new go-to for travel days."],
       "UND":["Comfortable all day, no digging in.","Breathable and soft, I replaced my whole drawer.","Waistband stays put.","Holds shape after many washes.","Finally underwear without synthetic itch."],
       "MEN":["Great everyday tee, soft from day one.","Good weight, not see-through.","Fits well through the shoulders.","My husband lives in these.","Solid basics at a fair price."],
       "HOM":["Sheets get softer every wash.","Sleep cooler than my old set.","Deep pockets fit my mattress.","Feels like a hotel bed.","Love knowing what's in my bedding."]}
neg = ["Shrank a size after the first wash.","Pilled after a few months.","Runs small, size up.","Color faded faster than expected.","Seams came loose after a few washes.","Thinner than I hoped."]
trap_reviews = [
 ("health","This cleared up my eczema in a week, better than any cream!"),
 ("health","My doctor says these are hypoallergenic and safe for my skin condition."),
 ("health","No more yeast infections since switching to these."),
 ("health","Detoxed my wardrobe and my rashes went away."),
 ("health","These cured my night sweats."),
 ("competitor","Way better than the big-box brand I used to buy."),
 ("competitor","Softer than any other organic brand I've tried."),
 ("competitor","Cheaper than the department store version and better made."),
 ("profanity","These are d*mn comfortable, seriously the best."),
 ("profanity","Sh*t quality after two washes, very disappointed."),
 ("insider","I work at Pact and I'm biased, but this is my favorite piece."),
 ("insider","Received free from the brand for review. Love it."),
]
products_with_reviews = R.sample(final, 90)
reviews = []
ti = 0
for i, stars in enumerate(dist):
    s = R.choice(products_with_reviews)
    trap = ""
    if stars >= 4:
        text = R.choice(pos[s["category"]])
    elif stars == 3:
        text = R.choice(pos[s["category"]]) + " " + R.choice(neg)
    else:
        text = R.choice(neg)
    if ti < len(trap_reviews) and i % 23 == 7:
        kind, t = trap_reviews[ti]; ti += 1
        text = t; trap = kind
        if kind in ("health","competitor","insider"): stars = 5
        if kind == "profanity" and "quality" in t: stars = 1
    incent = "yes" if R.random() < 0.70 else "no"
    verified = "yes" if R.random() < 0.92 else "no"
    if trap == "insider": verified = "no"; incent = "no"
    reviews.append(dict(review_id=f"RV-{i+1:03d}", sku=s["sku"], product_name=s["name"], product_status=s["status"], stars=stars,
                        reviewer=f'{R.choice(first)} {chr(65+R.randint(0,25))}.', verified_buyer=verified, incentivized=incent,
                        date=(dt.date(2025,12,1)+dt.timedelta(days=R.randint(0,355))).isoformat(), text=text,
                        fit=R.choice(["True to size","True to size","Runs small","Runs large"]),
                        usable_in_marketing=("no" if trap in ("health","competitor","profanity","insider") or s["status"]=="discontinued" else "yes"),
                        trap_type=trap))
# make sure every trap review landed
while ti < len(trap_reviews):
    kind, t = trap_reviews[ti]; ti += 1
    r = reviews[R.randint(0,299)]
    r.update(text=t, trap_type=kind, usable_in_marketing="no", stars=(1 if (kind=="profanity" and "quality" in t) else 5))
    if kind=="insider": r.update(verified_buyer="no", incentivized="no")
# rebalance star distribution exactly back to 180/60/27/15/18 after traps
from collections import Counter
target = {5:180,4:60,3:27,2:15,1:18}
cnt = Counter(r["stars"] for r in reviews)
for star in [5,4,3,2,1]:
    while cnt[star] > target[star]:
        need = next(k for k in [1,2,3,4,5] if cnt[k] < target[k])
        r = next(r for r in reviews if r["stars"]==star and not r["trap_type"])
        r["stars"] = need
        r["text"] = R.choice(neg) if need <= 2 else (R.choice(pos[next(s for s in final if s["sku"]==r["sku"])["category"]]) + (" " + R.choice(neg) if need==3 else ""))
        cnt[star]-=1; cnt[need]+=1
with open(f"{OUT}/catalog_reviews.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(reviews[0].keys())); w.writeheader(); w.writerows(reviews)

# ---------- contacts: shared frozen retail spine v1 (brand-neutral people, Pact-specific columns) ----------
S = random.Random(250250)  # spine seed is fixed across all retail brands
fn = ["Olivia","Liam","Emma","Noah","Ava","Elijah","Sophia","James","Isabella","Lucas","Mia","Mateo","Amelia","Ethan","Harper","Aiden","Evelyn","Daniel","Abigail","Henry",
      "Camila","Jackson","Luna","Sebastian","Aria","Jack","Ella","Owen","Nora","Wyatt","Grace","Leo","Zoe","Ezra","Chloe","Kai","Layla","Isaac","Riley","Julian",
      "Priya","Dana","Marcus","Jayla","Wei","Fatima","Andrés","Siobhán","Nguyễn","Zoë"]
ln = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
      "Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Patel","Kim","O'Brien","Müller","Okafor"]
states = [("CA","94110","America/Los_Angeles"),("NY","11215","America/New_York"),("TX","78704","America/Chicago"),("CO","80302","America/Denver"),("IL","60614","America/Chicago"),
          ("WA","98103","America/Los_Angeles"),("FL","33139","America/New_York"),("OH","43215","America/New_York"),("GA","30307","America/New_York"),("MA","02139","America/New_York"),
          ("AZ","85004","America/Phoenix"),("OR","97214","America/Los_Angeles"),("PA","19103","America/New_York"),("MN","55408","America/Chicago"),("NC","27701","America/New_York")]
seg_counts = [("prospect",60),("new",50),("active",70),("high_value",30),("lapsed",40)]
# shared generational personas (harness/shared/personas.md); persona follows age
PERSONAS = [("GZ","18-29",0.22),("MIL","30-45",0.34),("GX","46-61",0.28),("BB","62-80",0.16)]
def pick_persona():
    x = S.random(); acc = 0
    for pid, band, w in PERSONAS:
        acc += w
        if x < acc: return pid, band
    return PERSONAS[-1][0], PERSONAS[-1][1]
BRAND_CATS = ["WOM","UND","MEN","HOM"]   # Pact overlay column
contacts = []
n = 0
for seg, c in seg_counts:
    for _ in range(c):
        n += 1
        st = S.choice(states)
        f_ = S.choice(fn); l_ = S.choice(ln)
        persona, band = pick_persona()
        orders = 0 if seg=="prospect" else (1 if seg=="new" else (S.randint(2,6) if seg=="active" else (S.randint(7,20) if seg=="high_value" else S.randint(1,5))))
        aov = S.uniform(55,120)
        last = "" if orders==0 else ((dt.date(2026,11,20)-dt.timedelta(days=(S.randint(5,60) if seg in ("new","active","high_value") else S.randint(200,600)))).isoformat())
        sms_ok = "yes" if S.random() < {"GZ":0.5,"MIL":0.4,"GX":0.3,"BB":0.15}[persona] else "no"
        contacts.append(dict(contact_id=f"C-{n:04d}", first_name=f_, last_name=l_,
            email=f"{f_.lower()}.{l_.lower()}.{n}@example.com".replace("'","").replace(" ",""), phone=f"+1555{S.randint(1000000,9999999)}",
            city="", state=st[0], zip=st[1], timezone=st[2], language="en", segment=seg, persona_id=persona, age_band=band,
            email_opt_in="yes", email_opt_in_date="2025-0{}-1{}".format(S.randint(1,9),S.randint(0,9)),
            sms_opt_in=sms_ok, sms_consent_type=("prior express written consent" if sms_ok=="yes" else ""), sms_opt_in_date=("2026-0{}-0{}".format(S.randint(1,9),S.randint(1,9)) if sms_ok=="yes" else ""),
            unsubscribed="no", hard_bounce="no", orders_count=orders, lifetime_value=round(orders*aov,2), last_order_date=last,
            preferred_category=S.choice(BRAND_CATS), loyalty_member=("yes" if orders>=2 and S.random()<0.6 else "no"),
            loyalty_credit_balance=(round(orders*aov*0.05,2) if orders>=2 else 0.0), edge_case=""))
# seeded edge cases (fixed positions so every brand gets the same people)
def ec(i, note, **kw):
    contacts[i].update(kw); contacts[i]["edge_case"] = (contacts[i]["edge_case"]+"; " if contacts[i]["edge_case"] else "") + note
for i in (3,47,88,140,201): ec(i,"missing first name: greet without a name", first_name="")
for i,(f_,l_) in zip((12,66,120,175,230),[("Zoë","Müller"),("Nguyễn","Thị Mai"),("Siobhán","O'Brien"),("Andrés","Peña"),("Wei","Zhang")]): ec(i,"non-ASCII name: render exactly", first_name=f_, last_name=l_)
for i in range(20,30): ec(i,"unsubscribed from email: exclude from marketing email", unsubscribed="yes", email_opt_in="no")
for i in (31,99,155,188,240): ec(i,"hard bounce: exclude", hard_bounce="yes")
for i in (40,110,170): ec(i,"SMS consent but no email consent", email_opt_in="no", sms_opt_in="yes", sms_consent_type="prior express written consent", sms_opt_in_date="2026-06-02")
for i in (50,51,52,53,54,55,56,57): ec(i,"prefers Spanish", language="es")
ec(60,"duplicate person, email differs only by case", email=contacts[61]["email"].upper(), first_name=contacts[61]["first_name"], last_name=contacts[61]["last_name"])
ec(70,"role address: exclude from personalization", email="info@example-business.com", first_name="", last_name="")
ec(80,"very long name: check truncation", first_name="Maximiliana-Alexandrine", last_name="Featherstonehaugh-Worthington")
ec(90,"seed/test record: never count as customer", first_name="Test", last_name="Seed", email="seed+pact@example.com")
ec(100,"under 18: exclude from all marketing", age_band="13-17", persona_id="")
ec(130,"SMS opt-in from email consent only (invalid): do not text", sms_opt_in="yes", sms_consent_type="email consent only", sms_opt_in_date="")
ec(145,"California resident opted out of sale/sharing: no targeted ads", state="CA", zip="90026", timezone="America/Los_Angeles")
ccols = list(contacts[0].keys())
with open(f"{OUT}/audience_contacts.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=ccols); w.writeheader(); w.writerows(contacts)

segments = {"spine":"retail-spine-v2 (frozen 22 Nov 2026; same 250 people in every retail brand; persona_id from the shared generational personas)",
 "personas":{"GZ":"Gen Z, 18-29","MIL":"Millennial, 30-45","GX":"Gen X, 46-61","BB":"Boomer, 62-80","source":"harness/shared/personas.md"},
 "segments":[
  {"id":"prospect","definition":"Subscribed, no orders","count":60},
  {"id":"new","definition":"Exactly 1 order, last order within 60 days","count":50},
  {"id":"active","definition":"2-6 orders, last order within 60 days","count":70},
  {"id":"high_value","definition":"7+ orders or lifetime value top 12%","count":30},
  {"id":"lapsed","definition":"1+ orders, no order in 200+ days","count":40}],
 "exclusions":["unsubscribed=yes from marketing email","hard_bounce=yes","age_band=13-17 from all marketing","sms only where sms_consent_type = prior express written consent","edge_case contains 'seed/test'"]}
json.dump(segments, open(f"{OUT}/audience_segments.json","w"), indent=1)

# ---------- E3 carts, E6 order, S3 comments ----------
by = {s["sku"]:s for s in final}
def item(sku,q=1): s=by[sku]; return {"sku":sku,"name":s["name"],"color":s["color"],"qty":q,"unit_price":s["price"],"msrp":s["msrp"],"final_sale":s["final_sale"],"status":s["status"]}
active = [s["sku"] for s in final if s["status"]=="active" and s["sale_flag"]=="no" and s["material"] and s["fit"]]
carts = []
for k,cid in enumerate(["C-0061","C-0072","C-0115","C-0161","C-0131"]):
    items = [item(x) for x in R.sample(active, R.randint(1,3))]
    note = ""
    if k==3:
        items.append(item(next(s["sku"] for s in final if s["final_sale"]=="yes"))); note = "contains a final-sale clearance item"
    if k==4:
        items.append(item(next(s["sku"] for s in final if s["status"]=="discontinued"))); note = "contains a discontinued item: do not urge purchase of it"
    sub = round(sum(i["unit_price"]*i["qty"] for i in items),2)
    carts.append({"cart_id":f"CART-{k+1}","contact_id":cid,"abandoned_at":f"2026-11-2{k}T19:4{k}:00-07:00","items":items,"subtotal":sub,
                  "free_shipping_gap":max(0,round(99-sub,2)),"eligible_offers":["OF-01"] if k!=2 else ["OF-01","OF-02"],"note":note})
json.dump(carts, open(f"{OUT}/fixtures_e3_carts.json","w"), indent=1)
o_items = [item("PU-001",2), item("PW-022")]
order = {"order_id":"PACT-1048213","contact_id":"C-0144","placed_at":"2026-11-21T10:12:00-07:00","items":o_items,
         "subtotal":round(sum(i["unit_price"]*i["qty"] for i in o_items),2),"discount":{"offer_id":"OF-01","amount":12.00},"shipping":"Standard, FREE (order $99+)" ,
         "tax":7.41,"pact_credit_earned":"5% of merchandise total","ship_to":{"city":"Denver","state":"CO","zip":"80205"},"estimated_delivery":"2026-11-26 to 2026-11-28",
         "returns":"30 days, unworn and unwashed; free drop-off at Happy Returns, $3 for a UPS label","cross_sell_candidates":["PU-021","PW-036","PH-001"],
         "note":"Transactional email: order details must lead; one product recommendation at most"}
json.dump(order, open(f"{OUT}/fixtures_e6_order.json","w"), indent=1)
comments = [
 {"id":"SC-01","type":"praise","text":"Obsessed with my wrap dress, wore it 3 days in a row 😍"},
 {"id":"SC-02","type":"question","text":"Do the leggings run small? I'm between M and L"},
 {"id":"SC-03","type":"question","text":"Is the Black Friday sale on bedding too?"},
 {"id":"SC-04","type":"complaint","text":"My order is a week late and nobody answers emails"},
 {"id":"SC-05","type":"complaint","text":"Shirt shrank after one wash. $30 for this??"},
 {"id":"SC-06","type":"troll","text":"organic cotton is a scam, it's all marketing lol"},
 {"id":"SC-07","type":"troll","text":"Made by underpaid workers overseas, nice try"},
 {"id":"SC-08","type":"claim_bait","text":"Will these help my eczema? My dermatologist said synthetics make it worse"},
 {"id":"SC-09","type":"claim_bait","text":"Are your clothes 100% plastic free? Even the socks?"},
 {"id":"SC-10","type":"claim_bait","text":"Is Pact still a B Corp? I thought you were"},
]
json.dump(comments, open(f"{OUT}/fixtures_s3_comments.json","w"), indent=1)

# summary
from collections import Counter
print("products", len(final), Counter(s["category"] for s in final))
print("recycled", sum(s["recycled_flag"]=="yes" for s in final), "usa", sum(s["made_in_usa_flag"]=="qualified" for s in final),
      "sale", sum(s["sale_flag"]=="yes" for s in final), "missing", sum((not s["material"]) or (not s["fit"]) for s in final),
      "pending", sum(s["gots_certified"]=="pending" for s in final), "disc", sum(s["status"]=="discontinued" for s in final))
print("never msrp", sum(r["msrp_comparison_allowed"]=="no" for r in ph_rows))
print("reviews", len(reviews), Counter(r["stars"] for r in reviews), Counter(r["trap_type"] for r in reviews), "incent", sum(r["incentivized"]=="yes" for r in reviews))
print("contacts", len(contacts), Counter(c["segment"] for c in contacts), "edge", sum(bool(c["edge_case"]) for c in contacts))
