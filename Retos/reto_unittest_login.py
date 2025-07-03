import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# RETO LOGIN
#campos vacios
# usu y pass incorrectas
#usu compl y pass vacio
#usu vacio y pass completo
#campos correctos
class Login_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/v1/")
        time.sleep(3)

    def test_login_user_pass_fail(self):
        driver = self.driver
        user_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_field.send_keys("ged123")
        pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
        pass_field.send_keys("asd123")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error = error.text
        if(error == "Epic sadface: Username and password do not match any user in this service"):
            print("Los datos no son correctos.")
            print("Prueba OK")
        time.sleep(3)

    def test_login_user_empty(self):
        driver = self.driver
        pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
        pass_field.send_keys("asd123")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error = error.text
        if (error == "Username is required"):
            print("Falta el nombre.")
            print("Prueba OK")
        time.sleep(3)

    def test_login_pass_empty(self):
        driver = self.driver
        user_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_field.send_keys("ged123")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error = error.text
        if (error == "Password is required"):
            print("Falta el password.")
            print("Prueba OK")
        time.sleep(3)

    def test_login_user_pass_ok(self):
        driver = self.driver
        user_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_field.send_keys("standard_user")
        pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
        pass_field.send_keys("secret_sauce")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        confirm = driver.find_element(By.XPATH, "//div[@class='app_logo']")
        confirm.is_displayed()
        print("El elemento es: " + str(confirm))
        print("Prueba OK")
        time.sleep(3)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__== '__main__':
    unittest.main()



