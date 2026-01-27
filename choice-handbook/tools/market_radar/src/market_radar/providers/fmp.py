from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests


class FMPClient:
    def __init__(self, api_key: str, session: Optional[requests.Session] = None) -> None:
        self.api_key = api_key
        self.session = session or requests.Session()
        self.base_url = "https://financialmodelingprep.com/api/v3"

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        params = params or {}
        params["apikey"] = self.api_key
        url = f"{self.base_url}/{path}"
        resp = self.session.get(url, params=params, timeout=20)
        resp.raise_for_status()
        return resp.json()

    def get_quote(self, symbol: str) -> Optional[Dict[str, Any]]:
        try:
            data = self._get(f"quote/{symbol}")
            if not data:
                return None
            return data[0]
        except Exception:
            return None

    def get_historical(self, symbol: str, timeseries: int = 30) -> List[Dict[str, Any]]:
        try:
            data = self._get(
                f"historical-price-full/{symbol}", params={"timeseries": timeseries}
            )
            return data.get("historical", [])
        except Exception:
            return []

    def throttle(self, seconds: float = 0.2) -> None:
        time.sleep(seconds)
