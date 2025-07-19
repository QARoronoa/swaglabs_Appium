import time
import allure
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

def test_login_invalid_password(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    #verify title_page
    with allure.step("Verify login page title"):
        login_page.verify_login_page_title()

    #enter credentials
    with allure.step(f"Enter username: {'standard_user'} and password: {'sesscret_sauce'}"):
        login_page.fill_field_username("standard_user")
        login_page.fill_field_password("sesscret_sauce")

    #click on login button
    with allure.step("click on login button"):
        login_page.click_on_login_button()

    #verify error message is visible
    with allure.step("verify visibility of error message"):
        login_page.verify_error_message_invalid_password_is_visible()





