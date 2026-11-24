import json, sys
sys.path.insert(0, "/home/claude/pact/build")
from rules import RULES, BANNED, USE
O = "/home/claude/pact/out"
tok = json.load(open(f"{O}/brand_tokens.json"))

SEC = [("BRD","1. Brand essence"),("VOI","2. Voice and tone"),("MSG","3. Messaging"),("LOG","4. Logo"),("COL","5. Color"),("TYP","6. Typography"),
       ("IMG","7. Imagery"),("LAY","8. Layout"),("ACC","9. Accessibility"),("LEG","10. Legal"),("EML","11. Email and SMS"),("SOC","12. Social"),
       ("DR","13. Direct response"),("BRA","14. Brand campaign"),("DCO","15. DCO and catalog ads"),("LP","16. Landing page"),("WEB","17. Website and product pages")]
INTRO = {
"BRD": "**Purpose:** make getting dressed an act of self-care, with clothes made to clear, certified standards.\n\n**Positioning:** certified organic essentials, gentle on skin, priced for everyday life.\n\n| Trait | Is | Is not |\n|---|---|---|\n| Caring | Warm, reassuring | Preachy, guilt-driven |\n| Clear | Plain about what's in the clothes | Jargon, acronym stacks |\n| Grounded | Honest about limits, specific | Absolute, perfectionist |\n| Easygoing | Relaxed, a little playful | Slangy outside social, try-hard |",
"VOI": "**Words to use (20):** " + ", ".join(USE) + ".\n\n**Words never to use (30):** " + ", ".join(BANNED) + ". (Catalog product names are exempt, e.g. 'Perfect Rib'.)\n\n| Context | We say | We never say |\n|---|---|---|\n| Promo | Everything is up to 40% off through Sunday. / Restock what you wear most. | HURRY!!! Prices this low won't last!!! / Don't miss out! |\n| Service | Your order shipped today. Track it here. / We'll reply by email within one business day. | We are experiencing delays beyond our control. / Per our policy... |\n| Apology | We got this wrong. A replacement is on its way. / Thanks for telling us. Here's the fix. | Due to unprecedented demand, mistakes happen. / Sorry for any inconvenience. |\n| Onboarding | Welcome. Here's what certified organic means for what you wear. / Start with the basics you wear most. | Welcome! Here are 12 things about us... / You need to switch everything today. |\n| Sensitive news | We've paused sales of one style while we check a fabric issue. / Here's what this means for your order. | Oops! While we sort this out, shop new arrivals! / Nothing to worry about! |\n\n**Mechanics:** 'Pact' in running copy; serial comma optional but consistent within an asset; $10 not $10.00; 40% not 40 percent; spaced em dash for asides; grade 10 reading level or below for longer copy.",
"MSG": "| Value prop | Proof points |\n|---|---|\n| Gentle on skin | GOTS-certified organic cotton; made without harsh chemicals, toxic dyes and PFAS |\n| Verified standards | GOTS (Control Union) certification; Fair Trade Certified™ factories |\n| Organic for everyday life | Underwear from $10; leggings from $20 during OF-03; free shipping at $99+ |\n\n**Taglines:** current 'Dress Yourself Well'; retired 'Earth's Favorite™ Clothing' (decoy). **Boilerplate** and **approved claims:** library/copy-bank.md and library/claims.md.",
"LOG": "Versions: full (black wordmark, 2.63:1), mono (white), icon (square). Files in brand/; the legacy caps file in brand/deprecated/ is a decoy. Minimum size 64 px digital, 18 mm print.",
"COL": "Colors are referenced by hex only. All values come from wearpact.com's CSS (22 Nov 2026) except the logo black.\n\n| Name | Hex | Role | Used on the site for | Share |\n|---|---|---|---|---|\n" + "\n".join(f"| {k.replace('_',' ').title()} | {v['hex']} | {v['role']} | {v['used_for']} | {v['usage_share']} |" for k,v in tok["colors"].items()) +
       "\n\n**Approved text pairings:** " + "; ".join(tok["approved_text_pairings"]) + ".\n\n**Large text only:** " + "; ".join(tok["large_text_only"]) + ".\n\n**Banned text pairings:** " + "; ".join(tok["banned_text_pairings"]) + ".",
"TYP": "| Family | Type | Weights | Used on the site for |\n|---|---|---|---|\n| Juana | Serif | 300, 400, 600 + italics | Banners, collection and marketing headings, page titles |\n| Averta | Sans | 300, 400, 700, 900 | Body, navigation, buttons, forms |\n| GT Eesti | Sans | 300, 400 | Product titles, price block, loyalty headings |\n\nAll three are commercial fonts self-hosted by Pact. Test renders use the site's own fallback stacks unless licenses are in place. Third-party widget fonts on the site (Klaviyo pop-up, Global-e checkout, Algolia search) are not brand fonts.",
"IMG": "Image types for retail per the frameworks doc: product on figure, flat lay, home and bed scenes, texture close-ups, lifestyle in daily routines. Observed backdrop tones are warm neutrals (soil, slate, beige).",
"LAY": "Grids: 12-column web, single-column 600 px email. Spacing scale 4–64 px (tokens.json).",
"ACC": "Standard WCAG 2.2 AA. Body contrast 4.5:1; large text 3:1.",
"LEG": "Core legal rules (LEG-01 to LEG-09) apply to every brand; LEG-10 to LEG-20 are the retail and Pact overlay. Critical legal rules win over any other rule (precedence). Locked text: address '4725 Walnut St, Boulder, CO 80301'; SMS 'Reply STOP to opt out'; final sale 'Final sale, not eligible for return or exchange'.",
"EML": "Purpose and KPI: promo and lifecycle email drive repeat purchase (KPI: revenue per send, repeat rate). Specs: 600 px, subject 25–50, preheader 40–90, sender 'Pact'. Required: logo header, one primary CTA, terms line, full footer.",
"SOC": "Platforms: Instagram (primary), TikTok, Facebook, Threads, Pinterest; LinkedIn for corporate posts. Observed mechanics: comment-to-get-link, creator collaborations, giveaways.",
"DR": "Search and paid social. Observed paid social: Title Case headlines, price-led, CTA 'Shop now'.",
"BRA": "Brand video is light in Pact's current mix (inferred). Lengths :06, :15, :30; end card with logo and tagline.",
"DCO": "Pact runs Meta catalog ads (observed DPA template with a live price slot). Slots and fallbacks below.",
"LP": "Landing pages match the ad's promise and offer; one goal.",
"WEB": "Observed PDP pattern: name, price, colorways, sizes, short description (hook, what, fit, wear), then a 'Wellness ingredients' module (MADE WITH / MADE WITHOUT / CERTIFIED) and a blend footnote.",
}

