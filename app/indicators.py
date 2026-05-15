import pandas as pd
import numpy as np


def calculate_rsi(data, window=14):
    delta = data['Close'].diff()

    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def add_technical_indicators(df):
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()

    df['Daily_Return'] = df['Close'].pct_change()

    df['Volatility'] = df['Daily_Return'].rolling(window=10).std()

    df['RSI'] = calculate_rsi(df)

    df['Previous_Close'] = df['Close'].shift(1)

    return df
