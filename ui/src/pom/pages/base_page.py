from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_wait(self):
        return WebDriverWait(self.driver, 25)
