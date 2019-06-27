#! /usr/bin/env python
from __future__ import print_function
import subprocess
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

def Array(value):
  if isinstance(value, list):
    return value
  if isinstance(value, basestring):
    return value.strip().split(' ')
  return [ value ]

EXERCISE_FILE=Bash2Py("/tmp/exercises.txt")
EXERCISE_LIST_FILE=Bash2Py("/tmp/exercise-list.txt")
_rc0 = subprocess.Popen("su" + " " + "postgres",shell=True,stdin=subprocess.PIPE)
_rc0.communicate("cd /tmp\npsql -c \"copy (select ex_name from exercisemanager order by ex_name) to $EXERCISE_FILE\" ion | tail -n +3 | head -n -2 \npsql -c \"copy (select distinct exercisename from exercisearticle order by exercisename) to $EXERCISE_LIST_FILE\" ion | tail -n +3 | head -n -2\n")
_rc0 = _rc0.wait()print '''
cd /tmp
psql -c "copy (select ex_name from exercisemanager order by ex_name) to '$EXERCISE_FILE'" ion | tail -n +3 | head -n -2 
psql -c "copy (select distinct exercisename from exercisearticle order by exercisename) to '$EXERCISE_LIST_FILE'" ion | tail -n +3 | head -n -2
'''
< "$EXERCISE_LIST_FILE"while (if not Make("IFS").setValue():
    str(articleexercise.val) != ''):
    < "$EXERCISE_FILE"while (if not Make("IFS2").setValue():
        str(exercise.val) != ''):
        if (str(exercise.val) == str(articleexercise.val) ):
            Make("match").setValue("true")
            break < "$EXERCISE_FILE"
    if (str(match.val) != '' ):
        print("Match found for "+str(articleexercise.val))
    else:
        print("NO MATCH FOUND FOR "+str(articleexercise.val))
        Make("CLEANUP").setValue("("+str(articleexercise.val)+")")
    Make("match").setValue("false") < "$EXERCISE_LIST_FILE"
for Make("ex").val in Array(CLEANUP.val[@] ]):
    print()
    print("DELETEING "+str(ex.val)+" FROM EXERCISE ARTICLE TABLE")
    subprocess.Popen("su" + " " + "postgres",shell=True,stdin=subprocess.PIPE)
    _rc0.communicate("    cd /tmp\n    psql -c \"delete from exercisearticle where exercisename = $ex\" ion\n")
    _rc0 = _rc0.wait()print '''
        cd /tmp
        psql -c "delete from exercisearticle where exercisename = '$ex'" ion
'''
    print()
#Finally delete the files
_rc0 = subprocess.call(["rm","-f",str(EXERCISE_FILE.val)],shell=True)
_rc0 = subprocess.call(["rm","-f",str(EXERCISE_LIST_FILE.val)],shell=True)
exit(1)
