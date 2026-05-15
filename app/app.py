import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from indicators import add_technical_indicators

st.set_page_config(
    page_title="Indian Stock Market Predictor",
    layout="wide"
)

st.title("📈 AI-Based Indian Stock Market Prediction Platform")
st.markdown("Predict Indian NSE stock prices using Random Forest Regression")

st.sidebar.header("Stock Selection")

stock_options = [
    'RELIANCE.NS',
    'TCS.NS',
    'INFY.NS',
    'HDFCBANK.NS',
    'ICICIBANK.NS',
    'SBIN.NS',
    'TATAMOTORS.NS'
]

selected_stock = st.sidebar.selectbox(
    "Choose NSE Stock",
    stock_options
)

start_date = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime('2020-01-01')
)

end_date = st.sidebar.date_input(
    "End Date",
    pd.to_datetime('today')
)

stock_data = yf.download(selected_stock, start=start_date, end=end_date)

if stock_data.empty:
    st.error("No stock data found.")
    st.stop()

stock_data.reset_index(inplace=True)

stock_data = add_technical_indicators(stock_data)

stock_data['Target'] = stock_data['Close'].shift(-1)

stock_data.dropna(inplace=True)

features = [
    'Open',
    'High',
    'Low',
    'Volume',
    'Previous_Close',
    'Daily_Return',
    'SMA_10',
    'SMA_20',
    'EMA_10',
    'RSI',
    'Volatility'
]

X = stock_data[features]
y = stock_data['Target']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

latest_features = X.iloc[-1:]

predicted_price = model.predict(latest_features)[0]

current_price = stock_data['Close'].iloc[-1]

if predicted_price > current_price:
    recommendation = "BUY"
    trend = "Bullish 📈"
else:
    recommendation = "SELL"
    trend = "Bearish 📉"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Current Price", f"₹{current_price:.2f}")

with col2:
    st.metric("Predicted Price", f"₹{predicted_price:.2f}")

with col3:
    st.metric("Market Trend", trend)

with col4:
    st.metric("Recommendation", recommendation)

st.subheader("📊 Model Performance")

metric1, metric2, metric3 = st.columns(3)

metric1.metric("MAE", round(mae, 2))
metric2.metric("RMSE", round(rmse, 2))
metric3.metric("R² Score", round(r2, 2))

st.subheader("🕯️ Candlestick Chart")

candlestick = go.Figure(data=[go.Candlestick(
    x=stock_data['Date'],
    open=stock_data['Open'],
    high=stock_data['High'],
    low=stock_data['Low'],
    close=stock_data['Close']
)])

candlestick.update_layout(
    xaxis_rangeslider_visible=False,
    height=600
)

st.plotly_chart(candlestick, use_container_width=True)

st.subheader("📈 Historical Closing Price")

close_fig = px.line(
    stock_data,
    x='Date',
    y='Close',
    title='Closing Price Trend'
)

st.plotly_chart(close_fig, use_container_width=True)

st.subheader("📉 SMA & EMA Indicators")

indicator_fig = go.Figure()

indicator_fig.add_trace(go.Scatter(
    x=stock_data['Date'],
    y=stock_data['Close'],
    name='Close Price'
))

indicator_fig.add_trace(go.Scatter(
    x=stock_data['Date'],
    y=stock_data['SMA_10'],
    name='SMA 10'
))

indicator_fig.add_trace(go.Scatter(
    x=stock_data['Date'],
    y=stock_data['SMA_20'],
    name='SMA 20'
))

indicator_fig.add_trace(go.Scatter(
    x=stock_data['Date'],
    y=stock_data['EMA_10'],
    name='EMA 10'
))

st.plotly_chart(indicator_fig, use_container_width=True)

st.subheader("🎯 Actual vs Predicted")

comparison_df = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': predictions
})

comparison_fig = go.Figure()

comparison_fig.add_trace(go.Scatter(
    y=comparison_df['Actual'],
    mode='lines',
    name='Actual'
))

comparison_fig.add_trace(go.Scatter(
    y=comparison_df['Predicted'],
    mode='lines',
    name='Predicted'
))

st.plotly_chart(comparison_fig, use_container_width=True)

st.subheader("📦 Volume Chart")

volume_fig = px.bar(
    stock_data,
    x='Date',
    y='Volume',
    title='Trading Volume'
)

st.plotly_chart(volume_fig, use_container_width=True)

st.subheader("📄 Stock Data")

st.dataframe(stock_data.tail(20))
