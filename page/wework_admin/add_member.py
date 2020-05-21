from page.basepage import BasePage


class AddMember(BasePage):
    name_input = ('By.XPATH',"//*[@name='username']")
    account_input = ('By.XPATH',"//*[@name='acctid']")
    englishname_input = ('By.XPATH',"//*[@name = 'english_name']")
    male_radio = ('By.XPATH',"//*[@name = 'gender' and @value = '1']")
    female_radio = ('By.XPATH',"//*[@name = 'gender' and @value = '2']")
    def __init__(self):
        BasePage.__init__(self)







