# Сценарий 1
import pytest
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage

@pytest.mark.usefixtures("browser")
class TestSbisTensor:
    def test_full_scenario(self, browser):
        # Шаг 1: Переходим на sbis.ru в раздел Контакты
        sbis_page = SbisPage(browser, "https://sbis.ru/")
        sbis_page.open()
        sbis_page.go_to_contacts()

        # Шаг 2: Находим баннер Тензор и кликаем по нему
        sbis_page.click_tensor_banner()

        # Шаг 3: Переходим на tensor.ru
        browser.switch_to.window(browser.window_handles[1])
        tensor_page = TensorPage(browser, browser.current_url)

        # Шаг 4: Проверяем наличие блока "Сила в людях"
        assert tensor_page.power_in_people_block_is_present(), "Блок 'Сила в людях' не найден"

        # Шаг 5: Переходим в "Подробнее" и проверяем URL
        tensor_page.go_to_about_page()
        assert browser.current_url == "https://tensor.ru/about", "Неверный URL страницы 'О компании'"

        # Шаг 6: Проверяем размеры изображений в разделе "Работаем"
        tensor_about_page = TensorAboutPage(browser, browser.current_url)
        assert tensor_about_page.check_working_section_images_sizes(), "Размеры изображений в разделе 'Работаем' не совпадают"