"""Build a full Plumb retail harness for one brand from: configs.py (mechanics), content_<b>.py (brand book prose, policies, claims,
copy, goldens, traps), ev/products.json (real catalog), the shared contact spine, and Pact's rules.json as the rule template."""
import csv, json, os, re, random, sys, importlib, datetime as dt, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from configs import BRANDS
from brandkit import check, layer

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PACT_OUT = f"{ROOT}/harness/retail-pact"
SPINE = f"{ROOT}/harness/shared/contacts_spine_v2.csv"
MONTHS = ["2025-12","2026-01","2026-02","2026-03","2026-04","2026-05","2026-06","2026-07","2026-08","2026-09","2026-10","2026-11"]

def wcsv(path, rows, cols):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); [w.writerow({k: r.get(k, "") for k in cols}) for r in rows]

# ---------------------------------------------------------------- colors
def _lum(h):
    h = h.lstrip("#"); rgb = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    r, g, b = map(f, rgb); return 0.2126*r + 0.7152*g + 0.0722*b
def contrast(a, b):
    la, lb = sorted([_lum(a), _lum(b)], reverse=True); return round((la+0.05)/(lb+0.05), 2)

def tokens(C, cfg):
    pal = C["palette"]; bgs = [p for p in pal if p["role"] in ("neutral", "background")]
    texts = [p for p in pal if p["role"] not in ("background",)]
    ok, large, bad = [], [], []
    for t in texts:
        for b in bgs:
            if t["hex"] == b["hex"]: continue
            c = contrast(t["hex"], b["hex"]); s = f"{t['name']} {t['hex']} on {b['name']} {b['hex']} ({c}:1)"
            (ok if c >= 4.5 else large if c >= 3 else bad).append(s)
    tot = sum(p.get("uses") or 0 for p in pal)
    return {"brand": cfg["key"], "version": "0.3-public-build",
        "colors_note": f"Colors are referenced by hex only (no Pantone). Values and use counts come from {C['domain']} homepage HTML/CSS, 22 Nov 2026.",
        "colors": {p["name"].lower().replace(" ", "_"): {"hex": p["hex"], "rgb": [int(p["hex"][i:i+2], 16) for i in (1, 3, 5)], "role": p["role"],
                   "used_for": p["used_for"], "homepage_uses": p.get("uses"), "usage_share": f"{round(100*(p.get('uses') or 0)/tot)}%" if tot else None,
                   "source": p.get("source", f"{C['domain']} homepage, 22 Nov 2026")} for p in pal},
        "approved_text_pairings": ok, "large_text_only": large, "banned_text_pairings": bad,
        "typography": C["fonts"], "spacing_px": [4, 8, 12, 16, 24, 32, 48, 64], "radius_px": C.get("radius", 0),
        "logo": {"files": ["logo-full.svg (to supply)", "logo-mono.svg (to supply)", "logo-icon.svg (to supply)"], "notes": C["logo_note"]}}

# ---------------------------------------------------------------- catalog
def catalog(b, C, cfg, R):
    P = json.load(open(f"{HERE}/evidence/{b}/products.json"))
    seen = set(); U = []
    for p in P:
        k = p["title"] + "|" + "/".join(p["options"].get("Color") or [])
        if k in seen: continue
        seen.add(k); U.append(p)
    bycat = {c: [] for c, _ in C["categories"]}
    for p in U:
        c = C["categorize"](p)
        if c in bycat: bycat[c].append(p)
    rows = []; n = 0; prefix = C["sku_prefix"]
    for cat, cname in C["categories"]:
        pool = bycat[cat][:]; R.shuffle(pool); picked = pool[:50]; synth = []
        i = 0
        while len(picked) + len(synth) < 50:          # fill short categories with extra colorways of real styles
            base = pool[i % len(pool)]; synth.append((base, C["synth_colors"][i % len(C["synth_colors"])])); i += 1
        for j, item in enumerate([(p, None) for p in picked] + synth):
            p, sc = item; n += 1
            title = p["title"]; color = sc
            if not color:
                color = (p["options"].get("Color") or [""])[0] or C["color_from_title"](title)
            name = C["clean_name"](title)
            body = p["body"] or ""
            mat = C["material"](p); origin = C["origin"](p)
            price = float(p["price"] or 0); comp = float(p["compare"]) if p.get("compare") else None
            msrp = comp if comp and comp > price else price
            r = dict(sku=f"{prefix}{cat[0]}-{j+1:03d}", style_code=re.sub(r"[^A-Z0-9]", "", name.upper())[:6], name=name, category=cat, subcategory=C["subcat"](p),
                     gender=C["gender"](p), material=mat, color=color, sizes=C["sizes"](p), msrp=int(msrp) if msrp == int(msrp) else msrp,
                     price=int(price) if price == int(price) else price, sale_flag="yes" if msrp > price else "no", final_sale="no",
                     origin=origin, status="active", launch_date=(dt.date(2025, 1, 15) + dt.timedelta(days=R.randint(0, 640))).isoformat(),
                     hero="", rating=round(R.uniform(3.9, 4.9), 1), review_count=R.randint(3, 900), source_title=title,
                     care=C["care"](p), recycled_flag="yes" if "recycled" in body.lower() else "no",
                     synthetic_colorway="yes" if sc else "no", trap_notes="")
            for k, f in C.get("extra_cols", {}).items(): r[k] = f(p, r)
            rows.append(r)
    C["catalog_traps"](rows, R)
    cols = ["sku","style_code","name","category","subcategory","gender","material","recycled_flag","care","color","sizes","msrp","price","sale_flag",
            "final_sale","origin"] + list(C.get("extra_cols", {}).keys()) + ["status","launch_date","hero","rating","review_count","synthetic_colorway","source_title","trap_notes"]
    return rows, cols

