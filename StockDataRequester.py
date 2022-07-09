import requests
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
        #EPS, ForwardPE, PEGRatio, PERatio, DividendPerShare

        valuation_ratios = {"eps": "EPS", "forward_pe": "ForwardPE", "peg_ratio": "PEGRatio",
                            "pe_ratio": "PERatio", "dividend_per_share": "DividendPerShare"}

        for ratio in valuation_ratios:
            if valuation_ratios[ratio] != "None":
                valuation_ratios[ratio] = float(data[valuation_ratios[ratio]])
            else:
                valuation_ratios = None
                break

        return valuation_ratios

    def get_balance_sheet_data(self, ticker: str) -> (dict):
        #In annual reports, fictionary one of a list of dicitonaries
        #totalAssets,totalCurrentAssets, totalCurrentLiabilities,cashAndCashEquivalentsAtCarryingValue,totalShareholdersEquity
        url = self.format_api_key("BALANCE_SHEET", ticker)
        r = requests.get(url)
        data = r.json()

        prev_year_bs_data = data["annualReports"][0]

        assets = prev_year_bs_data["totalAssets"]
        current_assets = prev_year_bs_data["totalCurrentAssets"]
        current_liabilities = prev_year_bs_data["totalCurrentLiabilities"]
        owners_equity = prev_year_bs_data["totalShareholdersEquity"]

        assets, current_assets, current_liabilities, owners_equity = \
            float(assets), float(current_assets), float(current_liabilities), float(owners_equity)

        liquidity= current_assets/current_liabilities
        debt_to_equity = current_liabilities/owners_equity

        financial_ratios = {"liquidity_ratio":liquidity,
                            "debt_to_equity":debt_to_equity}

        return financial_ratios




        pprint(data)

