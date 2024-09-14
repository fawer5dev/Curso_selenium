import pytest  # For structuring and running tests
from selenium import webdriver  # To control the browser
from Funciones import Funciones_Globales  # Custom class for common Selenium functions

t = .8  # Time delay variable used in tests

# Function to provide login credentials (a data set with different user and password combinations)
def get_Data():
    return [
        ("rodrigo", "1234"),  # Test case 1: User 'rodrigo' with password '1234'
        ("juan", "1233234"),  # Test case 2: User 'juan' with password '1233234'
        ("pedro", "12232334"),  # Test case 3: User 'pedro' with password '12232334'
        ("erika", "1234232"),  # Test case 4: User 'erika' with password '1234232'
        ("carlos", "1234sdf"),  # Test case 5: User 'carlos' with password '1234sdf'
        ("Admin", "admin123")  # Test case 6: Admin login with password 'admin123'
    ]

# Parametrized test case using the 'login' marker, running the test with different sets of data from get_Data()
@pytest.mark.login  # Custom marker to identify this test case as a login test
@pytest.mark.parametrize("user, clave",
                         get_Data())  # Parametrize the test case with different user and password combinations
def test_login(user, clave):
    global driver  # Make driver accessible throughout the test
    # Create a new Edge browser instance (can be switched to Chrome or others)
    # driver = webdriver.Chrome()  # Uncomment to use Chrome
    driver = webdriver.Edge()  # Currently using Microsoft Edge browser
    # Navigate to the login page of the OrangeHRM demo site
    driver.get("https://opensource-demo.orangehrmlive.com/")
    # Maximize the browser window for better visibility and interactions
    driver.maximize_window()
    # Set an implicit wait to wait for elements to appear before throwing errors
    driver.implicitly_wait(20)
    # Create an instance of the custom Selenium helper class Funciones_Globales
    f = Funciones_Globales(driver)
    # Enter the username and password for login
    f.Texto_Mixto("xpath", "//INPUT[@data-v-1f99f73c='']", user, t)
    f.Texto_Mixto("xpath", "(//INPUT[@data-v-1f99f73c=''])[2]", clave, t)
    # Click the 'Log in' button
    f.Click_Mixto("xpath", "//BUTTON[@data-v-10d463b7='']", t)
    # Print a message indicating successful entry into the system
    print("Entrando al sistema")

# Teardown function to run after each test to close the browser
def teardown_function():
    print("Salida del test")  # Print a message indicating the end of the test
    driver.close()  # Close the browser window