def price_history(rows, C, R):
    out = []
    for r in rows:
        msrp = float(r["msrp"]); price = float(r["price"]); hist = []
        mode = C["history_mode"](r, R)              # 'msrp' (mostly sold at msrp) or 'comp' (comp value never charged)
        for m in MONTHS:
            if mode == "comp": v = price if R.random() < 0.85 else round(price*R.choice([0.5, 0.6, 0.7]))
            else: v = msrp if R.random() < 0.75 else round(msrp*R.choice([0.6, 0.7, 0.8]))
            hist.append(v)
        hist[-1] = price
        at = sum(1 for v in hist if float(v) >= msrp)
        h = {"sku": r["sku"], "msrp": r["msrp"], **{m: (int(v) if float(v) == int(v) else v) for m, v in zip(MONTHS, hist)},
             "months_at_msrp": at, "msrp_comparison_allowed": "yes" if at >= 6 else "no"}
        out.append(h)
    return out

def reviews(rows, C, R):
    act = [r for r in rows if r["status"] == "active"]; out = []
    stars = [5]*180 + [4]*60 + [3]*27 + [2]*15 + [1]*18; R.shuffle(stars)
    first = ["Ava","Mia","Zoe","Lena","Priya","Grace","Nora","Jade","Ruth","Ellen","Maya","Sam","Chris","Dana","Leah","Kate","Rosa","Ines","Tara","Jo"]
    for i, s in enumerate(stars):
        r = R.choice(act); bank = C["review_text"][r["category"]] if s >= 4 else C["review_neg"]
        out.append(dict(review_id=f"RV-{i+1:03d}", sku=r["sku"], product_name=r["name"], product_status=r["status"], stars=s,
                        reviewer=f"{R.choice(first)} {chr(65+R.randint(0,25))}.", verified_buyer="yes" if R.random() < .9 else "no",
                        incentivized="yes" if R.random() < .12 else "no", date=(dt.date(2025, 12, 1)+dt.timedelta(days=R.randint(0, 355))).isoformat(),
                        text=R.choice(bank), fit=R.choice(["True to size","True to size","Runs small","Runs large",""]), usable_in_marketing="yes", trap_type=""))
    for k, (ttype, text, stars_, note) in enumerate(C["review_traps"]):
        o = out[k*23]; o.update(text=text, stars=stars_, trap_type=ttype, usable_in_marketing="no")
        if ttype == "discontinued_product":
            d = next(r for r in rows if r["status"] == "discontinued"); o.update(sku=d["sku"], product_name=d["name"], product_status="discontinued")
    for o in out:
        if o["incentivized"] == "yes" and not o["trap_type"]: o["trap_type"] = "incentivized: label if quoted"
    return out

def contacts(C, R):
    rows = list(csv.DictReader(open(SPINE)))
    for r in rows:
        r["preferred_category"] = R.choice([c for c, _ in C["categories"]]) if r["orders_count"] != "0" else ""
        r["brand_fit"] = "primary" if r["persona_id"] == C["personas"][0] else "secondary" if r["persona_id"] == C["personas"][1] else "other"
        if C.get("contact_overlay"): C["contact_overlay"](r, R)
    cols = list(rows[0].keys())
    return rows, cols

