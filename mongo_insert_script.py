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
    # Connect to MongoDB (assuming local instance)
    client = MongoClient('mongodb://localhost:27017/')
    
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

def save_script_to_file(filename):
    """Save this script to a file with the given name"""
    script_content = '''
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
    # Connect to MongoDB (assuming local instance)
    client = MongoClient('mongodb://localhost:27017/')
    
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

if __name__ == "__main__":
    # Insert document
    inserted_doc = insert_document()
    print("Inserted document:", inserted_doc)
    
    # Generate random filename
    filename = generate_random_filename()
    print(f"Saving script to: {filename}")
    
    # Save script to file
    with open(__file__, 'r') as source_file:
        content = source_file.read()
    
    with open(filename, 'w') as target_file:
        target_file.write(content)
    
    print("Script saved successfully!")
'''

    with open(filename, 'w') as file:
        file.write(script_content)

if __name__ == "__main__":
    # Insert document
    inserted_doc = insert_document()
    print("Inserted document:", inserted_doc)
    
    # Generate random filename
    filename = generate_random_filename()
    print(f"Saving script to: {filename}")
    
    # Save script to file
    save_script_to_file(filename)
    print("Script saved successfully!")