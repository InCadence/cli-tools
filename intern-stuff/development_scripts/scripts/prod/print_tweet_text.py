#!/usr/bin/env python

# This script runs through the twitter files and prints 
# important values from the passed directory and search field.

import sys
import os
import subprocess

def main():
    # check to see if a directory name is given. Exit if not
    if(str(sys.argv[1]) == ''):
        print("Error! Must supply a directory name")
        exit(1)
    if(str(sys.argv[2] == '')):
        print("Error! Must supply a field to search")
        exit(1)

    ION_PATH = "/opt/ion_local_data"
    EXERCISE = str(sys.argv[1])
    COL_NAME = str(sys.argv[2]) # should be something like '"created_at":'

    os.chdir(str(EXERCISE))

    subprocess.call(["sed -e 's/[{}]/''g' *.json | awk -v k= 'text' '{n=split($0,a,','); for (i=1; i<=n; i++) print a[i]} | grep", COL_NAME], shell = True)