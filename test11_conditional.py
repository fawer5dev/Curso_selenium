# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Wait for x seconds
t=2
time.sleep(t)

# Navigate to the page on DemoQA
driver.get('https://demoqa.com')

# Maximize the window
driver.maximize_window()

# Find the element with the attribute XPATH of img request.
header = driver.find_element(By.XPATH, "//IMG[@src='/images/Toolsqa.jpg']")

# Coditional
if (header.is_displayed() == True):
    print("image available")
else:
    print("image UNavailable,try again")

# Close the browser
time.sleep(t)
driver.close()