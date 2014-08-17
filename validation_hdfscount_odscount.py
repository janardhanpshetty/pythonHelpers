#!/usr/bin/env python
''' Function to validate the counts of hdfs and ods tables
  1. get_counts_hdfs_day(hdfspath):
  2. getchangeddate(givendate,givenformat,requiredformat):
  3. get_counts_ods_day(tablename):
  4. compare(hdfs_count,ods_count):
'''

import sys
import datetime
from subprocess import Popen,PIPE

def getchangeddate(givendate,givenformat,requiredformat):
  chdate = datetime.datetime.strptime(givendate,givenformat)
  reqdateformat=chdate.strftime(requiredformat)
  return reqdateformat

def get_counts_hdfs_day(hdfspath):
    phadoopcat = Popen(["hadoop","fs","-cat",hdfspath],stdout=PIPE)
    linecount = Popen(["wc","-l"],stdin=phadoopcat.stdout,stdout=PIPE)
    count_hdfs = linecount.communicate()[0]
    return count_hdfs

def get_counts_ods_day(sqlCommand,connectstring):
  session = Popen(["sqlplus","-s",connectstring],stdin=PIPE, stdout=PIPE, stderr=PIPE)
  session.stdin.write(sqlCommand)
  count_ods=session.communicate()[0]
  return count_ods

if __name__=='__main__':
  dategiven=sys.argv[1]
  formatgiven='%Y%m%d'
  reqformat='%Y/%m/%d'
  changed_date_format=getchangeddate(dategiven,formatgiven,reqformat)
  print 'changed_date= %s'%changed_date_format
  hdfspath='/shared/CFL/EWS/Log_A_User_Metrics/%s/part*'%changed_date_format
  print 'The hdfs path is %s'%hdfspath
  count_hdfs_day=int(get_counts_hdfs_day(hdfspath))
  print 'Count from HDFS is %d'%count_hdfs_day
  if count_hdfs_day == 0:
    print 'ERROR:HDFS file is not present for validation'
    sys.exit(1)
  sqlcommand="set feed off \n set pages 0 \n select count(1) from ODS_S.ODS_LOG_USER_METRICS where log_date=to_date('%s','YYYY/MM/DD');"%changed_date_format
  connectstring="/@ods_ops_s"
  count_ods_day=int(get_counts_ods_day(sqlcommand,connectstring))
  print 'Count from ODS is %d'%count_ods_day
  if count_hdfs_day == count_ods_day:
    print 'Both counts same'
  else:
    print 'Both counts are different'
    sys.exit(1)
                 