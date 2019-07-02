#!/usr/bin/env python

# A first attempt at a translation of the bash script. This just
# implements the core feature of removing empty files. We can
# expand this later.


import sys
import os
import glob


def main():
    """
    Remove any zero byte files
    """

    # print a greeting to the terminal
    print("== REMOVING ZERO BYTE FILES ===")

    # get all of the arguments that were passed in to the script
    args = sys.argv

    # this should be the directory we want to clean
    dir_to_clean = sys.argv[1]

    print("")

    print("Scanning For Files to Remove")

    # list all of the files in our target directory
    for cur_file in os.listdir(dir_to_clean):
        # get the size of the current file
        file_data = os.stat(cur_file)
        file_size = file_data.st_size

        print("  %s : %s" % (cur_file, file_size))

        # check to see if the size is 0
        if file_size == 0:
            os.remove(cur_file)


if __name__ == "__main__":
    main()
