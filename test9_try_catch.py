import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(10)
t=3

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(t)

try:
    color= driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']")
    time.sleep(t)

    c1=Select(color)
    c1.select_by_visible_text("Rede")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento no existe")


multi= driver.find_element(By.XPATH, "//option[@value='saab']")
time.sleep(t)




driver.close()