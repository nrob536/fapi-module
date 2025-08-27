import pandas as pd

def sma(series: pd.Series, window: int = 20) -> pd.Series:
    """Simple Moving Average."""
    return series.rolling(window=window).mean()

def ema(series: pd.Series, window: int = 20) -> pd.Series:
    """Exponential Moving Average."""
    return series.ewm(span=window, adjust=False).mean()

def vwap(df: pd.DataFrame) -> pd.Series:
    """Volume Weighted Average Price."""
    return (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()

def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    """Relative Strength Index."""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    """MACD and Signal line."""
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    return pd.DataFrame({'MACD': macd_line, 'Signal': signal_line})

def volatility(series: pd.Series, window: int = 20) -> pd.Series:
    """Rolling volatility (standard deviation of returns)."""
    return series.pct_change().rolling(window=window).std()