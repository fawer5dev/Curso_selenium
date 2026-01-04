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
# Navigate to the module page on DemoQA
driver.get('https://demoqa.com/text-box')

# Find the element with the 'userName' attribute and enter the text xxx into it
driver.find_element(By.ID, "userName").send_keys("FAWER2")
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'userEmail' attribute and enter the text xxx into it
driver.find_element(By.ID, "userEmail").send_keys("xxx@gmail.com")
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'currentAddress' attribute and enter the text xxx into it
driver.find_element(By.ID, "currentAddress").send_keys("PRIMERA DIRECCION")
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'permanentAddress' attribute and enter the text xxx into it
driver.find_element(By.ID, "permanentAddress").send_keys("SEGUNDA DIRECCION")

# Wait for the submit button to be clickable, scroll into view and click.
try:
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
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