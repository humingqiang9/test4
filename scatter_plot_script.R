# Generate random data
set.seed(123)  # For reproducibility
x <- rnorm(100, mean = 50, sd = 10)
y <- 2 * x + rnorm(100, mean = 0, sd = 5)

# Create a random filename
random_name <- paste0("scatter_plot_", sprintf("%06d", sample(1:999999, 1)), ".png")

# Create and save the scatter plot
png(random_name)
plot(x, y, 
     main = "Scatter Plot of Random Data",
     xlab = "X Values",
     ylab = "Y Values",
     pch = 19,
     col = "blue")
dev.off()

# Print the filename to confirm
cat("Scatter plot saved as:", random_name, "\n")