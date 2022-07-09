import requests


class StockDataRequester:
    def __init__(self):
        self.api_key = "Q3SYRFTE15O6BSK5"

    def format_api_key(self, function: str, symbol: str) -> str:
        url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&apikey="+self.api_key
        return url
        
    def get_stock_data(self, ticker: str):
        url = self.format_api_key("OVERVIEW", ticker)
        r = requests.get(url)
        print(r)


    