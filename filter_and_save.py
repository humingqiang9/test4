import pandas as pd
import random
import string

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'],
    'Salary': [50000, 60000, 70000, 55000, 45000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Filter the DataFrame (example: people older than 25)
filtered_df = df[df['Age'] > 25]

print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# Generate a random filename
random_filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.py'

# Save the filtered DataFrame to the random .py file
# We'll save it as a Python script that recreates the filtered DataFrame
with open(random_filename, 'w') as f:
    f.write('import pandas as pd\n\n')
    f.write('# Recreated filtered DataFrame\n')
    f.write('data = {\n')
    for col in filtered_df.columns:
        f.write(f"    '{col}': {filtered_df[col].tolist()},\n")
    f.write('}\n\n')
    f.write('filtered_df = pd.DataFrame(data)\n')
    f.write('print(filtered_df)\n')

print(f"\nFiltered DataFrame saved to {random_filename}")