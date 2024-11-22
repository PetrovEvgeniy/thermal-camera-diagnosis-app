#!/usr/bin/env bash

# Build a snap of the whole battery diagnosis app
snapcraft clean --destructive-mode
snapcraft --enable-experimental-target-arch --target-arch=arm64 --destructive-mode
snapcraft clean --destructive-mode