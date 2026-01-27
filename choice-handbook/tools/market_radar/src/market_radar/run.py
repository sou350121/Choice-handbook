from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import requests
import yaml

from market_radar.mini06 import build_mini06
from market_radar.providers.futu import FutuClient
from market_radar.providers.yahoo import YahooClient
from market_radar.providers.rss import fetch_rss
from market_radar.providers.sec_edgar import SecEdgarClient
from market_radar.render.markdown import (
    render_mini06_report,
    render_rolling_summary,
    render_sources_digest,
)
from market_radar.signals import (
    FINANCIAL_KEYWORDS,
    PLATFORM_KEYWORDS,
    SUPPLYCHAIN_KEYWORDS,
    compute_metrics,
    count_keywords,
    score_signals,
)


def load_config(path: Path) -> Dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def build_text_blob(filings: List[Dict[str, str]], rss_items: List[Dict[str, str]]) -> str:
    parts = []
    for filing in filings:
        parts.append(filing.get("form", ""))
        parts.append(filing.get("description", ""))
    for item in rss_items:
        parts.append(item.get("title", ""))
    return " ".join(parts)


def load_last_run(cache_path: Path) -> Dict[str, Any]:
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    return {}


def compute_delta(last_run: Dict[str, Any], current_scores: Dict[str, int], top3: List[str]) -> List[str]:
    if not last_run:
        return ["No previous run."]
    lines: List[str] = []
    last_scores = last_run.get("scores", {})
    # Backward/forward compatible: accept either `top3` or split `top3_us/top3_cn`.
    last_top3 = set(last_run.get("top3", [])) | set(last_run.get("top3_us", [])) | set(last_run.get("top3_cn", []))
    for symbol in top3:
        if symbol not in last_top3:
            lines.append(f"NEW Top3: {symbol}")
    for symbol, score in current_scores.items():
        last_score = last_scores.get(symbol)
        if last_score is None:
            continue
        diff = score - last_score
        if abs(diff) >= 2:
            lines.append(f"Score change: {symbol} {last_score} -> {score} ({diff:+d})")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, required=True, help="choice-handbook root")
    parser.add_argument(
        "--config",
        type=str,
        default="tools/market_radar/config/watchlist.yaml",
    )
    parser.add_argument("--run-date", type=str, default=None)
    parser.add_argument(
        "--writeback-opportunity-map",
        action="store_true",
        help="Update distilled/opportunity_map.md in a safe auto block (per-universe).",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    config_path = root / args.config
    run_date = args.run_date or datetime.now().strftime("%Y-%m-%d")
    # Treat `run_date` as an as-of date for lightweight replay/backtest (Yahoo only).
    # If the user is running "today" but passes --run-date explicitly, this still works.
    try:
        asof_dt = datetime.strptime(run_date, "%Y-%m-%d")
        asof_ts = int(asof_dt.timestamp())
    except Exception:
        asof_ts = None

    yahoo_user_agent = os.environ.get("YAHOO_USER_AGENT")
    futu_host = os.environ.get("FUTU_HOST", "127.0.0.1")
    futu_port = int(os.environ.get("FUTU_PORT", "11111"))

    config = load_config(config_path)
    universe = config.get("universe", "us_ai_infra")
    primary_provider = config.get("primary_provider", "futu")
    fallback_provider = config.get("fallback_provider", "yahoo")
    futu_history_enabled = config.get("futu_history_enabled", True)
    futu_history_top_n = int(config.get("futu_history_top_n", 10))
    futu_snapshot_batch = int(config.get("futu_snapshot_batch", 50))

    cache_dir = root / ".cache" / "market_radar"
    cache_dir.mkdir(parents=True, exist_ok=True)
    last_run_path = cache_dir / "last_run.json"

    session = requests.Session()
    if yahoo_user_agent:
        session.headers.update({"User-Agent": yahoo_user_agent})
    yahoo = YahooClient(session=session, user_agent=yahoo_user_agent)
    futu = FutuClient(host=futu_host, port=futu_port)

    sec_user_agent = os.environ.get("SEC_USER_AGENT")
    sec_client = None
    ticker_map: Dict[str, str] = {}
    if sec_user_agent:
        sec_client = SecEdgarClient(user_agent=sec_user_agent, session=session)
        ticker_map = sec_client.load_ticker_map(cache_dir / "company_tickers.json")

    snapshot_cache: Dict[str, Dict[str, Any]] = {}
    if primary_provider == "futu" and futu.available:
        futu_codes = [item.get("futu_code") for item in config.get("tickers", []) if item.get("futu_code")]
        for i in range(0, len(futu_codes), futu_snapshot_batch):
            chunk = futu_codes[i : i + futu_snapshot_batch]
            snapshot_cache.update(futu.get_snapshots(chunk))

    entries: List[Dict[str, Any]] = []
    scores: Dict[str, int] = {}

    def normalize_change(quote_data: Dict[str, Any]) -> Dict[str, Any]:
        value = quote_data.get("changesPercentage")
        if value is not None and abs(value) > 1:
            quote_data["changesPercentage"] = value / 100
        return quote_data

    def fetch_with_provider(provider: str, item: Dict[str, Any]) -> Dict[str, Any]:
        symbol = item["symbol"].upper()
        futu_code = item.get("futu_code")
        if provider == "futu":
            if futu.available and futu_code:
                quote = snapshot_cache.get(futu_code) or futu.get_snapshot(futu_code)
                history = []
                if quote:
                    quote = normalize_change(quote)
                return {
                    "quote": quote,
                    "history": history,
                    "source": "futu",
                }
            # If futu is unavailable OR no futu_code is provided (common for US tickers),
            # transparently fall back to Yahoo so we don't end up with n/a everywhere.
            quote = yahoo.get_quote(symbol)
            history = yahoo.get_historical(symbol, range_="1mo", interval="1d")
            if quote:
                quote = normalize_change(quote)
            return {"quote": quote, "history": history, "source": "yahoo"}
        # Yahoo provider: if `asof_ts` is set, fetch history ending at that date,
        # and derive "quote" from the last two closes to avoid using today's quote.
        if asof_ts:
            history = yahoo.get_historical_asof(symbol, end_ts=asof_ts, lookback_days=45, interval="1d")
            quote = None
            if history:
                latest = history[0]
                prev = history[1] if len(history) > 1 else None
                price = latest.get("close")
                volume = latest.get("volume")
                change_pct = None
                if prev and prev.get("close") and price:
                    try:
                        change_pct = (price / prev["close"]) - 1
                    except Exception:
                        change_pct = None
                quote = {
                    "price": price,
                    "changesPercentage": change_pct,
                    "volume": volume,
                }
        else:
            quote = yahoo.get_quote(symbol)
            history = yahoo.get_historical(symbol, range_="1mo", interval="1d")
        if quote:
            quote = normalize_change(quote)
        return {"quote": quote, "history": history, "source": "yahoo"}

    for item in config.get("tickers", []):
        symbol = item["symbol"].upper()
        primary = fetch_with_provider(primary_provider, item)
        quote = primary["quote"]
        history = primary["history"]
        data_source = primary["source"]

        if (quote is None or not history) and fallback_provider and fallback_provider != primary_provider:
            fallback = fetch_with_provider(fallback_provider, item)
            if quote is None:
                quote = fallback["quote"]
            if not history:
                history = fallback["history"]
            if quote is not None or history:
                data_source = fallback["source"]

        metrics = compute_metrics(quote or {}, history)

        filings: List[Dict[str, str]] = []
        if sec_client and symbol in ticker_map:
            filings = sec_client.get_recent_filings(ticker_map[symbol], limit=3)

        rss_items: List[Dict[str, str]] = []
        for feed_url in item.get("rss", []):
            rss_items.extend(fetch_rss(feed_url, limit=3))

        text_blob = build_text_blob(filings, rss_items)
        text_hits = {
            "supplychain": count_keywords(text_blob, SUPPLYCHAIN_KEYWORDS),
            "platform": count_keywords(text_blob, PLATFORM_KEYWORDS),
            "financial": count_keywords(text_blob, FINANCIAL_KEYWORDS),
        }
        score, signal_tags, risk_flags = score_signals(metrics, text_hits)

        entry = {
            "symbol": symbol,
            "name": item.get("name", ""),
            "tags": item.get("tags", []),
            "metrics": metrics,
            "data_source": data_source,
            "filings": filings,
            "rss": rss_items,
            "score": score,
            "signal_tags": signal_tags,
            "risk_flags": risk_flags,
            "text_hits": text_hits,
            "futu_code": item.get("futu_code"),
        }
        entries.append(entry)
        scores[symbol] = score
        yahoo.throttle()

    if futu_history_enabled:
        futu_candidates = [
            e for e in entries if e.get("data_source") == "futu" and e.get("futu_code")
        ]
        futu_candidates = sorted(futu_candidates, key=lambda x: x.get("score", 0), reverse=True)
        for entry in futu_candidates[:futu_history_top_n]:
            history = futu.get_historical(entry["futu_code"], count=30)  # type: ignore[arg-type]
            if history:
                metrics = compute_metrics(entry.get("metrics", {}), history)
                entry["metrics"] = metrics
                score, signal_tags, risk_flags = score_signals(metrics, entry.get("text_hits", {}))
                entry["score"] = score
                entry["signal_tags"] = signal_tags
                entry["risk_flags"] = risk_flags

    region_tags = {"hk", "sh", "sz"}
    us_candidates = [
        e for e in entries if not (set(t.lower() for t in e.get("tags", [])) & region_tags)
    ]
    cn_candidates = [
        e for e in entries if (set(t.lower() for t in e.get("tags", [])) & region_tags)
    ]

    top3_us = sorted(us_candidates, key=lambda x: x.get("score", 0), reverse=True)[:3]
    top3_cn = sorted(cn_candidates, key=lambda x: x.get("score", 0), reverse=True)[:3]

    for entry in top3_us + top3_cn:
        entry["mini06"] = build_mini06(entry)

    last_run = load_last_run(last_run_path)
    top3_symbols = [e["symbol"] for e in top3_us] + [e["symbol"] for e in top3_cn]
    delta_lines = compute_delta(last_run, scores, top3_symbols)

    sources_dir = root / "sources"
    world_dir = root / "world_understanding"
    runs_dir = world_dir / "market_radar_runs"
    runs_dir.mkdir(parents=True, exist_ok=True)

    sources_path = sources_dir / f"{run_date}_market_radar_{universe}.md"
    mini06_path = runs_dir / f"{run_date}_{universe}_top3_mini06.md"
    rolling_path = world_dir / f"market_radar_{universe}.md"

    entries_sorted = sorted(entries, key=lambda x: x.get("score", 0), reverse=True)
    sources_md = render_sources_digest(run_date, universe, entries_sorted, delta_lines)
    sources_rel = sources_path.relative_to(root).as_posix()
    mini06_rel = mini06_path.relative_to(root).as_posix()
    mini06_md = render_mini06_report(run_date, universe, top3_us, top3_cn, sources_rel)
    rolling_md = render_rolling_summary(
        run_date,
        universe,
        sources_rel,
        mini06_rel,
        top3_us,
        top3_cn,
    )

    sources_path.write_text(sources_md, encoding="utf-8")
    mini06_path.write_text(mini06_md, encoding="utf-8")
    rolling_path.write_text(rolling_md, encoding="utf-8")

    # Writeback helpers (safe, marker-based). We avoid auto-editing meta tables because
    # they are hand-curated and table edits are easy to corrupt. Instead we:
    # 1) optionally update `distilled/opportunity_map.md` via per-universe markers
    # 2) always emit a short writeback suggestion note in runs_dir

    def _render_top_line(items: List[Dict[str, Any]]) -> str:
        parts = []
        for e in items[:3]:
            parts.append(f"{e['symbol']}({e.get('score')})")
        return ", ".join(parts) if parts else "n/a"

    def _bucket_to_hypothesis(bucket: str | None) -> str:
        if bucket in ("memory", "supplychain"):
            return "H-0002"
        if bucket == "platform":
            return "H-0013"
        if bucket == "financial":
            return "H-0010"
        return "H-0002"

    # Emit writeback suggestions for meta/hypotheses_registry.md (manual copy/paste).
    wb_path = runs_dir / f"{run_date}_{universe}_writeback.md"
    top_us_bucket = (top3_us[0].get("mini06") or {}).get("primary_bucket") if top3_us else None
    top_cn_bucket = (top3_cn[0].get("mini06") or {}).get("primary_bucket") if top3_cn else None
    wb_lines = [
        f"# {run_date} | Market Radar ({universe}) Writeback Suggestions",
        "",
        f"- Evidence snapshot: `{sources_rel}`",
        f"- Mini-06: `{mini06_rel}`",
        "",
        "## Suggested meta updates (copy/paste intent)",
        f"- Update `{_bucket_to_hypothesis(top_us_bucket)}`: Top US signals = {_render_top_line(top3_us)} (bucket={top_us_bucket or 'n/a'})",
        f"- Update `{_bucket_to_hypothesis(top_cn_bucket)}`: Top HK/SH/SZ signals = {_render_top_line(top3_cn)} (bucket={top_cn_bucket or 'n/a'})",
        "",
        "## Suggested distilled update (opportunity map)",
        f"- If this universe matters, reflect Gate/Tripwire/probe into `distilled/opportunity_map.md` (or keep as Gate2 watchlist).",
        "",
    ]
    wb_path.write_text("\n".join(wb_lines).strip() + "\n", encoding="utf-8")

    # Optional: update opportunity map auto-block (per universe).
    if args.writeback_opportunity_map:
        opp_path = root / "distilled" / "opportunity_map.md"
        if opp_path.exists():
            marker_start = f"<!-- market_radar:auto:{universe}:start -->"
            marker_end = f"<!-- market_radar:auto:{universe}:end -->"
            block = "\n".join(
                [
                    marker_start,
                    f"## Market Radar (auto) — {universe}",
                    f"- Latest run: {run_date}",
                    f"- Evidence: `{sources_rel}`",
                    f"- Mini-06: `{mini06_rel}`",
                    f"- Top US: {_render_top_line(top3_us)}",
                    f"- Top HK/SH/SZ: {_render_top_line(top3_cn)}",
                    "",
                    marker_end,
                ]
            )
            text = opp_path.read_text(encoding="utf-8")
            if marker_start in text and marker_end in text:
                before = text.split(marker_start, 1)[0]
                after = text.split(marker_end, 1)[1]
                text = before + block + after
            else:
                # Insert right after the first horizontal rule if present, else near top.
                insert_at = text.find("\n---\n")
                if insert_at != -1:
                    insert_at = insert_at + len("\n---\n")
                    text = text[:insert_at] + "\n" + block + "\n" + text[insert_at:]
                else:
                    text = block + "\n\n" + text
            opp_path.write_text(text, encoding="utf-8")

    last_run_payload = {
        "run_date": run_date,
        "scores": scores,
        "top3": top3_symbols,
        "top3_us": [e["symbol"] for e in top3_us],
        "top3_cn": [e["symbol"] for e in top3_cn],
    }
    last_run_path.write_text(json.dumps(last_run_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    futu.close()


if __name__ == "__main__":
    main()
