#! /usr/bin/env python
from __future__ import print_function
import os,subprocess,glob,re
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value
  def setValue(self, value=None):
    self.val = value
    return value

def GetVariable(name, local=locals()):
  if name in local:
    return local[name]
  if name in globals():
    return globals()[name]
  return None

def Make(name, local=locals()):
  ret = GetVariable(name, local)
  if ret is None:
    ret = Bash2Py(0)
    globals()[name] = ret
  return ret

def Str(value):
  if isinstance(value, list):
    return " ".join(value)
  if isinstance(value, basestring):
    return value
  return str(value)

def Glob(value):
  ret = glob.glob(value)
  if (len(ret) < 1):
    ret = [ value ]
  return ret

#######################################################################################
#  Author: James Stoup
#
#  Script for changing the color and text of the security banners
# 
#  This script changes the color of the security banner located here:
#
#  /opt/glassfish4/glassfish/domains/ion/applications/ion-browser-<version>/css/banner.css
# 
#  The text for the banner will also get changed in every HTML file that has a banner.
#  Those files can be found here:
#  
#  /opt/glassfish4/glassfish/domains/ion/applications/ion-browser-<version>
#
#  As a side note, if this suddenly stops working then the version probably changed
#  and we need to update this script.
#######################################################################################
# root check
if (int(EUID.val) != 0 ):
    print("Please run as root")
    exit()
BASE_PATH=Bash2Py("/opt/glassfish4/glassfish/domains/ion/applications")
BROWSER_PATH=Bash2Py(os.popen("find "+str(BASE_PATH.val)+" -name oetscmanage.html | rev | cut -d \"/\" -f 2 | rev | head -1").read().rstrip("\n"))
if (str(BROWSER_PATH.val) == '' ):
    print("ION is not installed. Please check that the war files are installed properly")
    exit(1)
BANNER_FILE_STR=Bash2Py("css/banner.css")
BANNER_FILE=Bash2Py(str(BASE_PATH.val)+"/"+str(BROWSER_PATH.val)+"/"+str(BANNER_FILE_STR.val))
INDEX_FILE_STR=Bash2Py("index.html")
INDEX_FILE=Bash2Py(str(BASE_PATH.val)+"/"+str(BROWSER_PATH.val)+"/"+str(INDEX_FILE_STR.val))
HTML_FILES_LOC=Bash2Py(str(BASE_PATH.val)+"/"+str(BROWSER_PATH.val))
NEW_COLOR=Bash2Py("green")
BANNER_TEXT=Bash2Py()
#####################################
# Check to see if we should quit
#####################################
def check_exit (_p1) :
    if (str(_p1) == "q" ):
        print()
        print()
        print("Quitting without saving changes")
        print()
        exit(1)

#####################################
# print instructions for color
#####################################
def color_usage () :
    subprocess.Popen("cat",shell=True,stdin=subprocess.PIPE)
    _rc0.communicate("Select a new banner color\n\n  1 - green\n  2 - red\n  3 - blue\n  4 - yellow\n  5 - orange\n  6 - gray\n")
    _rc0 = _rc0.wait()print '''
    Select a new banner color
    
      1 - green
      2 - red
      3 - blue
      4 - yellow
      5 - orange
      6 - gray
'''

#####################################
# print instructions for banner text
#####################################
def text_usage () :
    subprocess.Popen("cat",shell=True,stdin=subprocess.PIPE)
    _rc0.communicate("\nEnter the banner text\n")
    _rc0 = _rc0.wait()print '''
    
    Enter the banner text
'''

#####################################
# select the banner color
#####################################
def select_color () :
    global number
    global NEW_COLOR

    color_usage()
    number=Bash2Py()
    while (True):
        number = Bash2Py(raw_input())
        if (re.search(Str(Glob("^[123456]{1}"+"$")),str(number.val)) ):
            break
        else:
            print("Please enter a valid selection!")
            color_usage()
    
    if ( str(number.val) == '1'):
        Make("NEW_COLOR").setValue("green")
    elif ( str(number.val) == '2'):
        Make("NEW_COLOR").setValue("red")
    elif ( str(number.val) == '3'):
        Make("NEW_COLOR").setValue("blue")
    elif ( str(number.val) == '4'):
        Make("NEW_COLOR").setValue("yellow")
    elif ( str(number.val) == '5'):
        Make("NEW_COLOR").setValue("orange")
    elif ( str(number.val) == '6'):
        Make("NEW_COLOR").setValue("gray")

#####################################
# enter the banner text
#####################################
def enter_text () :
    text_usage()
    BANNER_TEXT = Bash2Py(raw_input())

#####################################
# confirm changes
#####################################
def confirm_changes () :
    global NEW_COLOR
    global BANNER_TEXT
    global REPLY

    print()
    print("NEW BANNER COLOR : "+str(NEW_COLOR.val))
    print("NEW BANNER TEXT  : "+str(BANNER_TEXT.val))
    print()
    print("Write changes to ION?")
    REPLY=Bash2Py()
    while (if print("choose [y]es | [q]uit ",end="")
    raw_input():
        str(REPLY.val) != Str(Glob("[ynq]"))):
        
        else:
            print("\nPlease enter y or q!")
    check_exit(REPLY.val)

#####################################
# write changes to the files
#####################################
def write_changes () :
    global NEW_COLOR
    global BANNER_FILE
    global SEARCH_STR
    global BANNER_TEXT
    global INDEX_FILE
    global HTML_FILES_LOC

    print()
    print()
    print("writing changes")
    # change the background color
    _rc0 = subprocess.call(["sed","-i","s/background-color:.*/background-color: "+str(NEW_COLOR.val)+";/",str(BANNER_FILE.val)],shell=True)
    # change the banner text
    SEARCH_STR=Bash2Py("\<span class\=security_banner\>")
    BANNER_TEXT=Bash2Py(os.popen("echo \""+str(BANNER_TEXT.val)+"\" | sed \"s/\\//\\\\\\//g\"").read().rstrip("\n"))
    if (int(os.popen("grep -c \""+str(SEARCH_STR.val)+"\" \""+str(INDEX_FILE.val)+"\"").read().rstrip("\n")) >= 1 ):
        subprocess.call(["sed","-i","s/<span class=security_banner>.*<\/span>/<span class=security_banner>"+str(BANNER_TEXT.val)+"<\/span>/",Str(Glob(str(HTML_FILES_LOC.val)+"/*.html"))],shell=True)
    else:
        subprocess.call(["sed","-i","s/<strong>.*<\/strong>/<strong><span class=security_banner>"+str(BANNER_TEXT.val)+"<\/span><\/strong>/",Str(Glob(str(HTML_FILES_LOC.val)+"/*.html"))],shell=True)

#####################################
# run everything
#####################################
select_color()
enter_text()
confirm_changes()
write_changes()
