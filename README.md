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
   
   ```
   set FLASK_APP = app.py
   
   $env:FLASK_ENV = "development"
   
   flask run
   ```

    Now you can test your bot locally via Postman. Make sure it will communicate with your exchange and execute orders correctly, and rejects any unauthorized requests.

7. On Heroku, create a new app, and follow Heroku instructions for either uploading directly from your local or for a Github repo.  <b>NOTE: Since this contains your account keys, if you upload to Github, make sure it is set to private.</b> Heroku will build and deploy it automatically.  If there are any build errors, make sure all the packages versions agree with Heroku's Python environment.

8. Provide your webhook endpoint and JSON-formatted password to whatever service will be making the requests.  
   
   Tradingview Alert Example

   Webhook: https://(example-app).herokuapp.com/webhook

   Message: { "password" : "123abc" }
