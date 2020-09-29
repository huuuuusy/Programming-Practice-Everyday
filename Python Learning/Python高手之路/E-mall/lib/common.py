from core import src
import logging.config
from conf import setting


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not src.user_data['name']:
            src.login()
        else:
            return func(*args, **kwargs)

    return wrapper


def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger
