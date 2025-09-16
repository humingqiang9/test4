import pandas as pd

# Recreated filtered DataFrame
data = {
    'Name': ['Bob', 'Charlie', 'David'],
    'Age': [30, 35, 28],
    'City': ['London', 'Paris', 'Tokyo'],
    'Salary': [60000, 70000, 55000],
}

filtered_df = pd.DataFrame(data)
print(filtered_df)
