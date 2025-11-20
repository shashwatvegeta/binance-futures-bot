from src.client import BinanceBotClient
from src.logger import logger

def place_limit_order(symbol: str, side: str, quantity: float, price: float):
    """
    Places a limit order on Binance Futures.
    """
    client = BinanceBotClient()
    logger.info(f"Attempting to place LIMIT order: {side} {quantity} {symbol} at {price}")
    
    response = client.place_limit_order(symbol, side, quantity, price)
    
    if response:
        logger.info(f"Limit order placed successfully: {response['orderId']}")
        print(f"Order Placed: {response}")
    else:
        logger.error("Failed to place limit order.")
        print("Failed to place order. Check logs for details.")
