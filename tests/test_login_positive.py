import pytest
from selenium import webdriver

class TestPositiveLogin():
    @pytest.mark.positive
    def test_login_positive(self):
        __url = "https://practice.expandtesting.com/login"

        browser = webdriver.Chrome()
        browser.get(__url)