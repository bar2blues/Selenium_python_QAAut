import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.ID, "userName")
nom.send_keys("Fede")
time.sleep(2)
driver.find_element(By.ID, "userEmail").send_keys("fede@mail.com")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
button = driver.find_element(By.ID, "submit")
button.click()
time.sleep(2)


driver.close()