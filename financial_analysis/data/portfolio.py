import pandas as pd
import numpy as np

def portfolio_returns(weights: list, returns: pd.DataFrame) -> pd.Series:
    """Calculate weighted portfolio returns."""
    return (returns * weights).sum(axis=1)

def annualized_return(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Annualized return from periodic returns."""
    compounded = (1 + returns).prod()
    n_periods = returns.shape[0]
    return compounded ** (periods_per_year / n_periods) - 1

def annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Annualized volatility."""
    return returns.std() * np.sqrt(periods_per_year)

def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0, periods_per_year: int = 252) -> float:
    """Sharpe ratio."""
    excess = returns - risk_free_rate / periods_per_year
    return annualized_return(excess, periods_per_year) / annualized_volatility(excess, periods_per_year)