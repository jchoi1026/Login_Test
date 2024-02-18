import pytest

from page_objects.login_page import LoginPage


class TestPositiveLogin:
    @pytest.mark.positive
    def test_login_positive(self, driver):
        # Create a login obj
        login = LoginPage(driver)

        # Open url
        login.open()
