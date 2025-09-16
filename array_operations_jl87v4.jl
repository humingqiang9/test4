# Basic Array Operations in Julia
# This script demonstrates common array operations like sum and mean

using Statistics

# Create sample arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30, 40, 50]
arr3 = [1.5, 2.7, 3.2, 4.8, 5.1]

println("Array Operations Examples")
println("========================")

# Sum operations
println("\nSum Operations:")
println("Sum of arr1: ", sum(arr1))
println("Sum of arr2: ", sum(arr2))
println("Sum of arr3: ", sum(arr3))

# Mean operations
println("\nMean Operations:")
println("Mean of arr1: ", mean(arr1))
println("Mean of arr2: ", mean(arr2))
println("Mean of arr3: ", mean(arr3))

# Additional operations
println("\nAdditional Operations:")
println("Length of arr1: ", length(arr1))
println("Maximum value in arr2: ", maximum(arr2))
println("Minimum value in arr3: ", minimum(arr3))

# Multi-dimensional arrays
println("\nMulti-dimensional Arrays:")
matrix = [1 2 3; 4 5 6; 7 8 9]
println("Matrix:")
println(matrix)
println("Sum of all elements: ", sum(matrix))
println("Mean of all elements: ", mean(matrix))
println("Sum along columns: ", sum(matrix, dims=1))
println("Sum along rows: ", sum(matrix, dims=2))