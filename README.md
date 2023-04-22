# Binance Trading API Use

## Background

Purpose of this repository is to demonstrate use of Binance API to buy and sell BTCUSDT futures on Binance Testnet.

I am sending a buy order, waiting 10 secs..After 10 secs checking if buy order by filled , if it is filled I am sending a sell order, if buy order was not filled, I am cancelling it and after 10 secs sending a new buy order..

For sell orders, I am waiting for them to be filled and once they get filled (which may take time depending on my price) , I am sending next buy order after 10 secs..

To use this program create an account in Binance and obtain API Key and API Secret for Binance Testnet.

Populate API Key and API Secret in APIData.json.

And then run TradeTestNetBinance.py. The program creates a buy order and after 1 minute executes a sell order.

DO NOT USE THIS PROGRAM IN PRODUCTION. THIS PROGRAM IS FOR EDUCATIONAL PURPOSES ONLY..
