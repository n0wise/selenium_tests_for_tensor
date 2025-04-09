from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class SbisPage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    CONTACTS_LIST = (By.CSS_SELECTOR, ".sbisru-Contacts-List__name")
    REGION_LOCATOR = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")
    REGION_CONTAINER = (By.XPATH, "//div[@class='sbis_ru-Region-Panel__container']")
    KAMCHATKA_REGION = (By.XPATH, "//*[contains(text(), 'Камчатский')]")
    DOWNLOAD_LINK = (By.LINK_TEXT, "Скачать локальные версии")

    def go_to_contacts(self):
        self.element_is_clickable(self.CONTACTS_LINK).click()

    def click_tensor_banner(self):
        time.sleep(3)
        self.element_is_clickable(self.TENSOR_BANNER).click()

    def check_contact_list(self):
        return self.element_is_present(self.CONTACTS_LIST).text

    def change_region_to_kamchatka(self):
        self.element_is_clickable(self.REGION_LOCATOR).click()
        time.sleep(5)
        region_container = self.element_is_present(self.REGION_CONTAINER)
        region_container.find_element(*self.KAMCHATKA_REGION).click()
        time.sleep(5)

    def check_current_region(self):
        return self.element_is_present(self.REGION_LOCATOR).text

    def go_to_downloads(self):
        self.element_is_clickable(self.DOWNLOAD_LINK).click()