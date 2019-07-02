#!/usr/bin/env python

# A second attempt at this script. Now we are adding some error checking
# and a little more output to make this more useful. The script is getting
# bigger and more robust.


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

    # sys.argv[0] is the script name, so anything else is arguments
    # but we only one argument, the name of the directory to clean
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply one directory to clean")

        # time to bail
        sys.exit()
    else:
        # ok, looking good. let's remove some files
        print("LET'S DO THIS!")

    print("")

    # this should be the directory we want to clean
    dir_to_clean = sys.argv[1]

    # check to see if this argument is actually a directory
    if os.path.isdir(dir_to_clean):
        print("Directory Found : %s" % os.path.abspath(dir_to_clean))
    else:
        print("My man, that wasn't a valid directory!")
        sys.exit()

    print("")

    print("Scanning For Files to Remove")

    # count of removed files
    removed_files = 0

    # list all of the files in our target directory
    for cur_file in os.listdir(dir_to_clean):
        # get the size of the current file
        file_data = os.stat(cur_file)
        file_size = file_data.st_size

        print("  %s : %s" % (cur_file, file_size))

        # check to see if the size is 0
        if file_size == 0:
            os.remove(cur_file)
            removed_files += 1

    # print summary and then bounce
    print("")
    print("Total Files Removed: %s" % removed_files)


if __name__ == "__main__":
    main()
