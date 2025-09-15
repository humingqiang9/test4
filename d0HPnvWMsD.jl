# Julia Script for Basic Array Operations
# File: d0HPnvWMsD.jl

# Function to calculate the sum of an array
function array_sum(arr)
    return sum(arr)
end

# Function to calculate the mean of an array
function array_mean(arr)
    return mean(arr)
end

# Function to demonstrate array operations
function demonstrate_operations()
    # Create a sample array
    sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate sum and mean
    arr_sum = array_sum(sample_array)
    arr_mean = array_mean(sample_array)
    
    # Display results
    println("Sample Array: ", sample_array)
    println("Sum: ", arr_sum)
    println("Mean: ", arr_mean)
    
    # Additional operations
    println("\nAdditional Operations:")
    println("Maximum: ", maximum(sample_array))
    println("Minimum: ", minimum(sample_array))
    println("Length: ", length(sample_array))
end

# Run the demonstration
demonstrate_operations()