"""Shared auto-check engine for Pact copy. check(text, channel, headline="", cta="") -> list of (rule_id, evidence)."""
import re, sys
sys.path.insert(0, "/home/claude/pact/build")
from rules import RULES, BANNED, USE
LAYER = {r["id"]: r["layer"] for r in RULES}
EMO = re.compile("[\U0001F300-\U0001FAFF☀-☄☆-➿]")  # excludes ★ (U+2605) rating stars
APPROVED_WITHOUT = ["harsh chemicals", "toxic dyes", "pfas"]
OFFER_PCT = {15, 20, 25, 30, 40}   # from catalog_offers.csv
UPTO_PCT = {40}                     # sitewide event varies by item

def _syl(w):
    w = w.lower(); n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and n > 1: n -= 1
    return max(1, n)
def fk(t):
    s = [x for x in re.split(r"[.!?]+", t) if x.strip()]; w = re.findall(r"[A-Za-z']+", t)
    return 0 if not s or not w else 0.39*len(w)/len(s) + 11.8*sum(_syl(x) for x in w)/len(w) - 15.59
def avg_sent(t):
    s = [x for x in re.split(r"[.!?]+|\s—\s|[\U0001F300-\U0001FAFF]", t) if x.strip()]
    return len(re.findall(r"\S+", t))/max(1, len(s))
def without_items(t):
    out = []
    for m in re.finditer(r"(made without|free from|\bno)\s+([^.;:—]+)", t, re.I):
        seg = re.split(r"\s+(?:and start|and made|in |made with|traceable|—)", m.group(2))[0]
        for part in re.split(r",\s*|\s+(?:and|or)\s+|\s*,?\s*no\s+", seg):
            part = part.strip().lower().rstrip("*")
            if part: out.append(part)
    return out

def check(text, channel, headline="", cta=""):
    """channel 'ad_line' = one headline/description inside an ad group: mechanics only; vocabulary is judged per group."""
    v = []
    line = channel == "ad_line"
    if line: channel = "ad"
    t = (headline + " \n" + text).strip()
    low = t.lower()
    # ---- compliance layer ----
    for w in BANNED:
        if re.search(r"(?<![\w-])" + re.escape(w.lower()) + r"(?![\w-])", low): v.append(("VOI-01", w))
    if re.search(r"\b(best|softest|#1|number one)\b(?! (deals?|sellers?|selling))", low) and channel in ("ad", "social", "dr", "dco"):
        v.append(("DR-03", "superlative"))
    for m in re.finditer(r"(up to )?\b(\d+)% off", low):
        n = int(m.group(2))
        if n not in OFFER_PCT: v.append(("MSG-06", f"{n}% off not in offers.csv"))
        elif n in UPTO_PCT and not m.group(1): v.append(("MSG-06", f"{n}% off needs 'up to'"))
    if re.search(r"95%\s+less water", low): v.append(("MSG-10", "retired 95% figure"))
    if "less water" in low and "conventional" not in low: v.append(("MSG-10", "no comparison"))
    if re.search(r"carbon neutral|zero (net )?(carbon )?emissions", low) and "offset" not in low: v.append(("MSG-11", "carbon claim without offsets"))
    if re.search(r"every (piece|garment)[^.]*certified|all organic, all the time|100% organic, all the time", low): v.append(("MSG-09", "absolute organic claim"))
    if re.search(r"\bno (pfas or )?dyes\b|dye-free|undyed", low): v.append(("MSG-16", "implies no dyes"))
    if re.search(r"\bbetter than\b|\bthe leading\b|\bleading brand\b", low): v.append(("MSG-17", "comparative or superiority claim"))
    if re.search(r"hypoallergenic|eczema|sensitive skin|\brash", low): v.append(("LEG-17", "health claim"))
    if re.search(r"\bsustainable\b", low) and not re.search(r"sustainab\w+ (organic|certified|standards)", low): v.append(("LEG-18", "unqualified 'sustainable'"))
    if re.search(r"(?<!cut and sewn in )\bmade in usa\b", low): v.append(("LEG-15", "Made in USA"))
    if re.search(r"free shipping[^.]*\$1\d\d\+|\$100\+", low): v.append(("LEG-12", "threshold not $99+"))
    if re.search(r"flattering for your shape|slimming|hides your|tummy control|problem areas", low): v.append(("VOI-23", "body language"))
    # ---- brand layer ----
    if re.search(r"Earth.?s Favorite", t): v.append(("BRD-08", "retired tagline"))
    if re.search(r"\bPACT\b", t): v.append(("VOI-03", "PACT"))
    with_s = re.findall(r"\w+, [\w' -]+, (?:and|or) ", text); without_s = [m for m in re.findall(r"\w+, [\w' -]+ (?:and|or) ", text) if not re.search(r", (?:and|or) $", m)]
    if with_s and without_s: v.append(("VOI-05", "mixed serial comma in one asset"))
    if re.search(r"\$\d+\.00\b", t): v.append(("VOI-06", "$x.00"))
    if re.search(r"\d+\s?percent", low): v.append(("VOI-07", "percent"))
    if "--" in t: v.append(("VOI-08", "--"))
    emo = len(EMO.findall(t))
    if channel in ("pdp", "web", "email_body", "pdp_module") and emo: v.append(("VOI-09", f"{emo} emoji"))
    if channel == "social" and emo > 3: v.append(("VOI-10", f"{emo} emoji"))
    if channel in ("ad", "dr", "dco") and emo > 1: v.append(("VOI-11", f"{emo} emoji"))
    ex = text.count("!")
    if (channel in ("ad", "pdp", "web", "email_body") and ex) or (channel == "social" and ex > 1): v.append(("VOI-12", f"{ex} '!'"))
    if channel in ("ad", "pdp", "web", "email_body") and len(text.split()) >= 12:
        if len([x for x in re.split(r"[.!?]+", text) if x.strip()]) >= 3 and fk(text) > 10: v.append(("VOI-13", f"grade {fk(text):.1f}"))
        if avg_sent(text) > 18: v.append(("VOI-14", f"{avg_sent(text):.0f} words/sentence"))
    items = without_items(text)
    bad = [i for i in items if not any(a in i for a in APPROVED_WITHOUT) and i != "dyes"]
    if bad and not all(re.match(r"(more|need|longer|matter|exception)", b) for b in bad): v.append(("VOI-16", "unapproved 'without' item: " + "; ".join(bad)))
    if channel == "social":
        tags = re.findall(r"#\w+", text)
        if len(tags) > 3 or (tags and "#organiccotton" not in [x.lower() for x in tags]): v.append(("SOC-01", f"{len(tags)} hashtags"))
    if channel in ("ad",) and not line:
        if headline and len(headline) > 40: v.append(("DR-04", f"headline {len(headline)} chars"))
        first = re.split(r"(?<=[.!?])\s", text.strip())[0] if text.strip() else ""
        if len(first) > 125: v.append(("DR-04", f"first sentence {len(first)} chars"))
        if cta and cta != "Shop now": v.append(("DR-04", f"CTA {cta}"))
        if headline and headline.isupper() and len(headline) > 4: v.append(("DR-05", "all caps"))
    offer_only = bool(re.search(r"% off|\bsale\b|\$\d", low)) and len(t.split()) < 40
    if not line and not offer_only and channel in ("ad", "pdp", "web", "email_body", "social") and len(t.split()) >= 6:
        if not any(w.lower().replace("™", "") in low for w in USE): v.append(("VOI-02", "no brand vocabulary"))
    if channel == "pdp":
        n = len(text.split())
        if not 40 <= n <= 90: v.append(("WEB-02", f"{n} words"))
    return v
