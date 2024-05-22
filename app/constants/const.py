import os

ACCOUNT_SID = os.environ.get('TWILIO_SID_ACCOUNT')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE')
RECIPIENT_PHONE_NUMBER = os.environ.get('TONI_PHONE')
URL = os.environ.get('ETHERSCAN_URL')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
TRANSACTION_FILE = "transaction.txt"