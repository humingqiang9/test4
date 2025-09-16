import requests
import json
import random
import string
import os
import sys

def generate_random_filename():
    """Generate a random filename with .py extension"""
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"api_script_{random_chars}.py"

def call_rest_api(url):
    """Call a REST API and return the response"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None

def save_script_with_random_name():
    """Save a copy of this script with a random filename"""
    current_script = sys.argv[0]
    random_name = generate_random_filename()
    
    # Copy the current script to a new file with random name
    with open(current_script, 'r') as original:
        with open(random_name, 'w') as copy:
            copy.write(original.read())
    
    print(f"Script copied to: {random_name}")
    return random_name

def main():
    # Save a copy of this script with a random name
    random_filename = save_script_with_random_name()
    
    # Example API endpoint (JSONPlaceholder is a free testing API)
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    
    print(f"Calling REST API: {api_url}")
    data = call_rest_api(api_url)
    
    if data:
        print("API Response:")
        print(json.dumps(data, indent=2))
    else:
        print("Failed to retrieve data from API")

if __name__ == "__main__":
    main()