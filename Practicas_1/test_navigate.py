import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

driver.get("https://www.youtube.com/")
time.sleep(2)

driver.get("https://www.programiz.com")
time.sleep(2)

driver.back()

driver.close()