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

# Navigate to the page on pixabay
driver.get('https://pixabay.com/')

# Maximize the window
driver.maximize_window()

# if the element is found, it is scrolled into view using the execute_script method
try:
    time.sleep(t)
    find = driver.find_element(By.XPATH, "//SPAN[@class='label--Ngqjq'][text()='Discover more']")
    go = driver.execute_script("arguments[0].scrollIntoView();", find)
    time.sleep(5)
except TimeoutException as ex:
    print(ex.msg + "ELEMENT UNAVAILABLE ")
    time.sleep(t)
    driver.close()