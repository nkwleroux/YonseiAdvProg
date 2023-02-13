from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def task(data):

    df = data[['Date', 'Close']]

    df = df.astype({"Close": int})
    df["Date"] = pd.to_datetime(df.Date, format="%m/%d/%Y")

    df.index = df['Date']

    df = df.sort_index(ascending=True, axis=0)
    new_dataFrame = pd.DataFrame(index=range(
        0, len(df)), columns=['Date', 'Close'])
    for i in range(0, len(new_dataFrame)):
        new_dataFrame['Date'][i] = df['Date'][i]
        new_dataFrame['Close'][i] = df['Close'][i]

    new_dataFrame = new_dataFrame.astype({"Close": int})
    new_dataFrame["Date"] = pd.to_datetime(new_dataFrame.Date)

    new_dataFrame.index = new_dataFrame.Date
    df_copy = new_dataFrame.copy()

    new_dataFrame.drop("Date", axis=1, inplace=True)

    final_data = new_dataFrame.values
    train_data_len = int(len(final_data) * 0.8)
    train_data = final_data[0:train_data_len, :]
    valid_data = final_data[train_data_len:, :]

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(final_data)
    x_train_data, y_train_data = [], []
    for i in range(60, len(train_data)):
        x_train_data.append(scaled_data[i-60:i, 0])
        y_train_data.append(scaled_data[i, 0])

    lstm_model = Sequential()
    lstm_model.add(LSTM(units=50, return_sequences=True,
                   input_shape=(np.shape(x_train_data)[1], 1)))
    lstm_model.add(LSTM(units=50))
    lstm_model.add(Dense(1))

    model_data = new_dataFrame[len(new_dataFrame)-len(valid_data)-60:].values
    model_data = model_data.reshape(-1, 1)
    model_data = scaler.transform(model_data)

    x_train_data, y_train_data = np.array(x_train_data), np.array(y_train_data)

    lstm_model.compile(loss='mean_squared_error', optimizer='adam')
    lstm_model.fit(x_train_data, y_train_data,
                   epochs=1, batch_size=1, verbose=2)

    X_test = []
    for i in range(60, model_data.shape[0]):
        X_test.append(model_data[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    predicted_stock_price = lstm_model.predict(X_test)
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price)

    train_data = data[:train_data_len]
    train_data.index = df_copy.Date[:train_data_len]
    valid_data = data[train_data_len:]
    valid_data['Predictions'] = predicted_stock_price
    valid_data.index = df_copy.Date[train_data_len:]

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(train_data['Close'], label='Actual data for training')
    ax.plot(valid_data['Close'], label='Actual data for validation')
    ax.plot(valid_data['Predictions'], label='Prediction')
    ax.legend()
    plt.gcf().autofmt_xdate()
    plt.suptitle('Close Price history for Samsung Electronics Co Ltd', fontsize=18)
    plt.show()


def main():
    print("Student id is:", 2022849446)

    dir_path = os.path.dirname(os.path.realpath(__file__))

    data = pd.read_csv(dir_path + '/Samsung_stock_price.csv')

    task(data)


if __name__ == "__main__":
    main()
