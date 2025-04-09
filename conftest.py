import pytest, os, shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    downloads_dir = os.path.join(os.path.dirname(__file__), "tests\\downloads")
    # Создаем папку для загрузок, если не существует
    os.makedirs(downloads_dir, exist_ok=True)

    # Настройки для скачивания
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downloads_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Инициализируем драйвер
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    shutil.rmtree(downloads_dir, ignore_errors=True)
    os.makedirs(downloads_dir, exist_ok=True)
    driver.quit()
