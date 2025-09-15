import pandas as pd
import random
import string

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 22],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
}
df = pd.DataFrame(data)

# Filter the DataFrame (e.g., people older than 21)
filtered_df = df[df['Age'] > 21]

# Generate a random filename
random_filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.py'

# Save the filtered DataFrame to the random .py file
with open(random_filename, 'w') as f:
    f.write(f"""
import pandas as pd

# Filtered DataFrame (Age > 21)
data = {filtered_df.to_dict('records')}
filtered_df = pd.DataFrame(data)

print("Filtered DataFrame:")
print(filtered_df)
""")
    
print(f"Script saved to {random_filename}")