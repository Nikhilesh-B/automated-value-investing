from StockPricePredictor import StockPricePredictor


if __name__ == "__main__":
    predictor = StockPricePredictor()
    predictor.ingest_data("NYSEstocks.csv")
    predictor.initialize_network()
    predictor.train_network()
