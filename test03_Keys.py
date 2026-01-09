# Automated test script for filling out form fields on testpages.herokuapp.com using Selenium WebDriver
# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Create a Edge browser instance
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Navigate to the module page on testpages.herokuapp.com
driver.get('https://testpages.herokuapp.com/pages/forms/text-inputs/')

# Find the element with the 'text-input' attribute XPath and enter the text xxx into it
nom=driver.find_element(By.XPATH, "//input[@id='text-input']")
nom.send_keys("PABLO MARMOL" + Keys.TAB)
# Wait for 0.5 seconds
time.sleep(0.5)
# Find the element with the 'email-input' attribute XPath nd enter the text xxx into it
driver.find_element(By.XPATH, "//input[@id='email-input']").send_keys("xxx@gmail.com" + Keys.TAB)
time.sleep(0.5)
# Find the element with the 'password-input' attribute XPath and enter the text xxx into it
driver.find_element(By.XPATH, "//input[@id='password-input']").send_keys("CLAVE123" + Keys.TAB)
time.sleep(0.5)
# Find the element with the 'url-input' attribute XPath and enter the text xxx into it
url_input = driver.find_element(By.XPATH, "//input[@id='url-input']")
url_input.send_keys("https://www.google.com/" + Keys.TAB)
time.sleep(0.5)
# Scroll smoothly to the URL input element to ensure visibility
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", url_input)

# Wait for the submit button to be clickable, scroll into view and click.
try:
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
    # Smooth scroll to submit button with center alignment
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit)
    time.sleep(0.5)  # Brief pause for smooth scroll to complete
    try:
        # Use ActionChains for more reliable clicking
        actions = ActionChains(driver)
        actions.move_to_element(submit).click().perform()
    except ElementClickInterceptedException:
        # Fallback: perform a JS click if another element overlays the button
        driver.execute_script("arguments[0].click();", submit)
except TimeoutException:
    print("Submit button was not clickable within the timeout.")

# Wait for 3 seconds
time.sleep(3)
# Close the browser
driver.close()