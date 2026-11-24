"""Pact rules: single source for rules.json, guidelines.md and rubric.md.
provenance: observed = seen in Pact's public material (evidence ids E01-E12);
inferred = pattern read across several sources; harness = set by Plumb (not observed, or stricter than observed)."""
import json

RULES = []
def r(id, sec, applies, rule, type_, sev, check, test=None, anchors=None, ok=None, bad=None, src="", prov="observed", prec=None):
    d = dict(id=id, section=sec, applies_to=applies, rule=rule, type=type_, severity=sev, check=check, provenance=prov, source=src)
    if test: d["test"] = test
    if anchors: d["anchors"] = anchors
    if prec: d["precedence"] = prec
    if ok: d["pass"] = ok
    if bad: d["fail"] = bad
    RULES.append(d)

ALL = ["email","sms","social","dr","brand","dco","lp","web","pdp"]
COPY = ALL
ADS = ["social","dr","dco"]

BANNED = ["eco-friendly","chemical-free","toxin-free","non-toxic","detox","hypoallergenic","antibacterial","cures","heals","treats",
          "eczema","dermatologist-approved","clinically proven","plastic-free","zero waste","carbon negative","climate positive","B Corp",
          "Earth's Favorite","cheap","flawless","guaranteed","#1","miracle","game-changer","insane","act now","don't miss out","once-in-a-lifetime","sweatshop-free"]
USE = ["organic cotton","GOTS-certified","Fair Trade Certified™","soft","breathable","everyday","essentials","clean","gentle on skin","made without",
       "wellness","feel-good","easy","comfort","layers","standards","certified","real life","intention","restock"]

# ---------------- BRD essence (8) ----------------
r("BRD-01","BRD",COPY,"Purpose: make getting dressed an act of self-care, with clothes made to clear, certified standards.","soft","major","AI judge",
  anchors={"1":"Reads as generic basics or fast fashion","4":"Ties the product to everyday wellness and verified standards"},src="E02",prov="observed")
r("BRD-02","BRD",COPY,"Positioning: certified organic essentials that are gentle on skin and priced for everyday life.","soft","major","AI judge",
  anchors={"1":"Positions as luxury or as cheapest","4":"Clean, certified, and within reach in one idea"},src="E02,E08",prov="inferred")
r("BRD-03","BRD",COPY,"Lead with personal wellness (what touches your skin); planet and people benefits support, never lead.","soft","major","AI judge",
  anchors={"1":"Opens on saving the planet","4":"Opens on skin, comfort or daily routine, then proof"},src="E02,E08",prov="inferred",
  ok="What touches your skin every day matters.",bad="Save the planet one pair of undies at a time.")
r("BRD-04","BRD",COPY,"Personality trait 1 — Caring: is warm and reassuring; is not preachy or guilt-driven.","soft","minor","AI judge",
  anchors={"1":"Shames the reader's current choices","4":"Invites, never scolds"},src="E02,E08",prov="inferred")
r("BRD-05","BRD",COPY,"Personality trait 2 — Clear: is plain about what's in the clothes; is not technical or jargon-heavy.","soft","minor","AI judge",
  anchors={"1":"Stacks certifications and acronyms","4":"Explains one standard in plain words"},src="E04",prov="inferred")
r("BRD-06","BRD",COPY,"Personality trait 3 — Grounded: is honest about limits; is not absolute or perfectionist.","soft","minor","AI judge",
  anchors={"1":"Claims perfection","4":"Committed to progress, specific about what is verified"},src="E04",prov="observed")
r("BRD-07","BRD",COPY,"Personality trait 4 — Easygoing: is relaxed and a little playful; is not slangy or try-hard outside social.","soft","minor","AI judge",
  anchors={"1":"Slang in email or PDP","4":"Light touch, fits the channel"},src="E08,E09",prov="inferred")
r("BRD-08","BRD",COPY,"Current tagline is 'Dress Yourself Well'. Never use the retired line \"Earth's Favorite\" in any form.","hard","major","auto",
  test={"not_contains_any":["Earth's Favorite","Earth’s Favorite","Earths Favorite"]},src="E01,E02",prov="observed",
  ok="Dress Yourself Well",bad="Earth's Favorite™ Clothing")

# ---------------- VOI voice (25) ----------------
r("VOI-01","VOI",COPY,"Never use any word on the banned list (30 words) in customer-facing copy.","hard","major","auto",
  test={"not_contains_any_ci":BANNED,"exceptions":["product names from catalog"]},src="harness, E04",prov="harness")
r("VOI-02","VOI",COPY,"Prefer the brand vocabulary (20 words); at least one brand word per asset.","hard","minor","auto",
  test={"contains_any_ci":USE},src="E01-E09",prov="observed")
r("VOI-03","VOI",COPY,"Write the brand name as 'Pact' in running copy. Never 'PACT' or 'pact' in sentences.","hard","major","auto",
  test={"regex_absent":r"\bPACT\b(?!-)|(?<![@#/\w])pact\b(?!\.com)"},src="E07,E08,E10",prov="observed",ok="Pact makes organic essentials.",bad="PACT is organic cotton.")
