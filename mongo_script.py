import random
import string
from pymongo import MongoClient

def generate_random_filename():
    """Generate a random filename with .py extension"""
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(10))
    return f"{random_name}.py"

def insert_document():
    """Insert a document into MongoDB"""
    try:
        # Connect to MongoDB (assuming local instance)
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
        
        # Access database and collection
        db = client['test_database']
        collection = db['test_collection']
        
        # Document to insert
        document = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30,
            "city": "New York"
        }
        
        # Insert document
        result = collection.insert_one(document)
        print(f"Document inserted with ID: {result.inserted_id}")
        
        # Close connection
        client.close()
        
        return document
    except Exception as e:
        print(f"Could not connect to MongoDB: {e}")
        print("Note: This script requires a running MongoDB instance to insert documents.")
        return None

if __name__ == "__main__":
    # Generate random filename first
    filename = generate_random_filename()
    print(f"Script will be saved to: {filename}")
    
    # Try to insert document
    inserted_doc = insert_document()
    if inserted_doc:
        print("Inserted document:", inserted_doc)
    else:
        print("Document insertion skipped due to MongoDB connection issue.")
    
    # Save this script to the randomly named file
    with open(__file__, 'r') as source_file:
        content = source_file.read()
    
    with open(filename, 'w') as target_file:
        target_file.write(content)
    
    print(f"Script saved successfully to {filename}!")