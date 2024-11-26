#!/usr/bin/env bash

# Build a snap
snapcraft clean --destructive-mode
snapcraft --enable-experimental-target-arch --target-arch=arm64 --destructive-mode
snapcraft clean --destructive-mode