r("VOI-04","VOI",["brand","social","web"],"The spaced wordmark 'p a c t' appears only as a logo or display lockup, never in a sentence.","hard","minor","auto",
  test={"regex_absent_in_body":r"p a c t"},src="E08,E10",prov="observed")
r("VOI-05","VOI",COPY,"Serial comma is optional (Pact uses both); be consistent within one asset.","hard","minor","auto",test={"serial_comma":"consistent_within_asset"},src="realcopy: 13 lists with, 9 without",prov="observed",
  ok="soft, breathable, and easy ... calm, clean, and simple",bad="soft, breathable, and easy ... calm, clean and simple")
r("VOI-06","VOI",COPY,"Prices drop trailing zeros: $10 not $10.00; keep cents only when non-zero.","hard","minor","auto",test={"regex_absent":r"\$\d+\.00\b"},src="E08",prov="observed")
r("VOI-07","VOI",COPY,"Percentages as numerals with %: '40%' not '40 percent'.","hard","minor","auto",test={"regex_absent":r"\d+\s?percent"},src="E01",prov="observed")
r("VOI-08","VOI",COPY,"Use a spaced em dash ' — ' for asides; never double hyphens.","hard","minor","auto",test={"regex_absent":r"--"},src="E08",prov="observed")
r("VOI-09","VOI",["email","web","pdp","lp"],"No emoji in email body, web, PDP or landing page copy (subject lines may carry one).","hard","minor","auto",test={"emoji_max":0,"fields":["body","pdp","lp"]},src="E01,E07",prov="observed")
r("VOI-10","VOI",["social"],"Organic social: up to 3 emoji per caption.","hard","minor","auto",test={"emoji_max":3},src="E09",prov="observed")
r("VOI-11","VOI",["dr","dco"],"Paid ads: no more than 1 emoji per ad.","hard","minor","auto",test={"emoji_max":1},src="E08",prov="observed")
r("VOI-12","VOI",COPY,"Exclamation marks: none in ads, PDP, web and email body; one per social caption at most.","hard","minor","auto",test={"exclaim_max":{"ad":0,"pdp":0,"web":0,"email_body":0,"social":1}},src="realcopy: 0 of 29 ads, max 1 per IG caption",prov="observed")
r("VOI-13","VOI",[c for c in COPY if c!="social"],"Reading level: grade 10 or below (Flesch-Kincaid) for ads, email, web and PDP copy of 3+ sentences; shorter copy and social are judged, not scored.","hard","minor","auto",test={"fk_grade_max":10},src="realcopy: ads median 7.9, p90 8.9",prov="observed")
r("VOI-14","VOI",[c for c in COPY if c!="social"],"Sentences average 18 words or fewer (ads, email, web, PDP); a spaced em dash counts as a break.","hard","minor","auto",test={"avg_sentence_words_max":18},src="realcopy: ads median 10, max 21 (SEO copy)",prov="observed")
r("VOI-15","VOI",COPY,"Speak to the reader as 'you'; refer to the brand as 'we' or 'Pact', never 'the company'.","hard","minor","auto",test={"regex_absent":r"\bthe company\b"},src="E02,E08",prov="observed")
r("VOI-16","VOI",COPY,"'Made without' / 'free from' / 'no' lists name only the approved items (harsh chemicals, toxic dyes, PFAS), in any order and any subset. Never add other substances (bare 'dyes' is MSG-16).","hard","major","auto",
  test={"without_list_items_subset_of":["harsh chemicals","toxic dyes","PFAS"]},src="realcopy: 10 lists, 5 orderings",prov="observed")
r("VOI-17","VOI",COPY,"Tone — promo: upbeat and direct about the deal, never frantic.","soft","major","AI judge",anchors={"1":"Countdown panic, stacked urgency","4":"Clear deal, calm confidence"},src="E01,E08",prov="inferred",
  ok="Everything is up to 40% off through Sunday.",bad="HURRY!!! Prices this low won't last!!!")
r("VOI-18","VOI",COPY,"Tone — service: practical, specific, owns the next step.","soft","minor","AI judge",anchors={"1":"Vague or defensive","4":"Names the fix and the timeline"},src="harness",prov="harness",
  ok="Your order shipped today. Track it here.",bad="We are experiencing delays beyond our control.")
r("VOI-19","VOI",COPY,"Tone — apology: brief, sincere, no excuses, one concrete remedy.","soft","major","AI judge",anchors={"1":"Blames others","4":"Owns it and offers a fix"},src="harness",prov="harness",
  ok="We got this wrong. A replacement is on its way.",bad="Due to unprecedented demand, mistakes happen.")
r("VOI-20","VOI",COPY,"Tone — onboarding: welcoming, explains what makes Pact different in one idea per message.","soft","minor","AI judge",anchors={"1":"Info dump","4":"One clear idea, one next step"},src="E05,E09",prov="inferred",
  ok="Welcome. Here's what 'certified organic' means for what you wear.",bad="Welcome! Here are 12 things about us, our certifications, our mission...")
