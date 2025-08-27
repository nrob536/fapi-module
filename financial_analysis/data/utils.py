import pandas as pd

def validate_prices(df: pd.DataFrame, price_col: str = "Close") -> pd.DataFrame:
    """Remove rows with non-positive prices."""
    return df[df[price_col] > 0]

def fill_missing(df: pd.DataFrame, method: str = "ffill") -> pd.DataFrame:
    """Fill missing data."""
    return df.fillna(method=method)