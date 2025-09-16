#!/usr/bin/env python3
"""
PostgreSQL Connection Script

This script demonstrates how to connect to a PostgreSQL database using psycopg2.
"""

import psycopg2
from psycopg2 import sql

def connect_to_postgres():
    """
    Establishes a connection to a PostgreSQL database.
    
    Returns:
        connection object or None
    """
    try:
        # Database connection parameters
        # Please update these with your actual database credentials
        conn_params = {
            'dbname': 'your_database_name',
            'user': 'your_username',
            'password': 'your_password',
            'host': 'localhost',  # or your database host
            'port': '5432'        # default PostgreSQL port
        }
        
        # Attempt to connect to the database
        print("Connecting to PostgreSQL database...")
        conn = psycopg2.connect(**conn_params)
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Execute a simple query to test the connection
        cur.execute("SELECT version();")
        
        # Fetch the result
        db_version = cur.fetchone()
        print(f"PostgreSQL database version: {db_version[0]}")
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        print("Database connection closed.")
        
        return conn
        
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def main():
    """Main function to run the PostgreSQL connection example."""
    connection = connect_to_postgres()
    if connection:
        print("Successfully connected to the database!")
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()