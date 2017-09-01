#coding=utf-8

# 进程

import os
import time

pid = os.fork()

if pid < 0:
    print 'create process failed'

elif pid == 0:
    time.sleep(2)
    print 'this is child process:',os.getpid()
    print os.getppid()
else:
    
    print 'parent process:',os.getpid()
    print pid


print '*************fork*********************'