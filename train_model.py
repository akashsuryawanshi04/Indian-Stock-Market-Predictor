import pandas as pd
import numpy as np
import yfinance as yf
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from app.indicators import add_technical_indicators

# ==========================================
# STOCK SYMBOL
# ==========================================

STOCK_SYMBOL = "TCS.NS"

# ==========================================
# DOWNLOAD STOCK DATA
# ==========================================

print("Downloading stock data...")

stock_data = yf.download(
    STOCK_SYMBOL,
    start="2018-01-01",
    end="2026-05-14",
    auto_adjust=False,
    progress=False
)

# ==========================================
# CHECK EMPTY DATA
# ==========================================

if stock_data.empty:
    raise ValueError("No stock data downloaded.")

# ==========================================
# FIX MULTI-INDEX COLUMNS
# ==========================================

stock_data.columns = stock_data.columns.droplevel(1)

# ==========================================
# RESET INDEX
# ==========================================

stock_data.reset_index(inplace=True)

# ==========================================
# ADD TECHNICAL INDICATORS
# ==========================================

stock_data = add_technical_indicators(stock_data)

# ==========================================
# TARGET COLUMN
# ==========================================

stock_data["Target"] = stock_data["Close"].shift(-1)

# ==========================================
# REMOVE NULL VALUES
# ==========================================

stock_data.dropna(inplace=True)

# ==========================================
# FEATURES
# ==========================================

features = [
    "Open",
    "High",
    "Low",
    "Volume",
    "Previous_Close",
    "Daily_Return",
    "SMA_10",
    "SMA_20",
    "EMA_10",
    "RSI",
    "Volatility"
]

X = stock_data[features]

y = stock_data["Target"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# RANDOM FOREST MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

print("Training model...")

model.fit(X_train, y_train)

# ==========================================
# PREDICTIONS
# ==========================================

predictions = model.predict(X_test)

# ==========================================
# MODEL EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, predictions)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

r2 = r2_score(y_test, predictions)

print("\n===================================")
print(" MODEL PERFORMANCE ")
print("===================================\n")

print(f"MAE Score   : {mae:.2f}")

print(f"RMSE Score  : {rmse:.2f}")

print(f"R2 Score    : {r2:.4f}")

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(model, "models/random_forest_model.pkl")

print("\nModel saved successfully!")

print("\n===================================")