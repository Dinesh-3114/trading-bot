import logging
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Use module-level logger (BEST PRACTICE)
logger = logging.getLogger(__name__)


class BinanceClient:
    def __init__(self):
        logger.info("Initializing Binance Spot Testnet client...")

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            logger.error("API keys not found in .env file")
            raise Exception("Missing API keys")

        # Initialize client
        self.client = Client(api_key, api_secret)

        # ✅ Set Spot Testnet URL
        self.client.API_URL = "https://testnet.binance.vision/api"

        logger.info("Binance client initialized successfully")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        # Prepare parameters
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        # Add price for LIMIT orders
        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order | {params}")

        try:
            # Place order (SPOT)
            response = self.client.create_order(**params)

            logger.info(
                f"Order success | ID={response.get('orderId')} Status={response.get('status')}"
            )

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error {e.code} | {e.message}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise