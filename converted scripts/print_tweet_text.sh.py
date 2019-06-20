#! /usr/bin/env python
from __future__ import print_function
import sys,os,subprocess,glob
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value

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

# This is a simple script for digging though the massive twitter
# files and printing something useful out of them. To use this
# run the script and pass in directory of tweets to search and
# a field name to search on. The script will then pull out the
# values associated with that key. This is a quick way of finding
# all of the authors or all of the text values from 10,000 tweets.
# must supply a dir name to clean
if (str(sys.argv[1]) == '' ):
    print("ERROR! Must supply a dir name")
    exit(1)
if (str(sys.argv[2]) == '' ):
    print("ERROR! Must supply a field to search")
    exit(1)
ION_PATH=Bash2Py("/opt/ion_local_data")
EXERCISE=Bash2Py(sys.argv[1])
COL_NAME=Bash2Py(sys.argv[2])
# should be something like '"created_at":"'
os.chdir(str(EXERCISE.val))
_rc0 = _rcr1, _rcw1 = os.pipe()
if os.fork():
    os.close(_rcw1)
    os.dup2(_rcr1, 0)
    _rcr2, _rcw2 = os.pipe()
    if os.fork():
        os.close(_rcw2)
        os.dup2(_rcr2, 0)
        subprocess.call(["grep",str(COL_NAME.val)],shell=True)
    else:
        os.close(_rcr2)
        os.dup2(_rcw2, 1)
        subprocess.call(["awk","-v","k=text","{n=split($0,a,\",\"); for (i=1; i<=n; i++) print a[i]}"],shell=True)
        sys.exit(0)
    
else:
    os.close(_rcr1)
    os.dup2(_rcw1, 1)
    subprocess.call(["sed","-e","s/[{}]//g",Str(Glob("*.json"))],shell=True)
    sys.exit(0)

