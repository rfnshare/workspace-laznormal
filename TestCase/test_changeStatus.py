from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestLogin(BaseTest):
    def test_status(self):
        homepage = HomePage(self.driver)
        homepage.change_to_stage()
        homepage.change_to_online()


# python -m unittest TestCase.test_changeStatus
