import json, sys, os, importlib, shutil, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen_brand, runtests
from configs import BRANDS

SEC = [("BRD","1. Brand essence"),("VOI","2. Voice and tone"),("MSG","3. Messaging"),("LOG","4. Logo"),("COL","5. Color"),("TYP","6. Typography"),
       ("IMG","7. Imagery"),("LAY","8. Layout"),("ACC","9. Accessibility"),("LEG","10. Legal"),("EML","11. Email and SMS"),("SOC","12. Social"),
       ("DR","13. Direct response"),("BRA","14. Brand campaign"),("DCO","15. DCO and catalog ads"),("LP","16. Landing page"),("WEB","17. Website and product pages")]

def md_table(head, rows): return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|"*len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])

def build(b):
    res = gen_brand.run(b); C, cfg, rules, O = res["C"], res["cfg"], res["rules"], res["O"]; D = importlib.import_module(f"docs_{b}").D
    N = cfg["name"]; tok = json.load(open(f"{O}/brand_tokens.json"))
    fid = runtests.fidelity(b); M = runtests.discrimination()
    P = N + ("'" if N.endswith('s') else "'s"); W = lambda name, txt: open(f"{O}/{name}", "w").write(txt)
    # evidence + assumptions
    W("evidence_log.md", f"# {N} — evidence log (pulled 22 Nov 2026)\n\n" + "\n".join(f"{i} {t}" for i, t in D["evidence"]) + "\n")
    W("assumptions_method-a.md", f"# {N} — Method A: assumptions written before research, then tested\n\nAssumptions were written on 22 Nov 2026 before any {N} source was opened, with a confidence level (H/M/L). Each is scored against the evidence log.\n\n" + md_table(["#", "Assumption (conf.)", "Verdict", "Evidence"], D["scores"]) + "\n")
    # brief
    W("brief.md", f"# {N} — brand brief (brief.md)\n\nPublic build v0.3, 22 Nov 2026. Built from {P} public website, product feed, Meta ad library, Instagram and press (see evidence_log.md). Fields are marked observed, inferred or harness. Partner-supplied guidelines replace this build when available.\n\n" + md_table(["Field", "Content", "Basis"], D["brief"]) + f"\n\nQuadrant: {cfg['quadrant']}. Personas: shared (harness/shared/personas.md); primary {C['personas'][0]}, secondary {C['personas'][1]}.\n")
    # guidelines
    pal = "\n".join(f"| {v['hex']} | {k.replace('_',' ').title()} | {v['role']} | {v['used_for']} | {v['homepage_uses']} |" for k, v in tok["colors"].items())
    fonts = "\n".join(f"| {f['name']} | {f['type']} | {f['weights']} | {f['use']} | {f['source']} |" for f in tok["typography"]["families"])
    INTRO = {
     "BRD": "\n".join(f"- {x}" for x in D["methodB"]),
     "VOI": f"**Brand words:** {', '.join(cfg['vocab'])}.\n\n**Off-voice words:** {', '.join(cfg['banned_voice'])}.\n\n**Compliance banned list:** {', '.join(cfg['banned_compliance'])}.",
     "COL": "Colors are referenced by hex only, pulled from the live homepage.\n\n| Hex | Name | Role | Used for | Homepage uses |\n|---|---|---|---|---|\n" + pal + "\n\n**Approved text pairings:** " + "; ".join(tok["approved_text_pairings"][:12]) + ".\n\n**Large text only:** " + ("; ".join(tok["large_text_only"][:8]) or "none") + ".",
     "TYP": "| Family | Type | Weights | Use | Source |\n|---|---|---|---|---|\n" + fonts,
     "LEG": f"Compliance rules are stricter than {P} own copy and win over brand rules (precedence). Address used: '{C['address']}' (confirm). Shipping: {C['ship_text']}.",
    }
    lines = [f"# {N} — brand guidelines (guidelines.md)", "",
     f"Public build v0.3, 22 Nov 2026, built the same way as Pact (assumptions first, then evidence, then rules calibrated against {P} real copy; see test_report_fidelity.md). **Brand** rules describe how {N} actually writes and are tuned to pass its real copy; **compliance** rules are stricter than the brand's own copy and win on conflict.", "",
     f"Rules: {len(rules)} ({sum(r['layer']=='brand' for r in rules)} brand, {sum(r['layer']=='compliance' for r in rules)} compliance). Checked automatically: {sum(r['check']=='auto' for r in rules)} ({round(100*sum(r['check']=='auto' for r in rules)/len(rules))}%).", ""]
    for code, title in SEC:
        lines += [f"## {title} ({code})", "", INTRO.get(code, ""), ""]
        for r in [r for r in rules if r["section"] == code]:
            lines.append(f"- **{r['id']}** {r['rule']} _[{r['layer']} layer, {r['type']}, {r['severity']}, {r['check']}, {r.get('provenance','observed')}]_")
        lines.append("")
    W("guidelines.md", "\n".join(lines))
    rub = [f"# {N} — rubric (rubric.md)", "", "Same scoring as every Plumb harness: (1) gate — any critical miss fails; (2) adherence 0–100, major weighted 3, minor 1; (3) craft 1–4 by AI judge against the anchors below and the golden examples; (4) human review on a 10% sample and every critical flag.", "", "## Craft criteria (AI judge, 1–4)", "", "| Rule | Criterion | 1 looks like | 4 looks like |", "|---|---|---|---|"]
    rub += [f"| {r['id']} | {r['rule']} | {r['anchors']['1']} | {r['anchors']['4']} |" for r in rules if r["check"] == "AI judge" and r.get("anchors")]
    rub += ["", "## Gate rules (critical)", ""] + [f"- {r['id']} — {r['rule']}" for r in rules if r["severity"] == "critical"]
    W("rubric.md", "\n".join(rub))
    # claims, copy bank
    W("library_claims.md", f"# {N} — approved claims (library/claims.md)\n\nUse these claims only, worded as shown. Check catalog fields before using a product-level claim.\n\n" + md_table(["ID", "Claim (approved wording)", "Scope / condition", "Substantiation", "Status"], D["claims"]) + "\n")
    cb = [f"# {N} — copy bank (library/copy-bank.md)", "", "Observed lines come from the brand's own public material; harness lines are written in the brand voice. DEPRECATED lines are decoys.", "", "## Boilerplate", f"**Short:** {D['boiler_short']}", "", f"**Long:** {D['boiler_long']}", "", "## Tagline"] + [f"- {t}" for t in D["tagline"]]
    n = 0
    for sec, items in D["copy"].items():
        cb += ["", f"## {sec}"] + [f"{i+1}. {x}" for i, x in enumerate(items)]; n += len(items)
    W("library_copy-bank.md", "\n".join(cb) + f"\n\n_{n} lines plus boilerplate._\n")
    # goldens
    gl = [f"# {N} — golden examples, wave 1 (history/)", "", "Two on-brand examples per wave 1 task (P1, E1, A1). Each passes every automatic rule (validated by checks.py); the AI judge uses them as 4-anchors.", ""]
    for task, title in (("P1", "P1 — product descriptions"), ("E1", f"E1 — promo email ({D['e1_campaign']})"), ("A1", "A1 — paid search ads")):
        gl += [f"## {title}", ""]
        for g in [g for g in C["goldens"] if g["task"] == task]:
            gl += [f"### {g['id']} · {g['title']}"] + ([f"Trap covered: {g['trap']}"] if g.get("trap") else []) + ["```json", json.dumps(g["out"], indent=1, ensure_ascii=False), "```", ""]
    W("history_golden_wave1.md", "\n".join(gl))
    nv = sum(len(d["expected_violations"]) for d in C["drafts"])
    W("traps.md", f"# {N} — conflicts, gaps, decoys and memory traps (traps/)\n\nAgents never see this file except in review tasks. Off-brand drafts are in traps_offbrand_drafts.json (10 drafts, {nv} seeded violations).\n\n## Conflicts (3)\n\n" + md_table(["ID", "Clash", "Triggered in", "Winning rule", "Correct behavior"], D["conflicts"]) +
      "\n\n## Gaps (3)\n\n" + md_table(["ID", "Situation", "What a brand lead would sign off"], D["gaps"]) + "\n\n## Decoys (2)\n\n" + md_table(["ID", "Decoy", "Where it sits", "Check"], D["decoys"]) +
      "\n\n## Memory traps (from the Method A test)\n\nStale beliefs a model may hold from training data; the files contradict each one.\n\n" + md_table(["ID", "Stale belief", "What the files say", "Caught by"], D["memory"]) + "\n")
    W("tasks_wave1.md", f"""# {N} — task briefs (tasks/)

Same task set as every retail harness. Output schemas match Pact so results compare across brands.

## P1 — Product descriptions
Write product copy for all 200 SKUs in catalog_products.csv. Return one JSON object per SKU with: sku, title, description ({cfg['pdp_words'][0]}–{cfg['pdp_words'][1]} words), fiber_content, care, fit, sizes, origin (plus brand fields shown in history P1-G1/G2). Use catalog fields only; leave a field empty when the catalog is empty. Skip status = discontinued; tease status = coming_soon.

## E1 — Promo email
Campaign: {D['e1_campaign']}. Write one email for segment **active** (persona {C['personas'][0]}) and one for **lapsed** (persona {C['personas'][1]}). Return subject, preheader, body, cta, terms, footer. {D['tasks_extra']}

## A1 — Paid search ads
15 headlines (max 30 characters) and 4 descriptions (max 90) for each of 5 ad groups: {D['a1_groups']}.

## Fixtures for waves 2 and 3
| Task | Fixture |
|---|---|
| E3 abandoned cart | fixtures_e3_carts.json (5 carts with notes) |
| E6 order confirmation | fixtures_e6_order.json (cross-sell pool with traps) |
| S3 comment replies | fixtures_s3_comments.json (10 comments) |
| M1 SMS | audience_contacts.csv (consent and under-18 edge cases) |
| B1 brand edit | traps_offbrand_drafts.json |
""")
    yaml = f"""# {N} harness manifest (harness.yaml)
id: retail-{b}
version: 0.3-public-build
built: 2026-11-22
segment: retail
quadrant: {cfg['quadrant'].replace('×','x')}
source: public material (see evidence_log.md); partner swap pending
rule_count: {len(rules)}
auto_share: {round(sum(r['check']=='auto' for r in rules)/len(rules),2)}
personas: shared (primary {C['personas'][0]}, secondary {C['personas'][1]})
files:
  brief: brief.md
  guidelines: guidelines.md
  rules: rules.json
  rubric: rubric.md
  checks: checks.py
  brand: [brand_tokens.json, logo files (to supply)]
  catalog: [catalog_products.csv (200), catalog_offers.csv (10), catalog_price_history.csv (200 x 12), catalog_reviews.csv (300)]
  audience: [audience_segments.json, audience_contacts.csv (250, retail-spine-v2 + {N} columns)]
  shared: [harness/shared/personas.md, harness/shared/contacts_spine_v2.csv]
  library: [library_copy-bank.md, library_claims.md (25)]
  history: [history_golden_wave1.md (6)]
  traps: [traps.md, traps_offbrand_drafts.json (10 drafts, {nv} violations)]
  tasks: [tasks_wave1.md]
  fixtures: [fixtures_e3_carts.json, fixtures_e6_order.json, fixtures_s3_comments.json]
  tests: [realcopy_corpus.json, test_report_fidelity.md]
  method: [evidence_log.md, assumptions_method-a.md]
deprecated: {json.dumps([d[1] for d in D['decoys']])}
not_yet_built: [logo files, image library, golden examples for waves 2-3, AI judge calibration]
"""
    W("harness.yaml", yaml)
    # realcopy_corpus.json is written by corpus_build.py straight into the harness folder
    # checks.py bundle
    kit = open(f"{HERE}/brandkit.py").read()
    W("checks.py", kit + f"\n\n# ---- {N} config (from configs.py) ----\nimport json as _j\nCFG = {repr(cfg)}\n\nif __name__ == '__main__':\n    import sys\n    print(check(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'ad', CFG))\n")
    # test report
    val = res["val"]; det = sum(len(e) - len(m) for _, e, m, _ in val["drafts"])
    others = [k for k in BRANDS if k != b]
    rej_by_me = {s: M[f"{s}->{b}"] for s in others}
    rep = [f"# {N} — fidelity and discrimination tests (test_report_fidelity.md)", "",
      f"Run 22 Nov 2026 with checks.py (shared Plumb engine + {N} config). Real copy was split before tuning: **T** (tuning) and **H** (held out). Rules were tuned on T only.", "",
      "## Results", "", "| Test | Result | Pact target |", "|---|---|---|",
      f"| Fidelity, tuning (brand layer) | {fid['T']['passed']}/{fid['T']['n']} = {fid['T']['rate']:.0%} | ~90% |",
      f"| Fidelity, held-out (brand layer) | {fid['H']['passed']}/{fid['H']['n']} = {fid['H']['rate']:.0%} | ~90% |"] + \
      [f"| Discrimination: {BRANDS[s]['name']} ads + posts rejected by {N} rules | {r}/{t} = {r/t:.0%} | ≥85% |" for s, (r, t) in rej_by_me.items()] + \
      [f"| Goldens pass all automatic rules | {sum(1 for _, v in val['golden'] if not v)}/{len(val['golden'])} | 6/6 |",
       f"| Seeded trap violations detected | {det}/{nv} | all |", "",
       "## Brand-layer misses on the brand's own copy", "", "These are the brand's own inconsistencies (kept as findings, not tuned away):", ""] + \
      [f"- {sp} · {ch}: {', '.join(r for r, _ in f)} — “{txt[:80]}”" for sp in "TH" for ch, txt, f in fid[sp]["fails"]] + \
      ["", "## Compliance findings on real copy", "", f"Compliance rules flagged {fid['T']['compliance_flagged']} tuning and {fid['H']['compliance_flagged']} held-out assets. This is expected: compliance is stricter than the brand's own practice.", "",
       "## Calibration notes", "", "- One engine (checks.py) for all four brands; brand differences live in config only (emoji and caps ranges, vocabulary, off-voice words, category boundaries, reading level, thresholds).",
       "- Held-out results were inspected after the first tuning round. Any later change was justified by a tuning-split asset, and is noted in the cross-brand summary.", ""]
    W("test_report_fidelity.md", "\n".join(rep))
    # comparison doc
    comp = [f"# {N} — harness build and method comparison", "", f"Built 22 Nov 2026 on the Pact path: Method A (assumptions written first, then tested) and Method B (brand book reverse-engineered from evidence), then a full dataset and the four tests. Harness files: harness/retail-{b}/.", "",
      "## Headline findings", ""] + [f"- {h}" for h in D["headline"]] + ["", "## Method A: assumptions tested", "", md_table(["#", "Assumption (conf.)", "Verdict", "Evidence"], D["scores"]), "",
      "## Method B: the reverse-engineered brand book (summary)", ""] + [f"- {x}" for x in D["methodB"]] + ["",
      "## Where the methods differ", "", f"Method A scored: {sum(1 for s in D['scores'] if s[2].startswith('Confirmed'))} confirmed, {sum(1 for s in D['scores'] if s[2].startswith('Partly'))} partly, {sum(1 for s in D['scores'] if '**' in s[2])} wrong or outdated, {sum(1 for s in D['scores'] if s[2].startswith('Unverified'))} unverified, out of {len(D['scores'])}. Method B supplied every number the rules need (emoji and caps ranges, reading level, hex values, fonts, thresholds); Method A supplied none of them reliably. The wrong or outdated assumptions became memory traps in traps.md.", "",
      "## Tests", ""] + rep[4:4+6+len(others)]
    NOTE = {"mml": "10", "edikted": "11", "topo": "12"}[b]
    open(f"{gen_brand.ROOT}/docs/notes/{NOTE}-{b}-build-and-comparison.md", "w").write("\n".join(comp) + "\n")
    return dict(fid=fid, M=M, det=det, nv=nv, goldens=val["golden"], rules=rules, res=res)

if __name__ == "__main__":
    for b in sys.argv[1:]:
        r = build(b)
        print(b, "T", r["fid"]["T"]["rate"], "H", r["fid"]["H"]["rate"], "drafts", r["det"], "/", r["nv"], "goldens", sum(1 for _, v in r["goldens"] if not v), "files", len(os.listdir(f"{gen_brand.ROOT}/harness/retail-{b}")))
