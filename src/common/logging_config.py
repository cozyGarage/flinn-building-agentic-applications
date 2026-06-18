"""Minimal logging configuration used by tools in this repository.
This mirrors a stripped-down version of the project's logging helpers required by demos.
"""
import logging
from typing import Optional


def configure_logging(level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger("flinn")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


# Module-level logger used by tools
logger = configure_logging()