r("VOI-21","VOI",COPY,"Tone — sensitive news (recall, price change, delay): plain facts first, no promotional lines.","soft","critical","AI judge",anchors={"1":"Sells during bad news","4":"Facts, impact, what to do"},src="harness",prov="harness",
  ok="We've paused sales of one style while we check a fabric issue.",bad="Oops! While we sort this out, shop our new arrivals!")
r("VOI-22","VOI",["social"],"Social may use light internet phrases already in brand use (e.g. 'girl math', 'restock'); never slurs, body comments or slang that mocks.","soft","minor","AI judge",anchors={"1":"Slang that punches down","4":"Playful, kind"},src="E08,E09",prov="observed")
r("VOI-23","VOI",COPY,"No body-shaming or body-fixing language ('flattering for your shape', 'hides', 'slimming').","hard","major","auto",test={"not_contains_any_ci":["flattering for your shape","slimming","hides your","tummy control","problem areas"]},src="harness",prov="harness")
r("VOI-24","VOI",COPY,"No fake familiarity or guilt ('you NEED this', 'shame on').","hard","minor","auto",test={"not_contains_any_ci":["you need this","shame on","you deserve better than"]},src="harness",prov="harness")
r("VOI-25","VOI",COPY,"Sounds like Pact: warm, clear, grounded, easy (matches golden examples).","soft","major","AI judge",anchors={"1":"Could be any brand","4":"Indistinguishable from golden examples"},src="history/",prov="inferred")

# ---------------- MSG messaging (15) ----------------
r("MSG-01","MSG",COPY,"Use only claims listed in library/claims.md, worded as approved.","hard","critical","auto",test={"claims_from":"library/claims.md"},src="claims.md",prov="harness")
r("MSG-02","MSG",COPY,"Value prop 1 — Gentle on skin: certified organic cotton made without harsh chemicals, toxic dyes and PFAS.","soft","major","AI judge",anchors={"1":"Missing or wrong proof","4":"Prop plus one proof point"},src="E02,E07",prov="observed")
r("MSG-03","MSG",COPY,"Value prop 2 — Verified standards: GOTS-certified organic cotton, made in Fair Trade Certified™ factories.","soft","major","AI judge",anchors={"1":"Vague 'sustainable'","4":"Names the certification"},src="E03,E04",prov="observed")
r("MSG-04","MSG",COPY,"Value prop 3 — Organic for everyday life: essentials priced for real routines (proof: prices from catalog).","soft","major","AI judge",anchors={"1":"Positions as premium","4":"Price proof from the catalog"},src="E08",prov="observed",
  ok="Think organic costs more? Our leggings start at $20.",bad="Luxury organic at a premium worth paying.")
r("MSG-05","MSG",COPY,"'Starting at $X' only when an active, in-stock SKU is currently priced at $X.","hard","critical","auto",test={"lookup":"catalog_products.csv","field":"price","rule":"min(active price in group) == X"},src="E08",prov="harness")
r("MSG-06","MSG",COPY,"'Up to X% off' only with the maximum stated in offers.csv for that offer.","hard","critical","auto",test={"lookup":"catalog_offers.csv","rule":"X <= offer max"},src="E01",prov="harness")
r("MSG-07","MSG",COPY,"Say 'made with organic cotton' for blends; say '100% organic cotton' only when material is 100% organic cotton.","hard","critical","auto",test={"lookup":"catalog_products.csv","field":"material"},src="E07",prov="observed")
r("MSG-08","MSG",COPY,"Call a product 'GOTS-certified' only when gots_certified = yes. Pending SKUs: 'made with organic cotton'.","hard","critical","auto",test={"lookup":"catalog_products.csv","field":"gots_certified","equals":"yes"},src="E04",prov="harness")
r("MSG-09","MSG",COPY,"Never say every Pact product is certified organic or 100% organic; socks and blends contain recycled nylon or elastane.","hard","critical","auto",
  test={"not_contains_any_ci":["every piece is gots","every garment we make is certified","100% organic, all the time","all organic, all the time"]},src="E04,E09 vs catalog",prov="harness")
r("MSG-10","MSG",COPY,"Water and energy claim: only '81% less water and 62% less energy than conventional cotton', with the comparison. The 95% water figure is retired.","hard","critical","auto",
  test={"regex_absent":r"95%\s+less water","if_contains":"less water","must_contain":"conventional cotton"},src="E06 vs E12",prov="harness")
r("MSG-11","MSG",COPY,"Carbon claims must say how: 'carbon neutral through verified offsets with SimpliZero'. Never 'zero emissions' alone.","hard","critical","auto",
  test={"if_contains_any":["carbon neutral","zero net carbon"],"must_contain":"offset"},src="E03",prov="harness")
r("MSG-12","MSG",COPY,"Do not disparage other brands or certifications by name in ads ('If it's not GOTS, it's not organic' stays on the Standards page only).","hard","major","auto",
  test={"applies_to":ADS,"not_contains_any_ci":["it's not organic","not real organic","OEKO-TEX","OCS"]},src="E04",prov="harness")
r("MSG-13","MSG",COPY,"Boilerplate (short, 50 words) and (long, 100 words) are used word for word from library/copy-bank.md.","hard","minor","auto",test={"exact_match":"copy-bank.md#boilerplate"},src="harness",prov="harness")
r("MSG-14","MSG",COPY,"Name product lines exactly as in the catalog (e.g. 'On The Go-To Legging', 'Room Service Sateen').","hard","major","auto",test={"lookup":"catalog_products.csv","field":"name"},src="E10",prov="observed")
r("MSG-16","MSG",COPY,"Never imply the clothes have no dyes; say 'toxic dyes', not 'dyes'.","hard","critical","auto",test={"regex_absent":r"\bno (pfas or )?dyes\b|dye-free|undyed"},src="realcopy held-out ad",prov="harness")
r("MSG-17","MSG",COPY,"No comparative or superiority claims ('better than denim', 'the leading brand') unless in claims.md.","hard","major","auto",test={"regex_absent":r"\bbetter than\b|\bthe leading\b|\bleading brand\b"},src="realcopy held-out PDP",prov="harness")
r("MSG-15","MSG",COPY,"Message fits the shared persona (GZ, MIL, GX, BB) and segment named in the task.","soft","major","AI judge",anchors={"1":"Generic","4":"Clearly for that persona, uses a relevant proof"},src="harness/shared/personas.md",prov="harness")

# ---------------- LOG logo (12) ----------------
for i,(t,ty,sev,chk) in enumerate([
 ("Use logo-full (black wordmark) on light backgrounds.","hard","major","auto"),
 ("Use logo-mono (white wordmark) on dark or photo backgrounds.","hard","major","auto"),
 ("Use logo-icon only where space is under 120 px wide (avatars, favicons).","hard","minor","auto"),
 ("Clear space on all sides equals the height of the letter 'p'.","hard","minor","auto"),
 ("Minimum size digital: 64 px wide for the wordmark.","hard","minor","auto"),
 ("Minimum size print: 18 mm wide for the wordmark.","hard","minor","auto"),
 ("Approved placements: top-left, top-center, bottom-center end card, bottom-left footer.","hard","minor","auto"),
 ("Never recolor the wordmark outside black or white.","hard","major","auto"),
 ("Never stretch, rotate, outline or add effects to the wordmark.","hard","major","AI judge"),
 ("Never set the wordmark in caps ('PACT') or re-type it in another font.","hard","major","AI judge"),
 ("Never use the retired caps logo file (brand/deprecated/logo-legacy.svg).","hard","major","auto"),
 ("Never place the logo on busy image areas without the mono version and 4.5:1 contrast.","hard","minor","AI judge")],1):
    r(f"LOG-{i:02d}","LOG",["email","social","dr","brand","dco","lp","web"],t,ty,sev,chk,src="E11",prov=("observed" if i in (1,8,10) else "harness"))

# ---------------- COL color (12) ----------------
cols = [("COL-01","Primary: Warm Charcoal #4D4A43 for body text, UI text and primary buttons (the site's most-used color).","observed"),
        ("COL-02","Primary: Pact Black #040404 for the wordmark only.","observed"),
        ("COL-03","Secondary: Deep Charcoal #3E3B36 for hover and pressed states; Wine #7D2D3B for Sale and Gift navigation; Tan #A98D6D for loyalty (Pact Balance) accents only.","observed"),
        ("COL-04","Neutrals: White #FFFFFF, Off-White #F7F7F5 and Stone #EBEAE8 for backgrounds; Grey #CAC9C7 for borders; Muted Grey #94928E for non-essential labels at large sizes only.","observed"),
        ("COL-05","Alerts: Sale Red #C8422D for sale prices, errors and final-sale markers; Earth Green #38761D for sustainability headings and success messages.","observed"),
        ("COL-06","Reference colors by hex only (no Pantone); use only the 12 palette hex values.","harness"),
        ("COL-07","Usage share: neutrals about 70%, primaries about 20%, secondaries about 8%, alerts under 2%.","inferred"),
        ("COL-08","Text pairings: use only the approved pairings in brand_tokens.json (all 4.5:1 or higher).","harness"),
        ("COL-09","Never set body text in Grey, Muted Grey or Tan on White, Off-White or Stone (below 4.5:1).","harness"),
        ("COL-10","Sale Red on Stone (4.09:1) only at 18.66 px bold or 24 px and above.","harness"),
        ("COL-11","Struck-through reference prices use Warm Charcoal, not Muted Grey (site's grey fails AA).","harness"),
        ("COL-12","No gradients; flat color only.","observed")]
for cid,t,pv in cols:
    r(cid,"COL",["email","social","dr","brand","dco","lp","web"],t,"hard","minor" if cid not in ("COL-06","COL-09","COL-11") else "major","auto",src="E13 (site CSS), brand_tokens.json",prov=pv)

