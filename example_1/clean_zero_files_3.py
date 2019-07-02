#!/usr/bin/env python

# A third attempt, we can go deeper! So, at this point we have printing
# error checking, which is really good. But we are just pulling in the
# arg from sys.argv[] directly, which isn't good. Also we could probably
# make some functions out of all this.


import sys
import os
import glob
from optparse import OptionParser


def delete_file_if_empty(cur_file):
    """ 
    Delete the file if it is empty 
    """

    # get the size of the current file
    file_data = os.stat(cur_file)
    file_size = file_data.st_size

    print("  %s : %s" % (cur_file, file_size))

    # check to see if the size is 0
    if file_size == 0:
        os.remove(cur_file)


def enable_arg_parser():
    """
    Add argument parsing to the script
    """

    parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0.0")
    parser.add_option(
        "-d",
        "--dir-to-clean",
        action="store",
        dest="target_dir",
        help="The directory you want to remove zero byte files from",
    )

    (options, args) = parser.parse_args()

    # print help if no args
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # check to see if this argument is actually a directory
    if os.path.isdir(options.target_dir):
        print("Directory Found : %s" % os.path.abspath(options.target_dir))
    else:
        print("My man, that wasn't a valid directory!")
        sys.exit()

    return (options, args)


def main():
    """
    Remove any zero byte files
    """

    # Enable the arg parser
    (options, args) = enable_arg_parser()

    # print a greeting to the terminal
    print("== REMOVING ZERO BYTE FILES ===")
    print("Scanning For Files to Remove")

    # list all of the files in our target directory
    for cur_file in os.listdir(options.target_dir):
        delete_file_if_empty(cur_file)


if __name__ == "__main__":
    main()
