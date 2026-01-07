from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import os
from pathlib import Path
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get('https://testpages.herokuapp.com/styled/file-upload-test.html')
    driver.maximize_window()

    file_input = wait.until(EC.presence_of_element_located((By.ID, "fileinput")))

    # prefer image from environment: set TEST_IMAGE=/full/path/to/image.png
    # otherwise use a path relative to this test file: `images/bicycle-g5335ffc14_1280.png`
    image_path = Path(os.environ.get('TEST_IMAGE') or Path(__file__).parent / 'images' / 'bicycle-g5335ffc14_1280.png')

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    file_input.send_keys(str(image_path))

    itsan = wait.until(EC.element_to_be_clickable((By.ID, "itsanimage")))
    try:
        itsan.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].scrollIntoView(true);", itsan)
        time.sleep(0.3)
        try:
            itsan.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", itsan)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
    submit.click()

    time.sleep(2)

except TimeoutException as ex:
    print("Timeout:", ex)
finally:
    driver.quit()