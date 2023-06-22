from StockPricePredictor import StockPricePredictor

if __name__ == "__main__":
    predictor = StockPricePredictor(test_size=0.15)
    predictor.ingest_data("fundamental_stock_data")
    predictor.initialize_network()
    predictor.train_network()
    predictor.test_network()
    predictor.compute_mean_absolute_relative_error()
    predictor.print_mean_absolute_relative_error()
    predictor.print_undervalued_stocks()
