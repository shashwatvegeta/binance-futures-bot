import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_TESTNET_API_KEY = os.getenv("BINANCE_TESTNET_API_KEY")
BINANCE_TESTNET_API_SECRET = os.getenv("BINANCE_TESTNET_API_SECRET")
BINANCE_TESTNET_BASE_URL = "https://testnet.binancefuture.com"

if not BINANCE_TESTNET_API_KEY or not BINANCE_TESTNET_API_SECRET:
    print("WARNING: API keys not found in environment variables. Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET in .env file.")
