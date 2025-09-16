import requests
import json

# Test data
test_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello World"
}

# Send POST request
response = requests.post("http://localhost:8000/submit", 
                         headers={"Content-Type": "application/json"},
                         data=json.dumps(test_data))

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")