#!/usr/bin/env python3
"""
MySQL SELECT Query Executor
This script connects to a MySQL database and executes a SELECT query.
"""

import mysql.connector
import random
import string

def generate_random_string(length=8):
    """Generate a random string of specified length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def execute_select_query():
    # Database connection parameters
    config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'database': 'your_database',
        'raise_on_warnings': True
    }

    try:
        # Establish connection
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        
        # Execute SELECT query
        query = "SELECT * FROM your_table LIMIT 10"
        cursor.execute(query)
        
        # Fetch and print results
        results = cursor.fetchall()
        print("Query Results:")
        for row in results:
            print(row)
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        # Clean up connections
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    print("Executing SELECT query on MySQL database...")
    execute_select_query()
    print("Operation completed.")