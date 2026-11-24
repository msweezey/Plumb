"""Run Pact's real copy through the rules. Brand-layer hits = rule is wrong about Pact (or Pact is inconsistent).
Compliance-layer hits = real risk in Pact's own copy (expected; that is what Plumb verifies)."""
import json, sys
from collections import Counter, defaultdict
sys.path.insert(0, "/home/claude/pact/build")
from checks import check, LAYER
C = json.load(open("/home/claude/pact/out/realcopy_corpus.json"))
report = {}
for split in ("T", "H"):
    rows = [c for c in C if c["split"] == split]
    brand, comp = defaultdict(list), defaultdict(list)
    clean_brand = 0
    for c in rows:
        hits = check(c["body"], c["channel"], c["headline"], c["cta"])
        b = [h for h in hits if LAYER.get(h[0]) == "brand"]
        if not b: clean_brand += 1
        for rid, ev in hits:
            (brand if LAYER.get(rid) == "brand" else comp)[rid].append(f'[{c["channel"]}] {(c["headline"]+" | "+c["body"])[:90]} :: {ev}')
    report[split] = dict(n=len(rows), brand_pass=clean_brand, brand_hits={k: v for k, v in brand.items()}, compliance_hits={k: v for k, v in comp.items()})
    print(f"\n=== {'TUNING' if split=='T' else 'HELD-OUT'} set: {len(rows)} real assets; brand-layer pass {clean_brand}/{len(rows)} ({clean_brand/len(rows):.0%})")
    for k, v in sorted(brand.items()):
        print(f"  BRAND {k} x{len(v)}"); [print("     ", x) for x in v[:4]]
    print("  compliance findings:", {k: len(v) for k, v in sorted(comp.items())})
json.dump(report, open("/home/claude/pact/out/fidelity_report.json", "w"), indent=1, ensure_ascii=False)
