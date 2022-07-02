from preprocessing_data import preprocess_data
import tensorflow as tf
from tensorflow import keras
from keras import layers
from sklearn.model_selection import train_test_split

'''In an ideal software engineering project you would want 
    this object to ingest values and work with them in here.'''


class StockPricePredictor:
    def __init__(self):
        self.network = None
        self.data = None
        self.training_data = None
        self.testing_data = None
        self.training_data_tickers = None
        self.testing_data_tickers = None
        self.training_data_prices = None
        self.testing_data_prices = None
        self.optimizer = None

    def ingest_data(self, file_name):
        stock_data = preprocess_data(file_name)
        stock_train_data, stock_test_data = train_test_split(stock_data, test_size=0.1)
        self.training_data_tickers = stock_train_data['Ticker']
        self.testing_data_tickers = stock_test_data['Ticker']
        self.training_data_prices = stock_train_data['Price']
        self.testing_data_prices = stock_test_data['Price']
        self.training_data = stock_train_data.drop(columns=['Ticker','Price'])
        self.testing_data = stock_test_data.drop(columns=['Ticker','Price'])

        self.training_data = self.training_data.astype(float)
        self.training_data_prices = self.training_data_prices.astype(float)
        self.testing_data = self.testing_data.astype(float)
        self.testing_data_prices = self.testing_data_prices.astype(float)

        self.training_data_prices = self.training_data_prices.to_numpy()
        self.training_data = self.training_data.to_numpy()

        self.testing_data_prices = self.testing_data_prices.to_numpy()
        self.testing_data = self.testing_data.to_numpy()

    def initialize_network(self):
        input_len = len(self.training_data[0])
        self.network = keras.Sequential([
            layers.Dense(input_len, activation="relu", name="layer1"),
            layers.Dense(input_len*2, activation="relu", name="layer2"),
            layers.Dense(input_len, activation="relu", name="layer3"),
            layers.Dense(1, name="output")
        ])
        self.optimizer = tf.keras.optimizers.Adagrad(learning_rate=0.01)

    def train_network(self):
        for index, row in enumerate(self.training_data):
            ticker_data = tf.convert_to_tensor(row)
            ticker_data = tf.reshape(ticker_data, [1, len(ticker_data)])

            with tf.GradientTape() as tape:
                predicted_price = self.network(ticker_data)
                actual_price = self.training_data_prices[index]

                price_difference = actual_price-predicted_price
                loss = tf.math.pow(price_difference, tf.constant([4.0]))

            grads = tape.gradient(loss, self.network.trainable_variables)
            self.optimizer.apply_gradients(zip(grads, self.network.trainable_variables))