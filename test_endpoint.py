import requests
import json
import os
import time

# Test data
test_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "This is a test message"
}

# Wait a moment for the server to start
time.sleep(2)

# Send POST request to the endpoint
try:
    response = requests.post("http://localhost:8000/submit", json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Check if file was created
    filename = response.json().get("filename")
    if filename and os.path.exists(filename):
        print(f"File {filename} was created successfully")
        with open(filename, "r") as f:
            saved_data = json.load(f)
            print(f"Saved data: {saved_data}")
        # Clean up test file
        os.remove(filename)
        print(f"Cleaned up test file: {filename}")
    else:
        print("File was not created")
        
except Exception as e:
    print(f"Error during test: {e}")