# ---------------- TYP typography (10) ----------------
typ = ["Display family: Juana (serif; light 300, regular 400, semibold 600, with italics) for banners, collection and marketing headings and page titles.",
       "Body and UI family: Averta (sans; 300, 400, 700, 900) for body copy, navigation, buttons and forms.",
       "Product family: GT Eesti (sans; light 300, regular 400) for product titles and the price block.",
       "Fallback stacks: Juana → Georgia, 'Times New Roman', serif; Averta and GT Eesti → 'Helvetica Neue', Arial, sans-serif (as in site CSS).",
       "Hierarchy: H1, H2, H3, body, caption, legal; one H1 per page or email.",
       "Web sizes: banner headings 24-28 px Juana; PDP title 20 px GT Eesti light; body 16 px Averta; price 14 px GT Eesti; legal 12 px.",
       "Email sizes: H1 28 px, H2 22 px, body 16 px, legal 12 px.",
       "Social: on-image headline at least 48 px on a 1080 px canvas, Juana or Averta only.",
       "Buttons: Averta, sentence case, 6 px radius; uppercase with 2 px tracking only in loyalty modules.",
       "Never use third-party widget fonts (Nunito Sans, Poppins, Open Sans) in brand assets."]
for i,t in enumerate(typ,1):
    r(f"TYP-{i:02d}","TYP",["email","social","dr","brand","dco","lp","web"],t,"hard","minor","auto",src="E13 (site @font-face and CSS)",prov=("harness" if i in (5,7,8,10) else "observed"))

# ---------------- IMG imagery (15) ----------------
img = [("Image types: product on figure, flat lay, home and bed scenes, texture close-ups, lifestyle in daily routines.","soft","minor","AI judge","inferred"),
 ("Real-feeling people in everyday settings; natural light; warm neutral tones.","soft","minor","AI judge","inferred"),
 ("Show a range of ages, bodies and skin tones across a campaign.","soft","major","AI judge","harness"),
 ("No retouching that changes body shape.","hard","major","AI judge","harness"),
 ("Texture close-ups must show the actual fabric of the SKU named.","hard","major","AI judge","harness"),
 ("Product color in imagery matches the catalog color name.","hard","major","AI judge","harness"),
 ("No medical or clinical imagery (lab coats, dermatology visuals) implying health benefits.","hard","critical","AI judge","harness"),
 ("No nature-as-proof imagery (earth from space, leaves on product) next to a green claim.","hard","major","AI judge","harness"),
 ("Use the 20-tag vocabulary in library/images tags for every asset.","hard","minor","auto","harness"),
 ("Icons: 24 line icons, 1.5 px stroke, Pact Black only.","hard","minor","auto","harness"),
 ("Certification marks (GOTS, Fair Trade) appear only next to certified SKUs and at official artwork.","hard","critical","auto","harness"),
 ("Do/don't pairs: 6 pairs in library/images/do-dont.","soft","minor","AI judge","harness"),
 ("AI-image policy: AI-generated people may not appear in ads; AI-generated product images are labeled and never replace real product shots on PDPs.","hard","critical","auto","harness"),
 ("Reviews shown in imagery use real review text from reviews.csv only.","hard","critical","auto","harness"),
 ("Alt text describes product, color and setting in one sentence.","hard","minor","auto","harness")]
for i,(t,ty,sev,chk,pv) in enumerate(img,1):
    r(f"IMG-{i:02d}","IMG",["email","social","dr","brand","dco","lp","web","pdp"],t,ty,sev,chk,src="E08,E11",prov=pv)

# ---------------- LAY layout (8) ----------------
lay = ["Web grid: 12 columns, 24 px gutters, 1280 px max width.","Email grid: single column, 600 px wide.",
       "Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64 px.","One focal point per module.",
       "Price sits directly under the product name.","CTA is the last element in a module, never above the proof.",
       "Generous white space: at least 32 px between modules.","Legal lines sit in the footer, never inside a hero."]
for i,t in enumerate(lay,1):
    r(f"LAY-{i:02d}","LAY",["email","lp","web","dco"],t,"hard" if i in (1,2,3,5,7,8) else "soft","minor","auto" if i in (1,2,3,7,8) else "AI judge",src="harness",prov="harness")

# ---------------- ACC accessibility (12) ----------------
acc = [("Standard: WCAG 2.2 AA for every asset.","major"),("Body text contrast at least 4.5:1.","major"),("Large text (24 px+, or 18.66 px bold) at least 3:1.","major"),
       ("Every image has alt text; decorative images use empty alt.","major"),("Video has captions; 15-second hooks have on-screen text matching audio.","major"),
       ("Link text describes the destination; never 'click here'.","minor"),("Buttons at least 44 x 44 px.","minor"),("Never use color alone to show a sale or status.","minor"),
       ("Email has a plain-text version.","minor"),("Headings in order; no skipped levels.","minor"),("Emoji are never the only carrier of meaning.","minor"),
       ("Footer links to the accessibility page (/accessibility).","minor")]