lines = ["# Pact — brand guidelines (guidelines.md)", "",
 "Public build v0.3, 22 Nov 2026 (calibrated against Pact's real copy; see test_report_fidelity.md). Rules come in two layers: **brand** rules describe how Pact actually writes and are tuned to pass its real copy; **compliance** rules are stricter than Pact's own copy on purpose, because catching legal and claims risk is what Plumb verifies. The build was reverse-engineered from Pact's public website, Meta ads, Instagram, Google Shopping listings and press, then completed by Plumb where the public record is silent. Each rule is tagged by provenance: **observed** (seen in Pact's own material), **inferred** (a pattern across sources) or **harness** (set by Plumb). Partner-supplied guidelines replace this build; rule IDs stay the same.", "",
 f"Rules: {len(RULES)}. Checked automatically: {sum(r['check']=='auto' for r in RULES)} ({round(100*sum(r['check']=='auto' for r in RULES)/len(RULES))}%). Severity: {sum(r['severity']=='critical' for r in RULES)} critical, {sum(r['severity']=='major' for r in RULES)} major, {sum(r['severity']=='minor' for r in RULES)} minor.", ""]
for code, title in SEC:
    rs = [r for r in RULES if r["section"]==code]
    lines += [f"## {title} ({code})", "", INTRO.get(code,""), ""]
    for r in rs:
        extra = ""
        if r.get("pass"): extra += f" Pass: \"{r['pass']}\"."
        if r.get("fail"): extra += f" Fail: \"{r['fail']}\"."
        lines.append(f"- **{r['id']}** {r['rule']} _[{r['layer']} layer, {r['type']}, {r['severity']}, {r['check']}, {r['provenance']}]_{extra}")
    lines.append("")
