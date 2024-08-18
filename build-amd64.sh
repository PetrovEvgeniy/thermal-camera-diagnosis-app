#!/usr/bin/env bash

# Build a snap of the whole battery diagnosis app
snapcraft clean --destructive-mode
snapcraft --destructive-mode
snapcraft clean --destructive-mode

# Remove the build directory
rm -rf ./build