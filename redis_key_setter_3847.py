#!/usr/bin/env python3
"""
A simple script to set a key-value pair in Redis.
"""

import redis
import random
import string

def generate_random_key():
    """Generate a random key for demonstration."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def main():
    # Connect to Redis (assuming it's running on localhost:6379)
    try:
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        
        # Generate a random key and value
        key = generate_random_key()
        value = "Hello, Redis!"
        
        # Set the key-value pair
        r.set(key, value)
        
        # Verify it was set
        retrieved_value = r.get(key)
        
        print(f"Set key: {key}")
        print(f"Set value: {value}")
        print(f"Retrieved value: {retrieved_value}")
        
        # List all keys to show our new key
        all_keys = r.keys('*')
        print(f"All keys in database: {all_keys}")
        
    except redis.ConnectionError:
        print("Error: Could not connect to Redis. Please ensure Redis is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()