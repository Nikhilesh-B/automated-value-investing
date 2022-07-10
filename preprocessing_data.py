import pandas as pd
import numpy as np
from sklearn.utils import shuffle


def preprocess_data(filename):
    stock_data = pd.read_csv(filename)
    nan_value = np.nan
    stock_data = stock_data.replace("-", nan_value)
    stock_data = stock_data.dropna()
    stock_data = shuffle(stock_data)

    return stock_data