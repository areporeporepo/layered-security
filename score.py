#!/usr/bin/env python3
"""Weekly Aggregate Exposure Index (AEI) report from an incident log.

Reads incidents.csv (the schema in docs/incident-log-template.md) and prints, per
ISO week, the summed severity for each layer plus the total across layers — the
Aggregate Exposure Index — with an up/down trend arrow versus the prior week.

This is the model in docs/scoring.md:
    Layer score (week) = sum of severities of incidents in that layer
    AEI (week)         = sum of all layer scores
The single AEI number is the thing no individual actor in any layer can see.

Severity that is missing, empty, or non-numeric is treated as 0 so a half-filled
log still reports rather than crashing — see the honesty check in scoring.md.

Usage:
    python3 score.py [path-to-csv]      # default: incidents.csv
"""

import csv
import sys
from collections import defaultdict
from datetime import date

# Layer order matches the table in docs/scoring.md (Work Social Nbhd Home Inst).
# Maps the layer tags used in the log to display columns.
LAYERS = [
    ("workplace", "Work"),
    ("social", "Social"),
    ("neighborhood", "Nbhd"),
    ("home", "Home"),
    ("institutional", "Inst"),
]


def parse_severity(raw):
    """Return an int severity, or 0 if missing/empty/non-numeric."""
    if raw is None:
        return 0
    raw = raw.strip()
    if not raw:
        return 0
    try:
        return int(float(raw))
    except ValueError:
        return 0


def iso_week_label(date_str):
    """Return an ISO-week label like '2026-W25' from a YYYY-MM-DD date, or None."""
    try:
        y, m, d = (int(p) for p in date_str.strip().split("-"))
        iso_year, iso_week, _ = date(y, m, d).isocalendar()
        return f"{iso_year}-W{iso_week:02d}"
    except (ValueError, AttributeError):
        return None


def load(path):
    """Aggregate the log into {week: {layer_tag: summed_severity}}."""
    weeks = defaultdict(lambda: defaultdict(int))
    skipped = 0
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            week = iso_week_label(row.get("date", ""))
            layer = (row.get("layer") or "").strip().lower()
            if week is None or layer not in dict(LAYERS):
                skipped += 1
                continue
            weeks[week][layer] += parse_severity(row.get("severity_1to5"))
    return weeks, skipped


def trend_arrow(current, previous):
    """Arrow + word comparing this week's AEI to the prior reported week's."""
    if previous is None:
        return ""
    if current > previous:
        return "▲ up"
    if current < previous:
        return "▼ down"
    return "= flat"


def report(weeks):
    if not weeks:
        print("No scorable incidents found.")
        return

    headers = [name for _, name in LAYERS]
    cols = "  ".join(f"{h:>6}" for h in headers)
    print(f"{'Week':<10}{cols}  {'AEI':>5}   trend")
    print("-" * (10 + len(cols) + 14))

    prev_aei = None
    for week in sorted(weeks):
        scores = weeks[week]
        layer_vals = [scores.get(tag, 0) for tag, _ in LAYERS]
        aei = sum(layer_vals)
        cells = "  ".join(f"{v:>6}" for v in layer_vals)
        arrow = trend_arrow(aei, prev_aei)
        print(f"{week:<10}{cells}  {aei:>5}   {arrow}")
        prev_aei = aei


def main(argv):
    path = argv[1] if len(argv) > 1 else "incidents.csv"
    try:
        weeks, skipped = load(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        print("Usage: python3 score.py [path-to-csv]")
        return 1
    report(weeks)
    if skipped:
        print(f"\n({skipped} row(s) skipped: bad date or unknown layer.)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
