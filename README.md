# Scrapper_test

In order to run this application for the first time you have to run `make fisrt` in the terminal, once that has been done you can always run it with `make start`. Keep in mind to have docker opened when doing it.

Also, in order to properly run it you'll have to provide the environment variables in the `.env` file. Where `TWILIO_SID_ACCOUNT`, `TWILIO_AUTH_TOKEN` and `TWILIO_PHONE` should be retrieved from Twilio API. `RECIPIENT_PHONE_NUMBER` should be provided by the user and `ETHERSCAN_URL` should be fetched from etherscan page, an example of a valid URL would be the following: `https://etherscan.io/address/0xbc7cDa2fe846bdfFDE69a63A81c7b8ec352E3b24` 
