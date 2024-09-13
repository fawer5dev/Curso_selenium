# Import the necessary modules from Selenium
import time
from selenium import webdriver
from Funciones import Funciones_Globales

def test_login1():
    # Create a Edge browser instance
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()

    # Maximize the window
    driver.maximize_window()

    # Navigate to the module page on DemoQA
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

    f = Funciones_Globales(driver)
    f.Texto_Mixto("id","Email", "", 2)
    f.Texto_Mixto("id", "Password", "admin", 2)
    f.Click_Mixto("xpath","//BUTTON[@type='submit'][text()='Log in']", 2)

    e1=f.SEX("//SPAN[@id='Email-error']")
    e1=e1.text
    print(e1)

    if (e1=="Please enter your email"):
        print("Prueba Exitosa")
    else:
        print("Prueba con errores")

    # Wait for x seconds
    time.sleep(2)

    # Close the browser
    driver.close()