import random
import string
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def generate_random_string(length=10):
    """Generate a random string of specified length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def insert_document():
    # Connect to MongoDB (assuming local instance)
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
    
    try:
        # Check if MongoDB is accessible
        client.admin.command('ping')
        print("Connected to MongoDB successfully")
        
        # Access database and collection
        db = client['test_database']
        collection = db['test_collection']
        
        # Create a sample document
        document = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30,
            "random_id": generate_random_string(8)
        }
        
        # Insert the document
        result = collection.insert_one(document)
        
        print(f"Document inserted with ID: {result.inserted_id}")
        print(f"Inserted document: {document}")
        
    except ConnectionFailure:
        print("Failed to connect to MongoDB. The script is designed to insert a document into a MongoDB collection.")
        print("Sample document that would be inserted:")
        document = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30,
            "random_id": generate_random_string(8)
        }
        print(document)
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    insert_document()