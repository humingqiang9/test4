#!/bin/bash
# Bash script to get list of processes and save to a file with random name

# Generate a random file name
randomFileName="processes_$(shuf -i 1000-9999 -n 1).txt"

# Get the list of processes and save to the file
ps aux > "$randomFileName"

# Output the file name to confirm
echo "Processes saved to: $randomFileName"