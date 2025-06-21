# reporter.py
import smtplib
from email.mime.text import MIMEText
from utils import format_usd, calculate_percent_change
from config import EMAIL_CONFIG

def send_daily_report(start, end):
    gain = end - start
    percent = calculate_percent_change(start, end)
    msg = MIMEText(f"""
    Guardian AI Trader Report

    Starting Balance: {format_usd(start)}
    Ending Balance:   {format_usd(end)}
    Gain/Loss:        {format_usd(gain)} ({percent}%)
    """)

    msg["Subject"] = "Daily Trading Summary"
    msg["From"] = EMAIL_CONFIG["sender"]
    msg["To"] = EMAIL_CONFIG["receiver"]

    with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["port"]) as server:
        server.starttls()
        server.login(EMAIL_CONFIG["username"], EMAIL_CONFIG["password"])
        server.send_message(msg)
