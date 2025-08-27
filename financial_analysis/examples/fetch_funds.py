from financial_analysis.api.yahoo_finance import YahooFinance

def main():
    yf_api = YahooFinance()
    funds = {
        "Vanguard International Shares Select Exclusions Index Fund (ETF)": "VESG.AX",
        "Smart - Australian Top 200 ETF (AUS)": "AUS.NZ"
        # Managed fund with APIR: VAN1579AU not available via yfinance
    }
    for name, ticker in funds.items():
        print(f"\nFetching data for: {name} ({ticker})")
        try:
            data = yf_api.get_historical_data(ticker, start="2020-01-01", end="2025-01-01")
            print(data.tail())
        except Exception as e:
            print(f"Error fetching {name}: {e}")

    print("\nVanguard Intl Shares Selected Exclusions Index Fund - NZD Hedge (VAN1579AU) is not available on Yahoo Finance. Please download data manually from the provider's website.")

if __name__ == "__main__":
    main()