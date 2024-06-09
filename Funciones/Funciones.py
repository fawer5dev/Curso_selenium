import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        # Navigate to a given URL and maximize the window
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: " + str(Url))
        t = time.sleep(Tiempo)
        return t
    
    def SEX (self, elemento):
        # Wait for the element to become visible, then scroll to it and find it by xpath
        val = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        # Find the element
        val = self.driver.find_element(By.XPATH, elemento)
        return val
    
    def SEI (self, elemento):
         # Wait for the element to become visible, then scroll to it and find it by ID
        val = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        # Find the element
        val = self.driver.find_element(By.ID, elemento)
        return val

    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if tipo == "xpath":
            try:
                val = self.SEX(selector)
                # Clear the text field and enter the desired text
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif tipo == "id":
            try:
                val = self.SEI(selector)
                # Clear the text field and enter the desired text
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Click_Mixto(self, tipo, selector, tiempo):
        if tipo == "xpath":
            try:
                val = self.SEX(selector)
                val.click()
                print("Dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif tipo == "id":
            try:
                val = self.SEI(selector)
                val.click()
                print("Dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    # Define a function to print a message when the test is finished
    def Salida(self):
        print("Se termina la prueba Exitosamente")

    # Define a function to print a message when the test is finished
    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            val = self.SEX(dato)
            # Create a Select object
            val = Select(val)
            # Select the option based on the input type
            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)
            # Print a message with the selected option
            print("El campo Seleccionado es {} ".format(dato))
            # Sleep for the input time
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t

    def Select_ID_Type(self, id, tipo, dato, tiempo):
        try:
            val = self.SEI(dato)
            # Create a Select object
            val = Select(val)
            # Select the option based on the input type
            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)
            print("El campo Seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            val = self.SEX(ruta)
            # Send the file path to the element
            val.send_keys(ruta)
            # Print a message indicating the image has been uploaded
            print("Se carga la imagen {} ".format(ruta))
            # Pause for the specified amount of time
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            # Print an error message if the element could not be found
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t

    def Upload_ID(self, id, ruta, tiempo):
        try:
            val = self.SEI(ruta)
            # Send the file path to the element
            val.send_keys(ruta)
            # Print a message indicating the image has been uploaded
            print("Se carga la imagen {} ".format(ruta))
            # Pause for the specified amount of time
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            # Print an error message if the element could not be found
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    def Check_Xpath(self, xpath, tiempo):
        try:
            val = self.SEX(xpath)
            # Click the element
            val.click()
            # Print a message indicating the element has been clicked
            print("Click en el elemento {} ".format(xpath))
            # Pause for the specified amount of time
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            # Print an error message if the element could not be found
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)
            return t

    def Check_ID(self, id, tiempo):
        try:
            val = self.SEI(id)
            # Click the element
            val.click()
            # Print a message indicating the element has been clicked
            print("Click en el elemento {} ".format(id))
            # Pause for the specified amount of time
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            # Print an error message if the element could not be found
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t

    # Define a method named Check_Xpath_Multiples that takes in a variable
    # tiempo and an unknown number of arguments with the *args parameter
    def Check_Xpath_Multiples(self, tiempo, *args):
        try:
            # Loop through each argument in args
            for num in args:
                val = self.SEX(num)
                # Click on the element
                val.click()
                # Print a message indicating which element was clicked
                print("Click en el elemento {} ".format(num))
                # Pause for tiempo seconds
                t = time.sleep(tiempo)
                # Return the value of t
                return t
        # Catch a TimeoutException
        except TimeoutException as ex:
            # Loop through each argument in args
            for num in args:
                # Print the error message for the exception
                print(ex.msg)
                # Print a message indicating that the element specified by num was not found
                print("No se encontro el Elemento" + num)

    # Define a method named Existe that takes in a variable tipo, a selector, and a tiempo
    def Existe(self, tipo, selector, tiempo):
        # If tipo is "xpath"
        if tipo == "xpath":
            try:
                val = self.SEX(selector)
                # Print a message indicating that the element exists
                print("El elemento  {} -> existe ".format(selector))
                # Pause for tiempo seconds
                t = time.sleep(tiempo)
                # Return the string "Existe"
                return "Existe"
            # Catch a TimeoutException
            except TimeoutException as ex:
                # Print the error message for the exception
                print(ex.msg)
                # Print a message indicating that the element specified by selector was not found
                print("No se encontro el Elemento" + selector)
                # Return the string "No Existe"
                return "No Existe"
        # If tipo is "id"
        elif tipo == "id":
            try:
                val = self.SEI(selector)
                # Print a message indicating that the element exists
                print("El elemento  {} -> existe ".format(selector))
                # Pause for tiempo seconds
                t = time.sleep(tiempo)
                # Return the string "Existe"
                return "Existe"
            # Catch a TimeoutException
            except TimeoutException as ex:
                # Print the error message for the exception
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"
    
    def Mouse_Derecho(self, tipo, selector, tiempo=.2):
        # If tipo is "xpath"
        if tipo == "xpath":
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Dando click Derecho en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        # If tipo is "id"
        elif tipo == "id":
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                val.click()
                print("Dando click Derecho en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t