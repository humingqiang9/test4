#!/bin/bash

# Get disk usage percentage (using / partition as an example)
USAGE=$(df / | grep -oE '[0-9]+%' | tr -d '%')

# Check if usage is greater than 80%
if [ "$USAGE" -gt 80 ]; then
    echo "WARNING: Disk usage is at ${USAGE}% which exceeds 80% threshold!"
    # You can add more actions here like sending an email or logging to a file
else
    echo "Disk usage is at ${USAGE}%. All good."
fi
