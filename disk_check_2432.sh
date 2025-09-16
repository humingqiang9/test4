#!/bin/bash

# Script to check disk usage and alert if over 80%
# Generated on: $(date)

# Get the disk usage percentage (using / as the root filesystem)
USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

# Check if usage is greater than 80%
if [ "$USAGE" -gt 80 ]; then
    echo "WARNING: Disk usage is at ${USAGE}% which exceeds the 80% threshold!"
    echo "Consider cleaning up some files."
    exit 1
else
    echo "Disk usage is at ${USAGE}%. All good!"
    exit 0
fi