from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practice.expandtesting.com/secure"
    __confirmation_header_locator = (By.XPATH, "//div[@id='flash']/b")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def header(self) -> str:
        return super()._get_text(self.__confirmation_header_locator)

    @property
    def expected_url(self) -> str:
        return self.__url
