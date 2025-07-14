from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver



    def verify_title_page(self, expected_title):
        WebDriverWait(self.driver, 20).until(expected_conditions.title_is(expected_title))
        title_page = self.driver.title
        assert title_page == expected_title

    def verify_element_is_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    def fill_field(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()