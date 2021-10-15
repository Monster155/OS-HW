#!/usr/bin/python3

#Davletshin Damir 11-902

import os
import sys
import random
import subprocess

n = int(sys.argv[1]) 
for i in range(1, n + 1):
  child = os.fork()
  if child <= 0:
    r = random.randint(5, 10)
    subprocess.call(['./child.py', str(r)])
  else:
    parent = os.wait()
    print('Child process with PID {pid} ended. End status is {exitstatus}'.format(pid=parent[0], exitstatus=parent[1]))
