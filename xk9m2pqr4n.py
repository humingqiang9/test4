import requests
import json

def fetch_user_data(user_id):
    """Fetch user data from a REST API"""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    print("Fetching user data from REST API...")
    user_data = fetch_user_data(1)
    
    if user_data:
        print("User Information:")
        print(f"Name: {user_data['name']}")
        print(f"Email: {user_data['email']}")
        print(f"Phone: {user_data['phone']}")
    else:
        print("Failed to fetch user data")

if __name__ == "__main__":
    main()