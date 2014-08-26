#!/usr/bin/env python
import sys
from subprocess import Popen,PIPE
def emit_corrupt_files(hdfs_corrupt_dir,log_file):
    hdfs_list = Popen(["hadoop","fs","-ls","-R",hdfs_corrupt_dir],stdout=PIPE)
    full_path = Popen(["awk", "{print $8}"],stdin=hdfs_list.stdout,stdout=PIPE)
    corrupt_filenames = Popen(["awk","-F","/","{print $10}"],stdin=full_path.stdout,stdout=PIPE)
    corrupt_file_list = corrupt_filenames.communicate()[0]
    log_file.write(corrupt_file_list)


if __name__=='__main__':
  CORRUPT_DIR = "/shared/app_logs/corrupt/2014/05/06"
  output_file = "/home/jshetty/python/test_log"
  output_file = open(output_file,'w')
  emit_corrupt_files(CORRUPT_DIR,output_file)
  output_file.close()

