# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Define Class
class SeleniumExample:
    def __init__(self):
        # Create Edge browser instance
        self.driver = webdriver.Edge()

    def navigate_to_page(self):
        # Navigate to the module page on DemoQA
        self.driver.get('https://demoqa.com/select-menu')
        self.driver.maximize_window()

    def select_menu_by_class(self):
        # Find SELECT MENU by class name using XPath and Class parameter
        select_menu = self.driver.find_element(By.XPATH, "//div[contains(@class, 'css-2b097c-container')]").click();

        # Use Select class to work with the dropdown menu
        select = Select(select_menu)

        # Select an option by value
        select.select_by_value('Group 1, option 2')
        #select.select_by_value("Group 1, option 2")
        #select.select_by_index(2)

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


# Instantiate the class and call the methods
selenium_example = SeleniumExample()
selenium_example.navigate_to_page()
selenium_example.select_menu_by_class()
selenium_example.close_browser()