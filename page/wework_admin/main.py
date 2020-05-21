from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.wework_admin.add_member import AddMember


class Main(BasePage):
    add_member_entrance = (By.XPATH, "//*[@class ='ww_indexImg ww_indexImg_AddMember']")

    def __init__(self):
        BasePage.__init__(self)

    def goto_add_member(self):
        # self.driver.find_element(By)
        self.find(self.add_member_entrance).click()
        return AddMember()
