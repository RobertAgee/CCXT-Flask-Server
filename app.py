import ccxt as ccxt
from flask import Flask, Response, request

import config

app = Flask(__name__)
exchange = ccxt.kucoin({
    'adjustForTimeDifference': True,
    'apiKey': config.kucoin_api_key,
    'secret': config.kucoin_api_secret,
    'password': config.kucoin_api_password,
})
# exchange = ccxt.kucoinfutures({
#     'adjustForTimeDifference': True,
#     'apiKey': config.kucoinfutures_api_key,
#     'secret': config.kucoinfutures_api_secret,
#     'password': config.kucoinfutures_api_password
# })
exchange.load_markets()


@app.route('/webhook', methods=['POST'])
def respond():
    letter = request.get_json()
    name = letter.get('password', '')
    if name != config.webhook_password:
        return Response(status=406)
    else:
        # Example balance query and order creation
        #
        # currency = exchange.currency('USDT')
        # balance = float(str(exchange.fetch_balance({'currency': currency['id']})['USDT']['total']))
        # last = float(str(exchange.fetch_ticker('ETH/USDT')['last']))
        # symbol = 'ETH/USDT'
        # amount = 0.02*balance
        # price = last
        # type = 'market'
        # side = 'buy'
        # params = {"reduce_only": True}
        # order = exchange.create_order(symbol, type, side, amount, price, params)
        return Response(response=order, status=200)
