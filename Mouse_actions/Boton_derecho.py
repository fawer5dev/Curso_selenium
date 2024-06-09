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
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons",2)
        f.Mouse_Derecho("id", "rightClickBtn", 2)
    
    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()