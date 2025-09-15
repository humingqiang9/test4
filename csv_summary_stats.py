import pandas as pd
import numpy as np
import random
import os

# Set seed for reproducibility
random.seed(123)
np.random.seed(123)

# Generate a random filename
random_filename = f"data_{random.randint(1000, 9999)}.csv"

# Check if file exists, if not create a sample dataset and save it
if not os.path.exists(random_filename):
    # Create sample data
    sample_data = pd.DataFrame({
        'ID': range(1, 101),
        'Age': np.random.randint(18, 81, 100),
        'Income': np.round(np.random.normal(50000, 15000, 100)).astype(int),
        'Score': np.random.uniform(0, 100, 100)
    })
    
    # Write to CSV
    sample_data.to_csv(random_filename, index=False)
    print(f"Created sample data file: {random_filename}")

# Load the CSV file
data = pd.read_csv(random_filename)

# Print summary statistics
print(f"Summary Statistics for {random_filename}")
print("=" * (30 + len(random_filename)))
print(data.describe())

# Additional statistics
print("\nData Info:")
print(data.info())