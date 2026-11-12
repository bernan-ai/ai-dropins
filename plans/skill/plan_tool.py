#!/usr/bin/env python3
"""Check a plan takeoff's math, draw the marked-up plan, and price it from your own rate sheet.

Usage:
  python3 plan_tool.py check                                   # offline self-test, needs nothing
  python3 plan_tool.py totals --takeoff takeoff.json           # re-adds every column, flags any slip
  python3 plan_tool.py markup --takeoff takeoff.json --plan sheet-A-101.png
  python3 plan_tool.py price  --takeoff takeoff.json --rates rates.csv

The takeoff is the JSON block your AI writes from the plans.md prompt.
Nothing here goes online. It reads your files and writes new files beside them. It never changes your plan.
"""
import argparse, csv, json, os, sys, tempfile

TOTAL_KEYS = ["floor_sf", "wall_sf", "ceiling_sf", "base_lf", "doors"]
COLORS = [(240, 108, 28), (52, 120, 200), (40, 160, 110), (170, 80, 190), (210, 170, 30), (200, 60, 80)]


def load_takeoff(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # Accept the whole chat answer: take the last ```json block if there is one.
    if "```json" in text:
        text = text.rsplit("```json", 1)[1].split("```", 1)[0]
    data = json.loads(text)
    if not isinstance(data.get("rooms"), list) or not data["rooms"]:
        raise SystemExit("the takeoff has no rooms list")
    return data


def num(v):
    return float(v) if isinstance(v, (int, float)) else 0.0


def recount(t):
    """Totals added up again from the rooms and doors, never copied from the AI's own totals line."""
    rooms = t["rooms"]
    sums = {k: round(sum(num(r.get(k)) for r in rooms), 1) for k in TOTAL_KEYS if k != "doors"}
    sums["doors"] = int(sum(num(d.get("leaves", 1)) for d in t.get("doors", [])))
    return sums


def totals_report(t):
    """Lines that name every slip between the AI's totals and the re-added rooms."""
    got, said, out = recount(t), t.get("totals", {}), []
    for k in TOTAL_KEYS:
        if k not in said:
            out.append(f"{k}: no total given; re-added {got[k]:,}")
        elif abs(num(said[k]) - got[k]) > max(1.0, 0.005 * got[k]):
            out.append(f"{k}: the AI said {num(said[k]):,} but the rooms add to {got[k]:,}")
    for r in t["rooms"]:
        h, p, w = num(r.get("ceiling_height_ft")), num(r.get("perimeter_lf")), num(r.get("wall_sf"))
        if h and p and w and abs(h * p - w) > max(1.0, 0.01 * w):
            out.append(f"room {r.get('number')}: wall_sf {w:,} is not perimeter {p} x height {h} = {p * h:,}")
    return got, out


def read_rates(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("item") or "").strip() and not r["item"].startswith("#")]
    for r in rows:
        try:
            r["rate"] = float(str(r["rate"]).replace("$", "").replace(",", ""))
        except ValueError:
            raise SystemExit(f"rate sheet: '{r['item']}' has no number in the rate column")
    return rows


def price(t, rates):
    """One line per rate row: quantity from the re-added totals or a fixture count, times your rate."""
    q = recount(t)
    fixtures = {}
    for fx in t.get("fixtures", []):
        name = str(fx.get("item", "")).strip().lower()
        fixtures[name] = fixtures.get(name, 0) + num(fx.get("count"))
    lines, missing, markup = [], [], 0.0
    for r in rates:
        key = r["quantity"].strip()
        if key == "markup_pct":
            markup += r["rate"]
            continue
        if key.startswith("fixture:"):
            qty = fixtures.get(key.split(":", 1)[1].strip().lower())
        else:
            qty = q.get(key)
        if not qty:
            missing.append(f"{r['item']}: no quantity for '{key}' in this takeoff")
            continue
        lines.append((r["item"], qty, r.get("unit", ""), r["rate"], round(qty * r["rate"], 2)))
    sub = round(sum(l[4] for l in lines), 2)
    return lines, sub, round(sub * markup / 100, 2), markup, missing


