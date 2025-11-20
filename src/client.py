from binance.client import Client
from binance.exceptions import BinanceAPIException as ClientError
from src.config import BINANCE_TESTNET_API_KEY, BINANCE_TESTNET_API_SECRET, BINANCE_TESTNET_BASE_URL
from src.logger import logger

class BinanceBotClient:
    def __init__(self):
        try:
            self.client = Client(BINANCE_TESTNET_API_KEY, BINANCE_TESTNET_API_SECRET, testnet=True)
            self.client.API_URL = BINANCE_TESTNET_BASE_URL # Ensure testnet URL is used
            logger.info("Binance Client initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize Binance Client: {e}")
            raise

    def get_account_info(self):
        try:
            return self.client.futures_account()
        except ClientError as e:
            logger.error(f"Error fetching account info: {e}")
            return None

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market Order Placed: {order}")
            return order
        except ClientError as e:
            logger.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit Order Placed: {order}")
            return order
        except ClientError as e:
            logger.error(f"Error placing limit order: {e}")
            return None
