import abc
import logging

class APIBase(abc.ABC):
    """
    Abstract base class for financial data APIs.
    """

    def __init__(self):
        self.session = None
        self.logger = logging.getLogger(self.__class__.__name__)

    @abc.abstractmethod
    def get_historical_data(self, symbol: str, start: str = None, end: str = None):
        pass

    def handle_error(self, error):
        """
        Handle errors in API responses and log them.
        """
        self.logger.error(f"API Error: {error}")
        raise Exception(f"API Error: {error}")