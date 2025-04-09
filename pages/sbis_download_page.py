from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisDownloadPage(BasePage):
    WEB_INSTALLER_LINK = (By.XPATH, "//*[contains(text(), 'Веб-установщик')]/following::a[contains(text(), 'Скачать')]")

    def click_download(self):
        self.element_is_clickable(self.WEB_INSTALLER_LINK).click()

    def get_installer_desc(self):
        return self.element_is_present(self.WEB_INSTALLER_LINK).text