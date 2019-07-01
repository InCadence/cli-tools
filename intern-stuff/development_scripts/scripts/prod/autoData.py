#!/usr/bin/env python

import os
import sys
import subprocess
import datetime

AUTO_DATA_LOC = "/opt/ion_file_uploads"
LOCK_FILE = os.path.join(AUTO_DATA_LOC,"/.lockfile")

MAX_LOCKFILE_AGE = subprocess.call("bc <<< \'60*60*3\'")

CHECK_SUM_FILE_CURRENT = "/tmp/ion_file_uploads_check_sums_current.txt"
CHECK_SUM_FILE_OLD = "/tmp/ion_file_uploads_check_sums_old.txt"

TWITTER_DUMP = (AUTO_DATA_LOC,"/raw_tweets")

#check if already running
LOCK_FILE = None
FILE_AGE = None
MAX_LOCKFILE_AGE = None
DATE = None
if(os.path.isfile(LOCK_FILE)):
    st = os.stat(LOCK_FILE)
    mtime = st.st_mtime

    if int(FILE_AGE) < int(MAX_LOCKFILE_AGE):
        exit(1)
    subprocess.call("rm LOCK_FILE", shell = True)
    else: 
        DATE = datetime.datetime.now
        print("lockfile created at ",DATE," ", LOCK_FILE)
    




