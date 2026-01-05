import numpy as np

# calculates total return given a series of closing prices
def total_return(close_prices):
    if close_prices.empty:
        return 0
    else:
        return close_prices.iloc[-1] / close_prices.iloc[0] - 1

# calculates annualized volatility given a series of returns and the data interval
def annualized_volatility(returns, interval):
    if returns.empty:
        return 0

    trading_days = 252

    if interval == "1d":
        periods_per_year = trading_days
    elif interval == "1h":
        periods_per_year = trading_days * 6.5
    else:
        periods_per_year = trading_days

    return returns.std() * np.sqrt(periods_per_year)


# calculates maximum drawdown given a series of closing prices
def max_drawdown(close_prices):
    running_max = close_prices.cummax()
    drawdown = (close_prices / running_max) - 1
    return drawdown.min(), drawdown

# calculates moving average given a series of closing prices and the period
def moving_average(close_prices, period):
    moving_avg = close_prices.rolling(period).mean()
    return moving_avg

# calculates Relative Strength Index (RSI) given a series of closing prices and the period (14)
def rsi(prices, period=14):
    change = prices.diff()
    gains = change.where(change > 0, 0)
    losses = -change.where(change < 0, 0)

    avg_gain = gains.rolling(period).mean()
    avg_loss = losses.rolling(period).mean()

    relative_strength = avg_gain / avg_loss

    # RSI formula
    rsi = 100 - (100 / (1 + relative_strength))

    return rsi

