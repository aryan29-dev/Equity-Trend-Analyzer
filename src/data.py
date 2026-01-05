import yfinance as yf
import pandas as pd

# function to fetch historical price data for a given ticker symbol
def price_data(ticker, start_date, end_date, interval):

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date) + pd.Timedelta(days=1)

    prices_df = yf.download(ticker, start=start_date, end=end_date, interval=interval, auto_adjust=True, progress=False)

    if prices_df is None or prices_df.empty:
        return None

    if "Close" not in prices_df.columns:
        return None

    return prices_df.copy()