# ---------------------------------------------------------------- rules
PACT_WORDS = ["GOTS","Fair Trade","PFAS","Juana","Averta","GT Eesti","Boulder","Walnut","wellness","#organiccotton","Dress Yourself Well","Earth's",
              "Pact","organic cotton","p a c t","SimpliZero","Wine #","Warm Charcoal","made without","Room Service","On The Go-To","toxic dyes"]
def build_rules(b, C, cfg):
    tpl = json.load(open(f"{PACT_OUT}/rules.json"))["rules"]; out = []
    ov = C["R"]; mech = mech_rules(C, cfg); ov = {**mech, **ov}
    for r in tpl:
        if r["id"] in C.get("R_drop", []): continue
        r = copy.deepcopy(r)
        if r["id"] in ov:
            o = ov[r["id"]]; o = {"rule": o} if isinstance(o, str) else o
            for k in ("pass", "fail", "test", "anchors"): r.pop(k, None)
            r.update(o)
            if r.get("check") == "AI judge" and not r.get("anchors"):
                r["anchors"] = {"1": "Ignores or contradicts this rule", "4": "Does this clearly, at the level of the golden examples"}; r.setdefault("provenance", "observed")
            r["source"] = o.get("source", r.get("source", "")) if "source" in o else C["R_src"].get(r["section"], "E01")
        else:
            for a, bb in C["subs"]:
                r["rule"] = r["rule"].replace(a, bb)
                for k in ("pass", "fail", "test"):
                    if isinstance(r.get(k), str): r[k] = r[k].replace(a, bb)
                if r.get("anchors"): r["anchors"] = {kk: vv.replace(a, bb) for kk, vv in r["anchors"].items()}
        r["layer"] = layer(r["id"]) if r["section"] not in ("LEG", "ACC") else "compliance"
        if r["id"] in ("VOI-21", "MSG-01", "MSG-05", "MSG-08", "MSG-09", "MSG-10", "MSG-11", "MSG-16", "DR-01", "DR-06", "DCO-03", "DCO-05", "EML-07", "EML-08",
                       "SOC-06", "SOC-07", "WEB-05", "IMG-04", "IMG-07", "IMG-08", "IMG-11", "IMG-13", "IMG-14", "LP-05"): r["layer"] = "compliance"
        out.append(r)
    for a in C.get("R_add", []): a = dict(a); a.setdefault("layer", "brand"); out.append(a)
    # leak check: no Pact specifics left unless brand-legit
    allow = C.get("allow_words", [])
    leaks = [(r["id"], w) for r in out for w in PACT_WORDS if re.search(r"(?<![a-z])" + re.escape(w.lower()) + r"(?![a-z])", json.dumps(r, ensure_ascii=False).lower()) and w not in allow and not (w == "wellness" and r["id"] == "VOI-24")]
    return out, leaks

def mech_rules(C, cfg):
    n = C["name"]; e = cfg["emoji"]; x = cfg["exclaim"]; cp = cfg["caps"]
    lim = lambda t: "none" if t == (0, 0) else f"{t[0]}–{t[1]}" if t[0] else f"up to {t[1]}"
    return {
     "VOI-01": f"Never use any word on the compliance banned list ({len(cfg['banned_compliance'])} words) in customer-facing copy: {', '.join(cfg['banned_compliance'])}.",
     "VOI-02": {"rule": f"Use the brand vocabulary: at least one brand word per asset (offer-only lines exempt). Brand words: {', '.join(cfg['vocab'][:40])}." + (f" Product pages use the product vocabulary: {', '.join(cfg['vocab_pdp'])}." if cfg.get('vocab_pdp') else ""), "check": "auto"},
     "VOI-03": f"Write the brand name as '{n}' in running copy. Never: {', '.join(C['name_bad_examples'])}.",
     "VOI-05": "Serial comma: " + ("optional, but consistent within one asset." if cfg["serial_comma"] == "consistent" else f"{n} uses both styles; no rule beyond clarity (observed {C['serial_obs']}).") ,
     "VOI-06": "Prices drop trailing zeros: $26 not $26.00; keep cents only when non-zero." if cfg["price_zeros"] == "strip" else "Prices as the catalog shows them ($26 or $25.99); never invent cents.",
     "VOI-09": f"Emoji in product pages and web copy: {lim(e['pdp'])}; email body: {lim(e['email_body'])}.",
     "VOI-10": f"Emoji per organic social caption: {lim(e['social'])}." + (" At least one." if e['social'][0] else ""),
     "VOI-11": f"Emoji per paid ad: {lim(e['ad'])}." + (" Emoji used as list bullets in product call-outs do not count." if cfg.get("emoji_bullets_ok") else "") + f" All-caps words (excluding acronyms) per ad: {lim(cp['ad'])}; per social caption: {lim(cp['social'])}; per PDP: {lim(cp['pdp'])}.",
     "VOI-12": f"Exclamation marks: ads up to {x['ad']}, social up to {x['social']}, PDP up to {x['pdp']}, web up to {x['web']}, email body up to {x['email_body']}.",
     "VOI-13": f"Reading level: grade {cfg['fk_max']} or below (Flesch-Kincaid) for ads, email, web and PDP copy of 3+ sentences.",
     "VOI-14": f"Sentences average {cfg['sent_max']} words or fewer (ads, email, web); a spaced em dash or an emoji counts as a break.",
     "VOI-24": {"rule": f"Off-voice words never used: {', '.join(cfg['banned_voice'])}.", "check": "auto"},
     "SOC-01": f"Instagram: hook in the first 125 characters; {cfg['hashtags'][0]}–{cfg['hashtags'][1]} hashtags" + (f", always including {cfg['hashtag_required']}." if cfg.get('hashtag_required') else "."),
     "DR-04": f"Paid social: first sentence of primary text within 125 characters; headline up to {cfg['headline_max']} characters; CTA one of {', '.join(cfg['ctas'])}.",
     "DR-05": "Paid ad headlines in Title Case or sentence case; " + ("all caps allowed for event lines (e.g. 'BLACK FRIDAY')." if cfg["allcaps_headline_ok"] else "never all caps."),
     "WEB-02": f"PDP description {cfg['pdp_words'][0]}–{cfg['pdp_words'][1]} words." + (" " + C["pdp_shape"] if C.get("pdp_shape") else ""),
     "LEG-12": f"Free shipping: state the threshold exactly as {C['ship_text']}.",
     "BRD-08": C["tagline_rule"],
    }

