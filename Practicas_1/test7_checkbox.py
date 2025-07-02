import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
driver.implicitly_wait(10)
t=3

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(t)

check_list= driver.find_element(By.XPATH, "//button[@title='Toggle']")
check_list.click()
time.sleep(t)

check_desktop = driver.find_element(By.XPATH,"//label[@for='tree-node-desktop']//span[@class='rct-checkbox']//*[name()='svg']")
check_desktop.click()
time.sleep(t)



driver.close()