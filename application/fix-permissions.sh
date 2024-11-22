#!/bin/bash

# Directory to target
TARGET_DIR="config/models/semi-supervised-ad"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Directory $TARGET_DIR does not exist."
  exit 1
fi

# Change directory permissions to drwxrwxr-x (775)
find "$TARGET_DIR" -type d -exec chmod 775 {} \;

# Change file permissions to -rw-rw-r-- (664)
find "$TARGET_DIR" -type f -exec chmod 664 {} \;

echo "Permissions updated successfully."