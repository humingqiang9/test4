#!/usr/bin/env python3
"""
Web Scraper for Page Titles
This script uses BeautifulSoup to scrape the title of a webpage.
"""

import requests
from bs4 import BeautifulSoup
import random
import string


def generate_random_filename(length=10):
    """Generate a random filename with .py extension"""
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(length))
    return random_name + ".py"


def scrape_page_title(url):
    """Scrape the title of a webpage"""
    try:
        # Send GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the title
        title = soup.title.string if soup.title else "No title found"
        return title.strip()
    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"
    except Exception as e:
        return f"Error parsing the webpage: {e}"


def main():
    # Example URL to scrape
    url = "https://www.python.org"
    
    print(f"Scraping title from: {url}")
    title = scrape_page_title(url)
    print(f"Page title: {title}")
    
    # Generate a random filename and save this script to it
    random_filename = generate_random_filename()
    print(f"\nSaving this script to: {random_filename}")
    
    # Read the current script
    with open(__file__, 'r') as f:
        script_content = f.read()
    
    # Write to the new random filename
    with open(random_filename, 'w') as f:
        f.write(script_content)
    
    print("Script saved successfully!")


if __name__ == "__main__":
    main()