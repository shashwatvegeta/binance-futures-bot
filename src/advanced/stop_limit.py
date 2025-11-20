from src.client import BinanceBotClient
from src.logger import logger
from binance.exceptions import BinanceAPIException as ClientError

def place_stop_limit_order(symbol: str, side: str, quantity: float, price: float, stop_price: float):
    """
    Places a Stop-Limit order on Binance Futures.
    """
    client = BinanceBotClient()
    logger.info(f"Attempting to place STOP-LIMIT order: {side} {quantity} {symbol} at {price}, stop: {stop_price}")
    
    try:
        order = client.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP',
            timeInForce='GTC',
            quantity=quantity,
            price=price,
            stopPrice=stop_price
        )
        logger.info(f"Stop-Limit Order Placed: {order}")
        print(f"Order Placed: {order}")
        return order
    except ClientError as e:
        logger.error(f"Error placing stop-limit order: {e}")
        print("Failed to place order. Check logs for details.")
        return None
