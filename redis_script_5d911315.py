#!/usr/bin/env python3
"""
A simple script to set a key-value pair in Redis.
"""

import redis
import sys

def connect_to_redis():
    """Establish a connection to Redis."""
    try:
        # Connect to Redis server on localhost default port 6379
        # decode_responses=True allows us to get strings instead of bytes
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        # Test the connection
        r.ping()
        print("Connected to Redis successfully!")
        return r
    except redis.ConnectionError:
        print("Error: Unable to connect to Redis. Please ensure Redis server is running.")
        sys.exit(1)

def set_key_value(r, key, value):
    """Set a key-value pair in Redis."""
    try:
        result = r.set(key, value)
        if result:
            print(f"Key '{key}' set to '{value}' successfully!")
        else:
            print(f"Failed to set key '{key}'")
    except Exception as e:
        print(f"Error setting key-value pair: {e}")

def main():
    # Connect to Redis
    r = connect_to_redis()
    
    # Set a sample key-value pair
    sample_key = "greeting"
    sample_value = "Hello, Redis!"
    set_key_value(r, sample_key, sample_value)
    
    # Verify by getting the value back
    retrieved_value = r.get(sample_key)
    print(f"Retrieved value for '{sample_key}': {retrieved_value}")

if __name__ == "__main__":
    main()