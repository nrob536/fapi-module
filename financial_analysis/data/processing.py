import pandas as pd

def calculate_returns(df: pd.DataFrame, price_col: str = "Close") -> pd.Series:
    """Calculate % returns from price series."""
    return df[price_col].pct_change().dropna()