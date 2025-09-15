
import pandas as pd

# Filtered DataFrame (Age > 21)
data = {'Name': {0: 'Alice', 1: 'Bob', 3: 'David', 4: 'Eve'}, 'Age': {0: 25, 1: 32, 3: 47, 4: 22}, 'City': {0: 'New York', 1: 'London', 3: 'Tokyo', 4: 'Berlin'}}
filtered_df = pd.DataFrame(data)
print(filtered_df)
