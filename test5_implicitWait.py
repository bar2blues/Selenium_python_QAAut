import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)
t=1
time.sleep(t)

nom = driver.find_element(By.XPATH, "//input[@id='userName']")
nom.send_keys("Fede")
time.sleep(t)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("fede@mail.com")
time.sleep(t)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(t)
button = driver.find_element(By.XPATH, "//button[@id='submit']")
button.click()
time.sleep(t)


driver.close()