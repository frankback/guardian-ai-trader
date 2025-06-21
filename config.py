# config.py
KILL_SWITCH = False  # Set to True to pause all trading
REINVESTMENT_PERCENTAGE = 100  # Can be adjusted via dashboard
EMAIL_CONFIG = {
    "sender": "your_email@example.com",
    "receiver": "receiver_email@example.com",
    "smtp_server": "smtp.example.com",
    "port": 587,
    "username": "your_email@example.com",
    "password": "your_password"  # Use environment variable or secrets manager ideally
}
