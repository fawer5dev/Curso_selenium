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
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons", t)

        elemento = driver.find_element(By.ID, "doubleClickBtn")

        act = ActionChains(driver)
        act.double_click(elemento).perform()

        time.sleep(4)
    
    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()