def price_text(t, rates, rates_name):
    lines, sub, add, pct, missing = price(t, rates)
    out = [f"# First-pass price: {t.get('job', 'this job')}", "",
           f"Rates from {rates_name}. FIRST PASS, NOT A PRICE TO SEND. A person checks every line first.", "",
           "| Item | Quantity | Unit | Rate | Amount |", "|---|---|---|---|---|"]
    out += [f"| {i} | {q:,.{0 if q == int(q) else 1}f} | {u} | {r:,.2f} | {a:,.2f} |" for i, q, u, r, a in lines]
    out += ["", f"Subtotal: {sub:,.2f}"]
    if pct:
        out.append(f"Markup at {pct:g} percent: {add:,.2f}")
    out.append(f"First-pass total: {sub + add:,.2f}")
    if missing:
        out += ["", "Not priced:"] + [f"- {m}" for m in missing]
    flags = t.get("flags", [])
    if flags:
        out += ["", f"Open flags from the takeoff ({len(flags)}), settle these before trusting the total:"]
        out += [f"- {f.get('where', '')}: {f.get('reason', '')}" for f in flags]
    return "\n".join(out) + "\n"


def markup(t, plan, out):
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        raise SystemExit("markup needs Pillow: python3 -m pip install --user pillow")

    def font(px):
        try:
            return ImageFont.load_default(size=px)
        except TypeError:
            raise SystemExit("markup needs Pillow 10.1 or later: python3 -m pip install --user --upgrade pillow")
    base = Image.open(plan).convert("RGBA")
    W, H = base.size
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    s = max(1, W // 1200)

    def tag(x, y, text, px, anchor="la"):
        """Text on a white card sized to the text itself."""
        f = font(px * s)
        bx = d.textbbox((x, y), text, font=f, anchor=anchor)
        d.rectangle([bx[0] - 3 * s, bx[1] - 3 * s, bx[2] + 3 * s, bx[3] + 3 * s], fill=(255, 255, 255, 235))
        d.text((x, y), text, fill=(20, 25, 35, 255), font=f, anchor=anchor)

    drawn = 0
    for i, r in enumerate(t["rooms"]):
        box = r.get("box")
        if not (isinstance(box, list) and len(box) == 4 and all(0 <= num(v) <= 1 for v in box)):
            print(f"room {r.get('number')}: no box on the plan, listed but not shaded")
            continue
        x0, y0, x1, y1 = box[0] * W, box[1] * H, box[2] * W, box[3] * H
        c = COLORS[i % len(COLORS)]
        d.rectangle([x0, y0, x1, y1], fill=c + (70,), outline=c + (255,), width=3 * s)
        tag(x0 + 8 * s, y1 - 22 * s, f"{r.get('number', '')} {r.get('name', '')}", 8, "ld")
        tag(x0 + 8 * s, y1 - 8 * s, f"{num(r.get('floor_sf')):,.0f} SF", 8, "ld")
        drawn += 1
    for dr in t.get("doors", []):
        at = dr.get("at")
        if not (isinstance(at, list) and len(at) == 2):
            continue
        cx, cy, rad = at[0] * W, at[1] * H, 10 * s
        d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=(220, 30, 40, 235))
        d.text((cx, cy), str(dr.get("mark", "?")), fill=(255, 255, 255, 255), font=font(9 * s), anchor="mm")
    tag(18 * s, 16 * s, f"{drawn} rooms shaded, {recount(t)['doors']} doors marked. FIRST PASS, CHECK IT.", 12)
    Image.alpha_composite(base, layer).convert("RGB").save(out)   # plain PNG, no text chunks
    return drawn


SAMPLE = {
    "job": "sample box",
    "rooms": [
        {"number": "1", "name": "ROOM A", "floor_sf": 100, "perimeter_lf": 40, "ceiling_height_ft": 10,
         "wall_sf": 400, "ceiling_sf": 100, "base_lf": 37, "box": [0.1, 0.1, 0.5, 0.5]},
        {"number": "2", "name": "ROOM B", "floor_sf": 50, "perimeter_lf": 30, "ceiling_height_ft": 9,
         "wall_sf": 270, "ceiling_sf": 50, "base_lf": 27, "box": [0.5, 0.1, 0.9, 0.5]},
    ],
    "doors": [{"mark": "D1", "room": "1", "leaves": 2, "at": [0.3, 0.5]}, {"mark": "D2", "room": "2", "at": [0.7, 0.5]}],
    "fixtures": [{"item": "sink", "room": "2", "count": 2}],
    "flags": [{"where": "ROOM B", "reason": "ceiling height not on the sheet"}],
    "totals": {"floor_sf": 150, "wall_sf": 670, "ceiling_sf": 150, "base_lf": 64, "doors": 3},
}
SAMPLE_RATES = "item,quantity,unit,rate,note\nFloor,floor_sf,SF,2,x\nWalls,wall_sf,SF,1,x\nSink,fixture:sink,EA,10,x\nGlass,glass_sf,SF,9,x\nMarkup,markup_pct,%,10,x\n"


