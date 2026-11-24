"""Pact real-copy corpus. T = tuning set, H = held-out set (never used to tune rules)."""
import json
E = "/home/claude/pact/evidence"
def ads(path, split):
    out = []
    seen = set()
    for a in json.load(open(path)):
        k = (a["title"], a["body"])
        if k in seen or "{{" in (a["title"] or ""): continue
        seen.add(k)
        out.append(dict(split=split, channel="ad", headline=a["title"] or "", body=a["body"] or "", cta=a.get("cta") or ""))
    return out
CORPUS = ads(f"{E}/meta_ads_clean.json", "T") + ads(f"{E}/meta_ads_p2_clean.json", "H")
for p in json.load(open(f"{E}/ig_clean.json")):
    if p["owner"] == "pact":
        CORPUS.append(dict(split="T", channel="social", headline="", body=p["caption"], cta=""))
SITE_T = [
 ("web", "wellness shouldn't be a luxury", "Shop our best deals on organic gifts and feel-good favorites before Black Friday begins."),
 ("web", "black friday early access", "Entire site on sale. Everything is up to 40% off through Sunday."),
 ("web", "Dress Yourself Well", "We created Pact because we believe what you put closest to your skin, day and night, is essential to your wellbeing. And because what touches your skin should feel as good as it looks. Gentle-on-skin certified organic essentials, free from toxic dyes, harsh chemicals or PFAS."),
 ("web", "Our Sustainability Story", "We think you should know that not all organic is created equal. A lot of brands say organic. We go further, because real organic should always come with real standards that protect your skin, the people who make your clothes, and the planet."),
 ("web", "Our Standards", "Every garment we make is certified organic. That means oversight across the entire supply chain, not just the fiber itself. We don't claim perfection. We commit to progress."),
 ("web", "Soft Layers for Every Kind of Day.", "Pact uses Sustainable Materials, Ethical Manufacturing, and is Climate Friendly and Carbon Neutral. By choosing Organic Cotton, we can create Non-Toxic Clothing that uses 81% less water and 62% less energy."),
 ("web_meta", "Pact | Dress Yourself Well", "Pact is the leading brand in Sustainable & Ethical Clothing - Organic Cotton, Fair Trade & Carbon Neutral. Get 15% off your first order. Free Shipping on orders $100+."),
 ("web_meta", "About Pact", "Our mission is to build Earth’s Favorite™ Clothing Company."),
 ("pdp", "Organic Fit & Flare Wrap Dress", "The dress that takes you from desk to dinner. A midi in our GOTS-certified organic cotton jersey knit, soft, drapey, wrinkle-resistant. Faux wrap bodice, built-in support, removable belt, and two hidden pockets. Wear with a blazer to the office, or heels for evenings. One wrap, all day long."),
 ("pdp_module", "Wellness ingredients", "MADE WITH organic cotton*. MADE WITHOUT harsh chemicals, toxic dyes, and PFAS. CERTIFIED GOTS & Fair Trade. *Also with 5% Elastane for stretch and recovery"),
]
SITE_H = [
 ("pdp", "Organic All-Day Twill Wide Leg Pant", "The wide leg that flatters every single time. A modern mid-rise in our GOTS-certified organic cotton All-Day Twill, better than denim and soft against the skin. Elastic at side waist, zipper fly, 5-pocket construction. Wear with a tee and sneakers, or sweater and boots. The pant worth living in."),
 ("pdp_module", "Wellness ingredients", "MADE WITH organic cotton*. MADE WITHOUT harsh chemicals, toxic dyes, and PFAS. CERTIFIED GOTS & Fair Trade. *Also with 2% Elastane for stretch and recovery"),
 ("web_meta", "All-Day Twill Wide Leg Pant", "Discover Earth’s Favorite™ Clothing. All-day Twill Wide Leg Pant made with Organic Cotton in a Fair Trade Certified™ factory. 98% GOTS-certified Organic Cotton, 2% Elastane."),
]
for split, rows in (("T", SITE_T), ("H", SITE_H)):
    for ch, h, b in rows:
        CORPUS.append(dict(split=split, channel=ch, headline=h, body=b, cta=""))
if __name__ == "__main__":
    from collections import Counter
    print(len(CORPUS), Counter((c["split"], c["channel"]) for c in CORPUS))
    json.dump(CORPUS, open("/home/claude/pact/out/realcopy_corpus.json", "w"), indent=1, ensure_ascii=False)
