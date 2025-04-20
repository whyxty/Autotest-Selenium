from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
