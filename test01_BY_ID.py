# Automated test script for filling out form fields on testpages.herokuapp.com using Selenium WebDriver

# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Create a Chrome browser instance
driver = webdriver.Chrome()
# Maximize the window
driver.maximize_window()
# Navigate to the module page on testpages.herokuapp.com
driver.get('https://testpages.herokuapp.com/pages/forms/text-inputs/')

# Find the element with the 'text-input' attribute and enter the text xxx into it
driver.find_element(By.ID, "text-input").send_keys("PEDRO PICAPIEDRA")
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'email-input' attribute and enter the text xxx into it
driver.find_element(By.ID, "email-input").send_keys("xxx@gmail.com")
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'password-input' attribute and enter the text xxx into it
driver.find_element(By.ID, "password-input").send_keys("CLAVE123")
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'url-input' attribute and enter the text xxx into it
driver.find_element(By.ID, "url-input").send_keys("https://www.google.com/")

# Scroll down window
# driver.execute_script("window.scrollTo(0,300)")

# Wait for the submit button to be clickable, scroll into view and click.
try:
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    try:
        submit.click()
    except ElementClickInterceptedException:
        # Fallback: perform a JS click if another element overlays the button
        driver.execute_script("arguments[0].click();", submit)
except TimeoutException:
    print("Submit button was not clickable within the timeout.")

# Wait for 3 seconds
time.sleep(3)
# Close the browser
driver.close()