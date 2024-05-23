import os, requests, logging 
from bs4 import BeautifulSoup
from app.utils.file_manager import open_file, save_file
from app.utils.phone_call import call_toni
from app.constants.indexes import URL, HEADERS, TRANSACTION_FILE

def fetch_and_process_data():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        transaction_elements = soup.select('#transactions > div > div.table-responsive > table > tbody > tr > td:nth-child(2) > div > a')

        transactions = [item.get_text(strip=True) for item in transaction_elements]

        last_transaction = transactions[0] if transactions else None

        print(f'Last Transaction: {last_transaction}')

        if not os.path.exists(TRANSACTION_FILE):
            save_file(TRANSACTION_FILE, last_transaction)
        else:
            current_transaction = open_file(TRANSACTION_FILE)
            if last_transaction != current_transaction:
                call_toni()
                save_file(TRANSACTION_FILE, last_transaction)
    except ValueError as ve:
        logging.error(f'ValueError occurred n "get_embedding": {ve}')
        raise ValueError(f'ValueError occurred n "get_embedding": {ve}')
    except Exception as e:
        logging.error(f'An unexpected error occurred in "get_embedding": {e}')
        raise ValueError(f"An unexpected error occurred in get embedding: {e}") 


