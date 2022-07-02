from StockPricePredictor import StockPricePredictor


if __name__ == "__main__":
    predictor = StockPricePredictor()
    predictor.ingest_data("NYSEstocks.csv")
    predictor.initialize_network()
    predictor.train_network()
    predictor.test_network()
    predictor.compute_mean_absolute_relative_error()
    predictor.print_mean_absolute_relative_error()
    predictor.print_undervalued_stocks()