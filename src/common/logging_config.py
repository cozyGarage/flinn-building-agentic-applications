import logging
from typing import Any, Optional

jsonlogger: Optional[Any] = None
try:
    from pythonjsonlogger import jsonlogger as _jsonlogger

    jsonlogger = _jsonlogger
    _HAS_JSONLOGGER = True
except Exception:
    jsonlogger = None
    _HAS_JSONLOGGER = False


def configure_logging(name: str = "flinn") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        if _HAS_JSONLOGGER and jsonlogger is not None and getattr(jsonlogger, "JsonFormatter", None):
            formatter_cls = getattr(jsonlogger, "JsonFormatter")
            handler.setFormatter(formatter_cls())
        else:
            handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


logger = configure_logging()
