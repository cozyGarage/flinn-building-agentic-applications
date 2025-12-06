import logging

try:
    from pythonjsonlogger import jsonlogger  # type: ignore

    _HAS_JSONLOGGER = True
except Exception:
    jsonlogger = None
    _HAS_JSONLOGGER = False


def configure_logging(name: str = "flinn") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        if _HAS_JSONLOGGER and jsonlogger is not None:
            handler.setFormatter(jsonlogger.JsonFormatter())
        else:
            handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


logger = configure_logging()
