import pandas as pd
import yfinance as yf

# Set the stock symbol and time interval
symbol = "AAPL"
interval = "1m"

# Download the data from Yahoo Finance
data = yf.download(symbol, interval=interval, period="7d")

# Save the data to a CSV file
data.to_csv("data/AAPL_1min_last_7_days.csv")