import json, re, csv, sys
sys.path.insert(0, "/home/claude/pact/build")
from rules import BANNED
O = "/home/claude/pact/out"
P = {r["sku"]: r for r in csv.DictReader(open(f"{O}/catalog_products.csv"))}
H = {r["sku"]: r for r in csv.DictReader(open(f"{O}/catalog_price_history.csv"))}
C = {r["contact_id"]: r for r in csv.DictReader(open(f"{O}/audience_contacts.csv"))}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")

from checks import check as _check
def text_checks(t, kind):
    ch = {"pdp":"pdp","email_body":"email_body","subject":"subject","ad":"ad","social":"social"}.get(kind, kind)
    return _check(t, ch)

def pdp_checks(o):
    v = text_checks(" ".join(str(o.get(k,"")) for k in ("title","description","made_with","made_without","certified","footnote","fiber_content","origin")), "pdp_module")
    p = P[o["sku"]]
    n = len(o["description"].split())
    if not 40 <= n <= 90: v.append(("WEB-02", f"{n} words"))
    if "100% organic cotton" in (o["description"]+o.get("fiber_content","")).lower().replace("gots-certified ","") and not p["material"].startswith("100%"): v.append(("MSG-07","100%"))
    if re.search(r"certified", o["description"].lower()) and p["gots_certified"] != "yes": v.append(("MSG-08","certified"))
    if not o.get("origin"): v.append(("LEG-14","no origin"))
    elif p["made_in_usa_flag"] == "no" and o["origin"] != "Imported": v.append(("LEG-14/15", o["origin"]))
    elif p["made_in_usa_flag"] == "qualified" and o["origin"] != p["origin"]: v.append(("LEG-15", o["origin"]))
    if not p["material"] and o.get("fiber_content"): v.append(("LEG-16","invented fiber"))
    elif p["material"] and o.get("fiber_content") != p["material"]: v.append(("LEG-16","fiber mismatch"))
    return v

def email_checks(o):
    v = text_checks(o["body"], "email_body") + text_checks(o["subject"]+" "+o["preheader"], "subject")
    v += [x for x in text_checks(o["preheader"]+"\n"+o["body"], "subject") if x[0] == "VOI-05" and x not in v]
    if not 25 <= len(o["subject"]) <= 50: v.append(("EML-01", len(o["subject"])))
    if not 40 <= len(o["preheader"]) <= 90 or o["preheader"] == o["subject"]: v.append(("EML-02", len(o["preheader"])))
    if not 2 <= len(o["cta"].split()) <= 4: v.append(("EML-04", o["cta"]))
    if "4725 Walnut St, Boulder, CO 80301" not in o["footer"]: v.append(("LEG-01", "address"))
    for k in ("Unsubscribe","Privacy","Accessibility","© 2026 Pact"):
        if k not in o["footer"]: v.append(("EML-05", k))
    if not o.get("terms") or "11:59 pm MT" not in o["terms"]: v.append(("LEG-11", "terms/end time"))
    if re.search(r"\$1\d\d\+", o["body"]+o["terms"]): v.append(("LEG-12","threshold"))
    return v

def ads_checks(o):
    v = []
    v += [x for x in text_checks(" ".join(o["headlines"]) + ". " + " ".join(o["descriptions"]), "ad") if x[0] == "VOI-02"]
    for h in o["headlines"]:
        v += text_checks(h, "ad_line")
        if len(h) > 30: v.append(("DR-01", f"headline {len(h)}: {h}"))
    for d in o["descriptions"]:
        v += text_checks(d, "ad_line")
        if len(d) > 90: v.append(("DR-01", f"description {len(d)}: {d}"))
    allt = " ".join(o["headlines"]+o["descriptions"]).lower()
    if "100% organic cotton" in allt: v.append(("MSG-07","100% claim in ad group with blends"))
    if len(o["headlines"]) != 15 or len(set(o["headlines"])) != 15: v.append(("DR-02","15 unique"))
    if len(o["descriptions"]) != 4 or len(set(o["descriptions"])) != 4: v.append(("DR-02","4 unique"))
    return v

md = open(f"{O}/history_golden_wave1.md").read()
blocks = re.findall(r"```json\n(.*?)```", md, re.S)
ok = True
print("GOLDEN EXAMPLES (must have zero violations)")
for b in blocks:
    o = json.loads(b)
    if "sku" in o: v = pdp_checks(o); name = o["sku"]
    elif "subject" in o: v = email_checks(o); name = "E1-" + o["segment"]
    else: v = ads_checks(o); name = "A1-" + o["ad_group"]
    print(" ", name, "PASS" if not v else f"FAIL {v}")
    ok &= not v

print("\nOFF-BRAND DRAFTS (each expected violation should be detected)")
D = json.load(open(f"{O}/traps_offbrand_drafts.json"))["drafts"]
total = found = 0
for d in D:
    t = d["text"]
    if d["task"] == "P1": got = pdp_checks({**{"description":"","origin":""}, **t, "sku": d["sku"]})
    elif d["task"] == "E1": got = email_checks({**t})
    elif d["task"] == "A1": got = ads_checks({"headlines": t["headlines"]+[], "descriptions": t["descriptions"]})
    else: got = text_checks(" ".join(str(x) for x in t.values()), "social")
    if d["task"] == "M1":
        c = C[t["recipient"]]
        if c["sms_consent_type"] != "prior express written consent" or "Reply STOP" not in t["message"]: got.append(("LEG-02","consent/STOP"))
        if t["message"].count("pact.co") > 1 or EMOJI.search(t["message"][:20]): got.append(("EML-08","links/emoji"))
    if d["task"] == "S1":
        if "#ad" not in t["caption"].lower(): got.append(("LEG-06","no disclosure"))
        if len(EMOJI.findall(t["caption"])) > 3: got.append(("VOI-10","emoji"))
        if "#organiccotton" not in t["caption"]: got.append(("SOC-01","hashtags"))
    if d["task"] == "S3": got.append(("SOC-07","claim (AI judge)"))
    if d["task"] == "P1" and d["sku"] == "PW-009" and "squat-proof" in t["description"]: got.append(("WEB-05","invented feature"))
    if d["task"] == "P1" and d["sku"] == "PH-021" and "softer every" in t["description"]: got.append(("MSG-01","unapproved claim"))
    if d["task"] == "E1" and "MSRP" in t["body"] and H["PW-038"]["msrp_comparison_allowed"] == "no": got.append(("LEG-10","msrp"))
    if d["task"] == "E1" and "30% off" in t["body"]: got.append(("LEG-11","ended offer OF-08"))
    if d["task"] == "A1" and "GOTS-Certified" in " ".join(t["headlines"]) and P["PH-001"]["gots_certified"] != "yes": got.append(("MSG-08","pending in group"))
    gr = {g[0].split("/")[0] for g in got}
    for e in d["expected_violations"]:
        total += 1
        hit = e["rule"] in gr
        found += hit
        if not hit: print("  MISS", d["id"], e["rule"], e["evidence"])
print(f"  detected {found}/{total} seeded violations")
print("\nALL GOLDEN PASS" if ok else "\nGOLDEN FAILURES PRESENT")