open(f"{O}/guidelines.md","w").write("\n".join(lines))

# rubric
rub = ["# Pact — rubric (rubric.md)", "",
 "Generated from rules.json plus the universal criteria in the Eval & Rubric Spec. Scoring runs in four steps: (1) gate — any critical miss fails the asset; (2) adherence 0–100 — share of applicable rules met, major weighted 3 and minor 1; (3) craft 0–100 — AI-judged 1–4 criteria rescaled; (4) quality gate — no critical miss, adherence 90+, craft 3.0+.", "",
 "AI judge: fixed model, rubric anchors plus golden examples (history_golden_wave1.md), 3 runs, median. Human review: calibration each cycle, 10% sample, every critical flag, and any asset where judge runs differ by more than 1 point.", "",
 "## Craft criteria (AI judge, 1–4)", "", "| Rule | Criterion | 1 looks like | 4 looks like |", "|---|---|---|---|"]
for r in RULES:
    if r["check"]=="AI judge" and r.get("anchors"):
        rub.append(f"| {r['id']} | {r['rule']} | {r['anchors']['1']} | {r['anchors']['4']} |")
rub += ["", "## Gate rules (critical; any miss fails the asset)", ""]
rub += [f"- {r['id']} — {r['rule']}" for r in RULES if r["severity"]=="critical"]
rub += ["", "## Wave 1 task mapping", "", "| Task | Rules in scope (applies_to) |", "|---|---|"]
for t, ap in (("P1 product descriptions","pdp"),("E1 promo email","email"),("A1 paid search","dr")):
    ids = [r["id"] for r in RULES if ap in r["applies_to"]]
    rub.append(f"| {t} | {len(ids)} rules: {', '.join(ids)} |")
open(f"{O}/rubric.md","w").write("\n".join(rub))

# manifest
yaml = f"""# Pact harness manifest (harness.yaml)
id: retail-pact
version: 0.3-public-build
built: 2026-11-22
segment: retail
quadrant: restrained x value
source: public material (see evidence log); partner swap pending
rule_count: {len(RULES)}
auto_share: {round(sum(r['check']=='auto' for r in RULES)/len(RULES),2)}
files:
  brief: brief.md
  guidelines: guidelines.md
  rules: rules.json
  rubric: rubric.md
  brand: [brand_tokens.json, logo-full.svg (to supply), logo-mono.svg (to supply), logo-icon.svg (to supply)]
  catalog: [catalog_products.csv (200), catalog_offers.csv (10), catalog_price_history.csv (200 x 12), catalog_reviews.csv (300)]
  audience: [audience_segments.json, audience_contacts.csv (250, retail-spine-v2 + Pact columns)]
  shared: [harness/shared/personas.md (GZ, MIL, GX, BB), harness/shared/contacts_spine_v2.csv]
  library: [library_copy-bank.md (50 lines + boilerplate), library_claims.md (25)]
  history: [history_golden_wave1.md (6)]
  traps: [traps.md, traps_offbrand_drafts.json (10 drafts, 36 violations)]
  tasks: [tasks_wave1.md]
  fixtures: [fixtures_e3_carts.json, fixtures_e6_order.json, fixtures_s3_comments.json]
deprecated:
  - "tagline: Earth's Favorite™ Clothing"
  - brand/deprecated/logo-legacy.svg
not_yet_built: [logo files, library/images (60), golden examples for waves 2-3]
"""
open(f"{O}/harness.yaml","w").write(yaml)
print("ok")
