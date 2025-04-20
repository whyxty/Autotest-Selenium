import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver
    time.sleep(3)

    driver.quit()