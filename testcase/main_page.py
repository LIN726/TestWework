from page.wework_admin.main import Main


class TestMainPage():
    def setup(self):
        self.main = Main()

    def test_goto_add_member(self):
        self.main.goto_add_member()

    def teardown(self):
        self.main.driver.quit()