#!/usr/bin/env python

#Input the path you wish to clean
#This will recursively find all files
# of 0 size and remove them
import sys
import os

#gets path
path = input("Enter the path: ")

#loops through the dir and cleans files of 0 size
for root, dirs, files in os.walk(path):
    for name in files:
        filename = os.path.join(root,name)
        if os.stat(filename).st_size == 0:
            print("removing ", filename)
            os.remove(filename)
