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
#driver.get('https://demoqa.com/modal-dialogs')
driver.get('https://demoqa.com/alerts')

# Maximize the window
driver.maximize_window()

# Find the Modal with the attribute XPATH and click to open modal.
#driver.find_element(By.XPATH, "//button[@id='showSmallModal']").click()

# Find the Button with the attribute XPATH and click to open alert .
driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
time.sleep(t)

# Close button Modal opened
#driver.find_element(By.XPATH, "//button[@id='closeSmallModal']").click()

# Accept Alert
#alert = driver.switch_to.alert
#alert.accept()
#time.sleep(t)

# Cancel Alert
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(t)

# Close the browser
driver.close()