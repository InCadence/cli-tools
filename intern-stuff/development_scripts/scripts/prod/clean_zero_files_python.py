#!/usr/bin/env python

#Input the path you wish to clean
#This will recursively find all files
# of 0 size and remove them

import sys
import os

#main method
def main():

    #gets path from user
    path = str(input("Enter the path surrounded by quotes (\"p/a/t/h...\"): "))

    #loops through the directory and removes any files of size 0
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root,name)
            if os.stat(filename).st_size == 0:
                print("removing ", filename)
                os.remove(filename)

if __name__ == "__main__":
    main()
