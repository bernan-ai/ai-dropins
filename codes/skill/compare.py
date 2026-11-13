#!/usr/bin/env python3
"""Add up rental car and hotel quotes and print one table, cheapest first.

Usage:
  python3 compare.py check                  # offline self-test, needs nothing
  python3 compare.py table --quotes q.csv   # prints the table

q.csv has one row per price you read off a booking page:
  kind,company,offer,code,pay,site_total,extra_per_day,extra_cap,days,cancel
  car,Avis,Midsize SUV,A519320,pay later,412.80,14.50,72.50,3,free until pickup

kind is car or room. site_total is the total the page showed, with taxes.
extra_per_day and extra_cap are an add-on the page priced apart, like a child seat; leave them blank if none.
The total is site_total plus the add-on: extra_per_day x days, never above extra_cap when a cap is given.
Nothing here goes online. It reads your file and prints. It writes nothing.
"""
import argparse, csv, io, sys

COLUMNS = ["kind", "company", "offer", "code", "pay", "site_total", "extra_per_day", "extra_cap", "days", "cancel"]


def money(v, field, n):
    v = (v or "").strip().replace("$", "").replace(",", "")
    if not v:
        return 0.0
    try:
        out = float(v)
    except ValueError:
        raise SystemExit(f"row {n}: {field} is not a number: {v!r}")
    if out < 0:
        raise SystemExit(f"row {n}: {field} is below zero")
    return out


def read_quotes(text):
    rows = list(csv.DictReader(io.StringIO(text)))
    if not rows:
        raise SystemExit("no quotes in the file")
    missing = [c for c in COLUMNS if c not in rows[0]]
    if missing:
        raise SystemExit("missing columns: " + ", ".join(missing))
    out = []
    for n, r in enumerate(rows, start=2):
        kind = (r["kind"] or "").strip().lower()
        if kind not in ("car", "room"):
            raise SystemExit(f"row {n}: kind must be car or room")
        site = money(r["site_total"], "site_total", n)
        if not site:
            raise SystemExit(f"row {n}: no site_total; price only what a page showed")
        per_day, cap = money(r["extra_per_day"], "extra_per_day", n), money(r["extra_cap"], "extra_cap", n)
        days = money(r["days"], "days", n)
        if per_day and not days:
            raise SystemExit(f"row {n}: an add-on per day needs days")
        extra = per_day * days
        if cap:
            extra = min(extra, cap)
        out.append({**{k: (r[k] or "").strip() for k in COLUMNS}, "kind": kind, "extra": round(extra, 2),
                    "total": round(site + extra, 2)})
    return out


def table(quotes):
    order = sorted(quotes, key=lambda q: (q["kind"] != "car", q["total"]))
    lines = ["| # | Company | Car or room | Code | Pay now or later | Total with taxes and extras | Cancel |",
             "|---|---|---|---|---|---|---|"]
    for i, q in enumerate(order, start=1):
        extra = f" (incl. ${q['extra']:,.2f} add-on)" if q["extra"] else ""
        lines.append(f"| {i} | {q['company']} | {q['offer']} | {q['code'] or 'none'} | {q['pay']} | "
                     f"${q['total']:,.2f}{extra} | {q['cancel']} |")
    return "\n".join(lines)


def check():
    sample = ("kind,company,offer,code,pay,site_total,extra_per_day,extra_cap,days,cancel\n"
              "room,Hilton,King room,AAA,pay later,610.00,,,3,free until 2 days before\n"
              "car,Hertz,Midsize,,pay later,455.00,13.99,40.00,3,free\n"
              "car,Avis,Midsize,A519320,pay now,380.00,14.50,,3,fee to cancel\n")
    q = read_quotes(sample)
    got = {(x["company"], x["total"]) for x in q}
    assert got == {("Hilton", 610.0), ("Hertz", 495.0), ("Avis", 423.5)}, got  # Hertz seat capped at 40
    rows = table(q).splitlines()[2:]
    assert rows[0].startswith("| 1 | Avis") and rows[1].startswith("| 2 | Hertz") and rows[2].startswith("| 3 | Hilton")
    for bad in ("kind,company\ncar,Avis\n",
                sample.replace("380.00", ""),
                sample.replace("380.00", "abc"),
                sample.replace("455.00,13.99,40.00,3", "455.00,13.99,40.00,")):
        try:
            read_quotes(bad)
        except SystemExit:
            continue
        raise AssertionError("a bad file was accepted: " + bad[:60])
    print("check: ok")


def main(argv):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    t = sub.add_parser("table")
    t.add_argument("--quotes", required=True)
    a = p.parse_args(argv)
    if a.cmd == "check":
        return check()
    with open(a.quotes, encoding="utf-8", newline="") as f:
        print(table(read_quotes(f.read())))


if __name__ == "__main__":
    main(sys.argv[1:])
