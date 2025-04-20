from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6').click()

    def click_monitors(self):
        monitors = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]').click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CLASS_NAME, 'card-title')
        assert len(monitors) == count