from StockDataRequester import StockDataRequester
import random, csv


def return_tickers():
    nasdaq_tickers = []
    nyse_tickers = []

    with open('NASDAQ_ticker_names.csv') as nasdaq_file:
        csv_reader = csv.reader(nasdaq_file, delimiter=",")
        for row in csv_reader:
            nasdaq_tickers.append(row[0])

    nasdaq_file.close()

    with open('NYSE_ticker_names.csv') as nyse_file:
        csv_reader = csv.reader(nyse_file, delimiter=",")

        for row in csv_reader:
            nyse_tickers.append(row[0])

    nyse_file.close()

    return nasdaq_tickers, nyse_tickers


if __name__ == '__main__':
    print("Hello")
    nasdaq_tickers, nyse_tickers = return_tickers()
    tickers = set(nasdaq_tickers + nyse_tickers)
    tickers = list(tickers)
    random.shuffle(tickers)
    requester = StockDataRequester()
    requester.write_data("fundamental_stock_data", tickers)
    print("done")
