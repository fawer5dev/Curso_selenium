import pytest

# Time delay variable (used for pauses or timing in tests)
t = .5

# Fixture for setting up the login process for system one
@pytest.fixture(scope='module')  # Scope is 'module', meaning this fixture is run once per module
def setup_login_uno():
    # This code runs before the tests that use this fixture
    print("Empezando el login del sistema uno")
    yield  # Allows the test to run
    # This code runs after the tests that use this fixture have completed
    print("Saliendo del sistema prueba ok")


# Fixture for setting up the tests for system two
@pytest.fixture(scope='module')  # Scope is 'module', runs once per module
def setup_login_dos():
    # This code runs before the tests that use this fixture
    print("Empezando las pruebas del sistema dos")
    yield  # Allows the test to run
    # This code runs after the tests that use this fixture have completed
    print("Fin de las pruebas del sistema dos")


# Test function that uses the 'setup_login_uno' fixture
def test_uno(setup_login_uno):
    # Test case for login system one
    print("##### empezando las pruebas del test uno##########")


# Test function that uses the 'setup_login_dos' fixture
def test_dos(setup_login_dos):
    # Test case for login system two
    print("Esto es para la prueba dos")


# Using 'setup_login_dos' fixture directly with the @mark.usefixtures decorator
@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    # Another test case for login system two
    print("Prueba tres del modulo login dos")