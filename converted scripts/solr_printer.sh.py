#! /usr/bin/env python
import sys,os,subprocess,glob
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

# this will print 10 dates from the exercise noted. need to 
# improve this, but it is a start
_rc0 = _rcr1, _rcw1 = os.pipe()
if os.fork():
    os.close(_rcw1)
    os.dup2(_rcr1, 0)
    _rcr2, _rcw2 = os.pipe()
    if os.fork():
        os.close(_rcw2)
        os.dup2(_rcr2, 0)
        _rcr3, _rcw3 = os.pipe()
        if os.fork():
            os.close(_rcw3)
            os.dup2(_rcr3, 0)
            _rcr4, _rcw4 = os.pipe()
            if os.fork():
                os.close(_rcw4)
                os.dup2(_rcr4, 0)
                _rcr5, _rcw5 = os.pipe()
                if os.fork():
                    os.close(_rcw5)
                    os.dup2(_rcr5, 0)
                    subprocess.call(["xargs","-I{}","bash","-c","echo $(date --date=@{} +%c)"],shell=True)
                else:
                    os.close(_rcr5)
                    os.dup2(_rcw5, 1)
                    subprocess.call(["cut","-d",",","-f1"],shell=True)
                    sys.exit(0)
                
            else:
                os.close(_rcr4)
                os.dup2(_rcw4, 1)
                subprocess.call(["cut","-d",":","-f2"],shell=True)
                sys.exit(0)
            
        else:
            os.close(_rcr3)
            os.dup2(_rcw3, 1)
            subprocess.call(["grep","\":"],shell=True)
            sys.exit(0)
        
    else:
        os.close(_rcr2)
        os.dup2(_rcw2, 1)
        subprocess.call(["grep","publishtime"],shell=True)
        sys.exit(0)
    
else:
    os.close(_rcr1)
    os.dup2(_rcw1, 1)
    subprocess.call(["curl","-u","ion:ionuser",Str(Glob("http://localhost:8081/solr/exercises/select?q=exercise%3A75TH-RSTB-IA-18"))],shell=True)
    sys.exit(0)

