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

    # Set Params to Buy
    params = {
    'symbol': 'BTCUSDT',
    'side': 'BUY',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.003,
    'price': round(float(umFuturesClient.ticker_price("BTCUSDT")["price"]) + 10) # Setting price as ticker price plus 10 so that buy order gets filled
    }

    # Execute Buy
    buyOrderId = executeOrder(params)
    print('\n\n*** BUY Order Sent ****')
    print(f'Buy Order Id is {buyOrderId}')

    # Wait for 30 seconds
    time.sleep(30)

    # Query Order to check if it was FILLED
    print("\n\n*** Checking Buy Order Status ***")
    orderStatus = queryOrder("BTCUSDT",buyOrderId)
    print(f'*** Order status for order id {buyOrderId} is {orderStatus} ***')
    if (orderStatus == "FILLED"):
        print("*** Sell order will be send in a while ***")
    else:
        print("*** Order will be cancelled in a while ***")
        cancelOrder('BTCUSDT',buyOrderId)
        print('*** Order Cancelled ****')
        quit()

    # Wait for 30 seconds
    time.sleep(30)

    if (orderStatus == "FILLED"):
        # Set Params to Sell
        params = {
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.003,
        'price': round(float(umFuturesClient.ticker_price("BTCUSDT")["price"])-10) # Setting price as ticker price minus 10 so that buy order gets filled
        }

        # Execute Sell
        sellOrderId = executeOrder(params)
        print('\n\n*** SELL Order Sent ****')

        # Query Order to check if it was FILLED
        time.sleep(10)
        print("*** Checking Sell Order Status ***")
        orderStatus = queryOrder("BTCUSDT",sellOrderId)
        print(f'*** Order status for order id {sellOrderId} is {orderStatus} ***')

