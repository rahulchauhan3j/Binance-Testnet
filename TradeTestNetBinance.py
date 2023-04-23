# This script uses Binance APIs to trade BTCUSDT on Binance TestNet
# Market Orders to Buy and Sell fixed quantity of BTCUSDT are sent every 10second
import time
import json
from binance.cm_futures import CMFutures  # uses https://dapi.binance.com
from binance.um_futures import UMFutures  # uses https://fapi.binance.com 


# TestNet URL for Binance
def getTestBaseURL():
    return 'https://testnet.binancefuture.com'

# Fetch api and secret
def fetchAPIAndSecret():
    apiFile = open('APIData.json')
    apiData = json.load(apiFile)
    return (apiData["key"],apiData["secret"])


# initiate client
def initiateClient(base_url,key,data):
    return UMFutures(key=key, secret=secret,base_url=base_url)

# execute order
def executeOrder(params):
    response = umFuturesClient.new_order(**params)
    return response["orderId"]

# query order
def queryOrder(symbol,orderId):
    order = umFuturesClient.query_order(symbol=symbol,orderId=orderId)
    return order["status"]

# cancel order
def cancelOrder(symbol,orderId):
    umFuturesClient.cancel_order(symbol=symbol,orderId=orderId)


if __name__ == "__main__":
    # Initialize Base URL
    base_url = getTestBaseURL()

    # Get API Data Key and Secret
    (key,secret) = fetchAPIAndSecret()
    
    # Initiate Client
    umFuturesClient = initiateClient(base_url,key,secret)

    for i in range(40):  # Repeat 40 times
        # Set Params to Buy
        params = {
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'MARKET',
        'quantity': 0.003
        }

        # Execute Buy
        buyOrderId = executeOrder(params)
        print('\n\n*** BUY Order Sent ****')
        print(f'Buy Order Id is {buyOrderId}')

        # Wait for 10 seconds before next order
        time.sleep(10)


        # Set Params to Sell
        params = {
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'MARKET',
        'quantity': 0.003
        }

        # Execute Sell
        sellOrderId = executeOrder(params)
        print('\n\n*** SELL Order Sent ****')
        
                # Wait for 10 seconds before next order
        time.sleep(10)
    

