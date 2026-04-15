import logging
from bot.client import BinanceClient

logger = logging.getLogger(__name__)

def place_order(symbol, side, order_type, quantity, price=None):
    client = BinanceClient()
    return client.place_order(symbol, side, order_type, quantity, price)

def print_order_summary(symbol, side, order_type, quantity, price):
    print("\n--- Order Request ---")
    print(f"  Symbol    : {symbol}")
    print(f"  Side      : {side}")
    print(f"  Type      : {order_type}")
    print(f"  Quantity  : {quantity}")
    if price:
        print(f"  Price     : {price}")

def print_order_response(response):
    print("\n--- Order Response ---")
    print(f"  Order ID     : {response.get('orderId')}")
    print(f"  Status       : {response.get('status')}")
    print(f"  Executed Qty : {response.get('executedQty')}")
    print(f"  Price        : {response.get('price')}")
    print("\n✅ Order placed successfully!\n")