# ---------------------------------------------------------------- validation of goldens and traps
def v_text(t, ch, cfg, **kw): return check(t, ch, cfg, **kw)
def validate(b, C, cfg, rows):
    P = {r["sku"]: r for r in rows}; out = {"golden": [], "drafts": []}
    def pdp(o):
        p = P[o["sku"]]; v = v_text(o["description"], "pdp", cfg, headline=o["title"])
        v += [x for x in v_text(" ".join(str(o.get(k, "")) for k in ("fiber_content", "care", "origin", "fit")), "pdp_module", cfg) if layer(x[0]) == "compliance"]
        if o.get("fiber_content", "") != (p["material"] or ""): v.append(("LEG-16", f"fiber '{o.get('fiber_content')}' vs catalog '{p['material']}'"))
        if not o.get("origin"): v.append(("LEG-14", "no origin"))
        elif o["origin"] != p["origin"]: v.append(("LEG-14", f"origin '{o['origin']}' vs catalog '{p['origin']}'"))
        if p["status"] != "active": v.append(("DCO-05", "not active"))
        v += C["pdp_extra"](o, p)
        return v
    def email(o):
        v = v_text(o["body"], "email_body", cfg) + v_text(o["subject"], "subject", cfg)
        if not 25 <= len(o["subject"]) <= 50: v.append(("EML-01", len(o["subject"])))
        if not 40 <= len(o["preheader"]) <= 90 or o["preheader"] == o["subject"]: v.append(("EML-02", len(o["preheader"])))
        if not 2 <= len(o["cta"].split()) <= 4: v.append(("EML-04", o["cta"]))
        if C["address"] not in o["footer"]: v.append(("LEG-01", "address"))
        for k in ("Unsubscribe", "Privacy", "Accessibility", f"© 2026 {C['name']}"):
            if k not in o["footer"]: v.append(("EML-05", k))
        if not o.get("terms") or C["tz_end"] not in o["terms"]: v.append(("LEG-11", "terms/end time"))
        v += [x for x in v_text(o["terms"], "web", cfg) if x[0] in ("LEG-12", "MSG-06")]
        v += C["email_extra"](o, P)
        return v
    def ads(o):
        v = [x for x in v_text(" ".join(o["headlines"]) + ". " + " ".join(o["descriptions"]), "ad", cfg) if x[0] in ("VOI-02",)]
        for h in o["headlines"]:
            v += v_text(h, "ad_line", cfg)
            if len(h) > 30: v.append(("DR-01", f"headline {len(h)}: {h}"))
        for d in o["descriptions"]:
            v += v_text(d, "ad_line", cfg)
            if len(d) > 90: v.append(("DR-01", f"description {len(d)}: {d}"))
        if len(o["headlines"]) != 15 or len(set(o["headlines"])) != 15: v.append(("DR-02", "15 unique"))
        if len(o["descriptions"]) != 4 or len(set(o["descriptions"])) != 4: v.append(("DR-02", "4 unique"))
        v += C["ads_extra"](o)
        return v
    def social(o):
        v = v_text(o["caption"], "social", cfg)
        v += C["social_extra"](o)
        return v
    def sms(o):
        v = v_text(o["text"], "social", cfg)
        v = [x for x in v if layer(x[0]) == "compliance"]
        if len(o["text"]) > 160: v.append(("EML-08", f"{len(o['text'])} chars"))
        if "Reply STOP to opt out" not in o["text"]: v.append(("EML-08", "no STOP line"))
        c = o.get("contact")
        if c: v += C["sms_extra"](o)
        return v
    F = dict(P1=pdp, E1=email, A1=ads, S1=social, S3=social, M1=sms)
    for g in C["goldens"]:
        out["golden"].append((g["id"], F[g["task"]](g["out"])))
    for d in C["drafts"]:
        found = F[d["task"]](d["text"]); ids = {x[0] for x in found}
        exp = [e["rule"] for e in d["expected_violations"]]
        out["drafts"].append((d["id"], exp, [e for e in exp if e not in ids], found))
    return out

def run(b):
    cfg = BRANDS[b]; C = importlib.import_module(f"content_{b}").C; C["name"] = cfg["name"]
    O = f"{ROOT}/harness/retail-{b}"; os.makedirs(O, exist_ok=True)
    R = random.Random(C["seed"])
    rows, cols = catalog(b, C, cfg, R); wcsv(f"{O}/catalog_products.csv", rows, cols)
    ph = price_history(rows, C, R); wcsv(f"{O}/catalog_price_history.csv", ph, list(ph[0].keys()))
    for r in rows:
        h = next(x for x in ph if x["sku"] == r["sku"]); r["_cmp"] = h["msrp_comparison_allowed"]
    wcsv(f"{O}/catalog_offers.csv", C["offers"], list(C["offers"][0].keys()))
    rv = reviews(rows, C, R); wcsv(f"{O}/catalog_reviews.csv", rv, list(rv[0].keys()))
    ct, ccols = contacts(C, R); wcsv(f"{O}/audience_contacts.csv", ct, ccols)
    seg = json.load(open(f"{PACT_OUT}/audience_segments.json")); seg["brand"] = b
    seg["brand_persona_fit"] = {"primary": C["personas"][0], "secondary": C["personas"][1], "note": "Personas are shared across brands (harness/shared/personas.md); this brand's fit is a column, not a new persona."}
    json.dump(seg, open(f"{O}/audience_segments.json", "w"), indent=1)
    json.dump(tokens(C, cfg), open(f"{O}/brand_tokens.json", "w"), indent=1, ensure_ascii=False)
    for k, v in C["fixtures"](rows, ct, ph).items(): json.dump(v, open(f"{O}/{k}.json", "w"), indent=1, ensure_ascii=False)
    rules, leaks = build_rules(b, C, cfg)
    json.dump({"brand": b, "version": "0.3-public-build", "built": "2026-11-22", "rules": rules}, open(f"{O}/rules.json", "w"), indent=1, ensure_ascii=False)
    val = validate(b, C, cfg, rows)
    json.dump({"note": C["drafts_note"], "drafts": C["drafts"]}, open(f"{O}/traps_offbrand_drafts.json", "w"), indent=1, ensure_ascii=False)
    return dict(cfg=cfg, C=C, rows=rows, ph=ph, rv=rv, ct=ct, rules=rules, leaks=leaks, val=val, O=O)

if __name__ == "__main__":
    b = sys.argv[1]; res = run(b)
    rows = res["rows"]
    from collections import Counter
    print(b, "SKUs", len(rows), Counter(r["category"] for r in rows), "synthetic", sum(r["synthetic_colorway"] == "yes" for r in rows))
    print("traps", Counter(t for r in rows for t in r["trap_notes"].split(";") if t).most_common(12))
    print("cmp allowed", Counter(h["msrp_comparison_allowed"] for h in res["ph"]), "rules", len(res["rules"]), "leaks", res["leaks"][:30])
    for gid, v in res["val"]["golden"]: print("GOLDEN", gid, "PASS" if not v else v)
    det = sum(len(e) - len(m) for _, e, m, _ in res["val"]["drafts"]); tot = sum(len(e) for _, e, _, _ in res["val"]["drafts"])
    print(f"drafts detected {det}/{tot}"); [print("  MISS", i, m) for i, e, m, f in res["val"]["drafts"] if m]
