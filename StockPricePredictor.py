from preprocessing_data import preprocess_data
import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np


class StockPricePredictor:
    def __init__(self):
        self.model = keras.Sequential([
            layers.Dense(1, activation="relu", name="layer1"),
            layers.Dense(1, activation="relu", name="layer2"),
            layers.Dense(1, activation="relu", name="layer3"),
            layers.Dense(1, name="output")
        ])
        self.data = None
        self.training_data = None
        self.test_data = None

    @staticmethod
    def ingest_data(file_name):
        stock_data = preprocess_data(file_name)
        stock_data = stock_data.drop(['Company'], axis=1)

        nan_value = np.nan
        print(stock_data)
        stock_data = stock_data.replace("-", nan_value, inplace=True)
        print(stock_data)
        stock_data = stock_data.dropna(inplace=True)


        print(stock_data)