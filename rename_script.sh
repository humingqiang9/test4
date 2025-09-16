#!/bin/bash

# Generate a random name using /dev/urandom and tr
RANDOM_NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)

# Rename the R script with the random name
mv /workspace/data_analysis_script.R /workspace/${RANDOM_NAME}.r

echo "R script saved as ${RANDOM_NAME}.r"