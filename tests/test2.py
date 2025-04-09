# Сценарий 2
import pytest, time
from pages.sbis_page import SbisPage

@pytest.mark.usefixtures("browser")
class TestSbis:
    def test_full_scenario(self, browser):
        # Шаг 1: Переходим на sbis.ru в раздел Контакты
        sbis_page = SbisPage(browser, "https://sbis.ru/")
        sbis_page.open()
        sbis_page.go_to_contacts()
        time.sleep(2)

        # Шаг 2: Проверяем, что определился наш регион (в данном случае - Москва)
        region = sbis_page.check_current_region()
        assert "Москва" in region, f"Ожидался регион 'Москва', но получен '{region}'"
        first_contact = sbis_page.check_contact_list()
        assert "Москва" in first_contact, f"Ожидался регион 'Москва', но получен '{first_contact}'"

        # Шаг 3: Меняем регион на Камчатский край
        sbis_page.change_region_to_kamchatka()
        time.sleep(2)

        # Шаг 4: Проверяем, что подставился выбранный регион, список партнеров изменился, url и
        # title содержат информацию выбранного региона

        region = sbis_page.check_current_region()
        assert region == "Камчатский край", f"Ожидался регион 'Камчатский край', но получен '{region}'"
        first_contact = sbis_page.check_contact_list()
        assert "Камчат" in first_contact, f"Ожидался регион 'Камчатский край', но получен '{first_contact}'"
        assert "kamchatskij" in browser.current_url, f"Ожидался регион 'Камчатский край (kamchatskij)', но получен '{browser.current_url}'"