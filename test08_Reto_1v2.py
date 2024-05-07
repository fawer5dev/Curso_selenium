# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()

# Wait for x seconds
t=2
time.sleep(t)

# Navigate to the module page on testingqarvn
driver.get('https://testingqarvn.com.es/contacto-2/')

# scroll down window
driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

# Find the element with the attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-110']").send_keys("PEDRO" + Keys.TAB
                                                                          + "PICAPIEDRA" + Keys.TAB
                                                                          + "xxx@gmail.com" + Keys.TAB
                                                                          + "55555555" + Keys.TAB
                                                                          + "test reto")

# Find the element with the 'Consent' attribute XPath and click to accept
driver.find_element(By.XPATH, "//LABEL[@id='wsf-1-label-115-row-1']").click()

# Find the element with the 'submit' XPath attribute and send data
driver.find_element(By.XPATH, "//BUTTON[@id='wsf-1-field-116']").click()
time.sleep(5)

# Close the browser
driver.close()