import requests
import json
import random
import string

def generate_random_filename():
    """Generate a random filename with .py extension"""
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_name}.py"

def call_rest_api(url):
    """Call a REST API and return the response"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None

def create_api_script(filename, api_data):
    """Create a Python script that displays API data"""
    script_content = f'''import json

# API response data
api_data = {json.dumps(api_data, indent=2)}

def display_data():
    """Display the API data"""
    print("API Data:")
    print(json.dumps(api_data, indent=2))

if __name__ == "__main__":
    display_data()
'''
    
    with open(filename, 'w') as file:
        file.write(script_content)
    
    print(f"API response saved in Python script: {filename}")

def main():
    # Call a public API
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    print(f"Calling API: {api_url}")
    
    data = call_rest_api(api_url)
    
    if data:
        # Generate a random filename
        filename = generate_random_filename()
        
        # Create a script with the API data
        create_api_script(filename, data)
        
        print(f"Created script: {filename}")
    else:
        print("Failed to retrieve API data")

if __name__ == "__main__":
    main()