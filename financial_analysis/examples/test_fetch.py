from financial_analysis.api import YahooFinance

def main():
    yf_api = YahooFinance()
    data = yf_api.get_historical_data("VT", start="2024-01-01", end="2024-01-31")
    print(data.tail())

if __name__ == "__main__":
    main()