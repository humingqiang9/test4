# R script to load a CSV file and print summary statistics

# Load required library
# install.packages("readr") # Uncomment if readr is not installed
library(readr)

# Read the CSV file
data <- read_csv("sample_data.csv")

# Print summary statistics
print("Summary Statistics:")
print(summary(data))

# Print structure of the data
print("Data Structure:")
print(str(data))