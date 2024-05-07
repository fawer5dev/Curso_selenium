# Import necessary libraries
import time
import unittest
from Funciones_Ex import *
from selenium import webdriver
from Funciones.Funciones import Funciones_Globales

# Wait for x seconds
tg = .2


# Create a base test class
class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Microsoft Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the browser window
        self.driver.maximize_window()

    def test1(self):
        # Get the driver instance
        driver = self.driver
        # Create instances of custom functions
        f = Funciones_Globales(driver)
        fe = Funexcel(driver)

        # Navigate to the specified URL
        f.Navegar("https://demoqa.com/text-box", tg)

        # Define the path to the Excel file and get the number of rows
        ruta = "E://Mi PC//Programacion//Python//Selenium-Course//Excel//Datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")

        # Loop through rows in the Excel file
        for r in range(2, filas + 1):
            # Read data from Excel
            nombre = fe.readData(ruta, "Hoja1", r, 1)
            email = fe.readData(ruta, "Hoja1", r, 2)
            dir1 = fe.readData(ruta, "Hoja1", r, 3)
            dir2 = fe.readData(ruta, "Hoja1", r, 4)

            # Enter data into text fields and submit
            f.Texto_Mixto("id", "userName", nombre, tg)
            f.Texto_Mixto("id", "userEmail", email, tg)
            f.Texto_Mixto("id", "currentAddress", dir1, tg)
            f.Texto_Mixto("id", "permanentAddress", dir2, tg)
            f.Click_Mixto("id", "submit", tg)

            # Check if the element with id "name" exists
            e = f.Existe("id", "name", tg)

            if e == "Existe":
                print("El elemento se insertó correctamente")
                fe.writeData(ruta, "Hoja1", r, 5, "Insertado")
            else:
                print("No se insertó")
                fe.writeData(ruta, "Hoja1", r, 5, "Error")

    def tearDown(self):
        # Close the browser window
        driver = self.driver
        driver.close()


# Entry point for the script
if __name__ == '__main__':
    unittest.main()
