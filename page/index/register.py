from selenium.webdriver.chrome.webdriver import WebDriver

from page.basepage import BasePage


class Register(BasePage):
    def __init__(self):
        BasePage.__init__(self)
