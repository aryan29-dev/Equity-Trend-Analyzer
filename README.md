# Equity Trend Analyzer

Interactive equity analysis dashboard that uses historical market data to evaluate price trends, risk, return, momentum, and technical indicators for a selected stock.

The application combines linear regression, moving averages, risk metrics, and optional RSI analysis in a Streamlit dashboard with downloadable market data.

## Features

- **Historical market data:** Retrieves daily or hourly price history for a selected ticker using `yfinance`.

- **Risk and return metrics:** Calculates total return, annualized volatility, and maximum drawdown.

- **Trend analysis:** Uses linear regression to estimate price direction, returning the slope and R² value as a measure of trend strength.

- **Trend classification:** Categorizes the resulting trend as Uptrend, Downtrend, or No Clear Trend.

- **Moving-average signals:** Compares short- and long-term moving averages to provide an additional view of price momentum.

- **RSI analysis:** Optionally calculates the 14-period Relative Strength Index (RSI) with 70 and 30 reference levels.

- **Interactive visualizations:** Displays price history, moving averages, regression trendline, and optional RSI charts.

- **Data inspection:** Provides a preview of the underlying historical dataset used in the analysis.

- **CSV export:** Allows users to download the complete analyzed dataset.

## Metrics

| Metric | What It Measures |
| --- | --- |
| Total Return | Cumulative return over the selected period |
| Annualized Volatility | Annualized variability of historical returns |
| Maximum Drawdown | Largest peak-to-trough decline |
| Regression Slope | Direction and magnitude of the fitted price trend |
| R² | Strength of the linear regression fit |
| RSI (14) | Momentum indicator based on recent price movements |

## Trend Analysis

The application fits a linear regression model to historical price data and uses the resulting slope to evaluate the direction of the trend.

The R² value provides additional context by showing how closely the observed price movement follows the fitted linear trend. Together, these measures are used to classify the stock as:

- **Uptrend**
- **Downtrend**
- **No Clear Trend**

Moving-average signals and RSI can then provide additional context alongside the regression-based trend analysis.

## Tech Stack

| Area | Technology |
| --- | --- |
| Language | Python |
| Application | Streamlit |
| Market Data | yfinance |
| Data Processing | pandas |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |

## Project Structure

```text
equity-trend-analyzer/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── src/
    ├── data.py
    ├── key_metrics.py
    ├── trends.py
    └── graphs.py
```