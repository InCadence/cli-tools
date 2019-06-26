#!/usr/bin/env python

#root check
import os
import subprocess

if os.geteuid()==0:
    print("running as root")
else:
    sys.exit("this script must be run as root")

basePath = "/opt/glassfish4/glassfish/domains/ion/applications"

browserPath = 

bannerFileStr= "css/banner.css"
bannerFile= str(basePath)+"/"+str(browserPath)+"/"+str(bannerFileStr)

indexFileStr = "index.html"
indexFile =  str(basePath)+"/"+str(browserPath)+"/"+str(indexFileStr)

htmlFilesLoc = str(basePath)+"/"+str(browserPath)

newColor=""
bannerText = ""

#####################################
# select the banner color
#####################################
def select_color():
    number =""
    while True:
        print("Select a new banner color\n\n 1 - green\n 2 - red\n 3 - blue\n 4-yellow\n 5 - orange\n 6 - gray")
        number = input()
        
        if number < 1 or number > 6:
            print("Please enter a valid selection")
        else:
            break
    if number == 1:
        newColor = "green"
    else if number == 2:
        newColor = "red"
    else if number == 3:
        newColor = "blue"
    else if number == 4:
        newColor = "yellow"
    else if number == 5:
        newColor = "orange"
    else: 
        newColor = "gray"

    

#####################################
# enter the banner text
#####################################
def enter_text():
    print("Enter the banner text")
    bannerText = input()

#####################################
# confirm changes
#####################################

def confirm_changes():
    print("NEW BANNER COLOR: ", newColor)
    print("NEW BANNER TEXT: ", bannerText)

    print("Write changes to ION?")
    
    while True:
        choice = input("[y]es or [q]uit")
        if choice != "y" or choice != "q":
            print("Please choose [y]es or [q]uit!")
        else:
            break

def write_changes():
    print("\n\n writing changes")
    bs1 = subprocess.call(["sed","-i","s/background-color:.*/background-color: "+str(newColor.val)+";/",str(bannerFile.val)],shell=True)
    SearchStr="\<span class\=security_banner\>"
    bannerText = os.popen("echo \""+str(bannerText.val)+"\" | sed \"s/\\//\\\\\\//g\"").read().rstrip("\n")
    if (int(os.popen("grep -c \""+str(searchStr.val)+"\" \""+str(indexFile.val)+"\"").read().rstrip("\n")) >= 1 ):
        subprocess.call(["sed","-i","s/<span class=security_banner>.*<\/span>/<span class=security_banner>"+str(bannerText.val)+"<\/span>/",Str(Glob(str(htmlFilesLoc.val)+"/*.html"))],shell=True)
    else:
        subprocess.call(["sed","-i","s/<strong>.*<\/strong>/<strong><span class=security_banner>"+str(bannerText.val)+"<\/span><\/strong>/",Str(Glob(str(htmlFilesLoc.val)+"/*.html"))],shell=True)

#####################################
# run everything
#####################################
select_color()
enter_text()
confirm_changes()
write_changes()
