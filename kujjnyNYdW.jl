# Basic Array Operations in Julia
# This script demonstrates common array operations like sum and mean

using Statistics

# Create sample arrays
array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30, 40, 50]
array3 = [2.5, 3.7, 1.2, 8.9, 5.1]

println("Sample Arrays:")
println("Array 1: ", array1)
println("Array 2: ", array2)
println("Array 3: ", array3)
println()

# Sum operations
println("Sum Operations:")
println("Sum of Array 1: ", sum(array1))
println("Sum of Array 2: ", sum(array2))
println("Sum of Array 3: ", sum(array3))
println()

# Mean operations
println("Mean Operations:")
println("Mean of Array 1: ", mean(array1))
println("Mean of Array 2: ", mean(array2))
println("Mean of Array 3: ", mean(array3))
println()

# Additional operations
println("Additional Operations:")
println("Length of Array 1: ", length(array1))
println("Maximum value in Array 3: ", maximum(array3))
println("Minimum value in Array 3: ", minimum(array3))