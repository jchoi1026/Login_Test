import pytest

from page_objects.login_page import LoginPage


class TestNegativeLogins:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_err_msg",
                             [("invalidUserName", "SuperSecretPassword!", "Your username is invalid!"),
                              ("practice", "invalidPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_err_msg):
        # Create a login obj
        login = LoginPage(driver)

        # Open url
        login.open()

        # Execute login with invalid credentials
        login.execute_login(username, password)

        # Verify if the error message is displayed
        assert login.get_error_msg() == expected_err_msg, "Error message text is not expected."
