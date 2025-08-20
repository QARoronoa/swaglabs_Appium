from selenium.webdriver.common.by import By

from pagesObjects.BasePage import BasePage

class Cart_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    #locators
    subheader_cart_page = (By.CSS_SELECTOR, ".subheader")
    remove_button = (By.XPATH, "//button[text()='REMOVE']")
    item_name_in_cart = (By.CSS_SELECTOR, ".inventory_item_name")
    checkout_button = (By.CSS_SELECTOR, "a.checkout_button")


    #methodes

    def verify_redirected_to_cart_page(self):
        titre = self.verify_element_is_visible(self.subheader_cart_page)
        assert titre == "Your Cart"

    def click_on_remove_button(self):
        self.click_on_element(self.remove_button)

    def verify_cart_is_empty(self):
        self.verify_element_is_not_visible(self.item_name_in_cart)

    def click_on_checkout_button(self):
        self.click_on_element(self.checkout_button)
