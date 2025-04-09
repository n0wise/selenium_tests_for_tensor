from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from conftest import browser

actions = ActionChains(browser)

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_present(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                          message=f"Element is not present. {locator}")
    def elements_is_present(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Elements is not present. {locator}")

    def element_is_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator),
                                                          message=f"Element is not clickable. {locator}")

    def scroll_to_element(self, locator):
        element = self.element_is_present(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_popup(self):
        popup = self.browser.switch_to.alert
        return popup