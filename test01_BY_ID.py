# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
# driver = webdriver.Chrome()
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()

# Navigate to the module page on DemoQA
driver.get('https://demoqa.com/text-box')

# Find the element with the 'userName' attribute and enter the text xxx into it
driver.find_element(By.ID, "userName").send_keys("FAWER2")
# Wait for 1 seconds
time.sleep(1)
# Find the element with the 'userEmail' attribute and enter the text xxx into it
driver.find_element(By.ID, "userEmail").send_keys("xxx@gmail.com")
time.sleep(1)
# Find the element with the 'currentAddress' attribute and enter the text xxx into it
driver.find_element(By.ID, "currentAddress").send_keys("PRIMERA DIRECCION")
time.sleep(1)
# Find the element with the 'permanentAddress' attribute and enter the text xxx into it
driver.find_element(By.ID, "permanentAddress").send_keys("SEGUNDA DIRECCION")
# scroll down window
driver.execute_script("window.scrollTo(0,300)")

# Find the element with the 'submit' attribute and send data
driver.find_element(By.ID, "submit").click()

time.sleep(5)
# Close the browser
driver.close()