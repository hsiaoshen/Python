#coding=utf-8


# 同步互斥机制:Lock锁
from threading import Lock,Thread
import time

a = 1

def fun1():
    lock.acquire()
    global a
    a = 10 
    time.sleep(1) 
    print 'fun1',a
    lock.release()
    

def fun2():
    lock.acquire()
    global a
    a = 100
    print 'fun2',a
    lock.release() 

lock = Lock()

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()

t1.join()
t2.join()