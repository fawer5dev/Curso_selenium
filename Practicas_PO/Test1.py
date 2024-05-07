# Import the necessary modules from Selenium
import unittest
from selenium import webdriver
from Funciones.Funciones import Funciones_Globales

# Wait for x seconds
tg = .2


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
        f.Navegar("https://www.saucedemo.com/", tg)
        f.Texto_Mixto("id", "user-name", "standard_user", tg)
        f.Texto_Mixto("id", "password", "secret_sauce", tg)
        f.Click_Mixto("id", "login-button", tg)

    # Define a test function click a select with a text
    def test2(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/basic-html-form-test.html", tg)
        f.Select_Xpath_Type("//SELECT[@name='dropdown']", "text", "Drop Down Item 5", tg)

    # Define a test function upload a file
    def test3(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", tg)
        f.Upload_Xpath("//INPUT[@id='fileinput']",
                       "E://Mi PC//Programacion//Python//Selenium-Course//images//bicycle-g5335ffc14_1280.png", tg)

    # Define a test function with multiple checkbox
    def test4(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/basic-html-form-test.html", tg)
        for n in range(2,3):
            f.Check_Xpath_Multiples(tg, "(//INPUT[@type='checkbox'])["+str(n)+"]" )

    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()