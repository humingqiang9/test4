import random
import string
import os

def generate_random_filename():
    """Generate a random filename with .py extension"""
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test_{random_chars}.py"

def create_selenium_test_file():
    # Generate a random filename
    filename = generate_random_filename()
    
    # Create the Selenium test code
    test_code = '''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google():
    # Initialize the driver (you'll need to set up the appropriate driver for your browser)
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
    
    try:
        # Open Google
        driver.get("https://www.google.com")
        
        # Wait for page to load
        time.sleep(3)
        
        # Verify we're on Google by checking the title
        assert "Google" in driver.title
        print("Successfully opened Google")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google()
'''
    
    # Write the code to the file
    with open(filename, 'w') as f:
        f.write(test_code)
    
    print(f"Selenium test file '{filename}' created successfully!")
    return filename

if __name__ == "__main__":
    create_selenium_test_file()