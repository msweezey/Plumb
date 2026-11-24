"""Generalized Plumb brand kit: one check engine + rule builder driven by per-brand config. Pact is the base."""
import re, json
EMO = re.compile("[\U0001F300-\U0001FAFF☀-☄☆-➿‼⁉]")
ACRO = {"USA","US","GOTS","PFAS","NYC","DC","EDC","MAP","TSA","YKK","UV","XL","XS","XXS","RFID","USB","GNO","LA","CEO","BFCM","DTC","AM","PM","MT","ET","PT","II","III","SPF","RN","DM","NY","CA","CO","OK","WARNING","APP10","GOTS"}

def _syl(w):
    n = len(re.findall(r"[aeiouy]+", w.lower())); return max(1, n - (1 if w.lower().endswith("e") and n > 1 else 0))
def fk(t):
    s = [x for x in re.split(r"[.!?]+", t) if x.strip()]; w = re.findall(r"[A-Za-z']+", t)
    return 0 if not s or not w else 0.39*len(w)/len(s) + 11.8*sum(_syl(x) for x in w)/len(w) - 15.59
def nsent(t): return len([x for x in re.split(r"[.!?]+", t) if x.strip()])
def avg_sent(t):
    s = [x for x in re.split(r"[.!?]+|\s—\s|[\U0001F300-\U0001FAFF]", t) if x.strip()]
    return len(re.findall(r"\S+", t))/max(1, len(s))
def caps_words(t): return [w for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in ACRO]

