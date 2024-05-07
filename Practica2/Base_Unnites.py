# Import the necessary modules from Selenium
from selenium import webdriver
import time
import unittest

# Wait for x seconds
t = 2


class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()
        # Suspends execution for a given number of seconds
        time.sleep(t)

    # Define a test function
    def test1(self):
        driver = self.driver
        driver.get('')
        time.sleep(t)

    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()
