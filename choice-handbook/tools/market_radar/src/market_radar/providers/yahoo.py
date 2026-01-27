from __future__ import annotations

from typing import Any, Dict, List, Optional

import requests


class YahooClient:
    def __init__(
        self, session: Optional[requests.Session] = None, user_agent: Optional[str] = None
    ) -> None:
        self.session = session or requests.Session()
        if user_agent:
            self.session.headers.update({"User-Agent": user_agent})

    def get_quote(self, symbol: str) -> Optional[Dict[str, Any]]:
        url = "https://query1.finance.yahoo.com/v7/finance/quote"
        params = {"symbols": symbol}
        try:
            resp = self.session.get(url, params=params, timeout=20)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("quoteResponse", {}).get("result", [])
            if not results:
                return None
            q = results[0]
            return {
                "price": q.get("regularMarketPrice"),
                "changesPercentage": q.get("regularMarketChangePercent"),
                "volume": q.get("regularMarketVolume"),
            }
        except Exception:
            return None

    def get_historical(self, symbol: str, range_: str = "1mo", interval: str = "1d") -> List[Dict[str, Any]]:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        params: Dict[str, Any] = {"range": range_, "interval": interval}
        try:
            resp = self.session.get(url, params=params, timeout=20)
            resp.raise_for_status()
            data = resp.json()
            result = data.get("chart", {}).get("result", [])
            if not result:
                return []
            series = result[0]
            timestamps = series.get("timestamp", [])
            indicators = series.get("indicators", {}).get("quote", [])
            if not indicators:
                return []
            quotes = indicators[0]
            closes = quotes.get("close", [])
            volumes = quotes.get("volume", [])
            records = []
            for ts, close, volume in zip(timestamps, closes, volumes):
                if close is None:
                    continue
                records.append({"date": ts, "close": close, "volume": volume})
            records.reverse()
            return records
        except Exception:
            return []

    def get_historical_asof(
        self, symbol: str, end_ts: int, lookback_days: int = 45, interval: str = "1d"
    ) -> List[Dict[str, Any]]:
        """
        Fetch history ending at end_ts (unix seconds). Useful for lightweight backtests.
        Yahoo chart API supports period1/period2.
        """
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        period2 = int(end_ts)
        period1 = int(end_ts) - int(lookback_days) * 86400
        params: Dict[str, Any] = {"period1": period1, "period2": period2, "interval": interval}
        try:
            resp = self.session.get(url, params=params, timeout=20)
            resp.raise_for_status()
            data = resp.json()
            result = data.get("chart", {}).get("result", [])
            if not result:
                return []
            series = result[0]
            timestamps = series.get("timestamp", [])
            indicators = series.get("indicators", {}).get("quote", [])
            if not indicators:
                return []
            quotes = indicators[0]
            closes = quotes.get("close", [])
            volumes = quotes.get("volume", [])
            records = []
            for ts, close, volume in zip(timestamps, closes, volumes):
                if close is None:
                    continue
                records.append({"date": ts, "close": close, "volume": volume})
            records.reverse()
            return records
        except Exception:
            return []

    def throttle(self, seconds: float = 0.2) -> None:
        import time

        time.sleep(seconds)