for i,(t,sev) in enumerate(acc,1):
    r(f"ACC-{i:02d}","ACC",["email","sms","social","dr","brand","dco","lp","web","pdp"],t,"hard",sev,"auto",src="WCAG 2.2; E01 footer",prov=("observed" if i==12 else "harness"))

# ---------------- LEG legal (20): 9 core + 11 retail/Pact overlay ----------------
leg = [
 ("LEG-01","Marketing email: accurate sender, honest subject, physical address '4725 Walnut St, Boulder, CO 80301', working unsubscribe honored within 10 business days.","critical","auto",["email"],"FTC CAN-SPAM; E01","observed"),
 ("LEG-02","SMS: send only where sms_consent_type = 'prior express written consent'; include brand name and 'Reply STOP to opt out'; send 8am-8pm recipient local time.","critical","auto",["sms"],"TCPA/FCC; state quiet-hours laws","harness"),
 ("LEG-03","Privacy link in every email, SMS program terms and landing page footer.","major","auto",["email","sms","lp","web"],"E01","observed"),
 ("LEG-04","Trademark symbols: 'Fair Trade Certified™' with ™ on first mention.","minor","auto",COPY,"E03,E04","observed"),
 ("LEG-05","Every objective claim has substantiation listed in claims.md.","critical","auto",COPY,"FTC","harness"),
 ("LEG-06","Endorsements: creators and partners disclose the material connection (#ad, 'Paid partnership' label, or 'gifted') in the first line; brand reposts keep the disclosure.","critical","auto",["social","dr","dco"],"FTC Endorsement Guides; E09","harness"),
 ("LEG-07","Reviews: quote only reviews from reviews.csv with usable_in_marketing = yes; label incentivized reviews as incentivized; never use insider or edited reviews.","critical","auto",COPY,"FTC fake-reviews rule; E07","observed"),
 ("LEG-08","AI content: disclose AI-generated or AI-altered realistic people or scenes, and declare AI creative in Meta, Google and TikTok ad settings.","critical","auto",["social","dr","dco","brand"],"EU AI Act Art. 50; NY synthetic performer law; platform policies","harness"),
 ("LEG-09","Accessibility statement link and copyright line '© 2026 Pact' in web and email footers.","minor","auto",["email","web","lp"],"E01","harness"),
 ("LEG-10","Reference prices: show 'MSRP' or a was-price only when catalog_price_history.csv says msrp_comparison_allowed = yes (charged at MSRP at least 3 of the last 12 months).","critical","auto",COPY,"16 CFR 233.1/233.3; E01,E07","harness"),
 ("LEG-11","Promotions show the end date and time (Mountain Time) and any code, minimum spend and exclusions from offers.csv; never reference ended offers.","major","auto",COPY,"Brand policy; E01","harness"),
 ("LEG-12","Free shipping: state the threshold exactly as '$99+' (standard shipping, contiguous US).","major","auto",COPY,"E05 (site meta says $100+; policy table governs)","observed"),
 ("LEG-13","Final sale: clearance items say 'Final sale, not eligible for return or exchange' wherever they are promoted.","major","auto",COPY,"E05","observed"),
 ("LEG-14","Textile origin: every online product description states origin ('Imported' or the qualified USA line from catalog).","critical","auto",["pdp","web","dco"],"Textile Products Identification Act; FTC","harness"),
 ("LEG-15","Made in USA: only the qualified line from catalog ('Cut and sewn in USA from imported organic cotton fabric'); never unqualified 'Made in USA'.","critical","auto",COPY,"FTC Made in USA rule","harness"),
 ("LEG-16","Fiber content: list fibers by percentage, in descending order, exactly as catalog material. If material is blank, do not state fiber content.","critical","auto",["pdp","web","dco"],"Textile Act; FTC","harness"),
 ("LEG-17","No health, disease or skin-condition claims (eczema, rashes, infections, allergies, 'hypoallergenic', 'detox').","critical","auto",COPY,"FTC Act s.5; FDA device rules","harness"),
 ("LEG-18","Green claims: no unqualified 'sustainable', 'eco-friendly' or 'green'; qualify with the specific certification or attribute.","major","auto",COPY,"FTC Green Guides","harness"),
 ("LEG-19","'Made without PFAS' only for SKUs with pfas_free = yes; never 'PFAS-free guaranteed' or 'tested free of all chemicals'.","critical","auto",COPY,"State PFAS-in-apparel laws (e.g. CA AB 1817)","harness"),
 ("LEG-20","Loyalty: describe Pact Balance as '5% Pact Credit on orders' and link terms; credit is not cash.","minor","auto",COPY,"E01","observed"),
]
for (lid,t,sev,chk,ap,src,pv) in leg:
    r(lid,"LEG",ap,t,"hard",sev,chk,src=src,prov=pv, prec=("LEG beats any VOI, MSG or channel rule" if sev=="critical" else None))

