#! /usr/bin/env python
from __future__ import print_function
import sys,os,subprocess,glob
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value

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

def Array(value):
  if isinstance(value, list):
    return value
  if isinstance(value, basestring):
    return value.strip().split(' ')
  return [ value ]

def Glob(value):
  ret = glob.glob(value)
  if (len(ret) < 1):
    ret = [ value ]
  return ret

###############################################
# Simple script for generating documentation.
# Run this with no args and it will run
# javadoc on the modules listed below and
# dump the generated files into the
# ion-suite/docs directory.
###############################################
# grab the location of the script
bin_loc=Bash2Py(os.popen("dirname ""+__file__+""").read().rstrip("\n"))
bin_loc=Bash2Py(os.popen("(cd ""+str(bin_loc.val)+"" && pwd)").read().rstrip("\n"))
# set the module and output directories
modules_loc=Bash2Py(str(bin_loc.val)+"/../../modules")
output_loc=Bash2Py(str(bin_loc.val)+"/../../docs/dev")
_rc0 = subprocess.call(["mkdir","-p",str(output_loc.val)],shell=True)
# modules to build
BUILD_DIRS=Bash2Py("(common-utilities facebook gmail hdfs-utils ion-bender ion-bender-webapp ion-browser ion-logging ion-profiles ion-publisher-webapp ion-twitter-harvester ion-twitter-server ion-web-utilities logging twitter-core youtube-webapp)")
# make sure we delete the old docs
if (os.path.isdir(str(output_loc.val)) ):
    subprocess.call(["rm","-rf",str(output_loc.val)],shell=True)
_rc0 = subprocess.call(["mkdir",str(output_loc.val)],shell=True)
# Build each package
os.chdir(str(modules_loc.val))
for Make("repo").val in Array(BUILD_DIRS.val[@] ]):
    os.chdir(str(repo.val))
    print("=================================================")
    print("GENERATING JAVA DOCUMENTATION: "+str(repo.val))
    print("=================================================")
    # make sure we delete the old docs
    if (os.path.isdir(str(output_loc.val)+"/"+str(repo.val)) ):
        subprocess.call(["rm","-rf",str(output_loc.val)+"/"+str(repo.val)],shell=True)
    subprocess.call(["mkdir",str(output_loc.val)+"/"+str(repo.val)],shell=True)
    # find all the java files in the main/src tree and generate docs from them
    _rcr5, _rcw5 = os.pipe()
    if os.fork():
        os.close(_rcw5)
        os.dup2(_rcr5, 0)
        subprocess.call(["xargs","javadoc","-d",str(output_loc.val)+"/"+str(repo.val)],shell=True)
    else:
        os.close(_rcr5)
        os.dup2(_rcw5, 1)
        subprocess.call(["find","src/main","-type","f","-name",Str(Glob("*.java"))],shell=True)
        sys.exit(0)
    
    print()
    print()
    os.chdir("../")
