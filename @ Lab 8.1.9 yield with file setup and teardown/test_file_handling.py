import pytest
import os
from file_handler import FileHandler

# Define a fixture to set up and tear down a temporary file
@pytest.fixture
def temp_file(tmpdir):
    
    # Please open a tempory file with its name "filename"
    filename = os.path.join(tmpdir, 'test_file.txt')
    print(filename)
    # This is where the test function runs
    yield filename
    
    # Please close the tempory file and remove it from the file systems
    if os.path.exists(filename):
        os.remove(filename)        

# Test function that uses the temp_file fixture
def test_file_handling(temp_file):
    # Arrange: Write content to the temporary file
    handler = FileHandler()
    handler.write_file(temp_file, "Hello, pytest!")

    # Act: Read content from the file
    content = handler.read_file(temp_file)

    # Assert the result
    assert content == "Hello, pytest!"

if __name__ == "_main_":
    pytest.main()