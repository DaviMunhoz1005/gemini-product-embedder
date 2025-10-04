import logging
import sys

class CenteredFormatter(logging.Formatter):
    def format(self, record):
        record.name = f"{record.name:^20}"
        record.levelname = f"{record.levelname:^10}"
        return super().format(record)

def setup_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a standard logger for the project.

    Args:
        name (str): Logger name, usually __name__.
        level (int): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        formatter = CenteredFormatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
