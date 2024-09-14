import time
from selenium import webdriver
from Funciones import Funciones_Globales  # Custom functions for Selenium actions

# Class for login functionalities
class Funciones_Login():

    # Constructor to initialize the WebDriver and navigate to the login page
    def __init__(self, driver):
        # Store the driver instance
        self.driver = driver
        # Initialize the global functions class
        self.f = Funciones_Globales(driver)
        # Create a new Edge browser instance
        self.driver = webdriver.Edge()
        # Navigate to the login page
        self.f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 1)
        # Maximize the browser window
        self.driver.maximize_window()
        # Wait for 2 seconds
        time.sleep(2)

    # Function to test login with invalid credentials (user not found)
    def L1(self, email, clave, message, t=.1):
        # Enter the email and password into their respective fields
        self.f.Texto_Mixto("id", "Email", email, t)
        self.f.Texto_Mixto("id", "Password", clave, t)
        # Click the 'Log in' button
        self.f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        # Capture the error message for invalid login
        er1 = self.f.SEX("//li[contains(.,'No customer account found')]")
        er1 = er1.text
        print(str(er1))  # Print the error message

        # Check if the error message matches the expected message
        if (er1 == message):
            print("El Error es Correcto")  # Correct error message
            self.driver.close()  # Close the browser
        else:
            print("No esta bien el error")  # Incorrect error message
            self.driver.close()  # Close the browser

    # Function to test login with invalid email format
    def L2(self, email, clave, message, t=.1):
        # Enter the email and password into their respective fields
        self.f.Texto_Mixto("id", "Email", email, t)
        self.f.Texto_Mixto("id", "Password", clave, t)
        # Click the 'Log in' button
        self.f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        # Capture the error message for invalid email format
        e1 = self.f.SEX("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        print(e1)  # Print the error message

        # Check if the error message matches the expected message
        if (e1 == message):
            print("Email no valido prueba Exitosa")  # Test passed, invalid email
            self.driver.close()  # Close the browser
        else:
            print("Prueba de Email no Exitosa")  # Test failed
            self.driver.close()  # Close the browser

    # Function to test a successful login
    def l3(self, email, clave, message, t=.1):
        # Navigate to the login page
        self.f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        # Enter the email and password into their respective fields
        self.f.Texto_Mixto("id", "Email", email, t)
        self.f.Texto_Mixto("id", "Password", clave, t)
        # Click the 'Log in' button
        self.f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        # Capture the text from the dashboard page
        e1 = self.f.SEX("//h1[contains(.,'Dashboard')]")
        e1 = e1.text
        print(e1)  # Print the dashboard message

        # Check if the dashboard message matches the expected message
        if (e1 == message):
            print("Login Exitoso")  # Test passed, login successful
            self.driver.close()  # Close the browser
        else:
            print("Prueba no exitosa")  # Test failed
            self.driver.close()  # Close the browser