# This function is called at the beginning of each test
def setup_function(function):
    # Print a message indicating the start of a test
    print("esto va al Inicio de cada test")

# This function is called at the end of each test
def teardown_function(function):
    # Print a message indicating the end of a test
    print("esto va al final de cada test")

# First test case
def test_uno():
    # Print a message for Test Uno
    print("Test Uno")

# Second test case
def test_dos():
    # Print a message for Test Dos
    print("Test dos")

# Third test case
def test_tres():
    # Print a message for Test Tres
    print("Test tres")