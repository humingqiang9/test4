# R Script for Loading CSV and Printing Summary Statistics
# Generated on: September 15, 2025

# Load necessary libraries
# If any libraries are needed, they would be loaded here
# library(readr)  # Example of loading a library

# Load the CSV file
# Replace 'data.csv' with the path to your actual CSV file
data <- read.csv("data.csv")

# Print summary statistics
print("Summary Statistics:")
print(summary(data))

# Print structure of the data
print("Data Structure:")
print(str(data))

# Print first few rows
print("First few rows:")
print(head(data))