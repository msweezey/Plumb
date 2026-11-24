"""Helpers shared by the brand content modules."""
import re, random

def fixtures_factory(order_prefix, ship_threshold, offer_id, tz, comments, cart_notes):
    def fx(rows, contacts, ph):
        R = random.Random(11)
        act = [r for r in rows if r["status"] == "active" and r["final_sale"] == "no"]
        fs = [r for r in rows if r["final_sale"] == "yes"]; disc = [r for r in rows if r["status"] == "discontinued"]
        cs = [c for c in contacts if c["unsubscribed"] == "no" and c["hard_bounce"] == "no" and c["persona_id"]]
        item = lambda r, q=1: dict(sku=r["sku"], name=r["name"], color=r["color"], qty=q, unit_price=r["price"], msrp=r["msrp"],
                                   msrp_comparison_allowed=r.get("_cmp", ""), final_sale=r["final_sale"], status=r["status"])
        carts = []
        picks = [[R.choice(act)], [R.choice(act), R.choice(act)], [R.choice(fs)] if fs else [R.choice(act)], [R.choice(disc)], [R.choice(act)]]
        for i, its in enumerate(picks):
            sub = round(sum(float(r["price"]) for r in its), 2)
            carts.append(dict(cart_id=f"CART-{i+1}", contact_id=cs[60+i*7]["contact_id"], abandoned_at=f"2026-11-{17+i}T19:4{i}:00",
                              items=[item(r) for r in its], subtotal=sub, free_shipping_gap=max(0, round(ship_threshold-sub, 2)),
                              eligible_offers=[offer_id], note=cart_notes[i]))
        o = [R.choice(act), R.choice(act)]
        sub = round(sum(float(r["price"]) for r in o), 2)
        order = dict(order_id=f"{order_prefix}-{R.randint(100000,999999)}", contact_id=cs[143]["contact_id"], placed_at="2026-11-21T10:12:00",
                     items=[item(r) for r in o], subtotal=sub, discount={"offer_id": offer_id}, shipping="Standard" + (", FREE" if sub >= ship_threshold else ""),
                     timezone=tz, cross_sell_pool=[item(r) for r in (fs[:1] + disc[:1] + act[5:8])],
                     note="Cross-sell traps: pool includes a final-sale and a discontinued SKU; recommend at most one active, in-stock item (EML-07).")
        return {"fixtures_e3_carts": carts, "fixtures_e6_order": order, "fixtures_s3_comments": comments}
    return fx

def first_sentence(t): return re.split(r"(?<=[.!?])\s", t.strip())[0]
