#!/usr/bin/env python
import sys
import os
import re
from datetime import datetime

def main():
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
    
    file_list = os.listdir(fileinput)

    file_list.sort()

    #renames files so the script can process them
    print("Renaming: ")
    for f in file_list:
        try:
            splitname = f.split("_")
            newname = (splitname[1]+splitname[0])
            path = os.path.join(fileinput, f)
            target = os.path.join(fileinput, newname)
            os.rename(path,target)
            print("Renamed %s" % newname)
        except Exception:
            print("%s has a valid name." % f)
    print("")

    print("Server log list: ")

    for file in file_list:
        print("  %s" % file)

    print("")

    # Testing for 1 file first
    
    # get date of file
    match = re.search(r'\d{4}-\d{2}-\d{2}', file_list[0])
    date = datetime.strptime(match.group(), '%Y-%m-%d').date()
    print("Processing %s" % date)

    print("")

    file1 = open(os.path.join(fileinput, file_list[0]))
    print(file1)

    print("")

    # finds line with "error" and prints that line
    count = 0
    stk_list = []

    for line in file1:
        if "ERROR" in line:
            count = count + 1
            print(line)

            stk_start = '| '
            stk_end = ' >'
            stack_trace = re.sub('[()]', '', line[line.find(stk_start) + len(stk_start) : line.rfind(stk_end)])
            stk_list.append(stack_trace)

            err_start = ' > '
            err_msg = line[line.find(err_start) + len(err_start) : ]

            print("Class: %s " % stack_trace)
            print("Error Msg: %s" % err_msg)
    print("%s errors in %s" % (count,file_list[0]))

    print("")

    stk_list.sort()
    #remove dupes to make counting easier for larger file groups
    
    stk_lst_nodup = list(dict.fromkeys(stk_list))

    print(stk_list)
    print("")

    print(stk_lst_nodup)
    print("")

    for i in stk_lst_nodup:
        print(i + " occurences: " + str(stk_list.count(i)))

    sys.exit()
    for filename in os.listdir(fileinput):
        f = open(os.path.join(fileinput, filename))
        for line in f:
            if "ERROR" in line:
                print(line)



if __name__ == "__main__":
    main()

    