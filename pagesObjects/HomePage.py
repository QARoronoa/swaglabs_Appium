from selenium.webdriver.common.by import By

from pagesObjects.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    #locators
    products_title = (By.CSS_SELECTOR, ".product_label")

    #methodes
    def verify_products_title_is_visible(self):
        element_text = self.verify_element_is_visible(self.products_title)
        assert element_text == "Products"