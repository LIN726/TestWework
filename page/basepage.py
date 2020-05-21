from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def open(self, url):
        self.driver.get(url)

    def find(self, *args):
        return self.driver.find_element(*args[0])

    def finds(self, *args):

        return self.driver.find_elements(*args[0])


    def click(self,*args):
        self.find(*args).click()


