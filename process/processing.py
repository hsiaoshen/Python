#coding=utf-8

# pyhton中使用multiprocessing模块生成进程
# 利用Queue(消息队列)和Pipe(管道)进行通信

import multiprocessing
from time import ctime,sleep
import os
from  multiprocessing import Queue,Pipe

def worker(interval,q):
    print q.get()
    print 'this time is {}'.format(ctime())
    n = 5
    while n > 0:
        print 'this worker pid is-->',os.getppid()
        sleep(interval)
        n -= 1

def teacher(interval,q):
    q.put(['11','adada'])
    print 'this time is {}'.format(ctime())
    n = 5
    while n > 0:
        print 'this teacher pid is-->',os.getppid()
        sleep(interval)
        n -= 1

if  __name__ == '__main__':
    q = Queue()
    wk = multiprocessing.Process(name = worker, target =  worker, args=(2,q))
    wk.start() 
    th = multiprocessing.Process(name = teacher, target =  teacher, args=(3,q))
    th.start()


    wk.join()
    th.join()       
