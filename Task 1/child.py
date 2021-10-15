#!/usr/bin/python3

#Davletshin Damir 11-902

import os
import sys
import time
import random

print('Child programm is running in process with PID {pid} witharg {arg}'.format(pid=os.getpid(), arg=sys.argv[1]))
time.sleep(sys.argv[1])
print('Process with PID {pid} ended'.format(pid=os.getpid()))
os._exit(random.randint(0, 1))
