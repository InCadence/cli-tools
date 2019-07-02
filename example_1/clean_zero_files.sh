#!/bin/bash

# Run this in the directory that you want to clean and
# this will recursively find all files of 0 size and
# remove them.

find . -size 0 | while read f; do echo "Removing: $f"; rm -f "$f"; done
