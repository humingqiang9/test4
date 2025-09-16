import requests
from bs4 import BeautifulSoup
import random
import string

def generate_random_filename():
    """Generate a random filename with .py extension"""
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(10))
    return f"{random_name}.py"

def scrape_page_title(url):
    """Scrape the title of a webpage"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return title.strip()
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def main():
    # Example URLs to scrape
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    
    print("Scraping page titles...")
    results = {}
    
    for url in urls:
        title = scrape_page_title(url)
        results[url] = title
        print(f"{url}: {title}")
    
    # Generate random filename
    filename = generate_random_filename()
    
    # Save results to file
    with open(filename, 'w') as f:
        f.write("# Scraped Page Titles\n\n")
        for url, title in results.items():
            f.write(f"{url}: {title}\n")
    
    print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    main()