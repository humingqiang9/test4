import pandas as pd
import random
import string

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 22],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'],
    'Salary': [50000, 75000, 30000, 90000, 45000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Filter the DataFrame (example: people older than 25 with salary > 40000)
filtered_df = df[(df['Age'] > 25) & (df['Salary'] > 40000)]

print("\nFiltered DataFrame (Age > 25 and Salary > 40000):")
print(filtered_df)

# Generate a random filename
def generate_random_filename():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string + '.py'

# Save the script to a randomly named .py file
filename = generate_random_filename()
print(f"\nSaving to file: {filename}")

# In a real scenario, we would save the actual script content to the file
# For this example, we'll just save some information about what we did
script_content = f"""
# This script was generated automatically
# It created a DataFrame and filtered it based on age and salary criteria

import pandas as pd

# Original data
data = {data}

df = pd.DataFrame(data)

# Applied filter: Age > 25 and Salary > 40000
filtered_df = df[(df['Age'] > 25) & (df['Salary'] > 40000)]

print("Filtered Results:")
print(filtered_df)
"""

with open(filename, 'w') as f:
    f.write(script_content)

print("Script saved successfully!")