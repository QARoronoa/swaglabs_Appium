from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def verify_title_page(self, expected_title):
        WebDriverWait(self.driver, 20).until(EC.title_is(expected_title))
        title_page = self.driver.title
        assert title_page == expected_title

    def verify_element_is_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.text

    def verify_element_is_not_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element(locator))

    def fill_field(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()



