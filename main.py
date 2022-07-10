from StockDataRequester import StockDataRequester
from StockPricePredictor import StockPricePredictor
from tickers import returnTickers

if __name__ == "__main__":

    requester = StockDataRequester()
    requester.get_price_data("IBM")

    '''
    predictor = StockPricePredictor()
    predictor.ingest_data("stockInformation.csv")
    predictor.initialize_network()
    predictor.train_network()
    predictor.test_network()
    predictor.compute_mean_absolute_relative_error()
    predictor.print_mean_absolute_relative_error()
    predictor.print_undervalued_stocks()
    '''