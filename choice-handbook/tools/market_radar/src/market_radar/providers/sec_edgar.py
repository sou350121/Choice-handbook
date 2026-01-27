from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

SEC_TICKER_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_SUBMISSION_URL = "https://data.sec.gov/submissions/CIK{cik}.json"


class SecEdgarClient:
    def __init__(self, user_agent: str, session: Optional[requests.Session] = None) -> None:
        self.user_agent = user_agent
        self.session = session or requests.Session()

    def _get(self, url: str) -> Any:
        headers = {"User-Agent": self.user_agent}
        resp = self.session.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        return resp.json()

    def load_ticker_map(self, cache_path: Path) -> Dict[str, str]:
        if cache_path.exists():
            return json.loads(cache_path.read_text(encoding="utf-8"))
        data = self._get(SEC_TICKER_URL)
        ticker_map: Dict[str, str] = {}
        for _, item in data.items():
            ticker = item.get("ticker")
            cik = item.get("cik_str")
            if ticker and cik:
                ticker_map[ticker.upper()] = f"{int(cik):010d}"
        cache_path.write_text(json.dumps(ticker_map, ensure_ascii=False, indent=2), encoding="utf-8")
        return ticker_map

    def get_recent_filings(self, cik: str, limit: int = 3) -> List[Dict[str, str]]:
        data = self._get(SEC_SUBMISSION_URL.format(cik=cik))
        filings = data.get("filings", {}).get("recent", {})
        forms = filings.get("form", [])
        dates = filings.get("filingDate", [])
        accessions = filings.get("accessionNumber", [])
        primary_docs = filings.get("primaryDocument", [])
        descriptions = filings.get("primaryDocDescription", [])
        results: List[Dict[str, str]] = []
        for idx in range(min(limit, len(forms))):
            accession = accessions[idx].replace("-", "")
            url = (
                f"https://www.sec.gov/Archives/edgar/data/"
                f"{int(cik)}/{accession}/{primary_docs[idx]}"
            )
            results.append(
                {
                    "form": forms[idx],
                    "date": dates[idx],
                    "description": descriptions[idx] if idx < len(descriptions) else "",
                    "url": url,
                }
            )
        return results
