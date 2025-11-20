from src.client import BinanceBotClient
from src.logger import logger

def place_market_order(symbol: str, side: str, quantity: float):
    """
    Places a market order on Binance Futures.
    """
    client = BinanceBotClient()
    logger.info(f"Attempting to place MARKET order: {side} {quantity} {symbol}")
    
    response = client.place_market_order(symbol, side, quantity)
    
    if response:
        logger.info(f"Market order placed successfully: {response['orderId']}")
        print(f"Order Placed: {response}")
    else:
        logger.error("Failed to place market order.")
        print("Failed to place order. Check logs for details.")
