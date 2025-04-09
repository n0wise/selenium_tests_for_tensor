# Cценарий 3
import pytest, time, os, re
from pages.sbis_page import SbisPage
from pages.sbis_download_page import SbisDownloadPage

@pytest.mark.usefixtures("browser")
class TestSbisDownload:
    def test_full_scenario(self, browser):
        # Шаг 1: Переходим на sbis.ru в раздел Контакты
        sbis_page = SbisPage(browser, "https://sbis.ru/")
        sbis_page.open()

        # Шаг 2: В Footer'e находим и переходим в загрузки"
        sbis_page.go_to_downloads()
        time.sleep(5)
        sbis_download_page = SbisDownloadPage(browser, browser.current_url)
        size_desc = float(re.findall(r'\d+\.\d+', sbis_download_page.get_installer_desc())[0]) # Размер на сайте

        # Шаг 3: Скачиваем Плагин для Windows в папку "downloads" в папке с тестом
        sbis_download_page.click_download()
        time.sleep(10)
        files = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\downloads")
        files_and_path = [os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\downloads", f) for f in files]
        size_bytes = os.path.getsize(files_and_path[0])  # Размер скачанного файла в байтах
        size_mb = round((size_bytes / (1024 * 1024)), 2)  # Конвертация в мегабайты

        # Шаг 4: Убеждаемся что Плагин скачался (проверяем что файл не временный, а имеет расширение .exe)
        assert len(files) > 0 and files[0].endswith(".exe"), "Файл не был скачан"

        # Шаг 5: Сравниваем размер скачанного файла в мегабайтах с размером указанным на сайте
        assert size_mb == size_desc, f"Размер файла {size_mb} не соответсвует указанному на сайте {size_desc}"