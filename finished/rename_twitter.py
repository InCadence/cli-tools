#!/usr/bin/env python

# Script for renaming the twitter json directory
# Run this script while passing a directory that
# needs to be renamed. changes ownership of files 
# to glassfish.

import os
import sys
import pwd
import grp
import calendar

def main():

    # directory passed in
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply a directory to rename")
        # bail
        sys.exit()
    else:
        # rename the directory
        fileinput = sys.argv[1]
        print("Renaming : %s\n" % fileinput)

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

    # sort alphabetically
    file_list.sort()

    print("Sorted File List")
    for file in file_list:
        print("  %s" % file)

    length = len(file_list)
    first_file = file_list[0]
    last_file = file_list[length - 1]

    print("")
    print("first : %s" % first_file)
    print("last  : %s" % last_file)
    print("")

    firstdate = first_file.split("_")[1]  # splits and keeps middle,
    lastdate = last_file.split("_")[1]  # which is the date

    print("First Date : %s" % firstdate)
    print("Last Date  : %s" % lastdate)
    print("")

    # dates are seperated date-month-year into an array
    first_list = firstdate.split("-")
    last_list = lastdate.split("-")

    # pick out vals from array
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
