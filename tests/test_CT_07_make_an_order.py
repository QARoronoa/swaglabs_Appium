import time

import allure
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage
from pagesObjects.Checkout_Page import Checkout_Page
from pagesObjects.Cart_Page import Cart_Page

def test_make_an_order(setup, fill_checkout_info):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    cart_page = Cart_Page(setup)
    checkout_page = Checkout_Page(setup)

    # verify title_page
    with allure.step("Verify login page title"):
        login_page.verify_login_page_title()

    # enter credentials
    with allure.step(f"Enter username: {'standard_user'} and password: {'secret_sauce'}"):
        login_page.fill_field_username("standard_user")
        login_page.fill_field_password("secret_sauce")

    # click on login button
    with allure.step("click on login button"):
        login_page.click_on_login_button()

        # add item on cart
    with allure.step("click on add to cart first product"):
        home_page.click_on_add_to_cart()

    # click on cart page button
    with allure.step("click on cart button"):
        home_page.click_on_cart_link()

    with allure.step("clickon checkout button"):
        cart_page.click_on_checkout_button()
        checkout_page.verify_redirected_to_checkout_page()

    with allure.step("remplir le formulaire"):
        checkout_page.fill_checkout_information(fill_checkout_info["firstName"],
                                                fill_checkout_info["lastName"],
                                                fill_checkout_info["zipCode"])
        checkout_page.click_on_continue_button()
        checkout_page.click_on_finish_button()
        checkout_page.verify_message_success_message()




