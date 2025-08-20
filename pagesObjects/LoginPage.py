import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pagesObjects.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #locators
    logo = (By.CSS_SELECTOR, ".login_logo")
    username_field = (By.CSS_SELECTOR, "#user-name")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    error_message = (By.CSS_SELECTOR, "h3")

        #methodes
    def verify_login_page_title(self):
        self.verify_title_page("Swag Labs")


    def fill_field_username(self, text):
        with allure.step(f"🖊️ Saisie du nom d'utilisateur : {text}"):
            self.fill_field(LoginPage.username_field, text)

    def fill_field_password(self, text):
        with allure.step(f"🔒 Saisie du mot de passe : {text}"):
            self.fill_field(LoginPage.password_field, text)

    def click_on_login_button(self):
        with allure.step("👆 Clic sur le bouton de connexion"):
            self.click_on_element(LoginPage.login_button)

    def verify_error_message_invalid_password_is_visible(self):
        error_message = self.verify_element_is_visible(self.error_message)
        assert "Username and password do not match" in error_message

    def verify_error_message_user_locked_out(self):
        error_message = self.verify_element_is_visible(self.error_message)
        assert "Sorry, this user has been locked out." in error_message

    def verify_error_message_with_credentials_empty(self):
        error_message = self.verify_element_is_visible(self.error_message)
        assert "Username is required" in error_message