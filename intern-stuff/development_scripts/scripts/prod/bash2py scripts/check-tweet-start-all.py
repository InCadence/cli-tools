#! /usr/bin/env python
from __future__ import print_function
import subprocess,glob
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

print( "\t\t----------------------------------\n" )

print( "\t\tVALIDATING THE START OF EACH TWEET\n" )

print( "\t\t----------------------------------\n\n" )

print( "  %-60s %-10s\n" % ("EXERCISE", "STATUS") )

print( "==============================================================================\n" )

_rc0 = subprocess.call(["find",Str(Glob("/opt/ion_local_data/*")),"-name","addedTweets.json","-exec","check-tweet-start","{}","\;"],shell=True)
