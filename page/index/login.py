from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.index.register import Register


class Login(BasePage):
    _register_entrace = (By.LINK_TEXT,'企业登录')

    def scanf(self):
        pass

    def goto_register(self):
        self.find(self._register_entrace).click()
        return Register()