from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.index.register import Register


class Login(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def scanf(self):
        pass

    def goto_register(self):
        self.find(By.LINK_TEXT,'企业登录').click()
        return Register()