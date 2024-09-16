# Import pytest to use its testing functionalities
import pytest


# Define a custom pytest hook to modify or extend the behavior of test report generation
# The hook is marked as hookwrapper=True, meaning it can wrap around the default pytest behavior
# tryfirst=True ensures that this hook will run before any other hooks of the same type
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Capture the result of the test execution using 'yield' to pause the function and return control back to pytest
    outcome = yield

    # Retrieve the actual test result (pass/fail/skip) from the outcome object
    rep = outcome.get_result()

    # Use 'setattr' to dynamically set attributes on the 'item' object, which represents the test item
    # This will store the test result report (rep) for different phases (setup, call, teardown) with names like 'rep_setup', 'rep_call', 'rep_teardown'
    setattr(item, "rep_" + rep.when, rep)

    # Return the test result report (rep)
    return rep
