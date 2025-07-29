# Financial Analysis Python Module

## Overview
A comprehensive Python module for financial data analysis, leveraging various financial APIs to gather, process, and visualize market data. This project aims to provide tools for both technical and fundamental analysis, with a focus on API integration and dynamic visualization.

## Features

### 1. API Integration 🔌
- Unified interface for multiple financial data providers:
  - Yahoo Finance
  - Alpha Vantage
  - Financial Modeling Prep
- Rate limiting and error handling
- Response caching system
- Automatic retry mechanisms

### 2. Data Processing 📊
- Historical price analysis
- Technical indicators calculation
  - Moving averages (SMA, EMA, VWAP)
  - Momentum indicators (RSI, MACD)
  - Volatility measures
- Portfolio performance metrics
  - Returns calculation
  - Risk assessment
  - Sharpe ratio and other performance metrics
- Data validation and cleaning utilities

### 3. Visualization 📈
Interactive visualization tools using Plotly:
- Candlestick charts
- Technical indicator overlays
- Volume analysis
- Correlation matrices
- Portfolio performance dashboards

## Project Structure
```
financial_analysis/
├── __init__.py
├── api/                  # API integration modules
│   ├── __init__.py
│   ├── base.py
│   ├── yahoo_finance.py
│   └── alpha_vantage.py
├── analysis/            # Data analysis modules
│   ├── __init__.py
│   ├── technical.py
│   └── portfolio.py
├── visualization/       # Visualization components
│   ├── __init__.py
│   ├── charts.py
│   └── dashboard.py
├── utils/              # Utility functions
│   ├── __init__.py
│   ├── cache.py
│   └── helpers.py
└── tests/              # Test suite
    ├── __init__.py
    ├── test_api.py
    └── test_analysis.py
```

## Installation

### Requirements
- Python 3.9 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/nrob536/financial-analysis.git
   cd financial-analysis
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Example
```python
from financial_analysis.api import YahooFinance
from financial_analysis.analysis import TechnicalAnalysis
from financial_analysis.visualization import Charts

# Initialize API client
api = YahooFinance()

# Fetch historical data
data = api.get_historical_data("AAPL", start="2024-01-01")

# Perform analysis
analysis = TechnicalAnalysis(data)
sma = analysis.calculate_sma(window=20)
rsi = analysis.calculate_rsi()

# Create visualization
chart = Charts()
chart.plot_with_indicators(data, [sma, rsi])
```

## Development

### Setting Up Development Environment
1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

### Running Tests
```bash
pytest tests/
```

### Code Style
This project follows PEP 8 style guidelines. Use flake8 for linting:
```bash
flake8 financial_analysis
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Yahoo Finance API
- Alpha Vantage API
- Financial Modeling Prep API
- Plotly visualization library

## Roadmap
- [ ] Phase 1: Core API Integration
  - Basic API wrapper implementation
  - Data fetching and caching
  - Error handling

- [ ] Phase 2: Data Processing
  - Technical indicators
  - Portfolio analytics
  - Risk metrics

- [ ] Phase 3: Visualization
  - Interactive charts
  - Dashboard components
  - Export capabilities

- [ ] Phase 4: Documentation & Testing
  - API documentation
  - Usage examples
  - Test coverage
