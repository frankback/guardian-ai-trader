# Guardian AI Trader

## Features
- 100% Autonomous trading bot (mock Robinhood API included)
- Kill switch for emergency stop
- Reinvestment slider via dashboard
- End-of-day email report
- Live growth chart
- Dark mode dashboard

## Setup
1. Install Python packages:
```bash
pip install streamlit matplotlib
```

2. Run the bot:
```bash
python main.py
```

3. Run the dashboard:
```bash
streamlit run dashboard.py
```

4. Configure `config.py` for your email settings.

> Replace `robinhood_api.py` with real Robinhood integration when ready.
