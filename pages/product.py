from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Добавляем инициализацию wait

    def check_title_is(self, expected_title):
        try:
            title_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//h2[@class="name"]'))
            )
            assert expected_title.lower() in title_element.text.lower()
        except Exception as e:
            self.driver.save_screenshot("product_title_error.png")
            raise e