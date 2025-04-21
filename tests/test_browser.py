import time
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage
from pages.signup import SignUp

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitors()
    time.sleep(3)
    homepage.check_products_count(2)

def test_sign_up(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_sign_up()
    time.sleep(3)
    homepage.click_login()
    homepage.generate_login()
    time.sleep(3)
    homepage.click_password()
    homepage.generate_password()