# ---------------- asset types ----------------
r("EML-01","EML",["email"],"Subject line 25-50 characters.","hard","major","auto",test={"field":"subject","length":[25,50]},src="harness",prov="harness")
r("EML-02","EML",["email"],"Preheader 40-90 characters and never repeats the subject.","hard","major","auto",test={"field":"preheader","length":[40,90],"not_equal":"subject"},src="harness",prov="harness")
r("EML-03","EML",["email"],"Sender name 'Pact'; reply-to a monitored address.","hard","minor","auto",src="harness",prov="harness")
r("EML-04","EML",["email"],"One primary CTA per email; button text 2-4 words in sentence case (e.g. 'Shop the sale').","hard","major","auto",test={"cta_count":1,"cta_words":[2,4]},src="E08",prov="inferred")
r("EML-05","EML",["email"],"Footer: address, unsubscribe, preferences, privacy, accessibility, '© 2026 Pact'.","hard","critical","auto",src="E01",prov="observed")
r("EML-06","EML",["email"],"Promo emails carry offer terms in a terms line above the footer.","hard","major","auto",src="harness",prov="harness")
r("EML-07","EML",["email"],"Transactional emails (order, shipping) lead with order facts; at most one product recommendation, below the order details.","hard","critical","auto",test={"recommendations_max":1,"position":"after_order_details"},src="CAN-SPAM primary purpose",prov="harness")
r("EML-08","EML",["sms"],"SMS: 160 characters max including 'Reply STOP to opt out'; one link; no emoji in the first 20 characters.","hard","major","auto",test={"length_max":160,"must_contain":"Reply STOP to opt out","links_max":1},src="TCPA/CTIA",prov="harness")
r("SOC-01","SOC",["social"],"Instagram: hook in the first 125 characters; 0-3 hashtags, and #organiccotton whenever hashtags are used.","hard","minor","auto",test={"hashtags":[0,3],"if_any_must_contain":"#organiccotton"},src="realcopy: 0-2 hashtags on 7 posts",prov="observed")
r("SOC-02","SOC",["social"],"TikTok: caption up to 150 chars; 2-4 hashtags; on-screen text in the top 80% safe zone.","hard","minor","auto",test={"length_max":150,"hashtags":[2,4]},src="platform norms",prov="harness")
r("SOC-03","SOC",["social"],"Pinterest: title up to 100 chars, description up to 500 chars, no hashtags, keyword-led.","hard","minor","auto",test={"title_max":100,"desc_max":500,"hashtags":[0,0]},src="platform norms",prov="harness")
r("SOC-04","SOC",["social"],"LinkedIn (S2): no emoji in first line; 1,300 characters max; up to 3 hashtags.","hard","minor","auto",test={"length_max":1300,"hashtags":[0,3]},src="platform norms",prov="harness")
r("SOC-05","SOC",["social"],"Comment-to-get-link posts state what the reader will receive and that it comes by DM.","hard","minor","auto",src="E09",prov="observed")
r("SOC-06","SOC",["social"],"Giveaways state eligibility, end date, 'not affiliated with Instagram' and link to rules.","hard","critical","auto",src="E09; platform promo rules",prov="observed")
r("SOC-07","SOC",["social"],"Replies: answer the question, never argue; move order issues to DM or support; never make a claim not in claims.md.","soft","critical","AI judge",anchors={"1":"Argues or makes a health claim","4":"Kind, specific, on-claim"},src="harness",prov="harness")
r("SOC-08","SOC",["social"],"Video hook: first 2 seconds name the benefit or the price; never fake urgency.","soft","minor","AI judge",anchors={"1":"Slow or clickbait","4":"Benefit or price immediately"},src="E08",prov="inferred")
r("DR-01","DR",["dr"],"Search headlines max 30 characters; descriptions max 90.","hard","critical","auto",test={"headline_max":30,"description_max":90},src="Google Ads",prov="harness")
r("DR-02","DR",["dr"],"Each ad group has 15 unique headlines and 4 unique descriptions.","hard","major","auto",test={"headlines":15,"descriptions":4,"unique":True},src="Google Ads",prov="harness")
r("DR-03","DR",["dr","social","dco"],"No product superlatives ('best', '#1', 'softest') unless listed in claims.md. 'Best deals' and 'best sellers' are allowed.","hard","critical","auto",test={"superlative_regex":r"\b(best|softest|#1|number one)\b(?! (deals?|sellers?|selling))"},src="FTC; realcopy",prov="harness")
r("DR-04","DR",["dr","social"],"Paid social: first sentence of primary text within 125 characters; headline up to 40; CTA 'Shop now'.","hard","minor","auto",test={"first_sentence_max":125,"headline_max":40,"cta":"Shop now"},src="realcopy: headlines max 34 chars, CTA always Shop now",prov="observed")
r("DR-05","DR",["dr","social","dco"],"Paid ad headlines in Title Case (default) or sentence case; never all caps.","hard","minor","auto",src="realcopy: 23 of 29 Title Case",prov="observed")
r("DR-06","DR",["dr","social"],"Ad copy matches the landing page offer, price and dates.","hard","critical","auto",src="harness",prov="harness")
r("BRA-01","BRA",["brand"],"Tagline 'Dress Yourself Well' set as written, title case, no punctuation.","hard","major","auto",src="E01",prov="observed")
r("BRA-02","BRA",["brand"],"Video lengths :06, :15, :30; end card shows logo and tagline for at least 1.5 seconds.","hard","minor","auto",src="harness",prov="harness")
r("BRA-03","BRA",["brand"],"Concept extends 'what touches your skin matters'; never planet-guilt as the lead.","soft","major","AI judge",anchors={"1":"Off-idea","4":"Extends the brand idea"},src="E02,E08",prov="inferred")
r("BRA-04","BRA",["brand"],"Key visual: warm neutral palette, one product hero, generous white space.","soft","minor","AI judge",anchors={"1":"Busy, off-palette","4":"Calm, on-palette"},src="E11",prov="inferred")
r("DCO-01","DCO",["dco"],"Slots: headline (40), body (125), price, compare_price, product_name, cta, badge; each has a fallback.","hard","major","auto",src="E08 (DPA template)",prov="observed")
r("DCO-02","DCO",["dco"],"Price slot uses the feed value with trailing zeros stripped ('$98').","hard","critical","auto",src="E08",prov="observed")
r("DCO-03","DCO",["dco"],"compare_price slot renders only when msrp_comparison_allowed = yes; otherwise it is empty.","hard","critical","auto",src="16 CFR 233",prov="harness")
r("DCO-04","DCO",["dco"],"No slot overflow; text never truncates mid-word.","hard","major","auto",src="harness",prov="harness")
r("DCO-05","DCO",["dco"],"Discontinued or final-sale SKUs are excluded from the feed.","hard","major","auto",src="harness",prov="harness")
r("LP-01","LP",["lp"],"Hero headline repeats the ad's offer or promise word for word or near it.","hard","major","AI judge",src="harness",prov="harness")
r("LP-02","LP",["lp"],"One conversion goal; one primary CTA repeated at most twice.","hard","major","auto",src="harness",prov="harness")
r("LP-03","LP",["lp"],"Three benefit blocks map to the three value props.","soft","minor","AI judge",anchors={"1":"Random benefits","4":"One block per value prop with proof"},src="harness",prov="harness")
r("LP-04","LP",["lp"],"FAQ answers shipping ($99+), returns (30 days; clearance final sale) and certifications.","hard","major","auto",src="E05",prov="observed")
r("LP-05","LP",["lp"],"Legal footer present with offer terms, privacy and accessibility links.","hard","critical","auto",src="E01",prov="observed")
r("WEB-01","WEB",["web","pdp"],"Page title 60 characters max; meta description 160 max.","hard","minor","auto",test={"title_max":60,"meta_max":160},src="SEO",prov="harness")
r("WEB-02","WEB",["pdp"],"PDP description 40-90 words: one-line hook, what it is, how it fits, how to wear it.","hard","major","auto",test={"words":[40,90]},src="E07",prov="observed")
r("WEB-03","WEB",["pdp"],"PDP 'Wellness ingredients' module: MADE WITH / MADE WITHOUT / CERTIFIED, from catalog fields.","hard","major","auto",src="E07",prov="observed")
r("WEB-04","WEB",["pdp"],"Footnote blends: '*Also with X% elastane for stretch and recovery' (or the recycled fiber).","hard","major","auto",src="E07",prov="observed")
r("WEB-05","WEB",["pdp"],"Never invent fit, fabric weight, thread count or features not in catalog.","hard","critical","auto",src="harness",prov="harness")
r("WEB-06","WEB",["pdp"],"Product names start with 'Organic' as in the catalog.","hard","minor","auto",src="E07,E10",prov="observed")

