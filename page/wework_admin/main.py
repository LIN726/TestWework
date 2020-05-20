from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.wework_admin.add_member import AddMember


class Main(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def goto_add_member(self):
        self.find(By.XPATH,"//*[@class ='index_service_cnt_item_title']").click()
        return AddMember()