import yfinance as yf
from .base import APIBase
from financial_analysis.utils.cache import SimpleCache


class YahooFinance(APIBase):
    """
    Yahoo Finance API wrapper using yfinance.
    """

    def __init__(self):
        super().__init__()
        self.cache = SimpleCache(expire_seconds=600)

    def get_historical_data(self, symbol: str, start: str = None, end: str = None):
        cache_key = f"{symbol}_{start}_{end}"
        cached_data = self.cache.get(cache_key)
        if cached_data is not None:
            return cached_data
        try:
            data = yf.download(symbol, start=start, end=end)
            if data.empty:
                raise Exception("No data returned from Yahoo Finance.")
            return data
        except Exception as e:
            self.handle_error(e)