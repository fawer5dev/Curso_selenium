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

# Find the element with the 'userName' attribute XPath and enter the text xxx into it
nom=driver.find_element(By.XPATH, "//input[@id='userName']")
nom.send_keys("FAWER3")
# Wait for 1 seconds
time.sleep(1)
# Find the element with the 'userEmail' attribute XPath nd enter the text xxx into it
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("xxx@gmail.com")
time.sleep(1)
# Find the element with the 'currentAddress' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("PRIMERA DIRECCION")
time.sleep(1)
# Find the element with the 'permanentAddress' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("SEGUNDA DIRECCION")
# scroll down window
driver.execute_script("window.scrollTo(0,300)")

# Find the element with the 'submit' XPath attribute and send data
driver.find_element(By.XPATH, "//button[@id='submit']").click()

time.sleep(5)
# Close the browser
driver.close()