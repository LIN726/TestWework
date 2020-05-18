from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.basepage import Base
from page.index.login import Login
from page.index.register import Register


class Index(Base):
    def __init__(self):
        Base.__init__(self)
        self.open('https://work.weixin.qq.com/')

    def goto_login(self):
        self.find(By.LINK_TEXT,'企业登录').click()
        return Login()


    def goto_register(self):
        self.find(By.LINK_TEXT,'立即注册').click()
        return Register()