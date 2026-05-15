import yfinance as yf
import os

# ==========================================
# CREATE DATA DIRECTORY
# ==========================================

os.makedirs("data", exist_ok=True)

# ==========================================
# NSE STOCK SYMBOLS
# ==========================================

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS",
    "TATAMOTORS.NS",
    "WIPRO.NS",
    "HCLTECH.NS",
    "ITC.NS"
]

# ==========================================
# DOWNLOAD STOCK DATA
# ==========================================

for stock in stocks:

    print(f"\nDownloading {stock}...")

    data = yf.download(
        stock,
        start="2018-01-01",  // date from 
        end="2026-05-14", // date up to
        auto_adjust=False,
        progress=False
    )

    # Skip empty datasets
    if data.empty:
        print(f"Failed to download {stock}")
        continue

    # Fix MultiIndex columns
    data.columns = data.columns.droplevel(1)

    # Create filename
    filename = stock.replace(".NS", "").lower()

    # Save CSV
    data.to_csv(f"data/{filename}_data.csv")

    print(f"{stock} dataset saved successfully!")

print("\n===================================")
print(" ALL DATASETS DOWNLOADED ")
print("===================================")