def check(text, channel, cfg, headline="", cta=""):
    """Returns list of (rule_id, evidence). channel: ad | ad_line | social | pdp | web | email_body | subject | pdp_module"""
    text = text.replace("\u2019","'"); headline = headline.replace("\u2019","'")
    v = []; line = channel == "ad_line"
    if line: channel = "ad"
    t = (headline + " \n" + text).strip(); low = t.lower()
    # ================= compliance layer (shared core + brand patterns) =================
    for w in cfg["banned_compliance"]:
        if re.search(r"(?<![\w-])" + re.escape(w.lower()) + r"(?![\w-])", low): v.append(("VOI-01", w))
    if channel in ("ad","social","dr","dco") and re.search(r"\b(best|softest|#1|number one)\b(?! (deals?|sellers?|selling|sale|of the (year|season)))", low):
        v.append(("DR-03", "product superlative"))
    for m in re.finditer(r"(up to )?\b(\d+)% (?:off|on)\b", low):
        n = int(m.group(2))
        if n not in cfg["offer_pct"]: v.append(("MSG-06", f"{n}% off not in offers.csv"))
        elif n in cfg["upto_pct"] and not m.group(1) and not re.search(r"off (everything|sitewide)", low[m.start():m.end()+15]) :
            v.append(("MSG-06", f"{n}% off needs 'up to'"))
        if re.search(rf"{n}% (off|on) (everything|sitewide)", low) and cfg.get("sitewide_has_exclusions"):
            v.append(("MSG-06", "'everything/sitewide' but offer has exclusions"))
    if re.search(r"\bbetter than\b|\bthe leading\b|\bleading brand\b", low): v.append(("MSG-17", "comparative or superiority claim"))
    if re.search(r"hypoallergenic|eczema|sensitive skin|\brash\b|cures?\b|heals?\b", low): v.append(("LEG-17", "health claim"))
    if re.search(r"\bsustainable\b", low) and not re.search(r"sustainab\w+ (organic|certified|standards)", low): v.append(("LEG-18", "unqualified 'sustainable'"))
    if re.search(r"(?<!cut and sewn in )(?<!assembled in )\bmade in (the )?usa\b|\bamerican[- ]made\b|\bmade in colorado\b", low): v.append(("LEG-15", "Made in USA type claim"))
    if re.search(r"\bwaterproof\b", low): v.append(("LEG-21", "'waterproof' (only 'water resistant' is substantiated)"))
    for pat, rid, ev in cfg.get("compliance_patterns", []):
        if re.search(pat, low): v.append((rid, ev))
    m = re.search(r"free (?:u\.s\. |us |standard )?shipping[^.]{0,25}\$(\d+)", low)
    if m and int(m.group(1)) != cfg["ship_threshold"]: v.append(("LEG-12", f"threshold ${m.group(1)} (policy ${cfg['ship_threshold']})"))
    if re.search(r"flattering for your shape|slimming|hides your|tummy control|problem areas", low): v.append(("VOI-23", "body language"))
    # ================= brand layer =================
    for tl in cfg["retired"]:
        if tl.lower() in low: v.append(("BRD-08", f"retired line: {tl}"))
    for pat in cfg["name_bad"]:
        if re.search(pat, t): v.append(("VOI-03", "brand name form"))
    if cfg["serial_comma"] == "consistent":
        ws = re.findall(r"\w+, (?:(?!and |or )[\w'-]+ ){0,2}(?!and |or )[\w'-]+, (?:and|or) ", text); wo = re.findall(r"\w+, (?:(?!and |or )[\w'-]+ ){0,2}(?!and |or )[\w'-]+ (?:and|or) ", text)
        if ws and wo: v.append(("VOI-05", "mixed serial comma in one asset"))
    if cfg["price_zeros"] == "strip" and re.search(r"\$\d+\.00\b", t): v.append(("VOI-06", "$x.00"))
    et = re.sub(r"(^|\n|\s{2,})[\u2728\u2714\u25AA\u2022]", r"\1", t) if cfg.get("emoji_bullets_ok") else t
    emo = len(EMO.findall(et)); lim = cfg["emoji"]
    if channel in lim and lim[channel] is not None:
        lo, hi = lim[channel]
        if emo > hi: v.append(("VOI-10", f"{emo} emoji (max {hi})"))
        if not line and emo < lo and len(t.split()) >= 4: v.append(("VOI-10", f"{emo} emoji (min {lo})"))
    ex = text.count("!") + headline.count("!"); xl = cfg["exclaim"].get(channel)
    if xl is not None and ex > xl: v.append(("VOI-12", f"{ex} '!' (max {xl})"))
    cw = caps_words(t); cl = cfg["caps"].get(channel)
    if cl is not None:
        lo, hi = cl
        if len(cw) > hi: v.append(("VOI-11", f"{len(cw)} all-caps words (max {hi})"))
        if not line and len(cw) < lo and len(t.split()) >= 4: v.append(("VOI-11", f"{len(cw)} all-caps words (min {lo})"))
    if channel in ("ad","pdp","web","email_body") and nsent(text) >= 3 and len(text.split()) >= 12:
        g = fk(text)
        if g > cfg["fk_max"]: v.append(("VOI-13", f"grade {g:.1f} (max {cfg['fk_max']})"))
    if channel in ("ad","web","email_body") and len(text.split()) >= 12 and avg_sent(text) > cfg["sent_max"]:
        v.append(("VOI-14", f"{avg_sent(text):.0f} words/sentence"))
    offer_only = bool(re.search(r"% off|\bsale\b|\$\d|black friday", low)) and len(t.split()) < 40
    quote = cfg.get("quote_posts_ok") and bool(re.match(r'\s*["\u201c]', text)) and bool(re.search(r"[\u2015\u2014-]\s*[A-Z][a-z]+ [A-Z]", text))
    for w in cfg.get("off_category", []):
        if re.search(r"(?<![\w-])" + re.escape(w.lower()) + r"s?(?![\w-])", low): v.append(("BRD-09", f"off-category term: {w}")); break
    if not line and not offer_only and not quote and channel in ("ad","pdp","web","email_body","social") and len(t.split()) >= 6:
        vocab = (cfg.get("vocab_pdp") if channel == "pdp" else None) or cfg["vocab"]
        if not any(re.search(r"(?<![\w])" + re.escape(w.lower()) + r"(?![\w])", low) for w in vocab): v.append(("VOI-02", "no brand vocabulary"))
    for w in cfg["banned_voice"]:
        if re.search(r"(?<![\w-])" + re.escape(w.lower()) + r"(?![\w-])", low): v.append(("VOI-24", f"off-voice word: {w}"))
    if channel == "social":
        tags = re.findall(r"#\w+", text); lo, hi = cfg["hashtags"]
        if len(tags) > hi or (len(tags) < lo): v.append(("SOC-01", f"{len(tags)} hashtags ({lo}-{hi})"))
        if tags and cfg.get("hashtag_required") and cfg["hashtag_required"].lower() not in [x.lower() for x in tags]: v.append(("SOC-01", f"missing {cfg['hashtag_required']}"))
    if channel == "ad" and not line:
        if headline and len(headline) > cfg["headline_max"]: v.append(("DR-04", f"headline {len(headline)} chars"))
        if cta and cta not in cfg["ctas"]: v.append(("DR-04", f"CTA {cta}"))
        if headline and headline.isupper() and not cfg["allcaps_headline_ok"] and len(headline) > 4: v.append(("DR-05", "all-caps headline"))
    if channel == "pdp":
        n = len(text.split()); lo, hi = cfg["pdp_words"]
        if not lo <= n <= hi: v.append(("WEB-02", f"{n} words ({lo}-{hi})"))
        for pat, ev in cfg.get("pdp_required", []):
            if not re.search(pat, t, re.I): v.append(("WEB-03", ev))
    return v

