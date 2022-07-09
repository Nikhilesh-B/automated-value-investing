import requests
import csv
from pprint import pprint

class StockDataRequester:
    def __init__(self):
        self.api_key = "Q3SYRFTE15O6BSK5"

    def format_api_key(self, function: str, symbol: str) -> str:
        url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&apikey="+self.api_key
        return url
        
    def get_fundamental_data(self, ticker: str) -> dict:
        url = self.format_api_key("OVERVIEW", ticker)
        r = requests.get(url)
        data = r.json()

        valuation_ratios = {"eps": "EPS", "forward_pe": "ForwardPE", "peg_ratio": "PEGRatio",
                            "pe_ratio": "PERatio", "dividend_per_share": "DividendPerShare"}

        for ratio in valuation_ratios:
            if valuation_ratios[ratio] != "None":
                valuation_ratios[ratio] = float(data[valuation_ratios[ratio]])
            else:
                return None

        return valuation_ratios

    def get_balance_sheet_data(self, ticker: str) -> (dict):
        url = self.format_api_key("BALANCE_SHEET", ticker)
        r = requests.get(url)
        data = r.json()
        prev_year_bs_data = data["annualReports"][0]

        balance_sheet_data = {"assets":"totalAssets",
                              "current_assets":"totalCurrentAssets",
                              "current_liabilities":"totalCurrentLiabilities",
                              "owners_equity":"totalShareholdersEquity",
                              "debt":"totalDebt"
                              }

        for stat in balance_sheet_data:
            if balance_sheet_data[stat] != None:
                balance_sheet_data[stat] = float(prev_year_bs_data[balance_sheet_data[stat]])
            else:
                return None

        liquidity = balance_sheet_data["current_assets"]/balance_sheet_data["current_liabilities"]
        debt_to_equity = balance_sheet_data["owners_equity"]/balance_sheet_data["debt"]

        balance_sheet_data["liquidity"]= liquidity
        balance_sheet_data["debt_to_equity"] = debt_to_equity

        return balance_sheet_data

    def write_data(self, filename: str, tickers: list):
        with open(filename, 'w', newline='') as csvfile:
            headers = ["Ticker", "eps", "forward_pe", "peg_ratio", "pe_ratio", "dividend_per_share"]
            csvwriter = csv.DictWriter(filename, fieldnames=headers)
            csvwriter.writeheader()
            for ticker in tickers:
                valuation_ratios = self.get_fundamental_data(ticker)
                balance_sheet_data = self.get_balance_sheet_data(ticker)

                important_data = {**valuation_ratios, **balance_sheet_data, **{"Ticker": ticker}}
                csvwriter.writeheader()

        csvfile.close()











        pass






