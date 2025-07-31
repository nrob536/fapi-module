import abc

class APIBase(abc.ABC):
    """
    Abstract base class for financial data APIs.
    """

    def __init__(self):
        self.session = None

    @abc.abstractmethod
    def get_historical_data(self, symbol: str, start: str = None, end: str = None):
        """
        Fetch historical price data for a given symbol.
        """
        pass

    def handle_error(self, response):
        """
        Handle errors in API responses.
        """
        if hasattr(response, "status_code") and response.status_code != 200:
            raise Exception(f"API Error: {getattr(response, 'status_code', 'Unknown')} - {getattr(response, 'text', 'No message')}")
