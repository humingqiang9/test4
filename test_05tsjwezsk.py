from selenium import webdriver
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
