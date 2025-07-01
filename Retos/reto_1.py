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

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(t)

# UPLOAD FIRSTNAME, LASTNAME, EMAIL
try:
    first_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='firstName']")))
    first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
    first_name.send_keys("Fede")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento FirstName no existe")

try:
    last_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='lastName']")))
    last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
    last_name.send_keys("Bardo")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento LastName no existe")

try:
    email = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='userEmail']")))
    email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
    email.send_keys("email@mail.com")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento email no existe")

#SELECT GENDER
try:
    gender = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Male']")))
    gender = driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento gender no existe")

#UPLOAD MOBILE NUMBER, BIRTHDAY
try:
    mobile_number = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='userNumber']")))
    mobile_number = (driver.find_element(By.XPATH, "//input[@id='userNumber']"))
    mobile_number.send_keys("0123456789")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento mobileNumber no existe")

try:
    birthday = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='dateOfBirthInput']")))
    birthday = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento birthday no existe")

#CHECKS HOBBIES
try:
    hobbie1 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Sports']")))
    hobbie1 = driver.find_element(By.XPATH, "//label[normalize-space()='Sports']").click()
    time.sleep(t)

    hobbie2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Reading']")))
    hobbie2 = driver.find_element(By.XPATH, "//label[normalize-space()='Reading']").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento hobbies no existe")

#UPLOAD FILES
try:
    picture = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='uploadPicture']")))
    picture = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
    picture.send_keys("C://Users//Federico Barderi//Desktop//Projects//Selenium_python_QAAut//Images//miramar.jpg")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no existe")

#UPLOAD ADDRESS
try:
    address = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='currentAddress']")))
    address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("street false 123")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print ("El elemento address no existe")

#SELECT CITY
#SUBMIT

submit_button= driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(t)


driver.close()