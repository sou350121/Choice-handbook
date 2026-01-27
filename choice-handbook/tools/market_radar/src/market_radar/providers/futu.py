from __future__ import annotations

from typing import Any, Dict, List, Optional

try:
    from futu import OpenQuoteContext, RET_OK, AuType, KLType
except Exception:  # pragma: no cover - optional dependency
    OpenQuoteContext = None
    RET_OK = None
    AuType = None
    KLType = None


class FutuClient:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._ctx: Optional[OpenQuoteContext] = None  # type: ignore[name-defined]

    @property
    def available(self) -> bool:
        return OpenQuoteContext is not None

    def _ensure_ctx(self) -> bool:
        if not self.available:
            return False
        if self._ctx is None:
            self._ctx = OpenQuoteContext(host=self.host, port=self.port)  # type: ignore[call-arg]
        return True

    def close(self) -> None:
        if self._ctx is not None:
            self._ctx.close()
            self._ctx = None

    def get_snapshot(self, code: str) -> Optional[Dict[str, Any]]:
        snapshots = self.get_snapshots([code])
        return snapshots.get(code)

    def get_snapshots(self, codes: List[str]) -> Dict[str, Dict[str, Any]]:
        if not self._ensure_ctx():
            return {}
        if not codes:
            return {}
        ret, data = self._ctx.get_market_snapshot(codes)  # type: ignore[union-attr]
        if ret != RET_OK or data is None or data.empty:
            return {}
        results: Dict[str, Dict[str, Any]] = {}
        for _, row in data.iterrows():
            code = row.get("code")
            if not code:
                continue
            results[code] = {
                "price": row.get("last_price"),
                "changesPercentage": row.get("change_rate"),
                "volume": row.get("volume"),
            }
        return results

    def get_historical(self, code: str, count: int = 30) -> List[Dict[str, Any]]:
        if not self._ensure_ctx():
            return []
        ret, data, _ = self._ctx.request_history_kline(  # type: ignore[union-attr]
            code,
            ktype=KLType.K_DAY,  # type: ignore[arg-type]
            autype=AuType.QFQ,  # type: ignore[arg-type]
            max_count=count,
        )
        if ret != RET_OK or data is None or data.empty:
            return []
        records: List[Dict[str, Any]] = []
        for _, row in data.iterrows():
            records.append(
                {
                    "date": row.get("time_key"),
                    "close": row.get("close"),
                    "volume": row.get("volume"),
                }
            )
        records.reverse()
        return records
