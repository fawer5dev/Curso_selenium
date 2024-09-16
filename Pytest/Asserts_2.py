# Import the pytest library for writing and executing test cases
import pytest

# Define a variable 't' with a value of 0.8 (this is unused in the current test function)
t = 0.8


# Mark the test case with a custom marker 'validarif'
@pytest.mark.validarif
def test_validar_if():
    # Define two variables 'a' and 'b' with values 20 and 25, respectively
    a = 20
    b = 25

    # Conditional statement to check if 'a' and 'b' are equal
    if (a == b):
        # If 'a' is equal to 'b', the test will pass with the message "Los datos son iguales"
        assert True, "Los datos son iguales"
    else:
        # If 'a' is not equal to 'b', the test will fail with the message "Los datos no son iguales"
        assert False, "Los datos no son iguales"