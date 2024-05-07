# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# Wait for x seconds
t = 2


class base_test(unittest.TestCase):
    # Define general functions
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()

    # Define a test function
    def test_login1(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        # Find the username input field and enter a valid email
        driver.find_element(By.XPATH, "//INPUT[@id='user-name']").send_keys("xxx@gmail.com")
        # Find the password input field and enter a valid password
        driver.find_element(By.XPATH, "//INPUT[@id='password']").send_keys("admin123")
        # Find the login button and click on it
        driver.find_element(By.XPATH, "//INPUT[@id='login-button']").click()
        # Find the error message and get its text
        error = driver.find_element(By.XPATH, "//H3[@data-test='error']").text
        # Check if the error message is the expected one
        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos")
            print("Prueba 1 OK")
        # Wait for 2 seconds
        time.sleep(t)

    def test_login2(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        # Find the username input field and leave it empty
        driver.find_element(By.XPATH, "//INPUT[@id='user-name']").send_keys("")
        # Find the password input field and enter a valid password
        driver.find_element(By.XPATH, "//INPUT[@id='password']").send_keys("admin123")
        # Find the login button and click on it
        driver.find_element(By.XPATH, "//INPUT[@id='login-button']").click()
        # Find the error message and get its text
        error = driver.find_element(By.XPATH, "//H3[@data-test='error']").text
        # Check if the error message is the expected one
        if error == "Epic sadface: Username is required":
            print("Falta el nombre")
            print("Prueba 2 OK")
        # Wait for 2 seconds
        time.sleep(t)

    def test_login3(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        # Find the username input field and enter a valid email
        driver.find_element(By.XPATH, "//INPUT[@id='user-name']").send_keys("xxx@gmail.com")
        # Find the password input field and leave it empty
        driver.find_element(By.XPATH, "//INPUT[@id='password']").send_keys("")
        # Find the login button and click on it
        driver.find_element(By.XPATH, "//INPUT[@id='login-button']").click()
        # Find the error message and get its text
        error = driver.find_element(By.XPATH, "//H3[@data-test='error']").text
        # Check if the error message is the expected one
        if error == "Epic sadface: Password is required":
            print("Falta el password")
            print("Prueba 3 OK")
        # Wait for 2 seconds
        time.sleep(t)

    def test_login4(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        # Find the username input and send empty value
        driver.find_element(By.XPATH, "//INPUT[@id='user-name']").send_keys("")
        # Find the password input and send empty value
        driver.find_element(By.XPATH, "//INPUT[@id='password']").send_keys("")
        # Find the login button and click it
        driver.find_element(By.XPATH, "//INPUT[@id='login-button']").click()
        # Find the error message element and check if it matches the expected message
        error = driver.find_element(By.XPATH, "//H3[@data-test='error']").text
        if error == "Epic sadface: Username is required":
            # Print a message indicating that the test passed
            print("Falta ambos campos")
            print("Prueba 4 Pendiente")
        # Wait for 2 seconds
        time.sleep(t)

    def test_login5(self):
        # Initialize driver and navigate to website
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        # Enter valid username and invalid password and attempt login
        driver.find_element(By.XPATH, "//INPUT[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//INPUT[@id='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//INPUT[@id='login-button']").click()
        # Check if error message is displayed
        error = driver.find_element(By.XPATH, "//H3[@data-test='error']").text
        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Usuario o Contraseña incorrecta")
            print("Prueba 5 OK")
        # Wait for 2 seconds
        time.sleep(t)

    def test_login6(self):
        # Initialize driver and navigate to website
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        # Enter valid username and valid password and attempt login
        driver.find_element(By.XPATH, "//INPUT[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//INPUT[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//INPUT[@id='login-button']").click()
        # Check if page with app logo is displayed
        element = driver.find_element(By.XPATH, "//DIV[@class='app_logo'][text()='Swag Labs']")
        element.is_displayed()
        # Print success message
        print("Acceso Correcto")
        print("Prueba 6 OK")
        # Wait for x seconds
        time.sleep(t)

    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()
