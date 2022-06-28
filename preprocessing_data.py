import pandas as pd


def preprocess_data(filename):
    data_frame = pd.read_csv(filename)
    return data_frame



