# 📈 AI-Based Indian Stock Market Prediction & Analysis Platform

A complete end-to-end Machine Learning project that predicts next-day Indian NSE stock prices using **Random Forest Regression**, technical indicators, and interactive visualizations.

Built using **Python, Streamlit, Scikit-learn, Plotly, and yfinance**.

---

# 🚀 Project Overview

This project is an AI-powered stock market prediction system designed for Indian NSE stocks.

The platform:
- Fetches real-time NSE stock market data
- Performs technical analysis
- Trains a Random Forest Regression model
- Predicts next-day closing prices
- Generates Buy/Sell recommendations
- Displays interactive financial charts
- Provides an attractive Streamlit dashboard

This project demonstrates:
- Machine Learning workflow
- Financial data analysis
- Feature engineering
- Technical indicators
- Model evaluation
- Interactive dashboard development

---

# ✨ Features

## ✅ Real-Time NSE Stock Data
- Fetches Indian stock data using yfinance
- Supports multiple NSE stocks

## ✅ Technical Indicators
Implemented:
- SMA 10
- SMA 20
- EMA
- RSI
- Daily Returns
- Volatility

## ✅ Machine Learning Model
Uses:
- Random Forest Regression

Predicts:
- Next-day stock closing price

## ✅ Buy/Sell Recommendation
Logic:
- BUY → Predicted Price > Current Price
- SELL → Predicted Price < Current Price

## ✅ Interactive Streamlit Dashboard
Includes:
- Sidebar stock selector
- Date range selector
- Prediction cards
- Trend analysis
- Interactive charts
- Model performance metrics

## ✅ Financial Visualizations
Built with Plotly:
- Candlestick Chart
- Historical Price Graph
- Volume Chart
- SMA & EMA Graph
- Actual vs Predicted Graph

---

# 🧠 Machine Learning Workflow

## 1. Data Collection
- Download stock market data from Yahoo Finance

## 2. Data Preprocessing
- Handle missing values
- Clean dataset
- Date formatting

## 3. Feature Engineering
Generated features:
- Open
- High
- Low
- Volume
- Previous Close
- SMA
- EMA
- RSI
- Volatility

## 4. Model Training
Algorithm:
- Random Forest Regression

## 5. Model Evaluation
Metrics:
- MAE
- RMSE
- R² Score

## 6. Prediction
Predicts:
- Tomorrow's closing price

---

# 🏗️ Project Structure

```bash
indian-stock-market-predictor/
│
├── app/
│   ├── app.py
│   ├── predictor.py
│   ├── indicators.py
│   ├── utils.py
│
├── data/
│
├── models/
│
├── notebooks/
│
├── screenshots/
│
├── train_model.py
├── predict.py
├── download.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## Machine Learning
- Scikit-learn
- RandomForestRegressor

## Data Processing
- Pandas
- NumPy

## Visualization
- Plotly
- Matplotlib

## Stock Data API
- yfinance

## Model Saving
- Joblib

---

# 📊 Supported NSE Stocks

Examples:
- RELIANCE.NS
- TCS.NS
- INFY.NS
- HDFCBANK.NS
- ICICIBANK.NS
- SBIN.NS
- TATAMOTORS.NS
- WIPRO.NS
- ITC.NS

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/akashsuryawanshi04/indian-stock-market-predictor.git
```

---

## 2️⃣ Navigate to Project

```bash
cd indian-stock-market-predictor
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Download Stock Datasets

Run:

```bash
python download.py
```

Datasets will be saved inside:

```bash
data/
```

---

# 🧠 Train Machine Learning Model

Run:

```bash
python train_model.py
```

This will:
- Train Random Forest model
- Evaluate performance
- Save trained model

Saved model:

```bash
models/random_forest_model.pkl
```

---

# 🔮 Run Prediction System

```bash
python predict.py
```

Example Output:

```bash
===================================
 STOCK MARKET PREDICTION RESULT
===================================

Stock Name                : TCS.NS

Current Price Date        : 2025-05-13

Current Stock Price       : ₹3886.50

Predicted Price Date      : 2025-05-14

Predicted Tomorrow Price  : ₹3895.20

Recommendation            : BUY 📈
```

---

# 🌐 Run Streamlit Dashboard

```bash
streamlit run app/app.py
```

Open browser:

```bash
http://localhost:8501
```

---

# 📈 Dashboard Features

## Sidebar Controls
- Stock selector
- Date range selector

## Main Dashboard
- Current stock price
- Predicted price
- Buy/Sell signal
- Market trend

## Interactive Charts
- Candlestick chart
- Closing price graph
- SMA & EMA indicators
- Volume chart
- Actual vs Predicted graph

---

# 📸 Screenshots

## Dashboard

Add screenshot here:

```bash
screenshots/dashboard.png
```

---

# 📊 Model Performance Metrics

The system evaluates:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

# 🔥 Future Improvements

Future upgrades:
- LSTM Deep Learning Model
- Real-Time Live Predictions
- News Sentiment Analysis
- Portfolio Optimization
- AI Trading Assistant
- Deployment on AWS/Render
- User Authentication
- Database Integration

---

# 🎯 Resume Description

Developed an AI-powered Indian stock market prediction platform using Random Forest Regression and Streamlit. Integrated NSE stock data, technical indicators, interactive financial visualizations, and ML-based buy/sell recommendation system for real-time market analysis.

---

# 💼 Skills Demonstrated

- Machine Learning
- Financial Data Analysis
- Feature Engineering
- Technical Indicators
- Data Visualization
- Streamlit Dashboard Development
- Model Evaluation
- Python Development

---

# 📚 Learning Outcomes

This project helped in understanding:
- End-to-end ML workflow
- Financial market analysis
- Random Forest Regression
- Technical indicator calculations
- Interactive dashboard development
- Real-world ML project structuring

---

# 👨‍💻 Author

## Akash Suryawanshi

MCA Student | AI/ML Developer | Full Stack Developer

---


# 📄 License

This project is for educational and learning purposes.
