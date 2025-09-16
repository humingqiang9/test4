#!/bin/bash

# Generate a random filename
random_name=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
script_name="${random_name}.sh"

# Disk usage check script
cat > "$script_name" << 'EOF'
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
EOF

# Make the script executable
chmod +x "$script_name"

echo "Script created as $script_name"
echo "To run it, use: ./$script_name"