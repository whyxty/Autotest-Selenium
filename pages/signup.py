from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string



class SignUp:

    def click_sign_up(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link")))
            element.click()
        except Exception as e:
            self.driver.save_screenshot("error_sign_up.png")
            raise e


    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.sample(characters, length))


    def generate_login(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.sample(characters, self))


    def click_login(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.ID, "sign-username")))
            element.click()
        except Exception as e:
            self.driver.save_screenshot("error_login.png")
            raise e


    def click_password(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.ID, "sign-password")))
            element.click()
        except Exception as e:
            self.driver.save_screenshot("error_password.png")
            raise e