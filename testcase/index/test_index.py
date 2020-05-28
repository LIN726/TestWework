from page.index.index import Index


class TestIndex():

    def setup_class(self):
        self.index = Index()

    def test_goto_login(self):
        self.index.goto_login()

    def test_goto_register(self):
        self.goto_register()


