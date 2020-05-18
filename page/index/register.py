from selenium.webdriver.chrome.webdriver import WebDriver

from page.basepage import Base


class Register(Base):
    def __init__(self):
        Base.__init__(self)