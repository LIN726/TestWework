from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, expected_conditions as ec


class BasePage:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def open(self, url):
        """

        :param url:要打开的url
        :return:
        """
        self.driver.get(url)

    def find(self, locator):
        try:
            elements = self.wait_for_click(locator)
            return elements
        except:
            print("找不到元素:" + str(locator))

    def finds(self, locator):
        try:
            elements = self.wait_for_click(locator)
            return elements
        except:
            print("找不到元素:" + str(locator))

        # return self.driver.find_elements(*locator[0])

    def click(self, *locator):
        self.find(*locator).click()

    def wait_for_click(self, locator, time=10):

        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))

    def wait_for_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator))

    def quit(self):
        self.driver.quit()

    def send_keys(self, *locator, value):
        self.find(*locator).send_keys(value)
