#!/usr/bin/env python

import os
import sys
import natsort
import shutil

### NOTES ###
#
#  Let's go over what this script should do:
#
#    - we want to take as an input a directory name
#    - then we want to scan the file names of that directory
#    - based on the newest and oldest date we want to rename the initial directory
#    - So the directory "Canada" becomes "Canada-13OCT-20OCT2016"
#
#
#  Two use cases:
#
#    - ./renametwit2.py Canada
#    - ./renametwit2.py /home/shazam/stuff/more_stuff/junk/crud/Canada
#
#  In both cases we want the output to be the same
#
#
#  Other thoughts
#
#    - when in doubt put lots of print statements in
#    - seriously, print everything so you can watch how things go
#    - good job getting hold of the basic algorithm for this


def main():

    ################################################################
    #  Step 1 - Get the directory name
    ################################################################

    # gets directory passed in
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply a directory to rename")

        # time to bail
        sys.exit()
    else:
        # ok, looking good. let's rename the directory
        fileinput = sys.argv[1]
        print("Renaming : %s\n" % fileinput)

    ################################################################
    #  Step 2 - Get a list of files
    ################################################################
    file_list = os.listdir(fileinput)
    print("Initial File List")

    for file in file_list:
        print("  %s" % file)

    print("")

    # ????????????????????????????????????????????????????????
    # I'm not totally sure what you are doing here.
    # If fileinput is "Canada" what are you trying to split?

    # split at the / and keep the first section,
    # replace spaces with _
    exercise_name = fileinput.split("/")[0]
    new_exercise_name = exercise_name.replace(" ", "_")
    exercise_loc = new_exercise_name
    # ????????????????????????????????????????????????????????

    ################################################################
    #  Step 3 - Sort the files since we want the first and last one
    ################################################################
    # sort alphabetically

    # ????????????????????????????????????????????????????????
    # you are over thinking this, the basic sort will work fine
    # natsort.natsorted(file_list, reverse=False)
    # ????????????????????????????????????????????????????????

    file_list.sort()

    print("Sorted File List")
    for file in file_list:
        print("  %s" % file)

    ################################################################
    #  Step 4 - Get the first and last file
    ################################################################

    length = len(file_list)
    first_file = file_list[0]
    last_file = file_list[length - 1]

    print("")
    print("first : %s" % first_file)
    print("last  : %s" % last_file)
    print("")

    ################################################################
    #  Step 5 - Split it up
    ################################################################

    firstdate = first_file.split("_")[1]  # splits and keeps middle,
    lastdate = last_file.split("_")[1]  # which is the date

    print("First Date : %s" % firstdate)
    print("Last Date  : %s" % lastdate)
    print("")

    # dates are seperated date-month-year into an array
    first_list = firstdate.split("-")
    last_list = lastdate.split("-")

    # let's make a dictionary to make this easier
    months = {
        "1": "JAN",
        "2": "FEB",
        "3": "MAR",
        "4": "APR",
        "5": "MAY",
        "6": "JUN",
        "7": "JUL",
        "8": "AUG",
        "9": "SEP",
        "10": "OCT",
        "11": "NOV",
        "12": "DEC",
    }

    # now we can just pick out the values from the array
    start_year = first_list[0]
    start_month = months[first_list[1]]
    start_day = first_list[2]

    print("Start Date")
    print("Year  : %s" % start_year)
    print("Month : %s" % start_month)
    print("Day   : %s" % start_day)

    sys.exit()  # <-- remove this to keep testing

    ################################################################
    #  And you can take it from here. Does this help?
    ################################################################

    # end date
    end_year = lastlist[0]
    end_month = int(lastlist[1])

    if end_month == 1:
        end_month = "JAN"
    elif end_month == 2:
        end_month = "FEB"
    elif end_month == 3:
        end_month = "MAR"
    elif end_month == 4:
        end_month = "APR"
    elif end_month == 5:
        end_month = "MAY"
    elif end_month == 6:
        end_month = "JUN"
    elif end_month == 7:
        end_month = "JUL"
    elif end_month == 8:
        end_month = "AUG"
    elif end_month == 9:
        end_month = "SEP"
    elif end_month == 10:
        end_month = "OCT"
    elif end_month == 11:
        end_month = "NOV"
    elif end_month == 12:
        end_month = "DEC"
    else:
        end_month = None

    end_day = lastlist[2]

    new_dir_path = os.path.join(
        new_exercise_name,
        "-",
        start_day,
        "{",
        start_month,
        "}",
        "-",
        end_day,
        "{",
        end_month,
        "}",
        end_year,
    )

    os.rename(exercise_loc, new_dir_path)

    # change ownership
    shutil.chown(new_dir_path, user="glassfish", group="glassfish")
    for f in new_dir_path:
        shutil.chown(f, user="glassfish", group="glassfish")
        os.chmod(f, 0o755)


if __name__ == "__main__":
    main()
