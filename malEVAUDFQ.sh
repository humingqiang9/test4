#!/bin/bash

# Backup script that creates a timestamped copy of a directory
# Usage: ./backup_script.sh <source_directory>

# Check if source directory is provided
if [ $# -eq 0 ]; then
    echo "Error: No source directory provided"
    echo "Usage: $0 <source_directory> [destination_directory]"
    exit 1
fi

# Get the source directory from first argument
SOURCE_DIR="$1"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist"
    exit 1
fi

# Get destination directory from second argument or use current directory
if [ $# -eq 2 ]; then
    DEST_DIR="$2"
else
    DEST_DIR="./backups"
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Create timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Get the base name of the source directory
DIR_NAME=$(basename "$SOURCE_DIR")

# Create backup directory name
BACKUP_DIR="$DEST_DIR/${DIR_NAME}_backup_$TIMESTAMP"

# Perform the backup using cp
echo "Creating backup of '$SOURCE_DIR' to '$BACKUP_DIR'"
cp -r "$SOURCE_DIR/" "$BACKUP_DIR/"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup location: $BACKUP_DIR"
else
    echo "Error: Backup failed!"
    exit 1
fi