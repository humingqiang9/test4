from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    """Return sample JSON data"""
    data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {
            "id": 123,
            "name": "Sample Data",
            "items": ["item1", "item2", "item3"]
        }
    }
    return jsonify(data)

@app.route('/', methods=['GET'])
def home():
    """Home route with simple message"""
    return jsonify({"message": "Flask API is running!", "status": "active"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')