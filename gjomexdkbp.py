import requests
from bs4 import BeautifulSoup

def scrape_page_title(url):
    """Scrape the title of a webpage"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title')
        return title.text.strip() if title else "No title found"
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def main():
    # Example URLs to scrape
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    
    print("Scraping page titles...")
    for url in urls:
        title = scrape_page_title(url)
        print(f"{url} - {title}")

if __name__ == "__main__":
    main()
