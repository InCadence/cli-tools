#!/usr/bin/env python

import os
import sys
import pwd
import grp
import calendar

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

    cleaned_name = os.path.normpath(fileinput)
    new_exercise_name = os.path.basename(cleaned_name)
    exercise_loc = new_exercise_name
    print("New Name : %s" % new_exercise_name)
    print("")

    # ????????????????????????????????????????????????????????
    # I'm not totally sure what you are doing here.
    # If fileinput is "Canada" what are you trying to split?

    # split at the / and keep the first section,
    # replace spaces with _
    # exercise_name = filelist.split("/")[0]
    # new_exercise_name = exercise_name.replace(" ", "_")
    # exercise_loc = new_exercise_name
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

    # now we can just pick out the values from the array
    start_year = first_list[0]
    start_month = str.upper(calendar.month_abbr[int(first_list[1])])
    start_day = first_list[2]

    print("Start Date")
    print("Year  : %s" % start_year)
    print("Month : %s" % start_month)
    print("Day   : %s" % start_day)
    print("")

    # end date
    end_year = last_list[0]
    end_month = start_month = str.upper(calendar.month_abbr[int(last_list[1])])
    end_day = last_list[2]

    print("End Date")
    print("Year  : %s" % end_year)
    print("Month : %s" % end_month)
    print("Day   : %s" % end_day)

    # new_dir_path = (
    #     new_exercise_name
    #     + "-"
    #     + start_day
    #     + "{"
    #     + start_month
    #     + "}"
    #     + "-"
    #     + end_day
    #     + "{"
    #     + end_month
    #     + "}"
    #     + end_year
    # )

    # much easier way of doing this. each '%s' gets replaced by a variable
    new_dir_path = "%s-%s%s-%s%s%s" % (
        new_exercise_name,
        start_day,
        start_month,
        end_day,
        end_month,
        end_year,
    )

    print(new_dir_path)
    os.rename(exercise_loc, new_dir_path)

    ## remove to test below
    sys.exit()

    uid = pwd.getpwnam("glassfish").pw_uid
    gid = grp.getgrnam("glassfish").gr_gid
    # change ownership of path
    os.chown(new_dir_path, uid, gid)
    os.chmod(new_dir_path, 0o755)
    # change ownership of files
    for f in new_dir_path:
        os.chown(f, uid, gid)
        os.chmod(f, 0o755)


if __name__ == "__main__":
    main()
