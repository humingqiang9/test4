#!/usr/bin/env python3
"""
Test script for Flask JSON route
"""
from flask import Flask, jsonify

# Create a simple Flask app with JSON route
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    """Return sample JSON data"""
    data = {
        'message': 'Hello, World!',
        'status': 'success',
        'data': {
            'id': 123,
            'name': 'Sample Data',
            'items': ['item1', 'item2', 'item3']
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    # Test the function directly
    with app.test_request_context('/api/data'):
        response = get_data()
        print("Function test:")
        print(f"Status: {response.status_code}")
        print(f"Data: {response.get_json()}")
        
    # Test with test client
    app.testing = True
    with app.test_client() as c:
        response = c.get('/api/data')
        print("\nClient test:")
        print(f"Status: {response.status_code}")
        print(f"Data: {response.get_json()}")