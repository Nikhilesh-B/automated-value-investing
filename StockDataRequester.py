import requests
import csv
from api_key import API_key
import time


class StockDataRequester:
    def __init__(self):
        self.api_key = API_key

    def format_api_key(self, function: str, symbol: str) -> str:
        url = "https://www.alphavantage.co/query?function=" + function + "&symbol=" + symbol + "&apikey=" + self.api_key
        return url

    def get_fundamental_data(self, ticker: str) -> dict:
        url = self.format_api_key("OVERVIEW", ticker)
        try:
            r = requests.get(url)
            data = r.json()

            valuation_ratios = {"eps": "EPS", "forward_pe": "ForwardPE", "peg_ratio": "PEGRatio",
                                "pe_ratio": "PERatio", "dividend_per_share": "DividendPerShare"}

            for ratio in valuation_ratios:
                if valuation_ratios[ratio] != "None":
                    try:
                        valuation_ratios[ratio] = float(data[valuation_ratios[ratio]])

                    except (KeyError, ValueError):
                        return {}
                else:
                    return {}
        except (requests.exceptions.ConnectionError,requests.exceptions.JSONDecodeError):
            return {}

        return valuation_ratios

    def get_price_data(self, ticker: str) -> dict:
        url = self.format_api_key("GLOBAL_QUOTE", ticker)
        try:
            r = requests.get(url)
            data = r.json()
            try:
                pricing_data = data['Global Quote']

                try:
                    price = pricing_data['05. price']

                    if price == "None":
                        return {}

                    else:
                        pricing_data = {"price": float(price)}
                        return pricing_data

                except KeyError:
                    return {}

            except KeyError:
                return {}
        except (requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError):
            return {}

    def get_balance_sheet_data(self, ticker: str) -> dict:
        url = self.format_api_key("BALANCE_SHEET", ticker)
        try:
            r = requests.get(url)
            data = r.json()
            try:
                prev_year_bs_data = data["quarterlyReports"][0]

                balance_sheet_data = {"assets": "totalAssets",
                                      "current_assets": "totalCurrentAssets",
                                      "current_liabilities": "totalCurrentLiabilities",
                                      "owners_equity": "totalShareholderEquity",
                                      "debt": "totalLiabilities"}

                for stat in balance_sheet_data:
                    if balance_sheet_data[stat] is not None:
                        try:
                            balance_sheet_data[stat] = float(prev_year_bs_data[balance_sheet_data[stat]])

                        except ValueError:
                            return {}
                    else:
                        return {}

                try:
                    liquidity = balance_sheet_data["current_assets"] / balance_sheet_data["current_liabilities"]
                    debt_to_equity = balance_sheet_data["owners_equity"] / balance_sheet_data["debt"]

                    balance_sheet_data["liquidity"] = liquidity
                    balance_sheet_data["debt_to_equity"] = debt_to_equity

                except ZeroDivisionError:
                    return {}

                return balance_sheet_data

            except (KeyError, IndexError):
                return {}

        except (requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError):
            return {}

    def write_data(self, filename: str, tickers: list):
        with open(filename, 'w', newline='') as csvfile:
            headers = ["Ticker", "eps", "forward_pe", "peg_ratio", "pe_ratio", "dividend_per_share", "liquidity",
                       "debt_to_equity", "price"]
            csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
            csvwriter.writeheader()
            for ticker in tickers:
                valuation_ratios = self.get_fundamental_data(ticker)
                balance_sheet_data = self.get_balance_sheet_data(ticker)
                pricing_data = self.get_price_data(ticker)
                print(pricing_data, balance_sheet_data, valuation_ratios)
                if balance_sheet_data and valuation_ratios and pricing_data:
                    important_data = {**valuation_ratios, **balance_sheet_data, **{"Ticker": ticker}, **pricing_data}
                    important_data = {k: important_data[k] for k in important_data if k in headers}
                    csvwriter.writerow(important_data)

        csvfile.close()
