from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class TensorAboutPage(BasePage):
    WORKING_SECTION = (By.XPATH, "//h2[contains(text(), 'Работаем')]/ancestor:"
                                 ":div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']")

    def get_working_section_images(self):
        self.scroll_to_element(self.WORKING_SECTION)
        time.sleep(5)
        # Находим раздел "Работаем"
        section = self.element_is_present(self.WORKING_SECTION)

        # Получаем все изображения внутри этого раздела
        return section.find_elements(By.TAG_NAME, "img")

    def check_working_section_images_sizes(self):
        images = self.get_working_section_images()
        sizes = []
        for img in images:
            sizes.append((img.size['width'], img.size['height']))

        # Проверяем, что все изображения имеют одинаковые размеры
        first_size = sizes[0]
        for size in sizes[1:]:
            assert size == first_size, f"Размеры изображений различаются: {size} != {first_size}"
        return True