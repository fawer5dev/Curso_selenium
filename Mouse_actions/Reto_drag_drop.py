import unittest
from selenium import webdriver
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
        # sets an implicit wait of x seconds for the WebDriver instance.
        driver.implicitly_wait(5)
        # Create an instance of the Funciones_Globales class
        f = Funciones_Globales(driver)
        # Call the Navegar method of the Funciones_Globales class to navigate to the specified URL
        f.Navegar("https://jqueryui.com/draggable/", 2)
        # Call the Mouse_DragDrop method of the Funciones_Globales class to perform a drag and drop operation
        f.Mouse_DragDropXY("id", "draggable", "150", "120", 3)
    
    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()