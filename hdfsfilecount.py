#!/usr/bin/env python
''' Function to get the filecounts of hdfs using hadoop shell commands'''

from subprocess import Popen,PIPE
def get_file_counts_hdfs_day(hdfspath):
  phadoopcount = Popen(["hadoop","fs","-count","/shared/app_logs"],stdout=PIPE)
  countoutput=phadoopcount.communicate()[0]
  filecount=countoutput.split()[1]
  return filecount
  
