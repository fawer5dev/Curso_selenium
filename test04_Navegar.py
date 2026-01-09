# This script uses Selenium WebDriver with Chrome to automate browser navigation testing.
# It opens several web pages, then uses JavaScript window.history.go() calls to move
# backward and forward through the browser history before closing the browser.

# Import the necessary modules from Selenium
from selenium import webdriver
import time

# Create a Chrome browser instance
driver = webdriver.Chrome()
t=3
back="window.history.go(-1)"
back2="window.history.go(2)"

# Maximize the window
driver.maximize_window()
time.sleep(t)

# Navigate to the module page on testpages.herokuapp.com
driver.get('https://testpages.herokuapp.com')
time.sleep(t)

# Navigate to Google
driver.get('https://www.google.com.co/')
time.sleep(t)

# Navigate to Tohodo Autofill form page
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