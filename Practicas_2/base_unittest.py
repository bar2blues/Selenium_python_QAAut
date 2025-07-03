import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1(self):
        driver = self.driver
        driver.get("https://demoqa.com")
        time.sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__== '__main__':
    unittest.main()



