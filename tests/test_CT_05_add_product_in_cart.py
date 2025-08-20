import allure
from pagesObjects.LoginPage import LoginPage
from pagesObjects.HomePage import HomePage


def test_add_product_in_cart(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)


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


    #verify quantity
    with allure.step("The quantity is 1"):
        home_page.verify_quantity_item_in_cart()
