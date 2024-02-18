import time

import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveLogin:
    @pytest.mark.positive
    def test_login_positive(self, driver):
        # Create a login obj
        login = LoginPage(driver)
        login_successfully = LoggedInSuccessfullyPage(driver)

        # Open url
        login.open()

        # Execute login with correct username and password
        login.execute_login("practice", "SuperSecretPassword!")

        # Verify new page url contains "/secure"
        assert login_successfully.expected_url == login_successfully.current_url, "Actual url is not the same expected."

        # Verify new page url contains expected text
        assert login_successfully.header == "You logged into a secure area!", "The login successful text isn't expected."

