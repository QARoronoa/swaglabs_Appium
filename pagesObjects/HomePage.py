from selenium.webdriver.common.by import By

from pagesObjects.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    #locators
    products_title = (By.CSS_SELECTOR, ".product_label")
    add_to_cart_button_home_page = (By.CSS_SELECTOR, "div.inventory_item:nth-of-type(1) button")
    number_item_cart = (By.CSS_SELECTOR, ".fa-layers-counter")
    cart_page_link = (By.CSS_SELECTOR, "a[href*='./cart.html']")

    #methodes
    def verify_products_title_is_visible(self):
        element_text = self.verify_element_is_visible(self.products_title)
        assert element_text == "Products"

    def click_on_add_to_cart(self):
        self.click_on_element(self.add_to_cart_button_home_page)

    def verify_quantity_item_in_cart(self):
        quantity = self.verify_element_is_visible(self.number_item_cart)
        assert quantity == "1"

    def click_on_cart_link(self):
        self.click_on_element(self.cart_page_link)
