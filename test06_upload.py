# Upload a file test

# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Wait for x seconds
t=2
time.sleep(t)

# Navigate to the page on testpages.herokuapp.com
driver.get('https://testpages.herokuapp.com/styled/file-upload-test.html')

# Maximize the window
driver.maximize_window()

# Find the SELECT MENU with the attribute CLASS_NAME and Select it.
try:
    time.sleep(t)
    file = driver.find_element(By.XPATH, "//input[@id='fileinput']")
    file.send_keys("E://Mi PC//Programacion//Python//Selenium-Course//images//bicycle-g5335ffc14_1280.png")
    driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg + "ELEMENT UNAVAILABLE ")
    time.sleep(t)
    driver.close()