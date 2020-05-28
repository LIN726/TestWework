from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def explicit_wait_visiable(func):
    def deco(*args, **kwargs):
        ins: BasePage = args[0]
        print(args[2])
        try:
            WebDriverWait(ins.driver, timeout=10).until(ec.visibility_of_element_located((args[1],args[2])))
            return func(*args, **kwargs)
        except:
            print('找不到元素')

    return deco
def explicit_wait_clickable(func):
    def deco(*args, **kwargs):
        ins: BasePage = args[0]
        print(args[2])
        try:
            WebDriverWait(ins.driver, timeout=10).until(ec.element_to_be_clickable((args[1],args[2])))
            return func(*args, **kwargs)
        except:
            print('找不到元素')

    return deco


class BasePage:
    _base_url = ''

    def __init__(self):
        self.options = Options()
        self.options.debugger_address = '127.0.0.1:9223'
        self.driver = webdriver.Chrome(options=self.options)
        if self._base_url != '':
            self.open(self._base_url)

    def open(self, url):
        """

        :param url:要打开的url
        :return:
        """
        self.driver.get(url)

    @explicit_wait_visiable
    def find(self, By, value):
        """

        :param locator:
        :return: 找到的元素
        判断元素是否可见，再去查找
        """
        # if self.driver.find_element(By,value).is_displayed():
        return self.driver.find_element(By, value)

    def finds(self, locator):

        try:
            self.wait_for_visible(locator)
            return self.driver.find_elements(*locator)
        except:
            print("找不到元素:" + str(locator))
    @explicit_wait_clickable
    def click(self, By, value):
        self.driver.find_element(By, value).click()

    def wait_for_click(self, locator, time=10):

        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))

    def wait_for_visible(self, By, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(By, locator))

    def quit(self):
        self.driver.quit()

    def send_keys(self, locator, value):
        self.find(locator).send_keys(value)
