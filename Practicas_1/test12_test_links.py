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

driver.get("https://demoqa.com/links")
driver.maximize_window()
time.sleep(t)

#OBTENER TODOS OS LINKS
links = driver.find_elements(By.TAG_NAME, "a")
print("Hay ", len(links), " links en la página")

#Imprime los nombres de los links
for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Home").click()
time.sleep(t)

driver.close()