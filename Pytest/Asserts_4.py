# Import pytest for writing test cases
import pytest

# Define a variable 't' with a value of 0.8 (this is unused in the current test functions)
t = 0.8

# Mark the function with 'run' to allow selective execution of this test
@pytest.mark.run
def test_validar_if():
    # Print a message to indicate the first test is running
    print("Primer test")
    # Simple test that always passes
    assert True

# Mark the function with 'run' to allow selective execution of this test
@pytest.mark.run
def test_dos():
    # Assign values to 'a' and 'b'
    a = 10
    b = 10
    # Test if 'a' and 'b' are equal, should pass
    assert a == b, "No son iguales"  # They are equal, so this should pass
    # Test if 'a' and 'b' are not equal, this will fail as they are equal
    assert a != b, "Son iguales"  # This will fail because 'a' is equal to 'b'
    # Test if 'a' is less than 'b', this will fail because 'a' is not less than 'b'
    assert a < b, "A no es menor que B"  # This will fail since 'a' is not less than 'b'
    # Test if 'a' is greater than 'b', this will fail because 'a' is not greater than 'b'
    assert a > b, "A no es menor que B"  # This will fail as 'a' is not greater than 'b'

# Mark the function with 'run' to allow selective execution of this test
@pytest.mark.run
def test_tres():
    # Assign values to 'a' and 'b'
    a = 5
    b = 10
    # Test if 'a' is equal to 'b', this will fail as 5 is not equal to 10
    assert a == b, "No son iguales"  # This will fail because 'a' is not equal to 'b'

# Mark the function with 'run' to allow selective execution of this test
@pytest.mark.run
def test_cuatro():
    # Assign values to 'a' and 'b'
    a = 15
    b = 10
    # Test if 'a' is greater than 'b', this will pass
    assert a > b, "a no es mayor que b"  # This will pass since 'a' is greater than 'b'

# Mark the function with 'run' to allow selective execution of this test
@pytest.mark.run
def test_cinco():
    # Assign a value to the variable 'nombre'
    nombre = "Rodri"
    # Test if 'nombre' is "Rodrigo", this will fail because 'nombre' is "Rodri"
    assert nombre == "Rodrigo", "El nombre no es Rodrigo"  # This will fail because 'nombre' is "Rodri"