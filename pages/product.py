from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        page_title = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/h2')
        assert page_title.text == 'Samsung galaxy s6'

