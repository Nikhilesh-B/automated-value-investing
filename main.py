from StockDataRequester import StockDataRequester
from StockPricePredictor import StockPricePredictor

if __name__ == "__main__":
    requester = StockDataRequester()
    requester.get_fundamental_data("BOX")
    requester.get_balance_sheet_data("BOX")

    '''
    predictor = StockPricePredictor()
    predictor.ingest_data("NYSEstocks.csv")
    predictor.initialize_network()
    predictor.train_network()
    predictor.test_network()
    predictor.compute_mean_absolute_relative_error()
    predictor.print_mean_absolute_relative_error()
    predictor.print_undervalued_stocks()
    '''