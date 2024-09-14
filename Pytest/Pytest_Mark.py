import pytest  # For structuring and running tests

t = .8  # Global time delay variable (used in pauses or timeouts in tests)

# Test case that prints "Test uno"
@pytest.mark.run  # Custom marker indicating this test should run
def test_uno():
    print("Test uno")  # Print message for identification

# Test case that prints "Test dos"
@pytest.mark.run  # Custom marker indicating this test should run
def test_dos():
    print("Test dos")  # Print message for identification

# Test case that prints "Test tres"
@pytest.mark.run  # Custom marker indicating this test should run
def test_tres():
    print("Test tres")  # Print message for identification

# Test case that prints "Test cuatro" (will not be executed)
@pytest.mark.notrun  # Custom marker indicating this test will not run
def test_cuatro():
    print("Test cuatro")  # Print message for identification (this won't be executed)

# Test case that prints "Test cinco"
@pytest.mark.run  # Custom marker indicating this test should run
def test_cinco():
    print("Test cinco")  # Print message for identification

# Test case that prints "Test seis"
@pytest.mark.run  # Custom marker indicating this test should run
def test_seis():
    print("Test seis")  # Print message for identification

# Test case that prints "Test siete" (will be skipped)
@pytest.mark.skip  # Built-in pytest marker to skip this test
def test_siete():
    print("Test siete")  # Print message for identification (this won't be executed)