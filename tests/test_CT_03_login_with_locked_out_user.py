import time

from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

def test_login_with_blocked_user(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    #verify title_page
    login_page.verify_login_page_title()

    # enter credentials locked_out_user
    login_page.fill_field_username("locked_out_user")
    login_page.fill_field_password("secret_sauce")

    # click on login button
    login_page.click_on_login_button()

    #verify erreur message user blocked
    login_page.verify_error_message_user_locked_out()
