#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Match:
    score: int
    path: Path
    title: str
    snippet: str


def resolve_root(override: str | None) -> Path:
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parent.parent / "references" / "zh-cn"


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return fallback


def excerpt(text: str, terms: list[str]) -> str:
    lower = text.casefold()
    best = len(text)
    for term in terms:
        idx = lower.find(term.casefold())
        if idx >= 0 and idx < best:
            best = idx

    if best == len(text):
        return re.sub(r"\s+", " ", text[:180]).strip()

    start = max(0, best - 60)
    end = min(len(text), best + 140)
    chunk = text[start:end]
    chunk = re.sub(r"\s+", " ", chunk).strip()
    if start > 0:
        chunk = "..." + chunk
    if end < len(text):
        chunk += "..."
    return chunk


def score_doc(path: Path, title: str, text: str, terms: list[str]) -> int:
    haystack = f"{path.name}\n{title}\n{text}".casefold()
    score = 0
    for term in terms:
        needle = term.casefold()
        hits = haystack.count(needle)
        if hits:
            score += hits * 10
            if needle in path.name.casefold():
                score += 40
            if needle in title.casefold():
                score += 25
    return score


def collect_matches(root: Path, terms: list[str]) -> list[Match]:
    matches: list[Match] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        title = first_heading(text, path.stem)
        score = score_doc(path, title, text, terms)
        if score <= 0:
            continue
        rel = path.relative_to(root)
        matches.append(Match(score, rel, title, excerpt(text, terms)))
    matches.sort(key=lambda item: (-item.score, str(item.path)))
    return matches


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search the webman zh-cn manual by keyword."
    )
    parser.add_argument("terms", nargs="+", help="Keywords to search for")
    parser.add_argument("--root", help="Override manual root directory")
    parser.add_argument("--limit", type=int, default=8, help="Max matches to print")
    args = parser.parse_args()

    root = resolve_root(args.root)
    if not root.exists():
        raise SystemExit(f"manual root not found: {root}")

    matches = collect_matches(root, args.terms)
    if not matches:
        print("No matches.")
        return 1

    for match in matches[: args.limit]:
        print(f"{match.score:>4}  {match.path.as_posix()}")
        print(f"      {match.title}")
        print(f"      {match.snippet}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
