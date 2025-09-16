#!/bin/bash

# Generate a random filename
RANDOM_NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
FILENAME="${RANDOM_NAME}.py"

# Copy the template to the new random filename
cp /workspace/scrape_titles_template.py "/workspace/${FILENAME}"

echo "Python script saved as: ${FILENAME}"

# Display the content of the created file
echo "Content of the created file:"
echo "----------------------------------------"
cat "/workspace/${FILENAME}"