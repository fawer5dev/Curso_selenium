import time
from selenium import webdriver
from selenium.webdriver import Keys
from Funciones import Funciones_Globales
from selenium.webdriver.common.by import By

t = 1  # Time delay variable used in the custom functions
driver = ""  # Global variable for the webdriver instance
f = ""  # Global variable for the function instance


# Setup function to initialize the driver and the webpage
def setup_function(function):
    global driver
    # Create a new Edge browser instance (can be switched to Chrome or others)
    # driver = webdriver.Chrome()  # Uncomment to use Chrome
    driver = webdriver.Edge()  # Currently using Microsoft Edge browser

    # Maximize the browser window to full screen
    driver.maximize_window()

    # Navigate to the login page of the application
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

    # Initialize the custom global functions class with the driver instance
    f = Funciones_Globales(driver)

    # Perform login by entering credentials
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)  # Enter email
    f.Texto_Mixto("id", "Password", "admin", t)  # Enter password
    f.Click_Mixto("xpath", "//BUTTON[@type='submit'][text()='Log in']", t)  # Click on the login button

    # Set an implicit wait for elements to be available
    driver.implicitly_wait(20)

# Teardown function to clean up after tests
def teardown_function(function):
    print("Fin de los tests")  # Print a message indicating the tests are finished
    driver.close()  # Close the browser window


# First test case - Search for a product
def test_uno():
    # Click login button again (probably redundant if already logged in)
    f.Click_Mixto("xpath", "//BUTTON[@type='submit'][text()='Log in']", t)

    # Navigate to the 'Catalog' section
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)

    # Navigate to the 'Products' section within Catalog
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)

    # Enter the search term 'computer' in the product search field
    f.Texto_Mixto("xpath", "//INPUT[@id='SearchProductName']", "computer", t)

    # Click the search button to perform the search
    f.Click_Mixto("xpath", "//BUTTON[@id='search-products']", t)


# Second test case - Add a new product
def test_dos():
    f = Funciones_Globales(driver)  # Re-initialize the function handler

    # Navigate to 'Catalog' section
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)

    # Navigate to 'Products' section
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)

    # Click on 'Add new product' button
    f.Click_Mixto("xpath", "//a[@href='/Admin/Product/Create']", t)

    # Enter the product name as 'Laptop Dell'
    f.Texto_Mixto("xpath", "//input[@id='Name']", "Laptop Dell", t)

    # Enter a short description of the product
    f.Texto_Mixto("xpath", "//textarea[contains(@id,'ShortDescription')]", "Laptop modelo nuevo tipo dell", t)

    # Open the file menu within the product description editor
    f.Click_Mixto("xpath", "//span[@class='tox-mbtn__select-label'][contains(.,'File')]", t)

    # Select 'New document' option from the file menu
    f.Click_Mixto("xpath", "//div[@class='tox-collection__item-label'][contains(.,'New document')]", t)

    # Switch to the iframe that contains the text editor
    driver.switch_to.frame(0)

    # Enter a detailed description inside the editor and simulate pressing TAB + some numeric input
    driver.find_element(By.ID, "tinymce").send_keys("Descripción Larga" + Keys.TAB + "34567")

    # Pause the execution for 4 seconds to allow interactions to complete
    time.sleep(4)