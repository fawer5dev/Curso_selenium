# Import necessary libraries: time for sleep delays, unittest for creating test cases, and selenium for browser automation
import time
import unittest
from selenium import webdriver

# Define a variable 't' with a value of 0.2 seconds (used as a delay in the test)
t = 0.2


# Define a test class 'base_test' that inherits from unittest.TestCase, which provides test case structure
class base_test(unittest.TestCase):

    # The setUp method is called before each test case to initialize the browser
    def setUp(self):
        # Create a new instance of the Edge browser using Selenium WebDriver
        self.driver = webdriver.Edge()

    # Define the first test case named 'test1'
    def test1(self):
        # Assign the driver instance to a local variable for convenience
        driver = self.driver
        # Use Selenium to navigate to the OrangeHRM login page (a demo HR management site)
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        # Maximize the browser window to ensure all elements are visible and accessible
        driver.maximize_window()
        # Pause the execution for 't' seconds (0.2 seconds) to wait for the page to load
        time.sleep(t)

    # The tearDown method is called after each test case to clean up (close the browser)
    def tearDown(self):
        # Close the browser window to free up resources
        driver = self.driver
        driver.close()


# The main entry point for running the unittest framework
if __name__ == '__main__':
    # Run the test cases defined in the 'base_test' class
    unittest.main()