import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(10)
t=3

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(t)

#WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.XPATH, "1"))
# value = driver.find_element(By.XPATH, "//div[contains(text(),'Select Option')]")
# value.click()
# time.sleep(t)
#
# v1=Select(value)
# v1.select_by_visible_text("Group 2, option 1") -> falta marcar la seleccion!!!
# time.sleep(t)

color= driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']")
time.sleep(t)

c1=Select(color)
c1.select_by_visible_text("Yellow")
time.sleep(t)


driver.close()