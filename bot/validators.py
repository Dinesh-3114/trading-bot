class InvalidSymbolError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class InvalidPriceError(Exception):
    pass

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price=None):
    if not symbol:
        raise InvalidSymbolError(f"Invalid symbol: {symbol}")

    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Side must be BUY or SELL, got: {side}")

    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError(f"Order type must be MARKET or LIMIT, got: {order_type}")

    if quantity <= 0:
        raise InvalidQuantityError(f"Quantity must be positive, got: {quantity}")

    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        raise InvalidPriceError("Price is required and must be positive for LIMIT orders")