#!/usr/bin/env python3
"""knowledge_updater.py — Business Data Analysis & Insights (Idea 67)

Crawl analytics-method + KPI-benchmark sources, score by recency + relevance,
append deduplicated entries to SECOND-KNOWLEDGE-BRAIN.md.

Run: python knowledge_updater.py [--dry-run]   Schedule: weekly cron.
Dependencies: crawl4ai (optional; degrades gracefully).
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, pathlib, re

BRAIN = pathlib.Path(__file__).resolve().parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"

SOURCES = [
    {"name": "SSRN Analytics", "url": "https://www.ssrn.com/index.cfm/en/"},
    {"name": "HBR Analytics", "url": "https://hbr.org/topic/subject/analytics"},
    {"name": "Towards Data Science", "url": "https://towardsdatascience.com/"},
]
QUERIES = ["business analytics method 2026", "KPI benchmark report",
           "data storytelling", "cohort analysis business"]
KEYWORDS = ["analytics", "kpi", "metric", "cohort", "revenue", "trend", "segmentation",
            "pareto", "insight", "data", "benchmark"]


def fetch(source: dict) -> list[dict]:
    try:
        from crawl4ai import WebCrawler  # type: ignore
        c = WebCrawler(); c.warmup()
        text = getattr(c.run(url=source["url"]), "markdown", "") or ""
    except Exception as exc:
        print(f"[warn] crawl unavailable for {source['name']}: {exc}")
        return []
    out = []
    for line in text.splitlines():
        t = line.strip("#* -").strip()
        if 20 < len(t) < 200 and any(k in t.lower() for k in KEYWORDS):
            out.append({"title": t, "source": source["name"], "url": source["url"]})
    return out


def score(e: dict) -> float:
    return sum(k in e["title"].lower() for k in KEYWORDS)


def existing_hashes(text: str) -> set[str]:
    return set(re.findall(r"<!--h:([0-9a-f]{12})-->", text))


def entry_hash(e: dict) -> str:
    return hashlib.sha1((e["url"] + e["title"]).encode()).hexdigest()[:12]


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    brain = BRAIN.read_text(encoding="utf-8") if BRAIN.exists() else ""
    seen = existing_hashes(brain)
    collected: list[dict] = []
    for s in SOURCES:
        collected.extend(fetch(s))
    collected.sort(key=score, reverse=True)
    today = dt.date.today().isoformat()
    lines = []
    for e in collected:
        h = entry_hash(e)
        if h in seen:
            continue
        seen.add(h)
        lines.append(f"- [{today}] {e['title']} — {e['source']} — {e['url']} <!--h:{h}-->")
    if not lines:
        print("No new entries."); return
    block = f"\n### Auto-update {today}\n" + "\n".join(lines) + "\n"
    if args.dry_run:
        print(block); return
    with BRAIN.open("a", encoding="utf-8") as fh:
        fh.write(block)
    print(f"Appended {len(lines)} entries.")


if __name__ == "__main__":
    main()
