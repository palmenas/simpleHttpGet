#!/usr/bin/env python

import os
import time
import datetime
import requests
i=0

while (1):
  i+=1
  d = datetime.datetime.now()
  f = open('results.txt', 'a')
  print "Attempt:", i
  try:
    r = requests.get('https://www.google.com', timeout=10)
    f.write("Date: "+d.strftime('%x %X')+" Ret Code: "+str(r.status_code)+" Headers:"+str(r.headers)+" URL: "+str(r.url)+"\n")
  except requests.exceptions.Timeout:
    f.write("Date: "+d.strftime('%x %X')+" Msg: Timeout\n")
  except requests.exceptions.HTTPError:
    f.write("Date: "+d.strftime('%x %X')+" Msg: Error\n")
  f.close()
  time.sleep(120)
