# main.py
from config import KILL_SWITCH, REINVESTMENT_PERCENTAGE
from robinhood_api import RobinhoodAPI
from trade_engine import TradeEngine
from reporter import send_daily_report

def run_bot():
    if KILL_SWITCH:
        return {"error": "Trading disabled via kill switch."}

    api = RobinhoodAPI()
    engine = TradeEngine(api)

    start_balance = api.get_balance()
    engine.evaluate_and_trade()
    end_balance = api.get_balance()

    send_daily_report(start_balance, end_balance)

    gain = end_balance - start_balance
    percent = round(((end_balance - start_balance) / start_balance) * 100, 2)
    return {
        "starting_balance": round(start_balance, 2),
        "ending_balance": round(end_balance, 2),
        "gain": round(gain, 2),
        "percent": percent
    }
