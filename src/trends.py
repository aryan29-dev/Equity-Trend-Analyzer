import numpy as np

# performs linear regression on log prices to determine slope and R^2
def regression_trend(close_prices):
    
    log_prices = np.log(close_prices.dropna().values)
    time = np.arange(len(log_prices))

    if len(log_prices) < 5:
        return 0, 0

    time_avg = time.mean()
    prices_avg = log_prices.mean()
    
    if ((time - time_avg) ** 2).sum() == 0:
        return 0, 0

    slope = (((time - time_avg) * (log_prices - prices_avg)).sum()) / (((time - time_avg) ** 2).sum())
    y_intercept = prices_avg - slope * time_avg

    trend_line = slope * time + y_intercept

    error = ((log_prices - trend_line) ** 2).sum()
    total = ((log_prices - prices_avg) ** 2).sum()

    r_squared = 0 if total == 0 else 1 - (error / total)

    return slope, r_squared

# determines type of trend based on slope and R^2 value
def type_of_trend(slope, r_squared):
    if r_squared < 0.25:
        return "No Clear Trend"
    if slope > 0:
        return "Uptrend"
    if slope < 0:
        return "Downtrend"
    return "Flat"

# determines moving average crossover signals
# Source: https://www.investopedia.com/terms/m/movingaverage.asp
def momentum_signal(short_ma, long_ma, short_period, long_period):
    short_ma = short_ma.squeeze().dropna()
    long_ma = long_ma.squeeze().dropna()

    if short_ma.empty or long_ma.empty:
        return "N/A"

    short_last = float(short_ma.iloc[-1])
    long_last = float(long_ma.iloc[-1])

    if short_last > long_last:
        return f"{short_period}D MA above {long_period}D MA (Above long-term average)"
    elif short_last < long_last:
        return f"{short_period}D MA below {long_period}D MA (Below long-term average)"
    else:
        return "MAs equal"