COMPLIANCE = {"VOI-01","DR-03","MSG-06","MSG-07","MSG-12","MSG-17","VOI-23"}
def layer(rid): return "compliance" if rid in COMPLIANCE or rid.startswith(("LEG","ACC")) else "brand"


# ---- Edikted config (from configs.py) ----
import json as _j
CFG = {'key': 'edikted', 'name': 'Edikted', 'quadrant': 'expressive × value', 'personas': ('GZ', 'MIL'), 'banned_compliance': ['eco-friendly', 'chemical-free', 'toxin-free', 'non-toxic', 'detox', 'hypoallergenic', 'antibacterial', 'cures', 'heals', 'eczema', 'dermatologist-approved', 'clinically proven', 'plastic-free', 'zero waste', 'carbon negative', 'climate positive', 'guaranteed', 'miracle', 'sweatshop-free'], 'banned_voice': ['timeless', 'investment piece', 'heirloom', 'intention', 'intentional', 'wellness', 'purposeful', 'executive', 'polished', 'refined', 'understated', 'sophisticated', 'certified'], 'vocab': ['shop', 'fits', 'fit', 'need', 'obsessed', 'babe', 'babes', 'cozy', 'hot', 'dream', 'outfit', 'haul', 'must-have', 'must-haves', 'edikted', 'rotation', 'vibe', 'vibes', 'era', 'energy', 'cute', 'new drop', 'drop', 'sale', 'black friday', 'irl', 'rn', 'girl', 'gno', 'tune in', 'going out', 'set', 'sets'], 'vocab_pdp': ['model wears', 'item care', 'polyester', 'spandex', 'cotton', 'nylon', 'rayon', 'detailing', 'closure', 'fabric', 'measurements', 'neckline', 'polyamide'], 'retired': [], 'name_bad': ['\\bEdicted\\b', '\\bEDICTED\\b', '\\bEdi[ck]ted Clothing\\b'], 'serial_comma': 'any', 'price_zeros': 'any', 'emoji': {'ad': (1, 6), 'social': (1, 5), 'pdp': (0, 0), 'web': (0, 3), 'email_body': (1, 8)}, 'exclaim': {'ad': 3, 'social': 2, 'pdp': 0, 'web': 2, 'email_body': 3}, 'caps': {'ad': (1, 14), 'social': (0, 14), 'pdp': (0, 0), 'web': (0, 10)}, 'fk_max': 9, 'sent_max': 22, 'hashtags': (1, 2), 'hashtag_required': '#EDIKTED', 'off_category': ['suiting', 'boardroom', 'executive', 'backpack', 'daypack', 'trail', 'gear', 'bedding', 'organic cotton', 'gots', 'fair trade'], 'headline_max': 70, 'ctas': ['Shop now'], 'allcaps_headline_ok': True, 'pdp_words': (10, 90), 'pdp_required': [('item care|wash|dry clean', 'missing care line')], 'offer_pct': {80, 50, 70, 10, 60}, 'upto_pct': {80, 70}, 'sitewide_has_exclusions': True, 'ship_threshold': 80, 'compliance_patterns': [('(?:save|\\boff\\b|% on)(?![\\s\\S]*comp value)(?=[\\s\\S]*\\b(?:everything|sitewide)\\b)', 'MSG-12', "% savings without '*Based on comp value' reference")]}

if __name__ == '__main__':
    import sys
    print(check(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'ad', CFG))
