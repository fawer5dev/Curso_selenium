# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
# driver = webdriver.Chrome()
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

# Find the element with the 'First Name' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-110']").send_keys("PEDRO")

# Find the element with the 'Last Name' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-111']").send_keys("PICAPIEDRA")

# Find the element with the 'Email' attribute XPath nd enter the text xxx into it
driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-112']").send_keys("xxx@gmail.com")

# Find the element with the 'Phone' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-113']").send_keys("55555555")

# Find the element with the 'Inquiry' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//TEXTAREA[@id='wsf-1-field-114']").send_keys("test reto")

# Find the element with the 'Consent' attribute XPath and click to accept
driver.find_element(By.XPATH, "//LABEL[@id='wsf-1-label-115-row-1']").click()

# Find the element with the 'submit' XPath attribute and send data
driver.find_element(By.XPATH, "//BUTTON[@id='wsf-1-field-116']").click()
time.sleep(5)

# Close the browser
driver.close()