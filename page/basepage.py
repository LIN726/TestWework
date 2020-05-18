
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def open(self,url):
        self.driver.get(url)


    def find(self,By,locator):
        return self.driver.find_element(By,locator)
    def finds(self,By,locator):
        return self.driver.find_elements(By,locator)
