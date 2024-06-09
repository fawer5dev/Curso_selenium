import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..Funciones.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains

class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",2)
        f.Texto_Mixto("xpath","//INPUT[@data-v-1f99f73c='']", "Admin", 2)
        f.Texto_Mixto("xpath", "(//INPUT[@data-v-1f99f73c=''])[2]", "admin123", 2)
        f.Click_Mixto("xpath", "//BUTTON[@data-v-10d463b7='']", 5)        

        admin = driver.find_element(By.XPATH, "//SPAN[@data-v-7b563373=''][text()='Admin']").click()
        #sub1=driver.find_element(By.XPATH, "(//SPAN[@class='oxd-topbar-body-nav-tab-item'])[1]").click()
        #sub2=driver.find_element(By.ID, "//A[@href='#'][text()='Users']").click()

        time.sleep(3)
    
    # Close the browser
    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()