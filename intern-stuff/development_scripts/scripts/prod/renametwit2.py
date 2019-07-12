#!/usr/bin/env python

import os
fileinput = str(input("Please input a directory: "))
file_list = os.listdir(fileinput)

exercise_name = fileinput.split('/')[0]
new_exercise_name = exercise_name.replace(" ","_")

execise_loc = new_exercise_name

def middle_vals(x):
    return(x[7:])

sorted(file_list, key = middle_vals)

length = len(os.listdir(file_list))

first = str(os.listdir(file_list)[0])
last = str(os.listdir(file_list)[length - 1])

firstdate = first.split('_')[1] # splits and keeps middle
lastdate = last.split('_')[1] # which is the date 

firstlist = firstdate.split('-') 
lastlist = lastdate.split('-')

start_year = firstlist[0]
start_month = firstlist[1]
start_day = firstlist[2]

end_year = lastlist[0]
end_month = lastlist[1]
end_day = lastlist[2]

new_dir_path = os.path.join(new_exercise_name,'-',start_day,'{',start_month,'}','-',end_day,'{',end_month,'}',end_year)

os.rename(execise_loc, new_dir_path)