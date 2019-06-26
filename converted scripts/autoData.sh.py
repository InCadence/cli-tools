#! /usr/bin/env python
from __future__ import print_function
import os,subprocess
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

# auto deployment of data loaded into key directories
# does the following:
#  - checks every 10 seconds to see if a new file exists in ion_auto_data
#  - if a new file is found, check to see if it is done copying over
#  - make sure another instance of this script isn't running while this one is running
# place to copy auto deployment of data files
AUTO_DATA_LOC=Bash2Py("/opt/ion_file_uploads")
LOCK_FILE=Bash2Py(str(AUTO_DATA_LOC.val)+"/.lockfile")
# max age in seconds (in this case 3 hours)
MAX_LOCKFILE_AGE=Bash2Py(os.popen("bc <<< \"60*60*3\"").read().rstrip("\n"))
# check sum location
CHECK_SUM_FILE_CURRENT=Bash2Py("/tmp/ion_file_uploads_check_sums_current.txt")
CHECK_SUM_FILE_OLD=Bash2Py("/tmp/ion_file_uploads_check_sums_old.txt")
# location of specific dump points
TWITTER_DUMP=Bash2Py(str(AUTO_DATA_LOC.val)+"/raw_tweets")
# need to make sure we don't start this in the middle of already running it
def checkIfAlreadyRunning () :
    global LOCK_FILE
    global FILE_AGE
    global MAX_LOCKFILE_AGE
    global DATE

    # let's see if there is a previous lockfile
    if (os.path.isfile(str(LOCK_FILE.val)) ):
        # file age in seconds = current_time - file_modification_time.
        Make("FILE_AGE").setValue((os.popen("date +%s").read().rstrip("\n") - os.popen("stat -c \"%Y\" \""+str(LOCK_FILE.val)+"\"").read().rstrip("\n")))
        # so we found a previous lockfile, let's see how old it is
        if int(FILE_AGE.val) < int(MAX_LOCKFILE_AGE.val):
            # if it is less than MAX_LOCKFILE_AGE old then we should wait
            # the logic here being that it is possible a large copy command
            # is being executed and we don't want to interrupt that
            
                exit(1)
        
        # if we have gotten here then that means the previous attempt at running this
        # crashed due to reasons unknown and never deleted the lock file. so let's
        # clean that old file up and try this again.
        subprocess.call(["rm",str(LOCK_FILE.val)],shell=True)
    else:
        # if no lock file has been found, go ahead and create one
        # then once this script ends we can remove it
        Make("DATE").setValue(os.popen("date").read().rstrip("\n"))
        print("lockfile created at "+str(DATE.val),file=file(str(LOCK_FILE.val),'wb'))> $LOCK_FILE

# check to ensure all the directories are there
