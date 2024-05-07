# Select in checkbox

# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()
t=3
# Wait for x seconds
time.sleep(t)

# Navigate to the module page on DemoQA
driver.get('https://demoqa.com/checkbox')

# Find the element with the 'userName' attribute XPath and enter the text xxx into it

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//SPAN[@class='rct-title'][text()='Home']")))
    element.click()
    time.sleep(t)
    driver.quit()
except TimeoutException as ex:
    print(ex.msg + "EROOR TIMEOUT ")
    driver.close()