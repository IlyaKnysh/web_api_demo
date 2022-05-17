import tempfile

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from config.env import BROWSER

browsers = {
    'chrome': webdriver.Chrome,
    'remote': webdriver.Remote
}


class Driver:
    def __init__(self, **kwargs) -> None:
        """
        use if statement to set any driver (incl. remote)
        """
        profile_dir = tempfile.mkdtemp()
        self.kwargs = kwargs
        if BROWSER == 'chrome':
            self.kwargs['executable_path'] = ChromeDriverManager().install()
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=" + profile_dir)
            options.add_argument("--start-maximized")
            # options.add_argument("--headless")  # Add this option to run in headless node
            self.kwargs['options'] = options

    def start(self) -> WebDriver:
        driver = browsers[BROWSER](**self.kwargs)
        return driver
