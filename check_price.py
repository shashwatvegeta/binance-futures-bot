from src.client import BinanceBotClient

client = BinanceBotClient()
price = client.client.futures_symbol_ticker(symbol="BTCUSDT")
print(f"Current BTC Price: {price['price']}")
