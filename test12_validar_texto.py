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
driver.get('https://testingqarvn.com.es/campos-requeridos/')

# Maximize the window
driver.maximize_window()

# Find the element with the attribute XPATH of img request.
btn = driver.find_element(By.XPATH, "//BUTTON[@id='wsf-1-field-109']").click()
time.sleep(t)

name_val = driver.find_element(By.XPATH, "//DIV[@id='wsf-1-invalid-feedback-95']")
name = name_val.text
print("El valor del error es: " + name)

# Coditional
if (name == "Minimum character count: 4"):
    cn = driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-95']").send_keys("PEDRO")
    time.sleep(t)
    print("NAME CORRECTLY")
else:
    print("NAME MISSED,try again")

if (name == "Minimum character count: 4"):
    cn = driver.find_element(By.XPATH, "//INPUT[@id='wsf-1-field-95']").send_keys("PEDRO")
    time.sleep(t)
    print("NAME CORRECTLY")
else:
    print("NAME MISSED,try again")

# Close the browser
time.sleep(t)
driver.close()