#coding=utf-8

from threading import Thread
import time
import os

def music(name):
    print time.localtime()
    time.sleep(2)
    print name

def movie(name):
    print time.localtime()
    time.sleep(5)
    print name


if __name__ == '__main__':
    t1 = Thread(target=music, args=('body',))
    t1.setDaemon(True)       # 设置守护,如果没设置,那么主线程结束会有其他线程来接受子线程继续执行下去
    t1.start()
    t2 = Thread(target=movie, args=('xiha',))
    t2.setDaemon(True)
    t2.start()

    
    


    # t1.join()
    # t2.join()

    print os.getpid()
    print time.localtime()