import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()
t=3

driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")
driver.maximize_window()
time.sleep(t)

try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fileinput1']")))
    buscar = driver.find_element(By.XPATH, "//input[@id='fileinput']")
    buscar.send_keys("C://Users//Federico Barderi//Desktop//Projects//Selenium_python_QAAut//Images//miramar.jpg")
    driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
    driver.find_element(By.XPATH, "//input[@name='upload']").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no existe")

driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
driver.find_element(By.XPATH, "//input[@name='upload']").click()
time.sleep(t)

time.sleep(t)
driver.close()