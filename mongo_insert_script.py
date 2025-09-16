import pymongo
import random
import string

def generate_random_string(length=6):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def insert_document():
    # Connect to MongoDB (assuming local instance)
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Access or create database
    db = client["test_database"]
    
    # Access or create collection
    collection = db["test_collection"]
    
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
    
    # Verify insertion by finding the document
    inserted_doc = collection.find_one({"_id": result.inserted_id})
    print(f"Retrieved document: {inserted_doc}")
    
    # Close the connection
    client.close()

if __name__ == "__main__":
    insert_document()