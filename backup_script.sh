#!/bin/bash

# Check if source directory is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <source_directory> [destination_directory]"
    echo "Example: $0 /home/user/documents /backups"
    exit 1
fi

# Set source directory from first argument
SOURCE_DIR="$1"

# Set destination directory (optional second argument or default to current directory)
DEST_DIR="${2:-.}"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Create timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create backup folder name
BACKUP_FOLDER="backup_$TIMESTAMP"

# Create full path for backup
BACKUP_PATH="$DEST_DIR/$BACKUP_FOLDER"

# Create the backup directory
mkdir -p "$BACKUP_PATH"

# Perform the backup
echo "Backing up '$SOURCE_DIR' to '$BACKUP_PATH'..."
cp -r "$SOURCE_DIR" "$BACKUP_PATH"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup location: $BACKUP_PATH"
else
    echo "Error: Backup failed."
    exit 1
fi