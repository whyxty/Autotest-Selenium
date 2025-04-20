from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
            element.click()
        except Exception as e:
            self.driver.save_screenshot("error_galaxy_s6.png")
            raise e


    def click_monitors(self):
        monitors = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]').click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CLASS_NAME, 'card-title')
        assert len(monitors) == count