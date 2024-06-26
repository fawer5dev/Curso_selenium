import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ..Funciones.Funciones import Funciones_Globales

class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()

    def test1(self):
        # Get the driver instance from the base_test class
        driver = self.driver
         # Create an instance of the Funciones_Globales class
        f = Funciones_Globales(driver)
        # Call the Navegar method of the Funciones_Globales class to navigate to the specified URL
        f.Navegar("https://demoqa.com/buttons",2)
        # Call the Mouse_Derecho method of the Funciones_Globales class to perform a right click operation
        f.Mouse_Derecho("id", "rightClickBtn", 2)
    
    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()