# R Script to Load CSV and Print Summary Statistics
# Generate a random dataset for demonstration

# Create sample data
set.seed(123)  # For reproducibility
sample_data <- data.frame(
  ID = 1:100,
  Age = sample(18:80, 100, replace = TRUE),
  Income = sample(20000:150000, 100, replace = TRUE),
  Score = rnorm(100, mean = 75, sd = 10)
)

# Write to CSV file
write.csv(sample_data, "sample_data.csv", row.names = FALSE)

# Load the CSV file
data <- read.csv("sample_data.csv")

# Print summary statistics
cat("Summary Statistics:\n")
print(summary(data))

# Additional statistics
cat("\nStandard Deviations:\n")
print(sapply(data[, sapply(data, is.numeric)], sd))

cat("\nCorrelation Matrix:\n")
print(cor(data[, sapply(data, is.numeric)]))