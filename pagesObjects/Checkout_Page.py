from selenium.webdriver.common.by import By

from pagesObjects.BasePage import BasePage
class Checkout_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    #locators
    checkout_title = (By.CSS_SELECTOR, ".subheader")
    firstName_field = (By.CSS_SELECTOR, "#first-name")
    lastName_field = (By.CSS_SELECTOR, "#last-name")
    zipCode_field = (By.CSS_SELECTOR, "#postal-code")
    continue_button = (By.CSS_SELECTOR, "input.cart_button")
    finish_button = (By.LINK_TEXT, "FINISH")
    complete_order_message = (By.CSS_SELECTOR, ".complete-header")

    #methodes

    def verify_redirected_to_checkout_page(self):
        titre = self.verify_element_is_visible(self.checkout_title)
        assert titre == "Checkout: Your Information"

    def fill_checkout_information(self, firstName, lastName, zipCode):
        self.fill_field(self.firstName_field, firstName)
        self.fill_field(self.lastName_field,lastName)
        self.fill_field(self.zipCode_field, zipCode)

    def click_on_continue_button(self):
        self.click_on_element(self.continue_button)

    def click_on_finish_button(self):
        self.click_on_element(self.finish_button)

    def verify_message_success_message(self):
       title =  self.verify_element_is_visible(self.complete_order_message)
       assert title == "THANK YOU FOR YOUR ORDER"