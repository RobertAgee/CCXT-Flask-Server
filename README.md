# DeployReadyCCXTTradingBot

## About

This CCXT Trading Bot is pre-configured for deployment on Heroku.  You only need to provide the exchange, keys, and strategy.

## How To Deploy

1. Clone this repository to your local.

2. Add your respective exchange API keys to the config.py file.  (Note: Kucoin is used for example)

3. Create your personal webhook password in the config.py file.

4. Update config key references in the app.py file.

5. Code your trading strategy in app.py.  (Please see CCXT Manual for details.)

6. Postman Testing (Optional, but recommended)  
   <ol> Install project packages</ol>
   <ol> In terminal, enter commands: </ol>
   <ol> set FLASK_APP = app.py</ol>
   <ol> $env:FLASK_ENV = "development"</ol>
   <ol> flask run</ol>

    Now you can test your bot locally via Postman. Make sure it will communicate with your exchange and execute orders correctly, and rejects all unauthorized requests.

7. On Heroku, create a new app, and follow Heroku CLI instructions for uploading this project directly without Github.
   <b>Do not post your project to Github! It contains your secret keys.</b> Heroku will build and deploy it automatically.

8. Provide your webhook endpoint and JSON-formatted password to whatever service will be making the requests.  
   
   Tradingview Alert Example

   Webhook: https://(example-app).herokuapp.com/webhook

   Message: { "password" : "123abc" }