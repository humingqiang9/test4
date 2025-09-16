import sqlite3
import random
import string

def generate_random_name(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_database_and_table():
    # Generate a random database name
    db_name = generate_random_name() + ".db"
    
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create a sample table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            salary REAL
        )
    ''')
    
    # Insert sample data
    sample_data = [
        ("John Doe", 30, "Engineering", 75000.0),
        ("Jane Smith", 25, "Marketing", 65000.0),
        ("Mike Johnson", 35, "Sales", 70000.0),
        ("Emily Davis", 28, "HR", 60000.0)
    ]
    
    cursor.executemany('''
        INSERT INTO employees (name, age, department, salary)
        VALUES (?, ?, ?, ?)
    ''', sample_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print(f"Database '{db_name}' created with table 'employees' and sample data.")

if __name__ == "__main__":
    create_database_and_table()