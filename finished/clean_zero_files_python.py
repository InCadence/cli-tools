#!/usr/bin/env python

# Run the script while passing the directory you wish to clean.
# This will recursively find all files
# of 0 size and remove them

import sys
import os

# main method
def main(): 

    # passed in from user
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply one directory to clean")

        # bail
        sys.exit()
    else:
        # remove some files
        path = sys.argv[1]
        print("Cleaning Directory : %s" % path)

        # loops through the directory and removes any files of size 0
        for root, files in os.walk(path):
            for name in files:
                filename = os.path.join(root, name)
                if os.stat(filename).st_size == 0:
                    print("  removing :", filename)
                    os.remove(filename)


if __name__ == "__main__":
    main()
