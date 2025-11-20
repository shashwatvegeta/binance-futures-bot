# Binance Futures Trading Bot

A CLI-based trading bot for Binance USDT-M Futures Testnet. This bot supports Market, Limit, and Stop-Limit orders with robust logging and error handling.

## 🚀 Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
1. Rename `.env.example` to `.env`:
   - Windows: `ren .env.example .env`
   - Mac/Linux: `mv .env.example .env`
2. Open `.env` and paste your Binance Testnet API keys:
   ```ini
   BINANCE_TESTNET_API_KEY=your_actual_api_key_here
   BINANCE_TESTNET_API_SECRET=your_actual_secret_key_here
   ```
   *(Get keys from [testnet.binancefuture.com](https://testnet.binancefuture.com))*

## 💻 Usage Commands

Run the bot using `run.py`.

### Market Order
Buy or Sell immediately at the best available price.
```bash
# Buy 0.002 BTC
python run.py market BTCUSDT BUY 0.002
```

### Limit Order
Buy or Sell at a specific price.
```bash
# Sell 0.002 BTC at $95,000
python run.py limit BTCUSDT SELL 0.002 95000
```

### Stop-Limit Order (Advanced)
Trigger a limit order when the price hits a stop level.
```bash
# Sell 0.002 BTC if price drops to $86,000 (Limit price: $85,900)
python run.py stop-limit BTCUSDT SELL 0.002 85900 86000
```
**Note**: For a SELL Stop-Limit (Stop Loss), the Stop Price must be **BELOW** the current market price.

## 📂 Project Structure
- `src/`: Source code for the bot.
- `src/advanced/`: Advanced order logic (Stop-Limit).
- `bot.log`: Records all API requests, errors, and successful orders.
- `run.py`: Entry point script.

## 📝 Troubleshooting
- **"Order's notional must be no smaller than 100"**: Increase your quantity (e.g., use 0.002 BTC instead of 0.001).
- **"Order would immediately trigger"**: Check your Stop Price. For SELL, it must be lower than current price. For BUY, it must be higher.
