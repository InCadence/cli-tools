#! /usr/bin/env python
from __future__ import print_function
import sys,os
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

input=Bash2Py(sys.argv[1])
val=Bash2Py(os.popen("echo "+str(input.val)+" | cut -d \"/\" -f4").read().rstrip("\n"))
status=Bash2Py("looks good")
count=Bash2Py(0)
< $1while (json_line = Bash2Py(raw_input())):
    Make("count").setValue((count.val + 1))
    #echo $json_line | ${str:0:1}
    if (str(json_line.val:0:2) != "{\"" ):
        Make("status").setValue("ERROR @ line "+str(count.val))
        break < $1
print( "  %-60s %-10s\n" % (str(val.val), str(status.val)) )

