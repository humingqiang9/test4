import requests
import json
import random
import string

def generate_random_filename():
    """Generate a random filename with .py extension"""
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
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

def save_script_with_data(filename, data):
    """Save the API response data to a Python file"""
    script_content = f'''# API Response Data Script
import json

# Data retrieved from API
api_data = {json.dumps(data, indent=2)}

# Print the data
print("API Response:")
print(json.dumps(api_data, indent=2))
'''
    
    with open(filename, 'w') as f:
        f.write(script_content)
    
    print(f"Script saved as {filename}")

def main():
    # Example using JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    
    print(f"Calling REST API: {api_url}")
    data = call_rest_api(api_url)
    
    if data:
        filename = generate_random_filename()
        save_script_with_data(filename, data)
        print(f"Successfully created script with API data: {filename}")
    else:
        print("Failed to retrieve data from API")

if __name__ == "__main__":
    main()