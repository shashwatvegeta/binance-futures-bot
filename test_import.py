try:
    from binance.error import ClientError
    print("Imported from binance.error")
except ImportError:
    print("Failed to import from binance.error")

try:
    from binance.exceptions import BinanceAPIException as ClientError
    print("Imported from binance.exceptions")
except ImportError:
    print("Failed to import from binance.exceptions")
