import time

from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

def test_login_invalid_password(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    #verify title_page
    login_page.verify_login_page_title()

    #enter credentials
    login_page.fill_field_username("standard_user")
    login_page.fill_field_password("sesscret_sauce")

    #click on login button
    login_page.click_on_login_button()

    #verify error message is visible
    login_page.verify_error_message_invalid_password_is_visible()





