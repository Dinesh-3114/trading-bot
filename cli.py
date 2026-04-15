import argparse
import sys
import logging

from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.orders import place_order, print_order_summary, print_order_response

def main():
    setup_logging()

    logging.info("CLI started successfully")

    parser = argparse.ArgumentParser(description="Binance Spot Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, dest="order_type")
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", required=False, type=float)

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.order_type, args.qty, args.price)

        print_order_summary(args.symbol, args.side, args.order_type, args.qty, args.price)

        response = place_order(
            args.symbol,
            args.side,
            args.order_type,
            args.qty,
            args.price
        )

        print_order_response(response)

        sys.exit(0)

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()