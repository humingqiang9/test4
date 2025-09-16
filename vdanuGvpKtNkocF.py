import pymongo
import random
import string

def generate_random_string(length=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def main():
    # Connect to MongoDB (assuming it's running locally on default port)
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        
        # Create/access a database
        db = client["test_database"]
        
        # Create/access a collection
        collection = db["test_collection"]
        
        # Create a sample document
        document = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30,
            "random_id": generate_random_string()
        }
        
        # Insert the document
        result = collection.insert_one(document)
        
        print(f"Document inserted with ID: {result.inserted_id}")
        print(f"Document content: {document}")
        
        # Verify the document was inserted
        found_document = collection.find_one({"_id": result.inserted_id})
        print(f"Retrieved document: {found_document}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    main()