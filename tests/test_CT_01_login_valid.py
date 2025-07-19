import time
import allure
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

def test_login_valid(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    #verify title_page
    with allure.step("Verify login page title"):
     login_page.verify_login_page_title()

    #enter credentials
    with allure.step(f"Enter username: {'standard_user'} and password: {'secret_sauce'}"):
        login_page.fill_field_username("standard_user")
        login_page.fill_field_password("secret_sauce")

    #click on login button
    with allure.step("click on login button"):
        login_page.click_on_login_button()

    #verify redirected to home page
    with allure.step("verify redirected to home page"):
        home_page.verify_products_title_is_visible()




