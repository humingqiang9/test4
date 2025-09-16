#!/usr/bin/env python3
"""
Redis Key-Value Setter
This script connects to a Redis server and sets a key-value pair.
"""

import redis
import random
import string

def generate_random_key():
    """Generate a random key for demonstration."""
    return 'random_key_' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_random_value():
    """Generate a random value for demonstration."""
    return 'random_value_' + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def main():
    try:
        # Connect to Redis server (default: localhost:6379)
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        
        # Generate random key-value pair
        key = generate_random_key()
        value = generate_random_value()
        
        # Set the key-value pair in Redis
        r.set(key, value)
        
        print(f"Successfully set key '{key}' with value '{value}' in Redis.")
        
        # Verify by getting the value back
        retrieved_value = r.get(key)
        print(f"Retrieved value for key '{key}': {retrieved_value}")
        
    except redis.ConnectionError:
        print("Error: Could not connect to Redis server. Please ensure Redis is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()