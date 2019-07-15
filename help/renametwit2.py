#!/usr/bin/env python

import os
import sys
import natsort
import shutil
def main():

    # gets directory passed from use
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply a directory to rename")

        # time to bail
        sys.exit()
    else:
        # ok, looking good. let's remove some files
        fileinput = sys.argv[1]
        print("Renaming : %s\n" % fileinput)
    
    #fileinput = str(input("Please input a directory: "))
    file_list = os.listdir(fileinput)


    # split at the / and keep the first section,
    # replace spaces with _
    exercise_name = fileinput.split('/')[0]
    new_exercise_name = exercise_name.replace(" ","_")

    execise_loc = new_exercise_name

    #sort alphabetically
    natsort.natsorted(file_list,reverse = False)

    length = len(file_list)

    first = str(file_list[0])
    last = str(file_list[length - 1])

    firstdate = first.split('_')[1] # splits and keeps middle,
    lastdate = last.split('_')[1] # which is the date 

    firstlist = firstdate.split('-') 
    lastlist = lastdate.split('-')


    # dates are seperated date-month-year into an array
    start_year = firstlist[0]
    start_month = int(firstlist[1])

    if start_month == 1:
        start_month = "JAN"
    elif start_month == 2:
        start_month = "FEB"
    elif start_month == 3:
        start_month = "MAR"
    elif start_month == 4:
        start_month = "APR"
    elif start_month == 5:
        start_month = "MAY"
    elif start_month == 6:
        start_month = "JUN"
    elif start_month == 7:
        start_month = "JUL"
    elif start_month == 8:
        start_month = "AUG"
    elif start_month == 9:
        start_month = "SEP"
    elif start_month == 10:
        start_month = "OCT"
    elif start_month == 11:
        start_month = "NOV"
    elif start_month == 12:
        start_month = "DEC"
    else:
        start_month = None

    start_day = firstlist[2]

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

    new_dir_path = os.path.join(new_exercise_name,'-',start_day,'{',start_month,'}','-',end_day,'{',end_month,'}',end_year)

    os.rename(execise_loc, new_dir_path)

    #change ownership
    shutil.chown(new_dir_path, user = "glassfish", group = "glassfish")
    for f in new_dir_path:
        shutil.chown(f, user = "glassfish", group = "glassfish")
        os.chmod(f, 0o755)



