from twilio.rest import Client
from app.constants.const import ACCOUNT_SID, AUTH_TOKEN, RECIPIENT_PHONE_NUMBER, TWILIO_PHONE_NUMBER

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def call_toni():
    call = client.calls.create(
        to=RECIPIENT_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        url='http://demo.twilio.com/docs/voice.xml'
    )

    print(f'Call SID: {call.sid}')