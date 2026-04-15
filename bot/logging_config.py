import logging
import logging.config

def setup_logging():
    config = {
        "version": 1,
        "formatters": {
            "detailed": {
                "format": "%(asctime)s %(levelname)-8s [%(name)s] %(message)s"
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": "trading_bot.log",
                "formatter": "detailed",
                "level": "DEBUG"
            },
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "detailed",
                "level": "INFO"
            }
        },
        "root": {
            "handlers": ["file", "console"],
            "level": "DEBUG"
        }
    }
    logging.config.dictConfig(config)