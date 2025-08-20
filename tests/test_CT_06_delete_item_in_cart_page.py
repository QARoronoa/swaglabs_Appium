import time

import allure
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage
from pagesObjects.Cart_Page import Cart_Page

def test_delete_product_in_cart_page(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    cart_page = Cart_Page(setup)

    #verify title_page
    with allure.step("Verify title page"):
        login_page.verify_login_page_title()

    #enter credentials
    with allure.step(f"Enter username: {'standard_user'} and password: {'secret_sauce'}"):
        login_page.fill_field_username("standard_user")
        login_page.fill_field_password("secret_sauce")

    # click on login button
    with allure.step("click on login button"):
        login_page.click_on_login_button()

    # verify redirected to home page
    with allure.step("verify redirected to home page"):
        home_page.verify_products_title_is_visible()

    #add item on cart
    with allure.step("click on add to cart first product"):
        home_page.click_on_add_to_cart()

    #click on cart page button
    with allure.step("click on cart button"):
        home_page.click_on_cart_link()


    #verify quantity
    with allure.step("verify redirected to cart page"):
        cart_page.verify_redirected_to_cart_page()

    #click on remove button
        with allure.step("click on remove button"):
            cart_page.click_on_remove_button()

    #verify cart is empty
        with allure.step("cart is empty"):
            cart_page.verify_cart_is_empty()




