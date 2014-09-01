#!/usr/bin/env python

def find_dups(strlist):
  normalset = set()
  dupsset = set()
  for number in strlist:
    if number in normalset:
      dupsset.add(number)
    else:
      normalset.add(number)
  return dupsset

if __name__=="__main__":
  strlist = [1,2,3,5,3,5,6,7,7]
  dupset = find_dups(strlist)
  for numbers in dupset:
    print numbers
  
