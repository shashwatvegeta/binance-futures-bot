# Binance Bot Project Report

## Analysis
This project implements a CLI-based trading bot for Binance Futures Testnet.
It uses the `python-binance` library for API interactions and `typer` for the CLI interface.

### Architecture
- **`src/client.py`**: Wraps the Binance `Client` to handle authentication and error logging.
- **`src/market_orders.py` & `src/limit_orders.py`**: specific logic for order types.
- **`src/advanced/stop_limit.py`**: Logic for Stop-Limit orders.
- **`src/main.py`**: Entry point for the CLI, handling argument parsing and validation.

### Features
- **Market Orders**: Buy/Sell at current market price.
- **Limit Orders**: Buy/Sell at a specified price.
- **Stop-Limit Orders**: Advanced order type for risk management.
- **Logging**: All actions are logged to `bot.log`.
- **Input Validation**: Prevents invalid orders (negative quantities, invalid sides).

## Usage
1. Configure `.env` with API keys.
2. Run `python -m src.main --help` to see available commands.
3. Example: `python -m src.main market BTCUSDT BUY 0.001`

## Screenshots
*(Place screenshots of your bot running here)*
