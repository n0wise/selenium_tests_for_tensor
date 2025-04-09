from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorPage(BasePage):
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    ABOUT_LINK = (By.XPATH, "//*[contains(text(), 'Сила в людях')]/following::a[contains(text(), 'Подробнее')]")

    def power_in_people_block_is_present(self):
        return self.element_is_present(self.POWER_IN_PEOPLE_BLOCK)

    def go_to_about_page(self):
        self.scroll_to_element(self.POWER_IN_PEOPLE_BLOCK)
        self.element_is_clickable(self.ABOUT_LINK).click()