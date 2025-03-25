import logging
import os
from pathlib import Path
import logging.handlers

# Create logs directory outside of the app folder
BASE_DIR = Path(__file__).resolve().parents[3]
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# File handler log file path
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Logger configuration
def setup_logger():
    logger = logging.getLogger()  # Use a specific logger name
    if not logger.hasHandlers():  # Avoid adding handlers multiple times
        logger.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)

        # File handler
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        # Add handlers to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
