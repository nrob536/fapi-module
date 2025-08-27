import pandas as pd
from financial_analysis.data.processing import calculate_returns
from financial_analysis.data.indicators import sma, rsi, macd
from financial_analysis.data.portfolio import sharpe_ratio
from financial_analysis.data.utils import validate_prices, fill_missing

# Load price data
df = pd.read_csv("VESG.AX.csv", parse_dates=["Date"], index_col="Date")
df = validate_prices(df)
df = fill_missing(df)

# Calculate returns and indicators
returns = calculate_returns(df)
sma_20 = sma(df["Close"], 20)
rsi_14 = rsi(df["Close"], 14)
macd_df = macd(df["Close"])

# Portfolio Sharpe ratio (single asset example)
sr = sharpe_ratio(returns)
print(f"Sharpe Ratio: {sr:.2f}")