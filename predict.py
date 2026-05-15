import pandas as pd
import yfinance as yf

from app.indicators import add_technical_indicators
from app.predictor import predict_next_day

# ==========================================
# STOCK SYMBOL
# ==========================================

stock_symbol = 'TCS.NS'

# ==========================================
# DOWNLOAD STOCK DATA
# ==========================================

print("Downloading stock data...")

stock_data = yf.download(
    stock_symbol,
    start='2023-01-01',
    end='2026-05-14',
    auto_adjust=False,
    progress=False
)

# ==========================================
# FIX MULTI-INDEX COLUMNS
# ==========================================

stock_data.columns = stock_data.columns.droplevel(1)

# ==========================================
# RESET INDEX
# ==========================================

stock_data.reset_index(inplace=True)

# ==========================================
# CHECK EMPTY DATA
# ==========================================

if stock_data.empty:
    raise ValueError(
        "No stock data downloaded."
    )

# ==========================================
# ADD TECHNICAL INDICATORS
# ==========================================

stock_data = add_technical_indicators(stock_data)

# ==========================================
# REMOVE NULL VALUES
# ==========================================

stock_data.dropna(inplace=True)

# ==========================================
# PREDICT NEXT DAY PRICE
# ==========================================

predicted_price = float(
    predict_next_day(stock_data)
)

# ==========================================
# CURRENT PRICE
# ==========================================

current_price = float(
    stock_data['Close'].iloc[-1]
)

# ==========================================
# DATES
# ==========================================

current_date = stock_data['Date'].iloc[-1]

predicted_date = current_date + pd.Timedelta(days=1)

# ==========================================
# OUTPUT
# ==========================================

print("\n===================================")
print(" STOCK MARKET PREDICTION RESULT ")
print("===================================\n")

print(f"Stock Name                : {stock_symbol}")

print(f"Current Price Date        : {current_date.date()}")

print(f"Current Stock Price       : ₹{round(current_price, 2)}")

print(f"Predicted Price Date      : {predicted_date.date()}")

print(f"Predicted Tomorrow Price  : ₹{round(predicted_price, 2)}")

# ==========================================
# BUY/SELL RECOMMENDATION
# ==========================================

if predicted_price > current_price:
    print("\nRecommendation            : BUY 📈")
else:
    print("\nRecommendation            : SELL 📉")

print("\n===================================")