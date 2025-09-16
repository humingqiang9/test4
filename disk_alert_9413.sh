#!/bin/bash

# Disk usage alert script
# Checks if disk usage exceeds 80% and sends an alert

# Get disk usage percentage (using / as the root filesystem)
USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

# Check if usage is greater than 80%
if [ "$USAGE" -gt 80 ]; then
    echo "WARNING: Disk usage is at ${USAGE}% - Cleanup recommended!"
    # Here you could add code to send an email or other notification
    exit 1
else
    echo "Disk usage is at ${USAGE}% - Within acceptable limits"
    exit 0
fi