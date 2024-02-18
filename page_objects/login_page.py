from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practice.expandtesting.com/login"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __login_btn_field = (By.XPATH, "//form[@id='login']/button[@type='submit']")
    __login_successful_confirmation_msg_field = (By.XPATH, "//div[@id='flash']/b[.='You logged into a secure area!']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._find(self.__username_field).send_keys(username)
        super()._find(self.__password_field).send_keys(password)
        super()._click(self.__login_btn_field)
