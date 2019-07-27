#!/usr/bin/env python

# This script checks the server logs for errors and 
# displays data such as total errors and avg errors.
# displays error msg along with stack msg.
# Supply the directory with the server logs and the 
# script will attempt to rename the files if they are 
# in a certain incorrect format.

import sys
import os
import re
from datetime import datetime
import pprint
from decimal import *

def main():
    original = sys.stdout

    if os.geteuid() == 0:
        print("Running as root.")
    else:
        sys.exit("This script must be run as root!")
    
    # gets directory passed in
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply a directory to check")

        # time to bail
        sys.exit()
    else:
        # ok, looking good. let's check server logs 
        fileinput = sys.argv[1]
        print("Checking: %s\n" % fileinput)
    
    
    # redirect to txt
    sys.stdout = open("log_output.txt", "w")

    file_list = os.listdir(fileinput)

    file_list.sort()

    # removes store.ds from directory
    if os.path.isfile(os.path.join(fileinput, 'Store.DS')):
        os.remove(os.path.join(fileinput, 'Store.DS'))

    # renames given test file format only server.log_2019-07-21-123456
    print("Renaming: ")
    for f in file_list:
        end = f.endswith('.log')
        if end != True:
            try:
                splitname = f.split("_")
                newname = (splitname[1]+splitname[0])
                path = os.path.join(fileinput, f)
                target = os.path.join(fileinput, newname)
                os.rename(path,target)
                print("Renamed %s" % newname)
            except Exception:
                print("Could not rename the file! Please check to see if %s has a valid name." % f)
    print("")


    for file in file_list:
        print("  %s" % file)

    print("")

    total_count = []
    mydict = {}
    total_error_list = []
    total_err_nodup = []

    # Processes all .log files in the given directory
    # outputs error codes and stack messages and displays total 
    # errors for each .log file and for the whole directory.

    for file in file_list:
        if str(file).endswith('.log'):
            print("///////////////////////////////////////////////")

            # get date of file 
            try:
                match = re.search(r'\d{4}-\d{2}-\d{2}', file)
                date = datetime.strptime(match.group(), '%Y-%m-%d').date()
                print("Processing %s" % date)
            except Exception:
                print("%s has no date" % file)
            print(file)
            
            print("")
            f= open(os.path.join(fileinput, file))
            print(f)
            print("")
            print("")
     

            # finds line with "error" and prints that line
            count = 0
            stk_list = []
            print("**********ERRORS**********")
            for line in f:
                
                if "ERROR" in line:
                    count = count + 1
                    print(line)
                    # grab stack message
                    stk_start = '| '
                    stk_end = ' >'
                    stack_trace = re.sub('[()]', '', line[line.find(stk_start) + len(stk_start) : line.rfind(stk_end)])
                    stk_list.append(stack_trace)
                    # grab error message
                    err_start = ' > '
                    err_msg = line[line.find(err_start) + len(err_start) : ]

                    print("Class: %s " % stack_trace)
                    print("Error Msg: %s" % err_msg)

            print("")

            stk_list.sort()
            total_error_list = total_error_list + stk_list
            
            # remove dupes to make counting easier for larger file groups
            stk_lst_nodup = list(dict.fromkeys(stk_list))
            total_err_nodup = list(dict.fromkeys(total_error_list))


            #  Finish processing data
            print("End Processing: %s " % file)
            print("**************************************************")

            print("File date: %s" % date)

            print("%s errors in %s" % (count,file))
            print("")
            for i in stk_lst_nodup:
                print(i + " occurrences: " + str(stk_list.count(i)))
            print("**************************************************")
            print("")

            total_count.append(count)
            mydict.update({str(file): int(count)})

        else:
            print("Cannot process %s" % file)
    

    # pretty print overall data
    print("FILE : # OF ERRORS")
    pprint.pprint(mydict)

    print("")   

    print("SORTED FROM MOST TO LEAST ERRORS")
    print("FILE : # OF ERRORS")
    sorted_dict = sorted(mydict.items(), key = lambda kv: kv[1], reverse = True)

    pprint.pprint(sorted_dict)
    print("")

    # print total occurences of each error for whole directory
    for i in total_err_nodup:
        print(i + " occurrences: " + str(total_error_list.count(i)) + " in total")
    
    print("")

    # Print avg number of errors in total
    getcontext().prec = 6
    avg = Decimal(sum(total_count))/Decimal(len(total_count))
    dirlen = len(file_list)
    
    print("%s average errors per file for %s files" % (avg, dirlen))
    print("%s total errors" % sum(total_count))

    sys.stdout = original

    print("Done processings all files!")
    print("Data written to output_log")



if __name__ == "__main__":
    main()