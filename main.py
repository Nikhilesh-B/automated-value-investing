from StockDataRequester import StockDataRequester
from StockPricePredictor import StockPricePredictor
from tickers import returnTickers

if __name__ == "__main__":
    """
    NASDAQtickers, NYSEtickers = returnTickers()


    NASDAQtickers = NASDAQtickers[:500]

    requester = StockDataRequester()
    requester.write_data("stockInformation.csv",
                         NASDAQtickers)
    """


    predictor = StockPricePredictor()
    predictor.ingest_data("stockInformation.csv")
    predictor.initialize_network()
    predictor.train_network()
    predictor.test_network()
    predictor.compute_mean_absolute_relative_error()
    predictor.print_mean_absolute_relative_error()
    predictor.print_undervalued_stocks()
