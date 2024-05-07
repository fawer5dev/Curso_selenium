# Import the necessary modules from Selenium
from selenium import webdriver
import time

# Create a Edge browser instance
driver = webdriver.Edge()
t=3
back="window.history.go(-1)"
back2="window.history.go(2)"

# Maximize the window
driver.maximize_window()
time.sleep(t)

# Navigate to the module page on DemoQA
driver.get('https://demoqa.com/text-box')
time.sleep(t)

#driver.get('https://testingqarvn.com.es/')
driver.get('https://www.google.com.co/')
time.sleep(t)

driver.get('https://www.tohodo.com/autofill/form.html')
time.sleep(t)

#driver.back()
driver.execute_script(back)
time.sleep(t)

#driver.back()
driver.execute_script(back)
time.sleep(t)

driver.execute_script(back2)
time.sleep(t)

# Close the browser
driver.close()