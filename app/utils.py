import yfinance as yf
import pandas as pd


def fetch_stock_data(stock_symbol, start_date, end_date):
    try:
        data = yf.download(stock_symbol, start=start_date, end=end_date)

        if data.empty:
            raise ValueError("No stock data found.")

        data.reset_index(inplace=True)

        return data

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return pd.DataFrame()
