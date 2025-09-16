#!/bin/bash
# Generate a random filename with .lua extension
RANDOM_NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1).lua

# Copy the lua script to the random filename
cp /workspace/addition.lua "/workspace/$RANDOM_NAME"

echo "Lua script copied to: /workspace/$RANDOM_NAME"