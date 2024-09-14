import allure  # For reporting and attaching screenshots to reports
import pytest  # For structuring tests
import time  # To add delays where necessary

from allure_commons.types import AttachmentType  # For attaching files to allure reports
from selenium import webdriver  # For controlling the browser
from selenium.webdriver.common.keys import Keys  # For simulating keyboard key presses
from Funciones import Funciones_Globales  # Custom class for common Selenium functions
from selenium.webdriver.common.by import By  # For locating elements by different strategies

t = .8  # Global time delay variable (used in pauses or timeouts in tests)

# Fixture for logging screenshots on test failures
@pytest.fixture()
def log_on_failure(request):
    yield  # Test runs here
    item = request.node  # Captures the test item
    if item.rep_call.failed:  # If the test failed
        # Attach a screenshot to the report if the test failed
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

# Fixture for setting up login for system one (nopCommerce)
@pytest.fixture(scope='module')  # Module scope, runs once per module
def setup_login_uno():
    global driver, f  # Declare driver and f as global to use within the function
    # Create a new Edge browser instance (can be switched to Chrome or others)
    # driver = webdriver.Chrome()  # Uncomment to use Chrome
    driver = webdriver.Edge()  # Currently using Microsoft Edge browser
    # Navigate to the login page of the nopCommerce admin site
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    # Maximize the browser window
    driver.maximize_window()
    # Set an implicit wait of 20 seconds for elements to load
    driver.implicitly_wait(20)
    # Initialize the custom global functions class for browser actions
    f = Funciones_Globales(driver)
    # Enter the email and password for login
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    # Click the 'Log in' button
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Entrando al sistema")  # Log the login action
    yield  # Allows the test to run
    print("Salida del login uno")  # Log when exiting the system
    driver.close()  # Close the browser after the test finishes

# Fixture for setting up login for system two (OrangeHRM)
@pytest.fixture(scope='module')  # Module scope, runs once per module
def setup_Login_dos():
    global driver, f  # Declare driver and f as global to use within the function
    # Create a new Edge browser instance (can be switched to Chrome or others)
    # driver = webdriver.Chrome()  # Uncomment to use Chrome
    driver = webdriver.Edge()  # Currently using Microsoft Edge browser
    # Navigate to the OrangeHRM login page
    driver.get('https://opensource-demo.orangehrmlive.com/')
    # Maximize the browser window
    driver.maximize_window()
    # Set an implicit wait of 20 seconds for elements to load
    driver.implicitly_wait(20)
    # Initialize the custom global functions class for browser actions
    f = Funciones_Globales(driver)
    # Enter the username and password for login
    f.Texto_Mixto("xpath", "//INPUT[@data-v-1f99f73c='']", "Admin", t)
    f.Texto_Mixto("xpath", "(//INPUT[@data-v-1f99f73c=''])[2]", "admin123", t)
    # Click the 'Log in' button
    f.Click_Mixto("xpath", "//BUTTON[@data-v-10d463b7='']", t)
    print("Entrando al sistema")  # Log the login action
    yield  # Allows the test to run
    print("Salida del login dos")  # Log when exiting the system
    driver.close()  # Close the browser after the test finishes

# Test case for system one (nopCommerce)
@pytest.mark.usefixtures("log_on_failure")  # Attaches screenshots on failure
@pytest.mark.usefixtures("setup_login_uno")  # Uses the setup_login_uno fixture
def test_uno():
    print("Entrando el sistema uno")  # Log test start
    # Navigate to 'Customers' section and search for a customer named "Victoria"
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[2]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchFirstName')]", "victoria", t)
    # Attach a screenshot of the search for "Victoria" to the report
    allure.attach(driver.get_screenshot_as_png(), name="buscando_nombre", attachment_type=AttachmentType.PNG)
    # Click the 'Search' button
    f.Click_Mixto("xpath", "//button[contains(@id,'search-customers')]", t)
    # Attach a screenshot of the search results to the report
    allure.attach(driver.get_screenshot_as_png(), name="customers", attachment_type=AttachmentType.PNG)
    # Create a new customer with predefined details
    f.Click_Mixto("xpath", "//a[@href='/Admin/Customer/Create']", t)
    email = driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    # Enter email, password, first name, and last name
    email.send_keys("juan@gmail.com" + Keys.TAB + "12345" + Keys.TAB + "Juan" + Keys.TAB + "Perez")
    time.sleep(3)
    # Attach a screenshot of the new customer details to the report
    allure.attach(driver.get_screenshot_as_png(), name="datos", attachment_type=AttachmentType.PNG)
    # Select gender, date of birth, and attach the relevant screenshots
    f.Click_Mixto("xpath", "//input[contains(@id,'Gender_Male')]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'DateOfBirth')]", "2/20/2019", t)
    allure.attach(driver.get_screenshot_as_png(), name="fecha", attachment_type=AttachmentType.PNG)
    assert 1 == 2  # Intentionally failing the test for demonstration purposes
    driver.close()  # Close the browser

# Test case for system two (OrangeHRM)
@pytest.mark.usefixtures("log_on_failure")  # Attaches screenshots on failure
@pytest.mark.usefixtures("setup_Login_dos")  # Uses the setup_Login_dos fixture
def test_dos():
    print("Entrando el sistema dos")  # Log test start
    # Navigate to the 'Admin' section and user management
    f.Click_Mixto("xpath", "//b[contains(.,'Admin')]", t)
    f.Click_Mixto("xpath", "//a[contains(@id,'menu_admin_UserManagement')]", t)
    # Attach a screenshot of the Admin section to the report
    allure.attach(driver.get_screenshot_as_png(), name="Menu_admin", attachment_type=AttachmentType.PNG)
    # Search for a user named "Ananya Dash"
    f.Texto_Mixto("xpath", "//input[contains(@id,'searchSystemUser_userName')]", "ananya Dash", t)
    f.Click_Mixto("xpath", "//input[contains(@id,'searchBtn')]", t)
    # Attach a screenshot of the search results to the report
    allure.attach(driver.get_screenshot_as_png(), name="buscando", attachment_type=AttachmentType.PNG)
    # Click 'Add' button to add a new user
    f.Click_Mixto("xpath", "//input[contains(@id,'btnAdd')]", t)
    # Attach a screenshot of the 'Add User' section to the report
    allure.attach(driver.get_screenshot_as_png(), name="Agregando", attachment_type=AttachmentType.PNG)
    # Select a user role from a dropdown
    f.Select_Xpath_Type("//select[contains(@id,'systemUser_userType')]", "index", 0, t)
    assert 1 == 2  # Intentionally failing the test for demonstration purposes
    driver.close()  # Close the browser