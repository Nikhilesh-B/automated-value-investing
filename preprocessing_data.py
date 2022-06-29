import pandas as pd
import numpy as np
from sklearn.utils import shuffle


def preprocess_data(filename):
    stock_data = pd.read_csv(filename)
    stock_data = stock_data.drop(['Company'], axis=1)
    nan_value = np.nan
    stock_data = stock_data.replace("-", nan_value)
    stock_data = stock_data.replace(",", '', regex=True)
    stock_data = stock_data.dropna()
    stock_data['Debt_to_Equity'] = stock_data['Debt_to_Equity'].str.rstrip('%').astype('float') / 100.0
    stock_data['Debt_to_Assets'] = stock_data['Debt_to_Assets'].str.rstrip('%').astype('float') / 100.0
    stock_data['PEG'] = stock_data['PEG'].str.rstrip('x').astype('float')
    stock_data = shuffle(stock_data)

    return stock_data



