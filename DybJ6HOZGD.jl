# Basic Array Operations in Julia

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
    # Create sample arrays
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [10, 20, 30, 40, 50]
    arr3 = [1.5, 2.7, 3.2, 4.8, 5.1]
    
    println("Array Operations Demo")
    println("====================")
    
    # Demonstrate sum operation
    println("Array 1: ", arr1)
    println("Sum of Array 1: ", array_sum(arr1))
    println("Mean of Array 1: ", array_mean(arr1))
    
    println("\nArray 2: ", arr2)
    println("Sum of Array 2: ", array_sum(arr2))
    println("Mean of Array 2: ", array_mean(arr2))
    
    println("\nArray 3: ", arr3)
    println("Sum of Array 3: ", array_sum(arr3))
    println("Mean of Array 3: ", array_mean(arr3))
end

# Run the demonstration
demonstrate_operations()