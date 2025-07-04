import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()
t=3

driver.get("https://demoqa.com")
driver.maximize_window()

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())

btn1 = driver.find_element(By.XPATH, "//h5[normalize-space()='Elements']")

if(titulo.is_displayed() == True):
    print("Existe el elemento")
    btn1.click()
    time.sleep(t)
else:
    print("No existe el elemento")

time.sleep(t)
driver.close()