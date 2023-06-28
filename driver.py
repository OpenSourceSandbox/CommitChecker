from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service


class WebDriverManager:
    def __init__(self):
        self._set_chrome_options()

    def _set_chrome_options(self):
        self.selenium_options = ChromeOptions()
        self.selenium_options.add_argument('--headless=new')
        self.selenium_options.add_argument('--no-sandbox')
        self.selenium_options.add_argument('--disable-dev-shm-usage')
        self.selenium_options.add_argument('--start-maximized')
        self.selenium_options.add_argument('--disable-popup-blocking')

    def get_driver(self):
        driver = Chrome(
            service=Service('/usr/bin/google-chrome-stable'), version_main=113, options=self.selenium_options)
        driver.implicitly_wait(10)
        return driver
