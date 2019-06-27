#! /usr/bin/env python
import os,subprocess,glob
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

BASE_DIR=Bash2Py(os.path.expanduser("~+"/+"I+"O+"N+"/+"i+"o+"n+"-+"s+"u+"i+"t+"e+"/+"m+"o+"d+"u+"l+"e+"s+"/))
DEST_DIR=Bash2Py(os.path.expanduser("~+"/+"I+"O+"N+"/+"i+"o+"n+"-+"s+"u+"i+"t+"e+"/+"t+"a+"r+"g+"e+"t+"/))
# blow away the old destination directory and everything in it
if (os.path.isdir(str(DEST_DIR.val)) ):
    subprocess.call(["rm","-rf",str(DEST_DIR.val)],shell=True)
_rc0 = subprocess.call(["mkdir",str(DEST_DIR.val)],shell=True)
_rc0 = subprocess.call(["find",Str(Glob(str(BASE_DIR.val)+"/*/build/libs")),"-name",Str(Glob("*.war")),"-exec","cp","--","{}",str(DEST_DIR.val),"\;"],shell=True)
