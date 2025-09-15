# R Script to Load CSV and Print Summary Statistics
# Generate random filename for CSV loading

# Set seed for reproducibility
set.seed(123)

# Generate a random filename
random_filename <- paste0("data_", sample(1000:9999, 1), ".csv")

# Check if file exists, if not create a sample dataset and save it
if (!file.exists(random_filename)) {
  # Create sample data
  sample_data <- data.frame(
    ID = 1:100,
    Age = sample(18:80, 100, replace = TRUE),
    Income = round(rnorm(100, 50000, 15000)),
    Score = runif(100, 0, 100)
  )
  
  # Write to CSV
  write.csv(sample_data, random_filename, row.names = FALSE)
  cat("Created sample data file:", random_filename, "\n")
}

# Load the CSV file
data <- read.csv(random_filename)

# Print summary statistics
cat("Summary Statistics for", random_filename, "\n")
cat("=====================================\n")
print(summary(data))

# Additional statistics
cat("\nStandard Deviations:\n")
print(sapply(data[sapply(data, is.numeric)], sd))

cat("\nData Structure:\n")
str(data)