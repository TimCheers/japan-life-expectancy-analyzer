import logging

def get_logger(name="analyzer"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s — %(message)s")

    # Avoid duplicate handlers
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        fh = logging.FileHandler("analyzer.log")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
