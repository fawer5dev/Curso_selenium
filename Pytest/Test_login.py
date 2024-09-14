# Import the necessary modules from Selenium
import time
from selenium import webdriver
from Funciones import Funciones_Globales  # Custom functions for Selenium actions

def test_login1():
    # Create a new Edge browser instance (can switch to Chrome if needed)
    # driver = webdriver.Chrome()  # Uncomment to use Chrome
    driver = webdriver.Edge()  # Currently using Edge browser
    # Navigate to the login page of the application
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    # Maximize the browser window
    driver.maximize_window()
    # Initialize the custom global functions class with the driver instance
    f = Funciones_Globales(driver)
    # Enter an empty string as the email (to test the validation)
    f.Texto_Mixto("id", "Email", "", 2)
    # Enter the password as 'admin'
    f.Texto_Mixto("id", "Password", "admin", 2)
    # Click on the 'Log in' button
    f.Click_Mixto("xpath", "//BUTTON[@type='submit'][text()='Log in']", 2)
    # Capture the validation error message for the email field
    e1 = f.SEX("//SPAN[@id='Email-error']")
    e1 = e1.text  # Get the text of the error message
    print(e1)  # Print the error message to the console

    # Check if the error message matches the expected validation message
    if (e1 == "Please enter your email"):
        print("Prueba Exitosa")  # Test passes if validation message is correct
    else:
        print("Prueba con errores")  # Test fails if validation message is incorrect

    # Wait for 2 seconds before closing the browser
    time.sleep(2)
    # Close the browser
    driver.close()