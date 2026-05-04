#!/usr/bin/env python3
"""
Export SEC primary-document iXBRL/XBRL (.htm, .html, common inline filings) to:

  - text: one fact per line (good for grepping / LLM chunks)
  - json: full ixbrlparse structure (good for programmatic use)

Depends on: pip install ixbrlparse beautifulsoup4 lxml

Examples:
  python3 scripts/export_ixbrl_readable.py --format text filing.htm
  python3 scripts/export_ixbrl_readable.py --format json -o facts.json filing.htm
  python3 scripts/export_ixbrl_readable.py --format text *.htm > all_facts.txt
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _period(ctx) -> str:
    if ctx is None:
        return ""
    if getattr(ctx, "instant", None):
        return f"instant={ctx.instant}"
    if getattr(ctx, "startdate", None) and getattr(ctx, "enddate", None):
        return f"duration={ctx.startdate}..{ctx.enddate}"
    return ""


def _segments(ctx) -> str:
    if ctx is None or not getattr(ctx, "segments", None):
        return ""
    parts = []
    for s in ctx.segments:
        dim = s.get("dimension") or ""
        val = s.get("value") or ""
        parts.append(f"{dim}={val}")
    out = "; ".join(parts)
    if len(out) > 200:
        return out[:197] + "..."
    return out


def _norm_value(val) -> str:
    if val is None:
        return ""
    s = str(val)
    return " ".join(s.split())


def emit_text(ix, source: Path, out) -> None:
    rows = []
    for v in ix.numeric:
        ctx = v.context
        cid = getattr(ctx, "id", "") if ctx else ""
        rows.append(
            (
                f"{v.schema}:{v.name}",
                _norm_value(v.value),
                _norm_value(getattr(v, "unit", "") or ""),
                cid,
                _period(ctx),
                _segments(ctx),
            )
        )
    for v in ix.nonnumeric:
        ctx = v.context
        cid = getattr(ctx, "id", "") if ctx else ""
        rows.append(
            (
                f"{v.schema}:{v.name}",
                _norm_value(getattr(v, "value", None)),
                "",
                cid,
                _period(ctx),
                _segments(ctx),
            )
        )

    rows.sort(key=lambda r: (r[0], r[3], r[4]))

    print(f"=== SOURCE: {source} ===", file=out)
    print(f"filetype: {ix.filetype}", file=out)
    print(f"facts_numeric: {len(ix.numeric)}", file=out)
    print(f"facts_nonnumeric: {len(ix.nonnumeric)}", file=out)
    print(f"errors: {len(ix.errors)}", file=out)
    print("", file=out)
    print(
        "concept\tvalue\tunit\tcontext\tperiod\tsegments",
        file=out,
    )
    for concept, value, unit, ctx_id, period, segs in rows:
        print(f"{concept}\t{value}\t{unit}\t{ctx_id}\t{period}\t{segs}", file=out)
    print("", file=out)


def emit_json(ix, out, indent: int | None) -> None:
    payload = ix.to_json()
    json.dump(payload, out, indent=indent, ensure_ascii=False, default=str)
    out.write("\n")


def main() -> int:
    p = argparse.ArgumentParser(description="iXBRL / inline XBRL → text or JSON")
    p.add_argument(
        "filings",
        nargs="+",
        type=Path,
        help="Primary SEC instance (.htm / .html) or other ixbrlparse-supported file",
    )
    p.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="text = tab-separated facts; json = full ixbrlparse dump",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Write here instead of stdout (single filing only)",
    )
    p.add_argument(
        "--json-indent",
        type=int,
        default=2,
        help="Pretty-print indent for JSON (0 = compact)",
    )
    args = p.parse_args()

    try:
        from ixbrlparse import IXBRL
        from ixbrlparse.core import IXBRLParseError
    except ImportError:
        print(
            "Missing dependency: pip install ixbrlparse beautifulsoup4 lxml",
            file=sys.stderr,
        )
        return 1

    if args.output is not None and len(args.filings) > 1:
        print("--output supports only one input file", file=sys.stderr)
        return 1

    indent = None if args.json_indent <= 0 else args.json_indent

    for i, path in enumerate(args.filings):
        if not path.is_file():
            print(f"Not a file: {path}", file=sys.stderr)
            return 1
        try:
            ix = IXBRL.open(path)
        except IXBRLParseError as e:
            print(f"{path}: {e}", file=sys.stderr)
            return 1

        if args.output:
            fh = args.output.open("w", encoding="utf-8")
        else:
            fh = sys.stdout

        try:
            if args.format == "json":
                if len(args.filings) > 1:
                    print(f"=== SOURCE: {path} ===", file=fh)
                emit_json(ix, fh, indent)
                if len(args.filings) > 1 and i < len(args.filings) - 1:
                    print("\n", file=fh)
            else:
                emit_text(ix, path, fh)
        finally:
            if args.output:
                fh.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
