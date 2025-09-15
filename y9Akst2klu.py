# Python Script for Basic Array Operations
# File: y9Akst2klu.py

# Import necessary library
import statistics

# Function to calculate the sum of an array
def array_sum(arr):
    return sum(arr)

# Function to calculate the mean of an array
def array_mean(arr):
    return statistics.mean(arr)

# Function to demonstrate array operations
def demonstrate_operations():
    # Create a sample array
    sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate sum and mean
    arr_sum = array_sum(sample_array)
    arr_mean = array_mean(sample_array)
    
    # Display results
    print("Sample Array:", sample_array)
    print("Sum:", arr_sum)
    print("Mean:", arr_mean)
    
    # Additional operations
    print("\nAdditional Operations:")
    print("Maximum:", max(sample_array))
    print("Minimum:", min(sample_array))
    print("Length:", len(sample_array))

# Run the demonstration
if __name__ == "__main__":
    demonstrate_operations()