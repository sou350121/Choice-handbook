from __future__ import annotations

from typing import Dict, List

import feedparser


def fetch_rss(url: str, limit: int = 5) -> List[Dict[str, str]]:
    feed = feedparser.parse(url)
    entries: List[Dict[str, str]] = []
    for entry in feed.entries[:limit]:
        entries.append(
            {
                "title": getattr(entry, "title", ""),
                "link": getattr(entry, "link", ""),
                "published": getattr(entry, "published", ""),
            }
        )
    return entries
