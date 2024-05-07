# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Wait for x seconds
t=2
time.sleep(t)

# Navigate to the module page on DemoQA
driver.get('https://testingqarvn.com.es/colegio/')

# Maximize the window
driver.maximize_window()

# scroll down window
driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

# Find the elements links attribute XPath and click to accept
# driver.find_element(By.XPATH, "//LABEL[@id='wsf-1-label-115-row-1']").click()
driver.find_element(By.LINK_TEXT, "Personal Information").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT,"Secondary Education").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT,"Post-Secondary Education").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT,"Personal Statement").click()
time.sleep(t)

# Close the browser
driver.close()