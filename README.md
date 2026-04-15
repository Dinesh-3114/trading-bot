# Trading Bot — Binance Futures Testnet

## Setup
1. Clone the repo: `git clone <your-repo-url>`
2. Create a virtual environment: `python -m venv venv && venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your Binance Testnet API keys

## How to Run

# Market order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

# Limit order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 50000

## Assumptions
- All orders are placed on Binance Futures Testnet (USDT-M)
- Quantity and price validation is done before hitting the API
