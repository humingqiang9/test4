import json

# API response data
api_data = {
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

def display_data():
    """Display the API data"""
    print("API Data:")
    print(json.dumps(api_data, indent=2))

if __name__ == "__main__":
    display_data()
