from page.index.index import Index


class TestIndex():
    def setup(self):
        self.index = Index()

    def test_goto_login(self):
        self.index.goto_login()

    def test_goto_register(self):
        self.index.goto_register()


    def teardown(self):
        self.index.driver.quit()