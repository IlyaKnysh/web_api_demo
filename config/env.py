import os

from selene import config as _selene_config
from dotenv import load_dotenv

load_dotenv()  # load sys vars from .env file


def get(key: str, default: any = None) -> str:
    return os.environ.get(key=key, default=default)


PROJECT_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEST_REPORTS_DIR = os.environ.get("TEST_REPORTS_DIR", os.path.join(PROJECT_DIRECTORY, "tests/screenshots"))
SCREEN_PATH = os.path.join(TEST_REPORTS_DIR,
                           "screen_{}.png".format(str(_selene_config.counter)).replace('count(', '').replace(')', ''))

URL = get('URL', 'http://localhost:5000')
BROWSER = get('BROWSER', 'chrome')


class DbCredentials:
    """
    Sensitive credentials shouldn't be placed directly to a code. One of possible solution - use system variables
    """
    DB_USER = get('DB_USER')
    DB_HOST = get('DB_HOST')
    DB_PORT = int(get('DB_PORT'))
    DB_PASS = get('DB_PASS')
    DB_NAME = get('DB_NAME')
