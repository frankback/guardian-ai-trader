# utils.py
def format_usd(value):
    return f"${value:,.2f}"

def calculate_percent_change(old, new):
    if old == 0:
        return 0
    return round(((new - old) / old) * 100, 2)
