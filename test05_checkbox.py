# Create a Selenium script that navigates to a webpage with checkboxes,
# selects them in a specific order, submits the form, and then scrolls to view the
# results.

# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import time

# Create a Chrome browser instance
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Navigate to the module page on testpages.herokuapp.com
driver.get('https://testpages.herokuapp.com/pages/forms/html-form/')

# Find and click checkboxes in order: checkbox3, checkbox1, checkbox2
try:
    # Click checkbox 3
    checkbox3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[5]/td/input[3]")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox3)
    time.sleep(1)
    checkbox3.click()
    
    # Click checkbox 1
    checkbox1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[5]/td/input[1]")))
    checkbox1.click()
    
    # Click checkbox 2
    checkbox2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[5]/td/input[2]")))
    checkbox2.click()
    time.sleep(0.5)

except TimeoutException as ex:
    print(ex.msg + "Error Timeout ")
    driver.close()

# Wait for the submit button to be clickable, scroll into view and click.
try:
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
    # Smooth scroll to submit button with center alignment
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit)
    time.sleep(1)  # Brief pause for smooth scroll to complete
    try:
        # Use ActionChains for more reliable clicking
        actions = ActionChains(driver)
        actions.move_to_element(submit).click().perform()
    except ElementClickInterceptedException:
        # Fallback: perform a JS click if another element overlays the button
        driver.execute_script("arguments[0].click();", submit)
    # After submit, wait for results page and scroll to view submitted values
    time.sleep(2)  # Wait for page to load results
    # Then scroll down to see all results
    driver.execute_script("window.scrollTo({top: 1500, behavior: 'smooth', block: 'center'});")
    time.sleep(2)
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth', block: 'center'});")
except TimeoutException:
    print("Submit button was not clickable within the timeout.")

# Wait for 3 seconds
time.sleep(3)
# Close the browser
driver.close()