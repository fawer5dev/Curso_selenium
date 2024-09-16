# Import the pytest library for writing test cases and Selenium for browser automation
import pytest
from selenium import webdriver
from Funciones import Funciones_Globales  # Import custom functions for Selenium operations

# Define a variable 't' with a value of 0.8, likely used as a delay time in the helper functions
t = 0.8


# Define a fixture for setting up the login process, scope is set to 'module' meaning it runs once per module
@pytest.fixture(scope='module')
def setup_Login():
    # Make the driver and helper functions globally accessible throughout the tests
    global driver, f
    # Initialize the Edge WebDriver (can switch to other browsers like Chrome if needed)
    # driver = webdriver.Chrome()  # Uncomment to use Chrome
    driver = webdriver.Edge()  # Currently using Microsoft Edge browser
    # Navigate to the OrangeHRM login page (a demo website for HR management)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    # Maximize the browser window to ensure all elements are fully visible
    driver.maximize_window()
    # Implicitly wait for elements to appear for up to 20 seconds before throwing an error
    driver.implicitly_wait(20)
    # Create an instance of a helper class 'Funciones_Globales' which contains reusable functions for Selenium
    f = Funciones_Globales(driver)
    # Use a custom function 'Texto_Mixto' to enter the username "Admin" into the username input field
    f.Texto_Mixto("xpath", "//INPUT[@data-v-1f99f73c='']", "Admin", t)
    # Use the same function to enter the password "admin123" into the password field
    f.Texto_Mixto("xpath", "(//INPUT[@data-v-1f99f73c=''])[2]", "admin123", t)
    # Click the 'Log in' button using another custom function 'Click_Mixto'
    f.Click_Mixto("xpath", "//BUTTON[@data-v-10d463b7='']", t)


# Define a teardown function that runs after all tests to close the browser
def teardown_function():
    # Print a message to indicate the end of the tests
    print("Fin de todos los Test")
    # Close the browser instance to free up resources
    driver.close()


# Mark the test with 'login' to allow for selective test execution
# Also, apply the 'setup_Login' fixture to ensure the login process is completed before the test runs
@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    # Get the text of the dashboard header element using a custom function 'SEX'
    etiqueta = f.SEX("//h1[contains(.,'Dashboard')]").text
    # Print the extracted text to the console
    print(etiqueta)

    # Check if the extracted text matches the expected text "Dashboa" (intentionally incorrect)
    if (etiqueta == "Dashboa"):
        # If the condition is met, print "Adentro" (Inside) and assert that it matches "Dashboard"
        print("Adentro")
        assert etiqueta == "Dashboard"
    else:
        # If the condition is not met, print "Afuera" (Outside) and raise an assertion error with a message
        print("Afuera")
        assert etiqueta == "Dashboa", "No estas en la pagina de inicio"  # Not on the dashboard page