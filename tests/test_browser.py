import time
from selenium.webdriver.common.by import By

def test_open_s6(driver):
    driver.get('https://www.demoblaze.com/')
    driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
    title = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/h2')
    assert title.text == 'Samsung galaxy s6'

def test_twomonitors(driver):
    driver.get('https://www.demoblaze.com/')
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]').click()
    time.sleep(3)
    monitors = driver.find_elements(By.CLASS_NAME, 'card-title')
    assert len(monitors) == 2