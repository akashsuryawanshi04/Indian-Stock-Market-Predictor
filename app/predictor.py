import joblib

MODEL_PATH = 'models/random_forest_model.pkl'

FEATURE_COLUMNS = [
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


def load_model():
    return joblib.load(MODEL_PATH)


def predict_next_day(dataframe):
    model = load_model()

    latest_data = dataframe[FEATURE_COLUMNS].iloc[-1:]

    prediction = model.predict(latest_data)

    return prediction[0]
