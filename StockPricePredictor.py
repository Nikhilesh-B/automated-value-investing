from preprocessing_data import preprocess_data
import tensorflow as tf
from tensorflow import keras
from keras import layers
from sklearn.model_selection import train_test_split


'''In an ideal software engineering project you would want 
    this object to ingest values and work with them in here.'''


class StockPricePredictor:
    def __init__(self):
        self.model = None
        self.data = None
        self.training_data = None
        self.testing_data = None
        self.label_training_data =None
        self.label_test_data = None

    def ingest_data(self, file_name):
        stock_data = preprocess_data(file_name)
        stock_train_data, stock_test_data = train_test_split(stock_data, test_size=0.1)
        self.label_training_data = stock_train_data['Ticker']
        self.label_test_data = stock_test_data['Ticker']
        self.training_data = stock_train_data.drop(columns=['Ticker'])
        self.testing_data = stock_test_data.drop(columns=['Ticker'])

        self.training_data = self.training_data.astype(float)
        self.testing_data = self.testing_data.astype(float)

    def initialize_model(self):
        input_len = len(self.training_data.iloc[[0]])
        self.model = keras.Sequential([
            layers.Dense(input_len, activation="relu", name="layer1"),
            layers.Dense(input_len*2, activation="relu", name="layer2"),
            layers.Dense(input_len, activation="relu", name="layer3"),
            layers.Dense(1, name="output")
        ])

    '''Now you would want to insert the training data into the model 
        and check to see the output. We need to then pass this dataPoint to the model '''

    def train_model(self):
        for index, row in enumerate(self.training_data.to_numpy()):
            print("index=", index)
            dataPoint = tf.convert_to_tensor(row)
            print("datapoint=", dataPoint)













