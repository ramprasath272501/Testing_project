"""Project-wide logger factory.

Logs to the console and to a dated file under logs/ so every test run leaves
an auditable trail - useful when debugging CI failures.
"""
import logging
import os
from datetime import datetime


def get_logger(name):
    logger = logging.getLogger(name)
    if logger.handlers:  # avoid duplicate handlers on re-import
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler(
        os.path.join("logs", f"test_run_{datetime.now():%Y%m%d}.log")
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