def selftest():
    """Offline: re-adds known numbers, catches a planted slip, prices by hand-worked math, draws a markup."""
    got, slips = totals_report(SAMPLE)
    assert got == {"floor_sf": 150, "wall_sf": 670, "ceiling_sf": 150, "base_lf": 64, "doors": 3}, got
    assert slips == [], slips
    bad = json.loads(json.dumps(SAMPLE))
    bad["totals"]["floor_sf"] = 160
    bad["rooms"][1]["wall_sf"] = 300
    _, slips = totals_report(bad)
    assert any("floor_sf" in s for s in slips) and any("room 2" in s for s in slips), slips
    with tempfile.TemporaryDirectory() as tmp:
        rp = os.path.join(tmp, "rates.csv")
        open(rp, "w").write(SAMPLE_RATES)
        lines, sub, add, pct, missing = price(SAMPLE, read_rates(rp))
        # by hand: 150 x 2 = 300, 670 x 1 = 670, 2 sinks x 10 = 20; subtotal 990; markup 10 percent = 99
        assert [l[4] for l in lines] == [300, 670, 20] and sub == 990 and add == 99 and pct == 10, (lines, sub, add)
        assert len(missing) == 1 and "glass_sf" in missing[0], missing
        assert "First-pass total: 1,089.00" in price_text(SAMPLE, read_rates(rp), "rates.csv")
        try:
            from PIL import Image
        except ImportError:
            print("check: math passed; markup skipped, Pillow is not installed")
            return 0
        plan, out = os.path.join(tmp, "plan.png"), os.path.join(tmp, "marked.png")
        Image.new("RGB", (600, 400), "white").save(plan)
        assert markup(SAMPLE, plan, out) == 2
        px = Image.open(out).getpixel((120, 100))
        assert px != (255, 255, 255), "room A was not shaded"
    print("check: passed (totals, slip catch, price math, markup)")
    return 0


def main():
    ap = argparse.ArgumentParser(description="takeoff math, marked-up plan and first-pass price")
    ap.add_argument("command", choices=["check", "totals", "markup", "price"])
    ap.add_argument("--takeoff")
    ap.add_argument("--plan")
    ap.add_argument("--rates")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.command == "check":
        return selftest()
    if not a.takeoff or not os.path.isfile(a.takeoff):
        raise SystemExit("give --takeoff, the JSON file your AI wrote")
    t = load_takeoff(a.takeoff)
    here = os.path.dirname(os.path.abspath(a.takeoff))
    if a.command == "totals":
        got, slips = totals_report(t)
        print("re-added: " + ", ".join(f"{k} {v:,}" for k, v in got.items()))
        print("\n".join(slips) if slips else "every total matches its rooms")
        return 1 if slips else 0
    if a.command == "markup":
        if not a.plan or not os.path.isfile(a.plan):
            raise SystemExit("give --plan, the plan image the room boxes were read from")
        out = a.out or os.path.join(here, "marked-up-plan.png")
        if os.path.exists(out):
            raise SystemExit(f"{out} already exists; pass --out with a new name")
        markup(t, a.plan, out)
        print(f"saved {out}")
        return 0
    if not a.rates or not os.path.isfile(a.rates):
        raise SystemExit("give --rates, your rate sheet CSV (start from example-rates.csv)")
    text = price_text(t, read_rates(a.rates), os.path.basename(a.rates))
    out = a.out or os.path.join(here, "first-pass-price.md")
    if os.path.exists(out):
        raise SystemExit(f"{out} already exists; pass --out with a new name")
    open(out, "w", encoding="utf-8").write(text)
    print(text + f"\nsaved {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
