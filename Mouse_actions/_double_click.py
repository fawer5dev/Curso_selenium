# Import the necessary modules from Selenium
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Funciones.Funciones import Funciones_Globales
import time

# Wait for x seconds
t = 2


class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()

    # Define a test function sending text
    def test1(self):
        # Get the driver instance from the base_test class
        driver = self.driver
        # Create an instance of the Funciones_Globales class
        f = Funciones_Globales(driver)
        # Use the Navegar method of the Funciones_Globales class to navigate to the specified URL
        f.Navegar("https://demoqa.com/buttons", t)
        # Find the element with the ID "doubleClickBtn"
        elemento = driver.find_element(By.ID, "doubleClickBtn")
        # Create an ActionChains object to perform actions on the element
        act = ActionChains(driver)
        # Perform a double click action on the element
        act.double_click(elemento).perform()
        # Pause the execution for 4 seconds
        time.sleep(4)
    
    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()