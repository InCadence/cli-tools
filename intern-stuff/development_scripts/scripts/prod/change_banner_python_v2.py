#!/usr/bin/env python

# Script for changing color and txt of security banners 
# Changes banners loacted here: 
# /opt/glassfish4/glassfish/domains.ion.applications/ion-browser-<version>/css/banner.css
# The text for theb anner will asl get changed in every html file that has a banner 
# which can be found: 
# /opt/glassfish4/glassfish/domains/ion/applicaitons/ion-browswer-<version>

import os
import sys
import fileinput
import re
def main():

    #check for root permissions
    if os.geteuid() == 0:
        print("Running as root.")
    else:
        sys.exit("This script must be run as root!")

    #define paths
    BASE_PATH = "opt/glassfish4/domains/ion/applications/"
    BROWSER_PATH = "ion-browser-1.4.0/"

    BANNER_FILE_STR = "css/banner.css/"
    BANNER_FILE = os.path.join(BASE_PATH,BROWSER_PATH,BANNER_FILE_STR)

    INDEX_FILE_STR = "index.html/"
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
    BANNER_TEXT = str(input("Enter the banner text: "))
    
    #confirm changes
    #check for correct input
    print("NEW BANNER COLOR: ", NEW_COLOR)
    print("NEW BANNER TEXT: ", BANNER_TEXT)

    print("Write changes to ION?")
   
    while True:
        print("1. Continue \n2. Quit\n")
        choice = int(input())
        if choice < 1 or choice > 2:
            print("Please enter a valid selection")
        else:
            break
    if choice == 2:
        exit(1)

    #write changes
    print("Writing changes")

    #change background color
    BGCOLOR = "/background-color/",NEW_COLOR,";/"
    for line in fileinput.input(BANNER_FILE, inplace = True):
        line.replace("/background-color", BGCOLOR)
    # subprocess.call(["sed -i 's/background-color.*/background-color: $NEW_COLOR;/' $BANNER_FILE"])

    #change banner text
    SEARCH_STR = r"\<span class\=secur: ty_banner\>"
    #BANNER_TEXT = subprocess.call(["echo $BANNER_TEXT | sed 's/\//\\\//g'"])
    print(BANNER_TEXT)
    re.sub(r'''['"\n\\]''', lambda m: '\\{:X} '.format(ord(m.group())), BANNER_TEXT)
    print(BANNER_TEXT)


    HTMLSTR = HTML_FILES_LOC,"*.html"
    BT1 = r"<span class=security_banner>",BANNER_TEXT,r"<\/span>/"
    BT2 = r"<strong><span class=security_banner>",BANNER_TEXT,r"<\/span><\/strong>/"

    count = 0
    for line in open(INDEX_FILE):
        if SEARCH_STR in line:
            count = count + 1


    if(count >= 1):
        #subprocess.call(["sed -i 's/<span class=security_banner>.*<\/span>/<span class=security_banner>$BANNER_TEXT<\/span>/' $HTML_FILES_LOC/*.html"])
        with fileinput.FileInput(HTMLSTR, inplace = True, backup='.bak') as file:
            for line in file:
                line.replace(r"<span class=security_banner>.*<\/span>",BT1)
    else:
        #subprocess.call(["sed -i 's/<strong>.*<\/strong>/<strong><span class=security_banner>$BANNER_TEXT<\/span><\/strong>/' $HTML_FILES_LOC/*.html"])
         with fileinput.FileInput(HTMLSTR, inplace = True, backup='.bak') as file:
            for line in file:
                line.replace(r"<strong>.*<\/strong>",BT2)




if __name__ == "__main__":
    main()
