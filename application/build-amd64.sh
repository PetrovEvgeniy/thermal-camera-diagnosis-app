#!/usr/bin/env bash

# Build a snap
snapcraft clean --destructive-mode
snapcraft --destructive-mode
snapcraft clean --destructive-mode

# Remove the build directory
rm -rf ./build



