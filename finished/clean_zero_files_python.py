#!/usr/bin/env python

# Input the path you wish to clean
# This will recursively find all files
# of 0 size and remove them

import sys
import os

# main method
def main():
    """
    Michael cleans things up
    """

    # gets path passed in from the user
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply one directory to clean")

        # time to bail
        sys.exit()
    else:
        # ok, looking good. let's remove some files
        path = sys.argv[1]
        print("Cleaning Directory : %s" % path)

        # loops through the directory and removes any files of size 0
        for root, dirs, files in os.walk(path):
            for name in files:
                filename = os.path.join(root, name)
                if os.stat(filename).st_size == 0:
                    print("  removing :", filename)
                    os.remove(filename)


if __name__ == "__main__":
    main()