COMPLIANCE_IDS = {"VOI-01","VOI-21","VOI-23","MSG-01","MSG-05","MSG-06","MSG-07","MSG-08","MSG-09","MSG-10","MSG-11","MSG-12","MSG-16","MSG-17","DR-01","DR-03","DR-06","DCO-03","DCO-05","EML-07","EML-08","SOC-06","SOC-07","WEB-05","IMG-04","IMG-07","IMG-08","IMG-11","IMG-13","IMG-14","LP-05"}
for _r in RULES:
    _r["layer"] = "compliance" if (_r["section"] in ("LEG","ACC") or _r["id"] in COMPLIANCE_IDS) else "brand"

if __name__ == "__main__":
    from collections import Counter
    ids = [x["id"] for x in RULES]
    assert len(ids)==len(set(ids)), "duplicate ids"
    print(len(RULES), Counter(x["section"] for x in RULES))
    print("auto share", round(sum(x["check"]=="auto" for x in RULES)/len(RULES),2))
    print("severity", Counter(x["severity"] for x in RULES))
    print("provenance", Counter(x["provenance"] for x in RULES))
    print("layer", Counter(x["layer"] for x in RULES))
    json.dump({"brand":"pact","version":"0.1-public-build","built":"2026-11-22","rules":RULES}, open("/home/claude/pact/out/rules.json","w"), indent=1, ensure_ascii=False)
