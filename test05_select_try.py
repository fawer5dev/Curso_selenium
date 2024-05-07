# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time


# Create a Edge browser instance
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()
t=2
# Wait for x seconds
time.sleep(t)
driver.implicitly_wait(15)

# Navigate to the module page on DemoQA
driver.get('https://demoqa.com/select-menu')

# Find the SELECT MENU with the attribute CLASS_NAME and Select it.
try:
    groupSel = driver.find_element(By.XPATH, "//div[contains(@class, 'css-2b097c-container')]").click();
    #gs = Select(groupSel)
    #gs.select_by_visible_text("Group 1, option 2")
    #gs.select_by_value(str('Group 1, option 2'))
    time.sleep(t)
    driver.quit()
except TimeoutException as ex:
    print(ex.msg + "ERROR TIMEOUT ")
    driver.close()