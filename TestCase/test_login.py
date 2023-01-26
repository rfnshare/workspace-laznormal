from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestLogin(BaseTest):
    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.go_to_home_page()
        homepage.login()

# python -m unittest TestCase.test_login
