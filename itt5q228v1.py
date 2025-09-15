
import pandas as pd

# Filtered DataFrame (Age > 21)
data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'}, {'Name': 'Bob', 'Age': 32, 'City': 'London'}, {'Name': 'David', 'Age': 47, 'City': 'Tokyo'}, {'Name': 'Eve', 'Age': 22, 'City': 'Berlin'}]
filtered_df = pd.DataFrame(data)

print("Filtered DataFrame:")
print(filtered_df)
