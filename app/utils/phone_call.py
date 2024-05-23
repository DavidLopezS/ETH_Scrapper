import logging
from twilio.rest import Client
from app.constants.indexes import ACCOUNT_SID, AUTH_TOKEN, RECIPIENT_PHONE_NUMBER, TWILIO_PHONE_NUMBER

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def call_recipient():
    try:
        call = client.calls.create(
            to=RECIPIENT_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url='http://demo.twilio.com/docs/voice.xml'
        )

        logging.info(f'Call SID: {call.sid}')
    except ValueError as ve:
        logging.error(f'ValueError occurred n "get_embedding": {ve}')
        raise ValueError(f'ValueError occurred n "get_embedding": {ve}')
    except Exception as e:
        logging.error(f'An unexpected error occurred in "get_embedding": {e}')
        raise ValueError(f"An unexpected error occurred in get embedding: {e}") 