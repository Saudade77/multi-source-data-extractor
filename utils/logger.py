import logging
import os
from datetime import datetime


def setup_logger(name: str = "extractor") -> logging.Logger:
    """Configure and return a logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_format)

    # File handler
    os.makedirs("output", exist_ok=True)
    log_filename = f"output/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_filename, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger