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

def save_script_to_file(filename):
    """Save a sample API calling script to a file"""
    script_content = '''
import requests
import json

def call_api():
    """Example function to call a public API"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("API Response:")
        print(json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None

if __name__ == "__main__":
    call_api()
'''
    
    with open(filename, 'w') as file:
        file.write(script_content)
    
    print(f"Script saved to {filename}")

def main():
    # Generate a random filename
    filename = generate_random_filename()
    
    # Save the script
    save_script_to_file(filename)
    
    # Optionally, you can execute the script here
    # import subprocess
    # subprocess.run(['python', filename])

if __name__ == "__main__":
    main()