#!/usr/bin/env python

def match_pairs(males,females):
  pairset = set()
  while len(males):
    pairset.add((males.pop(),females.pop()))
  return pairset
 
if __name__=="__main__":
  males=set(('sam','rick','ravi','tejas','peter'))
  females=set(('rinky','savi','mady','susan','samtha'))
  if len(males) == len(females):
   pairset = set(match_pairs(males,females))
  else:
    print "Check males and females set for equality"
  print pairset 
