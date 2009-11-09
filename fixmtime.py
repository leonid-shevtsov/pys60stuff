# A script to fix modification times on files modified with obexfs
import os
import time
import re

for root, dirs, files in os.walk("E:\\"):
  for filename in files:
    if (re.search('\.py$',filename)!=None) and (os.stat(root + '\\' + filename).st_mtime==-1.0):
      print "fixed time on %s\\%s" % (root, filename)
      os.utime(root + '\\' + filename,(time.time(), time.time()))

