# Import the pytest library for writing test cases
import pytest

# Define a variable 't' with a value of 0.8 (this is unused in the current test function)
t = 0.8


# Mark the test case with a custom marker 'validarif'
@pytest.mark.validarif
def test_validar_if():
    # Define two strings for testing
    dato = "Ram"
    frase = "Dentro de las computadoras hay memoria Ram"

    # Assert that the string 'dato' is present within the string 'frase'
    # If not, display the message "El dato no esta dentro de la Frase"
    assert dato in frase, "El dato no esta dentro de la Frase"