# robinhood_api.py
# This is a mock interface. Replace with real Robinhood API when available.
class RobinhoodAPI:
    def __init__(self):
        self.balance = 100.0
        self.positions = {}

    def get_balance(self):
        return self.balance

    def get_quote(self, symbol):
        import random
        return round(random.uniform(5, 50), 2)

    def buy(self, symbol, amount):
        price = self.get_quote(symbol)
        qty = amount / price
        self.positions[symbol] = self.positions.get(symbol, 0) + qty
        self.balance -= amount
        return {"symbol": symbol, "qty": qty, "price": price}

    def sell(self, symbol, percent=100):
        if symbol not in self.positions:
            return None
        price = self.get_quote(symbol)
        qty = self.positions[symbol] * (percent / 100)
        self.balance += price * qty
        self.positions[symbol] -= qty
        return {"symbol": symbol, "qty": qty, "price": price}
