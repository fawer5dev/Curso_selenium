# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()
time.sleep(1)

# Navigate to the module page on DemoQA
driver.get('https://demoqa.com/text-box')

# Find the element with the 'userName' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("FAWER3" + Keys.TAB)

#Test with Keys
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("xxx@gmail.com" + Keys.TAB)
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("PRIMERA DIRECCION" + Keys.TAB)
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("SEGUNDA DIRECCION" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.XPATH, "//SPAN[@class='text'][text()='Check Box']").click()
time.sleep(2)

# Close the browser
driver.close()