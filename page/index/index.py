from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.index.login import Login
from page.index.register import Register


class Index(BasePage):
    _base_url = 'https://work.weixin.qq.com/'


    def goto_login(self):
        self.click(By.LINK_TEXT,'企业登录')
        return Login()


    def goto_register(self):
        self.find(By.LINK_TEXT,'立即注册').click()
        return Register()