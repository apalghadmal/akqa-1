from functools import wraps
import os
import json
import logging.config


def log_func_name(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info("Calling %s ..." % func.__name__)
        print("Calling %s ..." % func.__name__)
        return func(*args, **kwargs)
    return tmp


def setup_logging(
    default_path='src/utils/logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """setup logging config"""
    value = os.getenv(env_key)
    path = value or default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def create_log_directory():
    if not os.path.exists('logs/'):
        os.makedirs('logs')
    setup_logging()
