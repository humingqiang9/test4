from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    """Return sample JSON data"""
    data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {
            "id": random.randint(1, 100),
            "name": "Sample Data",
            "timestamp": "2023-01-01T00:00:00Z"
        }
    }
    return jsonify(data)

@app.route('/api/random', methods=['GET'])
def get_random():
    """Return random JSON data"""
    data = {
        "random_string": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "random_number": random.randint(1, 1000),
        "is_active": random.choice([True, False])
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)