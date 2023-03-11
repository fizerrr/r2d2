import pandas as pd
import yfinance as yf

# Set the stock symbol and time interval
symbol = "AAPL"
interval = "1d"

# Download the data from Yahoo Finance
data = yf.download(symbol, interval=interval, period="10y")

# Save the data to a CSV file
data.to_csv("AAPL_1min_last_5_years.csv")