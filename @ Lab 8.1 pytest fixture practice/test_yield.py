import pytest

# Define a fixture that sets up some resources
@pytest.fixture
def setup_teardown_example():

    print("\nSetting up resources...")
    # Code executed before the test function
    # This can be used to set up resources, like opening a file or database connection

    yield    #This is where the test function runs

    # Code executed after the test function
    print("\nTearing down resources...")
    # This can be used to perform cleanup, like closing a file or database connection

# Test function that uses the setup_teardown_example fixture
def test_example_with_setup_teardown(setup_teardown_example):
    print(" Running test function...")
    # Test logic here

#if _name_ == "_main_":
# — pytest.main()