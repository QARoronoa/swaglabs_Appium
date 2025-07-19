import time
import allure
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

def test_login_without_credentials(setup):
    login_page = LoginPage(setup)

    #verify title_page
    with allure.step("Verify title page"):
        login_page.verify_login_page_title()

    # click on login button
    with allure.step("click on login button"):
        login_page.click_on_login_button()

    #verify erreur message user blocked
    with allure.step("verify visibility of error message"):
        login_page.verify_error_message_with_credentials_empty()
