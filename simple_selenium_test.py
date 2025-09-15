from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def main():
    # Set up Firefox options for headless mode
    options = Options()
    options.add_argument("--headless")
    
    # Initialize the Firefox driver
    driver = webdriver.Firefox(options=options)
    
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
    main()