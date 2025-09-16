# Generate random data
categories <- c("A", "B", "C", "D", "E")
values <- sample(10:100, 5)

# Create bar plot
barplot(values, names.arg = categories, col = rainbow(5), main = "Random Bar Chart", xlab = "Categories", ylab = "Values")

# Save the plot to a file (filename will be based on the script name)