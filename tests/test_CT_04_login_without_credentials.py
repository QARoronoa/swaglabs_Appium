import time

from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

def test_login_without_credentials(setup):
    login_page = LoginPage(setup)

    #verify title_page
    login_page.verify_login_page_title()

    # click on login button
    login_page.click_on_login_button()

    #verify erreur message user blocked
    login_page.verify_error_message_with_credentials_empty()
