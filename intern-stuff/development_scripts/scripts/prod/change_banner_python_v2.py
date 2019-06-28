#!/usr/bin/env python

import os
import sys
import glob
def main():

    #check for root permissions
    if os.geteuid() == 0:
        print("Runnin as root.")
    else:
        sys.exit("This script must be run as root!")

    #define paths
    BASE_PATH = "opt/glassfish4/domains/ion/applications"
    BROWSER_PATH = "ion-browser-1.4.0"

    BANNER_FILE_STR = "css/banner.css"
    BANNER_FILE = os.path.join(BASE_PATH,BROWSER_PATH,BANNER_FILE_STR)

    INDEX_FILE_STR = "index.html"
    INDEX_FILE = os.path.join(BASE_PATH,BROWSER_PATH,INDEX_FILE_STR)

    HTML_FILES_LOC = os.path.join(BASE_PATH,BROWSER_PATH)

    NEW_COLOR = "green"
    BANNER_TEXT = ""

    #select color
    #check for correct input
    while True:
        print("Select a new banner color\n\n 1 - green\n 2 - red\n 3 - blue\n 4 - yellow\n 5 - orange\n 6 - gray")
        number = int(input())

        if number < 1 or number > 6:
            print("Please enter a valid selection")
        else:
            break
    if number == 1:
        NEW_COLOR = "green"
    elif number == 2:
        NEW_COLOR = "red"
    elif number == 3:
        NEW_COLOR = "blue"
    elif number == 4:
        NEW_COLOR = "yellow"
    elif number == 5:
        NEW_COLOR = "orange"
    else: 
        NEW_COLOR = "gray"
    
    #enter the new text
    BANNER_TEXT = input("Enter the banner: ")
    
    #confirm changes
    #check for correct input
    print("NEW BANNER COLOR: ", NEW_COLOR)
    print("NEW BANNER TEXT: ", BANNER_TEXT)

    print("Write changes to ION?")
   
    while True:
        print("1. Continue \n2. Quit\n")
        choice = int(input())
        if choice < "1" or choice >"2":
            print("Please choose: ")
            continue
        else:
            break

    #write changes



if __name__ == "__main__":
    main()

    

    
    




