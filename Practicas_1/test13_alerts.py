import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
t = 3

driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH, "//button[@id='showSmallModal']").click()

time.sleep(t)
driver.close()
