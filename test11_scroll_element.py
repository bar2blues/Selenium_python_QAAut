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
t=5

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)


try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='button--9NFL8 outline--rYKlp light--C3NP- center--ZZf40']")))
    buscar = driver.find_element(By.XPATH, "//a[@class='button--9NFL8 outline--rYKlp light--C3NP- center--ZZf40']")
    ir = driver.execute_script("arguments[0].scrollIntoView();", buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no existe")


time.sleep(t)
driver.close()