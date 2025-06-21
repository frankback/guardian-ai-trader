# trade_engine.py
from robinhood_api import RobinhoodAPI

class TradeEngine:
    def __init__(self, api: RobinhoodAPI):
        self.api = api
        self.watchlist = ["AAPL", "TSLA", "PLTR", "SOFI", "AMD"]

    def evaluate_and_trade(self):
        balance = self.api.get_balance()
        portion = balance / len(self.watchlist)
        for stock in self.watchlist:
            quote = self.api.get_quote(stock)
            if quote < 20:  # Buy threshold
                self.api.buy(stock, portion)
            elif quote > 30 and stock in self.api.positions:  # Sell threshold
                self.api.sell(stock, percent=100)
