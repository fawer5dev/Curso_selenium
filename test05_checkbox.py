# Select in checkbox

# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import time

# Create a Chrome browser instance
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()
t=3

# Wait for x seconds
time.sleep(t)

# Navigate to the module page on testpages.herokuapp.com
driver.get('https://testpages.herokuapp.com/pages/forms/html-form/')

# Scroll smoothly to the URL input element to ensure visibility
# driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", url_input)


# Find the element with the 'userName' attribute XPath and enter the text xxx into it
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(((By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[5]/td/input[1]"))))
    # Scroll to make the element visible before clicking
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(1)  # Give it a moment after scrolling
    element.click()
    time.sleep(t)
    #driver.quit()
except TimeoutException as ex:
    print(ex.msg + "Error Timeout ")
    driver.close()

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