# Basic Array Operations in Julia
# This script demonstrates common array operations like sum and mean

using Statistics

# Create sample arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30, 40, 50]
arr3 = [1.5, 2.7, 3.2, 4.8, 5.1]

println("Array 1: ", arr1)
println("Array 2: ", arr2)
println("Array 3: ", arr3)
println()

# Calculate sum of arrays
sum_arr1 = sum(arr1)
sum_arr2 = sum(arr2)
sum_arr3 = sum(arr3)

println("Sum of Array 1: ", sum_arr1)
println("Sum of Array 2: ", sum_arr2)
println("Sum of Array 3: ", sum_arr3)
println()

# Calculate mean of arrays
mean_arr1 = mean(arr1)
mean_arr2 = mean(arr2)
mean_arr3 = mean(arr3)

println("Mean of Array 1: ", mean_arr1)
println("Mean of Array 2: ", mean_arr2)
println("Mean of Array 3: ", mean_arr3)
println()

# Additional operations
println("Maximum value in Array 1: ", maximum(arr1))
println("Minimum value in Array 2: ", minimum(arr2))
println("Standard deviation of Array 3: ", std(arr3))