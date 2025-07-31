import yfinance as yf
from base import APIBase

class YahooFinance(APIBase):
    """
    Yahoo Finance API wrapper using yfinance.
    """

    def __init__(self):
        super().__init__()

    def get_historical_data(self, symbol: str, start: str = None, end: str = None):
        try:
            data = yf.download(symbol, start=start, end=end)
            if data.empty:
                raise Exception("No data returned from Yahoo Finance.")
            return data
        except Exception as e:
            self.handle_error(e)